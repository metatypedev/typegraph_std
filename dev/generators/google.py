import httpx
from typing import Dict
from generators.generator_script import GeneratorScript
from typegraph.importers.google_discovery import GoogleDiscoveryImporter
from tools.util import get_files_from_importer


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
        urls = self.get_links()
        # urls = {
        #     "healthcare": "https://healthcare.googleapis.com/$discovery/rest?version=v1beta1",
        #     "fcm": "https://fcm.googleapis.com/$discovery/rest?version=v1",
        #     "mybusiness": "https://mybusinessbusinessinformation.googleapis.com/$discovery/rest?version=v1",
        # }

        fail_count, counter, total = 0, 0, len(urls)
        for title, url in urls.items():
            counter += 1
            # Note: each iteration will do a request
            try:
                importer = GoogleDiscoveryImporter(name=title, url=url)
                self.files += get_files_from_importer(title, importer)
                self.log(f"[Ok] {counter}/{total} {title}: {url}")
            except Exception as e:
                self.error(f"[Fail] {title}: {url}")
                self.error(e)
                fail_count += 1

        if fail_count > 0:
            self.error(f"> Failed to process {fail_count}/{total} links")
