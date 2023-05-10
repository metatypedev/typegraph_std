from generators.generator_script import GeneratorScript, File
from typegraph.importers.base.importer import Codegen
from typegraph.importers.base.importer import Importer
from typegraph.importers.google_discovery import GoogleDiscoveryImporter


def complete_source_from(importer: Importer):
    body = importer.codegen(Codegen()).res
    preambule = ""
    for frm, imp in importer.imports:
        preambule += f"from {frm} import {imp}\n"
    preambule += f"def import_{importer.name}() -> Import:\n"
    return preambule + body


class Google(GeneratorScript):

    def __init__(self) -> None:
        super().__init__()

    def post_run(self):
        # TODO
        # Retrieve all available APIs
        urls = {
            "fcm": "https://fcm.googleapis.com/$discovery/rest?version=v1",
            "mybusiness": "https://mybusinessbusinessinformation.googleapis.com/$discovery/rest?version=v1",
        }
        path_prefix = "google"
        for title, url in urls.items():
            importer = GoogleDiscoveryImporter(name=title, url=url)
            content = complete_source_from(importer)
            # TODO
            # generate files using `res_hint`
            file = File(f"{path_prefix}/{title}.py", content)
            file.flag("black", True)
            self.files.append(file)
