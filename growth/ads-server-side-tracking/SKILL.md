---
name: ads-server-side-tracking
description: "Server-side tracking pipeline audit: sGTM, Meta CAPI Gateway, Conversions API health, event_id deduplication, server-side hit ratio, pixel debugging, PII hashing. Use when user says server-side tracking, sGTM, CAPI, Conversions API, event deduplication, pixel health, or iOS 14.5 recovery."
user-invokable: false
tested_date: 2026-05-17
tested_with: claude-code v2.x
---

# Server-Side Tracking Pipeline Audit

Audits the entire server-side measurement pipeline that backs every paid
channel's modeled conversion data. Without server-side tracking in 2026,
expect 30-40% conversion data loss from iOS ATT, ITP, and aggressive ad
blockers — that's the gap between what's actually happening and what your
bid algorithms can see.

This sub-skill is technical and deep. It's NOT the same as `ads-attribution`,
which audits the *attribution model* sitting on top of these events.

## Process

1. Collect server-side stack inventory: sGTM container info, Meta CAPI
   integration method (Gateway / direct / partner integration), event
   schema documentation, hosting infrastructure (Cloud Run / GCS / AWS)
2. Read `ads/references/conversion-tracking.md` for cross-platform baseline
3. Test event flow: trigger known events → verify they appear in BOTH
   client-side (Pixel Helper / Tag Assistant) AND server-side (Events
   Manager test events / GA4 DebugView)
4. Audit deduplication, hashing, and parameter completeness
5. Score health PASS / WARNING / FAIL per surface
6. Generate findings report

## What to Analyze

### Server-Side Google Tag Manager (sGTM)

- **sGTM container deployed** — hosted on Cloud Run, GCS, App Engine, or
  custom infrastructure. Self-hosted preferred over Google-managed for cost
  and data residency
- **Custom domain configured** (`tags.example.com`) — first-party domain
  avoids ITP / ad-blocker blocking that hits googletagmanager.com
- **Client-side GTM forwards to sGTM** correctly; cookies, IP, user-agent
  preserved
- **GA4 events flow via sGTM** (no direct client → GA4 fallback)
- **Conversion Linker tag** enabled — preserves Google click IDs (gclid,
  gbraid, wbraid) across cross-domain navigation
- **Server-side privacy filters** — strip non-essential PII before forwarding
  to analytics; only hash + forward what's needed for matching

### Meta CAPI / CAPI Gateway

- **CAPI active** — Conversions API server-to-server alongside the Pixel
- **CAPI Gateway** preferred over manual server implementation (auto-
  hashing, parameter coverage, lower maintenance)
- **All major events server-side**: PageView, ViewContent, AddToCart,
  InitiateCheckout, Purchase, Lead, CompleteRegistration
- **Event Match Quality (EMQ) ≥8.0** for Purchase — confirm via Events
  Manager → Overview → Data sources
- **customer_information parameters** sent server-side: `em` (email), `ph`
  (phone), `fn`/`ln` (name), `ct`/`st`/`zp` (geo), `external_id`,
  `client_ip_address`, `client_user_agent`, `fbc`, `fbp`
- **Hashing**: lowercased + trimmed SHA-256 for PII fields BEFORE send
- **action_source** field set per event (`website`, `app`, `physical_store`,
  `email`, `system_generated`)

### Event Deduplication

- **event_id** generated client-side, included in BOTH the Pixel event AND
  the CAPI / sGTM payload — Meta + Google both dedupe on this
- **Dedup rate ≥90%** measured in Events Manager → Diagnostics
- **Timestamp alignment** — server-side event timestamp within 5 minutes
  of client-side counterpart
- **event_name consistency** — server-side uses the same canonical event
  names as client-side (don't rename in transit)

### Server-Side Hit Ratio

- **Server-side ≥80% of client-side hits** for Purchase / Lead — anything
  lower means iOS / ITP / ad-blocker data loss isn't being recovered
- **Server-side >100% acceptable** — means server-side captures conversions
  the client-side missed (good — that's what server-side is for)
- **Hit ratio monitored over time** — drops below 60% indicate broken
  server-side firing or missing event_id

### Pixel / Tag Debug Walkthrough

When deployed, validate every event end-to-end:

- **Facebook Pixel Helper** (Chrome extension) shows the Pixel firing
  client-side with correct event_name + event_id + value + currency
- **Meta Events Manager → Test Events** shows the CAPI event arriving server-
  side with matching event_id and customer_information parameters populated
- **Google Tag Assistant** confirms client-side gtag firing
- **GA4 DebugView** confirms server-side event arriving with event params
- **Network tab** shows client → sGTM forwarding (not client → Google direct)
- **`window.dataLayer`** populates expected variables before any tag fires

### Custom Event Taxonomy

- **Canonical event names** documented (e.g., `purchase` not `Purchase` or
  `PURCHASE` or `order_complete`)
- **Standard params per event**: `value`, `currency`, `content_ids`,
  `content_type`, `num_items`
- **Custom params namespaced** (`cx_segment`, `cx_funnel_step`) to avoid
  collision with platform-standard params
- **Schema versioned** — when the taxonomy changes, bump a version param
  so downstream platforms can handle the cutover

### Hash Quality & PII Handling

- **Email**: lowercased + trimmed + SHA-256 (no other normalization)
- **Phone**: E.164 format + SHA-256 (e.g., `+15551234567`)
- **Name**: lowercased + trimmed + SHA-256 per first / last separately
- **City / state / zip**: lowercased + SHA-256
- **NEVER hash already-hashed values** — double-hashing breaks matching
- **NEVER send plain PII server-side** — only hashed
- **GDPR / CPRA / CDPA compliance**: confirm consent state is read before
  sending PII server-side, even hashed

## Key Thresholds

| Metric | Pass | Warning | Fail |
|--------|------|---------|------|
| sGTM custom domain | Active | Configured, not active | Not configured |
| CAPI Gateway | Active | Manual CAPI | Pixel-only |
| EMQ (Purchase) | ≥8.0 | 6.0-7.9 | <6.0 |
| Dedup rate | ≥90% | 70-89% | <70% |
| Server / client hit ratio | 80-120% | 50-79% | <50% |
| customer_information completeness | 6+ params | 4-5 params | <4 params |
| Hash convention | Documented + verified | Implicit | Inconsistent |
| Test events validation | All 6 events pass | 3-5 events pass | <3 events pass |

## Output

### Server-Side Tracking Health Score

```
Server-Side Tracking Health Score: XX/100 (Grade: X)

sGTM Pipeline:               XX/100  ████████░░  (20%)
CAPI / CAPI Gateway:         XX/100  ██████████  (25%)
Deduplication:               XX/100  █████████░  (15%)
Server-Side Hit Ratio:       XX/100  ████████░░  (15%)
Pixel Debug (6 events):      XX/100  ███████░░░  (10%)
Hash Quality / PII Handling: XX/100  ██████░░░░  (15%)
```

### Deliverables

- `SERVER-SIDE-TRACKING-AUDIT.md`: Full pipeline findings
- Test-event reproduction log (which events validated end-to-end on which
  date, with screenshots from Events Manager / DebugView)
- EMQ improvement roadmap (parameter-by-parameter)
- Hit-ratio dashboard recommendation
- Pre-launch checklist for any new platform integration (Amazon Marketing
  Cloud, Apple Ads, TikTok Events API)
