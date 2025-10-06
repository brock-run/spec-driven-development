# SDD Troubleshooting Guide

## Common Issues and Solutions

This guide addresses the most frequent problems teams encounter when implementing Spec-Driven Development and provides practical solutions.

## Specification Issues

### Problem: Vague or Ambiguous Requirements

**Symptoms:**
- AI generates code that doesn't match expectations
- Multiple interpretations of the same requirement
- Frequent back-and-forth during implementation

**Solutions:**

1. **Use EARS Format**: Structure requirements with specific triggers and responses
   ```markdown
   ❌ Bad: "The system should be fast"
   ✅ Good: "WHEN a user submits a search query THEN the system SHALL return results within 200ms"
   ```

2. **Add Concrete Examples**:
   ```markdown
   ## Example Scenarios
   - Input: User searches for "javascript tutorial"
   - Expected Output: List of 10 tutorials, sorted by relevance
   - Error Case: No results found → Display "No tutorials found" message
   ```

3. **Define Acceptance Criteria Clearly**:
   ```markdown
   #### Acceptance Criteria
   1. WHEN user enters valid email format THEN system SHALL accept the input
   2. WHEN user enters invalid email format THEN system SHALL display error "Please enter a valid email address"
   3. IF email is already registered THEN system SHALL display "Email already exists"
   ```

### Problem: Requirements Don't Match Implementation

**Symptoms:**
- Final code doesn't solve the original problem
- Features work differently than expected
- Missing edge cases in implementation

**Solutions:**

1. **Create Requirement Traceability Matrix**:
   ```markdown
   | Requirement ID | Description | Implementation Status | Test Coverage |
   |----------------|-------------|----------------------|---------------|
   | REQ-1.1 | User login validation | ✅ Complete | ✅ Covered |
   | REQ-1.2 | Password reset flow | 🔄 In Progress | ❌ Pending |
   ```

2. **Regular Spec Reviews**: Schedule weekly spec-to-code alignment checks

3. **Implement Acceptance Test-Driven Development**:
   ```markdown
   ## Acceptance Tests
   - [ ] Test user can log in with valid credentials
   - [ ] Test user cannot log in with invalid credentials
   - [ ] Test password reset email is sent
   - [ ] Test password reset link expires after 24 hours
   ```

### Problem: Specifications Are Too Technical or Too High-Level

**Symptoms:**
- Business stakeholders can't understand technical specs
- Developers can't implement from high-level requirements
- Disconnect between business needs and technical implementation

**Solutions:**

1. **Use Layered Specification Approach**:
   ```markdown
   # Business Layer (for stakeholders)
   As a customer, I want to save my payment information so that checkout is faster next time.

   # Functional Layer (for product managers)
   - System stores encrypted payment data
   - User can manage saved payment methods
   - Payment data expires after 2 years

   # Technical Layer (for developers)
   - Implement PCI-compliant tokenization
   - Use AES-256 encryption for stored data
   - Create payment_methods table with foreign key to users
   ```

2. **Create Multiple Views of Same Requirement**:
   - Business view: What value does this provide?
   - User view: How will users interact with this?
   - Technical view: How will this be implemented?

## AI Integration Issues

### Problem: AI Doesn't Understand Context

**Symptoms:**
- Generated code doesn't fit existing architecture
- AI suggests inappropriate technologies or patterns
- Implementation ignores project constraints

**Solutions:**

1. **Provide Comprehensive Context**:
   ```markdown
   ## Project Context
   - Technology stack: React, Node.js, PostgreSQL
   - Architecture pattern: Microservices with REST APIs
   - Existing conventions: Use TypeScript, follow ESLint rules
   - Performance requirements: Sub-200ms API responses
   - Security requirements: OWASP compliance, JWT authentication
   ```

2. **Include Architectural Decision Records (ADRs)**:
   ```markdown
   ## Architectural Decisions
   - ADR-001: Use PostgreSQL for primary data storage (not MongoDB)
   - ADR-002: Implement REST APIs (not GraphQL) for consistency
   - ADR-003: Use JWT tokens with 1-hour expiration
   ```

