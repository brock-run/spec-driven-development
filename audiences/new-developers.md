# New Developer Guide to Spec-Driven Development

## Welcome to SDD

If you're new to Spec-Driven Development (SDD), you're about to discover a methodology that transforms how you approach coding. Instead of diving straight into implementation ("vibe coding"), SDD helps you think through problems systematically, creating clear specifications that both humans and AI can understand.

## What is Spec-Driven Development?

Spec-Driven Development is a methodology where you write detailed specifications before implementing code. Think of it as creating a blueprint before building a house.

### SDD vs Other Approaches

**Vibe Coding** (Traditional approach):
- Start coding immediately based on rough ideas
- Figure out requirements as you go
- High chance of rework and missed edge cases
- Difficult for AI agents to provide meaningful assistance

**Test-Driven Development (TDD)**:
- Write tests first, then implement code to pass tests
- Focuses on behavior verification
- Great for ensuring code correctness

**Spec-Driven Development (SDD)**:
- Write comprehensive specifications first
- Define requirements, architecture, and implementation plan
- AI agents can understand and implement from clear specs
- Reduces rework and improves collaboration
- Includes TDD principles within the implementation phase

## Your First SDD Workflow

### Step 1: Write Requirements
Start by documenting what you're building and why. Use this structure:

```markdown
# Requirements Document

## Introduction
Brief overview of what you're building and its purpose.

## Requirements

### Requirement 1
**User Story:** As a [role], I want [feature], so that [benefit]

#### Acceptance Criteria
1. WHEN [event] THEN [system] SHALL [response]
2. IF [condition] THEN [system] SHALL [behavior]
```

### Step 2: Create Design Document
Plan your architecture and technical approach:

```markdown
# Design Document

## Overview
High-level description of your solution approach.

## Architecture
How components will interact and data will flow.

## Components and Interfaces
Detailed breakdown of what you'll build.
```

### Step 3: Break Down Into Tasks
Create actionable implementation steps:

```markdown
# Implementation Plan

- [ ] 1. Set up project structure
  - Create directory structure
  - Initialize configuration files
  - _Requirements: 1.1_

- [ ] 2. Implement core functionality
  - [ ] 2.1 Create data models
  - [ ] 2.2 Implement business logic
```

## SDD Fundamentals

Before diving into your **first workflow**, it's important to understand the core principles that make SDD effective. These fundamentals will guide you through creating better specifications and avoiding **common pitfalls**.

## Getting Started Walkthrough

Let's walk through creating your **first spec** for a simple todo application. This **first workflow** demonstrates the complete SDD process from requirements to implementation.

### Example: Todo App Specification

#### 1. Requirements (requirements.md)
```markdown
# Todo App Requirements

## Introduction
A simple todo application that allows users to manage their daily tasks with basic CRUD operations.

## Requirements

### Requirement 1
**User Story:** As a user, I want to add new tasks, so that I can track what I need to accomplish.

#### Acceptance Criteria
1. WHEN I enter a task description THEN the system SHALL save the task with a unique ID
2. WHEN I submit an empty task THEN the system SHALL display an error message
3. IF the task is successfully added THEN the system SHALL display it in the task list

### Requirement 2
**User Story:** As a user, I want to mark tasks as complete, so that I can track my progress.

#### Acceptance Criteria
1. WHEN I click on a task THEN the system SHALL toggle its completion status
2. WHEN a task is marked complete THEN the system SHALL visually distinguish it from incomplete tasks
```

#### 2. Design (design.md)
```markdown
# Todo App Design

## Overview
A client-side web application using vanilla JavaScript with local storage persistence.

## Architecture
- Frontend: HTML/CSS/JavaScript
- Storage: Browser localStorage
- No backend required for MVP

## Components and Interfaces
- TaskManager: Core business logic
- TaskRenderer: UI rendering and updates
- StorageService: Data persistence layer

## Data Models
```javascript
Task {
  id: string
  description: string
  completed: boolean
  createdAt: Date
}
```
```

