# GitHub Spec Kit Integration Guide

## Overview

GitHub Spec Kit is an open-source command-line toolkit that operationalizes Spec-Driven Development (SDD) principles. This guide provides comprehensive setup, usage, and troubleshooting information for integrating Spec Kit into your development workflow.

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Git repository (local or remote)
- Access to an AI coding agent (GitHub Copilot, Claude, Gemini CLI, etc.)

### Installation Options

#### Option 1: One-time Use with uvx (Recommended)
```bash
# Install uv package manager if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Use Spec Kit without permanent installation
uvx specify-cli init my-project
```

#### Option 2: Persistent Installation
```bash
# Install globally with uv
uv tool install specify-cli

# Or install with pip
pip install specify-cli
```

### Project Initialization

1. **Create or navigate to your project directory:**
   ```bash
   mkdir my-sdd-project
   cd my-sdd-project
   ```

2. **Initialize Spec Kit structure:**
   ```bash
   specify init my-project
   ```

3. **Verify setup:**
   The initialization creates:
   - `.github/copilot-instructions.md` (for GitHub Copilot)
   - `CLAUDE.md` (for Claude)
   - Basic project structure with spec directories

## Slash Command Reference

Spec Kit operates through a series of slash commands that guide you through the SDD workflow. These commands are issued to your AI agent within the project terminal.

### /constitution - Establish Project Guardrails

**Purpose:** Define high-level principles and constraints that govern the entire project.

**Usage:**
```
/constitution
```

**What it creates:**
- `constitution.md` file with project-wide rules
- Code quality standards
- Testing requirements
- Security policies
- Performance guidelines

**Example constitution elements:**
- "All functions must include TypeScript type annotations"
- "API responses must include proper error handling"
- "UI components must be accessible (WCAG 2.1 AA)"
- "Database queries must use parameterized statements"

### /specify - Define Requirements and User Stories

**Purpose:** Articulate what the software should do and why, from the user's perspective.

**Usage:**
```
/specify [feature-name]
```

**Focus areas:**
- User journeys and workflows
- Functional requirements
- Success criteria
- Business value
- User experience goals

**Avoid in this phase:**
- Technical implementation details
- Technology stack decisions
- Architecture specifics

### /plan - Define Technical Architecture

**Purpose:** Bridge user requirements with technical implementation strategy.

**Usage:**
```
/plan
```

**Key elements to define:**
- Technology stack (e.g., "React with TypeScript")
- Data storage solutions (e.g., "PostgreSQL with Prisma ORM")
- Integration points and APIs
- Deployment strategy
- Security considerations
- Performance requirements

### /tasks - Create Implementation Roadmap

**Purpose:** Break down the plan into granular, actionable work items.

**Usage:**
```
/tasks
```

**Generated task characteristics:**
- Small, focused scope (2-4 hours each)
- Independently testable
- Clear acceptance criteria
- Logical dependency order
- Traceable to requirements

### /analyze - Validate Consistency

**Purpose:** Perform cross-artifact analysis to ensure alignment between spec, plan, and tasks.

**Usage:**
```
/analyze
```

**Validation checks:**
- Requirements coverage in tasks
- Technical feasibility assessment
- Dependency analysis
- Gap identification

### /implement - Execute the Plan

**Purpose:** Begin AI-driven implementation of the task list.

**Usage:**
```
/implement
```

**Implementation characteristics:**
- Interactive process requiring human oversight
- May pause for clarification or approvals
- Iterative refinement based on feedback
- Continuous validation against specifications

## Multi-Agent Compatibility

Spec Kit is designed to work with multiple AI coding agents. Here's how to configure each:

### GitHub Copilot

**Setup:**
1. Ensure GitHub Copilot CLI is installed
2. Spec Kit automatically creates `.github/copilot-instructions.md`
3. Use slash commands directly in terminal with Copilot

**Command format:**
```bash
gh copilot suggest "/constitution"
```

### Claude (Anthropic)

**Setup:**
1. Install Claude CLI or use Claude in supported IDEs
2. Spec Kit creates `CLAUDE.md` with instructions
3. Copy slash commands to Claude interface

**Best practices:**
- Provide full project context when switching conversations
- Use Claude's artifact feature for reviewing generated specs
- Leverage Claude's strong reasoning for complex architectural decisions

### Gemini CLI

**Setup:**
1. Install Google AI CLI tools
2. Configure API access
3. Use Spec Kit commands through Gemini interface

**Optimization tips:**
- Gemini excels at code analysis and optimization
- Use for /analyze phase validation
- Leverage multimodal capabilities for UI/UX specifications

### Cursor IDE

