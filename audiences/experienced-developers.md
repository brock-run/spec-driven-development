# Experienced Developer Guide to Advanced SDD

## Beyond Basic Specs: Advanced SDD Practices

As an experienced developer, you understand the value of planning and documentation. This guide focuses on advanced SDD techniques that leverage your expertise while maximizing the potential of AI-assisted development.

## Advanced Planning and Context Engineering

### Context-Rich Specifications

Move beyond basic requirements to create specifications that capture domain knowledge, architectural constraints, and business context that AI agents need for intelligent implementation.

#### Domain Context Template
```markdown
## Domain Context
**Business Domain:** [e.g., Financial Services, Healthcare, E-commerce]
**Regulatory Requirements:** [GDPR, HIPAA, PCI-DSS, etc.]
**Performance Constraints:** [SLA requirements, scalability needs]
**Integration Points:** [Existing systems, third-party services]
**Technical Debt Considerations:** [Legacy code, migration constraints]
```

#### Architecture Decision Records (ADRs) in Specs
Embed architectural decisions directly in your design documents:

```markdown
## Architecture Decisions

### ADR-001: Database Choice
**Status:** Accepted
**Context:** Need to handle 10M+ records with complex queries
**Decision:** PostgreSQL with read replicas
**Consequences:** 
- Pros: ACID compliance, complex query support
- Cons: Operational complexity, scaling limitations
- Alternatives Considered: MongoDB, DynamoDB
```

### Multi-Layer Specification Strategy

#### Layer 1: System Architecture
```markdown
# System Design Document

## Service Architecture
- **API Gateway**: Request routing and authentication
- **Core Services**: Business logic microservices  
- **Data Layer**: Database and caching strategy
- **Integration Layer**: External service connections

## Cross-Cutting Concerns
- **Security**: Authentication, authorization, data protection
- **Observability**: Logging, metrics, tracing
- **Resilience**: Circuit breakers, retries, fallbacks
```

#### Layer 2: Service Specifications
Individual service specs that reference the system design:

```markdown
# User Service Specification

## Context
Part of the larger user management system defined in [System Design](../system-design.md).

## Service Boundaries
**Owns:** User profiles, authentication, preferences
**Depends On:** Notification service, audit service
**Provides To:** All client applications, other services
```

## Legacy System Integration Strategies

### Assessment Framework

Before integrating SDD with legacy systems, assess the current state:

#### Legacy System Evaluation Matrix
```markdown
| System Component | Modernization Strategy | SDD Integration Level |
|------------------|----------------------|---------------------|
| User Management  | Strangler Fig Pattern | Full SDD for new features |
| Payment Processing | Maintain & Wrap | API-only SDD specs |
| Reporting Engine | Rewrite in Phases | Complete SDD rewrite |
```

### Integration Patterns

#### 1. Strangler Fig Pattern with SDD
Gradually replace legacy functionality using SDD for new components:

```markdown
# Legacy Integration Plan

## Phase 1: API Facade
- [ ] Create SDD spec for API wrapper around legacy system
- [ ] Implement facade with comprehensive error handling
- [ ] Add monitoring and observability

## Phase 2: Feature Migration  
- [ ] Identify high-value features for migration
- [ ] Create SDD specs for replacement components
- [ ] Implement with feature flags for gradual rollout

## Phase 3: Data Migration
- [ ] Design data synchronization strategy
- [ ] Implement dual-write pattern with SDD specs
- [ ] Plan cutover and rollback procedures
```

#### 2. Event-Driven Integration
Use events to decouple legacy systems from new SDD-built components:

```markdown
# Event Integration Design

## Event Schema
```json
{
  "eventType": "user.profile.updated",
  "version": "1.0",
  "timestamp": "2025-01-01T00:00:00Z",
  "source": "legacy-user-system",
  "data": {
    "userId": "12345",
    "changes": ["email", "preferences"]
  }
}
```

## Event Handlers (SDD Specified)
- **Profile Sync Handler**: Updates modern user service
- **Notification Handler**: Triggers relevant notifications  
- **Audit Handler**: Records changes for compliance
```

