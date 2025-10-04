# Transitioning from writing code to writing specs

## The Mindset Shift: From Chore to Core Engineering Skill

Before any training begins, the first step is to reframe the purpose of a specification. Engineers must see it not as bureaucratic overhead, but as an essential engineering tool, akin to an architectural blueprint for software.

* **It's a De-risking Tool:** A good spec is the cheapest and fastest place to find flawed logic, uncover hidden dependencies, and identify edge cases. Finding a problem on paper costs minutes; finding it after code is written costs days or weeks.
* **It's an Alignment Contract:** The spec serves as the source of truth that aligns Product Managers, Designers, Engineers, and QA. It's the document that ensures everyone is building the same thing.
* **It's a Thinking Tool:** The act of writing forces clarity of thought. It converts a vague idea into a concrete plan, exposing gaps in the author's own understanding.

---

### A Multi-Dimensional Training Framework

A robust training program should be built on four distinct, yet interconnected, dimensions: **User & Business Context**, **Technical Blueprinting**, **Scope & Boundary Setting**, and the **Art of Communication**.

#### Dimension 1: The User & Business Context (The "Why")

Engineers often excel at the "how," but a great spec must be grounded in the "why." This dimension connects the technical solution to the user and business needs.

* **Training Module: "Who is this for?"**
    * **Skill:** User Empathy.
    * **Activity:** Work with Product Managers to review user personas, customer interviews, and "Jobs to be Done" (JTBD) frameworks. For a given feature, engineers should be able to articulate: "Who is the primary user?" and "What problem are we solving for them?"
* **Training Module: "How do we win?"**
    * **Skill:** Defining Success.
    * **Activity:** Practice writing clear, measurable success metrics (KPIs, OKRs) for a feature. For example, instead of "Improve the dashboard," a better metric is "Reduce the time it takes for users to find a key report from 60 seconds to 15 seconds." This forces engineers to think about the impact of their work.

#### Dimension 2: The Technical Blueprinting (The "What")

This is the core of the spec, where engineers translate requirements into a detailed technical plan.

* **Training Module: "Functional & Non-Functional Requirements"**
    * **Skill:** Comprehensive Requirement Definition.
    * **Activity:** Analyze existing products (e.g., Google Docs, Slack). Have engineers deconstruct them by listing their functional requirements (what it *does*, e.g., "allows real-time text editing") and, crucially, their non-functional requirements (the "-ilities," e.g., scalability, security, reliability, accessibility). Most junior engineers forget the latter.
* **Training Module: "Systems, Data, and Interfaces"**
    * **Skill:** System Design and API Definition. 
    * **Activity:** Host "Spec Dojos." Present a feature request and have engineers work in groups to draw the system architecture, define the data models (e.g., new database tables/columns), and draft the API contracts (endpoints, request/response payloads). This is a highly practical and collaborative exercise.

#### Dimension 3: Scope & Boundary Setting (The "What It Isn't")

A great spec is as much about what's *not* being built as what is. This prevents scope creep and manages expectations.

* **Training Module: "Drawing the Line"**
    * **Skill:** Scope Management.
    * **Activity:** Give engineers a vaguely defined project. Their first task is to write a "Scope and Non-Goals" section. A "Non-Goal" explicitly states what is out of scope for the current version (e.g., "This project will support single sign-on with Google, but not with SAML," or "This feature will be available on web, but not on the mobile app initially"). Reviewing these as a group is highly effective.
* **Training Module: "Uncovering the Unknowns"**
    * **Skill:** Risk and Dependency Identification.
    * **Activity:** Practice creating a "Questions & Assumptions" section. For any spec, engineers should list what they are assuming to be true and what questions need to be answered before development can begin. This surfaces dependencies on other teams early.

#### Dimension 4: The Art of Communication (The "How It's Understood")

The most brilliant technical plan is useless if it can't be understood by others. This dimension focuses on clarity and conciseness.

* **Training Module: "Writing for Your Audience"**
    * **Skill:** Clarity and Precision.
    * **Activity:** Provide a poorly written, overly technical spec. Have engineers rewrite it, creating two versions: one for a technical audience (other engineers) and one for a non-technical audience (product/marketing). This teaches them to adjust their language and level of detail.
* **Training Module: "A Picture is Worth 1,000 Lines of Text"**
    * **Skill:** Visual Communication.
    * **Activity:** Introduce lightweight diagramming tools (like Lucidchart, Miro, or even just Excalidraw). Challenge engineers to explain a complex workflow or system interaction using only a simple flowchart or sequence diagram. This builds the habit of using visuals to complement text.

### The Implementation Program: Putting It All Together

1.  **Develop a Standardized Spec Template:** Create a company-wide template that includes sections for all the key dimensions mentioned above. This provides a scaffold for engineers to build upon and ensures consistency.
2.  **Launch with a Workshop:** Kick off the initiative with a mandatory workshop that introduces the "Why," walks through the template, and uses examples of good and bad specs.
3.  **Institute Formal Spec Reviews:** Make spec reviews a required step in your development process, just like code reviews. This is the single most important reinforcement mechanism.
    * **Use a checklist:** Reviewers should check for clear success metrics, non-goals, non-functional requirements, etc.
    * **Involve cross-functional partners:** Invite a PM or Designer to the review. This reinforces that the spec is a team-wide alignment tool.
4.  **Create a "Hall of Fame":** Maintain a repository of exceptionally well-written specs. When new engineers join, point them to these as the gold standard. Acknowledge and praise the authors of these documents publicly.
5.  **Provide Mentorship:** Pair junior engineers with senior engineers who excel at spec writing. Have them pair-write their first few specs, offering real-time feedback and guidance.