**Integration approach:**
1. Use Spec Kit to generate specification artifacts
2. Import specs into Cursor's AI chat
3. Use Cursor's codebase awareness for implementation

### VS Code + Extensions

**Workflow:**
1. Generate specs with Spec Kit CLI
2. Use VS Code AI extensions (Copilot, CodeGPT, etc.)
3. Reference spec files during implementation

## Troubleshooting Guide

### Common Setup Issues

#### Issue: "specify command not found"
**Solution:**
```bash
# Verify installation
which specify-cli

# Reinstall if necessary
uv tool install specify-cli --force

# Or use uvx for one-time execution
uvx specify-cli --help
```

#### Issue: AI agent not recognizing slash commands
**Solutions:**
1. Verify instruction files exist (`.github/copilot-instructions.md`, `CLAUDE.md`)
2. Restart AI agent session
3. Manually copy instruction content to AI chat

#### Issue: Permission errors during initialization
**Solution:**
```bash
# Check directory permissions
ls -la

# Create project in user directory
cd ~/projects
specify init my-project
```

### Workflow Issues

#### Issue: Specifications are too vague or generic
**Solutions:**
- Add more specific user stories and acceptance criteria
- Include concrete examples and edge cases
- Reference existing system constraints
- Use domain-specific terminology

#### Issue: Generated tasks are too large or complex
**Solutions:**
- Refine the /plan phase with more detailed architecture
- Add explicit constraints about task granularity
- Use /analyze to identify overly complex tasks
- Manually break down large tasks in the task list

#### Issue: AI agent produces inconsistent results
**Solutions:**
- Strengthen the constitution with clearer guidelines
- Provide more context in the specification
- Use /analyze frequently to catch inconsistencies early
- Maintain conversation context across sessions

### Performance and Cost Optimization

#### Token Usage Management
- Keep constitution concise but comprehensive
- Use bullet points and structured formats
- Reference external documentation rather than duplicating
- Archive old conversation threads to reduce context

#### Quality Improvement Strategies
- Iterate on specifications before implementation
- Use multiple AI agents for cross-validation
- Implement peer review for critical specifications
- Maintain a project glossary for consistent terminology

## Best Practices

### Specification Writing
1. **Start with user value:** Always begin with why the feature matters
2. **Be specific:** Use concrete examples and measurable criteria
3. **Consider edge cases:** Document error conditions and boundary scenarios
4. **Maintain traceability:** Link tasks back to specific requirements

### Architecture Planning
1. **Define constraints early:** Establish technical boundaries upfront
2. **Consider scalability:** Plan for growth and changing requirements
3. **Document decisions:** Explain architectural choices and trade-offs
4. **Validate feasibility:** Ensure technical approach aligns with team capabilities

### Implementation Management
1. **Review frequently:** Don't let AI run unsupervised for long periods
2. **Test incrementally:** Validate each task completion before proceeding
3. **Maintain quality:** Enforce constitution guidelines throughout
4. **Document changes:** Track deviations from original specifications

## Integration with Existing Workflows

### Git Integration
- Commit specification artifacts alongside code
- Use branches for experimental specifications
- Tag releases with corresponding spec versions
- Include spec updates in pull request reviews

### CI/CD Integration
- Validate spec format and completeness
- Check task completion against requirements
- Generate documentation from specifications
- Run automated tests based on acceptance criteria

### Team Collaboration
- Review specifications before implementation begins
- Use specs as basis for technical discussions
- Share context through specification artifacts
- Maintain living documentation that evolves with code

## Advanced Usage Patterns

### Legacy System Integration

#### Modernization with Spec Kit
```bash
# Initialize Spec Kit in existing project
cd legacy-project
specify init modernization-project

# Create constitution for legacy constraints
/constitution
```

**Legacy Integration Constitution Example:**
```markdown
# Legacy System Integration Constitution

## Existing System Constraints
- Must maintain compatibility with COBOL mainframe system
- Database schema cannot be modified (read-only access)
- All new APIs must use existing authentication system
- Performance cannot degrade existing batch processes

## Integration Patterns
- Use adapter pattern for legacy system interfaces
- Implement circuit breaker for mainframe calls
- Cache frequently accessed legacy data
- Provide fallback mechanisms for system unavailability

## Migration Strategy
- Phase 1: Read-only integration with legacy data
- Phase 2: Bidirectional sync for critical entities
- Phase 3: Gradual migration of business logic
- Phase 4: Legacy system retirement
```

#### Incremental Modernization Workflow
```bash
# Specify integration requirements
/specify legacy-user-sync

# Plan technical bridge architecture
/plan

# Create incremental migration tasks
/tasks
```

### Multi-Team Coordination

