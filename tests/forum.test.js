import { describe, it, expect, beforeAll } from 'vitest';
import { loadForumUtils } from './helpers/loadForum.js';

let ago, aColor, esc, catLabel, catCls;

beforeAll(() => {
  ({ ago, aColor, esc, catLabel, catCls } = loadForumUtils());
});

// ── Helpers ───────────────────────────────────────────────────────────────────

/** ISO timestamp N minutes in the past. */
const minutesAgo = (n) => new Date(Date.now() - n * 60_000).toISOString();

/** The 8 valid avatar colours defined in forum.js. */
const AVATAR_COLOURS = [
  '#f97316', '#60a5fa', '#22c55e', '#a78bfa',
  '#f472b6', '#fb923c', '#34d399', '#38bdf8',
];

// ── esc — HTML escaping ────────────────────────────────────────────────────────

describe('esc (HTML escaping)', () => {
  it('leaves plain text unchanged', () => {
    expect(esc('hello world')).toBe('hello world');
  });

  it('escapes ampersands', () => {
    expect(esc('A & B')).toBe('A &amp; B');
  });

  it('escapes angle brackets', () => {
    expect(esc('<script>')).toBe('&lt;script&gt;');
  });

  it('escapes double quotes', () => {
    expect(esc('"quoted"')).toBe('&quot;quoted&quot;');
  });

  it('handles all four special characters together', () => {
    expect(esc('<a href="x&y">')).toBe('&lt;a href=&quot;x&amp;y&quot;&gt;');
  });

  it('returns empty string for null', () => {
    expect(esc(null)).toBe('');
  });

  it('returns empty string for undefined', () => {
    expect(esc(undefined)).toBe('');
  });

  it('coerces numbers to strings', () => {
    expect(esc(42)).toBe('42');
  });
});

// ── ago — relative timestamp ──────────────────────────────────────────────────

describe('ago (relative timestamp)', () => {
  it('returns "just now" for timestamps less than 1 minute ago', () => {
    expect(ago(minutesAgo(0.4))).toBe('just now');
  });

  it('returns "Xm ago" for timestamps in the past hour', () => {
    expect(ago(minutesAgo(5))).toBe('5m ago');
    expect(ago(minutesAgo(45))).toBe('45m ago');
  });

  it('returns "1m ago" at exactly the 1-minute boundary', () => {
    expect(ago(minutesAgo(1.1))).toBe('1m ago');
  });

  it('returns "Xh ago" for timestamps between 1 and 24 hours ago', () => {
    expect(ago(minutesAgo(60))).toBe('1h ago');
    expect(ago(minutesAgo(120))).toBe('2h ago');
    expect(ago(minutesAgo(23 * 60))).toBe('23h ago');
  });

  it('returns "Xd ago" for timestamps between 1 and 6 days ago', () => {
    expect(ago(minutesAgo(24 * 60))).toBe('1d ago');
    expect(ago(minutesAgo(3 * 24 * 60))).toBe('3d ago');
    expect(ago(minutesAgo(6 * 24 * 60))).toBe('6d ago');
  });

  it('returns a locale date string for timestamps 7+ days ago', () => {
    const result = ago(minutesAgo(8 * 24 * 60));
    // Should be a date like "1/1/2024" or "2024-01-01" — not an "ago" string
    expect(result).not.toContain('ago');
    expect(result).toMatch(/\d/);   // contains at least one digit
  });
});

// ── aColor — avatar colour hash ───────────────────────────────────────────────

describe('aColor (avatar colour hash)', () => {
  it('returns one of the 8 expected hex colours', () => {
    expect(AVATAR_COLOURS).toContain(aColor('Alice'));
  });

  it('is deterministic — same input always returns the same colour', () => {
    const names = ['Alice', 'Bob', 'Charlie', 'JW Sync User'];
    for (const name of names) {
      expect(aColor(name)).toBe(aColor(name));
    }
  });

  it('handles null without throwing', () => {
    expect(() => aColor(null)).not.toThrow();
    expect(AVATAR_COLOURS).toContain(aColor(null));
  });

  it('handles an empty string without throwing', () => {
    expect(() => aColor('')).not.toThrow();
    expect(AVATAR_COLOURS).toContain(aColor(''));
  });

  it('returns different colours for different inputs', () => {
    // With 8 colours and many inputs, at least 2 distinct ones should appear
    const colours = new Set(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve',
      'Frank', 'Grace', 'Heidi'].map(aColor));
    expect(colours.size).toBeGreaterThan(1);
  });

  it('returns "#f97316" for the input "Alice" (pre-computed hash check)', () => {
    // Verifies the hash algorithm hasn't changed unintentionally
    expect(aColor('Alice')).toBe('#f97316');
  });
});

// ── catLabel — category display labels ───────────────────────────────────────

describe('catLabel (category display labels)', () => {
  it('maps "question" to the question label', () => {
    expect(catLabel('question')).toBe('❓ Question');
  });

  it('maps "bug" to the bug label', () => {
    expect(catLabel('bug')).toBe('🐛 Bug');
  });

  it('maps "feature" to the feature label', () => {
    expect(catLabel('feature')).toBe('💡 Feature');
  });

  it('maps "general" to the general label', () => {
    expect(catLabel('general')).toBe('💬 General');
  });

  it('returns the raw value for unknown categories', () => {
    expect(catLabel('unknown-category')).toBe('unknown-category');
  });
});

// ── catCls — category CSS class ──────────────────────────────────────────────

describe('catCls (category CSS class)', () => {
  it('prefixes category with "cat-"', () => {
    expect(catCls('question')).toBe('cat-question');
    expect(catCls('bug')).toBe('cat-bug');
    expect(catCls('feature')).toBe('cat-feature');
    expect(catCls('general')).toBe('cat-general');
  });
});
