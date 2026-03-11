from typing import Dict, List
import io
import zipfile
import os


def generate_zip(files: Dict[str, str]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for filename, content in files.items():
            zf.writestr(filename, content)
    buffer.seek(0)
    return buffer.getvalue()


def create_file_structure(project_name: str, files: Dict[str, str]) -> Dict[str, str]:
    prefixed_files = {}
    for filename, content in files.items():
        prefixed_files[f"{project_name}/{filename}"] = content
    return prefixed_files
