from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_area120tables() -> Import:
    area120tables = HTTPRuntime("https://area120tables.googleapis.com/")

    renames = {
        "ErrorResponse": "_area120tables_1_ErrorResponse",
        "BatchCreateRowsResponseIn": "_area120tables_2_BatchCreateRowsResponseIn",
        "BatchCreateRowsResponseOut": "_area120tables_3_BatchCreateRowsResponseOut",
        "LookupDetailsIn": "_area120tables_4_LookupDetailsIn",
        "LookupDetailsOut": "_area120tables_5_LookupDetailsOut",
        "BatchDeleteRowsRequestIn": "_area120tables_6_BatchDeleteRowsRequestIn",
        "BatchDeleteRowsRequestOut": "_area120tables_7_BatchDeleteRowsRequestOut",
        "RowIn": "_area120tables_8_RowIn",
        "RowOut": "_area120tables_9_RowOut",
        "SavedViewIn": "_area120tables_10_SavedViewIn",
        "SavedViewOut": "_area120tables_11_SavedViewOut",
        "ListWorkspacesResponseIn": "_area120tables_12_ListWorkspacesResponseIn",
        "ListWorkspacesResponseOut": "_area120tables_13_ListWorkspacesResponseOut",
        "EmptyIn": "_area120tables_14_EmptyIn",
        "EmptyOut": "_area120tables_15_EmptyOut",
        "ListTablesResponseIn": "_area120tables_16_ListTablesResponseIn",
        "ListTablesResponseOut": "_area120tables_17_ListTablesResponseOut",
        "ColumnDescriptionIn": "_area120tables_18_ColumnDescriptionIn",
        "ColumnDescriptionOut": "_area120tables_19_ColumnDescriptionOut",
        "WorkspaceIn": "_area120tables_20_WorkspaceIn",
        "WorkspaceOut": "_area120tables_21_WorkspaceOut",
        "DateDetailsIn": "_area120tables_22_DateDetailsIn",
        "DateDetailsOut": "_area120tables_23_DateDetailsOut",
        "CreateRowRequestIn": "_area120tables_24_CreateRowRequestIn",
        "CreateRowRequestOut": "_area120tables_25_CreateRowRequestOut",
        "TableIn": "_area120tables_26_TableIn",
        "TableOut": "_area120tables_27_TableOut",
        "UpdateRowRequestIn": "_area120tables_28_UpdateRowRequestIn",
        "UpdateRowRequestOut": "_area120tables_29_UpdateRowRequestOut",
        "ListRowsResponseIn": "_area120tables_30_ListRowsResponseIn",
        "ListRowsResponseOut": "_area120tables_31_ListRowsResponseOut",
        "BatchUpdateRowsRequestIn": "_area120tables_32_BatchUpdateRowsRequestIn",
        "BatchUpdateRowsRequestOut": "_area120tables_33_BatchUpdateRowsRequestOut",
        "BatchUpdateRowsResponseIn": "_area120tables_34_BatchUpdateRowsResponseIn",
        "BatchUpdateRowsResponseOut": "_area120tables_35_BatchUpdateRowsResponseOut",
        "RelationshipDetailsIn": "_area120tables_36_RelationshipDetailsIn",
        "RelationshipDetailsOut": "_area120tables_37_RelationshipDetailsOut",
        "BatchCreateRowsRequestIn": "_area120tables_38_BatchCreateRowsRequestIn",
        "BatchCreateRowsRequestOut": "_area120tables_39_BatchCreateRowsRequestOut",
        "LabeledItemIn": "_area120tables_40_LabeledItemIn",
        "LabeledItemOut": "_area120tables_41_LabeledItemOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BatchCreateRowsResponseIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["RowIn"])).optional()}
    ).named(renames["BatchCreateRowsResponseIn"])
    types["BatchCreateRowsResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateRowsResponseOut"])
    types["LookupDetailsIn"] = t.struct(
        {
            "relationshipColumnId": t.string().optional(),
            "relationshipColumn": t.string().optional(),
        }
    ).named(renames["LookupDetailsIn"])
    types["LookupDetailsOut"] = t.struct(
        {
            "relationshipColumnId": t.string().optional(),
            "relationshipColumn": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LookupDetailsOut"])
    types["BatchDeleteRowsRequestIn"] = t.struct({"names": t.array(t.string())}).named(
        renames["BatchDeleteRowsRequestIn"]
    )
    types["BatchDeleteRowsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteRowsRequestOut"])
    types["RowIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListTablesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableIn"])).optional(),
        }
    ).named(renames["ListTablesResponseIn"])
    types["ListTablesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTablesResponseOut"])
    types["ColumnDescriptionIn"] = t.struct(
        {
            "relationshipDetails": t.proxy(renames["RelationshipDetailsIn"]).optional(),
            "multipleValuesDisallowed": t.boolean().optional(),
            "id": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabeledItemIn"])).optional(),
            "readonly": t.boolean().optional(),
            "dataType": t.string().optional(),
            "name": t.string().optional(),
            "dateDetails": t.proxy(renames["DateDetailsIn"]).optional(),
            "lookupDetails": t.proxy(renames["LookupDetailsIn"]).optional(),
        }
    ).named(renames["ColumnDescriptionIn"])
    types["ColumnDescriptionOut"] = t.struct(
        {
            "relationshipDetails": t.proxy(
                renames["RelationshipDetailsOut"]
            ).optional(),
            "multipleValuesDisallowed": t.boolean().optional(),
            "id": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabeledItemOut"])).optional(),
            "readonly": t.boolean().optional(),
            "dataType": t.string().optional(),
            "name": t.string().optional(),
            "dateDetails": t.proxy(renames["DateDetailsOut"]).optional(),
            "lookupDetails": t.proxy(renames["LookupDetailsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnDescriptionOut"])
    types["WorkspaceIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableIn"])).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["WorkspaceIn"])
    types["WorkspaceOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableOut"])).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceOut"])
    types["DateDetailsIn"] = t.struct({"hasTime": t.boolean().optional()}).named(
        renames["DateDetailsIn"]
    )
    types["DateDetailsOut"] = t.struct(
        {
            "hasTime": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateDetailsOut"])
    types["CreateRowRequestIn"] = t.struct(
        {
            "parent": t.string(),
            "view": t.string().optional(),
            "row": t.proxy(renames["RowIn"]),
        }
    ).named(renames["CreateRowRequestIn"])
    types["CreateRowRequestOut"] = t.struct(
        {
            "parent": t.string(),
            "view": t.string().optional(),
            "row": t.proxy(renames["RowOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateRowRequestOut"])
    types["TableIn"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "name": t.string().optional(),
            "columns": t.array(t.proxy(renames["ColumnDescriptionIn"])).optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "savedViews": t.array(t.proxy(renames["SavedViewIn"])).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "timeZone": t.string().optional(),
            "name": t.string().optional(),
            "columns": t.array(t.proxy(renames["ColumnDescriptionOut"])).optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "savedViews": t.array(t.proxy(renames["SavedViewOut"])).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["UpdateRowRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "view": t.string().optional(),
            "row": t.proxy(renames["RowIn"]),
        }
    ).named(renames["UpdateRowRequestIn"])
    types["UpdateRowRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "view": t.string().optional(),
            "row": t.proxy(renames["RowOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateRowRequestOut"])
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
    types["BatchUpdateRowsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateRowRequestIn"]))}
    ).named(renames["BatchUpdateRowsRequestIn"])
    types["BatchUpdateRowsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateRowRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateRowsRequestOut"])
    types["BatchUpdateRowsResponseIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["RowIn"])).optional()}
    ).named(renames["BatchUpdateRowsResponseIn"])
    types["BatchUpdateRowsResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateRowsResponseOut"])
    types["RelationshipDetailsIn"] = t.struct(
        {"linkedTable": t.string().optional()}
    ).named(renames["RelationshipDetailsIn"])
    types["RelationshipDetailsOut"] = t.struct(
        {
            "linkedTable": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipDetailsOut"])
    types["BatchCreateRowsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["CreateRowRequestIn"]))}
    ).named(renames["BatchCreateRowsRequestIn"])
    types["BatchCreateRowsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["CreateRowRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateRowsRequestOut"])
    types["LabeledItemIn"] = t.struct(
        {"id": t.string().optional(), "name": t.string().optional()}
    ).named(renames["LabeledItemIn"])
    types["LabeledItemOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabeledItemOut"])

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
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "view": t.string().optional(),
                "parent": t.string(),
                "updateTime": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "values": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsBatchUpdate"] = area120tables.post(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "view": t.string().optional(),
                "parent": t.string(),
                "updateTime": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "values": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsGet"] = area120tables.post(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "view": t.string().optional(),
                "parent": t.string(),
                "updateTime": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "values": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsBatchCreate"] = area120tables.post(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "view": t.string().optional(),
                "parent": t.string(),
                "updateTime": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "values": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsPatch"] = area120tables.post(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "view": t.string().optional(),
                "parent": t.string(),
                "updateTime": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "values": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsBatchDelete"] = area120tables.post(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "view": t.string().optional(),
                "parent": t.string(),
                "updateTime": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "values": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsList"] = area120tables.post(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "view": t.string().optional(),
                "parent": t.string(),
                "updateTime": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "values": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsCreate"] = area120tables.post(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "view": t.string().optional(),
                "parent": t.string(),
                "updateTime": t.string().optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "values": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RowOut"]),
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
        importer="area120tables",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
