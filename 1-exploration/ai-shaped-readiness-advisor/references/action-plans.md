# Action Plans — Detailed 4-Week Plans per Priority

Once the user selects (or accepts) a priority competency in Step 7, deliver the
matching plan below, tailored to their context from Step 0.

---

## If Priority = Context Design

**Goal:** Build a durable "reality layer" that both humans and AI trust—move from context stuffing to context engineering.

**Pre-Phase: Diagnose Context Stuffing (If Needed)**
If the user is at Level 1-2, first diagnose context stuffing symptoms:
1. Run through the 5 diagnostic questions (see `context-engineering-advisor`)
2. Identify what they're persisting that should be retrieved
3. Assign context boundary owner
4. Create Context Manifest (what's always-needed vs. episodic)

**Phase 1: Document Constraints (Week 1)**
1. Create a constraints registry:
   - Technical constraints (APIs, data models, performance limits)
   - Regulatory constraints (GDPR, HIPAA, etc.)
   - Strategic constraints (we will/won't build X)
2. Apply diagnostic question #4 to each constraint: "What fails if we exclude this?"
3. Format: Structured file AI agents can parse (YAML, JSON, or Markdown with frontmatter)
4. Version control in Git

**Phase 2: Build Operational Glossary (Week 2)**
1. List top 20-30 terms the team uses (e.g., "user," "customer," "activation," "churn")
2. Define each unambiguously (avoid "it depends")
3. Include edge cases and exceptions
4. Add to CLAUDE.md or project instructions
5. This becomes the **long-term persistent memory** (Declarative Memory)

**Phase 3: Establish Evidence Standards + Context Boundaries (Week 3)**
1. Define what counts as validation:
   - User feedback: "X users said Y" (with quotes)
   - Analytics: "Metric Z changed by N%" (with dashboard link)
   - Competitive intel: "Competitor A launched B" (with source)
2. Reject: "I think," "We feel," "It seems like"
3. Define context boundaries using the 5 diagnostic questions:
   - What specific decision does each piece of context support?
   - Can retrieval replace persistence?
   - Who owns the context boundary?
4. Create Context Manifest document
5. Codify in team docs

**Phase 4: Implement Memory Architecture + Workflows (Week 4)**
1. **Set up two-layer memory:**
   - **Short-term (conversational):** Summarize/truncate older parts of conversation
   - **Long-term (persistent):** Constraints registry + operational glossary (consider vector database for retrieval)
2. **Implement Research→Plan→Reset→Implement cycle:**
   - Research: Allow chaotic context gathering
   - Plan: Synthesize into high-density SPEC.md or PLAN.md
   - Reset: Clear context window
   - Implement: Use only the plan as context
3. Update AI prompts to reference constraints registry and glossary
4. Test: Ask AI to cite constraints when making recommendations
5. Measure: % of AI outputs that cite evidence vs. hallucinate; token usage efficiency

**Success Criteria:**
- Constraints registry has 20+ entries
- Operational glossary has 20-30 terms
- Evidence standards documented and shared
- Context Manifest created (always-needed vs. episodic)
- Context boundary owner assigned
- Two-layer memory architecture implemented
- Research→Plan→Reset→Implement cycle tested on 1 workflow
- AI agents reference these automatically
- Token usage down 30%+ (less context stuffing)
- Output consistency up (fewer retries)

**Related Skills:**
- `context-engineering-advisor` — Deep dive on diagnosing context stuffing and implementing memory architecture
- `problem-statement` — Define constraints before framing problems
- `epic-hypothesis` — Evidence-based hypothesis writing

---

## If Priority = Agent Orchestration

**Goal:** Turn one-off prompts into repeatable, traceable AI workflows.

**Phase 1: Map Current Workflows (Week 1)**
1. Pick the most frequent AI use case (e.g., "analyze user feedback")
2. Document every step currently taken:
   - Copy/paste feedback into ChatGPT
   - Ask for themes
   - Manually categorize
   - Write summary
3. Identify pain points (manual handoffs, inconsistent results)

**Phase 2: Design Orchestrated Workflow (Week 2)**
1. Define workflow loop:
   - **Research:** AI reads all feedback (structured input)
   - **Synthesis:** AI identifies themes (with evidence)
   - **Critique:** AI flags contradictions or weak signals
   - **Decision:** Human reviews and decides next steps
   - **Log:** AI records rationale and sources
2. Each step must be traceable (show sources, reasoning)

**Phase 3: Build and Test (Week 3)**
1. Implement workflow using:
   - Claude Projects (if simple)
   - Custom GPTs (if moderate)
   - API orchestration (if complex)
2. Run on 3 past examples; compare to manual process
3. Measure: Time saved, consistency improved, traceability added

**Phase 4: Document and Scale (Week 4)**
1. Version-control prompts (Git)
2. Document workflow steps for team
3. Train 2 teammates; observe results
4. Iterate based on feedback

**Success Criteria:**
- At least 1 workflow runs consistently (same inputs → predictable process)
- Each step is traceable (AI cites sources)
- Team can replicate workflow without the owner's involvement

**Related Skills:**
- `pol-probe-advisor` — Use orchestrated workflows for validation experiments

---

## If Priority = Outcome Acceleration

**Goal:** Use AI to compress learning cycles, not just speed up tasks.

**Phase 1: Identify Bottleneck (Week 1)**
1. Map the current learning cycle (e.g., hypothesis → experiment → analysis → decision)
2. Time each step
3. Identify slowest step (usually: validation lag, approval delays, or meeting overhead)

**Phase 2: Design AI Intervention (Week 2)**
1. Ask: "What if this step happened overnight?"
   - Feasibility checks: AI spike in 2 hours vs. 2 days
   - User research synthesis: AI analysis in 1 hour vs. 1 week
   - Approval pre-checks: AI validates against constraints before meeting
2. Design minimal AI workflow to eliminate bottleneck

**Phase 3: Run Pilot (Week 3)**
1. Test AI intervention on 1 real initiative
2. Measure cycle time: before vs. after
3. Validate quality: Did AI maintain rigor, or cut corners?

**Phase 4: Scale (Week 4)**
1. If successful (cycle time down 50%+, quality maintained), apply to 3 more initiatives
2. Document workflow
3. Train team

**Success Criteria:**
- Learning cycle compressed by 50%+ on at least 1 initiative
- Quality maintained (no shortcuts that compromise rigor)
- Team adopts the accelerated workflow

**Related Skills:**
- `pol-probe` — Use AI to run PoL probes faster
- `discovery-process` — Compress discovery cycles with AI

---

## If Priority = Team-AI Facilitation

**Goal:** Redesign team systems so AI operates as co-intelligence, not accountability shield.

**Phase 1: Establish Review Norms (Week 1)**
1. Codify rule: "AI outputs are drafts, not finals"
2. Define review protocol:
   - Who reviews AI outputs? (peer, lead PM, cross-functional partner)
   - When? (before sharing externally, before decisions)
   - What to check? (accuracy, completeness, evidence citation)
3. Share with team, get buy-in

**Phase 2: Set Evidence Standards (Week 2)**
1. AI must cite sources (no hallucinations)
2. Reject outputs that say "I think" or "it seems"
3. Require: "According to [source], [fact]"
4. Add to team operating docs

**Phase 3: Define Decision Authority (Week 3)**
1. Clarify: AI recommends, humans decide
2. Document who has authority to override AI recommendations (PM, team lead, cross-functional consensus)
3. Create escalation path (what if AI and human disagree?)

**Phase 4: Build Psychological Safety (Week 4)**
1. Team exercise: Share an AI mistake you caught (normalize catching errors)
2. Reward critical thinking ("Good catch on that AI hallucination!")
3. Avoid: "Why didn't you just use AI?" (shaming)

**Success Criteria:**
- Review norms documented and followed by team
- Evidence standards codified
- Decision authority clear
- Team comfortable challenging AI outputs

**Related Skills:**
- `problem-statement` — Evidence-based problem framing
- `epic-hypothesis` — Testable, evidence-backed hypotheses

---

## If Priority = Strategic Differentiation

**Goal:** Create defensible competitive advantages, not just efficiency gains.

**Phase 1: Identify Moat Opportunities (Week 1)**
1. Ask: "What could we do with AI that competitors can't replicate by adding headcount?"
   - New customer capabilities (e.g., "AI advisor suggests personalized roadmap")
   - Workflow rewiring (e.g., "Validate product ideas in 2 days vs. 3 weeks")
   - Economics shift (e.g., "Deliver enterprise features at SMB prices via AI automation")
2. List 5 candidates
3. Prioritize by defensibility (how hard to copy?)

**Phase 2: Design AI-Enabled Capability (Week 2)**
1. Pick top candidate
2. Design end-to-end workflow:
   - What does customer experience?
   - What does AI do behind the scenes?
   - What human judgment is required?
3. Sketch MVP (minimum viable moat)

**Phase 3: Build and Test (Weeks 3-4)**
1. Build prototype (can be PoL probe, not production)
2. Test with 5 customers
3. Measure: Does this create value competitors can't match?

**Phase 4: Validate Moat (Week 5)**
1. Ask: "How would a competitor replicate this?"
   - If answer is "hire more people," it's not a moat
   - If answer is "redesign their entire org," you have a moat
2. Document competitive analysis
3. Decide: Build full version, pivot, or kill

**Success Criteria:**
- Identified at least 1 AI-enabled capability competitors can't easily copy
- Validated with customers (they see the value)
- Confirmed defensibility (competitor analysis)

**Related Skills:**
- `positioning-statement` — Articulate the AI-driven differentiation
- `jobs-to-be-done` — Understand what customers hire the AI capabilities to do
