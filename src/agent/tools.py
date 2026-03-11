from typing import Dict, Any, Optional
from langchain_core.tools import tool
from src.agent.generator import BoilerplateGenerator, TemplateOptions


@tool
def generate_boilerplate(
    framework: str,
    project_name: str,
    include_tests: bool = True,
    include_ci: bool = True,
    include_docker: bool = False,
    include_database: bool = False,
    custom_options: Optional[Dict[str, Any]] = None,
) -> Dict[str, str]:
    """Generate boilerplate code for a specific framework.

    Args:
        framework: The framework to generate boilerplate for (e.g., 'nodejs', 'python', 'nextjs')
        project_name: Name of the project
        include_tests: Whether to include test files
        include_ci: Whether to include CI/CD workflows
        include_docker: Whether to include Docker configuration
        include_database: Whether to include database setup
        custom_options: Additional custom options

    Returns:
        Dictionary with file paths as keys and file contents as values
    """
    options = TemplateOptions(
        project_name=project_name,
        include_tests=include_tests,
        include_ci=include_ci,
        include_docker=include_docker,
        include_database=include_database,
        custom_options=custom_options or {},
    )

    generator = BoilerplateGenerator()
    return generator.generate_boilerplate(framework, options)


@tool
def list_frameworks() -> Dict[str, str]:
    """List all supported frameworks for boilerplate generation.

    Returns:
        Dictionary mapping framework IDs to descriptions
    """
    generator = BoilerplateGenerator()
    return generator.get_supported_frameworks()


@tool
def get_framework_info(framework: str) -> str:
    """Get detailed information about a specific framework.

    Args:
        framework: Framework identifier

    Returns:
        Information about the framework and its boilerplate
    """
    frameworks_info = {
        "nodejs": "Node.js - Express server with routes, controllers, services, and tests",
        "nextjs": "Next.js 14 with App Router, TypeScript, and API routes",
        "python": "Python FastAPI with routes, models, services, and pytest",
        "go": "Go with standard library HTTP server",
        "typescript": "TypeScript Node.js project with Jest testing",
        "rust": "Rust with Cargo, includes basic CLI structure",
        "dotnet": ".NET 8 ASP.NET Core with controllers and Swagger",
        "docker": "Docker Compose with multi-service setup and Nginx",
        "kubernetes": "Kubernetes deployment, service, ingress, and config",
        "ansible": "Ansible playbook with roles and handlers",
        "aws": "AWS CDK TypeScript with EC2 and ECS patterns",
        "azure": "Azure Bicep with App Service and SQL",
        "gcp": "GCP Terraform with Compute Engine",
        "terraform": "Terraform AWS with S3 and EC2",
        "solidity": "Solidity smart contract with Hardhat",
        "react": "React 18 with Create React App structure",
        "vue": "Vue 3 with Vite",
        "svelte": "Svelte with Vite",
        "flutter": "Flutter with Material Design",
        "react_native": "React Native with TypeScript",
        "postgres": "PostgreSQL with Docker Compose",
        "scala": "Scala with Akka HTTP",
    }

    return frameworks_info.get(framework, "Unknown framework")


def get_tools():
    return [generate_boilerplate, list_frameworks, get_framework_info]
