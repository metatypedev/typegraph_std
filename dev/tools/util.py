from typegraph.importers.base.importer import Codegen, Importer

def complete_source_from(importer: Importer):
    body = importer.codegen(Codegen()).res
    preambule = ""
    for frm, imp in importer.imports:
        preambule += f"from {frm} import {imp}\n"
    preambule += f"def import_{importer.name}() -> Import:\n"
    return preambule + body
