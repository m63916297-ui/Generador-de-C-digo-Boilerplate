# Configuración de Streamlit Cloud

## Requisitos
- Python 3.11+
- streamlit >= 1.28.0
- langchain >= 0.3.0
- langchain-openai >= 0.2.0
- langchain-anthropic >= 0.2.0
- langchain-google-genai >= 0.1.0

## Variables de Entorno

Configurar en la configuración de Streamlit Cloud:

```
OPENAI_API_KEY=sk-tu-clave-openai
ANTHROPIC_API_KEY=sk-ant-tu-clave-anthropic
GOOGLE_API_KEY=tu-clave-google
DEFAULT_LLM_PROVIDER=openai
DEFAULT_MODEL=gpt-4o-mini
```

## Pasos de Despliegue

1. Sube el código a GitHub
2. Ve a [Streamlit Cloud](https://share.streamlit.io)
3. Conecta tu repositorio de GitHub
4. Establece las variables de entorno en la configuración de la app
5. Despliega

## Estructura URL de la App

- App principal: `https://share.streamlit.io/tu-usuario/repo/main/app.py`

## Archivos de Configuración

### .streamlit/config.toml
```toml
[server]
port = 8501
headless = true

[browser]
serverAddress = "0.0.0.0"
gatherUsageStats = false
```

## Solución de Problemas

### Errores de Import
- Asegúrate de que todas las dependencias estén en requirements.txt
- Verifica que la versión de Python sea 3.11+

### Errores de API Key
- Verifica que las variables de entorno estén configuradas
- Verifica el formato de la API key
- Asegúrate de que la facturación esté configurada para OpenAI/Anthropic

### Problemas de Memoria
- Reduce la complejidad del modelo
- Limita solicitudes concurrentes
- Considera usar modelos más pequeños
