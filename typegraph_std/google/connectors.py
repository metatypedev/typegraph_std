from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_connectors():
    connectors = HTTPRuntime("https://connectors.googleapis.com/")

    renames = {
        "ErrorResponse": "_connectors_1_ErrorResponse",
        "FieldIn": "_connectors_2_FieldIn",
        "FieldOut": "_connectors_3_FieldOut",
        "ExecuteSqlQueryRequestIn": "_connectors_4_ExecuteSqlQueryRequestIn",
        "ExecuteSqlQueryRequestOut": "_connectors_5_ExecuteSqlQueryRequestOut",
        "QueryIn": "_connectors_6_QueryIn",
        "QueryOut": "_connectors_7_QueryOut",
        "ReferenceIn": "_connectors_8_ReferenceIn",
        "ReferenceOut": "_connectors_9_ReferenceOut",
        "ListEntityTypesResponseIn": "_connectors_10_ListEntityTypesResponseIn",
        "ListEntityTypesResponseOut": "_connectors_11_ListEntityTypesResponseOut",
        "EntityIn": "_connectors_12_EntityIn",
        "EntityOut": "_connectors_13_EntityOut",
        "ListActionsResponseIn": "_connectors_14_ListActionsResponseIn",
        "ListActionsResponseOut": "_connectors_15_ListActionsResponseOut",
        "InputParameterIn": "_connectors_16_InputParameterIn",
        "InputParameterOut": "_connectors_17_InputParameterOut",
        "EmptyIn": "_connectors_18_EmptyIn",
        "EmptyOut": "_connectors_19_EmptyOut",
        "ExecuteActionRequestIn": "_connectors_20_ExecuteActionRequestIn",
        "ExecuteActionRequestOut": "_connectors_21_ExecuteActionRequestOut",
        "UpdateEntitiesWithConditionsResponseIn": "_connectors_22_UpdateEntitiesWithConditionsResponseIn",
        "UpdateEntitiesWithConditionsResponseOut": "_connectors_23_UpdateEntitiesWithConditionsResponseOut",
        "ActionIn": "_connectors_24_ActionIn",
        "ActionOut": "_connectors_25_ActionOut",
        "ListEntitiesResponseIn": "_connectors_26_ListEntitiesResponseIn",
        "ListEntitiesResponseOut": "_connectors_27_ListEntitiesResponseOut",
        "ExecuteActionResponseIn": "_connectors_28_ExecuteActionResponseIn",
        "ExecuteActionResponseOut": "_connectors_29_ExecuteActionResponseOut",
        "EntityTypeIn": "_connectors_30_EntityTypeIn",
        "EntityTypeOut": "_connectors_31_EntityTypeOut",
        "ExecuteSqlQueryResponseIn": "_connectors_32_ExecuteSqlQueryResponseIn",
        "ExecuteSqlQueryResponseOut": "_connectors_33_ExecuteSqlQueryResponseOut",
        "ResultMetadataIn": "_connectors_34_ResultMetadataIn",
        "ResultMetadataOut": "_connectors_35_ResultMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FieldIn"] = t.struct(
        {
            "additionalDetails": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "dataType": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "reference": t.proxy(renames["ReferenceIn"]).optional(),
            "key": t.boolean().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "additionalDetails": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "dataType": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "reference": t.proxy(renames["ReferenceOut"]).optional(),
            "key": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["ExecuteSqlQueryRequestIn"] = t.struct(
        {"query": t.proxy(renames["QueryIn"])}
    ).named(renames["ExecuteSqlQueryRequestIn"])
    types["ExecuteSqlQueryRequestOut"] = t.struct(
        {
            "query": t.proxy(renames["QueryOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlQueryRequestOut"])
    types["QueryIn"] = t.struct({"query": t.string()}).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {"query": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QueryOut"])
    types["ReferenceIn"] = t.struct(
        {"type": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ReferenceIn"])
    types["ReferenceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceOut"])
    types["ListEntityTypesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unsupportedTypeNames": t.array(t.string()).optional(),
            "types": t.array(t.proxy(renames["EntityTypeIn"])).optional(),
        }
    ).named(renames["ListEntityTypesResponseIn"])
    types["ListEntityTypesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unsupportedTypeNames": t.array(t.string()).optional(),
            "types": t.array(t.proxy(renames["EntityTypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEntityTypesResponseOut"])
    types["EntityIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["ListActionsResponseIn"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unsupportedActionNames": t.array(t.string()).optional(),
        }
    ).named(renames["ListActionsResponseIn"])
    types["ListActionsResponseOut"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unsupportedActionNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListActionsResponseOut"])
    types["InputParameterIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dataType": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["InputParameterIn"])
    types["InputParameterOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dataType": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputParameterOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ExecuteActionRequestIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExecuteActionRequestIn"])
    types["ExecuteActionRequestOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteActionRequestOut"])
    types["UpdateEntitiesWithConditionsResponseIn"] = t.struct(
        {"response": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["UpdateEntitiesWithConditionsResponseIn"])
    types["UpdateEntitiesWithConditionsResponseOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEntitiesWithConditionsResponseOut"])
    types["ActionIn"] = t.struct(
        {
            "resultMetadata": t.array(t.proxy(renames["ResultMetadataIn"])).optional(),
            "name": t.string().optional(),
            "inputParameters": t.array(t.proxy(renames["InputParameterIn"])).optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "resultMetadata": t.array(t.proxy(renames["ResultMetadataOut"])).optional(),
            "name": t.string().optional(),
            "inputParameters": t.array(
                t.proxy(renames["InputParameterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["ListEntitiesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
        }
    ).named(renames["ListEntitiesResponseIn"])
    types["ListEntitiesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEntitiesResponseOut"])
    types["ExecuteActionResponseIn"] = t.struct(
        {"results": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["ExecuteActionResponseIn"])
    types["ExecuteActionResponseOut"] = t.struct(
        {
            "results": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteActionResponseOut"])
    types["EntityTypeIn"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EntityTypeIn"])
    types["EntityTypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityTypeOut"])
    types["ExecuteSqlQueryResponseIn"] = t.struct(
        {"results": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["ExecuteSqlQueryResponseIn"])
    types["ExecuteSqlQueryResponseOut"] = t.struct(
        {
            "results": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlQueryResponseOut"])
    types["ResultMetadataIn"] = t.struct(
        {
            "dataType": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ResultMetadataIn"])
    types["ResultMetadataOut"] = t.struct(
        {
            "dataType": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultMetadataOut"])

    functions = {}
    functions["projectsLocationsConnectionsExecuteSqlQuery"] = connectors.post(
        "v2/{connection}:executeSqlQuery",
        t.struct(
            {
                "connection": t.string(),
                "query": t.proxy(renames["QueryIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteSqlQueryResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsActionsList"] = connectors.post(
        "v2/{name}:execute",
        t.struct(
            {
                "name": t.string(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteActionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsActionsExecute"] = connectors.post(
        "v2/{name}:execute",
        t.struct(
            {
                "name": t.string(),
                "parameters": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ExecuteActionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsEntityTypesList"] = connectors.get(
        "v2/{parent}/entityTypes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntityTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsEntityTypesEntitiesDelete"] = connectors.get(
        "v2/{parent}/entities",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "sortBy": t.string().optional(),
                "parent": t.string(),
                "conditions": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsEntityTypesEntitiesPatch"] = connectors.get(
        "v2/{parent}/entities",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "sortBy": t.string().optional(),
                "parent": t.string(),
                "conditions": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesDeleteEntitiesWithConditions"
    ] = connectors.get(
        "v2/{parent}/entities",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "sortBy": t.string().optional(),
                "parent": t.string(),
                "conditions": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesUpdateEntitiesWithConditions"
    ] = connectors.get(
        "v2/{parent}/entities",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "sortBy": t.string().optional(),
                "parent": t.string(),
                "conditions": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsEntityTypesEntitiesGet"] = connectors.get(
        "v2/{parent}/entities",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "sortBy": t.string().optional(),
                "parent": t.string(),
                "conditions": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsEntityTypesEntitiesCreate"] = connectors.get(
        "v2/{parent}/entities",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "sortBy": t.string().optional(),
                "parent": t.string(),
                "conditions": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsEntityTypesEntitiesList"] = connectors.get(
        "v2/{parent}/entities",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "sortBy": t.string().optional(),
                "parent": t.string(),
                "conditions": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntitiesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="connectors",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
