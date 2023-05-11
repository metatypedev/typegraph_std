from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_connectors() -> Import:
    connectors = HTTPRuntime("https://connectors.googleapis.com/")

    renames = {
        "ErrorResponse": "_connectors_1_ErrorResponse",
        "QueryIn": "_connectors_2_QueryIn",
        "QueryOut": "_connectors_3_QueryOut",
        "ResultMetadataIn": "_connectors_4_ResultMetadataIn",
        "ResultMetadataOut": "_connectors_5_ResultMetadataOut",
        "ExecuteSqlQueryResponseIn": "_connectors_6_ExecuteSqlQueryResponseIn",
        "ExecuteSqlQueryResponseOut": "_connectors_7_ExecuteSqlQueryResponseOut",
        "ListEntitiesResponseIn": "_connectors_8_ListEntitiesResponseIn",
        "ListEntitiesResponseOut": "_connectors_9_ListEntitiesResponseOut",
        "EntityTypeIn": "_connectors_10_EntityTypeIn",
        "EntityTypeOut": "_connectors_11_EntityTypeOut",
        "ExecuteSqlQueryRequestIn": "_connectors_12_ExecuteSqlQueryRequestIn",
        "ExecuteSqlQueryRequestOut": "_connectors_13_ExecuteSqlQueryRequestOut",
        "EmptyIn": "_connectors_14_EmptyIn",
        "EmptyOut": "_connectors_15_EmptyOut",
        "UpdateEntitiesWithConditionsResponseIn": "_connectors_16_UpdateEntitiesWithConditionsResponseIn",
        "UpdateEntitiesWithConditionsResponseOut": "_connectors_17_UpdateEntitiesWithConditionsResponseOut",
        "ActionIn": "_connectors_18_ActionIn",
        "ActionOut": "_connectors_19_ActionOut",
        "ListActionsResponseIn": "_connectors_20_ListActionsResponseIn",
        "ListActionsResponseOut": "_connectors_21_ListActionsResponseOut",
        "ReferenceIn": "_connectors_22_ReferenceIn",
        "ReferenceOut": "_connectors_23_ReferenceOut",
        "EntityIn": "_connectors_24_EntityIn",
        "EntityOut": "_connectors_25_EntityOut",
        "ListEntityTypesResponseIn": "_connectors_26_ListEntityTypesResponseIn",
        "ListEntityTypesResponseOut": "_connectors_27_ListEntityTypesResponseOut",
        "FieldIn": "_connectors_28_FieldIn",
        "FieldOut": "_connectors_29_FieldOut",
        "ExecuteActionRequestIn": "_connectors_30_ExecuteActionRequestIn",
        "ExecuteActionRequestOut": "_connectors_31_ExecuteActionRequestOut",
        "ExecuteActionResponseIn": "_connectors_32_ExecuteActionResponseIn",
        "ExecuteActionResponseOut": "_connectors_33_ExecuteActionResponseOut",
        "InputParameterIn": "_connectors_34_InputParameterIn",
        "InputParameterOut": "_connectors_35_InputParameterOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["QueryIn"] = t.struct({"query": t.string()}).named(renames["QueryIn"])
    types["QueryOut"] = t.struct(
        {"query": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["QueryOut"])
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
    types["ExecuteSqlQueryResponseIn"] = t.struct(
        {"results": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["ExecuteSqlQueryResponseIn"])
    types["ExecuteSqlQueryResponseOut"] = t.struct(
        {
            "results": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlQueryResponseOut"])
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
    types["ExecuteSqlQueryRequestIn"] = t.struct(
        {"query": t.proxy(renames["QueryIn"])}
    ).named(renames["ExecuteSqlQueryRequestIn"])
    types["ExecuteSqlQueryRequestOut"] = t.struct(
        {
            "query": t.proxy(renames["QueryOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteSqlQueryRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ListActionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unsupportedActionNames": t.array(t.string()).optional(),
            "actions": t.array(t.proxy(renames["ActionIn"])).optional(),
        }
    ).named(renames["ListActionsResponseIn"])
    types["ListActionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unsupportedActionNames": t.array(t.string()).optional(),
            "actions": t.array(t.proxy(renames["ActionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListActionsResponseOut"])
    types["ReferenceIn"] = t.struct(
        {"name": t.string().optional(), "type": t.string().optional()}
    ).named(renames["ReferenceIn"])
    types["ReferenceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReferenceOut"])
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
    types["FieldIn"] = t.struct(
        {
            "nullable": t.boolean().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "key": t.boolean().optional(),
            "dataType": t.string().optional(),
            "additionalDetails": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "reference": t.proxy(renames["ReferenceIn"]).optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "nullable": t.boolean().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "key": t.boolean().optional(),
            "dataType": t.string().optional(),
            "additionalDetails": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "reference": t.proxy(renames["ReferenceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["ExecuteActionRequestIn"] = t.struct(
        {"parameters": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ExecuteActionRequestIn"])
    types["ExecuteActionRequestOut"] = t.struct(
        {
            "parameters": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteActionRequestOut"])
    types["ExecuteActionResponseIn"] = t.struct(
        {"results": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["ExecuteActionResponseIn"])
    types["ExecuteActionResponseOut"] = t.struct(
        {
            "results": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExecuteActionResponseOut"])
    types["InputParameterIn"] = t.struct(
        {
            "description": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["InputParameterIn"])
    types["InputParameterOut"] = t.struct(
        {
            "description": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nullable": t.boolean().optional(),
            "dataType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InputParameterOut"])

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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEntityTypesResponseOut"]),
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
        importer="connectors", renames=renames, types=types, functions=functions
    )
