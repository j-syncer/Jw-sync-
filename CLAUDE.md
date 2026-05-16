# JW Sync — Claude Instructions

## Development Workflow

All changes must go to the **beta site first**:

1. Make changes to `beta/index.html` (serves live at **jwsync.org/beta**)
2. Commit and push to `main` so the beta site updates immediately
3. Wait for the user to review at jwsync.org/beta
4. Only when the user says to push to the main site, apply the same changes to `index.html` and push — this updates **jwsync.org**

**Never touch `index.html` (production) unless the user explicitly approves.**

## File Map

| File | URL |
|------|-----|
| `beta/index.html` | jwsync.org/beta — staging/testing |
| `index.html` | jwsync.org — production/live |
