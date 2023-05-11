from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_firebasedatabase() -> Import:
    firebasedatabase = HTTPRuntime("https://firebasedatabase.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasedatabase_1_ErrorResponse",
        "UndeleteDatabaseInstanceRequestIn": "_firebasedatabase_2_UndeleteDatabaseInstanceRequestIn",
        "UndeleteDatabaseInstanceRequestOut": "_firebasedatabase_3_UndeleteDatabaseInstanceRequestOut",
        "DisableDatabaseInstanceRequestIn": "_firebasedatabase_4_DisableDatabaseInstanceRequestIn",
        "DisableDatabaseInstanceRequestOut": "_firebasedatabase_5_DisableDatabaseInstanceRequestOut",
        "ReenableDatabaseInstanceRequestIn": "_firebasedatabase_6_ReenableDatabaseInstanceRequestIn",
        "ReenableDatabaseInstanceRequestOut": "_firebasedatabase_7_ReenableDatabaseInstanceRequestOut",
        "ListDatabaseInstancesResponseIn": "_firebasedatabase_8_ListDatabaseInstancesResponseIn",
        "ListDatabaseInstancesResponseOut": "_firebasedatabase_9_ListDatabaseInstancesResponseOut",
        "DatabaseInstanceIn": "_firebasedatabase_10_DatabaseInstanceIn",
        "DatabaseInstanceOut": "_firebasedatabase_11_DatabaseInstanceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "databaseUrl": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseInstanceOut"])

    functions = {}
    functions["projectsLocationsInstancesList"] = firebasedatabase.delete(
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
    functions["projectsLocationsInstancesUndelete"] = firebasedatabase.delete(
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
    functions["projectsLocationsInstancesGet"] = firebasedatabase.delete(
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
        importer="firebasedatabase", renames=renames, types=types, functions=functions
    )
