from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_firebasedatabase() -> Import:
    firebasedatabase = HTTPRuntime("https://firebasedatabase.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasedatabase_1_ErrorResponse",
        "DisableDatabaseInstanceRequestIn": "_firebasedatabase_2_DisableDatabaseInstanceRequestIn",
        "DisableDatabaseInstanceRequestOut": "_firebasedatabase_3_DisableDatabaseInstanceRequestOut",
        "DatabaseInstanceIn": "_firebasedatabase_4_DatabaseInstanceIn",
        "DatabaseInstanceOut": "_firebasedatabase_5_DatabaseInstanceOut",
        "ListDatabaseInstancesResponseIn": "_firebasedatabase_6_ListDatabaseInstancesResponseIn",
        "ListDatabaseInstancesResponseOut": "_firebasedatabase_7_ListDatabaseInstancesResponseOut",
        "UndeleteDatabaseInstanceRequestIn": "_firebasedatabase_8_UndeleteDatabaseInstanceRequestIn",
        "UndeleteDatabaseInstanceRequestOut": "_firebasedatabase_9_UndeleteDatabaseInstanceRequestOut",
        "ReenableDatabaseInstanceRequestIn": "_firebasedatabase_10_ReenableDatabaseInstanceRequestIn",
        "ReenableDatabaseInstanceRequestOut": "_firebasedatabase_11_ReenableDatabaseInstanceRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DisableDatabaseInstanceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DisableDatabaseInstanceRequestIn"])
    types["DisableDatabaseInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DisableDatabaseInstanceRequestOut"])
    types["DatabaseInstanceIn"] = t.struct(
        {"type": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DatabaseInstanceIn"])
    types["DatabaseInstanceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "state": t.string().optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "databaseUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DatabaseInstanceOut"])
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
    types["ReenableDatabaseInstanceRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ReenableDatabaseInstanceRequestIn"])
    types["ReenableDatabaseInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReenableDatabaseInstanceRequestOut"])

    functions = {}
    functions["projectsLocationsInstancesDisable"] = firebasedatabase.post(
        "v1beta/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = firebasedatabase.post(
        "v1beta/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = firebasedatabase.post(
        "v1beta/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesReenable"] = firebasedatabase.post(
        "v1beta/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesUndelete"] = firebasedatabase.post(
        "v1beta/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = firebasedatabase.post(
        "v1beta/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DatabaseInstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = firebasedatabase.post(
        "v1beta/{parent}/instances",
        t.struct(
            {
                "parent": t.string(),
                "databaseId": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "type": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
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
