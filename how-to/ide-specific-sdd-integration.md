# IDE-Specific SDD Integration Guide

## Overview

This guide provides comprehensive integration instructions for implementing Spec-Driven Development workflows across different Integrated Development Environments (IDEs). Each IDE offers unique features and capabilities that can enhance or streamline the SDD process.

## Kiro IDE - Native SDD Integration

Kiro IDE provides built-in, native support for Spec-Driven Development with a structured three-phase workflow.

### Setup and Configuration

#### Installation and Initial Setup
```bash
# Download and install Kiro IDE from official website
# Launch Kiro and create new project
```

#### Project Configuration
1. **Create New SDD Project**
   - File → New → Spec-Driven Project
   - Choose project template (web app, mobile, API, etc.)
   - Configure initial project settings

2. **Enable SDD Features**
   - Navigate to Settings → Features → Spec-Driven Development
   - Enable "Native SDD Workflow"
   - Configure AI agent integration (Claude, Copilot, etc.)

### Native SDD Workflow in Kiro

#### Phase 1: User Stories and Requirements
Kiro's native interface provides structured forms for requirement gathering:

**User Story Creation:**
```
Template in Kiro:
As a [user type]
I want [functionality]
So that [benefit/value]

Acceptance Criteria:
- [ ] Criterion 1 with measurable outcome
- [ ] Criterion 2 with specific behavior
- [ ] Criterion 3 with error handling
```

**Kiro-Specific Features:**
- **Visual User Journey Mapping:** Drag-and-drop interface for creating user flows
- **Requirement Traceability:** Automatic linking between user stories and implementation tasks
- **Stakeholder Review Mode:** Share-friendly view for non-technical stakeholders
- **AI-Assisted Refinement:** Built-in prompts to help refine vague requirements

#### Phase 2: Technical Design
Kiro provides structured technical design templates:

**Architecture Definition:**
- **Component Diagrams:** Visual architecture builder with drag-and-drop components
- **Data Flow Diagrams:** Interactive data flow visualization
- **Technology Stack Selection:** Guided selection with compatibility checking
- **Integration Points:** Visual API and service dependency mapping

**Design Documentation Features:**
- **Live Architecture Diagrams:** Auto-updating diagrams based on code structure
- **Constraint Validation:** Real-time checking of technical feasibility
- **Design Pattern Suggestions:** AI-powered recommendations for common patterns
- **Performance Modeling:** Built-in performance estimation tools

#### Phase 3: Implementation Tasks
Kiro's task management integrates directly with the development workflow:

**Task Generation:**
- **Automatic Task Breakdown:** AI-generated tasks from design specifications
- **Dependency Management:** Visual task dependency graphs
- **Effort Estimation:** AI-assisted time and complexity estimation
- **Progress Tracking:** Real-time progress visualization

**Implementation Features:**
- **Task-Driven Development:** IDE guides you through tasks in optimal order
- **Context-Aware Code Generation:** AI understands full project context
- **Requirement Validation:** Automatic checking of implementation against requirements
- **Live Documentation Updates:** Specifications update as code changes

### Kiro-Specific Best Practices

#### Leveraging Native Features
```yaml
Kiro Workflow Optimization:
  visual_specification:
    - Use drag-and-drop user journey builder for stakeholder reviews
    - Create interactive wireframes linked to user stories
    - Generate visual architecture diagrams from code structure
    
  ai_integration:
    - Enable full project context for AI suggestions
    - Use requirement-aware code generation
    - Leverage automatic documentation updates
    
  collaboration:
    - Share specifications in stakeholder-friendly formats
    - Use built-in review and approval workflows
    - Track changes with automatic version control
    
  quality_assurance:
    - Enable real-time requirement traceability checking
    - Use automated acceptance criteria validation
    - Implement live code-to-spec alignment monitoring
```

#### Advanced Kiro Workflows

**Multi-Stakeholder Collaboration:**
```
Kiro Collaboration Workflow:
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Product Manager │───▶│ Kiro Spec View  │◀───│ Engineering Lead│
│ Creates Stories │    │ Visual Review   │    │ Technical Input │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Stakeholder     │    │ Design Review   │    │ Implementation  │
│ Approval        │    │ Session         │    │ Planning        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

**Live Documentation Example:**
```typescript
// Code changes in Kiro automatically update specifications

