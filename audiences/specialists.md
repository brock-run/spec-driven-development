# Specialist Guide to Role-Specific SDD Patterns

## Adapting SDD to Specialized Development Roles

Different development specializations require tailored approaches to Spec-Driven Development. This guide provides specific patterns, templates, and workflows for frontend developers, backend engineers, QA professionals, and designers working within SDD methodologies.

## Frontend Developer SDD Patterns

### Frontend-Specific Specification Structure

#### Component-Driven Requirements
```markdown
# Frontend Component Specification Template

## Component Overview
**Component Name:** [UserProfileCard]
**Component Type:** [Presentational/Container/Page]
**Design System:** [Reference to design system component]
**Accessibility Level:** [WCAG 2.1 AA compliance required]

## User Interface Requirements

### Requirement 1: Visual Presentation
**User Story:** As a user, I want to see my profile information in a clear, scannable format, so that I can quickly review and identify what needs updating.

#### Acceptance Criteria
1. WHEN the component loads THEN it SHALL display user avatar, name, email, and last login
2. WHEN user data is loading THEN the component SHALL show skeleton placeholders
3. WHEN user data fails to load THEN the component SHALL display a friendly error message with retry option
4. IF the user has no avatar THEN the component SHALL display initials in a colored circle
5. WHEN viewed on mobile THEN the component SHALL stack elements vertically and maintain readability

### Requirement 2: Interactive Behavior
**User Story:** As a user, I want to interact with my profile card to access editing functions, so that I can quickly update my information.

#### Acceptance Criteria
1. WHEN I hover over the profile card THEN it SHALL show an edit button overlay
2. WHEN I click the edit button THEN it SHALL navigate to the profile editing page
3. WHEN I press Tab THEN focus SHALL move logically through interactive elements
4. WHEN I press Enter on the edit button THEN it SHALL activate the edit action
5. IF I'm using a screen reader THEN all elements SHALL have appropriate ARIA labels

## Technical Specifications

### Component Architecture
**Framework:** [React/Vue/Angular/Vanilla]
**State Management:** [Local state/Redux/Vuex/Context]
**Styling Approach:** [CSS Modules/Styled Components/Tailwind]
**Testing Strategy:** [Jest + Testing Library/Cypress/Playwright]

### Props Interface
```typescript
interface UserProfileCardProps {
  user: {
    id: string;
    name: string;
    email: string;
    avatar?: string;
    lastLogin: Date;
  };
  onEdit: () => void;
  loading?: boolean;
  error?: string;
}
```

### Responsive Design Requirements
- **Mobile (320-768px):** Single column layout, touch-friendly buttons
- **Tablet (768-1024px):** Compact horizontal layout
- **Desktop (1024px+):** Full horizontal layout with hover states

## Performance Requirements
- **Initial Render:** < 100ms for component mount
- **Image Loading:** Progressive loading with placeholders
- **Bundle Size:** < 5KB gzipped for component and dependencies
- **Accessibility:** 100% keyboard navigable, screen reader compatible
```

#### State Management Specifications
```markdown
# Frontend State Management Specification

## State Architecture Requirements

### Requirement 1: Predictable State Updates
**User Story:** As a developer, I want predictable state management, so that I can debug issues and maintain code effectively.

#### Acceptance Criteria
1. WHEN state changes occur THEN they SHALL follow unidirectional data flow
2. WHEN debugging THEN all state changes SHALL be traceable through dev tools
3. WHEN testing THEN state changes SHALL be deterministic and repeatable
4. IF state becomes corrupted THEN the application SHALL recover gracefully

### State Schema Design
```typescript
interface AppState {
  user: {
    profile: UserProfile | null;
    preferences: UserPreferences;
    loading: boolean;
    error: string | null;
  };
  ui: {
    theme: 'light' | 'dark';
    sidebarOpen: boolean;
    notifications: Notification[];
  };
  data: {
    cache: Record<string, CacheEntry>;
    lastUpdated: Record<string, Date>;
  };
}
```

### Action Specifications
```typescript
// User Actions
type UserActions = 
  | { type: 'USER_LOAD_START' }
  | { type: 'USER_LOAD_SUCCESS'; payload: UserProfile }
  | { type: 'USER_LOAD_ERROR'; payload: string }
  | { type: 'USER_UPDATE'; payload: Partial<UserProfile> };

