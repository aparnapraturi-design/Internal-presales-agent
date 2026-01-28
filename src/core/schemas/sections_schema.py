
# from __future__ import annotations

# from typing import Dict, List
# from pydantic import BaseModel, Field


# class SectionConfig(BaseModel):
#     key: str
#     title: str
#     description: str
#     order: int
#     required: bool = True


# class DocumentTypeConfig(BaseModel):
#     type: str
#     label: str
#     description: str
#     sections: List[SectionConfig]


# DOCUMENT_SECTIONS_CONFIG: Dict[str, DocumentTypeConfig] = {
#     "technical-scope": DocumentTypeConfig(
#         type="technical-scope",
#         label="Technical Scope Document",
#         description="Detailed technical specifications and scope of work",
#         sections=[
#             SectionConfig(
#                 key="executive-summary",
#                 title="Executive Summary",
#                 description="High-level overview of the technical scope",
#                 order=1,
#             ),
#             SectionConfig(
#                 key="company-background",
#                 title="Company Background",
#                 description="Client company overview and context",
#                 order=2,
#             ),
#             SectionConfig(
#                 key="current-state",
#                 title="Current State Analysis",
#                 description="Assessment of existing systems and processes",
#                 order=3,
#             ),
#             SectionConfig(
#                 key="requirements",
#                 title="Requirements Overview",
#                 description="Functional and non-functional requirements",
#                 order=4,
#             ),
#             SectionConfig(
#                 key="proposed-solution",
#                 title="Proposed Solution",
#                 description="Technical solution architecture and approach",
#                 order=5,
#             ),
#             SectionConfig(
#                 key="technology-stack",
#                 title="Technology Stack",
#                 description="Recommended technologies and frameworks",
#                 order=6,
#             ),
#             SectionConfig(
#                 key="integration-points",
#                 title="Integration Points",
#                 description="System integrations and data flows",
#                 order=7,
#             ),
#             SectionConfig(
#                 key="security-compliance",
#                 title="Security & Compliance",
#                 description="Security considerations and compliance requirements",
#                 order=8,
#             ),
#             SectionConfig(
#                 key="implementation-timeline",
#                 title="Implementation Timeline",
#                 description="Project phases and milestones",
#                 order=9,
#             ),
#             SectionConfig(
#                 key="resource-requirements",
#                 title="Resource Requirements",
#                 description="Team structure and skill requirements",
#                 order=10,
#             ),
#             SectionConfig(
#                 key="risks-mitigations",
#                 title="Risks & Mitigations",
#                 description="Identified risks and mitigation strategies",
#                 order=11,
#             ),
#             SectionConfig(
#                 key="assumptions-dependencies",
#                 title="Assumptions & Dependencies",
#                 description="Key assumptions and external dependencies",
#                 order=12,
#             ),
#         ],
#     ),

#     "feasibility-report": DocumentTypeConfig(
#     type="feasibility-report",
#     label="Feasibility Report",
#     description="Assessment of project viability and recommendations",
#     sections=[
#         SectionConfig(
#             key="executive-summary",
#             title="Executive Summary",
#             description="Key findings and recommendations",
#             order=1,
#         ),
#         SectionConfig(
#             key="project-overview",
#             title="Project Overview",
#             description="Scope and objectives",
#             order=2,
#         ),
#         SectionConfig(
#             key="business-requirements",
#             title="Business Requirements",
#             description="Business needs and success criteria",
#             order=3,
#         ),
#         SectionConfig(
#             key="technical-assessment",
#             title="Technical Assessment",
#             description="Technical viability analysis",
#             order=4,
#         ),
#         SectionConfig(
#             key="resource-assessment",
#             title="Resource Assessment",
#             description="Required resources and availability",
#             order=5,
#         ),
#         SectionConfig(
#             key="cost-benefit-analysis",
#             title="Cost-Benefit Analysis",
#             description="Financial analysis and ROI",
#             order=6,
#         ),
#         SectionConfig(
#             key="risk-assessment",
#             title="Risk Assessment",
#             description="Risk identification and impact",
#             order=7,
#         ),
#         SectionConfig(
#             key="alternative-solutions",
#             title="Alternative Solutions",
#             description="Comparison of approaches",
#             order=8,
#         ),
#         SectionConfig(
#             key="timeline-feasibility",
#             title="Timeline Feasibility",
#             description="Schedule constraints",
#             order=9,
#         ),
#         SectionConfig(
#             key="stakeholder-analysis",
#             title="Stakeholder Analysis",
#             description="Stakeholders and needs",
#             order=10,
#         ),
#         SectionConfig(
#             key="recommendations",
#             title="Recommendations",
#             description="Final recommendations",
#             order=11,
#         ),
#         SectionConfig(
#             key="appendix",
#             title="Appendix",
#             description="Supporting material",
#             order=12,
#             required=False,
#         ),
#     ],
# ),

