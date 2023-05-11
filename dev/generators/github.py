from generators.generator_script import GeneratorScript, File
from typegraph.importers.base.importer import Codegen, Importer
from typegraph.importers.google_discovery import GoogleDiscoveryImporter


def complete_source_from(importer: Importer):
    body = importer.codegen(Codegen()).res
    preambule = ""
    for frm, imp in importer.imports:
        preambule += f"from {frm} import {imp}\n"
    preambule += f"def import_{importer.name}() -> Import:\n"
    return preambule + body


class Github(GeneratorScript):

    def __init__(self) -> None:
        super().__init__("github")

    def pre_run(self):
        title = "api"
        url = "https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json"
        print("yay")
        try:
            importer = GoogleDiscoveryImporter(name=title, url=url)
            content = complete_source_from(importer)
            # TODO
            # generate files using `res_hint`
            file = File(f"{title}.py", content)
            file.flag("black", True)
            self.files.append(file)
        except Exception:
            self.error(f"Failed {title}: {url}")