3. **Reference Existing Code Patterns**:
   ```markdown
   ## Code Style Examples
   Follow the pattern established in `src/services/UserService.ts`:
   - Use dependency injection for database connections
   - Implement error handling with custom error classes
   - Include comprehensive logging for debugging
   ```

### Problem: AI Generates Inconsistent Code

**Symptoms:**
- Different coding styles across components
- Inconsistent error handling patterns
- Mixed architectural approaches

**Solutions:**

1. **Create Style and Pattern Guidelines**:
   ```markdown
   ## Coding Standards
   - File naming: kebab-case for files, PascalCase for classes
   - Error handling: Always use custom error classes
   - Database queries: Use repository pattern with interfaces
   - API responses: Follow JSON:API specification
   ```

2. **Provide Code Templates**:
   ```typescript
   // Template for new service classes
   export class ExampleService {
     constructor(private repository: ExampleRepository) {}
     
     async create(data: CreateExampleDto): Promise<Example> {
       try {
         return await this.repository.create(data);
       } catch (error) {
         throw new ServiceError('Failed to create example', error);
       }
     }
   }
   ```

3. **Use Linting and Formatting Rules**:
   ```json
   // Include in spec: "Follow existing .eslintrc.json and .prettierrc rules"
   {
     "extends": ["@typescript-eslint/recommended"],
     "rules": {
       "no-console": "error",
       "prefer-const": "error"
     }
   }
   ```

### Problem: AI Misses Edge Cases

**Symptoms:**
- Code works for happy path but fails on edge cases
- Missing error handling for unusual inputs
- Security vulnerabilities in generated code

**Solutions:**

1. **Explicitly List Edge Cases in Specs**:
   ```markdown
   ## Edge Cases to Handle
   - Empty input strings
   - Null or undefined values
   - Network timeouts and connection failures
   - Database constraint violations
   - Concurrent access scenarios
   - Input validation failures
   ```

2. **Include Security Requirements**:
   ```markdown
   ## Security Considerations
   - Validate all user inputs against injection attacks
   - Implement rate limiting for API endpoints
   - Use parameterized queries for database access
   - Sanitize output to prevent XSS attacks
   ```

3. **Specify Error Handling Patterns**:
   ```markdown
   ## Error Handling Requirements
   - All functions must handle and log errors appropriately
   - User-facing errors should not expose internal details
   - System errors should be logged with correlation IDs
   - Failed operations should be retryable where appropriate
   ```

## Task Management Issues

### Problem: Tasks Are Too Large or Complex

**Symptoms:**
- Tasks take multiple days to complete
- Difficulty tracking progress
- High risk of scope creep

**Solutions:**

1. **Apply the 2-Hour Rule**: Break tasks into 2-hour maximum chunks
   ```markdown
   ❌ Bad: "Implement user authentication system"
   ✅ Good: 
   - [ ] Create User model with validation
   - [ ] Implement password hashing utility
   - [ ] Create login endpoint
   - [ ] Add JWT token generation
   - [ ] Implement token validation middleware
   ```

2. **Use Task Dependencies**:
   ```markdown
   - [ ] 1. Create database schema
   - [ ] 2. Implement User model (depends on #1)
   - [ ] 3. Create authentication service (depends on #2)
   - [ ] 4. Build login API endpoint (depends on #3)
   ```

3. **Define Clear Completion Criteria**:
   ```markdown
   - [ ] Create User model
     - Model includes email, password, createdAt fields
     - Validation ensures email format and password strength
     - Unit tests cover validation scenarios
     - Model is exported from models/index.ts
   ```

### Problem: Tasks Don't Build on Each Other

**Symptoms:**
- Orphaned code that doesn't integrate
- Rework needed to connect components
- Unclear implementation order

**Solutions:**

