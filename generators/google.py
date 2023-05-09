from generators.generator_script import GeneratorScript, File
from typegraph.importers.base.importer import Codegen
from typegraph.importers import GoogleDiscoveryImporter


class Google(GeneratorScript):

    def __init__(self) -> None:
        super().__init__()

    def post_run(self):
        urls = {
            "fcm": "https://fcm.googleapis.com/$discovery/rest?version=v1",
            "mybusiness": "https://mybusinessbusinessinformation.googleapis.com/$discovery/rest?version=v1",
        }
        path_prefix = "google"
        for title, url in urls:
            importer = GoogleDiscoveryImporter(title, url)
            content = importer.codegen(Codegen()).res
            file = File(f"{path_prefix}/{title}.py", content)
            self.files.append(file)
