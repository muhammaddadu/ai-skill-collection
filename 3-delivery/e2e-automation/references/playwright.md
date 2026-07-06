# Playwright (web E2E)

Implements the suite decisions in `../SKILL.md` with Playwright Test
(`@playwright/test`, TypeScript).

## Project config essentials

`playwright.config.ts` — the settings that matter for durability:

```ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  fullyParallel: true,          // per-file parallelism; tests must be order-free
  forbidOnly: !!process.env.CI, // a stray .only must fail CI, not shrink it
  retries: process.env.CI ? 1 : 0, // diagnostic only — see flake policy
  use: {
    baseURL: process.env.BASE_URL ?? 'http://127.0.0.1:3000',
    trace: 'on-first-retry',    // full trace exactly when you need to debug
    video: 'retain-on-failure', screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile-safari', use: { ...devices['iPhone 14'] } },
  ],
  webServer: {                  // boot the app for local runs; reuse in dev
    command: 'npm run dev',
    url: 'http://127.0.0.1:3000',
    reuseExistingServer: !process.env.CI,
  },
});
```

- **`baseURL`** makes tests environment-portable: `page.goto('/checkout')`,
  and CI swaps the env var to point at the ephemeral/staging environment.
- **`trace: 'on-first-retry'`** is the artifact contract: every CI failure
  ships a trace (`npx playwright show-trace`) — DOM snapshots, network,
  console at every step. This is what makes failures debuggable.
- **Projects** = browser/device matrix. Start with one desktop browser; add
  devices only when a journey genuinely differs.

## Locator strategy (precedence)

1. **`getByRole`** — first choice; asserts the accessible contract:
   `page.getByRole('button', { name: 'Place order' })`.
2. **`getByLabel` / `getByPlaceholder`** — form fields; **`getByText`** for
   non-interactive content assertions.
3. **`getByTestId`** — when no accessible handle exists; add
   `data-testid="order-total"` to the app rather than writing a CSS path.
4. **CSS/XPath structural paths — never.** `div.card:nth-child(3) button`
   encodes layout, not meaning.

Page objects wrap locators once:

```ts
export class CheckoutPage {
  constructor(private page: Page) {}
  readonly payButton = () => this.page.getByRole('button', { name: 'Pay now' });
  async payWith(card: TestCard) { /* fills + submits */ }
}
```

## Fixtures for auth and data setup

Use test fixtures so setup is declared, not repeated:

```ts
export const test = base.extend<{ user: TestUser }>({
  user: async ({}, use) => {
    const user = await api.createUser();      // API-seeded, unique per test
    await use(user);
    await api.deleteUser(user.id);            // teardown owns cleanup
  },
});
```

- **Auth once per worker, not per test:** a setup project logs in and saves
  `storageState`; tests start already authenticated. Per-identity state
  files support parallel runs without shared accounts.
- Data fixtures call your **API**, never click through the UI (SKILL step 4).

## Network stubbing boundaries

- **Stub third parties** you don't own — payment providers, analytics, email:
  `await page.route('**/api.stripe.com/**', route => route.fulfill({...}))`.
  Their sandbox outages must not fail your gate.
- **Never stub your own backend in a true E2E.** The moment `page.route`
  intercepts your own API, the test proves the frontend against your guess —
  it's a component test now; label it and move it to the merge-gate layer.
  A journey too hard to run against the real backend is an environment
  problem (SKILL step 4), not a stubbing opportunity.

## Sharding in CI

```yaml
strategy:
  matrix: { shard: [1/4, 2/4, 3/4, 4/4] }
steps:
  - run: npx playwright test --shard=${{ matrix.shard }}
  - uses: actions/upload-artifact@v4       # traces/videos per shard
    if: failure()
    with: { name: traces-${{ matrix.shard }}, path: test-results/ }
```

Merge reports with `npx playwright merge-reports`. Tag the smoke subset
(`{ tag: '@smoke' }`); run `--grep @smoke` on the merge gate, everything on
the release gate.

## Common failure patterns

- **Animation/async waits done with `waitForTimeout`** → flaky and slow. Use
  **web-first assertions** (`expect(locator).toBeVisible()`, `toHaveText`),
  which auto-retry; assert the post-animation state, never a delay.
- **Detached elements after navigation** → use locators (lazy, re-resolved),
  never held `elementHandle`s.
- **Race between click and network** → assert on the visible outcome
  (`expect(page.getByText('Order confirmed')).toBeVisible()`), or use
  `page.waitForResponse` when a journey has no visible marker.
- **First-load slowness misread as flake** → warm the app in the webServer
  healthcheck / global setup, not by padding every test's timeout.
