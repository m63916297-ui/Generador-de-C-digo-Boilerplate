import streamlit as st
import io
import zipfile
from typing import Dict
import base64

st.set_page_config(
    page_title="Agente 11 - Generador de Boilerplate",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "generated_files" not in st.session_state:
    st.session_state.generated_files = None
if "project_name" not in st.session_state:
    st.session_state.project_name = ""
if "selected_framework" not in st.session_state:
    st.session_state.selected_framework = ""


def load_frameworks():
    from src.templates.registry import get_frameworks_by_category, get_categories

    return get_frameworks_by_category(), get_categories()


def generate_boilerplate_files(
    framework: str, project_name: str, options: Dict = None
) -> Dict[str, str]:
    from src.templates.registry import get_generator

    generator = get_generator(framework)
    if generator:
        return generator(project_name, options)
    return {}


def create_zip_download(files: Dict[str, str], project_name: str) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for filename, content in files.items():
            zf.writestr(f"{project_name}/{filename}", content)
    buffer.seek(0)
    return buffer.getvalue()


def main():
    st.title("🚀 Agente 11 - Generador de Boilerplate")
    st.markdown("Genera código boilerplate para tus nuevos proyectos automáticamente")

    frameworks_by_category, categories = load_frameworks()

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📦 Generador", "👁️ Vista Previa", "💾 Descargar", "⚙️ Configuración"]
    )

    with tab1:
        st.header("Generar Nuevo Boilerplate")

        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("Seleccionar Framework")

            category = st.selectbox(
                "Categoría", options=categories, index=0, key="category_select"
            )

            frameworks_in_category = frameworks_by_category.get(category, {})

            if frameworks_in_category:
                framework_options = list(frameworks_in_category.keys())
                framework_display = {
                    k: v["name"] for k, v in frameworks_in_category.items()
                }

                selected_framework = st.selectbox(
                    "Framework",
                    options=framework_options,
                    format_func=lambda x: framework_display.get(x, x),
                    key="framework_select",
                )

                if selected_framework:
                    fw_info = frameworks_in_category[selected_framework]
                    st.caption(fw_info.get("description", ""))
            else:
                selected_framework = None
                st.warning("No hay frameworks disponibles en esta categoría")

            project_name = st.text_input(
                "Nombre del Proyecto",
                value="mi-proyecto",
                help="Nombre de tu proyecto (se usará para package.json, directorios, etc.)",
                key="project_name_input",
            )

        with col2:
            st.subheader("Opciones")

            include_tests = st.checkbox("Incluir Tests", value=True, key="opt_tests")
            include_ci = st.checkbox("Incluir CI/CD", value=True, key="opt_ci")
            include_docker = st.checkbox(
                "Configuración Docker", value=False, key="opt_docker"
            )

            if selected_framework:
                framework_display = {
                    k: v["name"] for k, v in frameworks_in_category.items()
                }
                st.info(
                    f"**Framework:** {framework_display.get(selected_framework, selected_framework)}"
                )

            generate_btn = st.button(
                "🚀 Generar Boilerplate",
                type="primary",
                use_container_width=True,
                key="generate_btn",
            )

        if generate_btn and selected_framework and project_name:
            with st.spinner("Generando boilerplate..."):
                try:
                    files = generate_boilerplate_files(selected_framework, project_name)
                    if files:
                        st.session_state.generated_files = files
                        st.session_state.project_name = project_name
                        st.session_state.selected_framework = selected_framework
                        st.success(
                            f"✅ ¡Se generaron {len(files)} archivos para {project_name}!"
                        )
                    else:
                        st.warning(
                            "El generador no produjo archivos. Usando plantilla base."
                        )
                        files = {
                            "README.md": f"# {project_name}\n\nProyecto generado con Agente 11"
                        }
                        st.session_state.generated_files = files
                        st.session_state.project_name = project_name
                        st.session_state.selected_framework = selected_framework
                except Exception as e:
                    st.error(f"Error al generar boilerplate: {str(e)}")

    with tab2:
        st.header("Vista Previa de Archivos Generados")

        if st.session_state.generated_files:
            files = st.session_state.generated_files

            st.markdown(f"**Proyecto:** `{st.session_state.project_name}`")
            st.markdown(f"**Framework:** `{st.session_state.selected_framework}`")
            st.markdown(f"**Archivos:** {len(files)}")

            file_list = sorted(files.keys())
            selected_file = st.selectbox(
                "Seleccionar Archivo", options=file_list, key="file_select"
            )

            if selected_file:
                content = files[selected_file]
                st.subheader(f"📄 {selected_file}")
                lang = "text"
                ext = selected_file.split(".")[-1] if "." in selected_file else ""
                lang_map = {
                    "js": "javascript",
                    "jsx": "javascript",
                    "ts": "typescript",
                    "tsx": "typescript",
                    "py": "python",
                    "json": "json",
                    "yml": "yaml",
                    "yaml": "yaml",
                    "html": "html",
                    "css": "css",
                    "go": "go",
                    "rs": "rust",
                    "sql": "sql",
                    "md": "markdown",
                    "sh": "bash",
                    "toml": "toml",
                    "xml": "xml",
                    "swift": "swift",
                    "kt": "kotlin",
                    "java": "java",
                }
                lang = lang_map.get(ext, "text")
                st.code(content, language=lang)
        else:
            st.info(
                "Aún no se ha generado boilerplate. Ve a la pestaña Generador para crear uno."
            )

    with tab3:
        st.header("Descargar Boilerplate")

        if st.session_state.generated_files:
            files = st.session_state.generated_files
            project_name = st.session_state.project_name

            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown(f"### 📦 {project_name}")
                st.markdown(f"**Framework:** {st.session_state.selected_framework}")
                st.markdown(f"**Total de Archivos:** {len(files)}")

                st.markdown("#### 📁 Estructura de Archivos")
                for filepath in sorted(files.keys()):
                    st.markdown(f"- `{filepath}`")

            with col2:
                zip_bytes = create_zip_download(files, project_name)
                b64 = base64.b64encode(zip_bytes).decode()
                href = f'<a href="data:application/zip;base64,{b64}" download="{project_name}.zip" class="stButton"><button style="background-color:#FF4B4B;color:white;padding:0.5rem 1rem;border:none;border-radius:0.25rem;cursor:pointer;width:100%;">📥 Descargar ZIP</button></a>'
                st.markdown(href, unsafe_allow_html=True)
        else:
            st.info(
                "Aún no se ha generado boilerplate. Ve a la pestaña Generador para crear uno."
            )

    with tab4:
        st.header("⚙️ Configuración")

        st.subheader("Configuración del Proveedor LLM")

        provider = st.selectbox(
            "Proveedor",
            options=["openai", "anthropic", "google", "ollama"],
            format_func=lambda x: {
                "openai": "OpenAI (GPT-4)",
                "anthropic": "Anthropic (Claude)",
                "google": "Google AI (Gemini)",
                "ollama": "Ollama (Local)",
            }.get(x, x),
            key="provider_select",
        )

        if provider == "openai":
            api_key = st.text_input(
                "Clave API de OpenAI",
                type="password",
                help="sk-...",
                key="api_key_openai",
            )
            model = st.selectbox(
                "Modelo", ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo"], key="model_openai"
            )
        elif provider == "anthropic":
            api_key = st.text_input(
                "Clave API de Anthropic",
                type="password",
                help="sk-ant-...",
                key="api_key_anthro",
            )
            model = st.selectbox(
                "Modelo",
                ["claude-3-5-sonnet-20241022", "claude-3-opus-20240229"],
                key="model_anthro",
            )
        elif provider == "google":
            api_key = st.text_input(
                "Clave API de Google", type="password", key="api_key_google"
            )
            model = st.selectbox(
                "Modelo", ["gemini-1.5-pro", "gemini-1.5-flash"], key="model_google"
            )
        else:
            base_url = st.text_input(
                "URL Base de Ollama", value="http://localhost:11434", key="ollama_url"
            )
            model = st.selectbox(
                "Modelo", ["llama2", "mistral", "codellama"], key="model_ollama"
            )

        st.subheader("Acerca de")
        st.markdown(f"""
        **Agente 11 - Generador de Boilerplate**
        
        Potenciado por LangChain y Streamlit.
        
        Soporta **{len(frameworks_by_category) * 10}+ frameworks**:
        """)

        for cat in categories:
            count = len(frameworks_by_category.get(cat, {}))
            st.markdown(f"- **{cat}**: {count} templates")

        st.subheader("Variables de Entorno")
        st.code(
            """# Archivo .env
OPENAI_API_KEY=sk-tu-clave-aqui
ANTHROPIC_API_KEY=sk-ant-tu-clave-aqui
GOOGLE_API_KEY=tu-clave-aqui
DEFAULT_LLM_PROVIDER=openai
DEFAULT_MODEL=gpt-4o-mini""",
            language="bash",
        )

    st.sidebar.header("📋 Resumen")
    if st.session_state.generated_files:
        st.sidebar.markdown(f"**Proyecto:** {st.session_state.project_name}")
        st.sidebar.markdown(f"**Framework:** {st.session_state.selected_framework}")
        st.sidebar.markdown(f"**Archivos:** {len(st.session_state.generated_files)}")

        if st.sidebar.button("🗑️ Limpiar Todo", key="clear_btn"):
            st.session_state.generated_files = None
            st.session_state.project_name = ""
            st.session_state.selected_framework = ""
            st.rerun()
    else:
        st.sidebar.info("Aún no se ha generado ningún proyecto")


if __name__ == "__main__":
    main()
