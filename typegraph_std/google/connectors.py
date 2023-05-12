from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_connectors() -> Import:
    connectors = HTTPRuntime("https://connectors.googleapis.com/")

    renames = {
        "ErrorResponse": "_connectors_1_ErrorResponse",
        "ListEntityTypesResponseIn": "_connectors_2_ListEntityTypesResponseIn",
        "ListEntityTypesResponseOut": "_connectors_3_ListEntityTypesResponseOut",
        "InputParameterIn": "_connectors_4_InputParameterIn",
        "InputParameterOut": "_connectors_5_InputParameterOut",
        "ExecuteSqlQueryRequestIn": "_connectors_6_ExecuteSqlQueryRequestIn",
        "ExecuteSqlQueryRequestOut": "_connectors_7_ExecuteSqlQueryRequestOut",
        "ListActionsResponseIn": "_connectors_8_ListActionsResponseIn",
        "ListActionsResponseOut": "_connectors_9_ListActionsResponseOut",
        "EntityIn": "_connectors_10_EntityIn",
        "EntityOut": "_connectors_11_EntityOut",
        "ActionIn": "_connectors_12_ActionIn",
        "ActionOut": "_connectors_13_ActionOut",
        "ResultMetadataIn": "_connectors_14_ResultMetadataIn",
        "ResultMetadataOut": "_connectors_15_ResultMetadataOut",
        "FieldIn": "_connectors_16_FieldIn",
        "FieldOut": "_connectors_17_FieldOut",
        "ExecuteSqlQueryResponseIn": "_connectors_18_ExecuteSqlQueryResponseIn",
        "ExecuteSqlQueryResponseOut": "_connectors_19_ExecuteSqlQueryResponseOut",
        "ExecuteActionResponseIn": "_connectors_20_ExecuteActionResponseIn",
        "ExecuteActionResponseOut": "_connectors_21_ExecuteActionResponseOut",
        "ListEntitiesResponseIn": "_connectors_22_ListEntitiesResponseIn",
        "ListEntitiesResponseOut": "_connectors_23_ListEntitiesResponseOut",
        "UpdateEntitiesWithConditionsResponseIn": "_connectors_24_UpdateEntitiesWithConditionsResponseIn",
        "UpdateEntitiesWithConditionsResponseOut": "_connectors_25_UpdateEntitiesWithConditionsResponseOut",
        "EntityTypeIn": "_connectors_26_EntityTypeIn",
        "EntityTypeOut": "_connectors_27_EntityTypeOut",
        "ReferenceIn": "_connectors_28_ReferenceIn",
        "ReferenceOut": "_connectors_29_ReferenceOut",
        "EmptyIn": "_connectors_30_EmptyIn",
        "EmptyOut": "_connectors_31_EmptyOut",
        "ExecuteActionRequestIn": "_connectors_32_ExecuteActionRequestIn",
        "ExecuteActionRequestOut": "_connectors_33_ExecuteActionRequestOut",
        "QueryIn": "_connectors_34_QueryIn",
        "QueryOut": "_connectors_35_QueryOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["InputParameterIn"] = t.struct(
        {
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["InputParameterIn"])
    types["InputParameterOut"] = t.struct(
        {
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputParameterOut"])
    types["ExecuteSqlQueryRequestIn"] = t.struct(
        {"query": t.proxy(renames["QueryIn"])}
    ).named(renames["ExecuteSqlQueryRequestIn"])
    types["ExecuteSqlQueryRequestOut"] = t.struct(
        {
            "query": t.proxy(renames["QueryOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlQueryRequestOut"])
    types["ListActionsResponseIn"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "unsupportedActionNames": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListActionsResponseIn"])
    types["ListActionsResponseOut"] = t.struct(
        {
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "unsupportedActionNames": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListActionsResponseOut"])
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
    types["ActionIn"] = t.struct(
        {
            "resultMetadata": t.array(t.proxy(renames["ResultMetadataIn"])).optional(),
            "inputParameters": t.array(t.proxy(renames["InputParameterIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ActionIn"])
    types["ActionOut"] = t.struct(
        {
            "resultMetadata": t.array(t.proxy(renames["ResultMetadataOut"])).optional(),
            "inputParameters": t.array(
                t.proxy(renames["InputParameterOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ActionOut"])
    types["ResultMetadataIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "dataType": t.string().optional(),
        }
    ).named(renames["ResultMetadataIn"])
    types["ResultMetadataOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "dataType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultMetadataOut"])
    types["FieldIn"] = t.struct(
        {
            "key": t.boolean().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "dataType": t.string().optional(),
            "reference": t.proxy(renames["ReferenceIn"]).optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "additionalDetails": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "key": t.boolean().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "dataType": t.string().optional(),
            "reference": t.proxy(renames["ReferenceOut"]).optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "additionalDetails": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["ExecuteSqlQueryResponseIn"] = t.struct(
        {"results": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["ExecuteSqlQueryResponseIn"])
    types["ExecuteSqlQueryResponseOut"] = t.struct(
        {
            "results": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlQueryResponseOut"])
    types["ExecuteActionResponseIn"] = t.struct(
        {"results": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["ExecuteActionResponseIn"])
    types["ExecuteActionResponseOut"] = t.struct(
        {
            "results": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteActionResponseOut"])
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
    types["UpdateEntitiesWithConditionsResponseIn"] = t.struct(
        {"response": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["UpdateEntitiesWithConditionsResponseIn"])
    types["UpdateEntitiesWithConditionsResponseOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEntitiesWithConditionsResponseOut"])
    types["EntityTypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
        }
    ).named(renames["EntityTypeIn"])
    types["EntityTypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityTypeOut"])
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
    types["QueryIn"] = t.struct({"query": t.string()}).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {"query": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QueryOut"])

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
    functions["projectsLocationsConnectionsEntityTypesList"] = connectors.get(
        "v2/{parent}/entityTypes",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntityTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesCreate"
    ] = connectors.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesUpdateEntitiesWithConditions"
    ] = connectors.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsEntityTypesEntitiesGet"] = connectors.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesDeleteEntitiesWithConditions"
    ] = connectors.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsEntityTypesEntitiesList"] = connectors.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesDelete"
    ] = connectors.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesPatch"
    ] = connectors.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "fields": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntityOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsActionsExecute"] = connectors.get(
        "v2/{parent}/actions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsActionsList"] = connectors.get(
        "v2/{parent}/actions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListActionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="connectors",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
