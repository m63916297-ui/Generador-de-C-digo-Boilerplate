import os
from typing import Literal
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    anthropic_api_key: str = Field(default="", alias="ANTHROPIC_API_KEY")
    google_api_key: str = Field(default="", alias="GOOGLE_API_KEY")
    ollama_base_url: str = Field(
        default="http://localhost:11434", alias="OLLAMA_BASE_URL"
    )
    default_llm_provider: str = Field(default="openai", alias="DEFAULT_LLM_PROVIDER")
    default_model: str = Field(default="gpt-4o-mini", alias="DEFAULT_MODEL")
    temperature: float = Field(default=0.7, alias="TEMPERATURE")
    max_tokens: int = Field(default=4000, alias="MAX_TOKENS")

    class Config:
        env_file = ".env"
        extra = "allow"


LLMProvider = Literal["openai", "anthropic", "google", "ollama"]

FRAMEWORKS = {
    "nodejs": "Node.js",
    "nextjs": "Next.js",
    "python": "Python (FastAPI)",
    "go": "Go",
    "typescript": "TypeScript",
    "rust": "Rust",
    "scala": "Scala",
    "solidity": "Solidity",
    "dotnet": ".NET",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "ansible": "Ansible",
    "aws": "AWS (CDK)",
    "azure": "Azure (Bicep)",
    "gcp": "GCP",
    "terraform": "Terraform",
    "react": "React",
    "vue": "Vue.js",
    "svelte": "Svelte",
    "flutter": "Flutter",
    "react_native": "React Native",
    "postgres": "PostgreSQL",
}


def get_settings() -> Settings:
    return Settings()
