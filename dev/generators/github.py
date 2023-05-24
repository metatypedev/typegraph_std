from generators.generator_script import GeneratorScript
from typegraph.importers.openapi import OpenApiImporter
from tools.util import get_files_from_importer


class Github(GeneratorScript):
    """
    Ref:
        - https://github.com/github/rest-api-description
    """

    def __init__(self) -> None:
        super().__init__("github")

    def pre_run(self):
        urls = {
            "ghes": "https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/ghes-3.0/ghes-3.0.yaml",
            "github": "https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.yaml",
        }

        try:
            for title, url in urls.items():
                importer = OpenApiImporter(name=title, url=url)
                self.files += get_files_from_importer(title, importer)
        except Exception as e:
            self.error(f"Failed {title}: {url}")
            self.error(e)