// Before: Component has 2 props
interface UserProfileProps {
  userId: string;
  displayMode: 'compact' | 'full';
}

// Developer adds new prop
interface UserProfileProps {
  userId: string;
  displayMode: 'compact' | 'full';
  showAvatar: boolean; // New prop added
}

// Kiro automatically detects change and prompts:
// "Component UserProfile has been modified. Update specification?"
// ✅ Yes, update design document
// ❌ No, keep current spec
// 📝 Review changes first
```

#### Integration with External Tools
```json
{
  "kiro_integrations": {
    "version_control": {
      "provider": "git",
      "auto_commit_specs": true,
      "branch_strategy": "feature_branches"
    },
    "project_management": {
      "provider": "linear",
      "sync_tasks": true,
      "status_mapping": {
        "kiro_in_progress": "linear_in_progress",
        "kiro_review": "linear_in_review",
        "kiro_complete": "linear_done"
      }
    },
    "design_tools": {
      "provider": "figma",
      "import_wireframes": true,
      "sync_components": true
    },
    "deployment": {
      "provider": "vercel",
      "auto_deploy_on_complete": true,
      "environment_mapping": {
        "development": "preview",
        "staging": "staging",
        "production": "production"
      }
    }
  }
}
```

#### Kiro Screenshot Workflow Examples

**Visual User Story Creation:**
```
Kiro User Story Builder Interface:
┌─────────────────────────────────────────────────────────────┐
│ 📝 User Story Builder                                       │
├─────────────────────────────────────────────────────────────┤
│ Story ID: US001                    Priority: High ▼         │
│                                                             │
│ 👤 User Type: [Small Business Owner          ▼]            │
│ 🎯 Action: [Track business expenses efficiently]            │
│ 💡 Benefit: [Simplify tax preparation and budgeting]       │
│                                                             │
│ ✅ Acceptance Criteria:                                     │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ ☐ Can photograph receipts with phone camera            │ │
│ │ ☐ OCR extracts vendor, amount, date automatically      │ │
│ │ ☐ Expenses categorized for tax purposes                │ │
│ │ ☐ Generate monthly expense reports                     │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ 🔗 Related Stories: [US002: Receipt Management]            │
│                                                             │
│ [💾 Save Story]  [👁️ Preview]  [🔄 Generate Tasks]        │
└─────────────────────────────────────────────────────────────┘
```

**Interactive Architecture Designer:**
```
Kiro Architecture Builder:
┌─────────────────────────────────────────────────────────────┐
│ 🏗️ System Architecture Designer                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📱 Mobile App     🔄 API Gateway     🗄️ Database          │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐       │
│  │ React Native│──▶│ Express.js  │──▶│ PostgreSQL  │       │
│  │             │   │             │   │             │       │
│  │ • Camera    │   │ • Auth      │   │ • Users     │       │
│  │ • OCR       │   │ • Expenses  │   │ • Expenses  │       │
│  │ • Offline   │   │ • Reports   │   │ • Categories│       │
│  └─────────────┘   └─────────────┘   └─────────────┘       │
│         │                   │                   │           │
│         ▼                   ▼                   ▼           │
│  ☁️ Cloud Storage    🔍 OCR Service     📊 Analytics        │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐       │
│  │ AWS S3      │   │ Google ML   │   │ Mixpanel    │       │
│  └─────────────┘   └─────────────┘   └─────────────┘       │
│                                                             │
│ 🎨 Drag components from palette to build architecture       │
│ 🔗 Click connections to define data flow and APIs          │
│ ⚙️ Right-click components to configure properties          │
│                                                             │
│ [💾 Save Design]  [🧪 Validate]  [📋 Generate Tasks]      │
└─────────────────────────────────────────────────────────────┘
```

**Task Management Dashboard:**
```
Kiro Task Dashboard:
┌─────────────────────────────────────────────────────────────┐
│ 📋 Implementation Tasks - Expense Tracker                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ 🏃‍♂️ In Progress (2)        ⏳ Todo (8)        ✅ Done (3)    │
│                                                             │
│ ┌─────────────────────┐  ┌─────────────────────┐           │
│ │ 🔄 T004: OCR Service│  │ ⭐ T006: User Auth  │           │
│ │ Assigned: @alice    │  │ Priority: High      │           │
│ │ Due: Tomorrow       │  │ Estimate: 6h        │           │
│ │ Progress: 60%       │  │ Depends: T003       │           │
│ │ [View Details]      │  │ [Start Task]        │           │
│ └─────────────────────┘  └─────────────────────┘           │
│                                                             │
│ ┌─────────────────────┐  ┌─────────────────────┐           │
│ │ 🔄 T005: Database   │  │ ⏳ T007: API Tests  │           │
│ │ Assigned: @bob      │  │ Priority: Medium    │           │
│ │ Due: Friday         │  │ Estimate: 4h        │           │
│ │ Progress: 30%       │  │ Depends: T006       │           │
│ │ [View Details]      │  │ [Schedule]          │           │
│ └─────────────────────┘  └─────────────────────┘           │
│                                                             │
│ 📊 Sprint Progress: 45% complete (5 of 11 tasks)           │
│ 🎯 On track for Friday delivery                            │
│                                                             │
│ [📈 View Analytics]  [🔄 Sync with Linear]  [📝 Add Task] │
└─────────────────────────────────────────────────────────────┘
```

## Cursor IDE - AI Pair Programming with SDD

Cursor IDE excels at AI-powered pair programming and can be optimized for SDD workflows.

### Setup and Configuration

#### Installation and AI Setup
```bash
# Download Cursor IDE
# Configure AI models (GPT-4, Claude, etc.)
# Set up codebase indexing for context awareness
```

#### SDD Workflow Configuration
1. **Create SDD Project Structure**
   ```
   project/
   ├── specs/
   │   ├── requirements.md
   │   ├── design.md
   │   └── tasks.md
   ├── docs/
   └── src/
   ```

2. **Configure AI Context**
   - Add `.cursorrules` file with SDD guidelines
   - Set up project-specific AI instructions
   - Configure codebase indexing for full context awareness

### SDD Workflow in Cursor

#### Specification Creation with AI Assistance
**Requirements Gathering:**
```markdown
<!-- In requirements.md -->
# Project Requirements

