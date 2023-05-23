import sys
import black
import os
import re
import traceback
from typing import List, Dict, Union


class File:
    path: str
    content: str
    flags: Dict[str, bool]

    def __init__(self, path: str = None, content: str = None) -> None:
        self.path = path
        self.content = content
        self.flags = {}

    def is_enabled(self, flag_name: str) -> bool:
        """Check if a given flag is enabled"""
        status = self.flags.get(flag_name)
        if status is None:
            return False
        return status

    def flag(self, name: str, status: bool):
        """Set a flag for the current instance"""
        self.flags[name] = status


class GeneratorScript:
    """Base generator class"""

    base_path: str
    """ Common prefix for all paths """

    folder_name: str
    """ Folder that contains the files relative to `base_path` """

    files: List[File]
    """ Files to be generated """

    _VERBOSE: bool = False

    def __init__(self, folder_name: str) -> None:
        self.base_path = "typegraph_std"
        self.folder_name = folder_name
        self.files = []

    def get_prefix_path(self):
        """`{base_path}/{folder_path}`"""
        return os.path.join(self.base_path, self.folder_name)

    def pre_run(self):
        """Override this function to manually populate `self.files: List[File]`"""
        raise Exception("Should be overriden")

    def log(self, msg: str):
        print(f"  {msg}", file=sys.stdout)

    def error(self, e: Union[str, Exception]):
        if isinstance(e, Exception):
            if not self._VERBOSE:
                print(e.__str__(), file=sys.stderr)
            else:
                traceback.print_exception(*sys.exc_info())
        else:
            print(f"  {e}", file=sys.stdout)

    def run(self):
        self.log("Preparing...")
        self.pre_run()
        self.log("File generation...")

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
        self.log(f"Total generated {count}")

        self.update_init_py()

    def update_init_py(self):
        code = ""
        for file in self.files:
            if file.path.endswith(".py"):
                fnames = re.findall(r"def\s+([A-Za-z0-9_]+)", file.content)
                for fname in fnames:
                    py_file = file.path.removesuffix(".py")
                    code += f"from .{py_file} import {fname}\n"

        complete_path = os.path.join(self.get_prefix_path(), "__init__.py")
        with open(complete_path, mode="w") as f:
            f.write(code)

        self.log(f"Updated {complete_path}")
