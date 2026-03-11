from typing import Dict, Any, Optional, Literal
from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field


class TemplateOptions(BaseModel):
    project_name: str = Field(default="my-project", description="Name of the project")
    include_tests: bool = Field(default=True, description="Include test files")
    include_ci: bool = Field(default=True, description="Include CI/CD workflows")
    include_docker: bool = Field(
        default=False, description="Include Docker configuration"
    )
    include_database: bool = Field(default=False, description="Include database setup")
    custom_options: Dict[str, Any] = Field(
        default_factory=dict, description="Additional custom options"
    )


class BoilerplateGenerator:
    def __init__(
        self,
        llm: Optional[BaseChatModel] = None,
        provider: Literal["openai", "anthropic", "google", "ollama"] = "openai",
        model: str = "gpt-4o-mini",
        temperature: float = 0.7,
        **kwargs,
    ):
        self.provider = provider
        self.model = model
        self.temperature = temperature

        if llm is not None:
            self.llm = llm
        else:
            self.llm = self._create_llm(provider, model, temperature, **kwargs)

    def _create_llm(
        self, provider: str, model: str, temperature: float, **kwargs
    ) -> BaseChatModel:
        api_key = kwargs.get("api_key", "")

        if provider == "openai":
            return ChatOpenAI(
                model=model, temperature=temperature, api_key=api_key or None
            )
        elif provider == "anthropic":
            return ChatAnthropic(
                model=model, temperature=temperature, api_key=api_key or None
            )
        elif provider == "google":
            return ChatGoogleGenerativeAI(
                model=model, temperature=temperature, google_api_key=api_key or None
            )
        elif provider == "ollama":
            from langchain_community.chat_models import ChatOllama

            base_url = kwargs.get("ollama_base_url", "http://localhost:11434")
            return ChatOllama(model=model, temperature=temperature, base_url=base_url)
        else:
            return ChatOpenAI(model=model, temperature=temperature)

    def generate_boilerplate(
        self, framework: str, options: Optional[TemplateOptions] = None
    ) -> Dict[str, str]:
        from src.templates.frameworks import (
            generate_nodejs_template,
            generate_nextjs_template,
            generate_python_template,
            generate_go_template,
            generate_typescript_template,
            generate_rust_template,
            generate_dotnet_template,
            generate_docker_template,
            generate_kubernetes_template,
            generate_ansible_template,
            generate_aws_template,
            generate_azure_template,
            generate_gcp_template,
            generate_terraform_template,
            generate_solidity_template,
            generate_react_template,
            generate_vue_template,
            generate_svelte_template,
            generate_flutter_template,
            generate_react_native_template,
            generate_postgres_template,
            generate_scala_template,
        )

        if options is None:
            options = TemplateOptions()

        project_name = options.project_name

        framework_generators = {
            "nodejs": generate_nodejs_template,
            "nextjs": generate_nextjs_template,
            "python": generate_python_template,
            "go": generate_go_template,
            "typescript": generate_typescript_template,
            "rust": generate_rust_template,
            "dotnet": generate_dotnet_template,
            "docker": generate_docker_template,
            "kubernetes": generate_kubernetes_template,
            "ansible": generate_ansible_template,
            "aws": generate_aws_template,
            "azure": generate_azure_template,
            "gcp": generate_gcp_template,
            "terraform": generate_terraform_template,
            "solidity": generate_solidity_template,
            "react": generate_react_template,
            "vue": generate_vue_template,
            "svelte": generate_svelte_template,
            "flutter": generate_flutter_template,
            "react_native": generate_react_native_template,
            "postgres": generate_postgres_template,
            "scala": generate_scala_template,
        }

        generator = framework_generators.get(framework)
        if generator is None:
            raise ValueError(f"Unsupported framework: {framework}")

        return generator(project_name, options.custom_options if options else None)

    def get_supported_frameworks(self) -> Dict[str, str]:
        return {
            "nodejs": "Node.js - Express server",
            "nextjs": "Next.js 14 - React framework",
            "python": "Python - FastAPI",
            "go": "Go - HTTP server",
            "typescript": "TypeScript - Node.js",
            "rust": "Rust - Binary executable",
            "dotnet": ".NET 8 - ASP.NET Core",
            "docker": "Docker - Container setup",
            "kubernetes": "Kubernetes - K8s manifests",
            "ansible": "Ansible - Automation",
            "aws": "AWS - CDK (TypeScript)",
            "azure": "Azure - Bicep IaC",
            "gcp": "GCP - Terraform",
            "terraform": "Terraform - AWS IaC",
            "solidity": "Solidity - Smart contract",
            "react": "React - SPA",
            "vue": "Vue.js 3 - Framework",
            "svelte": "Svelte - Framework",
            "flutter": "Flutter - Mobile",
            "react_native": "React Native - Mobile",
            "postgres": "PostgreSQL - Database",
            "scala": "Scala - Akka HTTP",
        }
