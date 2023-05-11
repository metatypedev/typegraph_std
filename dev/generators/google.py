import httpx
from typing import Dict
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
        super().__init__("google")

    def get_links(self) -> Dict[str, str]:
        """
        Ref:
            - https://developers.google.com/apis-explorer
            - https://discovery.googleapis.com/discovery/v1/apis
        """
        url = "https://discovery.googleapis.com/discovery/v1/apis"
        apis = httpx.get(url).json()
        items = apis.get("items")
        assert items is not None
        assert len(items) > 0
        urls = {}
        for item in items:
            name = item.get("name")
            url = item.get("discoveryRestUrl")
            if name is not None and url is not None:
                urls[name.replace(' ', '_')] = url
        return urls

    def pre_run(self):
        urls = self.get_links()
        # urls = {
        #     "fcm": "https://fcm.googleapis.com/$discovery/rest?version=v1",
        #     "mybusiness": "https://mybusinessbusinessinformation.googleapis.com/$discovery/rest?version=v1",
        # }
        for title, url in urls.items():
            # Note:
            # Each iteration will do a request
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
