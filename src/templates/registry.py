from typing import Dict, Optional, Callable

FRAMEWORK_TEMPLATES: Dict[str, Dict] = {
    # === BACKEND WEB (23) ===
    "nodejs_express": {
        "name": "Node.js Express",
        "category": "Backend Web",
        "description": "Servidor Express con estructura MVC",
        "generator": "nodejs",
    },
    "nodejs_fastify": {
        "name": "Node.js Fastify",
        "category": "Backend Web",
        "description": "Servidor Fastify de alto rendimiento",
        "generator": "nodejs",
    },
    "nodejs_nest": {
        "name": "NestJS",
        "category": "Backend Web",
        "description": "Framework Node.js escalable con TypeScript",
        "generator": "nodejs",
    },
    "python_fastapi": {
        "name": "Python FastAPI",
        "category": "Backend Web",
        "description": "API moderna y rápida con Python",
        "generator": "python",
    },
    "python_flask": {
        "name": "Python Flask",
        "category": "Backend Web",
        "description": "Microframework Python ligero",
        "generator": "python",
    },
    "python_django": {
        "name": "Python Django",
        "category": "Backend Web",
        "description": "Framework Python completo",
        "generator": "python",
    },
    "python_aiohttp": {
        "name": "Python Aiohttp",
        "category": "Backend Web",
        "description": "Async HTTP para Python",
        "generator": "python",
    },
    "go_gin": {
        "name": "Go Gin",
        "category": "Backend Web",
        "description": "Framework web Go rápido",
        "generator": "go",
    },
    "go_fiber": {
        "name": "Go Fiber",
        "category": "Backend Web",
        "description": "Framework Go inspirado en Express",
        "generator": "go",
    },
    "go_standard": {
        "name": "Go Standard",
        "category": "Backend Web",
        "description": "Servidor HTTP Go estándar",
        "generator": "go",
    },
    "dotnet_aspnet": {
        "name": ".NET 8 ASP.NET Core",
        "category": "Backend Web",
        "description": "Framework web moderno Microsoft",
        "generator": "dotnet",
    },
    "rust_actix": {
        "name": "Rust Actix",
        "category": "Backend Web",
        "description": "Framework Rust Actor",
        "generator": "rust",
    },
    "rust_axum": {
        "name": "Rust Axum",
        "category": "Backend Web",
        "description": "Framework Rust ergonomic",
        "generator": "rust",
    },
    "rust_warp": {
        "name": "Rust Warp",
        "category": "Backend Web",
        "description": "Servidor web Rust composable",
        "generator": "rust",
    },
    "scala_akka": {
        "name": "Scala Akka HTTP",
        "category": "Backend Web",
        "description": "Framework reactivo Scala",
        "generator": "scala",
    },
    "scala_play": {
        "name": "Scala Play",
        "category": "Backend Web",
        "description": "Framework Scala full-stack",
        "generator": "scala",
    },
    "java_spring": {
        "name": "Java Spring Boot",
        "category": "Backend Web",
        "description": "Framework Java enterprise",
        "generator": "java",
    },
    "kotlin_spring": {
        "name": "Kotlin Spring",
        "category": "Backend Web",
        "description": "Spring Boot con Kotlin",
        "generator": "kotlin",
    },
    "php_laravel": {
        "name": "PHP Laravel",
        "category": "Backend Web",
        "description": "Framework PHP elegante",
        "generator": "php",
    },
    "php_symfony": {
        "name": "PHP Symfony",
        "category": "Backend Web",
        "description": "Framework PHP reutilizable",
        "generator": "php",
    },
    "ruby_rails": {
        "name": "Ruby on Rails",
        "category": "Backend Web",
        "description": "Framework Ruby full-stack",
        "generator": "ruby",
    },
    "ruby_sinatra": {
        "name": "Ruby Sinatra",
        "category": "Backend Web",
        "description": "Microframework Ruby",
        "generator": "ruby",
    },
    # === FRONTEND WEB (12) ===
    "nextjs_app": {
        "name": "Next.js 14 App Router",
        "category": "Frontend Web",
        "description": "React framework con App Router",
        "generator": "nextjs",
    },
    "nextjs_pages": {
        "name": "Next.js 14 Pages Router",
        "category": "Frontend Web",
        "description": "React framework con Pages Router",
        "generator": "nextjs",
    },
    "react_cra": {
        "name": "React Create React App",
        "category": "Frontend Web",
        "description": "SPA React estándar",
        "generator": "react",
    },
    "react_vite": {
        "name": "React Vite",
        "category": "Frontend Web",
        "description": "React con Vite bundler",
        "generator": "react",
    },
    "vue_vite": {
        "name": "Vue.js 3 Vite",
        "category": "Frontend Web",
        "description": "Vue 3 con Vite",
        "generator": "vue",
    },
    "vue_nuxt": {
        "name": "Nuxt.js",
        "category": "Frontend Web",
        "description": "Vue meta-framework",
        "generator": "vue",
    },
    "svelte_vite": {
        "name": "Svelte Vite",
        "category": "Frontend Web",
        "description": "Svelte con Vite",
        "generator": "svelte",
    },
    "sveltekit": {
        "name": "SvelteKit",
        "category": "Frontend Web",
        "description": "Framework Svelte full-stack",
        "generator": "svelte",
    },
    "angular": {
        "name": "Angular",
        "category": "Frontend Web",
        "description": "Framework Google",
        "generator": "angular",
    },
    "solid_vite": {
        "name": "SolidJS Vite",
        "category": "Frontend Web",
        "description": "SolidJS con Vite",
        "generator": "solid",
    },
    "alpine": {
        "name": "Alpine.js",
        "category": "Frontend Web",
        "description": "JS reactivo ligero",
        "generator": "alpine",
    },
    "htmx": {
        "name": "HTMX",
        "category": "Frontend Web",
        "description": "HTML moderno con hipermedia",
        "generator": "htmx",
    },
    # === MÓVIL (8) ===
    "flutter": {
        "name": "Flutter",
        "category": "Móvil",
        "description": "UI toolkit multiplataforma",
        "generator": "flutter",
    },
    "react_native": {
        "name": "React Native",
        "category": "Móvil",
        "description": "Apps nativas con React",
        "generator": "react_native",
    },
    "expo": {
        "name": "Expo",
        "category": "Móvil",
        "description": "React Native simplificado",
        "generator": "expo",
    },
    "ionic": {
        "name": "Ionic",
        "category": "Móvil",
        "description": "Apps híbridas HTML/CSS/JS",
        "generator": "ionic",
    },
    "capacitor": {
        "name": "Capacitor",
        "category": "Móvil",
        "description": "Apps web nativas",
        "generator": "capacitor",
    },
    "kotlin_android": {
        "name": "Kotlin Android",
        "category": "Móvil",
        "description": "App Android nativa",
        "generator": "kotlin_android",
    },
    "swift_ios": {
        "name": "Swift iOS",
        "category": "Móvil",
        "description": "App iOS nativa",
        "generator": "swift_ios",
    },
    "tauri": {
        "name": "Tauri",
        "category": "Móvil",
        "description": "Apps desktop con web tech",
        "generator": "tauri",
    },
    # === BLOCKCHAIN (5) ===
    "solidity_hardhat": {
        "name": "Solidity Hardhat",
        "category": "Blockchain",
        "description": "Smart contracts con Hardhat",
        "generator": "solidity",
    },
    "solidity_truffle": {
        "name": "Solidity Truffle",
        "category": "Blockchain",
        "description": "Smart contracts con Truffle",
        "generator": "solidity",
    },
    "rust_substrate": {
        "name": "Rust Substrate",
        "category": "Blockchain",
        "description": "Blockchain framework Polkadot",
        "generator": "rust_substrate",
    },
    "solana_rust": {
        "name": "Solana Rust",
        "category": "Blockchain",
        "description": "Programas Solana",
        "generator": "solana",
    },
    "near_rust": {
        "name": "NEAR Rust",
        "category": "Blockchain",
        "description": "Smart contracts NEAR",
        "generator": "near",
    },
    # === DEVOPS (11) ===
    "docker": {
        "name": "Docker",
        "category": "DevOps",
        "description": "Contenedores Docker",
        "generator": "docker",
    },
    "docker_compose": {
        "name": "Docker Compose",
        "category": "DevOps",
        "description": "Multi-contenedor Docker",
        "generator": "docker_compose",
    },
    "kubernetes": {
        "name": "Kubernetes",
        "category": "DevOps",
        "description": "Orquestación K8s",
        "generator": "kubernetes",
    },
    "helm": {
        "name": "Helm",
        "category": "DevOps",
        "description": "Charts Kubernetes",
        "generator": "helm",
    },
    "ansible": {
        "name": "Ansible",
        "category": "DevOps",
        "description": "Automatización Ansible",
        "generator": "ansible",
    },
    "terraform": {
        "name": "Terraform AWS",
        "category": "DevOps",
        "description": "IaC Terraform AWS",
        "generator": "terraform",
    },
    "packer": {
        "name": "Packer",
        "category": "DevOps",
        "description": "Imágenes Packer",
        "generator": "packer",
    },
    "jenkins": {
        "name": "Jenkins Pipeline",
        "category": "DevOps",
        "description": "CI/CD Jenkins",
        "generator": "jenkins",
    },
    "github_actions": {
        "name": "GitHub Actions",
        "category": "DevOps",
        "description": "CI/CD GitHub",
        "generator": "github_actions",
    },
    "gitlab_ci": {
        "name": "GitLab CI",
        "category": "DevOps",
        "description": "CI/CD GitLab",
        "generator": "gitlab_ci",
    },
    "argocd": {
        "name": "ArgoCD",
        "category": "DevOps",
        "description": "GitOps Kubernetes",
        "generator": "argocd",
    },
    # === CLOUD (8) ===
    "aws_cdk": {
        "name": "AWS CDK TypeScript",
        "category": "Cloud",
        "description": "IaC AWS CDK",
        "generator": "aws",
    },
    "aws_cdk_python": {
        "name": "AWS CDK Python",
        "category": "Cloud",
        "description": "IaC AWS CDK Python",
        "generator": "aws",
    },
    "aws_sam": {
        "name": "AWS SAM",
        "category": "Cloud",
        "description": "Serverless AWS SAM",
        "generator": "aws_sam",
    },
    "azure_bicep": {
        "name": "Azure Bicep",
        "category": "Cloud",
        "description": "IaC Azure Bicep",
        "generator": "azure",
    },
    "azure_arm": {
        "name": "Azure ARM",
        "category": "Cloud",
        "description": "IaC Azure ARM",
        "generator": "azure",
    },
    "gcp_terraform": {
        "name": "GCP Terraform",
        "category": "Cloud",
        "description": "IaC GCP Terraform",
        "generator": "gcp",
    },
    "gcp_cloudfunctions": {
        "name": "GCP Cloud Functions",
        "category": "Cloud",
        "description": "Functions GCP",
        "generator": "gcp_functions",
    },
    "digitalocean": {
        "name": "DigitalOcean",
        "category": "Cloud",
        "description": "Droplets DO",
        "generator": "digitalocean",
    },
    # === BASE DE DATOS (5) ===
    "postgresql": {
        "name": "PostgreSQL",
        "category": "Base de Datos",
        "description": "Base de datos PostgreSQL",
        "generator": "postgres",
    },
    "mongodb": {
        "name": "MongoDB",
        "category": "Base de Datos",
        "description": "Base de datos MongoDB",
        "generator": "mongodb",
    },
    "redis": {
        "name": "Redis",
        "category": "Base de Datos",
        "description": "Cache Redis",
        "generator": "redis",
    },
    "mysql": {
        "name": "MySQL",
        "category": "Base de Datos",
        "description": "Base de datos MySQL",
        "generator": "mysql",
    },
    "dynamodb": {
        "name": "DynamoDB",
        "category": "Base de Datos",
        "description": "NoSQL AWS",
        "generator": "dynamodb",
    },
}


