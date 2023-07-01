from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_apigateway():
    apigateway = HTTPRuntime("https://apigateway.googleapis.com/")

    renames = {
        "ErrorResponse": "_apigateway_1_ErrorResponse",
        "ApigatewayListApisResponseIn": "_apigateway_2_ApigatewayListApisResponseIn",
        "ApigatewayListApisResponseOut": "_apigateway_3_ApigatewayListApisResponseOut",
        "EmptyIn": "_apigateway_4_EmptyIn",
        "EmptyOut": "_apigateway_5_EmptyOut",
        "ApigatewayTestIamPermissionsResponseIn": "_apigateway_6_ApigatewayTestIamPermissionsResponseIn",
        "ApigatewayTestIamPermissionsResponseOut": "_apigateway_7_ApigatewayTestIamPermissionsResponseOut",
        "ApigatewayOperationMetadataDiagnosticIn": "_apigateway_8_ApigatewayOperationMetadataDiagnosticIn",
        "ApigatewayOperationMetadataDiagnosticOut": "_apigateway_9_ApigatewayOperationMetadataDiagnosticOut",
        "ApigatewayBindingIn": "_apigateway_10_ApigatewayBindingIn",
        "ApigatewayBindingOut": "_apigateway_11_ApigatewayBindingOut",
        "ApigatewayApiConfigOpenApiDocumentIn": "_apigateway_12_ApigatewayApiConfigOpenApiDocumentIn",
        "ApigatewayApiConfigOpenApiDocumentOut": "_apigateway_13_ApigatewayApiConfigOpenApiDocumentOut",
        "ApigatewayCancelOperationRequestIn": "_apigateway_14_ApigatewayCancelOperationRequestIn",
        "ApigatewayCancelOperationRequestOut": "_apigateway_15_ApigatewayCancelOperationRequestOut",
        "ApigatewayOperationMetadataIn": "_apigateway_16_ApigatewayOperationMetadataIn",
        "ApigatewayOperationMetadataOut": "_apigateway_17_ApigatewayOperationMetadataOut",
        "ApigatewaySetIamPolicyRequestIn": "_apigateway_18_ApigatewaySetIamPolicyRequestIn",
        "ApigatewaySetIamPolicyRequestOut": "_apigateway_19_ApigatewaySetIamPolicyRequestOut",
        "ApigatewayAuditConfigIn": "_apigateway_20_ApigatewayAuditConfigIn",
        "ApigatewayAuditConfigOut": "_apigateway_21_ApigatewayAuditConfigOut",
        "ApigatewayLocationIn": "_apigateway_22_ApigatewayLocationIn",
        "ApigatewayLocationOut": "_apigateway_23_ApigatewayLocationOut",
        "ApigatewayExprIn": "_apigateway_24_ApigatewayExprIn",
        "ApigatewayExprOut": "_apigateway_25_ApigatewayExprOut",
        "ApigatewayGatewayIn": "_apigateway_26_ApigatewayGatewayIn",
        "ApigatewayGatewayOut": "_apigateway_27_ApigatewayGatewayOut",
        "ApigatewayApiIn": "_apigateway_28_ApigatewayApiIn",
        "ApigatewayApiOut": "_apigateway_29_ApigatewayApiOut",
        "ApigatewayTestIamPermissionsRequestIn": "_apigateway_30_ApigatewayTestIamPermissionsRequestIn",
        "ApigatewayTestIamPermissionsRequestOut": "_apigateway_31_ApigatewayTestIamPermissionsRequestOut",
        "ApigatewayApiConfigFileIn": "_apigateway_32_ApigatewayApiConfigFileIn",
        "ApigatewayApiConfigFileOut": "_apigateway_33_ApigatewayApiConfigFileOut",
        "ApigatewayListApiConfigsResponseIn": "_apigateway_34_ApigatewayListApiConfigsResponseIn",
        "ApigatewayListApiConfigsResponseOut": "_apigateway_35_ApigatewayListApiConfigsResponseOut",
        "ApigatewayStatusIn": "_apigateway_36_ApigatewayStatusIn",
        "ApigatewayStatusOut": "_apigateway_37_ApigatewayStatusOut",
        "ApigatewayListGatewaysResponseIn": "_apigateway_38_ApigatewayListGatewaysResponseIn",
        "ApigatewayListGatewaysResponseOut": "_apigateway_39_ApigatewayListGatewaysResponseOut",
        "ApigatewayPolicyIn": "_apigateway_40_ApigatewayPolicyIn",
        "ApigatewayPolicyOut": "_apigateway_41_ApigatewayPolicyOut",
        "ApigatewayApiConfigIn": "_apigateway_42_ApigatewayApiConfigIn",
        "ApigatewayApiConfigOut": "_apigateway_43_ApigatewayApiConfigOut",
        "ApigatewayListOperationsResponseIn": "_apigateway_44_ApigatewayListOperationsResponseIn",
        "ApigatewayListOperationsResponseOut": "_apigateway_45_ApigatewayListOperationsResponseOut",
        "ApigatewayApiConfigGrpcServiceDefinitionIn": "_apigateway_46_ApigatewayApiConfigGrpcServiceDefinitionIn",
        "ApigatewayApiConfigGrpcServiceDefinitionOut": "_apigateway_47_ApigatewayApiConfigGrpcServiceDefinitionOut",
        "ApigatewayOperationIn": "_apigateway_48_ApigatewayOperationIn",
        "ApigatewayOperationOut": "_apigateway_49_ApigatewayOperationOut",
        "ApigatewayAuditLogConfigIn": "_apigateway_50_ApigatewayAuditLogConfigIn",
        "ApigatewayAuditLogConfigOut": "_apigateway_51_ApigatewayAuditLogConfigOut",
        "ApigatewayListLocationsResponseIn": "_apigateway_52_ApigatewayListLocationsResponseIn",
        "ApigatewayListLocationsResponseOut": "_apigateway_53_ApigatewayListLocationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ApigatewayListApisResponseIn"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "apis": t.array(t.proxy(renames["ApigatewayApiIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ApigatewayListApisResponseIn"])
    types["ApigatewayListApisResponseOut"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "apis": t.array(t.proxy(renames["ApigatewayApiOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayListApisResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ApigatewayTestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["ApigatewayTestIamPermissionsResponseIn"])
    types["ApigatewayTestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayTestIamPermissionsResponseOut"])
    types["ApigatewayOperationMetadataDiagnosticIn"] = t.struct(
        {"location": t.string().optional(), "message": t.string().optional()}
    ).named(renames["ApigatewayOperationMetadataDiagnosticIn"])
    types["ApigatewayOperationMetadataDiagnosticOut"] = t.struct(
        {
            "location": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayOperationMetadataDiagnosticOut"])
    types["ApigatewayBindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ApigatewayExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["ApigatewayBindingIn"])
    types["ApigatewayBindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ApigatewayExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayBindingOut"])
    types["ApigatewayApiConfigOpenApiDocumentIn"] = t.struct(
        {"document": t.proxy(renames["ApigatewayApiConfigFileIn"]).optional()}
    ).named(renames["ApigatewayApiConfigOpenApiDocumentIn"])
    types["ApigatewayApiConfigOpenApiDocumentOut"] = t.struct(
        {
            "document": t.proxy(renames["ApigatewayApiConfigFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayApiConfigOpenApiDocumentOut"])
    types["ApigatewayCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ApigatewayCancelOperationRequestIn"])
    types["ApigatewayCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApigatewayCancelOperationRequestOut"])
    types["ApigatewayOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ApigatewayOperationMetadataIn"])
    types["ApigatewayOperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "diagnostics": t.array(
                t.proxy(renames["ApigatewayOperationMetadataDiagnosticOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayOperationMetadataOut"])
    types["ApigatewaySetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["ApigatewayPolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["ApigatewaySetIamPolicyRequestIn"])
    types["ApigatewaySetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["ApigatewayPolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewaySetIamPolicyRequestOut"])
    types["ApigatewayAuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["ApigatewayAuditLogConfigIn"])
            ).optional(),
        }
    ).named(renames["ApigatewayAuditConfigIn"])
    types["ApigatewayAuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["ApigatewayAuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayAuditConfigOut"])
    types["ApigatewayLocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ApigatewayLocationIn"])
    types["ApigatewayLocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayLocationOut"])
    types["ApigatewayExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ApigatewayExprIn"])
    types["ApigatewayExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayExprOut"])
    types["ApigatewayGatewayIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "apiConfig": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ApigatewayGatewayIn"])
    types["ApigatewayGatewayOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "defaultHostname": t.string().optional(),
            "displayName": t.string().optional(),
            "apiConfig": t.string(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayGatewayOut"])
    types["ApigatewayApiIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "managedService": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ApigatewayApiIn"])
    types["ApigatewayApiOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "managedService": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayApiOut"])
    types["ApigatewayTestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["ApigatewayTestIamPermissionsRequestIn"])
    types["ApigatewayTestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayTestIamPermissionsRequestOut"])
    types["ApigatewayApiConfigFileIn"] = t.struct(
        {"contents": t.string().optional(), "path": t.string().optional()}
    ).named(renames["ApigatewayApiConfigFileIn"])
    types["ApigatewayApiConfigFileOut"] = t.struct(
        {
            "contents": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayApiConfigFileOut"])
    types["ApigatewayListApiConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiConfigs": t.array(t.proxy(renames["ApigatewayApiConfigIn"])).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
        }
    ).named(renames["ApigatewayListApiConfigsResponseIn"])
    types["ApigatewayListApiConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiConfigs": t.array(
                t.proxy(renames["ApigatewayApiConfigOut"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayListApiConfigsResponseOut"])
    types["ApigatewayStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["ApigatewayStatusIn"])
    types["ApigatewayStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayStatusOut"])
    types["ApigatewayListGatewaysResponseIn"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "gateways": t.array(t.proxy(renames["ApigatewayGatewayIn"])).optional(),
        }
    ).named(renames["ApigatewayListGatewaysResponseIn"])
    types["ApigatewayListGatewaysResponseOut"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "gateways": t.array(t.proxy(renames["ApigatewayGatewayOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayListGatewaysResponseOut"])
    types["ApigatewayPolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["ApigatewayBindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["ApigatewayAuditConfigIn"])
            ).optional(),
        }
    ).named(renames["ApigatewayPolicyIn"])
    types["ApigatewayPolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["ApigatewayBindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["ApigatewayAuditConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayPolicyOut"])
    types["ApigatewayApiConfigIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "grpcServices": t.array(
                t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
            ).optional(),
            "managedServiceConfigs": t.array(
                t.proxy(renames["ApigatewayApiConfigFileIn"])
            ).optional(),
            "gatewayServiceAccount": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "openapiDocuments": t.array(
                t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
            ).optional(),
        }
    ).named(renames["ApigatewayApiConfigIn"])
    types["ApigatewayApiConfigOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "grpcServices": t.array(
                t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "managedServiceConfigs": t.array(
                t.proxy(renames["ApigatewayApiConfigFileOut"])
            ).optional(),
            "state": t.string().optional(),
            "gatewayServiceAccount": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "serviceConfigId": t.string().optional(),
            "openapiDocuments": t.array(
                t.proxy(renames["ApigatewayApiConfigOpenApiDocumentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayApiConfigOut"])
    types["ApigatewayListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["ApigatewayOperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ApigatewayListOperationsResponseIn"])
    types["ApigatewayListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["ApigatewayOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayListOperationsResponseOut"])
    types["ApigatewayApiConfigGrpcServiceDefinitionIn"] = t.struct(
        {
            "fileDescriptorSet": t.proxy(
                renames["ApigatewayApiConfigFileIn"]
            ).optional(),
            "source": t.array(t.proxy(renames["ApigatewayApiConfigFileIn"])).optional(),
        }
    ).named(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
    types["ApigatewayApiConfigGrpcServiceDefinitionOut"] = t.struct(
        {
            "fileDescriptorSet": t.proxy(
                renames["ApigatewayApiConfigFileOut"]
            ).optional(),
            "source": t.array(
                t.proxy(renames["ApigatewayApiConfigFileOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayApiConfigGrpcServiceDefinitionOut"])
    types["ApigatewayOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ApigatewayStatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApigatewayOperationIn"])
    types["ApigatewayOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApigatewayOperationOut"])
    types["ApigatewayAuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["ApigatewayAuditLogConfigIn"])
    types["ApigatewayAuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayAuditLogConfigOut"])
    types["ApigatewayListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["ApigatewayLocationIn"])).optional(),
        }
    ).named(renames["ApigatewayListLocationsResponseIn"])
    types["ApigatewayListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["ApigatewayLocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayListLocationsResponseOut"])

    functions = {}
    functions["projectsLocationsList"] = apigateway.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayLocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = apigateway.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayLocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = apigateway.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = apigateway.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = apigateway.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = apigateway.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisTestIamPermissions"] = apigateway.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisSetIamPolicy"] = apigateway.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisList"] = apigateway.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDelete"] = apigateway.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisCreate"] = apigateway.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisPatch"] = apigateway.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGet"] = apigateway.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGetIamPolicy"] = apigateway.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsGetIamPolicy"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsGet"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsCreate"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsSetIamPolicy"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsList"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsPatch"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsTestIamPermissions"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsDelete"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysCreate"] = apigateway.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["ApigatewayPolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysList"] = apigateway.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["ApigatewayPolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysDelete"] = apigateway.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["ApigatewayPolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysTestIamPermissions"] = apigateway.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["ApigatewayPolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysGetIamPolicy"] = apigateway.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["ApigatewayPolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysGet"] = apigateway.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["ApigatewayPolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysPatch"] = apigateway.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["ApigatewayPolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGatewaysSetIamPolicy"] = apigateway.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["ApigatewayPolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="apigateway",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