## User Stories
<!-- Use Cursor's AI to expand and refine user stories -->
@cursor: Help me refine this user story with specific acceptance criteria:
"As a user, I want to manage my tasks efficiently"
```

**AI-Enhanced Design Process:**
```markdown
<!-- In design.md -->
# Technical Design

## Architecture Overview
<!-- Use Cursor's AI for architecture suggestions -->
@cursor: Based on the requirements in requirements.md, suggest a scalable 
architecture for a task management application using React and Node.js
```

#### Implementation with Spec Awareness
**Context-Aware Development:**
```typescript
// Cursor AI understands full project context
// Reference specs directly in code comments

/**
 * Task Management Component
 * Implements requirements from specs/requirements.md - User Story US001
 * Follows design patterns from specs/design.md - Section 3.2
 */
export const TaskManager: React.FC = () => {
  // Cursor AI generates implementation based on specs
};
```

### Cursor-Specific Features for SDD

#### AI Pair Programming Optimization
- **Spec-Aware Code Generation:** AI references specification documents
- **Requirement Traceability:** Comments link code to specific requirements
- **Design Pattern Enforcement:** AI suggests patterns from design documents
- **Cross-File Context:** AI understands relationships between specs and code

#### Advanced Cursor Techniques
```typescript
// Use Cursor's multi-file editing for spec-driven refactoring
// Select multiple files: specs/design.md, src/components/TaskList.tsx
// Ask AI to refactor based on updated design specifications

