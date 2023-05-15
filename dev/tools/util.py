from typegraph.importers.base.importer import Codegen, Importer
from typing import Tuple, List
from generators.generator_script import File


def complete_source_from(importer: Importer) -> Tuple[str, str]:
    gen = importer.codegen(Codegen())
    body = gen.res
    preambule = ""
    for frm, imp in importer.imports:
        preambule += f"from {frm} import {imp}\n"
    preambule += f"def import_{importer.name}() -> Import:\n"
    source = preambule + body
    source_hint = gen.res_hint
    return source, source_hint


def get_files_from_importer(title: str, importer: Importer) -> List[File]:
    source, source_hint = complete_source_from(importer)
    files = [
        File(f"{title}.py", source),
        File(f"{title}.pyi", source_hint),
    ]
    for file in files:
        file.flag("black", True)
    return files
