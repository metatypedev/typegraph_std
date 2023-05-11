import sys
import black
import os
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
    """ Common prefix for all paths """

    folder_name: str
    """ Folder that contains the files relative to `base_path` """

    files: List[File]
    """ Files to be generated """

    def __init__(self, folder_name: str) -> None:
        self.base_path = "typegraph_std"
        self.folder_name = folder_name
        self.files = []

    def get_prefix_path(self):
        """ `{base_path}/{folder_path}` """
        return os.path.join(self.base_path, self.folder_name)

    def post_run(self):
        """ Override this function to manually populate `self.files: List[File]` """
        pass

    def log(self, msg: str):
        print(f"  {msg}", file=sys.stdout)

    def error(self, msg: str):
        print(f"  {msg}", file=sys.stderr)

    def run(self):
        self.post_run()

        count = 0

        for file in self.files:
            path, content = file.path, file.content
            if file.is_enabled("black"):
                content = black.format_str(content, mode=black.FileMode())
            complete_path = os.path.join(self.get_prefix_path(), path)

            os.makedirs(os.path.dirname(complete_path), exist_ok=True)
            with open(complete_path, mode="w") as f:
                f.write(content)
                self.log(f"Generated file {complete_path}")
            count += 1

        print(f"Total generated {count}")
