# Template Migration and Deprecation Guide

This guide provides information about template lifecycle management, including deprecation processes and migration pathways for evolving SDD templates.

## Template Lifecycle

### Status Levels

Templates progress through the following status levels:

1. **Draft** - New templates under development
2. **Stable** - Production-ready templates with community validation
3. **Deprecated** - Templates being phased out with migration paths available

### Version Management

Templates follow semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes requiring migration
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes and minor improvements

## Deprecation Process

### When Templates Are Deprecated

Templates may be deprecated when:

- Better alternatives become available
- Industry practices evolve significantly
- AI agent compatibility changes
- Community feedback indicates issues
- Maintenance becomes unsustainable

### Deprecation Timeline

1. **Announcement** (Month 0)
   - Deprecation notice added to template metadata
   - Community notification through discussions
   - Migration guide published

2. **Warning Period** (Months 1-6)
   - Templates marked as deprecated in metadata
   - Warnings added to template headers
   - Migration assistance provided

3. **Removal** (Month 6+)
   - Templates moved to archive directory
   - Redirects established to replacement templates
   - Final migration notifications sent

### Deprecation Metadata

Deprecated templates include deprecation information in their metadata:

```json
{
  "maintenance": {
    "status": "deprecated",
    "deprecation": {
      "reason": "Replaced by improved template with better AI compatibility",
      "replacement": "resources/templates/api/rest-api-spec-v2.md",
      "migration_guide": "docs/migrations/api-spec-v1-to-v2.md",
      "removal_date": "2024-06-01"
    }
  }
}
```

## Migration Pathways

### Automatic Migration

For minor changes, we provide automated migration scripts:

```bash
# Run migration script
./scripts/migrate-template.py --from old-template.md --to new-template.md --version 2.0.0
```

### Manual Migration

For major changes requiring human review:

1. **Review Changes**: Compare old and new template structures
2. **Update Content**: Manually transfer content to new format
3. **Validate**: Run validation scripts on migrated content
4. **Test**: Verify with AI agents and team workflows

### Migration Checklist

- [ ] **Backup Original**: Save copy of original template usage
- [ ] **Review Differences**: Understand structural and content changes
- [ ] **Update Placeholders**: Map old placeholders to new format
- [ ] **Validate Sections**: Ensure all required sections are present
- [ ] **Test AI Compatibility**: Verify with target AI agents
- [ ] **Update References**: Fix cross-references to migrated template
- [ ] **Team Training**: Brief team on changes and new features

## Specific Migration Guides

### API Template v1 to v2 Migration

**Changes:**
- Enhanced OpenAPI integration
- Improved error handling sections
- Updated AI agent compatibility

**Migration Steps:**
1. Copy existing API specifications
2. Add new error handling section
3. Update OpenAPI schema references
4. Validate with new metadata schema

**Example:**
```markdown
<!-- Old format -->
## API Endpoints
- GET /users

<!-- New format -->
## API Specifications
### Endpoints
- **GET /users**
  - Purpose: Retrieve user list
  - Parameters: page, limit
  - Response: UserList schema
  - Errors: 400, 401, 500
```

### Frontend Template Evolution

**Changes:**
- Component-based architecture focus
- Accessibility requirements integration
- Modern framework patterns

**Migration Steps:**
1. Restructure around component specifications
2. Add accessibility acceptance criteria
3. Update state management patterns
4. Include responsive design requirements

### Backend Service Template Updates

**Changes:**
- Microservices architecture emphasis
- Container deployment specifications
- Observability requirements

**Migration Steps:**
1. Break monolithic specs into service specs
2. Add containerization requirements
3. Include monitoring and logging specs
4. Update dependency management

## Community Support

### Migration Assistance

- **GitHub Discussions**: Ask questions about specific migrations
- **Migration Office Hours**: Weekly community sessions for migration help
- **Peer Review**: Community review of migrated templates
- **Documentation**: Comprehensive guides for each migration path

### Feedback Collection

We collect feedback on migrations through:

- **Migration Surveys**: Post-migration experience surveys
- **Issue Tracking**: GitHub issues for migration problems
- **Success Stories**: Community sharing of successful migrations
- **Improvement Suggestions**: Feedback for future migration processes

## Best Practices

### For Template Maintainers

1. **Plan Deprecations Early**: Give community advance notice
2. **Provide Clear Migration Paths**: Document exact steps needed
3. **Support During Transition**: Be available for questions
4. **Test Migration Scripts**: Validate automated migration tools
5. **Gather Feedback**: Learn from each deprecation cycle

### For Template Users

1. **Stay Informed**: Subscribe to template update notifications
2. **Plan Migration Time**: Budget time for template updates
3. **Test Early**: Try new templates before old ones are deprecated
4. **Share Feedback**: Help improve migration processes
5. **Document Changes**: Keep team informed of template updates

### For Organizations

1. **Template Inventory**: Maintain list of templates in use
2. **Migration Planning**: Include template updates in sprint planning
3. **Team Training**: Ensure team knows about template changes
4. **Validation Process**: Test migrated templates before deployment
5. **Rollback Plans**: Have plans for reverting problematic migrations

## Tooling Support

### Migration Scripts

```bash
# Check for deprecated templates
./scripts/check-deprecated-templates.py --directory ./specs

# Migrate specific template
./scripts/migrate-template.py --template spec.md --target-version 2.0.0

# Validate migrated content
./scripts/validate-template-metadata.py --template migrated-spec.md
```

### CI/CD Integration

```yaml
# GitHub Actions workflow for migration checking
name: Check Template Deprecations
on:
  schedule:
    - cron: '0 0 * * 1'  # Weekly check
jobs:
  check-deprecations:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check for deprecated templates
        run: ./scripts/check-deprecated-templates.py
```

### IDE Integration

- **VS Code Extension**: Template deprecation warnings
- **Kiro Integration**: Native migration assistance
- **Cursor Support**: AI-assisted migration suggestions

## Archive Management

### Archived Template Structure

```
resources/templates/archive/
├── v1/
│   ├── api-spec-v1.md
│   ├── api-spec-v1.meta.json
│   └── README.md
├── v2/
└── deprecated/
    ├── old-frontend-spec.md
    └── migration-notes.md
```

### Archive Policies

- **Retention Period**: Archived templates kept for 2 years
- **Access Method**: Available through archive directory
- **Documentation**: Each archive includes migration notes
- **Search**: Archived templates excluded from main search

## Future Considerations

### Emerging Patterns

- **AI-Native Templates**: Templates designed specifically for AI agents
- **Multi-Modal Specs**: Templates supporting text, diagrams, and code
- **Dynamic Templates**: Templates that adapt based on project context
- **Collaborative Templates**: Real-time collaborative editing support

### Technology Evolution

- **New AI Agents**: Adapting templates for emerging AI tools
- **Framework Changes**: Updating for new development frameworks
- **Industry Standards**: Incorporating evolving industry practices
- **Accessibility Updates**: Keeping pace with accessibility requirements

---

## Getting Help

For migration assistance:

- **Documentation**: Check specific migration guides
- **Community**: Ask in GitHub Discussions
- **Issues**: Report problems via GitHub Issues
- **Direct Support**: Contact maintainers for complex migrations

Remember: Migration is an opportunity to improve your specifications and adopt better practices. Take time to review and enhance your content during the migration process.