// Leverage Cursor's codebase chat for spec validation
// @codebase: Does the current TaskList implementation satisfy 
// the requirements in specs/requirements.md section 2.1?
```

## Claude Code - Spec-to-Implementation Workflows

Claude Code (via Claude.ai or API) provides powerful reasoning capabilities for SDD workflows.

### Setup and Integration

#### Project Structure for Claude
```
project/
├── .claude/
│   ├── project-context.md
│   └── sdd-instructions.md
├── specs/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
└── src/
```

#### Claude-Specific Configuration
Create `.claude/sdd-instructions.md`:
```markdown
# SDD Instructions for Claude

## Project Context
This project follows Spec-Driven Development methodology.

## Workflow Rules
1. Always reference specification documents before generating code
2. Ensure implementation matches acceptance criteria
3. Maintain traceability between specs and implementation
4. Follow design patterns specified in design.md

## File References
- Requirements: specs/requirements.md
- Design: specs/design.md
- Tasks: specs/tasks.md
```

### SDD Workflow with Claude

#### Specification Development
**Iterative Requirement Refinement:**
```
Prompt: "Review the attached requirements.md file. Identify any vague 
or incomplete user stories and suggest specific, measurable acceptance 
criteria for each."
```

**Design Validation:**
```
Prompt: "Analyze the technical design in design.md against the 
requirements in requirements.md. Identify any gaps, inconsistencies, 
or missing components."
```

#### Implementation with Claude
**Spec-Driven Code Generation:**
```
Prompt: "Based on task T001 in tasks.md, implement the UserAuthentication 
component. Ensure it satisfies the acceptance criteria in requirements.md 
section 2.1 and follows the architecture patterns in design.md section 3."
```

**Quality Assurance:**
```
Prompt: "Review the attached implementation against the original 
specifications. Create a checklist to verify all requirements are met."
```

### Claude Best Practices for SDD

#### Effective Prompting Strategies
- **Context Loading:** Always provide relevant spec documents
- **Specific References:** Point to exact sections and requirements
- **Iterative Refinement:** Use Claude's reasoning for spec improvement
- **Cross-Validation:** Ask Claude to check consistency across documents

#### Advanced Claude Techniques
```
Multi-Document Analysis:
"Compare the implementation in UserService.ts with:
1. Requirements in specs/requirements.md (sections 2.1-2.3)
2. Design patterns in specs/design.md (section 4)
3. Task specifications in specs/tasks.md (tasks T001-T003)

Identify any deviations and suggest corrections."
```

## VS Code + Copilot - SDD Setup and Optimization

VS Code with GitHub Copilot can be optimized for effective SDD workflows.

### Setup and Configuration

#### Extension Installation
```bash
# Install essential extensions
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
code --install-extension ms-vscode.vscode-markdown
code --install-extension yzhang.markdown-all-in-one
```

#### Workspace Configuration
Create `.vscode/settings.json`:
```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": true,
    "plaintext": true,
    "markdown": true
  },
  "github.copilot.advanced": {
    "length": 500,
    "temperature": 0.1
  },
  "files.associations": {
    "*.md": "markdown"
  },
  "markdown.preview.breaks": true
}
```

#### SDD Workspace Setup
Create workspace structure:
```
.vscode/
├── settings.json
├── tasks.json
└── launch.json
specs/
├── requirements.md
├── design.md
└── tasks.md
docs/
└── sdd-guidelines.md
```

### SDD Workflow in VS Code

#### Specification Management
**Markdown-Based Specifications:**
```markdown
<!-- Use VS Code's markdown features for structured specs -->
# Requirements Document

## User Stories
- [ ] US001: User authentication
  - Acceptance Criteria:
    - [ ] AC001: Login with email/password
    - [ ] AC002: Password reset functionality
    - [ ] AC003: Session management
```

**Copilot-Enhanced Spec Writing:**
```markdown
<!-- Use Copilot suggestions for expanding specifications -->
## Technical Requirements
<!-- Type comment and let Copilot suggest technical details -->
// Based on the user authentication requirements above, the system needs:
```

#### Implementation with Spec Awareness
**Copilot Context Optimization:**
```typescript
/**
 * User Authentication Service
 * 
 * Implements requirements from specs/requirements.md:
 * - US001: User authentication with email/password
 * - US002: Password reset functionality
 * 
 * Follows design patterns from specs/design.md:
 * - Section 3.1: Service layer architecture
 * - Section 3.2: Error handling patterns
 */
