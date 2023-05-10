from generators.generator_script import GeneratorScript, File
from typegraph.importers.base.importer import Codegen
from typegraph.importers.google_discovery import GoogleDiscoveryImporter


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
            content = importer.codegen(Codegen()).res
            file = File(f"{path_prefix}/{title}.py", content)
            self.files.append(file)
