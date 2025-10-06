# Model Context Protocol (MCP) Integration Guide

## Overview

Model Context Protocol (MCP) is an open standard that enables AI applications to securely connect to external data sources and tools. In the context of Spec-Driven Development, MCP allows multiple AI agents to share context, collaborate on specifications, and maintain consistency across complex development workflows.

## What is MCP?

MCP provides:
- **Standardized Communication:** Common protocol for AI agents to exchange information
- **Secure Context Sharing:** Safe methods for sharing sensitive development context
- **Tool Interoperability:** Ability for different AI agents to use the same tools and data sources
- **Workflow Orchestration:** Coordination between multiple AI agents in complex development tasks

## MCP Setup and Configuration

### Prerequisites

- Understanding of your AI agent ecosystem (Claude, Copilot, Gemini, etc.)
- Development environment with appropriate permissions
- Basic knowledge of JSON configuration and API concepts
- Access to MCP-compatible AI tools and platforms

### Core MCP Configuration

#### 1. MCP Server Configuration
Create an MCP configuration file (`mcp-config.json`):

```json
{
  "mcpServers": {
    "sdd-context-server": {
      "command": "uvx",
      "args": ["sdd-context-mcp-server@latest"],
      "env": {
        "SDD_PROJECT_ROOT": "/path/to/your/project",
        "LOG_LEVEL": "INFO"
      },
      "disabled": false,
      "autoApprove": ["read_spec", "read_plan", "read_tasks"],
      "disabledTools": []
    },
    "github-integration": {
      "command": "uvx",
      "args": ["github-mcp-server@latest"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}",
        "GITHUB_REPO": "your-org/your-repo"
      },
      "disabled": false,
      "autoApprove": ["read_issues", "read_prs"],
      "disabledTools": ["create_issue"]
    },
    "documentation-server": {
      "command": "uvx",
      "args": ["docs-mcp-server@latest"],
      "env": {
        "DOCS_PATH": "./docs",
        "INCLUDE_PATTERNS": "*.md,*.rst,*.txt"
      },
      "disabled": false,
      "autoApprove": ["search_docs", "read_file"],
      "disabledTools": []
    }
  }
}
```

#### 2. Environment Setup
```bash
# Set up environment variables
export GITHUB_TOKEN="your-github-token"
export MCP_CONFIG_PATH="./mcp-config.json"

# Install MCP servers (examples)
uvx install sdd-context-mcp-server
uvx install github-mcp-server
uvx install docs-mcp-server
```

### Agent-Specific Configuration

#### Claude Desktop Configuration
Add to `~/.claude/config.json`:

```json
{
  "mcpServers": {
    "sdd-workflow": {
      "command": "uvx",
      "args": ["sdd-context-mcp-server"],
      "env": {
        "PROJECT_ROOT": "/Users/yourname/projects/current-project"
      }
    }
  }
}
```

#### Kiro IDE Configuration
Add to `.kiro/settings/mcp.json`:

```json
{
  "mcpServers": {
    "spec-context": {
      "command": "uvx",
      "args": ["sdd-context-mcp-server@latest"],
      "env": {
        "SPEC_DIR": "./.kiro/specs",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": ["read_requirements", "read_design", "read_tasks"],
      "disabledTools": []
    }
  }
}
```

## MCP Integration Examples

### Example 1: Multi-Agent Spec Development

This example shows how multiple AI agents can collaborate on creating and refining specifications using MCP.

#### Scenario Setup
- **Agent A (Claude):** Requirements analysis and user story creation
- **Agent B (Copilot):** Technical architecture and implementation planning
- **Agent C (Gemini):** Code review and quality assurance

#### MCP Server Configuration for Shared Context
```json
{
  "mcpServers": {
    "shared-spec-context": {
      "command": "uvx",
      "args": ["spec-collaboration-server@latest"],
      "env": {
        "WORKSPACE_PATH": "./shared-workspace",
        "COLLABORATION_MODE": "multi-agent",
        "SYNC_INTERVAL": "30s"
      },
      "disabled": false,
      "autoApprove": [
        "read_spec_artifacts",
        "write_spec_updates",
        "notify_changes"
      ],
      "disabledTools": ["delete_artifacts"]
    }
  }
}
```

#### Workflow Implementation