export class AuthService {
  // Copilot generates implementation based on comments
}
```

### VS Code + Copilot Best Practices

#### Maximizing Copilot Effectiveness
- **Rich Comments:** Provide detailed context in code comments
- **Spec References:** Link code to specific requirements and design sections
- **Consistent Naming:** Use terminology from specifications
- **Structured Files:** Organize code to match specification structure

#### Advanced VS Code Techniques
```json
// .vscode/tasks.json - Automate SDD workflows
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Validate Specs",
      "type": "shell",
      "command": "markdownlint",
      "args": ["specs/*.md"],
      "group": "build"
    },
    {
      "label": "Generate Implementation Tasks",
      "type": "shell",
      "command": "node",
      "args": ["scripts/generate-tasks.js"],
      "group": "build"
    }
  ]
}
```

## IDE Capability Comparison Matrix

| Feature | Kiro IDE | Cursor IDE | Claude Code | VS Code + Copilot |
|---------|----------|------------|-------------|-------------------|
| **Native SDD Support** | ✅ Built-in | ⚠️ Manual setup | ⚠️ Manual setup | ⚠️ Manual setup |
| **Visual Spec Creation** | ✅ GUI forms | ❌ Text-based | ❌ Text-based | ⚠️ Extensions |
| **AI Context Awareness** | ✅ Full project | ✅ Codebase-wide | ✅ Multi-document | ⚠️ File-based |
| **Requirement Traceability** | ✅ Automatic | ⚠️ Manual linking | ⚠️ Manual tracking | ⚠️ Comment-based |
| **Live Documentation** | ✅ Auto-update | ❌ Manual sync | ❌ Manual sync | ❌ Manual sync |
| **Multi-Agent Support** | ✅ Built-in | ✅ Configurable | ✅ API-based | ⚠️ Extensions |
| **Collaboration Features** | ✅ Native sharing | ⚠️ Git-based | ⚠️ External tools | ⚠️ Extensions |
| **Learning Curve** | Low | Medium | Medium | Low |
| **Customization** | Medium | High | High | High |
| **Cost** | Paid | Paid | API costs | Free + Copilot |

## Choosing the Right IDE for Your SDD Workflow

### Decision Framework

#### For Teams New to SDD
**Recommended: Kiro IDE**
- Native SDD support reduces learning curve
- Visual tools help with stakeholder communication
- Built-in guidance for SDD best practices
- Integrated workflow minimizes tool switching

#### For Experienced Developers
**Recommended: Cursor IDE or VS Code + Copilot**
- Maximum flexibility and customization
- Integration with existing development workflows
- Advanced AI capabilities for complex projects
- Extensive ecosystem of extensions and tools

#### For AI-Heavy Workflows
**Recommended: Claude Code + Any IDE**
- Superior reasoning capabilities for complex specifications
- Excellent at cross-document analysis and validation
- Strong at identifying inconsistencies and gaps
- Can be integrated with any preferred IDE

#### For Enterprise Teams
**Recommended: VS Code + Copilot or Kiro IDE**
- VS Code: Mature ecosystem, extensive enterprise features
- Kiro IDE: Standardized SDD workflow, easier governance
- Both offer good security and compliance features
- Strong integration with enterprise development tools

### Migration Strategies

#### From Traditional Development to SDD
1. **Start with Familiar Tools:** Use existing IDE with SDD methodology
2. **Gradual Adoption:** Begin with simple specification documents
3. **Tool Enhancement:** Add SDD-specific extensions and configurations
4. **Team Training:** Invest in SDD methodology training
5. **Tool Migration:** Consider specialized SDD tools after team adoption

#### Between SDD-Enabled IDEs
1. **Specification Portability:** Ensure specs are in standard markdown format
2. **Workflow Mapping:** Document current SDD processes
3. **Tool-Specific Training:** Focus on new IDE's unique features
4. **Gradual Migration:** Migrate projects incrementally
5. **Process Optimization:** Refine SDD workflow for new tool capabilities

## Advanced Integration Patterns

### Multi-IDE Workflows
Some teams benefit from using different IDEs for different phases:

```yaml
SDD Phase Distribution:
  Requirements_Gathering:
    Primary: Kiro IDE (visual tools)
    Secondary: Claude Code (refinement)
  
  Technical_Design:
    Primary: Claude Code (reasoning)
    Secondary: Cursor IDE (architecture validation)
  
  Implementation:
    Primary: Cursor IDE or VS Code (development)
    Secondary: Claude Code (code review)
