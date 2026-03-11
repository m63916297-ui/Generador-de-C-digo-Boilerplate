# Templates - Base module
from typing import Dict, Optional


class TemplateRegistry:
    _templates: Dict[str, callable] = {}
    _metadata: Dict[str, Dict] = {}

    @classmethod
    def register(
        cls, name: str, description: str, category: str, generator_fn: callable
    ):
        cls._templates[name] = generator_fn
        cls._metadata[name] = {
            "name": name,
            "description": description,
            "category": category,
        }

    @classmethod
    def get_template(cls, name: str) -> Optional[callable]:
        return cls._templates.get(name)

    @classmethod
    def get_all_metadata(cls) -> Dict[str, Dict]:
        return cls._metadata

    @classmethod
    def get_by_category(cls, category: str) -> Dict[str, Dict]:
        return {
            name: meta
            for name, meta in cls._metadata.items()
            if meta["category"] == category
        }

    @classmethod
    def get_categories(cls) -> list:
        return list(set(meta["category"] for meta in cls._metadata.values()))


def get_template(
    framework: str, project_name: str, options: Optional[Dict] = None
) -> Dict[str, str]:
    from src.templates.frameworks import get_generator

    generator = get_generator(framework)
    if generator:
        return generator(project_name, options)
    return {}