1. **Create Integration-Focused Task Sequence**:
   ```markdown
   - [ ] 1. Set up project structure and dependencies
   - [ ] 2. Create core interfaces and types
   - [ ] 3. Implement data layer (models, repositories)
   - [ ] 4. Build business logic layer (services)
   - [ ] 5. Create API layer (controllers, routes)
   - [ ] 6. Add authentication middleware
   - [ ] 7. Integrate all layers with error handling
   - [ ] 8. Add comprehensive testing
   ```

2. **Include Integration Tasks**:
   ```markdown
   - [ ] Wire UserService into AuthController
   - [ ] Connect AuthController to Express routes
   - [ ] Integrate authentication middleware with protected routes
   - [ ] Add error handling to complete request flow
   ```

## Team Collaboration Issues

### Problem: Multiple People Working on Same Spec

**Symptoms:**
- Conflicting changes to specifications
- Inconsistent understanding of requirements
- Merge conflicts in spec files

**Solutions:**

1. **Establish Spec Ownership**:
   ```markdown
   ## Specification Ownership
   - Spec Owner: [Name] - Final authority on requirements
   - Technical Lead: [Name] - Architecture and implementation guidance
   - Reviewers: [Names] - Must approve changes before implementation
   ```

2. **Use Branching Strategy for Specs**:
   ```bash
   # Create feature branch for spec changes
   git checkout -b feature/user-authentication-spec
   # Make spec changes
   git commit -m "Add user authentication specification"
   # Create PR for spec review before implementation
   ```

3. **Implement Spec Review Process**:
   ```markdown
   ## Spec Review Checklist
   - [ ] Requirements are clear and testable
   - [ ] Technical approach is feasible
   - [ ] Security considerations are addressed
   - [ ] Performance requirements are specified
   - [ ] Integration points are defined
   ```

### Problem: Specs Get Out of Sync with Code

**Symptoms:**
- Documentation doesn't match implementation
- New team members confused by outdated specs
- Specs become ignored over time

**Solutions:**

1. **Implement Living Documentation**:
   ```markdown
   ## Maintenance Schedule
   - Weekly: Review active specs for accuracy
   - Sprint End: Update specs based on implementation learnings
   - Release: Ensure specs match deployed functionality
   ```

2. **Link Specs to Code**:
   ```typescript
   /**
    * Implements user authentication as specified in:
    * docs/specs/user-authentication.md#login-endpoint
    */
   export class AuthController {
     // Implementation
   }
   ```

3. **Automate Spec Validation**:
   ```yaml
   # GitHub Action to check spec-code alignment
   name: Spec Validation
   on: [pull_request]
   jobs:
     validate-specs:
       runs-on: ubuntu-latest
       steps:
         - name: Check spec references in code
         - name: Validate API documentation matches implementation
         - name: Ensure all requirements have corresponding tests
   ```

## Tool-Specific Issues

### Problem: GitHub Spec Kit Integration Issues

**Symptoms:**
- Spec Kit commands don't work as expected
- Generated code doesn't follow project patterns
- Integration with existing workflow is clunky

**Solutions:**

1. **Configure Spec Kit for Your Project**:
   ```json
   // .speckit/config.json
   {
     "templates": {
       "spec": "custom-templates/spec.md",
       "plan": "custom-templates/plan.md"
     },
     "codeStyle": {
       "language": "typescript",
       "framework": "express",
       "testFramework": "jest"
     }
   }
   ```

2. **Create Custom Templates**:
   ```markdown
   # Custom Spec Template for Your Project
   ## Requirements
   [Your specific requirement format]
   
   ## Technical Constraints
   - Must use existing database schema
   - Follow established API patterns
   - Integrate with current authentication system
   ```

### Problem: Multiple AI Tools Give Different Suggestions

**Symptoms:**
- Conflicting implementation approaches from different AIs
- Inconsistent code quality across tools
- Confusion about which approach to follow

**Solutions:**

1. **Establish Tool Hierarchy**:
   ```markdown
   ## AI Tool Usage Guidelines
   - Primary: GitHub Copilot for code completion
   - Secondary: Claude for architecture review
   - Tertiary: ChatGPT for documentation generation
   - Final Authority: Human code review
   ```