// Each action must include:
// - Clear intent and naming
// - Type safety with TypeScript
// - Payload validation
// - Error handling strategy
```
```

### Frontend Testing Specifications
```markdown
# Frontend Testing Strategy Specification

## Testing Requirements

### Requirement 1: Component Testing
**User Story:** As a developer, I want comprehensive component tests, so that I can refactor with confidence and catch regressions early.

#### Acceptance Criteria
1. WHEN components render THEN they SHALL match approved snapshots
2. WHEN user interactions occur THEN they SHALL trigger expected state changes
3. WHEN props change THEN components SHALL update appropriately
4. IF errors occur THEN components SHALL handle them gracefully
5. WHEN accessibility features are used THEN they SHALL work as expected

### Testing Implementation Plan
```javascript
// Component Test Structure
describe('UserProfileCard', () => {
  describe('Rendering', () => {
    it('displays user information correctly');
    it('shows loading state when data is loading');
    it('displays error message when loading fails');
    it('renders accessibility attributes correctly');
  });

  describe('Interactions', () => {
    it('calls onEdit when edit button is clicked');
    it('handles keyboard navigation properly');
    it('supports screen reader interactions');
  });

  describe('Responsive Behavior', () => {
    it('adapts layout for mobile screens');
    it('shows appropriate touch targets on mobile');
    it('maintains usability across breakpoints');
  });
});
```

### Integration Testing Requirements
- **API Integration:** Mock API responses and test error handling
- **State Management:** Test state updates and side effects
- **Routing:** Test navigation and URL state synchronization
- **Performance:** Test bundle size and render performance
```

## Backend API-First Development Integration

### API Specification-Driven Backend Development

#### API Contract Specifications
```markdown
# Backend API Specification Template

## API Overview
**Service Name:** [UserManagementService]
**API Version:** [v1.0]
**Base URL:** [https://api.example.com/v1]
**Authentication:** [JWT Bearer Token]

## Endpoint Specifications

### Requirement 1: User Profile Retrieval
**User Story:** As a client application, I want to retrieve user profile data, so that I can display current user information.

#### Acceptance Criteria
1. WHEN I request GET /users/{id} with valid auth THEN I SHALL receive user profile data
2. WHEN I request with invalid user ID THEN I SHALL receive 404 with error details
3. WHEN I request without auth THEN I SHALL receive 401 with auth requirements
4. WHEN the user is deleted THEN I SHALL receive 410 with deletion timestamp
5. WHEN rate limits are exceeded THEN I SHALL receive 429 with retry information

### API Contract
```yaml
paths:
  /users/{userId}:
    get:
      summary: Retrieve user profile
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: User profile data
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserProfile'
        '404':
          description: User not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
```

### Data Model Specifications
```yaml
components:
  schemas:
    UserProfile:
      type: object
      required:
        - id
        - email
        - createdAt
      properties:
        id:
          type: string
          format: uuid
          description: Unique user identifier
        email:
          type: string
          format: email
          description: User's email address
        name:
          type: string
          maxLength: 100
          description: User's display name
        avatar:
          type: string
          format: uri
          description: URL to user's avatar image
        createdAt:
          type: string
          format: date-time
          description: Account creation timestamp
        lastLogin:
          type: string
          format: date-time
          description: Last successful login timestamp
```
```

#### Service Implementation Specifications
```markdown
# Backend Service Implementation Specification

## Service Architecture Requirements

### Requirement 1: Layered Service Architecture
**User Story:** As a developer, I want a clean service architecture, so that I can maintain and test the codebase effectively.

#### Acceptance Criteria
1. WHEN handling requests THEN the system SHALL separate concerns into distinct layers
2. WHEN business logic changes THEN it SHALL not affect data access or presentation layers
3. WHEN testing THEN each layer SHALL be testable in isolation
4. IF dependencies fail THEN the system SHALL handle errors gracefully at appropriate layers

### Layer Specifications

#### Controller Layer
```typescript
// API Controller Specification
@Controller('/users')
export class UserController {
  constructor(private userService: UserService) {}

  @Get('/:id')
  @UseGuards(AuthGuard)
  async getUser(@Param('id') id: string): Promise<UserProfileDto> {
    // Input validation
    // Service delegation
    // Response formatting
    // Error handling
  }
}
```

#### Service Layer
```typescript
// Business Logic Service Specification
@Injectable()
export class UserService {
  constructor(
    private userRepository: UserRepository,
    private auditService: AuditService
  ) {}

