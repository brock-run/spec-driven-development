# Technical Guidelines

## Tech Stack

This is a **documentation and resource repository** - not a software application. The primary technologies are:

- **Markdown**: All content is written in structured Markdown for maximum compatibility
- **Git**: Version control for collaborative editing and contribution management
- **Static Site Generators**: Compatible with Jekyll, Hugo, GitBook, and other documentation platforms

## File Formats and Standards

### Markdown Conventions
- Use standard GitHub Flavored Markdown (GFM)
- Include front matter for metadata when needed
- Use consistent heading hierarchy (# for main sections, ## for subsections)
- Code blocks should specify language for syntax highlighting

### Template Structure
- All templates follow the base structure: `spec.md`, `plan.md`, `tasks.md`
- Templates use placeholder text in brackets: `[user role]`, `[functionality]`
- Include requirement traceability with `_Requirements: [reference]_` format

### File Organization
- Use kebab-case for file and folder names
- Group related content in logical folder hierarchies
- Include README files in major directories for navigation

## Content Guidelines

### Writing Style
- Clear, actionable language suitable for technical audiences
- Avoid jargon unless necessary and defined
- Use bullet points and structured formats for scanability
- Include practical examples and real-world scenarios

### Template Design
- Focus on AI-consumable structure and clarity
- Include both functional and non-functional requirements sections
- Provide guidance comments and examples within templates
- Ensure templates work across different AI agents and tools

## Common Commands

Since this is a documentation repository, common operations are:

```bash
# Clone and setup
git clone <repository-url>
cd spec-driven-development-blueprint

# Content validation
# Check markdown formatting
markdownlint **/*.md

# Spell check (if available)
aspell check *.md

# Generate documentation site (example with Jekyll)
bundle exec jekyll serve

# Search content
grep -r "search-term" --include="*.md" .
```

## Quality Standards

- All templates must be tested with at least one AI agent
- Include clear examples and use cases for each resource
- Maintain consistency across similar document types
- Regular review and updates based on community feedback