# STRIDE checklist

Prompt questions per category, with one concrete example each for a web app, a
mobile app, and an API/event system. Use while walking each trust boundary in
Step 3 of the workflow. Record "considered, not applicable" for categories that
genuinely don't apply at a boundary — silence reads as "not considered".

## Spoofing — pretending to be someone or something else

- How does each side of this boundary know who it's talking to?
- Can an attacker present someone else's identity (stolen session, forged token, borrowed device)?
- Are any identifiers guessable or reusable (sequential IDs, predictable tokens, long-lived links)?
- Is there any path that skips authentication (health endpoints, webhooks, "internal" services)?

**Web:** a password-reset link that doesn't expire lets anyone with an old email spoof the account owner.
**Mobile:** the app trusts the device-stored user ID; a rooted device edits it and becomes another user.
**API/event:** a webhook receiver accepts any POST with the right shape — no signature check — so anyone can fake "payment succeeded" events.

## Tampering — modifying data or code in flight or at rest

- What data crosses this boundary, and what stops it being modified in transit?
- Can the client alter values the server trusts (prices, role flags, hidden form fields, JWT claims)?
- Who can write to the stores and queues behind this boundary, and is that write path scoped?
- Are updates validated against invariants, or just persisted as sent?

**Web:** the checkout form posts the price from a hidden field; editing the DOM buys the item for $0.01.
**Mobile:** the app caches entitlements in a plist; editing the file unlocks premium features offline.
**API/event:** a consumer trusts the `amount` field in a queue message; anything that can publish to the topic can mint money.

## Repudiation — doing something and deniably

- If a user or admin disputes an action, what evidence exists that it happened and who did it?
- Are security-relevant actions (logins, permission changes, exports, deletes) logged with actor + timestamp?
- Can logs themselves be altered or deleted by the people they'd implicate?
- Do shared/service accounts make "who did it" unanswerable?

**Web:** admins share one login; when a customer record is deleted, no one can say which admin did it.
**Mobile:** in-app purchases are granted client-side with no server receipt trail; refund disputes are unwinnable.
**API/event:** events carry no producer identity, so a poisoned message can't be traced to its source service.

## Information disclosure — data reaching eyes it shouldn't

- What sensitive data (PII, secrets, tokens, internal IDs) crosses or sits near this boundary?
- Do error messages, logs, or verbose responses leak internals (stack traces, SQL, other users' data)?
- Are list/detail endpoints scoped to the caller, or do they return everything and filter client-side?
- Where is this data at rest, who can read it, and is it in backups/exports/analytics too?

**Web:** the API returns the full user object — including email and phone — to any logged-in viewer of a public profile.
**Mobile:** the app logs the auth token to the device console, where any connected debugger reads it.
**API/event:** an events topic carries full customer records; every consumer team gets PII it never needed.

## Denial of service — making it unavailable

- What's the most expensive operation an unauthenticated caller can trigger, and how often?
- Are there rate limits/quotas at this boundary, per user and per IP?
- Can one tenant's load starve others (shared pools, unbounded queries, missing pagination)?
- What happens when a downstream dependency at this boundary is slow rather than down?

**Web:** the search endpoint runs an unindexed scan; a crafted query pegs the DB for everyone.
**Mobile:** the app retries failed syncs in a tight loop; a backend blip becomes a self-inflicted stampede.
**API/event:** one oversized message with no size limit wedges the consumer and blocks the whole partition.

## Elevation of privilege — doing what you're not authorized to do

- Where is authorization enforced at this boundary — and is it checked on every path, or only in the UI?
- Can a caller act on another user's resources by swapping an ID (IDOR)?
- Do any roles/flags get decided client-side or copied into tokens that outlive a demotion?
- Is there an admin/support path with weaker checks than the user-facing one?

**Web:** `/orders/{id}` checks login but not ownership; changing the ID reads anyone's order.
**Mobile:** the app hides admin screens for non-admins but the underlying endpoints don't check the role.
**API/event:** an internal service-to-service API assumes "inside the VPC = authorized"; any compromised pod has full access.

## Trust-boundary spotting guide

A trust boundary is any point where the level of trust changes — where data or
a request moves from a less-trusted context to a more-trusted one (or vice
versa). Walk these five; most systems have all of them:

- **User ↔ app:** everything from a browser, mobile app, or user device is attacker-controlled input — including headers, cookies, and "hidden" fields. The client is never trusted.
- **App ↔ backend:** the frontend/backend seam. Anything enforced only in the client (validation, role checks, rate limiting) does not exist at this boundary.
- **Backend ↔ third-party:** outbound calls and inbound webhooks. You trust their availability, their data quality, and their security posture — decide how much of each you actually should. Verify webhook signatures; treat their data as input, not truth.
- **Service ↔ service:** internal doesn't mean trusted. "It's inside the network" is the assumption behind most lateral-movement breaches; authenticate and scope service calls.
- **Human ↔ admin-tooling:** support consoles, ops scripts, and dashboards usually have the system's highest privileges and its weakest controls (shared accounts, no audit log, no MFA). Model them like a public endpoint with superpowers.
