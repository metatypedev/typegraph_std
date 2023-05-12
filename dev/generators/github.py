from generators.generator_script import GeneratorScript, File
from typegraph.importers.openapi import OpenApiImporter
from tools.util import complete_source_from


class Github(GeneratorScript):
    """
    Ref:
        - https://github.com/github/rest-api-description
    """

    def __init__(self) -> None:
        super().__init__("github")

    def pre_run(self):
        # FIX
        # 'BoxList' object has no attribute 'items'
        title = "ghes"
        url = "https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/dereferenced/api.github.com.2022-11-28.deref.yaml"
        try:
            importer = OpenApiImporter(name=title, url=url)
            content, content_hint = complete_source_from(importer)
            files = [
                File(f"{title}.py", content),
                File(f"{title}.pyi", content_hint),
            ]
            for file in files:
                file.flag("black", True)
                self.files.append(file)
        except Exception as e:
            self.error(f"Failed {title}: {url}")
            self.error(e)