#### Shared Constitution Framework
```markdown
# Multi-Team Shared Constitution

## Cross-Team Standards
- All teams use TypeScript for type safety
- API contracts defined with OpenAPI 3.0
- Database migrations use Flyway versioning
- Error handling follows RFC 7807 Problem Details

## Team-Specific Sections
### Frontend Team
- React components use functional style with hooks
- State management with Redux Toolkit
- Testing with React Testing Library

### Backend Team  
- Microservices with Express.js framework
- Database access through repository pattern
- Authentication with JWT tokens

### DevOps Team
- Infrastructure as Code with Terraform
- CI/CD with GitHub Actions
- Monitoring with Prometheus and Grafana
```

#### Interface Specification Pattern
```bash
# Create API contract specifications
/specify user-service-api

# Define service boundaries
/plan

# Coordinate implementation tasks across teams
/tasks
```

**Cross-Team Task Coordination:**
```markdown
# Multi-Team Implementation Tasks

## Frontend Team Tasks
- [ ] FE001: Implement user profile component
  - Depends on: BE002 (User API endpoint)
  - Requirements: US001, US002
  - Estimated: 6 hours

## Backend Team Tasks  
- [ ] BE001: Set up user service infrastructure
  - Dependencies: None
  - Requirements: US001
  - Estimated: 4 hours

- [ ] BE002: Implement user CRUD API endpoints
  - Depends on: BE001
  - Requirements: US001, US002
  - Estimated: 8 hours

## DevOps Team Tasks
- [ ] DO001: Configure user service deployment
  - Depends on: BE001
  - Requirements: US001 (performance requirements)
  - Estimated: 3 hours
```

### Enterprise-Scale Patterns

#### Organization-Wide Constitution Template
```markdown
# Enterprise SDD Constitution Template

## Compliance Requirements
- SOC 2 Type II compliance for all customer data
- GDPR compliance for EU user data
- HIPAA compliance for healthcare integrations
- PCI DSS compliance for payment processing

## Security Standards
- All APIs require authentication and authorization
- Sensitive data encrypted at rest and in transit
- Regular security scanning and penetration testing
- Incident response procedures documented

## Performance Standards
- API response times under 200ms for 95% of requests
- System availability of 99.9% uptime
- Database queries optimized with proper indexing
- Caching strategy for frequently accessed data

## Quality Gates
- Minimum 80% code coverage for all services
- All code reviewed by senior developer
- Automated security scanning in CI pipeline
- Performance testing for all major releases
```

#### Specification Governance Process
```bash
# Enterprise spec review workflow
specify init enterprise-feature

# Create specification with governance checkpoints
/constitution  # Must align with enterprise standards
/specify      # Requires product owner approval
/plan         # Needs architecture review board approval
/tasks        # Requires technical lead sign-off
/implement    # Includes automated quality gates
```

### Continuous Improvement

#### Metrics Collection Framework
```javascript
// scripts/collect-sdd-metrics.js
class SDDMetrics {
  collectSpecificationQuality() {
    return {
      completeness: this.measureRequirementCoverage(),
      clarity: this.analyzeAcceptanceCriteria(),
      traceability: this.validateTaskLinkage(),
      consistency: this.checkTerminologyUsage()
    };
  }
  
  measureImplementationSuccess() {
    return {
      requirementsSatisfied: this.validateAcceptanceCriteria(),
      codeQuality: this.analyzeCodeMetrics(),
      testCoverage: this.measureTestCompleteness(),
      performanceMetrics: this.collectPerformanceData()
    };
  }
  
  trackProcessEfficiency() {
    return {
      specToCodeTime: this.measureDevelopmentVelocity(),
      reworkFrequency: this.trackSpecificationChanges(),
      defectRate: this.analyzePostReleaseIssues(),
      teamSatisfaction: this.collectDeveloperFeedback()
    };
  }
}
```

#### Automated Quality Assessment
```yaml
# .github/workflows/sdd-quality-check.yml
name: SDD Quality Assessment
on:
  pull_request:
    paths: ['specs/**', 'constitution.md']

jobs:
  validate-specifications:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate Spec Kit Format
        run: |
          uvx specify-cli validate specs/
          
      - name: Check Requirement Completeness
        run: |
          node scripts/validate-requirements.js
          
      - name: Analyze Specification Quality
        run: |
          node scripts/analyze-spec-quality.js
          
      - name: Generate Quality Report
        run: |
          node scripts/generate-quality-report.js
          
      - name: Comment PR with Results
        uses: actions/github-script@v6
        with:
          script: |
            const report = require('./quality-report.json');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## SDD Quality Report\n\n${report.summary}`
            });
