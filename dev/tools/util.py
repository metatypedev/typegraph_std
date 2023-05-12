from typegraph.importers.base.importer import Codegen, Importer
from typing import Tuple


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