def get_framework_list() -> Dict[str, Dict]:
    return FRAMEWORK_TEMPLATES


def get_frameworks_by_category() -> Dict[str, Dict[str, Dict]]:
    categories = {}
    for key, value in FRAMEWORK_TEMPLATES.items():
        cat = value["category"]
        if cat not in categories:
            categories[cat] = {}
        categories[cat][key] = value
    return categories


def get_categories() -> list:
    return list(set(v["category"] for v in FRAMEWORK_TEMPLATES.values()))


def get_generator(framework: str) -> Optional[Callable]:
    from src.templates.frameworks import (
        generate_nodejs_template,
        generate_nextjs_template,
        generate_python_template,
        generate_go_template,
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

    generators = {
        "nodejs": generate_nodejs_template,
        "nextjs": generate_nextjs_template,
        "python": generate_python_template,
        "go": generate_go_template,
        "rust": generate_rust_template,
        "dotnet": generate_dotnet_template,
        "scala": generate_scala_template,
        "solidity": generate_solidity_template,
        "docker": generate_docker_template,
        "docker_compose": generate_docker_template,
        "kubernetes": generate_kubernetes_template,
        "ansible": generate_ansible_template,
        "aws": generate_aws_template,
        "aws_sam": generate_aws_template,
        "azure": generate_azure_template,
        "gcp": generate_gcp_template,
        "gcp_functions": generate_gcp_template,
        "terraform": generate_terraform_template,
        "react": generate_react_template,
        "vue": generate_vue_template,
        "svelte": generate_svelte_template,
        "flutter": generate_flutter_template,
        "react_native": generate_react_native_template,
        "postgres": generate_postgres_template,
    }

    fw = FRAMEWORK_TEMPLATES.get(framework, {})
    gen_key = fw.get("generator")

    if gen_key in generators:
        return generators[gen_key]
    return None
