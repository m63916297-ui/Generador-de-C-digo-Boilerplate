# Agente 11 - Generador de Boilerplate

Generador de código boilerplate potenciado por IA para **72+ frameworks**.

## Características

- **72+ Frameworks** - Genera código para Node.js, Python, Go, Rust, .NET, Flutter, React Native, y más
- **Listo para Producción** - Incluye tests, CI/CD, Docker y documentación
- **Múltiples Proveedores LLM** - OpenAI, Anthropic, Google AI, Ollama
- **Interfaz Streamlit** - Interfaz fácil de usar con vista previa y descarga
- **Exportación ZIP** - Descarga el proyecto completo como archivo ZIP

## Frameworks Soportados (72)

### Backend Web (23)
Node.js Express, Node.js Fastify, NestJS, Python FastAPI, Python Flask, Python Django, Python Aiohttp, Go Gin, Go Fiber, Go Standard, .NET 8, Rust Actix, Rust Axum, Rust Warp, Scala Akka, Scala Play, Java Spring, Kotlin Spring, PHP Laravel, PHP Symfony, Ruby on Rails, Ruby Sinatra

### Frontend Web (12)
Next.js 14 (App/Pages), React CRA, React Vite, Vue.js 3, Nuxt.js, Svelte Vite, SvelteKit, Angular, SolidJS, Alpine.js, HTMX

### Móvil (8)
Flutter, React Native, Expo, Ionic, Capacitor, Kotlin Android, Swift iOS, Tauri

### Blockchain (5)
Solidity Hardhat, Solidity Truffle, Rust Substrate, Solana Rust, NEAR Rust

### DevOps (11)
Docker, Docker Compose, Kubernetes, Helm, Ansible, Terraform, Packer, Jenkins, GitHub Actions, GitLab CI, ArgoCD

### Cloud (8)
AWS CDK (TS/Python), AWS SAM, Azure Bicep, Azure ARM, GCP Terraform, GCP Functions, DigitalOcean

### Base de Datos (5)
PostgreSQL, MongoDB, Redis, MySQL, DynamoDB

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
├── SKILLS.md                  # Capacidades del agente (72 frameworks)
├── RULES.md                   # Reglas de generación
├── WORKFLOWS.md               # Flujos de usuario
├── STREAMLIT_CLOUD.md        # Guía de despliegue
├── README.md                  # Este archivo
└── src/
    ├── agent/
    │   ├── generator.py       # Generador de boilerplate
    │   ├── prompts.py        # Prompts del agente
    │   └── tools.py          # Herramientas LangChain
    ├── templates/
    │   ├── registry.py       # Registro de 72 frameworks
    │   └── frameworks/       # Plantillas de frameworks
    └── config/
        └── settings.py        # Configuración
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

## Licencia

MIT