2. **Create Consistent Prompting Strategy**:
   ```markdown
   ## Standard AI Prompt Template
   Context: [Project description and constraints]
   Current Task: [Specific task from spec]
   Requirements: [Relevant requirements from spec]
   Existing Code: [Link to related existing code]
   Expected Output: [What type of code/documentation needed]
   ```

## Performance and Quality Issues

### Problem: Generated Code Has Performance Issues

**Symptoms:**
- Slow API responses
- High memory usage
- Inefficient database queries

**Solutions:**

1. **Include Performance Requirements in Specs**:
   ```markdown
   ## Performance Requirements
   - API response time: < 200ms for 95% of requests
   - Database queries: Maximum 3 queries per API call
   - Memory usage: < 100MB per service instance
   - Concurrent users: Support 1000 simultaneous users
   ```

2. **Specify Performance Testing**:
   ```markdown
   ## Performance Testing Tasks
   - [ ] Load test with 100 concurrent users
   - [ ] Profile memory usage under normal load
   - [ ] Analyze database query performance
   - [ ] Test with large datasets (10k+ records)
   ```

### Problem: Code Quality Is Inconsistent

**Symptoms:**
- Some components well-tested, others not
- Inconsistent error handling
- Mixed code styles and patterns

**Solutions:**

1. **Define Quality Gates**:
   ```markdown
   ## Quality Requirements
   - Test coverage: Minimum 80% line coverage
   - Code review: All code must be reviewed by senior developer
   - Static analysis: Must pass ESLint and SonarQube checks
   - Documentation: All public APIs must be documented
   ```

2. **Implement Automated Quality Checks**:
   ```yaml
   # CI pipeline quality gates
   - name: Run tests
     run: npm test -- --coverage --threshold=80
   - name: Lint code
     run: npm run lint
   - name: Security scan
     run: npm audit --audit-level=moderate
   ```

## Getting Help

### When to Escalate Issues

- **Technical Blockers**: Architecture decisions that affect multiple teams
- **Requirement Conflicts**: Stakeholders disagree on specifications
- **Tool Limitations**: AI tools consistently produce inadequate results
- **Timeline Risks**: Spec-driven approach is taking longer than traditional methods

### Resources for Additional Support

- **Community Forums**: GitHub Discussions for this repository
- **Documentation**: Check [AI Integration Guide](ai-integration.md) for tool-specific help
- **Training Materials**: Review [Training Index](../training/index.md) for skill gaps
- **Expert Consultation**: Consider bringing in SDD specialists for complex scenarios

### Contributing Solutions

Found a solution not covered here? Please contribute:

1. **Document the Problem**: Clearly describe symptoms and context
2. **Provide Solution**: Include step-by-step resolution
3. **Add Examples**: Show before/after code or spec examples
4. **Test with Others**: Verify solution works in different contexts
5. **Submit PR**: Add to this troubleshooting guide

## Quick Reference

### Emergency Fixes

```bash
# Spec is too vague - add concrete examples
# AI output is wrong - provide more context
# Tasks are too big - break into 2-hour chunks
# Code doesn't integrate - add integration tasks
# Team conflicts - establish clear ownership
# Tools don't work - check configuration and templates
```

### Diagnostic Questions

When facing issues, ask:
1. Is the problem with the spec, the AI, or the process?
2. Can I reproduce this issue with a simpler example?
3. What context might the AI be missing?
4. Are my requirements specific and testable?
5. Do my tasks build incrementally toward the goal?

## Next Steps

- **Prevention**: Review [Getting Started Guide](getting-started.md) for best practices
- **Advanced Scenarios**: Check [Advanced Flows](advanced-flows.md) for complex patterns
- **Tool Optimization**: Read [AI Integration Guide](ai-integration.md) for better tool usage
- **Continuous Improvement**: Establish feedback loops to prevent recurring issues