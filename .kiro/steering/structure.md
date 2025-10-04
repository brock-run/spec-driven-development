# Project Structure and Organization

## Repository Layout

```
├── resources/           # Core tools and templates
│   ├── decision-trees/  # Visual decision aids for critical choices
│   ├── templates/       # GitHub Spec Kit compatible templates
│   └── checklists/      # Quality and review checklists
├── how-to/             # Practical implementation guides
├── audiences/          # Role-specific guidance
├── training/           # Structured learning materials
├── examples/           # Real-world case studies and samples
└── docs/               # Research and supporting documentation
```

## Content Organization Principles

### Templates Directory (`resources/templates/`)
- **Base Templates**: Core `spec.md`, `plan.md`, `tasks.md` structure
- **Specialized Templates**: Domain-specific variants (api/, backend/, frontend/, mobile/)
- **Consistency**: All templates follow the same structural patterns for AI compatibility

### Decision Trees (`resources/decision-trees/`)
- Interactive guides for critical SDD adoption decisions
- Focus on practical decision points teams face
- Include escalation frameworks and validation gates

### Checklists (`resources/checklists/`)
- Quality assurance and review processes
- Organizational readiness assessments
- Cross-functional collaboration guides

### Audience-Specific Content (`audiences/`)
- Role-based guidance and workflows
- Tailored to different skill levels and responsibilities
- Cross-references to relevant templates and resources

### How-To Guides (`how-to/`)
- Step-by-step implementation instructions
- Practical workflows and best practices
- Integration guides for different AI tools

## File Naming Conventions

### General Rules
- Use kebab-case for all files and directories
- Be descriptive but concise
- Include context when needed (e.g., `frontend-spec.md` vs `spec.md`)

### Template Files
- Base templates: `spec.md`, `plan.md`, `tasks.md`
- Specialized variants: `[domain]-spec.md` (e.g., `api-spec.md`)
- Keep consistent structure across all template types

### Documentation Files
- Use descriptive names: `getting-started.md`, `advanced-flows.md`
- Include version or date when relevant
- Group related files in subdirectories

## Content Cross-References

### Template Relationships
- All templates reference the base structure
- Specialized templates extend base templates with domain-specific sections
- Maintain traceability between spec → plan → tasks

### Guide Integration
- How-to guides reference specific templates
- Decision trees link to relevant checklists
- Audience guides cross-reference appropriate resources

## Maintenance Guidelines

### Content Updates
- Keep templates synchronized across domains
- Update examples to reflect current best practices
- Maintain consistency in terminology and structure

### Quality Assurance
- All new templates must include working examples
- Test templates with multiple AI agents when possible
- Regular review of content accuracy and relevance

### Community Contributions
- Follow existing structure and naming conventions
- Include clear documentation for new resources
- Maintain backward compatibility when updating templates