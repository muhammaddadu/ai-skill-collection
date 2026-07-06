# Worked Examples — Diagnosis → Intervention → Outcome

Three end-to-end runs of the diagnostic, covering solo PM, team-with-agents,
and enterprise-RAG contexts. Use to calibrate assessments and interventions.

## Example 1: Solo PM Context Stuffing → Engineering

**Context:**
- Solo PM at early-stage startup
- Using Claude Projects for PRD writing
- Pasting entire PRDs (20 pages) + all user interviews (50 transcripts) every time
- Getting vague, inconsistent responses

**Assessment:**
- Symptoms: Hedged responses, normalized retries (4+ symptoms)
- Q1 (Decision): "I just want AI to understand my product" (no specific decision)
- Q2 (Persist/Retrieve): Persisting everything (no retrieval strategy)
- Q3 (Ownership): No formal owner (solo PM, ad-hoc)
- Q4 (Failure): Can't identify concrete failures for most context
- Q5 (Structure): Avoiding constraint documentation

**Diagnosis:** Active Context Hoarding Disorder

**Intervention:**
1. **Immediate:** Delete all context that fails Q4 test → keeps 20% of original
2. **Week 1:** Build constraints registry (10 technical constraints, 5 strategic)
3. **Week 2:** Create operational glossary (25 terms)
4. **Week 3:** Implement Research→Plan→Reset→Implement for next PRD

**Outcome:** Token usage down 70%, output quality up significantly, responses crisp and actionable.

---

## Example 2: Growth-Stage Team with Agent Chains

**Context:**
- Product team with 5 PMs
- Custom AI agents for discovery synthesis
- Agent A (research) → Agent B (synthesis) → Agent C (recommendations)
- Each agent passes full context to next → context window explodes to 100k+ tokens

**Assessment:**
- Symptoms: Escalating token costs, inconsistent outputs (3 symptoms)
- Q1 (Decision): Each agent has clear decision, but passes unnecessary context
- Q2 (Persist/Retrieve): Mixing persistent and episodic without strategy
- Q3 (Ownership): No explicit owner; each PM adds context
- Q4 (Failure): Agents pass "just in case" context with no falsifiable failure
- Q5 (Structure): Missing Context Manifest

**Diagnosis:** Agent orchestration without boundaries

**Intervention:**
1. **Immediate:** Define bounded context per agent (Agent A outputs only 2-page synthesis to Agent B, not full research)
2. **Week 1:** Assign context boundary owner (Lead PM)
3. **Week 2:** Create Context Manifest (what persists, what's retrieved, what's excluded)
4. **Week 3:** Implement Research→Plan→Reset→Implement between Agent B and Agent C

**Outcome:** Token usage down 60%, agent chain reliability up, costs reduced by 50%.

---

## Example 3: Enterprise with RAG but No Context Engineering

**Context:**
- Large enterprise with vector database RAG system
- "Stuff the whole knowledge base" approach (10,000+ documents)
- Retrieval returns 50+ chunks per query → floods context window
- Accuracy declining as knowledge base grows

**Assessment:**
- Symptoms: Vague responses despite "complete knowledge," normalized retries (2 symptoms)
- Q1 (Decision): Decisions clear, but retrieval has no intent (returns everything)
- Q2 (Persist/Retrieve): Good instinct to retrieve, but no filtering
- Q3 (Ownership): Engineering owns RAG, Product doesn't own context boundaries
- Q4 (Failure): Can't identify why 50 chunks needed vs. 5
- Q5 (Structure): Knowledge base has no structure (flat documents, no metadata)

**Diagnosis:** Retrieval without intent (RAG as context stuffing)

**Intervention:**
1. **Immediate:** Limit retrieval to top 5 chunks per query (down from 50)
2. **Week 1:** Implement Contextual Retrieval (Anthropic) — prepend explanatory context to each chunk during indexing
3. **Week 2:** Add metadata to documents (category, recency, authority)
4. **Week 3:** Product team defines retrieval intent per query type (discovery = customer insights, feasibility = technical constraints)

**Outcome:** Accuracy up 35% (from Anthropic benchmark), latency down 60%, token usage down 80%.
