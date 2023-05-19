from generators.generator_script import GeneratorScript
from typegraph.importers.openapi import OpenApiImporter
from tools.util import get_files_from_importer


class Stripe(GeneratorScript):
    """
    Ref:
        - https://github.com/stripe/openapi
    """

    def __init__(self) -> None:
        super().__init__("stripe")

    def pre_run(self):
        urls = {
            "spec3": "https://raw.githubusercontent.com/stripe/openapi/master/openapi/spec3.yaml",
            "spec3_sdk": "https://raw.githubusercontent.com/stripe/openapi/master/openapi/spec3.sdk.yaml",
        }
        for title, url in urls.items():
            try:
                importer = OpenApiImporter(name=title, url=url)
                self.files += get_files_from_importer(title, importer)
            except Exception as e:
                self.error(f"Failed {title}: {url}")
                self.error(e)