#### 3. Tasks (tasks.md)
```markdown
# Todo App Implementation Plan

- [ ] 1. Set up project structure
  - Create HTML file with basic structure
  - Set up CSS for styling
  - Initialize JavaScript modules
  - _Requirements: 1.1_

- [ ] 2. Implement data layer
  - [ ] 2.1 Create Task model with validation
  - [ ] 2.2 Implement localStorage service
  - [ ] 2.3 Add error handling for storage operations
  - _Requirements: 1.1, 2.1_

- [ ] 3. Build core functionality
  - [ ] 3.1 Implement task creation with validation
  - [ ] 3.2 Add task completion toggle
  - [ ] 3.3 Create task list rendering
  - _Requirements: 1.1, 1.2, 2.1, 2.2_
```

## Common Pitfalls and How to Avoid Them

Understanding these **common pitfalls** will help you create better specifications and avoid typical mistakes that new developers make when starting with SDD.

### 1. Writing Vague Requirements
**Problem:** "The app should be fast and user-friendly"
**Solution:** Be specific with measurable criteria
```markdown
WHEN a user adds a task THEN the system SHALL respond within 100ms
WHEN displaying the task list THEN the system SHALL show all tasks in under 200ms
```

### 2. Skipping Edge Cases
**Problem:** Only considering the happy path
**Solution:** Think about error conditions and edge cases
```markdown
WHEN a user enters a task longer than 500 characters THEN the system SHALL truncate and warn
IF localStorage is full THEN the system SHALL display a storage limit warning
```

### 3. Over-Engineering the Design
**Problem:** Planning every possible feature upfront
**Solution:** Start with MVP and plan for iteration
```markdown
## Future Considerations
- Task categories (Phase 2)
- Due dates (Phase 2)
- Collaboration features (Phase 3)
```

### 4. Tasks Too Large or Vague
**Problem:** "Implement the frontend"
**Solution:** Break into specific, actionable steps
```markdown
- [ ] 3.1 Create task input form with validation
- [ ] 3.2 Implement task list component
- [ ] 3.3 Add task completion toggle functionality
```

## Integration with AI Tools

### Working with GitHub Spec Kit
1. Use `/specify` to generate initial requirements
2. Use `/plan` to create technical design
3. Use `/tasks` to break down implementation
4. Use `/implement` to generate code from specs

### Tips for AI-Friendly Specs
- Use consistent terminology throughout documents
- Include specific examples and expected outputs
- Reference requirements explicitly in tasks
- Provide context about technical constraints

## Next Steps

### Essential Reading
- [Templates Overview](../resources/templates/README.md) - Standard spec formats
- [Decision Trees](../resources/decision-trees/README.md) - When to use SDD
- [Quality Checklists](../resources/checklists/README.md) - Validation guidelines

### Practice Exercises
1. **Simple Calculator**: Practice basic SDD workflow
2. **Weather App**: Work with external APIs
3. **Blog System**: Handle more complex data relationships

### Advanced Topics (After Mastering Basics)
- [Experienced Developer Guide](experienced-developers.md)
- [AI Integration Patterns](../how-to/ai-integration.md)
- [Legacy System Integration](../how-to/legacy-integration.md)

## Getting Help

### Community Resources
- GitHub Discussions for questions and examples
- Issue tracker for bugs and improvements
- Community examples in `/examples` directory

### Quick Reference
- **Requirements Format**: User stories + EARS acceptance criteria
- **Design Sections**: Overview, Architecture, Components, Data Models
- **Task Format**: Numbered checklist with requirement references
- **File Names**: `requirements.md`, `design.md`, `tasks.md`

Remember: SDD is about thinking before coding. Take time to understand the problem, plan your approach, and create clear specifications. Your future self (and your AI coding assistants) will thank you!