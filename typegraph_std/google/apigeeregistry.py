from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_apigeeregistry() -> Import:
    apigeeregistry = HTTPRuntime("https://apigeeregistry.googleapis.com/")

    renames = {
        "ErrorResponse": "_apigeeregistry_1_ErrorResponse",
        "CancelOperationRequestIn": "_apigeeregistry_2_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_apigeeregistry_3_CancelOperationRequestOut",
        "PolicyIn": "_apigeeregistry_4_PolicyIn",
        "PolicyOut": "_apigeeregistry_5_PolicyOut",
        "ArtifactIn": "_apigeeregistry_6_ArtifactIn",
        "ArtifactOut": "_apigeeregistry_7_ArtifactOut",
        "TagApiSpecRevisionRequestIn": "_apigeeregistry_8_TagApiSpecRevisionRequestIn",
        "TagApiSpecRevisionRequestOut": "_apigeeregistry_9_TagApiSpecRevisionRequestOut",
        "ListApiSpecRevisionsResponseIn": "_apigeeregistry_10_ListApiSpecRevisionsResponseIn",
        "ListApiSpecRevisionsResponseOut": "_apigeeregistry_11_ListApiSpecRevisionsResponseOut",
        "ListApisResponseIn": "_apigeeregistry_12_ListApisResponseIn",
        "ListApisResponseOut": "_apigeeregistry_13_ListApisResponseOut",
        "ApiIn": "_apigeeregistry_14_ApiIn",
        "ApiOut": "_apigeeregistry_15_ApiOut",
        "ListOperationsResponseIn": "_apigeeregistry_16_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_apigeeregistry_17_ListOperationsResponseOut",
        "LocationIn": "_apigeeregistry_18_LocationIn",
        "LocationOut": "_apigeeregistry_19_LocationOut",
        "ListArtifactsResponseIn": "_apigeeregistry_20_ListArtifactsResponseIn",
        "ListArtifactsResponseOut": "_apigeeregistry_21_ListArtifactsResponseOut",
        "EmptyIn": "_apigeeregistry_22_EmptyIn",
        "EmptyOut": "_apigeeregistry_23_EmptyOut",
        "ConfigIn": "_apigeeregistry_24_ConfigIn",
        "ConfigOut": "_apigeeregistry_25_ConfigOut",
        "SetIamPolicyRequestIn": "_apigeeregistry_26_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_apigeeregistry_27_SetIamPolicyRequestOut",
        "HttpBodyIn": "_apigeeregistry_28_HttpBodyIn",
        "HttpBodyOut": "_apigeeregistry_29_HttpBodyOut",
        "ApiSpecIn": "_apigeeregistry_30_ApiSpecIn",
        "ApiSpecOut": "_apigeeregistry_31_ApiSpecOut",
        "BindingIn": "_apigeeregistry_32_BindingIn",
        "BindingOut": "_apigeeregistry_33_BindingOut",
        "RollbackApiSpecRequestIn": "_apigeeregistry_34_RollbackApiSpecRequestIn",
        "RollbackApiSpecRequestOut": "_apigeeregistry_35_RollbackApiSpecRequestOut",
        "ListApiSpecsResponseIn": "_apigeeregistry_36_ListApiSpecsResponseIn",
        "ListApiSpecsResponseOut": "_apigeeregistry_37_ListApiSpecsResponseOut",
        "RollbackApiDeploymentRequestIn": "_apigeeregistry_38_RollbackApiDeploymentRequestIn",
        "RollbackApiDeploymentRequestOut": "_apigeeregistry_39_RollbackApiDeploymentRequestOut",
        "ExprIn": "_apigeeregistry_40_ExprIn",
        "ExprOut": "_apigeeregistry_41_ExprOut",
        "TestIamPermissionsRequestIn": "_apigeeregistry_42_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_apigeeregistry_43_TestIamPermissionsRequestOut",
        "OperationMetadataIn": "_apigeeregistry_44_OperationMetadataIn",
        "OperationMetadataOut": "_apigeeregistry_45_OperationMetadataOut",
        "ListApiDeploymentsResponseIn": "_apigeeregistry_46_ListApiDeploymentsResponseIn",
        "ListApiDeploymentsResponseOut": "_apigeeregistry_47_ListApiDeploymentsResponseOut",
        "BuildIn": "_apigeeregistry_48_BuildIn",
        "BuildOut": "_apigeeregistry_49_BuildOut",
        "InstanceIn": "_apigeeregistry_50_InstanceIn",
        "InstanceOut": "_apigeeregistry_51_InstanceOut",
        "ListApiVersionsResponseIn": "_apigeeregistry_52_ListApiVersionsResponseIn",
        "ListApiVersionsResponseOut": "_apigeeregistry_53_ListApiVersionsResponseOut",
        "OperationIn": "_apigeeregistry_54_OperationIn",
        "OperationOut": "_apigeeregistry_55_OperationOut",
        "ApiDeploymentIn": "_apigeeregistry_56_ApiDeploymentIn",
        "ApiDeploymentOut": "_apigeeregistry_57_ApiDeploymentOut",
        "ListApiDeploymentRevisionsResponseIn": "_apigeeregistry_58_ListApiDeploymentRevisionsResponseIn",
        "ListApiDeploymentRevisionsResponseOut": "_apigeeregistry_59_ListApiDeploymentRevisionsResponseOut",
        "TagApiDeploymentRevisionRequestIn": "_apigeeregistry_60_TagApiDeploymentRevisionRequestIn",
        "TagApiDeploymentRevisionRequestOut": "_apigeeregistry_61_TagApiDeploymentRevisionRequestOut",
        "ApiVersionIn": "_apigeeregistry_62_ApiVersionIn",
        "ApiVersionOut": "_apigeeregistry_63_ApiVersionOut",
        "StatusIn": "_apigeeregistry_64_StatusIn",
        "StatusOut": "_apigeeregistry_65_StatusOut",
        "ListLocationsResponseIn": "_apigeeregistry_66_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_apigeeregistry_67_ListLocationsResponseOut",
        "TestIamPermissionsResponseIn": "_apigeeregistry_68_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_apigeeregistry_69_TestIamPermissionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ArtifactIn"] = t.struct(
        {
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "contents": t.string().optional(),
        }
    ).named(renames["ArtifactIn"])
    types["ArtifactOut"] = t.struct(
        {
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "sizeBytes": t.integer().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "hash": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "contents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactOut"])
    types["TagApiSpecRevisionRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["TagApiSpecRevisionRequestIn"]
    )
    types["TagApiSpecRevisionRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TagApiSpecRevisionRequestOut"])
    types["ListApiSpecRevisionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiSpecs": t.array(t.proxy(renames["ApiSpecIn"])).optional(),
        }
    ).named(renames["ListApiSpecRevisionsResponseIn"])
    types["ListApiSpecRevisionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiSpecs": t.array(t.proxy(renames["ApiSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiSpecRevisionsResponseOut"])
    types["ListApisResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
        }
    ).named(renames["ListApisResponseIn"])
    types["ListApisResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApisResponseOut"])
    types["ApiIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "availability": t.string().optional(),
            "recommendedVersion": t.string().optional(),
            "recommendedDeployment": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "availability": t.string().optional(),
            "recommendedVersion": t.string().optional(),
            "recommendedDeployment": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ListArtifactsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "artifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
        }
    ).named(renames["ListArtifactsResponseIn"])
    types["ListArtifactsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "artifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListArtifactsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ConfigIn"] = t.struct({"cmekKeyName": t.string()}).named(renames["ConfigIn"])
    types["ConfigOut"] = t.struct(
        {
            "cmekKeyName": t.string(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["ApiSpecIn"] = t.struct(
        {
            "filename": t.string().optional(),
            "description": t.string().optional(),
            "sourceUri": t.string().optional(),
            "contents": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApiSpecIn"])
    types["ApiSpecOut"] = t.struct(
        {
            "filename": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "hash": t.string().optional(),
            "revisionUpdateTime": t.string().optional(),
            "sourceUri": t.string().optional(),
            "contents": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "revisionId": t.string().optional(),
            "mimeType": t.string().optional(),
            "name": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "sizeBytes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiSpecOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["RollbackApiSpecRequestIn"] = t.struct({"revisionId": t.string()}).named(
        renames["RollbackApiSpecRequestIn"]
    )
    types["RollbackApiSpecRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackApiSpecRequestOut"])
    types["ListApiSpecsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiSpecs": t.array(t.proxy(renames["ApiSpecIn"])).optional(),
        }
    ).named(renames["ListApiSpecsResponseIn"])
    types["ListApiSpecsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiSpecs": t.array(t.proxy(renames["ApiSpecOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiSpecsResponseOut"])
    types["RollbackApiDeploymentRequestIn"] = t.struct(
        {"revisionId": t.string()}
    ).named(renames["RollbackApiDeploymentRequestIn"])
    types["RollbackApiDeploymentRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackApiDeploymentRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListApiDeploymentsResponseIn"] = t.struct(
        {
            "apiDeployments": t.array(t.proxy(renames["ApiDeploymentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListApiDeploymentsResponseIn"])
    types["ListApiDeploymentsResponseOut"] = t.struct(
        {
            "apiDeployments": t.array(t.proxy(renames["ApiDeploymentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiDeploymentsResponseOut"])
    types["BuildIn"] = t.struct({"_": t.string().optional()}).named(renames["BuildIn"])
    types["BuildOut"] = t.struct(
        {
            "repo": t.string().optional(),
            "commitId": t.string().optional(),
            "commitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOut"])
    types["InstanceIn"] = t.struct(
        {"config": t.proxy(renames["ConfigIn"]), "name": t.string().optional()}
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "build": t.proxy(renames["BuildOut"]).optional(),
            "config": t.proxy(renames["ConfigOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["ListApiVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiVersions": t.array(t.proxy(renames["ApiVersionIn"])).optional(),
        }
    ).named(renames["ListApiVersionsResponseIn"])
    types["ListApiVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiVersions": t.array(t.proxy(renames["ApiVersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiVersionsResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["ApiDeploymentIn"] = t.struct(
        {
            "description": t.string().optional(),
            "externalChannelUri": t.string().optional(),
            "name": t.string().optional(),
            "accessGuidance": t.string().optional(),
            "apiSpecRevision": t.string().optional(),
            "endpointUri": t.string().optional(),
            "displayName": t.string().optional(),
            "intendedAudience": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ApiDeploymentIn"])
    types["ApiDeploymentOut"] = t.struct(
        {
            "description": t.string().optional(),
            "externalChannelUri": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "accessGuidance": t.string().optional(),
            "apiSpecRevision": t.string().optional(),
            "revisionCreateTime": t.string().optional(),
            "revisionUpdateTime": t.string().optional(),
            "endpointUri": t.string().optional(),
            "displayName": t.string().optional(),
            "revisionId": t.string().optional(),
            "intendedAudience": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiDeploymentOut"])
    types["ListApiDeploymentRevisionsResponseIn"] = t.struct(
        {
            "apiDeployments": t.array(t.proxy(renames["ApiDeploymentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListApiDeploymentRevisionsResponseIn"])
    types["ListApiDeploymentRevisionsResponseOut"] = t.struct(
        {
            "apiDeployments": t.array(t.proxy(renames["ApiDeploymentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiDeploymentRevisionsResponseOut"])
    types["TagApiDeploymentRevisionRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["TagApiDeploymentRevisionRequestIn"]
    )
    types["TagApiDeploymentRevisionRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TagApiDeploymentRevisionRequestOut"])
    types["ApiVersionIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "primarySpec": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ApiVersionIn"])
    types["ApiVersionOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "primarySpec": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiVersionOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])

    functions = {}
    functions["projectsLocationsList"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = apigeeregistry.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = apigeeregistry.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = apigeeregistry.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = apigeeregistry.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesTestIamPermissions"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesSetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDelete"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisList"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGetIamPolicy"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisCreate"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDelete"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisPatch"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisTestIamPermissions"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGet"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisSetIamPolicy"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSetIamPolicy"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApiVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsCreate"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApiVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsList"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApiVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsDelete"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApiVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsPatch"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApiVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsTestIamPermissions"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApiVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsGetIamPolicy"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApiVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsGet"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ApiVersionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsGetContents"
    ] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsCreate"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsList"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsGet"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsReplaceArtifact"
    ] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsGetIamPolicy"
    ] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsTestIamPermissions"
    ] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsSetIamPolicy"
    ] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsDelete"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGetContents"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsDeleteRevision"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsRollback"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGetIamPolicy"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsList"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsTestIamPermissions"
    ] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGet"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsTagRevision"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsSetIamPolicy"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsPatch"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsListRevisions"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsDelete"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsCreate"] = apigeeregistry.post(
        "v1/{parent}/specs",
        t.struct(
            {
                "parent": t.string(),
                "apiSpecId": t.string(),
                "filename": t.string().optional(),
                "description": t.string().optional(),
                "sourceUri": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsDelete"
    ] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsGet"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsCreate"
    ] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsReplaceArtifact"
    ] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsList"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsSetIamPolicy"
    ] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsGetIamPolicy"
    ] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsGetContents"
    ] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsTestIamPermissions"
    ] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsTagRevision"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsPatch"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsListRevisions"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsTestIamPermissions"
    ] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsGet"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsSetIamPolicy"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsGetIamPolicy"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsDelete"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsCreate"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsDeleteRevision"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsRollback"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsList"] = apigeeregistry.get(
        "v1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsGet"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "contents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsList"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "contents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsArtifactsGetContents"
    ] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "contents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsDelete"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "contents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsCreate"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "contents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsArtifactsReplaceArtifact"
    ] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "contents": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsGet"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsDelete"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsGetContents"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsCreate"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsList"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsReplaceArtifact"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsSetIamPolicy"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsGetIamPolicy"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsTestIamPermissions"] = apigeeregistry.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsSetIamPolicy"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsCreate"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsReplaceArtifact"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsTestIamPermissions"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGetContents"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGet"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsDelete"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGetIamPolicy"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsList"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimeTestIamPermissions"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimeGetIamPolicy"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimeSetIamPolicy"] = apigeeregistry.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="apigeeregistry",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
