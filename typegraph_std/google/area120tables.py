from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_area120tables():
    area120tables = HTTPRuntime("https://area120tables.googleapis.com/")

    renames = {
        "ErrorResponse": "_area120tables_1_ErrorResponse",
        "UpdateRowRequestIn": "_area120tables_2_UpdateRowRequestIn",
        "UpdateRowRequestOut": "_area120tables_3_UpdateRowRequestOut",
        "RowIn": "_area120tables_4_RowIn",
        "RowOut": "_area120tables_5_RowOut",
        "BatchCreateRowsResponseIn": "_area120tables_6_BatchCreateRowsResponseIn",
        "BatchCreateRowsResponseOut": "_area120tables_7_BatchCreateRowsResponseOut",
        "ListRowsResponseIn": "_area120tables_8_ListRowsResponseIn",
        "ListRowsResponseOut": "_area120tables_9_ListRowsResponseOut",
        "RelationshipDetailsIn": "_area120tables_10_RelationshipDetailsIn",
        "RelationshipDetailsOut": "_area120tables_11_RelationshipDetailsOut",
        "CreateRowRequestIn": "_area120tables_12_CreateRowRequestIn",
        "CreateRowRequestOut": "_area120tables_13_CreateRowRequestOut",
        "WorkspaceIn": "_area120tables_14_WorkspaceIn",
        "WorkspaceOut": "_area120tables_15_WorkspaceOut",
        "ColumnDescriptionIn": "_area120tables_16_ColumnDescriptionIn",
        "ColumnDescriptionOut": "_area120tables_17_ColumnDescriptionOut",
        "ListTablesResponseIn": "_area120tables_18_ListTablesResponseIn",
        "ListTablesResponseOut": "_area120tables_19_ListTablesResponseOut",
        "EmptyIn": "_area120tables_20_EmptyIn",
        "EmptyOut": "_area120tables_21_EmptyOut",
        "ListWorkspacesResponseIn": "_area120tables_22_ListWorkspacesResponseIn",
        "ListWorkspacesResponseOut": "_area120tables_23_ListWorkspacesResponseOut",
        "BatchUpdateRowsResponseIn": "_area120tables_24_BatchUpdateRowsResponseIn",
        "BatchUpdateRowsResponseOut": "_area120tables_25_BatchUpdateRowsResponseOut",
        "LookupDetailsIn": "_area120tables_26_LookupDetailsIn",
        "LookupDetailsOut": "_area120tables_27_LookupDetailsOut",
        "BatchCreateRowsRequestIn": "_area120tables_28_BatchCreateRowsRequestIn",
        "BatchCreateRowsRequestOut": "_area120tables_29_BatchCreateRowsRequestOut",
        "BatchDeleteRowsRequestIn": "_area120tables_30_BatchDeleteRowsRequestIn",
        "BatchDeleteRowsRequestOut": "_area120tables_31_BatchDeleteRowsRequestOut",
        "BatchUpdateRowsRequestIn": "_area120tables_32_BatchUpdateRowsRequestIn",
        "BatchUpdateRowsRequestOut": "_area120tables_33_BatchUpdateRowsRequestOut",
        "TableIn": "_area120tables_34_TableIn",
        "TableOut": "_area120tables_35_TableOut",
        "DateDetailsIn": "_area120tables_36_DateDetailsIn",
        "DateDetailsOut": "_area120tables_37_DateDetailsOut",
        "SavedViewIn": "_area120tables_38_SavedViewIn",
        "SavedViewOut": "_area120tables_39_SavedViewOut",
        "LabeledItemIn": "_area120tables_40_LabeledItemIn",
        "LabeledItemOut": "_area120tables_41_LabeledItemOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UpdateRowRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "row": t.proxy(renames["RowIn"]),
            "view": t.string().optional(),
        }
    ).named(renames["UpdateRowRequestIn"])
    types["UpdateRowRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "row": t.proxy(renames["RowOut"]),
            "view": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateRowRequestOut"])
    types["RowIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["BatchCreateRowsResponseIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["RowIn"])).optional()}
    ).named(renames["BatchCreateRowsResponseIn"])
    types["BatchCreateRowsResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateRowsResponseOut"])
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
    types["WorkspaceIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableIn"])).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["WorkspaceIn"])
    types["WorkspaceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableOut"])).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceOut"])
    types["ColumnDescriptionIn"] = t.struct(
        {
            "dateDetails": t.proxy(renames["DateDetailsIn"]).optional(),
            "relationshipDetails": t.proxy(renames["RelationshipDetailsIn"]).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "multipleValuesDisallowed": t.boolean().optional(),
            "lookupDetails": t.proxy(renames["LookupDetailsIn"]).optional(),
            "readonly": t.boolean().optional(),
            "labels": t.array(t.proxy(renames["LabeledItemIn"])).optional(),
            "dataType": t.string().optional(),
        }
    ).named(renames["ColumnDescriptionIn"])
    types["ColumnDescriptionOut"] = t.struct(
        {
            "dateDetails": t.proxy(renames["DateDetailsOut"]).optional(),
            "relationshipDetails": t.proxy(
                renames["RelationshipDetailsOut"]
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "multipleValuesDisallowed": t.boolean().optional(),
            "lookupDetails": t.proxy(renames["LookupDetailsOut"]).optional(),
            "readonly": t.boolean().optional(),
            "labels": t.array(t.proxy(renames["LabeledItemOut"])).optional(),
            "dataType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnDescriptionOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["BatchCreateRowsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["CreateRowRequestIn"]))}
    ).named(renames["BatchCreateRowsRequestIn"])
    types["BatchCreateRowsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["CreateRowRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateRowsRequestOut"])
    types["BatchDeleteRowsRequestIn"] = t.struct({"names": t.array(t.string())}).named(
        renames["BatchDeleteRowsRequestIn"]
    )
    types["BatchDeleteRowsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteRowsRequestOut"])
    types["BatchUpdateRowsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateRowRequestIn"]))}
    ).named(renames["BatchUpdateRowsRequestIn"])
    types["BatchUpdateRowsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateRowRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateRowsRequestOut"])
    types["TableIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "columns": t.array(t.proxy(renames["ColumnDescriptionIn"])).optional(),
            "savedViews": t.array(t.proxy(renames["SavedViewIn"])).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "timeZone": t.string().optional(),
            "columns": t.array(t.proxy(renames["ColumnDescriptionOut"])).optional(),
            "savedViews": t.array(t.proxy(renames["SavedViewOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["DateDetailsIn"] = t.struct({"hasTime": t.boolean().optional()}).named(
        renames["DateDetailsIn"]
    )
    types["DateDetailsOut"] = t.struct(
        {
            "hasTime": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateDetailsOut"])
    types["SavedViewIn"] = t.struct(
        {"name": t.string().optional(), "id": t.string().optional()}
    ).named(renames["SavedViewIn"])
    types["SavedViewOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SavedViewOut"])
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

    functions = {}
    functions["tablesGet"] = area120tables.get(
        "v1alpha1/tables",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTablesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesList"] = area120tables.get(
        "v1alpha1/tables",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTablesResponseOut"]),
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
                "values": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
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
                "values": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
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
                "values": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
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
                "values": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
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
                "values": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
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
                "values": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
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
                "values": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
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
                "values": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RowOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["workspacesGet"] = area120tables.get(
        "v1alpha1/workspaces",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["workspacesList"] = area120tables.get(
        "v1alpha1/workspaces",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWorkspacesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="area120tables",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
