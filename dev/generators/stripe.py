from generators.generator_script import GeneratorScript, File
from typegraph.importers.openapi import OpenApiImporter
from tools.util import complete_source_from


class Stripe(GeneratorScript):
    """
    Ref:
        - https://github.com/stripe/openapi
    """

    def __init__(self) -> None:
        super().__init__("stripe")

    def pre_run(self):
        # FIX
        # Unsupported schema: {'anyOf': [{'$ref': '#/components/schemas/account_business_profile'}], ... }
        urls = {
            "spec3": "https://raw.githubusercontent.com/stripe/openapi/master/openapi/spec3.yaml",
            "spec3_sdk": "https://raw.githubusercontent.com/stripe/openapi/master/openapi/spec3.sdk.yaml",
        }
        for title, url in urls.items():
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
