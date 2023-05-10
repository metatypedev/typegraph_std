import sys
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


class Google(GeneratorScript):

    def __init__(self) -> None:
        super().__init__()

    def post_run(self):
        # TODO
        # Retrieve all available APIs
        # https://developers.google.com/apis-explorer
        urls = {
            "fcm": "https://fcm.googleapis.com/$discovery/rest?version=v1",
            "mybusiness": "https://mybusinessbusinessinformation.googleapis.com/$discovery/rest?version=v1",
            "abusiveexperiencereport": "https://abusiveexperiencereport.googleapis.com/$discovery/rest?version=v1",
            "sheets": "https://sheets.googleapis.com/$discovery/rest?version=v4",
            "slides": "https://slides.googleapis.com/$discovery/rest?version=v1",
            "docs": "https://slides.googleapis.com/$discovery/rest?version=v1"
        }
        path_prefix = "google"
        for title, url in urls.items():
            try:
                importer = GoogleDiscoveryImporter(name=title, url=url)
                content = complete_source_from(importer)
                # TODO
                # generate files using `res_hint`
                file = File(f"{path_prefix}/{title}.py", content)
                file.flag("black", True)
                self.files.append(file)
            except Exception:
                print(f"  Failed {title}: {url}", file=sys.stderr)
