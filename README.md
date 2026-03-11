# Agente 11 - Generador de Boilerplate

Generador de código boilerplate potenciado por IA para **108+ frameworks**.

## Características

- **108+ Frameworks** - Genera código para Node.js, Python, Go, Rust, .NET, Flutter, React Native, y más
- **Listo para Producción** - Incluye tests, CI/CD, Docker y documentación
- **Múltiples Proveedores LLM** - OpenAI, Anthropic, Google AI, Ollama
- **Interfaz Streamlit** - Interfaz fácil de usar con vista previa y descarga
- **Exportación ZIP** - Descarga el proyecto completo como archivo ZIP
- **Mejores Prácticas** - Arquitecturas MVC, DDD, Clean Architecture, SSR, etc.

## Frameworks Soportados (108)

### Backend Web (38)
Node.js (Express, Fastify, NestJS, Koa, Hapi), Python (FastAPI, Flask, Django, Aiohttp, Tornado, Starlette), Go (Gin, Fiber, Standard, Echo, Chi), .NET (ASP.NET Core, FastEndpoints), Rust (Actix, Axum, Warp, Rocket), Scala (Akka, Play), Java (Spring Boot, Quarkus), Kotlin (Spring, Ktor), PHP (Laravel, Symfony, Slim), Ruby (Rails, Sinatra), Elixir Phoenix, Haskell Servant, C++ REST, Nim Jester, Dart Aqueduct

### Frontend Web (15)
Next.js 14 (App/Pages), React (CRA, Vite, Remix), Vue.js (Vite, Nuxt), Svelte (Vite, Kit), Angular 17+, SolidJS, Alpine.js, HTMX, Qwik

### Móvil (10)
Flutter, React Native, Expo, Ionic, Capacitor, Kotlin (Android, Compose), Swift (SwiftUI, UIKit), Tauri

### Blockchain (8)
Solidity (Hardhat, Truffle, Foundry), Rust (Substrate), Solana, NEAR, Algorand, Cardano

### DevOps / Infra (15)
Docker, Docker Compose, Kubernetes, Helm, Kustomize, Ansible, Terraform, Terragrunt, Packer, Vault, Jenkins, GitHub Actions, GitLab CI, ArgoCD, Crossplane

### Cloud / IaaS (12)
AWS (CDK TS/Python, SAM), Azure (Bicep, ARM, Developer CLI), GCP (Terraform, Cloud Functions, Cloud Run), DigitalOcean

### Base de Datos (8)
PostgreSQL, TimescaleDB, MongoDB, Redis, MySQL, DynamoDB, CockroachDB

### Data / ML (7)
Python (Pandas, PyTorch, TensorFlow, Scikit-learn, Jupyter, MLflow), Apache Kafka

### Microservicios / Mesh (5)
gRPC, GraphQL Apollo, Istio, Envoy, NATS

## Inicio Rápido

### Desarrollo Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Copiar archivo de entorno
cp .env.example .env

# Agregar tus API keys al .env
OPENAI_API_KEY=sk-tu-clave

# Ejecutar la app
streamlit run app.py
```

### Despliegue en Streamlit Cloud

1. Sube el código a GitHub
2. Conecta el repositorio a [Streamlit Cloud](https://share.streamlit.io)
3. Configura las variables de entorno en la configuración de la app
4. Despliega

## Uso

1. **Seleccionar Framework** - Elige categoría y framework
2. **Configurar Opciones** - Establece nombre del proyecto y opciones
3. **Generar** - Haz clic en el botón generar
4. **Vista Previa** - Ver archivos generados
5. **Descargar** - Descarga como ZIP

## Estructura del Proyecto

```
agente-11/
├── app.py                      # Interfaz Streamlit
├── requirements.txt            # Dependencias
├── .env.example               # Plantilla de entorno
├── SKILLS.md                  # Capacidades del agente (108 frameworks)
├── RULES.md                   # Reglas de generación
├── WORKFLOWS.md               # Flujos de usuario
├── STREAMLIT_CLOUD.md         # Guía de despliegue
├── README.md                   # Este archivo
└── src/
    ├── agent/
    │   ├── generator.py       # Generador de boilerplate
    │   ├── prompts.py         # Prompts del agente
    │   └── tools.py           # Herramientas LangChain
    ├── templates/
    │   ├── registry.py       # Registro de 108 frameworks
    │   └── frameworks/        # Plantillas de frameworks
    └── config/
        └── settings.py         # Configuración
```

## Configuración

### Variables de Entorno

```bash
# Proveedores LLM (configura al menos uno)
OPENAI_API_KEY=sk-tu-clave-openai
ANTHROPIC_API_KEY=sk-ant-tu-clave-anthropic
GOOGLE_API_KEY=tu-clave-google

# Configuración
DEFAULT_LLM_PROVIDER=openai
DEFAULT_MODEL=gpt-4o-mini
TEMPERATURE=0.7
```

## Arquitecturas Soportadas

- **MVC** - Model-View-Controller
- **DDD** - Domain-Driven Design
- **Modular** - Arquitectura modular
- **Clean Architecture** - Capas limpias
- **SSR** - Server-Side Rendering
- **SSG** - Static Site Generation
- **SPA** - Single Page Application
- **Microservicios** - Servicios distribuidos
- **Event-Driven** - Orientado a eventos
- **GitOps** - Operaciones basadas en Git
- **IaC** - Infrastructure as Code

## Licencia

MIT
