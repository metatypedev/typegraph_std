from generators.generator_script import GeneratorScript, File
from typegraph.importers.openapi import OpenApiImporter
from tools.util import complete_source_from


class Github(GeneratorScript):

    def __init__(self) -> None:
        super().__init__("github")

    def pre_run(self):
        # FIX
        # 'BoxList' object has no attribute 'items'
        title = "ghes"
        url = "https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/dereferenced/api.github.com.2022-11-28.deref.yaml"
        try:
            importer = OpenApiImporter(name=title, url=url)
            content = complete_source_from(importer)
            # TODO
            # generate files using `res_hint`
            file = File(f"{title}.py", content)
            file.flag("black", True)
            self.files.append(file)
        except Exception as e:
            self.error(f"Failed {title}: {url}")
            self.error(e)
