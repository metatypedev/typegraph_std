from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_firebasedatabase():
    firebasedatabase = HTTPRuntime("https://firebasedatabase.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasedatabase_1_ErrorResponse",
        "ListDatabaseInstancesResponseIn": "_firebasedatabase_2_ListDatabaseInstancesResponseIn",
        "ListDatabaseInstancesResponseOut": "_firebasedatabase_3_ListDatabaseInstancesResponseOut",
        "DatabaseInstanceIn": "_firebasedatabase_4_DatabaseInstanceIn",
        "DatabaseInstanceOut": "_firebasedatabase_5_DatabaseInstanceOut",
        "ReenableDatabaseInstanceRequestIn": "_firebasedatabase_6_ReenableDatabaseInstanceRequestIn",
        "ReenableDatabaseInstanceRequestOut": "_firebasedatabase_7_ReenableDatabaseInstanceRequestOut",
        "UndeleteDatabaseInstanceRequestIn": "_firebasedatabase_8_UndeleteDatabaseInstanceRequestIn",
        "UndeleteDatabaseInstanceRequestOut": "_firebasedatabase_9_UndeleteDatabaseInstanceRequestOut",
        "DisableDatabaseInstanceRequestIn": "_firebasedatabase_10_DisableDatabaseInstanceRequestIn",
        "DisableDatabaseInstanceRequestOut": "_firebasedatabase_11_DisableDatabaseInstanceRequestOut",
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
    types["DatabaseInstanceIn"] = t.struct(
        {"type": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DatabaseInstanceIn"])
    types["DatabaseInstanceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "project": t.string().optional(),
            "state": t.string().optional(),
            "databaseUrl": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseInstanceOut"])
    types["ReenableDatabaseInstanceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReenableDatabaseInstanceRequestIn"])
    types["ReenableDatabaseInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReenableDatabaseInstanceRequestOut"])
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

    functions = {}
    functions["projectsLocationsInstancesReenable"] = firebasedatabase.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDisable"] = firebasedatabase.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = firebasedatabase.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = firebasedatabase.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = firebasedatabase.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUndelete"] = firebasedatabase.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = firebasedatabase.get(
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
