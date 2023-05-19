from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_apigateway() -> Import:
    apigateway = HTTPRuntime("https://apigateway.googleapis.com/")

    renames = {
        "ErrorResponse": "_apigateway_1_ErrorResponse",
        "ApigatewayBindingIn": "_apigateway_2_ApigatewayBindingIn",
        "ApigatewayBindingOut": "_apigateway_3_ApigatewayBindingOut",
        "ApigatewayTestIamPermissionsRequestIn": "_apigateway_4_ApigatewayTestIamPermissionsRequestIn",
        "ApigatewayTestIamPermissionsRequestOut": "_apigateway_5_ApigatewayTestIamPermissionsRequestOut",
        "ApigatewayListApisResponseIn": "_apigateway_6_ApigatewayListApisResponseIn",
        "ApigatewayListApisResponseOut": "_apigateway_7_ApigatewayListApisResponseOut",
        "ApigatewayListLocationsResponseIn": "_apigateway_8_ApigatewayListLocationsResponseIn",
        "ApigatewayListLocationsResponseOut": "_apigateway_9_ApigatewayListLocationsResponseOut",
        "ApigatewayApiConfigIn": "_apigateway_10_ApigatewayApiConfigIn",
        "ApigatewayApiConfigOut": "_apigateway_11_ApigatewayApiConfigOut",
        "ApigatewayListOperationsResponseIn": "_apigateway_12_ApigatewayListOperationsResponseIn",
        "ApigatewayListOperationsResponseOut": "_apigateway_13_ApigatewayListOperationsResponseOut",
        "ApigatewayAuditConfigIn": "_apigateway_14_ApigatewayAuditConfigIn",
        "ApigatewayAuditConfigOut": "_apigateway_15_ApigatewayAuditConfigOut",
        "ApigatewayCancelOperationRequestIn": "_apigateway_16_ApigatewayCancelOperationRequestIn",
        "ApigatewayCancelOperationRequestOut": "_apigateway_17_ApigatewayCancelOperationRequestOut",
        "ApigatewayListApiConfigsResponseIn": "_apigateway_18_ApigatewayListApiConfigsResponseIn",
        "ApigatewayListApiConfigsResponseOut": "_apigateway_19_ApigatewayListApiConfigsResponseOut",
        "ApigatewayGatewayIn": "_apigateway_20_ApigatewayGatewayIn",
        "ApigatewayGatewayOut": "_apigateway_21_ApigatewayGatewayOut",
        "ApigatewayAuditLogConfigIn": "_apigateway_22_ApigatewayAuditLogConfigIn",
        "ApigatewayAuditLogConfigOut": "_apigateway_23_ApigatewayAuditLogConfigOut",
        "ApigatewayTestIamPermissionsResponseIn": "_apigateway_24_ApigatewayTestIamPermissionsResponseIn",
        "ApigatewayTestIamPermissionsResponseOut": "_apigateway_25_ApigatewayTestIamPermissionsResponseOut",
        "ApigatewayExprIn": "_apigateway_26_ApigatewayExprIn",
        "ApigatewayExprOut": "_apigateway_27_ApigatewayExprOut",
        "ApigatewayStatusIn": "_apigateway_28_ApigatewayStatusIn",
        "ApigatewayStatusOut": "_apigateway_29_ApigatewayStatusOut",
        "ApigatewayApiConfigOpenApiDocumentIn": "_apigateway_30_ApigatewayApiConfigOpenApiDocumentIn",
        "ApigatewayApiConfigOpenApiDocumentOut": "_apigateway_31_ApigatewayApiConfigOpenApiDocumentOut",
        "ApigatewaySetIamPolicyRequestIn": "_apigateway_32_ApigatewaySetIamPolicyRequestIn",
        "ApigatewaySetIamPolicyRequestOut": "_apigateway_33_ApigatewaySetIamPolicyRequestOut",
        "EmptyIn": "_apigateway_34_EmptyIn",
        "EmptyOut": "_apigateway_35_EmptyOut",
        "ApigatewayOperationMetadataIn": "_apigateway_36_ApigatewayOperationMetadataIn",
        "ApigatewayOperationMetadataOut": "_apigateway_37_ApigatewayOperationMetadataOut",
        "ApigatewayApiConfigFileIn": "_apigateway_38_ApigatewayApiConfigFileIn",
        "ApigatewayApiConfigFileOut": "_apigateway_39_ApigatewayApiConfigFileOut",
        "ApigatewayPolicyIn": "_apigateway_40_ApigatewayPolicyIn",
        "ApigatewayPolicyOut": "_apigateway_41_ApigatewayPolicyOut",
        "ApigatewayLocationIn": "_apigateway_42_ApigatewayLocationIn",
        "ApigatewayLocationOut": "_apigateway_43_ApigatewayLocationOut",
        "ApigatewayOperationIn": "_apigateway_44_ApigatewayOperationIn",
        "ApigatewayOperationOut": "_apigateway_45_ApigatewayOperationOut",
        "ApigatewayApiConfigGrpcServiceDefinitionIn": "_apigateway_46_ApigatewayApiConfigGrpcServiceDefinitionIn",
        "ApigatewayApiConfigGrpcServiceDefinitionOut": "_apigateway_47_ApigatewayApiConfigGrpcServiceDefinitionOut",
        "ApigatewayApiIn": "_apigateway_48_ApigatewayApiIn",
        "ApigatewayApiOut": "_apigateway_49_ApigatewayApiOut",
        "ApigatewayOperationMetadataDiagnosticIn": "_apigateway_50_ApigatewayOperationMetadataDiagnosticIn",
        "ApigatewayOperationMetadataDiagnosticOut": "_apigateway_51_ApigatewayOperationMetadataDiagnosticOut",
        "ApigatewayListGatewaysResponseIn": "_apigateway_52_ApigatewayListGatewaysResponseIn",
        "ApigatewayListGatewaysResponseOut": "_apigateway_53_ApigatewayListGatewaysResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ApigatewayTestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["ApigatewayTestIamPermissionsRequestIn"])
    types["ApigatewayTestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayTestIamPermissionsRequestOut"])
    types["ApigatewayListApisResponseIn"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "apis": t.array(t.proxy(renames["ApigatewayApiIn"])).optional(),
        }
    ).named(renames["ApigatewayListApisResponseIn"])
    types["ApigatewayListApisResponseOut"] = t.struct(
        {
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "apis": t.array(t.proxy(renames["ApigatewayApiOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayListApisResponseOut"])
    types["ApigatewayListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["ApigatewayLocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ApigatewayListLocationsResponseIn"])
    types["ApigatewayListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["ApigatewayLocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayListLocationsResponseOut"])
    types["ApigatewayApiConfigIn"] = t.struct(
        {
            "managedServiceConfigs": t.array(
                t.proxy(renames["ApigatewayApiConfigFileIn"])
            ).optional(),
            "grpcServices": t.array(
                t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gatewayServiceAccount": t.string().optional(),
            "openapiDocuments": t.array(
                t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
            ).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ApigatewayApiConfigIn"])
    types["ApigatewayApiConfigOut"] = t.struct(
        {
            "serviceConfigId": t.string().optional(),
            "state": t.string().optional(),
            "managedServiceConfigs": t.array(
                t.proxy(renames["ApigatewayApiConfigFileOut"])
            ).optional(),
            "grpcServices": t.array(
                t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionOut"])
            ).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gatewayServiceAccount": t.string().optional(),
            "openapiDocuments": t.array(
                t.proxy(renames["ApigatewayApiConfigOpenApiDocumentOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
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
    types["ApigatewayCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ApigatewayCancelOperationRequestIn"])
    types["ApigatewayCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ApigatewayCancelOperationRequestOut"])
    types["ApigatewayListApiConfigsResponseIn"] = t.struct(
        {
            "apiConfigs": t.array(t.proxy(renames["ApigatewayApiConfigIn"])).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ApigatewayListApiConfigsResponseIn"])
    types["ApigatewayListApiConfigsResponseOut"] = t.struct(
        {
            "apiConfigs": t.array(
                t.proxy(renames["ApigatewayApiConfigOut"])
            ).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayListApiConfigsResponseOut"])
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
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "apiConfig": t.string(),
            "defaultHostname": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayGatewayOut"])
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
    types["ApigatewayTestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["ApigatewayTestIamPermissionsResponseIn"])
    types["ApigatewayTestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayTestIamPermissionsResponseOut"])
    types["ApigatewayExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ApigatewayExprIn"])
    types["ApigatewayExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayExprOut"])
    types["ApigatewayStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["ApigatewayStatusIn"])
    types["ApigatewayStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayStatusOut"])
    types["ApigatewayApiConfigOpenApiDocumentIn"] = t.struct(
        {"document": t.proxy(renames["ApigatewayApiConfigFileIn"]).optional()}
    ).named(renames["ApigatewayApiConfigOpenApiDocumentIn"])
    types["ApigatewayApiConfigOpenApiDocumentOut"] = t.struct(
        {
            "document": t.proxy(renames["ApigatewayApiConfigFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayApiConfigOpenApiDocumentOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ApigatewayOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ApigatewayOperationMetadataIn"])
    types["ApigatewayOperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "diagnostics": t.array(
                t.proxy(renames["ApigatewayOperationMetadataDiagnosticOut"])
            ).optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayOperationMetadataOut"])
    types["ApigatewayApiConfigFileIn"] = t.struct(
        {"path": t.string().optional(), "contents": t.string().optional()}
    ).named(renames["ApigatewayApiConfigFileIn"])
    types["ApigatewayApiConfigFileOut"] = t.struct(
        {
            "path": t.string().optional(),
            "contents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayApiConfigFileOut"])
    types["ApigatewayPolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["ApigatewayBindingIn"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["ApigatewayAuditConfigIn"])
            ).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["ApigatewayPolicyIn"])
    types["ApigatewayPolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["ApigatewayBindingOut"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["ApigatewayAuditConfigOut"])
            ).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayPolicyOut"])
    types["ApigatewayLocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ApigatewayLocationIn"])
    types["ApigatewayLocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayLocationOut"])
    types["ApigatewayOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ApigatewayStatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApigatewayOperationIn"])
    types["ApigatewayOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApigatewayOperationOut"])
    types["ApigatewayApiConfigGrpcServiceDefinitionIn"] = t.struct(
        {
            "source": t.array(t.proxy(renames["ApigatewayApiConfigFileIn"])).optional(),
            "fileDescriptorSet": t.proxy(
                renames["ApigatewayApiConfigFileIn"]
            ).optional(),
        }
    ).named(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
    types["ApigatewayApiConfigGrpcServiceDefinitionOut"] = t.struct(
        {
            "source": t.array(
                t.proxy(renames["ApigatewayApiConfigFileOut"])
            ).optional(),
            "fileDescriptorSet": t.proxy(
                renames["ApigatewayApiConfigFileOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayApiConfigGrpcServiceDefinitionOut"])
    types["ApigatewayApiIn"] = t.struct(
        {
            "managedService": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ApigatewayApiIn"])
    types["ApigatewayApiOut"] = t.struct(
        {
            "managedService": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayApiOut"])
    types["ApigatewayOperationMetadataDiagnosticIn"] = t.struct(
        {"message": t.string().optional(), "location": t.string().optional()}
    ).named(renames["ApigatewayOperationMetadataDiagnosticIn"])
    types["ApigatewayOperationMetadataDiagnosticOut"] = t.struct(
        {
            "message": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayOperationMetadataDiagnosticOut"])
    types["ApigatewayListGatewaysResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gateways": t.array(t.proxy(renames["ApigatewayGatewayIn"])).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
        }
    ).named(renames["ApigatewayListGatewaysResponseIn"])
    types["ApigatewayListGatewaysResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gateways": t.array(t.proxy(renames["ApigatewayGatewayOut"])).optional(),
            "unreachableLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApigatewayListGatewaysResponseOut"])

    functions = {}
    functions["projectsLocationsGet"] = apigateway.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = apigateway.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayListLocationsResponseOut"]),
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
    functions["projectsLocationsApisList"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisPatch"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGetIamPolicy"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisCreate"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGet"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisTestIamPermissions"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisSetIamPolicy"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDelete"] = apigateway.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsGetIamPolicy"] = apigateway.post(
        "v1/{parent}/configs",
        t.struct(
            {
                "apiConfigId": t.string(),
                "parent": t.string(),
                "managedServiceConfigs": t.array(
                    t.proxy(renames["ApigatewayApiConfigFileIn"])
                ).optional(),
                "grpcServices": t.array(
                    t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gatewayServiceAccount": t.string().optional(),
                "openapiDocuments": t.array(
                    t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsGet"] = apigateway.post(
        "v1/{parent}/configs",
        t.struct(
            {
                "apiConfigId": t.string(),
                "parent": t.string(),
                "managedServiceConfigs": t.array(
                    t.proxy(renames["ApigatewayApiConfigFileIn"])
                ).optional(),
                "grpcServices": t.array(
                    t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gatewayServiceAccount": t.string().optional(),
                "openapiDocuments": t.array(
                    t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsPatch"] = apigateway.post(
        "v1/{parent}/configs",
        t.struct(
            {
                "apiConfigId": t.string(),
                "parent": t.string(),
                "managedServiceConfigs": t.array(
                    t.proxy(renames["ApigatewayApiConfigFileIn"])
                ).optional(),
                "grpcServices": t.array(
                    t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gatewayServiceAccount": t.string().optional(),
                "openapiDocuments": t.array(
                    t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsTestIamPermissions"] = apigateway.post(
        "v1/{parent}/configs",
        t.struct(
            {
                "apiConfigId": t.string(),
                "parent": t.string(),
                "managedServiceConfigs": t.array(
                    t.proxy(renames["ApigatewayApiConfigFileIn"])
                ).optional(),
                "grpcServices": t.array(
                    t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gatewayServiceAccount": t.string().optional(),
                "openapiDocuments": t.array(
                    t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsList"] = apigateway.post(
        "v1/{parent}/configs",
        t.struct(
            {
                "apiConfigId": t.string(),
                "parent": t.string(),
                "managedServiceConfigs": t.array(
                    t.proxy(renames["ApigatewayApiConfigFileIn"])
                ).optional(),
                "grpcServices": t.array(
                    t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gatewayServiceAccount": t.string().optional(),
                "openapiDocuments": t.array(
                    t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsDelete"] = apigateway.post(
        "v1/{parent}/configs",
        t.struct(
            {
                "apiConfigId": t.string(),
                "parent": t.string(),
                "managedServiceConfigs": t.array(
                    t.proxy(renames["ApigatewayApiConfigFileIn"])
                ).optional(),
                "grpcServices": t.array(
                    t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gatewayServiceAccount": t.string().optional(),
                "openapiDocuments": t.array(
                    t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsSetIamPolicy"] = apigateway.post(
        "v1/{parent}/configs",
        t.struct(
            {
                "apiConfigId": t.string(),
                "parent": t.string(),
                "managedServiceConfigs": t.array(
                    t.proxy(renames["ApigatewayApiConfigFileIn"])
                ).optional(),
                "grpcServices": t.array(
                    t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gatewayServiceAccount": t.string().optional(),
                "openapiDocuments": t.array(
                    t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisConfigsCreate"] = apigateway.post(
        "v1/{parent}/configs",
        t.struct(
            {
                "apiConfigId": t.string(),
                "parent": t.string(),
                "managedServiceConfigs": t.array(
                    t.proxy(renames["ApigatewayApiConfigFileIn"])
                ).optional(),
                "grpcServices": t.array(
                    t.proxy(renames["ApigatewayApiConfigGrpcServiceDefinitionIn"])
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "gatewayServiceAccount": t.string().optional(),
                "openapiDocuments": t.array(
                    t.proxy(renames["ApigatewayApiConfigOpenApiDocumentIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApigatewayOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = apigateway.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = apigateway.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = apigateway.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = apigateway.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="apigateway",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