### Legacy Code Documentation Strategy

Transform undocumented legacy code into SDD-compatible specifications:

#### Reverse Engineering Template
```markdown
# Legacy System Analysis: [Component Name]

## Current Behavior (Observed)
**Input Processing:** [Document actual input handling]
**Business Rules:** [Extract implicit business logic]
**Error Conditions:** [Catalog failure modes]
**Dependencies:** [Map external dependencies]

## Proposed SDD Specification
**Requirements:** [Convert behavior to formal requirements]
**Design:** [Document intended architecture]
**Migration Tasks:** [Plan modernization steps]
```

## Multi-Agent Workflow Orchestration

### Agent Specialization Strategy

Design workflows that leverage different AI agents for their strengths:

#### Agent Assignment Matrix
```markdown
| Task Type | Primary Agent | Reasoning |
|-----------|---------------|-----------|
| Requirements Analysis | ChatPRD/Claude | Natural language processing |
| Architecture Design | GitHub Copilot | Code structure understanding |
| Implementation | Cursor/Kiro | Real-time coding assistance |
| Testing Strategy | Specialized Test Agent | Test case generation |
| Documentation | Claude/GPT-4 | Technical writing |
```

### Workflow Orchestration Patterns

#### Sequential Handoff Pattern
```markdown
# Multi-Agent SDD Workflow

## Phase 1: Requirements (ChatPRD)
- Generate initial requirements from PRD
- Refine with stakeholder input
- Output: `requirements.md`

## Phase 2: Architecture (Claude)  
- Analyze requirements for technical implications
- Design system architecture and component interfaces
- Output: `design.md`

## Phase 3: Task Planning (GitHub Copilot)
- Break down design into implementation tasks
- Sequence tasks for optimal development flow
- Output: `tasks.md`

## Phase 4: Implementation (Cursor/Kiro)
- Execute tasks with real-time AI assistance
- Maintain traceability to specifications
- Output: Working code + tests
```

#### Parallel Review Pattern
```markdown
# Concurrent Agent Review Process

## Specification Review
- **Agent A (Claude)**: Requirements completeness and clarity
- **Agent B (Copilot)**: Technical feasibility and implementation complexity  
- **Agent C (Specialized)**: Security and compliance considerations

## Synthesis Phase
- Combine feedback from all agents
- Resolve conflicts and inconsistencies
- Update specifications based on multi-agent input
```

## Performance Optimization for Large-Scale Specs

### Specification Modularity

Break large systems into manageable, interconnected specifications:

#### Microspec Architecture
```markdown
# System Specification Structure

## Core Specifications
- `user-management/` - User service specs
- `payment-processing/` - Payment service specs  
- `notification-system/` - Notification service specs

## Shared Specifications  
- `common/data-models.md` - Shared data structures
- `common/api-standards.md` - API design guidelines
- `common/security-patterns.md` - Security implementations

## Integration Specifications
- `integrations/user-payment.md` - Cross-service workflows
- `integrations/external-apis.md` - Third-party integrations
```

### Specification Dependency Management

#### Dependency Declaration Format
```markdown
# Service Dependencies

## Upstream Dependencies
- **User Service**: Provides authentication context
- **Configuration Service**: Provides feature flags and settings
- **Audit Service**: Receives all state change events

## Downstream Consumers  
- **Mobile App**: Consumes REST API
- **Web Dashboard**: Consumes GraphQL API
- **Analytics Pipeline**: Consumes event stream

## Specification References
- User authentication: [../user-service/auth-spec.md](../user-service/auth-spec.md)
- Event schema: [../common/event-schema.md](../common/event-schema.md)
```

### Performance Monitoring in Specifications

Include performance requirements and monitoring strategies:

