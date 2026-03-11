# Agente 11 - Flujos de Trabajo

## Flujo Principal: Generar Boilerplate

### Paso 1: Seleccionar Framework
1. Usuario selecciona categoría (Backend, Frontend, Móvil, etc.)
2. Sistema muestra frameworks en esa categoría
3. Usuario selecciona framework específico
4. Sistema muestra descripción del framework

### Paso 2: Configurar Opciones
1. Usuario ingresa nombre del proyecto
2. Usuario selecciona características opcionales:
   - Incluir tests
   - Incluir CI/CD
   - Incluir config Docker
3. Sistema valida entradas

### Paso 3: Generar Código
1. Usuario hace clic en "Generar" botón
2. Sistema crea archivos basándose en plantilla
3. Sistema almacena archivos en estado de sesión
4. Sistema muestra mensaje de éxito con cantidad de archivos

### Paso 4: Vista Previa
1. Usuario navega a pestaña Vista Previa
2. Usuario selecciona archivo del dropdown
3. Sistema muestra contenido del archivo con resaltado de sintaxis

### Paso 5: Descargar
1. Usuario navega a pestaña Descargar
2. Sistema muestra estructura de archivos
3. Usuario hace clic en botón descargar
4. Sistema genera ZIP y triggerea descarga

## Flujo de Configuración de LLM

### Paso 1: Acceder a Configuración
1. Usuario navega a pestaña Configuración
2. Sistema muestra opciones de proveedor

### Paso 2: Configurar Proveedor
1. Usuario selecciona proveedor LLM
2. Usuario ingresa API key (si es requerido)
3. Usuario selecciona modelo
4. Sistema valida configuración

### Paso 3: Guardar Configuración
1. Configuración almacenada en sesión
2. Usada para generaciones futuras

## Manejo de Errores

### Framework Inválido
- Mostrar mensaje de error
- Sugerir frameworks válidos
- Permitir reintento

### Fallo en Generación
- Mostrar detalles del error
- Registrar error para debug
- Permitir reintento

### Fallo en Descarga
- Mostrar mensaje de error
- Sugerir alternativa (copiar desde vista previa)