# "commercial-proposal": DocumentTypeConfig(
#     type="commercial-proposal",
#     label="Commercial Proposal",
#     description="Business proposal with pricing and terms",
#     sections=[
#         SectionConfig(
#             key="cover-letter",
#             title="Cover Letter",
#             description="Introduction and value proposition",
#             order=1,
#         ),
#         SectionConfig(
#             key="executive-summary",
#             title="Executive Summary",
#             description="Proposal highlights",
#             order=2,
#         ),
#         SectionConfig(
#             key="understanding",
#             title="Understanding of Requirements",
#             description="Client needs",
#             order=3,
#         ),
#         SectionConfig(
#             key="company-profile",
#             title="Company Profile",
#             description="Our capabilities",
#             order=4,
#         ),
#         SectionConfig(
#             key="proposed-solution",
#             title="Proposed Solution",
#             description="Solution overview",
#             order=5,
#         ),
#         SectionConfig(
#             key="methodology",
#             title="Methodology",
#             description="Delivery methodology",
#             order=6,
#         ),
#         SectionConfig(
#             key="team-structure",
#             title="Team Structure",
#             description="Team and roles",
#             order=7,
#         ),
#         SectionConfig(
#             key="project-plan",
#             title="Project Plan",
#             description="Timeline and deliverables",
#             order=8,
#         ),
#         SectionConfig(
#             key="pricing",
#             title="Pricing",
#             description="Cost breakdown and terms",
#             order=9,
#         ),
#         SectionConfig(
#             key="terms-conditions",
#             title="Terms & Conditions",
#             description="Commercial terms",
#             order=10,
#         ),
#         SectionConfig(
#             key="case-studies",
#             title="Case Studies",
#             description="Relevant examples",
#             order=11,
#             required=False,
#         ),
#         SectionConfig(
#             key="appendix",
#             title="Appendix",
#             description="Supporting materials",
#             order=12,
#             required=False,
#         ),
#     ],
# ),
# }


from __future__ import annotations

from typing import Dict, List
from pydantic import BaseModel, Field


class SectionConfig(BaseModel):
    key: str
    title: str
    description: str
    order: int
    required: bool = True
    llm_requirements: str = Field(
        ..., description="Authoritative, section-specific instructions for LLMs. Treated as a hard contract."
    )


class DocumentTypeConfig(BaseModel):
    type: str
    label: str
    description: str
    sections: List[SectionConfig]


