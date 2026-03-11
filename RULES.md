# Agente 11 - Reglas y Directrices

## Reglas de Generación

### 1. Nomenclatura de Proyectos
- Usar kebab-case para nombres de proyectos (mi-proyecto)
- Formatear automáticamente nombres para diferentes contextos
- Validar nombres de proyectos (sin caracteres especiales)

### 2. Selección de Framework
- Debe seleccionar un framework válido de la lista soportada
- Agrupar frameworks por categoría para facilitar selección
- Mostrar descripción del framework al seleccionar

### 3. Componentes de Plantilla

#### Archivos Requeridos
- README.md con instrucciones de inicio
- .gitignore apropiado para el framework
- .env.example con variables requeridas

#### Archivos Opcionales (según opciones)
- Directorio de tests con archivos básicos
- .github/workflows/ci.yml para CI/CD
- Archivos de configuración Docker

### 4. Reglas de Calidad de Código

#### General
- Usar últimas versiones estables de frameworks
- Seguir documentación oficial y mejores prácticas
- Incluir manejo adecuado de errores
- Usar variables de entorno para configuración
- Incluir configuraciones básicas de seguridad

#### Específico por Lenguaje
- **Node.js**: Usar CommonJS o ES modules consistentemente
- **Python**: Seguir PEP 8, usar type hints
- **TypeScript**: Habilitar modo estricto
- **Go**: Usar estructura estándar de proyecto

### 5. Reglas de Testing
- Incluir estructura básica de tests
- Usar framework de testing apropiado por lenguaje
- Agregar comandos de test en package.json/requirements.txt
- Incluir samples de tests que pasen

### 6. Reglas de CI/CD
- Workflows de GitHub Actions para todos los proyectos
- Ejecutar tests en push y PR
- Verificación de build
- Linting cuando aplique

### 7. Reglas de Seguridad
- Nunca incluir secrets reales en plantillas
- Usar valores placeholder para API keys
- Incluir mejores prácticas de seguridad por framework
- Agregar .env a .gitignore

## Reglas de Streamlit Cloud

### 1. UI/UX
- Usar tabs de Streamlit para navegación
- Mostrar estados de carga durante generación
- Mostrar mensajes claros de éxito/error
- Proporcionar funcionalidad de descarga

### 2. Configuración
- Establecer título e icono de página
- Usar layout ancho para mejor UX
- Configurar estado inicial del sidebar

### 3. Variables de Entorno
- Soportar múltiples proveedores LLM
- Almacenar API keys de forma segura (no en código)
- Permitir cambios de configuración en tiempo de ejecución

## Reglas de Salida

### 1. Organización de Archivos
- Crear estructura de directorios apropiada
- Usar nomenclatura consistente de archivos
- Ordenar archivos alfabéticamente en UI

### 2. Generación de ZIP
- Incluir carpeta raíz del proyecto en ZIP
- Preservar estructura de archivos
- Usar compresión deflate

### 3. Vista Previa
- Permitir selección de archivo para previsualización
- Usar resaltado de sintaxis
- Mostrar contenido completo del archivo
