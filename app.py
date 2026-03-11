import streamlit as st
import os
import io
import zipfile
from typing import Dict, List
import base64

st.set_page_config(
    page_title="Agente 11 - Generador de Boilerplate",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

FRAMEWORKS = {
    "nodejs": "Node.js - Servidor Express",
    "nextjs": "Next.js 14 - Framework React",
    "python": "Python - FastAPI",
    "go": "Go - Servidor HTTP",
    "typescript": "TypeScript - Node.js",
    "rust": "Rust - Binario Ejecutable",
    "dotnet": ".NET 8 - ASP.NET Core",
    "scala": "Scala - Akka HTTP",
    "solidity": "Solidity - Smart Contract",
    "docker": "Docker - Contenedores",
    "kubernetes": "Kubernetes - K8s Manifiestos",
    "ansible": "Ansible - Automatización",
    "aws": "AWS - CDK (TypeScript)",
    "azure": "Azure - Bicep IaC",
    "gcp": "GCP - Terraform",
    "terraform": "Terraform - AWS IaC",
    "react": "React - SPA",
    "vue": "Vue.js 3 - Framework",
    "svelte": "Svelte - Framework",
    "flutter": "Flutter - Móvil",
    "react_native": "React Native - Móvil",
    "postgres": "PostgreSQL - Base de Datos",
}

CATEGORIES = {
    "Backend Web": ["nodejs", "python", "go", "rust", "dotnet", "scala"],
    "Frontend Web": ["nextjs", "react", "vue", "svelte"],
    "Móvil": ["flutter", "react_native"],
    "Blockchain": ["solidity", "rust"],
    "DevOps": ["docker", "kubernetes", "ansible", "terraform"],
    "Cloud": ["aws", "azure", "gcp"],
    "Base de Datos": ["postgres"],
}

if "generated_files" not in st.session_state:
    st.session_state.generated_files = None
if "project_name" not in st.session_state:
    st.session_state.project_name = ""
if "selected_framework" not in st.session_state:
    st.session_state.selected_framework = ""


def generate_boilerplate_files(
    framework: str, project_name: str, options: Dict = None
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

    generators = {
        "nodejs": generate_nodejs_template,
        "nextjs": generate_nextjs_template,
        "python": generate_python_template,
        "go": generate_go_template,
        "typescript": generate_typescript_template,
        "rust": generate_rust_template,
        "dotnet": generate_dotnet_template,
        "scala": generate_scala_template,
        "solidity": generate_solidity_template,
        "docker": generate_docker_template,
        "kubernetes": generate_kubernetes_template,
        "ansible": generate_ansible_template,
        "aws": generate_aws_template,
        "azure": generate_azure_template,
        "gcp": generate_gcp_template,
        "terraform": generate_terraform_template,
        "react": generate_react_template,
        "vue": generate_vue_template,
        "svelte": generate_svelte_template,
        "flutter": generate_flutter_template,
        "react_native": generate_react_native_template,
        "postgres": generate_postgres_template,
    }

    generator = generators.get(framework)
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

    tab1, tab2, tab3, tab4 = st.tabs(
        ["📦 Generador", "👁️ Vista Previa", "💾 Descargar", "⚙️ Configuración"]
    )

    with tab1:
        st.header("Generar Nuevo Boilerplate")

        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("Seleccionar Framework")

            category = st.selectbox(
                "Categoría", options=list(CATEGORIES.keys()), index=0
            )

            frameworks_in_category = CATEGORIES[category]
            selected_framework = st.selectbox(
                "Framework",
                options=frameworks_in_category,
                format_func=lambda x: FRAMEWORKS.get(x, x),
            )

            project_name = st.text_input(
                "Nombre del Proyecto",
                value="mi-proyecto",
                help="Nombre de tu proyecto (se usará para package.json, directorios, etc.)",
            )

        with col2:
            st.subheader("Opciones")

            include_tests = st.checkbox("Incluir Tests", value=True)
            include_ci = st.checkbox("Incluir CI/CD", value=True)
            include_docker = st.checkbox("Configuración Docker", value=False)

            st.info(
                f"**Framework:** {FRAMEWORKS.get(selected_framework, selected_framework)}"
            )

            generate_btn = st.button(
                "🚀 Generar Boilerplate", type="primary", use_container_width=True
            )

        if generate_btn and project_name:
            with st.spinner("Generando boilerplate..."):
                try:
                    files = generate_boilerplate_files(selected_framework, project_name)
                    st.session_state.generated_files = files
                    st.session_state.project_name = project_name
                    st.session_state.selected_framework = selected_framework
                    st.success(
                        f"✅ ¡Se generaron {len(files)} archivos para {project_name}!"
                    )
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
            selected_file = st.selectbox("Seleccionar Archivo", options=file_list)

            if selected_file:
                content = files[selected_file]
                st.subheader(f"📄 {selected_file}")
                lang = "text"
                if selected_file.endswith((".js", ".ts", ".tsx", ".jsx")):
                    lang = "javascript"
                elif selected_file.endswith(".py"):
                    lang = "python"
                elif selected_file.endswith(".json"):
                    lang = "json"
                elif selected_file.endswith((".yml", ".yaml")):
                    lang = "yaml"
                elif selected_file.endswith(".html"):
                    lang = "html"
                elif selected_file.endswith(".css"):
                    lang = "css"
                elif selected_file.endswith((".go", ".rs")):
                    lang = "go"
                elif selected_file.endswith(".sql"):
                    lang = "sql"
                elif selected_file.endswith((".md", ".markdown")):
                    lang = "markdown"
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
                st.markdown(
                    f"**Framework:** {FRAMEWORKS.get(st.session_state.selected_framework, st.session_state.selected_framework)}"
                )
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
        )

        if provider == "openai":
            api_key = st.text_input(
                "Clave API de OpenAI", type="password", help="sk-..."
            )
            model = st.selectbox("Modelo", ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo"])
        elif provider == "anthropic":
            api_key = st.text_input(
                "Clave API de Anthropic", type="password", help="sk-ant-..."
            )
            model = st.selectbox(
                "Modelo", ["claude-3-5-sonnet-20241022", "claude-3-opus-20240229"]
            )
        elif provider == "google":
            api_key = st.text_input("Clave API de Google", type="password")
            model = st.selectbox("Modelo", ["gemini-1.5-pro", "gemini-1.5-flash"])
        else:
            base_url = st.text_input(
                "URL Base de Ollama", value="http://localhost:11434"
            )
            model = st.selectbox("Modelo", ["llama2", "mistral", "codellama"])

        st.subheader("Acerca de")
        st.markdown("""
        **Agente 11 - Generador de Boilerplate**
        
        Potenciado por LangChain y Streamlit.
        
        Soporta 22+ frameworks:
        - Web: Node.js, Python, Go, .NET, Rust, Scala
        - Frontend: Next.js, React, Vue, Svelte
        - Móvil: Flutter, React Native
        - Blockchain: Solidity
        - DevOps: Docker, Kubernetes, Ansible, Terraform
        - Cloud: AWS CDK, Azure Bicep, GCP
        - Base de Datos: PostgreSQL
        """)

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

        if st.sidebar.button("🗑️ Limpiar Todo"):
            st.session_state.generated_files = None
            st.session_state.project_name = ""
            st.session_state.selected_framework = ""
            st.rerun()
    else:
        st.sidebar.info("Aún no se ha generado ningún proyecto")


if __name__ == "__main__":
    main()