**Phase 1: Requirements Gathering (Agent A - Claude)**
```python
# MCP tool call example
{
  "tool": "create_spec_artifact",
  "parameters": {
    "type": "requirements",
    "content": {
      "user_stories": [
        {
          "id": "US001",
          "story": "As a developer, I want to create reusable components...",
          "acceptance_criteria": [
            "Component must be framework-agnostic",
            "Must include TypeScript definitions",
            "Must have comprehensive test coverage"
          ]
        }
      ]
    },
    "metadata": {
      "author": "claude-agent",
      "phase": "requirements",
      "timestamp": "2025-01-01T10:00:00Z"
    }
  }
}
```

**Phase 2: Technical Planning (Agent B - Copilot)**
```python
# MCP tool call to read requirements and create technical plan
{
  "tool": "read_spec_artifact",
  "parameters": {
    "type": "requirements",
    "filter": {"phase": "requirements"}
  }
}

# Then create technical plan
{
  "tool": "create_spec_artifact",
  "parameters": {
    "type": "technical_plan",
    "content": {
      "architecture": {
        "framework": "React + TypeScript",
        "build_system": "Vite",
        "testing": "Jest + React Testing Library"
      },
      "implementation_strategy": {
        "component_structure": "Atomic design principles",
        "state_management": "Context API + useReducer",
        "styling": "CSS Modules + design tokens"
      }
    },
    "references": ["US001"],
    "metadata": {
      "author": "copilot-agent",
      "phase": "technical_planning",
      "timestamp": "2025-01-01T11:00:00Z"
    }
  }
}
```

**Phase 3: Quality Review (Agent C - Gemini)**
```python
# MCP tool call to analyze all artifacts
{
  "tool": "analyze_spec_consistency",
  "parameters": {
    "artifacts": ["requirements", "technical_plan"],
    "checks": [
      "requirement_coverage",
      "technical_feasibility",
      "implementation_gaps"
    ]
  }
}

# Create quality assessment
{
  "tool": "create_spec_artifact",
  "parameters": {
    "type": "quality_assessment",
    "content": {
      "coverage_analysis": {
        "requirements_covered": 95,
        "missing_requirements": ["error_handling", "accessibility"]
      },
      "technical_risks": [
        {
          "risk": "Bundle size optimization",
          "mitigation": "Implement code splitting and lazy loading"
        }
      ],
      "recommendations": [
        "Add error boundary implementation",
        "Include accessibility testing in CI pipeline"
      ]
    },
    "metadata": {
      "author": "gemini-agent",
      "phase": "quality_review",
      "timestamp": "2025-01-01T12:00:00Z"
    }
  }
}
```

### Example 2: Cross-Platform Development Coordination

This example demonstrates MCP coordination between different development platforms and tools.

#### Scenario: Mobile App with Backend API
- **Frontend Team:** Using Kiro IDE with React Native
- **Backend Team:** Using VS Code with Node.js/Express
- **DevOps Team:** Using GitHub Actions and deployment tools

#### MCP Configuration for Cross-Platform Coordination
```json
{
  "mcpServers": {
    "api-contract-server": {
      "command": "uvx",
      "args": ["openapi-mcp-server@latest"],
      "env": {
        "OPENAPI_SPEC_PATH": "./api/openapi.yaml",
        "VALIDATION_MODE": "strict"
      },
      "disabled": false,
      "autoApprove": ["read_api_spec", "validate_endpoints"],
      "disabledTools": ["modify_spec"]
    },
    "mobile-context-server": {
      "command": "uvx",
      "args": ["react-native-mcp-server@latest"],
      "env": {
        "PLATFORM_TARGETS": "ios,android",
        "EXPO_CONFIG": "./app.json"
      },
      "disabled": false,
      "autoApprove": ["read_platform_constraints", "validate_dependencies"],
      "disabledTools": []
    },
    "deployment-server": {
      "command": "uvx",
      "args": ["deployment-mcp-server@latest"],
      "env": {
        "ENVIRONMENT": "staging",
        "DEPLOYMENT_CONFIG": "./deploy/config.yaml"
      },
      "disabled": false,
      "autoApprove": ["read_deployment_status", "validate_config"],
      "disabledTools": ["trigger_deployment"]
    }
  }
}
```