  async getUserProfile(id: string): Promise<UserProfile> {
    // Business rule validation
    // Data retrieval coordination
    // Business logic application
    // Audit logging
  }
}
```

#### Repository Layer
```typescript
// Data Access Repository Specification
@Injectable()
export class UserRepository {
  constructor(private database: Database) {}

  async findById(id: string): Promise<UserEntity | null> {
    // Query construction
    // Data mapping
    // Error handling
    // Performance optimization
  }
}
```

### Error Handling Specifications
```markdown
## Error Handling Requirements

### Requirement 1: Consistent Error Responses
**User Story:** As a client developer, I want consistent error responses, so that I can handle errors predictably.

#### Acceptance Criteria
1. WHEN errors occur THEN they SHALL follow RFC 7807 Problem Details format
2. WHEN validation fails THEN errors SHALL include field-specific details
3. WHEN system errors occur THEN they SHALL not expose internal details
4. WHEN rate limiting triggers THEN responses SHALL include retry guidance

### Error Response Schema
```json
{
  "type": "https://api.example.com/errors/validation-failed",
  "title": "Validation Failed",
  "status": 400,
  "detail": "The request body contains invalid data",
  "instance": "/users/12345",
  "errors": [
    {
      "field": "email",
      "code": "invalid_format",
      "message": "Email must be a valid email address"
    }
  ]
}
```
```
```

## QA Test-Spec Synchronization

### Test Strategy Alignment with Specifications

#### Specification-Driven Test Planning
```markdown
# QA Test Specification Template

## Test Strategy Overview
**Feature:** [User Profile Management]
**Specification Reference:** [requirements.md, design.md]
**Test Scope:** [Functional, Integration, Performance, Security]
**Test Environment:** [Staging, Production-like]

## Requirement Traceability Matrix

| Requirement ID | Acceptance Criteria | Test Cases | Test Type | Priority |
|----------------|-------------------|------------|-----------|----------|
| REQ-1.1 | User can view profile | TC-001, TC-002 | Functional | P0 |
| REQ-1.2 | Profile loads within 2s | TC-003 | Performance | P1 |
| REQ-1.3 | Error handling works | TC-004, TC-005 | Functional | P0 |

## Test Case Specifications

### Test Case TC-001: Successful Profile Display
**Requirement:** REQ-1.1 - WHEN user accesses profile THEN system SHALL display current information
**Preconditions:** 
- User is authenticated
- User has complete profile data
**Test Steps:**
1. Navigate to profile page
2. Verify all profile fields are displayed
3. Verify data accuracy against database
4. Verify responsive layout on different screen sizes
**Expected Results:**
- All profile information displays correctly
- Layout adapts to screen size
- No console errors or warnings
**Acceptance Criteria Validation:**
- ✓ Profile information is visible
- ✓ Data matches user record
- ✓ Responsive design works
```

#### Automated Test Implementation
```markdown
# Automated Test Specification

## Test Automation Requirements

### Requirement 1: Comprehensive Test Coverage
**User Story:** As a QA engineer, I want automated tests that validate all acceptance criteria, so that I can ensure consistent quality and catch regressions.

#### Acceptance Criteria
1. WHEN specifications change THEN automated tests SHALL be updated accordingly
2. WHEN tests run THEN they SHALL validate all acceptance criteria from specifications
3. WHEN tests fail THEN they SHALL provide clear diagnostic information
4. IF tests pass THEN the feature SHALL meet all specified requirements

### Test Implementation Strategy
```javascript
// Specification-Driven Test Structure
describe('User Profile Management - REQ-1', () => {
  describe('Profile Display - REQ-1.1', () => {
    it('displays user information when authenticated', async () => {
      // Test implementation validating acceptance criteria
      // Direct mapping to specification requirements
    });
    
    it('handles missing profile data gracefully', async () => {
      // Edge case testing from specification
    });
  });

  describe('Performance Requirements - REQ-1.2', () => {
    it('loads profile within 2 seconds', async () => {
      // Performance validation from non-functional requirements
    });
  });
});
```

### Test Data Management
```yaml
# Test Data Specification
test_scenarios:
  valid_user_profile:
    user_id: "test-user-001"
    name: "Test User"
    email: "test@example.com"
    avatar: "https://example.com/avatar.jpg"
    created_at: "2025-01-01T00:00:00Z"
    
  incomplete_user_profile:
    user_id: "test-user-002"
    email: "incomplete@example.com"
    # Missing name and avatar to test edge cases
    
  performance_test_user:
    user_id: "perf-user-001"
    # Large profile data for performance testing
