# Agente 11 - Generador de Boilerplate

Generador de código boilerplate potenciado por IA para 22+ frameworks.

## Características

- **22+ Frameworks** - Genera código para Node.js, Python, Go, Rust, .NET y más
- **Listo para Producción** - Incluye tests, CI/CD, Docker y documentación
- **Múltiples Proveedores LLM** - OpenAI, Anthropic, Google AI, Ollama
- **Interfaz Streamlit** - Interfaz fácil de usar con vista previa y descarga
- **Exportación ZIP** - Descarga el proyecto completo como archivo ZIP

## Frameworks Soportados

| Categoría | Frameworks |
|-----------|------------|
| Backend Web | Node.js, Python (FastAPI), Go, .NET, Rust, Scala |
| Frontend Web | Next.js, React, Vue.js, Svelte |
| Móvil | Flutter, React Native |
| Blockchain | Solidity |
| DevOps | Docker, Kubernetes, Ansible, Terraform |
| Cloud | AWS CDK, Azure Bicep, GCP |
| Base de Datos | PostgreSQL |

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
├── SKILLS.md                  # Capacidades del agente
├── RULES.md                   # Reglas de generación
├── WORKFLOWS.md               # Flujos de usuario
├── STREAMLIT_CLOUD.md        # Guía de despliegue
├── README.md                  # Este archivo
└── src/
    ├── agent/
    │   ├── generator.py       # Generador de boilerplate
    │   ├── prompts.py         # Prompts del agente
    │   └── tools.py           # Herramientas LangChain
    ├── templates/
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

## Licencia

MIT