#### Coordinated Workflow Example

**API Contract Definition (Backend Team)**
```python
# Create API specification through MCP
{
  "tool": "create_api_endpoint",
  "parameters": {
    "path": "/api/v1/users",
    "method": "POST",
    "request_schema": {
      "type": "object",
      "properties": {
        "email": {"type": "string", "format": "email"},
        "name": {"type": "string", "minLength": 1}
      },
      "required": ["email", "name"]
    },
    "response_schema": {
      "type": "object",
      "properties": {
        "id": {"type": "string"},
        "email": {"type": "string"},
        "name": {"type": "string"},
        "created_at": {"type": "string", "format": "date-time"}
      }
    },
    "metadata": {
      "team": "backend",
      "version": "1.0.0"
    }
  }
}
```

**Mobile Client Generation (Frontend Team)**
```python
# Generate client code based on API contract
{
  "tool": "generate_api_client",
  "parameters": {
    "api_spec_source": "api-contract-server",
    "target_platform": "react-native",
    "client_config": {
      "base_url": "${API_BASE_URL}",
      "timeout": 10000,
      "retry_policy": "exponential_backoff"
    },
    "output_path": "./src/api/generated"
  }
}
```

**Deployment Validation (DevOps Team)**
```python
# Validate deployment readiness
{
  "tool": "validate_deployment_readiness",
  "parameters": {
    "api_spec_source": "api-contract-server",
    "mobile_build_source": "mobile-context-server",
    "environment": "staging",
    "checks": [
      "api_contract_compatibility",
      "mobile_platform_requirements",
      "deployment_configuration"
    ]
  }
}
```

### Example 3: Legacy System Integration

This example shows how MCP can help coordinate between legacy systems and modern SDD workflows.

#### Scenario Setup
- **Legacy System:** Mainframe with COBOL business logic
- **Modern Interface:** REST API built with Spring Boot
- **Frontend:** React application using SDD methodology

#### MCP Configuration for Legacy Integration
```json
{
  "mcpServers": {
    "legacy-bridge-server": {
      "command": "uvx",
      "args": ["legacy-integration-mcp@latest"],
      "env": {
        "LEGACY_SYSTEM_HOST": "mainframe.company.com",
        "INTEGRATION_MODE": "api_bridge",
        "BUSINESS_RULES_PATH": "./legacy/business-rules.json"
      },
      "disabled": false,
      "autoApprove": ["read_business_rules", "validate_data_mapping"],
      "disabledTools": ["modify_legacy_data"]
    },
    "data-mapping-server": {
      "command": "uvx",
      "args": ["data-transformation-mcp@latest"],
      "env": {
        "MAPPING_CONFIG": "./integration/data-mappings.yaml",
        "VALIDATION_RULES": "./integration/validation-rules.json"
      },
      "disabled": false,
      "autoApprove": ["transform_data", "validate_mappings"],
      "disabledTools": []
    }
  }
}
```

#### Integration Workflow

**Business Rule Extraction**
```python
# Extract business rules from legacy system
{
  "tool": "extract_business_rules",
  "parameters": {
    "source_system": "mainframe",
    "rule_categories": ["validation", "calculation", "workflow"],
    "output_format": "structured_json"
  }
}
```

**Modern API Specification**
```python
# Create API spec that preserves business logic
{
  "tool": "create_api_specification",
  "parameters": {
    "business_rules_source": "legacy-bridge-server",
    "api_style": "REST",
    "data_transformation_rules": {
      "legacy_field_mapping": true,
      "validation_preservation": true,
      "calculation_logic_mapping": true
    }
  }
}
```

## Best Practices for MCP Context Sharing

### Security Considerations

#### Sensitive Data Handling
```json
{
  "mcpServers": {
    "secure-context-server": {
      "env": {
        "ENCRYPTION_KEY": "${MCP_ENCRYPTION_KEY}",
        "DATA_CLASSIFICATION": "confidential",
        "ACCESS_CONTROL": "role_based"
      },
      "autoApprove": [],
      "disabledTools": ["export_sensitive_data"]
    }
  }
}
```

#### Access Control Patterns
- Use environment variables for sensitive configuration
- Implement role-based access control for different agent types
- Regularly rotate API keys and tokens
- Audit MCP tool usage and data access