```
```

### Quality Gates Integration
```markdown
# Quality Gates Specification

## Quality Gate Requirements

### Requirement 1: Specification Compliance Validation
**User Story:** As a team lead, I want automated quality gates that ensure delivered features match specifications, so that we maintain consistent quality standards.

#### Acceptance Criteria
1. WHEN code is committed THEN automated tests SHALL validate specification compliance
2. WHEN tests fail THEN deployment SHALL be blocked until issues are resolved
3. WHEN specifications change THEN quality gates SHALL be updated to match
4. IF quality gates pass THEN the feature SHALL be ready for stakeholder review

### Quality Gate Implementation
```yaml
# CI/CD Quality Gates Configuration
quality_gates:
  specification_compliance:
    - requirement_traceability_check
    - acceptance_criteria_validation
    - test_coverage_minimum_80_percent
    
  functional_validation:
    - all_automated_tests_pass
    - integration_tests_pass
    - performance_benchmarks_met
    
  code_quality:
    - static_analysis_passes
    - security_scan_clean
    - accessibility_compliance_verified
```
```

## Designer Workflow Integration

### Design-to-Specification Workflow

#### Design System Integration
```markdown
# Design-Specification Integration Template

## Design Requirements Specification

### Requirement 1: Design System Consistency
**User Story:** As a user, I want a consistent visual experience across the application, so that I can navigate and use features intuitively.

#### Acceptance Criteria
1. WHEN components are implemented THEN they SHALL use approved design system tokens
2. WHEN new components are created THEN they SHALL extend existing design patterns
3. WHEN responsive breakpoints are reached THEN layouts SHALL follow design system guidelines
4. IF design system updates occur THEN components SHALL be updated to maintain consistency

### Design Token Specifications
```css
/* Design System Token Integration */
:root {
  /* Colors from design system */
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-success: #28a745;
  --color-error: #dc3545;
  
  /* Typography from design system */
  --font-family-primary: 'Inter', sans-serif;
  --font-size-base: 16px;
  --line-height-base: 1.5;
  
  /* Spacing from design system */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
}
```

### Component Design Specifications
```markdown
## Component Design Requirements

### Visual Design Specifications
**Component:** UserProfileCard
**Design Reference:** [Figma link or design system reference]
**Accessibility:** WCAG 2.1 AA compliant

#### Visual Requirements
1. **Layout:** Card container with 16px padding, 8px border radius
2. **Typography:** Primary text uses --font-size-base, secondary uses --font-size-sm
3. **Colors:** Background uses --color-surface, text uses --color-on-surface
4. **Spacing:** Elements separated by --spacing-md vertically
5. **States:** Hover state increases elevation, focus state shows outline

#### Interaction Design
1. **Hover:** Subtle elevation increase (2px shadow)
2. **Focus:** 2px solid outline in --color-primary
3. **Active:** Slight scale reduction (0.98 transform)
4. **Loading:** Skeleton animation with shimmer effect
5. **Error:** Red border with error icon and message

### Design Validation Checklist
- [ ] Matches approved design mockups
- [ ] Uses design system tokens consistently
- [ ] Responsive behavior follows design guidelines
- [ ] Accessibility requirements met
- [ ] Interactive states implemented correctly
```
```

#### Design-Development Handoff Process
```markdown
# Design-Development Handoff Specification

## Handoff Requirements

### Requirement 1: Complete Design Specifications
**User Story:** As a developer, I want complete design specifications, so that I can implement features accurately without multiple clarification rounds.

#### Acceptance Criteria
1. WHEN designs are handed off THEN they SHALL include all interactive states
2. WHEN responsive designs are provided THEN they SHALL cover all target breakpoints
3. WHEN accessibility requirements exist THEN they SHALL be clearly documented
4. IF design tokens are used THEN they SHALL be referenced in specifications

### Handoff Deliverables Checklist
- [ ] **Visual Design:** High-fidelity mockups for all states and breakpoints
- [ ] **Interaction Design:** Detailed interaction specifications and animations
- [ ] **Design Tokens:** CSS custom properties or design system references
- [ ] **Accessibility:** ARIA labels, focus management, and keyboard navigation
- [ ] **Content Guidelines:** Copy, alt text, and content structure requirements

### Design Review Process
```markdown
## Design Review Workflow