```

### Hybrid Approaches
```yaml
Team_Structure_Based:
  Product_Managers: Kiro IDE (visual specs)
  Senior_Engineers: Claude Code (architecture)
  Development_Team: Cursor IDE (implementation)
  
Tool_Strength_Based:
  Specification_Creation: Kiro IDE
  Code_Generation: Cursor IDE
  Quality_Assurance: Claude Code
  Maintenance: VS Code + Copilot
```

## Troubleshooting Common IDE Integration Issues

### Kiro IDE Issues

#### Issue: Specifications not syncing with implementation
**Solutions:**
- Verify SDD workflow is properly enabled
- Check AI agent configuration and connectivity
- Ensure project structure matches Kiro's expectations
- Review specification format for compatibility

#### Issue: AI suggestions not matching project context
**Solutions:**
- Rebuild project index in Kiro
- Verify all specification documents are complete
- Check AI model configuration and permissions
- Update project context and constraints

### Cursor IDE Issues

#### Issue: AI not understanding project specifications
**Solutions:**
- Ensure `.cursorrules` file includes SDD guidelines
- Add specification files to AI context
- Use explicit references to spec documents in prompts
- Verify codebase indexing is complete and up-to-date

#### Issue: Code generation ignoring design patterns
**Solutions:**
- Include design patterns in code comments
- Reference specific design document sections
- Use consistent terminology from specifications
- Provide examples of desired patterns in context

### Claude Code Issues

#### Issue: Context limits with large specifications
**Solutions:**
- Break specifications into focused sections
- Use summary documents for large projects
- Prioritize most relevant context for current task
- Implement incremental specification review process

#### Issue: Inconsistent responses across sessions
**Solutions:**
- Maintain consistent project context documents
- Use structured prompts with clear references
- Document decisions and rationale for future sessions
- Create project-specific instruction templates

### VS Code + Copilot Issues

#### Issue: Copilot suggestions not aligned with specifications
**Solutions:**
- Add detailed comments referencing specifications
- Use consistent naming conventions from specs
- Structure code to match specification organization
- Regularly update comments with spec references

#### Issue: Limited context awareness across files
**Solutions:**
- Use workspace-level configuration for consistency
- Create shared utility files with spec-derived types
- Implement consistent commenting patterns
- Use VS Code's multi-file editing features

## Resources and Next Steps

### IDE-Specific Resources

#### Kiro IDE
- [Official Documentation](https://kiro.ai/docs)
- [SDD Workflow Tutorials](https://kiro.ai/tutorials/sdd)
- [Community Examples](https://github.com/kiro-ai/examples)

#### Cursor IDE
- [Cursor Documentation](https://cursor.sh/docs)
- [AI Pair Programming Guide](https://cursor.sh/ai-programming)
- [Community Patterns](https://github.com/getcursor/cursor-examples)

#### Claude Code
- [Claude API Documentation](https://docs.anthropic.com/claude/docs)
- [Best Practices Guide](https://docs.anthropic.com/claude/docs/best-practices)
- [Integration Examples](https://github.com/anthropics/anthropic-cookbook)

#### VS Code + Copilot
- [GitHub Copilot Documentation](https://docs.github.com/copilot)
- [VS Code Extension Development](https://code.visualstudio.com/api)
- [SDD Extension Examples](https://marketplace.visualstudio.com/search?term=spec-driven)

### Community and Support
- Join IDE-specific communities and forums
- Participate in SDD methodology discussions
- Share successful integration patterns
- Contribute to open-source SDD tooling projects