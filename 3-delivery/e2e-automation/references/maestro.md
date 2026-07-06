# Maestro (Expo / React Native E2E)

Implements the suite decisions in `../SKILL.md` with Maestro: plain-YAML
flows run against real builds (including EAS builds) on simulators,
emulators, or devices — no native test code in the app.

## Flow YAML basics

One flow = one journey, in `e2e/flows/` (or `.maestro/`):

```yaml
# e2e/flows/checkout.yaml
appId: com.yourco.yourapp
tags: [smoke]
---
- launchApp:
    clearState: true          # every flow starts from a known state
- tapOn:
    id: "product-card-0"
- tapOn: "Add to cart"        # text match — fine for stable, user-visible copy
- tapOn:
    id: "cart-checkout-button"
- inputText: "4242 4242 4242 4242"
- tapOn: "Pay now"
- assertVisible: "Order confirmed"
```

- `tapOn: "Text"` matches visible text; `tapOn: { id: ... }` matches
  `testID`. Prefer text for stable user-facing copy (it doubles as a copy
  regression check), `testID` for anything dynamic, translated, or icon-only.
- **Reuse with `runFlow`:** shared steps live in `e2e/flows/common/`:

```yaml
- runFlow: common/login.yaml
```

- Parameterize with env: `${USER_EMAIL}` in YAML,
  `maestro test -e USER_EMAIL=e2e-${CI_RUN_ID}@test.dev flows/`.

## testID conventions for RN

- Put `testID` on every element a flow touches: screen roots
  (`checkout-screen`), actionable elements (`cart-checkout-button`), and
  dynamic list items (`product-card-${index}`).
- Naming: `<screen>-<element>[-<index>]`, kebab-case — greppable and unique.
- On iOS, a parent with `testID` can swallow children's IDs
  (`accessible={true}` collapses the subtree); set `accessible={false}` on
  containers whose children need their own IDs.
- `testID` is production-harmless; do not strip it from release builds —
  you want to test the binary you ship.

## State setup: launch arguments and deep links

Arrange state without driving the UI (SKILL step 4):

- **Deep links** jump straight to the screen under test:

```yaml
- openLink: yourapp://checkout?cart=fixture-3-items
```

- **Launch arguments** flip test affordances the app reads at boot:

```yaml
- launchApp:
    arguments: { e2eUser: "e2e-${CI_RUN_ID}@test.dev", skipOnboarding: true }
```

- Seed the backend data itself via API before the flow runs (a setup script
  in CI), not through screens. The flow proves the journey, not the seeding.

## Running against EAS builds and in CI

- Build an **E2E profile** binary: simulator/emulator build
  (`"ios": { "simulator": true }` in `eas.json`) with the real backend URL
  for the E2E environment. Download the artifact, install, run:

```bash
eas build --profile e2e --platform ios --non-interactive
maestro test e2e/flows/ --format junit
```

- **Maestro Cloud** (hosted): `maestro cloud --app-file app.zip e2e/flows/`
  — managed devices, parallelism, videos/logs per flow; least CI plumbing.
- **Self-hosted runners**: macOS + simulator for iOS, Linux + emulator for
  Android; you own device boot, caching, and artifact upload
  (`--debug-output` for screenshots/logs). Cheaper at scale, more upkeep.
- Tag smoke flows (`tags: [smoke]`); run
  `maestro test --include-tags smoke` on the merge gate, the full set on the
  release gate (SKILL step 5). EAS Workflows can chain build → maestro run
  (see `expo-cicd-workflows`).

## Platform-split flows

Most flows run on both platforms unchanged. When behavior diverges
(permissions UI, back navigation), split at the step level:

```yaml
- runFlow:
    when: { platform: iOS }
    file: common/allow-notifications-ios.yaml
```

Fork whole files per platform only when the journeys genuinely differ.

## Common RN pitfalls

- **List virtualization — off-screen elements don't exist.** FlatList only
  renders visible rows, so `assertVisible` on row 40 fails. Scroll to it
  first: `scrollUntilVisible: { element: { id: "row-40" }, direction: DOWN }`.
- **Permission dialogs are OS UI** and can eat the next tap. Grant upfront:
  `launchApp: { permissions: { notifications: allow } }`; cover the
  permission journey itself in one dedicated flow.
- **Flaky animations/transitions** — a tap lands mid-transition and misses →
  use `waitForAnimationToEnd` after navigation-triggering steps, or
  `extendedWaitUntil: { visible: ..., timeout: 10000 }` for slow loads.
  Never fixed sleeps; they're the RN equivalent of `waitForTimeout`.
- **New-arch/Fabric quirks:** if IDs stop matching after an RN upgrade, use
  `maestro studio` to inspect the live view hierarchy before rewriting
  selectors.