### Phase 1: Design Specification Review
**Participants:** Designer, PM, Tech Lead
**Duration:** 2 days
**Deliverable:** Approved design specification

### Phase 2: Technical Feasibility Review
**Participants:** Designer, Frontend Developer, QA
**Duration:** 1 day  
**Deliverable:** Implementation plan with any design adjustments

### Phase 3: Implementation Review
**Participants:** Designer, Developer
**Duration:** Ongoing during implementation
**Deliverable:** Pixel-perfect implementation matching specifications
```
```

## Cross-Role Integration Patterns

### Collaborative Specification Creation

#### Multi-Disciplinary Specification Workshops
```markdown
# Cross-Role Specification Workshop Template

## Workshop Structure (2-hour session)

### Phase 1: Requirement Alignment (30 minutes)
**Participants:** PM, Designer, Frontend Dev, Backend Dev, QA
**Activity:** Review and refine user stories and acceptance criteria
**Output:** Agreed-upon requirements with cross-functional input

### Phase 2: Technical Design (45 minutes)
**Participants:** All roles
**Activity:** Collaborative design of technical approach
**Output:** Architecture decisions with design and QA considerations

### Phase 3: Implementation Planning (30 minutes)
**Participants:** All roles
**Activity:** Break down work and identify dependencies
**Output:** Task list with role-specific responsibilities

### Phase 4: Quality Planning (15 minutes)
**Participants:** All roles
**Activity:** Define testing strategy and acceptance criteria
**Output:** Quality assurance plan with clear responsibilities

## Role-Specific Contributions

### Frontend Developer Input
- Component architecture and reusability considerations
- Performance implications and optimization strategies
- Accessibility implementation requirements
- Browser compatibility and responsive design constraints

### Backend Developer Input  
- API design and data modeling requirements
- Performance and scalability considerations
- Security and compliance requirements
- Integration complexity and dependencies

### Designer Input
- User experience flow and interaction design
- Visual design requirements and design system usage
- Accessibility and inclusive design considerations
- Content strategy and information architecture

### QA Input
- Testability requirements and edge case identification
- Performance and security testing considerations
- Cross-browser and device testing requirements
- Acceptance criteria validation and refinement
```

### Specification Maintenance Across Roles

#### Living Documentation Process
```markdown
# Cross-Role Specification Maintenance

## Maintenance Responsibilities

### Design Changes
**Owner:** Designer
**Process:** Update design specifications and notify development team
**Validation:** Design review with frontend developer and PM
**Documentation:** Update design system and component specifications

### Technical Changes
**Owner:** Tech Lead/Senior Developer
**Process:** Assess impact on specifications and update accordingly
**Validation:** Technical review with team and stakeholder notification
**Documentation:** Update architecture and implementation specifications

### Requirement Changes
**Owner:** Product Manager
**Process:** Stakeholder alignment and specification update
**Validation:** Cross-functional review and approval
**Documentation:** Update requirements and trace through to implementation

### Quality Changes
**Owner:** QA Lead
**Process:** Update test specifications and quality gates
**Validation:** Test strategy review with development team
**Documentation:** Update testing documentation and automation
```

## Next Steps for Specialists

### Advanced Specialization Resources
- [Frontend Performance Optimization with SDD](../how-to/frontend-performance-sdd.md)
- [API-First Backend Development](../how-to/api-first-backend.md)
- [Advanced QA Automation Strategies](../how-to/qa-automation-sdd.md)
- [Design System Integration Patterns](../how-to/design-system-sdd.md)

### Cross-Role Collaboration
- Participate in cross-functional specification workshops
- Contribute role-specific templates and patterns to the community
- Mentor other specialists in SDD adoption within your domain
- Share success stories and lessons learned from specialist perspective

### Continuous Learning
- Stay updated with role-specific SDD tools and techniques
- Experiment with AI agents specialized for your domain
- Contribute to role-specific SDD pattern development
- Participate in specialist communities within the broader SDD ecosystem

Remember: Effective SDD requires each specialist to understand not just their own role, but how their work integrates with others. The best specifications emerge from collaborative effort where each discipline contributes their expertise while maintaining shared understanding and common goals.