DOCUMENT_SECTIONS_CONFIG: Dict[str, DocumentTypeConfig] = {
    # =========================
    # TECHNICAL SCOPE DOCUMENT
    # =========================
    "technical-scope": DocumentTypeConfig(
        type="technical-scope",
        label="Technical Scope Document",
        description="Detailed technical specifications and scope of work",
        sections=[
            SectionConfig(
                key="executive-summary",
                title="Executive Summary",
                description="High-level overview of the technical scope",
                order=1,
                llm_requirements="""
Purpose:
Provide a concise, executive-level summary of the technical engagement.

Include:
- Business context and problem framing relevant to the technical scope
- The core technical objective and scope boundaries
- Key constraints, assumptions, or non-goals that materially shape the scope

Exclude:
- Detailed technical architecture or design decisions
- Implementation plans, milestones, or sequencing
- Cost, pricing, ROI, or commercial considerations

Writing Rules:
- Executive-ready, non-operational language
- Emphasize intent and boundaries, not mechanics

Stop Condition:
End after summarizing scope intent, boundaries, and constraints.
""",
            ),
            SectionConfig(
                key="company-background",
                title="Company Background",
                description="Client company overview and context",
                order=2,
                llm_requirements="""
Purpose:
Establish only the organizational and business context necessary to understand the technical scope.

Include:
- Industry context, scale, and operating environment
- Business lines, systems, or capabilities directly relevant to the engagement

Exclude:
- Corporate history or narrative not relevant to the scope
- Product marketing or solution positioning

Writing Rules:
- Factual, concise, and contextual
- Avoid repetition of information stated elsewhere

Stop Condition:
End once sufficient context for interpreting the technical scope is provided.
""",
            ),
            SectionConfig(
                key="current-state",
                title="Current State Analysis",
                description="Assessment of existing systems and processes",
                order=3,
                llm_requirements="""
Purpose:
Diagnose the current technical and operational state that the proposed work must operate within.

Include:
- Existing systems, platforms, workflows, and integrations
- Current process maturity, limitations, and known pain points
- Observable risks, technical debt, or control gaps

Exclude:
- Any description of proposed solutions or future-state vision
- Recommendations, improvements, or remediation plans
- Meeting notes, coordination details, or anecdotal commentary

Writing Rules:
- Diagnostic and evidence-based
- Neutral, non-advocacy tone
- Focus on facts and constraints, not opinions

Stop Condition:
End after the current limitations, constraints, and risks are clearly articulated.
""",
            ),
            SectionConfig(
                key="requirements",
                title="Requirements Overview",
                description="Functional and non-functional requirements",
                order=4,
                llm_requirements="""
Purpose:
Define what the solution must achieve, independent of how it will be implemented.

Include:
- Functional requirements expressed as capabilities or outcomes
- Non-functional requirements (performance, scalability, security, compliance, availability)
- Explicit assumptions where requirements are inferred

Exclude:
- Architectural or design decisions
- Justification, prioritization, or trade-off discussion

Writing Rules:
- Clear, testable, and unambiguous language
- Requirements-oriented phrasing ("must", "shall") where appropriate

Stop Condition:
End after all functional and non-functional requirements are stated.
""",
            ),
            SectionConfig(
                key="proposed-solution",
                title="Proposed Solution",
                description="Technical solution architecture and approach",
                order=5,
                llm_requirements="""
Purpose:
Describe the proposed technical approach at an architectural and conceptual level.

Include:
- High-level architecture and major components
- Design principles and key interactions between components
- Alignment to stated requirements

Exclude:
- Detailed implementation steps or algorithms
- Costing, ROI, or delivery timelines
- Operational runbooks or deployment details

Writing Rules:
- Structured and technical, but not code-level
- Focus on architecture and rationale, not execution

Stop Condition:
End after the solution approach and architecture are clearly described.
""",
            ),
            SectionConfig(
                key="technology-stack",
                title="Technology Stack",
                description="Recommended technologies and frameworks",
                order=6,
                llm_requirements="""
Purpose:
Specify the technologies required to support the proposed solution.

Include:
- Platforms, frameworks, tools, and infrastructure components
- Versioning or deployment assumptions where materially relevant

Exclude:
- Procurement strategy or licensing negotiation
- Comparative evaluation or vendor marketing

Writing Rules:
- Precise and factual
- One-line justification per technology at most

Stop Condition:
End after the complete stack is listed and briefly characterized.
""",
            ),
            SectionConfig(
                key="integration-points",
                title="Integration Points",
                description="System integrations and data flows",
                order=7,
                llm_requirements="""
Purpose:
Describe how the solution will interact with existing systems and external dependencies.

Include:
- Upstream and downstream systems
- High-level data flows and integration boundaries
- Assumptions about data ownership and responsibility

Exclude:
- Low-level API specifications or schemas
- Implementation sequencing or middleware configuration

Writing Rules:
- Boundary-focused and system-oriented

Stop Condition:
End after all required integrations and data flows are identified.
""",
            ),
            SectionConfig(
                key="security-compliance",
                title="Security & Compliance",
                description="Security considerations and compliance requirements",
                order=8,
                llm_requirements="""
Purpose:
Identify security, privacy, and compliance obligations that constrain the solution.

Include:
- Applicable regulations and standards
- Required security controls and principles
- Data protection and access considerations

Exclude:
- Tool-level configuration details
- Audit execution or certification processes

Writing Rules:
- Risk-oriented and compliance-focused

Stop Condition:
End after all security and compliance requirements are stated.
""",
            ),
            SectionConfig(
                key="implementation-timeline",
                title="Implementation Timeline",
                description="Project phases and milestones",
                order=9,
                llm_requirements="""
Purpose:
Provide a high-level view of delivery phases and milestones.

Include:
- Major phases and logical sequencing
- Key milestone outcomes

Exclude:
- Task-level plans or sprint breakdowns
- Resource allocation or staffing detail

Writing Rules:
- Milestone-oriented, not operational

Stop Condition:
End after the high-level timeline is outlined.
""",
            ),
            SectionConfig(
                key="resource-requirements",
                title="Resource Requirements",
                description="Team structure and skill requirements",
                order=10,
                llm_requirements="""
Purpose:
Identify the skills, roles, and capacity required to deliver the scope.

Include:
- Required roles and competencies
- Assumptions about client vs vendor responsibilities

Exclude:
- Named individuals or staffing assignments
- Hiring or onboarding plans

Writing Rules:
- Role- and capability-focused

Stop Condition:
End after resource needs and assumptions are stated.
""",
            ),
            SectionConfig(
                key="risks-mitigations",
                title="Risks & Mitigations",
                description="Identified risks and mitigation strategies",
                order=11,
                llm_requirements="""
Purpose:
Identify material technical and delivery risks and their mitigations.

Include:
- Risk description and potential impact
- High-level mitigation approach

Exclude:
- Contingency execution plans or operational playbooks

Writing Rules:
- Risk-based and concise

Stop Condition:
End after all material risks and mitigations are covered.
""",
            ),
            SectionConfig(
                key="assumptions-dependencies",
                title="Assumptions & Dependencies",
                description="Key assumptions and external dependencies",
                order=12,
                llm_requirements="""
Purpose:
Explicitly state assumptions and dependencies underpinning the scope.

Include:
- Business, technical, and third-party assumptions
- External dependencies and prerequisites

Exclude:
- Risk mitigation or recommendations

Writing Rules:
- Explicit and declarative

Stop Condition:
End after all assumptions and dependencies are listed.
""",
            ),
        ],
    ),

    # =========================
    # FEASIBILITY REPORT
    # =========================
    "feasibility-report": DocumentTypeConfig(
        type="feasibility-report",
        label="Feasibility Report",
        description="Assessment of project viability and recommendations",
        sections=[
            SectionConfig(
                key="executive-summary",
                title="Executive Summary",
                description="Key findings and recommendations",
                order=1,
                llm_requirements="""
Purpose:
Provide an executive decision summary of feasibility findings.

Include:
- Overall viability conclusion (e.g., feasible, conditionally feasible, not feasible)
- Primary value drivers and constraints
- Headline risks influencing the decision

Exclude:
- Detailed analysis or supporting data
- Implementation detail

Writing Rules:
- Decisive and outcome-oriented

Stop Condition:
End after presenting the feasibility conclusion and rationale at a high level.
""",
            ),
            SectionConfig(
                key="project-overview",
                title="Project Overview",
                description="Scope and objectives",
                order=2,
                llm_requirements="""
Purpose:
Define the scope, objectives, and boundaries of the initiative under evaluation.

Include:
- Objectives and success definition
- In-scope and out-of-scope elements

Exclude:
- Solution design or technical approach

Writing Rules:
- Clear boundary-setting language

Stop Condition:
End after scope and objectives are unambiguous.
""",
            ),
            SectionConfig(
                key="business-requirements",
                title="Business Requirements",
                description="Business needs and success criteria",
                order=3,
                llm_requirements="""
Purpose:
Articulate the business needs driving the initiative.

Include:
- Target business outcomes
- Quantitative or qualitative success criteria

Exclude:
- Technical requirements or solution assumptions

Writing Rules:
- Outcome-focused and measurable where possible

Stop Condition:
End after business requirements and success criteria are defined.
""",
            ),
            SectionConfig(
                key="technical-assessment",
                title="Technical Assessment",
                description="Technical viability analysis",
                order=4,
                llm_requirements="""
Purpose:
Assess whether the initiative is technically viable within current constraints.

Include:
- Capability gaps and constraints
- Technical risks and dependencies
- Alignment with existing systems

Exclude:
- Advocacy for a particular solution

Writing Rules:
- Analytical and constraint-driven

Stop Condition:
End after technical viability is assessed.
""",
            ),
            SectionConfig(
                key="resource-assessment",
                title="Resource Assessment",
                description="Required resources and availability",
                order=5,
                llm_requirements="""
Purpose:
Evaluate whether required resources are available or attainable.

Include:
- Skill, capacity, and organizational constraints
- External dependency assumptions

Exclude:
- Staffing or hiring plans

Writing Rules:
- Feasibility-focused

Stop Condition:
End after resource feasibility is assessed.
""",
            ),
            SectionConfig(
                key="cost-benefit-analysis",
                title="Cost-Benefit Analysis",
                description="Financial analysis and ROI",
                order=6,
                llm_requirements="""
Purpose:
Quantify the economic viability of the initiative.

Include:
- Cost categories and estimates
- Benefit categories and assumptions
- Financial metrics (ROI, payback, cost avoidance) if provided

Exclude:
- Recommendations or approvals
- Optimistic or promotional language

Writing Rules:
- Conservative and assumption-driven

Stop Condition:
End after costs, benefits, and assumptions are presented.
""",
            ),
            SectionConfig(
                key="risk-assessment",
                title="Risk Assessment",
                description="Risk identification and impact",
                order=7,
                llm_requirements="""
Purpose:
Identify business, technical, and execution risks.

Include:
- Risk description and impact
- Likelihood where known

Exclude:
- Mitigation strategies or contingency plans

Writing Rules:
- Risk-centric and neutral

Stop Condition:
End after all material risks are identified.
""",
            ),
            SectionConfig(
                key="alternative-solutions",
                title="Alternative Solutions",
                description="Comparison of approaches",
                order=8,
                llm_requirements="""
Purpose:
Compare feasible alternative approaches.

Include:
- High-level comparison criteria
- Strengths and weaknesses of alternatives

Exclude:
- Final recommendation or selection

Writing Rules:
- Comparative and balanced

Stop Condition:
End after alternatives are compared.
""",
            ),
            SectionConfig(
                key="timeline-feasibility",
                title="Timeline Feasibility",
                description="Schedule constraints",
                order=9,
                llm_requirements="""
Purpose:
Assess whether timelines are realistic.

Include:
- Schedule constraints and dependencies
- High-level feasibility assessment

Exclude:
- Detailed plans or milestones

Writing Rules:
- Constraint-oriented

Stop Condition:
End after timeline feasibility is assessed.
""",
            ),
            SectionConfig(
                key="stakeholder-analysis",
                title="Stakeholder Analysis",
                description="Stakeholders and needs",
                order=10,
                llm_requirements="""
Purpose:
Identify key stakeholders and their interests.

Include:
- Stakeholder groups and influence
- Alignment or conflict indicators

Exclude:
- Engagement or communication plans

Writing Rules:
- Analytical, not prescriptive

Stop Condition:
End after stakeholder landscape is described.
""",
            ),
            SectionConfig(
                key="recommendations",
                title="Recommendations",
                description="Final recommendations",
                order=11,
                llm_requirements="""
Purpose:
Provide clear, decision-ready recommendations based on the analysis.

Include:
- Directional guidance (e.g., proceed, defer, redesign)
- Conditions or prerequisites if applicable

Exclude:
- Re-analysis or restatement of evidence

Writing Rules:
- Decisive and concise

Stop Condition:
End after recommendations are stated.
""",
            ),
            SectionConfig(
                key="appendix",
                title="Appendix",
                description="Supporting material",
                order=12,
                required=False,
                llm_requirements="""
Purpose:
Provide supporting reference material.

Include:
- Detailed tables, assumptions, calculations
- Supplementary context

Exclude:
- Core narrative or conclusions

Writing Rules:
- Reference-only

Stop Condition:
End after supporting material.
""",
            ),
        ],
    ),

    # =========================
    # COMMERCIAL PROPOSAL
    # =========================
    "commercial-proposal": DocumentTypeConfig(
        type="commercial-proposal",
        label="Commercial Proposal",
        description="Business proposal with pricing and terms",
        sections=[
            SectionConfig(
                key="cover-letter",
                title="Cover Letter",
                description="Introduction and value proposition",
                order=1,
                llm_requirements="""
Purpose:
Introduce the proposal and establish value at an executive level.

Include:
- Client context and stated needs
- High-level value proposition and differentiation

Exclude:
- Technical detail or pricing specifics

Writing Rules:
- Persuasive but professional

Stop Condition:
End after introduction and value framing.
""",
            ),
            SectionConfig(
                key="executive-summary",
                title="Executive Summary",
                description="Proposal highlights",
                order=2,
                llm_requirements="""
Purpose:
Summarize the commercial proposal for executive review.

Include:
- Proposed value
- Commercial headline terms

Exclude:
- Detailed legal or technical content

Writing Rules:
- Outcome- and value-oriented

Stop Condition:
End after summarizing the proposal.
""",
            ),
            SectionConfig(
                key="understanding",
                title="Understanding of Requirements",
                description="Client needs",
                order=3,
                llm_requirements="""
Purpose:
Demonstrate clear understanding of client requirements.

Include:
- Client objectives and constraints

Exclude:
- Solution design or positioning

Writing Rules:
- Reflective and precise

Stop Condition:
End after requirements are articulated.
""",
            ),
            SectionConfig(
                key="company-profile",
                title="Company Profile",
                description="Our capabilities",
                order=4,
                llm_requirements="""
Purpose:
Present organizational credentials relevant to the proposal.

Include:
- Relevant experience and capabilities

Exclude:
- Marketing hype or unrelated achievements

Writing Rules:
- Evidence-based and concise

Stop Condition:
End after capability overview.
""",
            ),
            SectionConfig(
                key="proposed-solution",
                title="Proposed Solution",
                description="Solution overview",
                order=5,
                llm_requirements="""
Purpose:
Describe the proposed solution at a conceptual level.

Include:
- Approach and key components
- Alignment to client needs

Exclude:
- Deep technical architecture

Writing Rules:
- Client-oriented and clear

Stop Condition:
End after solution overview.
""",
            ),
            SectionConfig(
                key="methodology",
                title="Methodology",
                description="Delivery methodology",
                order=6,
                llm_requirements="""
Purpose:
Explain how the engagement will be delivered.

Include:
- Phases, governance, and quality controls

Exclude:
- Detailed schedules

Writing Rules:
- Process-focused and structured

Stop Condition:
End after methodology description.
""",
            ),
            SectionConfig(
                key="team-structure",
                title="Team Structure",
                description="Team and roles",
                order=7,
                llm_requirements="""
Purpose:
Describe the delivery team model.

Include:
- Roles and responsibilities

Exclude:
- Named individuals

Writing Rules:
- Role-based

Stop Condition:
End after team structure.
""",
            ),
            SectionConfig(
                key="project-plan",
                title="Project Plan",
                description="Timeline and deliverables",
                order=8,
                llm_requirements="""
Purpose:
Outline the proposed delivery plan.

Include:
- High-level milestones and deliverables

Exclude:
- Task-level detail

Writing Rules:
- Milestone-oriented

Stop Condition:
End after project plan.
""",
            ),
            SectionConfig(
                key="pricing",
                title="Pricing",
                description="Cost breakdown and terms",
                order=9,
                llm_requirements="""
Purpose:
Present pricing and commercial terms clearly.

Include:
- Pricing structure and assumptions
- Payment terms and validity

Exclude:
- Value justification or ROI arguments

Writing Rules:
- Precise and contract-ready

Stop Condition:
End after pricing and terms.
""",
            ),
            SectionConfig(
                key="terms-conditions",
                title="Terms & Conditions",
                description="Commercial terms",
                order=10,
                llm_requirements="""
Purpose:
State contractual and legal terms.

Include:
- Commercial and legal conditions

Exclude:
- Explanatory narrative

Writing Rules:
- Formal and unambiguous

Stop Condition:
End after terms are stated.
""",
            ),
            SectionConfig(
                key="case-studies",
                title="Case Studies",
                description="Relevant examples",
                order=11,
                required=False,
                llm_requirements="""
Purpose:
Provide evidence through relevant case studies.

Include:
- Brief, relevant case summaries

Exclude:
- Marketing language

Writing Rules:
- Fact-based

Stop Condition:
End after case studies.
""",
            ),
            SectionConfig(
                key="appendix",
                title="Appendix",
                description="Supporting materials",
                order=12,
                required=False,
                llm_requirements="""
Purpose:
Provide supporting reference material.

Include:
- Detailed tables, assumptions, or legal text

Exclude:
- Core narrative

Writing Rules:
- Reference-only

Stop Condition:
End after appendix content.
""",
            ),
        ],
    ),
}
