import black
from typing import List, Dict


class File:
    path: str
    content: str
    flags: Dict[str, bool]

    def __init__(
        self,
        path: str = None,
        content: str = None
    ) -> None:
        self.path = path
        self.content = content
        self.flags = {}

    def is_enabled(self, flag_name: str) -> bool:
        """ Check if a given flag is enabled """
        status = self.flags.get(flag_name)
        if status is None:
            return False
        return status

    def flag(self, name: str, status: bool):
        """ Set a flag for the current instance """
        self.flags[name] = status


class GeneratorScript:
    """ Base generator class """

    base_path: str
    """ Common prefix of all paths """

    files: List[File]
    """ Files to be generated """

    def __init__(self) -> None:
        self.base_path = "typegra_core"
        self.files = []

    def post_run(self):
        """Override this function to populate `self.files`"""
        pass

    def run(self):
        self.post_run()

        count = 0

        for file in self.files:
            path, content = file.path, file.content
            if file.is_enabled("black"):
                content = black.format_str(content, mode=black.FileMode())
            with open(f"{self.base_path}/{path}", "w") as f:
                f.write(content)
                print(f"Generated file {path}")
            count += 1

        print(f"Total generated {count}")