```

#### Team-Specific Template Development
```bash
# Create reusable templates for common patterns
mkdir -p .specify/templates/

# E-commerce application template
cat > .specify/templates/ecommerce-constitution.md << 'EOF'
# E-commerce Application Constitution

## Business Rules
- All prices stored in cents to avoid floating point errors
- Inventory checks required before order confirmation
- Payment processing must be PCI DSS compliant
- Order status updates trigger customer notifications

## Technical Standards
- Product catalog uses search-optimized database
- Shopping cart state persists across sessions
- Payment integration uses secure tokenization
- Order processing follows saga pattern for consistency
EOF

# Microservice template
cat > .specify/templates/microservice-spec.md << 'EOF'
# Microservice Specification Template

## Service Responsibility
- Single business capability: [DEFINE_CAPABILITY]
- Data ownership: [DEFINE_DATA_OWNERSHIP]
- API contract: [DEFINE_API_CONTRACT]

## Integration Points
- Upstream dependencies: [LIST_DEPENDENCIES]
- Downstream consumers: [LIST_CONSUMERS]
- Event publishing: [DEFINE_EVENTS]
- Event subscriptions: [DEFINE_SUBSCRIPTIONS]

## Operational Requirements
- Health check endpoints: /health, /ready
- Metrics exposition: Prometheus format
- Logging: Structured JSON with correlation IDs
- Deployment: Blue-green with automated rollback
EOF
```

### Success Pattern Library

#### High-Quality Specification Examples
```markdown
# Example: Payment Processing Specification

## User Stories

### US001: Secure Payment Processing
**As a** customer making a purchase
**I want** to pay securely with my credit card
**So that** my financial information is protected and my order is processed

#### Acceptance Criteria
- WHEN customer enters valid payment information THEN payment is processed within 3 seconds
- WHEN payment processing fails THEN customer receives clear error message with retry option
- WHEN payment succeeds THEN customer receives confirmation email within 30 seconds
- IF payment information is invalid THEN system displays specific validation errors
- WHEN payment is processing THEN customer sees loading indicator and cannot submit again

### US002: Payment Method Management
**As a** returning customer
**I want** to save my payment methods securely
**So that** I can checkout faster on future purchases

#### Acceptance Criteria
- WHEN customer chooses to save payment method THEN card is tokenized and stored securely
- WHEN customer views saved payment methods THEN only last 4 digits are displayed
- WHEN customer deletes payment method THEN token is immediately invalidated
- IF customer has multiple saved methods THEN they can select preferred default
```

#### Effective Task Breakdown Example
```markdown
# Payment Processing Implementation Tasks

## Phase 1: Infrastructure Setup
- [ ] T001: Set up payment service infrastructure
  - Configure Stripe API integration
  - Set up secure environment variables
  - Create payment database schema
  - _Requirements: US001, US002_
  - _Estimated: 4 hours_

- [ ] T002: Implement payment tokenization
  - Create secure token generation service
  - Implement token validation middleware
  - Add token storage with encryption
  - _Requirements: US002_
  - _Estimated: 6 hours_

## Phase 2: Core Payment Logic
- [ ] T003: Build payment processing service
  - Implement Stripe payment intent creation
  - Add payment confirmation handling
  - Create payment status tracking
  - _Requirements: US001_
  - _Estimated: 8 hours_

- [ ] T004: Add payment method management
  - Create save payment method endpoint
  - Implement payment method listing
  - Add payment method deletion
  - _Requirements: US002_
  - _Estimated: 6 hours_

## Phase 3: Error Handling and Security
- [ ] T005: Implement comprehensive error handling
  - Add payment failure scenarios
  - Create user-friendly error messages
  - Implement retry mechanisms
  - _Requirements: US001_
  - _Estimated: 4 hours_

- [ ] T006: Add security measures
  - Implement rate limiting for payment attempts
  - Add fraud detection integration
  - Create audit logging for all payment events
  - _Requirements: US001, US002_
  - _Estimated: 6 hours_
```

## Next Steps

After mastering GitHub Spec Kit integration:

1. **Explore complementary tools:** ChatPRD for product requirements, MCP for multi-agent workflows
2. **Develop team standards:** Create organization-specific constitution templates
3. **Measure impact:** Track quality improvements and development velocity
4. **Contribute back:** Share successful patterns with the SDD community

## Resources

- [GitHub Spec Kit Repository](https://github.com/github/spec-kit)
- [Official Documentation](https://github.com/github/spec-kit/blob/main/README.md)
- [Community Examples](https://github.com/github/spec-kit/tree/main/examples)
- [Issue Tracker](https://github.com/github/spec-kit/issues)