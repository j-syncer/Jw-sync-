import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'node',
    // sql.js compiles WASM on first use — allow extra time
    testTimeout: 30000,
    hookTimeout: 30000,
  },
});
