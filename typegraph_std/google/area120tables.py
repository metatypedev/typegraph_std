from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_area120tables() -> Import:
    area120tables = HTTPRuntime("https://area120tables.googleapis.com/")

    renames = {
        "ErrorResponse": "_area120tables_1_ErrorResponse",
        "WorkspaceIn": "_area120tables_2_WorkspaceIn",
        "WorkspaceOut": "_area120tables_3_WorkspaceOut",
        "ListRowsResponseIn": "_area120tables_4_ListRowsResponseIn",
        "ListRowsResponseOut": "_area120tables_5_ListRowsResponseOut",
        "RelationshipDetailsIn": "_area120tables_6_RelationshipDetailsIn",
        "RelationshipDetailsOut": "_area120tables_7_RelationshipDetailsOut",
        "DateDetailsIn": "_area120tables_8_DateDetailsIn",
        "DateDetailsOut": "_area120tables_9_DateDetailsOut",
        "BatchCreateRowsRequestIn": "_area120tables_10_BatchCreateRowsRequestIn",
        "BatchCreateRowsRequestOut": "_area120tables_11_BatchCreateRowsRequestOut",
        "RowIn": "_area120tables_12_RowIn",
        "RowOut": "_area120tables_13_RowOut",
        "CreateRowRequestIn": "_area120tables_14_CreateRowRequestIn",
        "CreateRowRequestOut": "_area120tables_15_CreateRowRequestOut",
        "BatchDeleteRowsRequestIn": "_area120tables_16_BatchDeleteRowsRequestIn",
        "BatchDeleteRowsRequestOut": "_area120tables_17_BatchDeleteRowsRequestOut",
        "LabeledItemIn": "_area120tables_18_LabeledItemIn",
        "LabeledItemOut": "_area120tables_19_LabeledItemOut",
        "BatchCreateRowsResponseIn": "_area120tables_20_BatchCreateRowsResponseIn",
        "BatchCreateRowsResponseOut": "_area120tables_21_BatchCreateRowsResponseOut",
        "UpdateRowRequestIn": "_area120tables_22_UpdateRowRequestIn",
        "UpdateRowRequestOut": "_area120tables_23_UpdateRowRequestOut",
        "ListTablesResponseIn": "_area120tables_24_ListTablesResponseIn",
        "ListTablesResponseOut": "_area120tables_25_ListTablesResponseOut",
        "BatchUpdateRowsRequestIn": "_area120tables_26_BatchUpdateRowsRequestIn",
        "BatchUpdateRowsRequestOut": "_area120tables_27_BatchUpdateRowsRequestOut",
        "EmptyIn": "_area120tables_28_EmptyIn",
        "EmptyOut": "_area120tables_29_EmptyOut",
        "SavedViewIn": "_area120tables_30_SavedViewIn",
        "SavedViewOut": "_area120tables_31_SavedViewOut",
        "TableIn": "_area120tables_32_TableIn",
        "TableOut": "_area120tables_33_TableOut",
        "LookupDetailsIn": "_area120tables_34_LookupDetailsIn",
        "LookupDetailsOut": "_area120tables_35_LookupDetailsOut",
        "ColumnDescriptionIn": "_area120tables_36_ColumnDescriptionIn",
        "ColumnDescriptionOut": "_area120tables_37_ColumnDescriptionOut",
        "ListWorkspacesResponseIn": "_area120tables_38_ListWorkspacesResponseIn",
        "ListWorkspacesResponseOut": "_area120tables_39_ListWorkspacesResponseOut",
        "BatchUpdateRowsResponseIn": "_area120tables_40_BatchUpdateRowsResponseIn",
        "BatchUpdateRowsResponseOut": "_area120tables_41_BatchUpdateRowsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["WorkspaceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableIn"])).optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["WorkspaceIn"])
    types["WorkspaceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableOut"])).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceOut"])
    types["ListRowsResponseIn"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRowsResponseIn"])
    types["ListRowsResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRowsResponseOut"])
    types["RelationshipDetailsIn"] = t.struct(
        {"linkedTable": t.string().optional()}
    ).named(renames["RelationshipDetailsIn"])
    types["RelationshipDetailsOut"] = t.struct(
        {
            "linkedTable": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipDetailsOut"])
    types["DateDetailsIn"] = t.struct({"hasTime": t.boolean().optional()}).named(
        renames["DateDetailsIn"]
    )
    types["DateDetailsOut"] = t.struct(
        {
            "hasTime": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateDetailsOut"])
    types["BatchCreateRowsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["CreateRowRequestIn"]))}
    ).named(renames["BatchCreateRowsRequestIn"])
    types["BatchCreateRowsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["CreateRowRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateRowsRequestOut"])
    types["RowIn"] = t.struct(
        {
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["CreateRowRequestIn"] = t.struct(
        {
            "view": t.string().optional(),
            "parent": t.string(),
            "row": t.proxy(renames["RowIn"]),
        }
    ).named(renames["CreateRowRequestIn"])
    types["CreateRowRequestOut"] = t.struct(
        {
            "view": t.string().optional(),
            "parent": t.string(),
            "row": t.proxy(renames["RowOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateRowRequestOut"])
    types["BatchDeleteRowsRequestIn"] = t.struct({"names": t.array(t.string())}).named(
        renames["BatchDeleteRowsRequestIn"]
    )
    types["BatchDeleteRowsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteRowsRequestOut"])
    types["LabeledItemIn"] = t.struct(
        {"name": t.string().optional(), "id": t.string().optional()}
    ).named(renames["LabeledItemIn"])
    types["LabeledItemOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabeledItemOut"])
    types["BatchCreateRowsResponseIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["RowIn"])).optional()}
    ).named(renames["BatchCreateRowsResponseIn"])
    types["BatchCreateRowsResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateRowsResponseOut"])
    types["UpdateRowRequestIn"] = t.struct(
        {
            "row": t.proxy(renames["RowIn"]),
            "updateMask": t.string().optional(),
            "view": t.string().optional(),
        }
    ).named(renames["UpdateRowRequestIn"])
    types["UpdateRowRequestOut"] = t.struct(
        {
            "row": t.proxy(renames["RowOut"]),
            "updateMask": t.string().optional(),
            "view": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateRowRequestOut"])
    types["ListTablesResponseIn"] = t.struct(
        {
            "tables": t.array(t.proxy(renames["TableIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTablesResponseIn"])
    types["ListTablesResponseOut"] = t.struct(
        {
            "tables": t.array(t.proxy(renames["TableOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTablesResponseOut"])
    types["BatchUpdateRowsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateRowRequestIn"]))}
    ).named(renames["BatchUpdateRowsRequestIn"])
    types["BatchUpdateRowsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateRowRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateRowsRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SavedViewIn"] = t.struct(
        {"id": t.string().optional(), "name": t.string().optional()}
    ).named(renames["SavedViewIn"])
    types["SavedViewOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedViewOut"])
    types["TableIn"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["ColumnDescriptionIn"])).optional(),
            "savedViews": t.array(t.proxy(renames["SavedViewIn"])).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["ColumnDescriptionOut"])).optional(),
            "savedViews": t.array(t.proxy(renames["SavedViewOut"])).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["LookupDetailsIn"] = t.struct(
        {
            "relationshipColumn": t.string().optional(),
            "relationshipColumnId": t.string().optional(),
        }
    ).named(renames["LookupDetailsIn"])
    types["LookupDetailsOut"] = t.struct(
        {
            "relationshipColumn": t.string().optional(),
            "relationshipColumnId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupDetailsOut"])
    types["ColumnDescriptionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "relationshipDetails": t.proxy(renames["RelationshipDetailsIn"]).optional(),
            "id": t.string().optional(),
            "lookupDetails": t.proxy(renames["LookupDetailsIn"]).optional(),
            "dataType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabeledItemIn"])).optional(),
            "readonly": t.boolean().optional(),
            "multipleValuesDisallowed": t.boolean().optional(),
            "dateDetails": t.proxy(renames["DateDetailsIn"]).optional(),
        }
    ).named(renames["ColumnDescriptionIn"])
    types["ColumnDescriptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "relationshipDetails": t.proxy(
                renames["RelationshipDetailsOut"]
            ).optional(),
            "id": t.string().optional(),
            "lookupDetails": t.proxy(renames["LookupDetailsOut"]).optional(),
            "dataType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabeledItemOut"])).optional(),
            "readonly": t.boolean().optional(),
            "multipleValuesDisallowed": t.boolean().optional(),
            "dateDetails": t.proxy(renames["DateDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnDescriptionOut"])
    types["ListWorkspacesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workspaces": t.array(t.proxy(renames["WorkspaceIn"])).optional(),
        }
    ).named(renames["ListWorkspacesResponseIn"])
    types["ListWorkspacesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workspaces": t.array(t.proxy(renames["WorkspaceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWorkspacesResponseOut"])
    types["BatchUpdateRowsResponseIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["RowIn"])).optional()}
    ).named(renames["BatchUpdateRowsResponseIn"])
    types["BatchUpdateRowsResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateRowsResponseOut"])

    functions = {}
    functions["tablesList"] = area120tables.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesGet"] = area120tables.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TableOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsDelete"] = area120tables.post(
        "v1alpha1/{parent}/rows:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsList"] = area120tables.post(
        "v1alpha1/{parent}/rows:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsBatchUpdate"] = area120tables.post(
        "v1alpha1/{parent}/rows:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsBatchCreate"] = area120tables.post(
        "v1alpha1/{parent}/rows:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsGet"] = area120tables.post(
        "v1alpha1/{parent}/rows:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsCreate"] = area120tables.post(
        "v1alpha1/{parent}/rows:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsPatch"] = area120tables.post(
        "v1alpha1/{parent}/rows:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsBatchDelete"] = area120tables.post(
        "v1alpha1/{parent}/rows:batchDelete",
        t.struct(
            {
                "parent": t.string(),
                "names": t.array(t.string()),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["workspacesList"] = area120tables.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkspaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["workspacesGet"] = area120tables.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["WorkspaceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="area120tables", renames=renames, types=types, functions=functions
    )
