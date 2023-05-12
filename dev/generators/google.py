import httpx
from typing import Dict
from generators.generator_script import GeneratorScript, File
from typegraph.importers.google_discovery import GoogleDiscoveryImporter
from tools.util import complete_source_from


class Google(GeneratorScript):
    """
    Ref:
        - https://developers.google.com/apis-explorer
        - https://discovery.googleapis.com/discovery/v1/apis
    """

    def __init__(self) -> None:
        super().__init__("google")

    def get_links(self) -> Dict[str, str]:
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
                urls[name.replace(" ", "_")] = url
        return urls

    def pre_run(self):
        # urls = self.get_links()
        urls = {
            "fcm": "https://fcm.googleapis.com/$discovery/rest?version=v1",
            "mybusiness": "https://mybusinessbusinessinformation.googleapis.com/$discovery/rest?version=v1",
        }

        fail_count, total = 0, len(urls)
        for title, url in urls.items():
            # Note: each iteration will do a request
            try:
                importer = GoogleDiscoveryImporter(name=title, url=url)
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
                fail_count += 1
        # > Failed to process 28/262 links
        if fail_count > 0:
            self.error(f"> Failed to process {fail_count}/{total} links")
