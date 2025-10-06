# Contributing to Spec-Driven Development Blueprint

Thank you for your interest in contributing to the SDD Blueprint! This repository serves as the definitive resource for Spec-Driven Development adoption, and community contributions are essential to its success.

## Table of Contents

- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Contribution Guidelines](#contribution-guidelines)
- [Pull Request Process](#pull-request-process)
- [Template Contributions](#template-contributions)
- [Content Standards](#content-standards)
- [Recognition and Attribution](#recognition-and-attribution)

## Getting Started

1. **Fork the repository** and clone your fork locally
2. **Read the README** to understand the project structure and goals
3. **Browse existing content** to understand our style and approach
4. **Check open issues** for contribution opportunities
5. **Join discussions** to connect with the community

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/spec-driven-development-blueprint.git
cd spec-driven-development-blueprint

# Create a feature branch
git checkout -b feature/your-contribution-name

# Make your changes and test locally
# (See testing guidelines below)

# Commit and push
git add .
git commit -m "feat: descriptive commit message"
git push origin feature/your-contribution-name
```

## Types of Contributions

### 🎯 Templates and Resources
- New spec templates for different domains
- Decision trees for common SDD scenarios
- Checklists for quality assurance and reviews
- Integration guides for AI tools and platforms

### 📚 Documentation and Guides
- How-to guides for specific workflows
- Audience-specific guidance improvements
- Training materials and exercises
- Case studies and real-world examples

### 🔧 Tooling and Automation
- GitHub Actions workflows for validation
- Scripts for content verification
- Template generation tools
- Integration examples

### 🐛 Bug Fixes and Improvements
- Fixing broken links or formatting issues
- Improving existing content clarity
- Updating outdated information
- Performance optimizations

## Contribution Guidelines

### Before You Start

1. **Check existing issues** to avoid duplicate work
2. **Open an issue** for significant changes to discuss approach
3. **Follow the project structure** outlined in `/docs/structure.md`
4. **Ensure your contribution aligns** with our target audiences

### Content Quality Standards

- **Clarity**: Write for your target audience with clear, actionable language
- **Accuracy**: Ensure technical information is correct and up-to-date
- **Completeness**: Include examples, use cases, and practical guidance
- **Consistency**: Follow existing patterns and formatting conventions

### Technical Requirements

- Use **GitHub Flavored Markdown** for all content
- Follow **kebab-case** naming for files and directories
- Include **front matter** when metadata is needed
- Test **template compatibility** with at least one AI agent
- Ensure **cross-references** are accurate and helpful

## Pull Request Process

### 1. Preparation
- Ensure your branch is up-to-date with main
- Run local validation checks (see Testing section)
- Write clear commit messages following conventional commits
- Update relevant documentation

### 2. Pull Request Creation
- Use the appropriate PR template (see `.github/pull_request_template/`)
- Provide clear description of changes and motivation
- Reference related issues using `Fixes #123` or `Relates to #456`
- Add appropriate labels and reviewers

### 3. Review Process
- Address reviewer feedback promptly and professionally
- Make requested changes in additional commits (don't force-push)
- Participate in discussions constructively
- Be patient - quality reviews take time

### 4. Merge Requirements
- All CI checks must pass
- At least one approving review from a maintainer
- No unresolved conversations
- Branch must be up-to-date with main

## Template Contributions

### New Template Guidelines

When contributing new templates, ensure they:

1. **Follow base structure**: Extend from `/resources/templates/base/`
2. **Include metadata**: Front matter with template type, audience, complexity
3. **Provide examples**: Working examples with placeholder content
4. **Reference requirements**: Clear traceability to functional requirements
5. **Support AI agents**: Structure optimized for AI consumption

### Template Validation Checklist

- [ ] Follows consistent naming convention
- [ ] Includes clear usage instructions
- [ ] Provides working examples
- [ ] References appropriate requirements
- [ ] Tested with at least one AI agent
- [ ] Includes metadata and tags
- [ ] Cross-references related templates

## Content Standards

### Writing Style
- **Audience-appropriate**: Match tone and complexity to target users
- **Action-oriented**: Focus on what users should do, not just concepts
- **Scannable**: Use headers, bullets, and formatting for easy reading
- **Inclusive**: Use inclusive language and consider diverse perspectives

### Formatting Conventions
- Use `#` for main sections, `##` for subsections
- Include code language specifiers: ```bash, ```yaml, ```markdown
- Use **bold** for emphasis, `code` for technical terms
- Include clear examples and use cases

### Link and Reference Standards
- Use relative links for internal content: `[link text](../path/to/file.md)`
- Include descriptive link text, avoid "click here"
- Verify all external links are accessible and relevant
- Update cross-references when moving or renaming files

## Recognition and Attribution

### Contributor Recognition

We value all contributions and recognize contributors through:

- **Contributors section** in README.md
- **Commit attribution** preserved in git history
- **Release notes** highlighting significant contributions
- **Community highlights** in discussions and social media

### Attribution Guidelines

- All contributors retain copyright to their contributions
- Contributions are licensed under the project's MIT license
- We follow the [All Contributors](https://allcontributors.org/) specification
- Recognition includes code, documentation, design, and community contributions

### Becoming a Maintainer

Active contributors may be invited to become maintainers based on:

- Consistent, high-quality contributions over time
- Positive community engagement and collaboration
- Understanding of project goals and standards
- Willingness to help review and mentor other contributors

## Testing and Validation

### Local Testing

Before submitting, please run these checks:

```bash
# Check markdown formatting (if markdownlint is installed)
markdownlint **/*.md

# Validate links (if markdown-link-check is installed)
find . -name "*.md" -exec markdown-link-check {} \;

# Spell check (if available)
aspell check your-new-file.md
```

### Automated Validation

Our CI pipeline automatically checks:

- Markdown formatting and syntax
- Link validity and accessibility
- Template structure and completeness
- Cross-reference accuracy
- Spelling and grammar (basic checks)

## Getting Help

### Community Support

- **GitHub Discussions**: Ask questions and share ideas
- **Issues**: Report bugs or request features
- **Pull Request Reviews**: Get feedback on your contributions
- **Documentation**: Comprehensive guides in `/docs/` directory

### Maintainer Contact

For questions about contribution process or project direction:

- Open a GitHub Discussion for general questions
- Tag `@maintainers` in issues for maintainer attention
- Use draft pull requests for early feedback on large changes

## Code of Conduct

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold these standards and help create a welcoming, inclusive community.

## License

By contributing to this project, you agree that your contributions will be licensed under the same [MIT License](LICENSE) that covers the project.

---

Thank you for contributing to the future of Spec-Driven Development! 🚀