```markdown
# Performance Specifications

## Service Level Objectives (SLOs)
- **Availability**: 99.9% uptime (8.76 hours downtime/year)
- **Latency**: P95 < 200ms for API calls
- **Throughput**: Handle 1000 requests/second sustained

## Performance Testing Requirements
- [ ] Load testing with realistic data volumes
- [ ] Stress testing to identify breaking points  
- [ ] Chaos engineering for resilience validation

## Monitoring Implementation
- **Metrics**: Response time, error rate, throughput
- **Alerting**: SLO breach notifications
- **Dashboards**: Real-time performance visibility
```

## Advanced AI Integration Techniques

### Prompt Engineering for Complex Specs

#### Context Injection Strategies
```markdown
# AI Context Template

## System Context
**Architecture Style:** [Microservices, Monolith, Serverless]
**Technology Stack:** [Languages, frameworks, databases]
**Deployment Environment:** [Cloud provider, container orchestration]
**Team Preferences:** [Coding standards, testing approaches]

## Business Context  
**Industry:** [Domain-specific considerations]
**Scale:** [User base, data volume, geographic distribution]
**Compliance:** [Regulatory requirements, security standards]

## Implementation Preferences
**Code Style:** [Functional, OOP, specific patterns]
**Testing Strategy:** [Unit, integration, e2e preferences]
**Documentation Level:** [Minimal, comprehensive, auto-generated]
```

### Specification Validation with AI

Use AI agents to validate specification quality:

```markdown
# AI-Assisted Spec Review Checklist

## Completeness Review (Claude)
- [ ] All user stories have acceptance criteria
- [ ] Edge cases and error conditions covered
- [ ] Non-functional requirements specified
- [ ] Integration points documented

## Technical Review (GitHub Copilot)  
- [ ] Architecture supports requirements
- [ ] Technology choices justified
- [ ] Scalability considerations addressed
- [ ] Security implications covered

## Implementation Review (Cursor)
- [ ] Tasks are appropriately sized
- [ ] Dependencies clearly identified  
- [ ] Implementation order optimized
- [ ] Testing strategy comprehensive
```

## Advanced Patterns and Anti-Patterns

### Specification Patterns

#### The Living Architecture Pattern
```markdown
# Architecture Evolution Strategy

## Current State (v1.0)
[Document current architecture]

## Planned Evolution (v2.0)  
[Describe next iteration]

## Migration Strategy
[Step-by-step evolution plan]

## Decision Points
[Criteria for architectural changes]
```

#### The Context Boundary Pattern
```markdown
# Service Context Definition

## What This Service Owns
- User profile data and validation
- Authentication and session management
- User preference storage and retrieval

## What This Service Does NOT Own
- Payment processing (owned by Payment Service)
- Order history (owned by Order Service)  
- Product catalog (owned by Catalog Service)

## Integration Contracts
[Define clear API boundaries and data ownership]
```

### Anti-Patterns to Avoid

#### The Mega-Spec Anti-Pattern
**Problem:** Single specification trying to cover entire system
**Solution:** Break into focused, cohesive specifications with clear boundaries

#### The Implementation Leak Anti-Pattern  
**Problem:** Specifications that dictate specific implementation details
**Solution:** Focus on requirements and interfaces, allow implementation flexibility

#### The Stale Spec Anti-Pattern
**Problem:** Specifications that become outdated as code evolves
**Solution:** Establish spec-code synchronization processes and tooling

## Next Steps for Mastery

### Advanced Resources
- [Multi-Agent Orchestration Guide](../how-to/multi-agent-workflows.md)
- [Legacy Integration Patterns](../how-to/legacy-integration.md)  
- [Performance Engineering Specs](../how-to/performance-specs.md)

### Community Contributions
- Share your advanced patterns and techniques
- Contribute to specification templates and examples
- Mentor other developers in advanced SDD practices

### Continuous Learning
- Stay updated with AI agent capabilities and limitations
- Experiment with new specification formats and tools
- Participate in SDD community discussions and case studies

Remember: Advanced SDD is about leveraging your experience to create specifications that not only guide implementation but also capture and transfer your architectural knowledge to both human and AI collaborators.