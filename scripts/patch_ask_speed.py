#!/usr/bin/env python3
"""Speed up Ask: L3 fast model, truncate to 600 chars, B=64."""

import sys

changes = []

def apply(path, old, new, label):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    count = c.count(old)
    if count != 1:
        print(f'  FAIL ({count} occurrences) [{path}]: {label}')
        sys.exit(1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c.replace(old, new, 1))
    changes.append(f'[{path}] {label}')
    print(f'  OK: {label}')

# ── 1. semantic-worker.js: add Light model + tighten truncation ──────────────
apply(
    'beta/js/semantic-worker.js',
    'const MODELS = {\n'
    '  en: \'Xenova/all-MiniLM-L6-v2\',\n'
    '  multi: \'Xenova/paraphrase-multilingual-MiniLM-L12-v2\',\n'
    '};',
    'const MODELS = {\n'
    '  fast: \'Xenova/all-MiniLM-L3-v2\',\n'
    '  en: \'Xenova/all-MiniLM-L6-v2\',\n'
    '  multi: \'Xenova/paraphrase-multilingual-MiniLM-L12-v2\',\n'
    '};',
    'worker: add fast (L3) model'
)
apply(
    'beta/js/semantic-worker.js',
    ".map((s) => String(s == null ? '' : s).slice(0, 4000));",
    # 600 chars ≈ 150 tokens — well within the 256-token model limit,
    # captures plenty of context, cuts tokenisation time for long notes.
    ".map((s) => String(s == null ? '' : s).slice(0, 600));",
    'worker: truncation 4000 → 600 chars'
)

# ── 2. beta/index.html ───────────────────────────────────────────────────────

# 2a. Add fast model i18n keys (English block, before ask_model_en_name)
apply(
    'beta/index.html',
    'ask_model_en_name:"English",ask_model_en_desc:"Best for notes written in English. Smaller, faster download.",',
    'ask_model_fast_name:"Light (fastest)",ask_model_fast_desc:"3-layer model — about 2× faster than English and half the download. Perfect for large libraries.",ask_model_en_name:"English",ask_model_en_desc:"Standard accuracy for notes written in English.",',
    'i18n: add fast model keys'
)

# 2b. ASK_MODELS: add fast
apply(
    'beta/index.html',
    'var ASK_MODELS = { en:23, multi:50 };',
    'var ASK_MODELS = { fast:11, en:23, multi:50 };',
    'ASK_MODELS: add fast:11'
)

# 2c. Model picker: 3 options
apply(
    'beta/index.html',
    "[['en',t('ask_model_en_name'),t('ask_model_en_desc')],['multi',t('ask_model_multi_name'),t('ask_model_multi_desc')]].forEach(function(m){",
    "[['fast',t('ask_model_fast_name'),t('ask_model_fast_desc')],['en',t('ask_model_en_name'),t('ask_model_en_desc')],['multi',t('ask_model_multi_name'),t('ask_model_multi_desc')]].forEach(function(m){",
    'model picker: add fast option'
)

# 2d. Batch size 48 → 64
apply(
    'beta/index.html',
    'var B=48, i=0;',
    'var B=64, i=0;',
    'batch size 48 → 64'
)

# 2e. Keep _B in sync
apply(
    'beta/index.html',
    'ASK._buildStart=Date.now(); ASK._snap=null; ASK._rates=[]; ASK._B=48;',
    'ASK._buildStart=Date.now(); ASK._snap=null; ASK._rates=[]; ASK._B=64;',
    '_B 48 → 64'
)

# ── 3. tests/11_semantic_search.js ───────────────────────────────────────────

# 3a. Add L3 model worker check
apply(
    'tests/11_semantic_search.js',
    "['English model wired', /Xenova\\/all-MiniLM-L6-v2/],",
    "['Light (L3) model wired', /Xenova\\/all-MiniLM-L3-v2/],\n"
    "  ['English model wired', /Xenova\\/all-MiniLM-L6-v2/],",
    'test: L3 model check'
)

# 3b. Update ASK_MODELS assertion
apply(
    'tests/11_semantic_search.js',
    "['both model sizes offered', /ASK_MODELS\\s*=\\s*\\{\\s*en:\\s*23,\\s*multi:\\s*50\\s*\\}/],",
    "['all three model sizes offered', /ASK_MODELS\\s*=\\s*\\{\\s*fast:\\s*11,\\s*en:\\s*23,\\s*multi:\\s*50\\s*\\}/],",
    'test: ASK_MODELS pattern'
)

# 3c. Add fast model i18n keys
apply(
    'tests/11_semantic_search.js',
    "'ask_model_en_name', 'ask_model_en_desc',",
    "'ask_model_fast_name', 'ask_model_fast_desc', 'ask_model_en_name', 'ask_model_en_desc',",
    'test: fast model i18n keys'
)

print(f'\nAll {len(changes)} changes applied.')
