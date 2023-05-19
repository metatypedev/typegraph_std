from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_firebasedatabase() -> Import:
    firebasedatabase = HTTPRuntime("https://firebasedatabase.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasedatabase_1_ErrorResponse",
        "ListDatabaseInstancesResponseIn": "_firebasedatabase_2_ListDatabaseInstancesResponseIn",
        "ListDatabaseInstancesResponseOut": "_firebasedatabase_3_ListDatabaseInstancesResponseOut",
        "UndeleteDatabaseInstanceRequestIn": "_firebasedatabase_4_UndeleteDatabaseInstanceRequestIn",
        "UndeleteDatabaseInstanceRequestOut": "_firebasedatabase_5_UndeleteDatabaseInstanceRequestOut",
        "DisableDatabaseInstanceRequestIn": "_firebasedatabase_6_DisableDatabaseInstanceRequestIn",
        "DisableDatabaseInstanceRequestOut": "_firebasedatabase_7_DisableDatabaseInstanceRequestOut",
        "ReenableDatabaseInstanceRequestIn": "_firebasedatabase_8_ReenableDatabaseInstanceRequestIn",
        "ReenableDatabaseInstanceRequestOut": "_firebasedatabase_9_ReenableDatabaseInstanceRequestOut",
        "DatabaseInstanceIn": "_firebasedatabase_10_DatabaseInstanceIn",
        "DatabaseInstanceOut": "_firebasedatabase_11_DatabaseInstanceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListDatabaseInstancesResponseIn"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["DatabaseInstanceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDatabaseInstancesResponseIn"])
    types["ListDatabaseInstancesResponseOut"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["DatabaseInstanceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatabaseInstancesResponseOut"])
    types["UndeleteDatabaseInstanceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UndeleteDatabaseInstanceRequestIn"])
    types["UndeleteDatabaseInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteDatabaseInstanceRequestOut"])
    types["DisableDatabaseInstanceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DisableDatabaseInstanceRequestIn"])
    types["DisableDatabaseInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DisableDatabaseInstanceRequestOut"])
    types["ReenableDatabaseInstanceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReenableDatabaseInstanceRequestIn"])
    types["ReenableDatabaseInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReenableDatabaseInstanceRequestOut"])
    types["DatabaseInstanceIn"] = t.struct(
        {"name": t.string().optional(), "type": t.string().optional()}
    ).named(renames["DatabaseInstanceIn"])
    types["DatabaseInstanceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "project": t.string().optional(),
            "databaseUrl": t.string().optional(),
            "state": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseInstanceOut"])

    functions = {}
    functions["projectsLocationsInstancesGet"] = firebasedatabase.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = firebasedatabase.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = firebasedatabase.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDisable"] = firebasedatabase.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesReenable"] = firebasedatabase.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUndelete"] = firebasedatabase.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = firebasedatabase.delete(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebasedatabase",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
