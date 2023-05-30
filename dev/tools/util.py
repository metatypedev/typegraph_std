from typegraph.importers.base.importer import Codegen, Importer
from typing import Tuple, Union, Dict, List
from generators.generator_script import File


def complete_source_from(
    importer: Importer, imp_params: Union[Dict[str, str], None]
) -> Tuple[str, str]:
    gen = importer.codegen(Codegen())
    body = gen.res
    preambule = ""
    for frm, imp in importer.imports:
        preambule += f"from {frm} import {imp}\n"
    if importer.enable_params:
        preambule += f"def import_{importer.name}(params={repr(imp_params)}):\n"
    else:
        preambule += f"def import_{importer.name}():\n"
    source = preambule + body
    source_hint = gen.res_hint
    return source, source_hint


def get_files_from_importer(
    title: str, importer: Importer, imp_params: Union[Dict[str, str], None] = None
) -> List[File]:
    source, source_hint = complete_source_from(importer, imp_params)
    files = [
        File(f"{title}.py", source),
        File(f"{title}.pyi", source_hint),
    ]
    for file in files:
        file.flag("black", True)
    return files
