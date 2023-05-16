from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_connectors() -> Import:
    connectors = HTTPRuntime("https://connectors.googleapis.com/")

    renames = {
        "ErrorResponse": "_connectors_1_ErrorResponse",
        "ExecuteSqlQueryRequestIn": "_connectors_2_ExecuteSqlQueryRequestIn",
        "ExecuteSqlQueryRequestOut": "_connectors_3_ExecuteSqlQueryRequestOut",
        "EntityIn": "_connectors_4_EntityIn",
        "EntityOut": "_connectors_5_EntityOut",
        "EmptyIn": "_connectors_6_EmptyIn",
        "EmptyOut": "_connectors_7_EmptyOut",
        "QueryIn": "_connectors_8_QueryIn",
        "QueryOut": "_connectors_9_QueryOut",
        "ExecuteSqlQueryResponseIn": "_connectors_10_ExecuteSqlQueryResponseIn",
        "ExecuteSqlQueryResponseOut": "_connectors_11_ExecuteSqlQueryResponseOut",
        "ExecuteActionResponseIn": "_connectors_12_ExecuteActionResponseIn",
        "ExecuteActionResponseOut": "_connectors_13_ExecuteActionResponseOut",
        "ListEntitiesResponseIn": "_connectors_14_ListEntitiesResponseIn",
        "ListEntitiesResponseOut": "_connectors_15_ListEntitiesResponseOut",
        "ExecuteActionRequestIn": "_connectors_16_ExecuteActionRequestIn",
        "ExecuteActionRequestOut": "_connectors_17_ExecuteActionRequestOut",
        "InputParameterIn": "_connectors_18_InputParameterIn",
        "InputParameterOut": "_connectors_19_InputParameterOut",
        "ActionIn": "_connectors_20_ActionIn",
        "ActionOut": "_connectors_21_ActionOut",
        "EntityTypeIn": "_connectors_22_EntityTypeIn",
        "EntityTypeOut": "_connectors_23_EntityTypeOut",
        "ListEntityTypesResponseIn": "_connectors_24_ListEntityTypesResponseIn",
        "ListEntityTypesResponseOut": "_connectors_25_ListEntityTypesResponseOut",
        "ReferenceIn": "_connectors_26_ReferenceIn",
        "ReferenceOut": "_connectors_27_ReferenceOut",
        "ResultMetadataIn": "_connectors_28_ResultMetadataIn",
        "ResultMetadataOut": "_connectors_29_ResultMetadataOut",
        "ListActionsResponseIn": "_connectors_30_ListActionsResponseIn",
        "ListActionsResponseOut": "_connectors_31_ListActionsResponseOut",
        "UpdateEntitiesWithConditionsResponseIn": "_connectors_32_UpdateEntitiesWithConditionsResponseIn",
        "UpdateEntitiesWithConditionsResponseOut": "_connectors_33_UpdateEntitiesWithConditionsResponseOut",
        "FieldIn": "_connectors_34_FieldIn",
        "FieldOut": "_connectors_35_FieldOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExecuteSqlQueryRequestIn"] = t.struct(
        {"query": t.proxy(renames["QueryIn"])}
    ).named(renames["ExecuteSqlQueryRequestIn"])
    types["ExecuteSqlQueryRequestOut"] = t.struct(
        {
            "query": t.proxy(renames["QueryOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlQueryRequestOut"])
    types["EntityIn"] = t.struct(
        {"fields": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "fields": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["QueryIn"] = t.struct({"query": t.string()}).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {"query": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QueryOut"])
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
    types["ExecuteActionRequestIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExecuteActionRequestIn"])
    types["ExecuteActionRequestOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteActionRequestOut"])
    types["InputParameterIn"] = t.struct(
        {
            "dataType": t.string().optional(),
            "nullable": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["InputParameterIn"])
    types["InputParameterOut"] = t.struct(
        {
            "dataType": t.string().optional(),
            "nullable": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputParameterOut"])
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
    types["ListEntityTypesResponseIn"] = t.struct(
        {
            "unsupportedTypeNames": t.array(t.string()).optional(),
            "types": t.array(t.proxy(renames["EntityTypeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEntityTypesResponseIn"])
    types["ListEntityTypesResponseOut"] = t.struct(
        {
            "unsupportedTypeNames": t.array(t.string()).optional(),
            "types": t.array(t.proxy(renames["EntityTypeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEntityTypesResponseOut"])
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
    types["ResultMetadataIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dataType": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ResultMetadataIn"])
    types["ResultMetadataOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dataType": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResultMetadataOut"])
    types["ListActionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
            "unsupportedActionNames": t.array(t.string()).optional(),
        }
    ).named(renames["ListActionsResponseIn"])
    types["ListActionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "unsupportedActionNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListActionsResponseOut"])
    types["UpdateEntitiesWithConditionsResponseIn"] = t.struct(
        {"response": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["UpdateEntitiesWithConditionsResponseIn"])
    types["UpdateEntitiesWithConditionsResponseOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateEntitiesWithConditionsResponseOut"])
    types["FieldIn"] = t.struct(
        {
            "key": t.boolean().optional(),
            "name": t.string().optional(),
            "nullable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "reference": t.proxy(renames["ReferenceIn"]).optional(),
            "additionalDetails": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "key": t.boolean().optional(),
            "name": t.string().optional(),
            "nullable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "reference": t.proxy(renames["ReferenceOut"]).optional(),
            "additionalDetails": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])

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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntityTypesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesUpdateEntitiesWithConditions"
    ] = connectors.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesDeleteEntitiesWithConditions"
    ] = connectors.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsConnectionsEntityTypesEntitiesGet"] = connectors.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesList"
    ] = connectors.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesPatch"
    ] = connectors.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesCreate"
    ] = connectors.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsConnectionsEntityTypesEntitiesDelete"
    ] = connectors.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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

    return Import(
        importer="connectors",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
