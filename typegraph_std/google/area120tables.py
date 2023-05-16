from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_area120tables() -> Import:
    area120tables = HTTPRuntime("https://area120tables.googleapis.com/")

    renames = {
        "ErrorResponse": "_area120tables_1_ErrorResponse",
        "DateDetailsIn": "_area120tables_2_DateDetailsIn",
        "DateDetailsOut": "_area120tables_3_DateDetailsOut",
        "UpdateRowRequestIn": "_area120tables_4_UpdateRowRequestIn",
        "UpdateRowRequestOut": "_area120tables_5_UpdateRowRequestOut",
        "TableIn": "_area120tables_6_TableIn",
        "TableOut": "_area120tables_7_TableOut",
        "ColumnDescriptionIn": "_area120tables_8_ColumnDescriptionIn",
        "ColumnDescriptionOut": "_area120tables_9_ColumnDescriptionOut",
        "BatchCreateRowsResponseIn": "_area120tables_10_BatchCreateRowsResponseIn",
        "BatchCreateRowsResponseOut": "_area120tables_11_BatchCreateRowsResponseOut",
        "EmptyIn": "_area120tables_12_EmptyIn",
        "EmptyOut": "_area120tables_13_EmptyOut",
        "WorkspaceIn": "_area120tables_14_WorkspaceIn",
        "WorkspaceOut": "_area120tables_15_WorkspaceOut",
        "BatchUpdateRowsRequestIn": "_area120tables_16_BatchUpdateRowsRequestIn",
        "BatchUpdateRowsRequestOut": "_area120tables_17_BatchUpdateRowsRequestOut",
        "BatchCreateRowsRequestIn": "_area120tables_18_BatchCreateRowsRequestIn",
        "BatchCreateRowsRequestOut": "_area120tables_19_BatchCreateRowsRequestOut",
        "SavedViewIn": "_area120tables_20_SavedViewIn",
        "SavedViewOut": "_area120tables_21_SavedViewOut",
        "CreateRowRequestIn": "_area120tables_22_CreateRowRequestIn",
        "CreateRowRequestOut": "_area120tables_23_CreateRowRequestOut",
        "ListTablesResponseIn": "_area120tables_24_ListTablesResponseIn",
        "ListTablesResponseOut": "_area120tables_25_ListTablesResponseOut",
        "RowIn": "_area120tables_26_RowIn",
        "RowOut": "_area120tables_27_RowOut",
        "BatchUpdateRowsResponseIn": "_area120tables_28_BatchUpdateRowsResponseIn",
        "BatchUpdateRowsResponseOut": "_area120tables_29_BatchUpdateRowsResponseOut",
        "BatchDeleteRowsRequestIn": "_area120tables_30_BatchDeleteRowsRequestIn",
        "BatchDeleteRowsRequestOut": "_area120tables_31_BatchDeleteRowsRequestOut",
        "LookupDetailsIn": "_area120tables_32_LookupDetailsIn",
        "LookupDetailsOut": "_area120tables_33_LookupDetailsOut",
        "ListRowsResponseIn": "_area120tables_34_ListRowsResponseIn",
        "ListRowsResponseOut": "_area120tables_35_ListRowsResponseOut",
        "ListWorkspacesResponseIn": "_area120tables_36_ListWorkspacesResponseIn",
        "ListWorkspacesResponseOut": "_area120tables_37_ListWorkspacesResponseOut",
        "LabeledItemIn": "_area120tables_38_LabeledItemIn",
        "LabeledItemOut": "_area120tables_39_LabeledItemOut",
        "RelationshipDetailsIn": "_area120tables_40_RelationshipDetailsIn",
        "RelationshipDetailsOut": "_area120tables_41_RelationshipDetailsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DateDetailsIn"] = t.struct({"hasTime": t.boolean().optional()}).named(
        renames["DateDetailsIn"]
    )
    types["DateDetailsOut"] = t.struct(
        {
            "hasTime": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateDetailsOut"])
    types["UpdateRowRequestIn"] = t.struct(
        {
            "view": t.string().optional(),
            "updateMask": t.string().optional(),
            "row": t.proxy(renames["RowIn"]),
        }
    ).named(renames["UpdateRowRequestIn"])
    types["UpdateRowRequestOut"] = t.struct(
        {
            "view": t.string().optional(),
            "updateMask": t.string().optional(),
            "row": t.proxy(renames["RowOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateRowRequestOut"])
    types["TableIn"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["ColumnDescriptionIn"])).optional(),
            "name": t.string().optional(),
            "timeZone": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "savedViews": t.array(t.proxy(renames["SavedViewIn"])).optional(),
        }
    ).named(renames["TableIn"])
    types["TableOut"] = t.struct(
        {
            "columns": t.array(t.proxy(renames["ColumnDescriptionOut"])).optional(),
            "name": t.string().optional(),
            "timeZone": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "savedViews": t.array(t.proxy(renames["SavedViewOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TableOut"])
    types["ColumnDescriptionIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabeledItemIn"])).optional(),
            "id": t.string().optional(),
            "relationshipDetails": t.proxy(renames["RelationshipDetailsIn"]).optional(),
            "lookupDetails": t.proxy(renames["LookupDetailsIn"]).optional(),
            "dateDetails": t.proxy(renames["DateDetailsIn"]).optional(),
            "name": t.string().optional(),
            "multipleValuesDisallowed": t.boolean().optional(),
            "readonly": t.boolean().optional(),
            "dataType": t.string().optional(),
        }
    ).named(renames["ColumnDescriptionIn"])
    types["ColumnDescriptionOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabeledItemOut"])).optional(),
            "id": t.string().optional(),
            "relationshipDetails": t.proxy(
                renames["RelationshipDetailsOut"]
            ).optional(),
            "lookupDetails": t.proxy(renames["LookupDetailsOut"]).optional(),
            "dateDetails": t.proxy(renames["DateDetailsOut"]).optional(),
            "name": t.string().optional(),
            "multipleValuesDisallowed": t.boolean().optional(),
            "readonly": t.boolean().optional(),
            "dataType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ColumnDescriptionOut"])
    types["BatchCreateRowsResponseIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["RowIn"])).optional()}
    ).named(renames["BatchCreateRowsResponseIn"])
    types["BatchCreateRowsResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateRowsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["WorkspaceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableIn"])).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["WorkspaceIn"])
    types["WorkspaceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "tables": t.array(t.proxy(renames["TableOut"])).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WorkspaceOut"])
    types["BatchUpdateRowsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["UpdateRowRequestIn"]))}
    ).named(renames["BatchUpdateRowsRequestIn"])
    types["BatchUpdateRowsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["UpdateRowRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateRowsRequestOut"])
    types["BatchCreateRowsRequestIn"] = t.struct(
        {"requests": t.array(t.proxy(renames["CreateRowRequestIn"]))}
    ).named(renames["BatchCreateRowsRequestIn"])
    types["BatchCreateRowsRequestOut"] = t.struct(
        {
            "requests": t.array(t.proxy(renames["CreateRowRequestOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateRowsRequestOut"])
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
    types["CreateRowRequestIn"] = t.struct(
        {
            "row": t.proxy(renames["RowIn"]),
            "view": t.string().optional(),
            "parent": t.string(),
        }
    ).named(renames["CreateRowRequestIn"])
    types["CreateRowRequestOut"] = t.struct(
        {
            "row": t.proxy(renames["RowOut"]),
            "view": t.string().optional(),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateRowRequestOut"])
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
    types["RowIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RowIn"])
    types["RowOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RowOut"])
    types["BatchUpdateRowsResponseIn"] = t.struct(
        {"rows": t.array(t.proxy(renames["RowIn"])).optional()}
    ).named(renames["BatchUpdateRowsResponseIn"])
    types["BatchUpdateRowsResponseOut"] = t.struct(
        {
            "rows": t.array(t.proxy(renames["RowOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateRowsResponseOut"])
    types["BatchDeleteRowsRequestIn"] = t.struct({"names": t.array(t.string())}).named(
        renames["BatchDeleteRowsRequestIn"]
    )
    types["BatchDeleteRowsRequestOut"] = t.struct(
        {
            "names": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchDeleteRowsRequestOut"])
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
    types["RelationshipDetailsIn"] = t.struct(
        {"linkedTable": t.string().optional()}
    ).named(renames["RelationshipDetailsIn"])
    types["RelationshipDetailsOut"] = t.struct(
        {
            "linkedTable": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RelationshipDetailsOut"])

    functions = {}
    functions["tablesGet"] = area120tables.get(
        "v1alpha1/tables",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTablesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsGet"] = area120tables.get(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsCreate"] = area120tables.get(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsBatchDelete"] = area120tables.get(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsDelete"] = area120tables.get(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsBatchCreate"] = area120tables.get(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsPatch"] = area120tables.get(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsBatchUpdate"] = area120tables.get(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tablesRowsList"] = area120tables.get(
        "v1alpha1/{parent}/rows",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "view": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRowsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["workspacesGet"] = area120tables.get(
        "v1alpha1/workspaces",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