### Performance Optimization

#### Efficient Context Sharing
```json
{
  "mcpServers": {
    "optimized-context-server": {
      "env": {
        "CACHE_STRATEGY": "intelligent",
        "COMPRESSION": "enabled",
        "BATCH_SIZE": "100",
        "SYNC_FREQUENCY": "on_change"
      }
    }
  }
}
```

#### Resource Management
- Implement caching for frequently accessed context
- Use compression for large specification documents
- Batch MCP operations when possible
- Monitor resource usage and optimize accordingly

### Error Handling and Resilience

#### Robust MCP Configuration
```json
{
  "mcpServers": {
    "resilient-server": {
      "env": {
        "RETRY_ATTEMPTS": "3",
        "TIMEOUT_SECONDS": "30",
        "FALLBACK_MODE": "local_cache",
        "ERROR_REPORTING": "enabled"
      }
    }
  }
}
```

#### Failure Recovery Strategies
- Implement graceful degradation when MCP servers are unavailable
- Use local caching for critical context data
- Provide clear error messages and recovery instructions
- Monitor MCP server health and performance

## Troubleshooting MCP Integration

### Common Configuration Issues

#### Issue: MCP server fails to start
**Diagnostic Steps:**
```bash
# Check server installation
uvx list | grep mcp-server

# Verify configuration syntax
cat mcp-config.json | jq .

# Test server connectivity
uvx run mcp-server-test --config mcp-config.json
```

**Solutions:**
- Verify all required environment variables are set
- Check file permissions for configuration files
- Ensure network connectivity to external services
- Review server logs for specific error messages

#### Issue: Agents cannot access shared context
**Diagnostic Steps:**
```bash
# Test MCP tool availability
mcp-cli list-tools --server shared-context-server

# Verify permissions
mcp-cli test-permissions --server shared-context-server

# Check agent configuration
cat ~/.claude/config.json | jq .mcpServers
```

**Solutions:**
- Verify autoApprove settings for required tools
- Check that agents are using correct MCP server endpoints
- Ensure proper authentication and authorization
- Review and update agent-specific MCP configurations

### Performance Issues

#### Issue: Slow context sharing between agents
**Solutions:**
- Implement local caching for frequently accessed data
- Optimize MCP server resource allocation
- Use compression for large context payloads
- Implement incremental sync instead of full context sharing

#### Issue: High resource usage by MCP servers
**Solutions:**
- Monitor and limit concurrent MCP connections
- Implement connection pooling and reuse
- Optimize data serialization and transfer formats
- Use lazy loading for large context datasets

## Advanced MCP Patterns

### Multi-Tenant Context Isolation
```json
{
  "mcpServers": {
    "tenant-isolated-server": {
      "env": {
        "TENANT_ID": "${PROJECT_TENANT_ID}",
        "ISOLATION_MODE": "strict",
        "CROSS_TENANT_ACCESS": "disabled"
      }
    }
  }
}
```

### Event-Driven Context Updates
```json
{
  "mcpServers": {
    "event-driven-server": {
      "env": {
        "EVENT_SOURCE": "git_hooks",
        "TRIGGER_EVENTS": "commit,push,merge",
        "UPDATE_STRATEGY": "incremental"
      }
    }
  }
}
```

### Hierarchical Context Management
```json
{
  "mcpServers": {
    "hierarchical-context": {
      "env": {
        "CONTEXT_HIERARCHY": "project,team,organization",
        "INHERITANCE_RULES": "./context-inheritance.yaml",
        "OVERRIDE_POLICY": "explicit_only"
      }
    }
  }
}
```

## Resources and Next Steps

### MCP Ecosystem Resources
- [MCP Specification](https://modelcontextprotocol.io/specification)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)
- [Community Examples](https://github.com/modelcontextprotocol/examples)
- [Best Practices Guide](https://modelcontextprotocol.io/best-practices)

### Integration Development
- Learn MCP server development for custom integrations
- Explore existing MCP servers for common use cases
- Contribute to open-source MCP server projects
- Build organization-specific MCP solutions

### Community and Support
- Join MCP developer community forums
- Participate in SDD + MCP integration discussions
- Share successful integration patterns
- Contribute to MCP ecosystem documentation