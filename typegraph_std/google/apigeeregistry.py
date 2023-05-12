from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_apigeeregistry() -> Import:
    apigeeregistry = HTTPRuntime("https://apigeeregistry.googleapis.com/")

    renames = {
        "ErrorResponse": "_apigeeregistry_1_ErrorResponse",
        "ListApiSpecRevisionsResponseIn": "_apigeeregistry_2_ListApiSpecRevisionsResponseIn",
        "ListApiSpecRevisionsResponseOut": "_apigeeregistry_3_ListApiSpecRevisionsResponseOut",
        "ListLocationsResponseIn": "_apigeeregistry_4_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_apigeeregistry_5_ListLocationsResponseOut",
        "ApiIn": "_apigeeregistry_6_ApiIn",
        "ApiOut": "_apigeeregistry_7_ApiOut",
        "RollbackApiSpecRequestIn": "_apigeeregistry_8_RollbackApiSpecRequestIn",
        "RollbackApiSpecRequestOut": "_apigeeregistry_9_RollbackApiSpecRequestOut",
        "BuildIn": "_apigeeregistry_10_BuildIn",
        "BuildOut": "_apigeeregistry_11_BuildOut",
        "ListApisResponseIn": "_apigeeregistry_12_ListApisResponseIn",
        "ListApisResponseOut": "_apigeeregistry_13_ListApisResponseOut",
        "EmptyIn": "_apigeeregistry_14_EmptyIn",
        "EmptyOut": "_apigeeregistry_15_EmptyOut",
        "ArtifactIn": "_apigeeregistry_16_ArtifactIn",
        "ArtifactOut": "_apigeeregistry_17_ArtifactOut",
        "LocationIn": "_apigeeregistry_18_LocationIn",
        "LocationOut": "_apigeeregistry_19_LocationOut",
        "ListOperationsResponseIn": "_apigeeregistry_20_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_apigeeregistry_21_ListOperationsResponseOut",
        "ApiVersionIn": "_apigeeregistry_22_ApiVersionIn",
        "ApiVersionOut": "_apigeeregistry_23_ApiVersionOut",
        "TestIamPermissionsResponseIn": "_apigeeregistry_24_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_apigeeregistry_25_TestIamPermissionsResponseOut",
        "InstanceIn": "_apigeeregistry_26_InstanceIn",
        "InstanceOut": "_apigeeregistry_27_InstanceOut",
        "OperationIn": "_apigeeregistry_28_OperationIn",
        "OperationOut": "_apigeeregistry_29_OperationOut",
        "ListApiDeploymentRevisionsResponseIn": "_apigeeregistry_30_ListApiDeploymentRevisionsResponseIn",
        "ListApiDeploymentRevisionsResponseOut": "_apigeeregistry_31_ListApiDeploymentRevisionsResponseOut",
        "ListArtifactsResponseIn": "_apigeeregistry_32_ListArtifactsResponseIn",
        "ListArtifactsResponseOut": "_apigeeregistry_33_ListArtifactsResponseOut",
        "OperationMetadataIn": "_apigeeregistry_34_OperationMetadataIn",
        "OperationMetadataOut": "_apigeeregistry_35_OperationMetadataOut",
        "ListApiDeploymentsResponseIn": "_apigeeregistry_36_ListApiDeploymentsResponseIn",
        "ListApiDeploymentsResponseOut": "_apigeeregistry_37_ListApiDeploymentsResponseOut",
        "TestIamPermissionsRequestIn": "_apigeeregistry_38_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_apigeeregistry_39_TestIamPermissionsRequestOut",
        "ApiDeploymentIn": "_apigeeregistry_40_ApiDeploymentIn",
        "ApiDeploymentOut": "_apigeeregistry_41_ApiDeploymentOut",
        "ConfigIn": "_apigeeregistry_42_ConfigIn",
        "ConfigOut": "_apigeeregistry_43_ConfigOut",
        "TagApiSpecRevisionRequestIn": "_apigeeregistry_44_TagApiSpecRevisionRequestIn",
        "TagApiSpecRevisionRequestOut": "_apigeeregistry_45_TagApiSpecRevisionRequestOut",
        "TagApiDeploymentRevisionRequestIn": "_apigeeregistry_46_TagApiDeploymentRevisionRequestIn",
        "TagApiDeploymentRevisionRequestOut": "_apigeeregistry_47_TagApiDeploymentRevisionRequestOut",
        "ListApiSpecsResponseIn": "_apigeeregistry_48_ListApiSpecsResponseIn",
        "ListApiSpecsResponseOut": "_apigeeregistry_49_ListApiSpecsResponseOut",
        "PolicyIn": "_apigeeregistry_50_PolicyIn",
        "PolicyOut": "_apigeeregistry_51_PolicyOut",
        "ApiSpecIn": "_apigeeregistry_52_ApiSpecIn",
        "ApiSpecOut": "_apigeeregistry_53_ApiSpecOut",
        "StatusIn": "_apigeeregistry_54_StatusIn",
        "StatusOut": "_apigeeregistry_55_StatusOut",
        "ListApiVersionsResponseIn": "_apigeeregistry_56_ListApiVersionsResponseIn",
        "ListApiVersionsResponseOut": "_apigeeregistry_57_ListApiVersionsResponseOut",
        "BindingIn": "_apigeeregistry_58_BindingIn",
        "BindingOut": "_apigeeregistry_59_BindingOut",
        "RollbackApiDeploymentRequestIn": "_apigeeregistry_60_RollbackApiDeploymentRequestIn",
        "RollbackApiDeploymentRequestOut": "_apigeeregistry_61_RollbackApiDeploymentRequestOut",
        "ExprIn": "_apigeeregistry_62_ExprIn",
        "ExprOut": "_apigeeregistry_63_ExprOut",
        "HttpBodyIn": "_apigeeregistry_64_HttpBodyIn",
        "HttpBodyOut": "_apigeeregistry_65_HttpBodyOut",
        "CancelOperationRequestIn": "_apigeeregistry_66_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_apigeeregistry_67_CancelOperationRequestOut",
        "SetIamPolicyRequestIn": "_apigeeregistry_68_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_apigeeregistry_69_SetIamPolicyRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["ApiIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "recommendedDeployment": t.string().optional(),
            "name": t.string().optional(),
            "recommendedVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "availability": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "recommendedDeployment": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "recommendedVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "availability": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["RollbackApiSpecRequestIn"] = t.struct({"revisionId": t.string()}).named(
        renames["RollbackApiSpecRequestIn"]
    )
    types["RollbackApiSpecRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackApiSpecRequestOut"])
    types["BuildIn"] = t.struct({"_": t.string().optional()}).named(renames["BuildIn"])
    types["BuildOut"] = t.struct(
        {
            "commitTime": t.string().optional(),
            "repo": t.string().optional(),
            "commitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ArtifactIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "contents": t.string().optional(),
        }
    ).named(renames["ArtifactIn"])
    types["ArtifactOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "hash": t.string().optional(),
            "createTime": t.string().optional(),
            "contents": t.string().optional(),
            "sizeBytes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["ApiVersionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "primarySpec": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ApiVersionIn"])
    types["ApiVersionOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "primarySpec": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiVersionOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["InstanceIn"] = t.struct(
        {"name": t.string().optional(), "config": t.proxy(renames["ConfigIn"])}
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "build": t.proxy(renames["BuildOut"]).optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "config": t.proxy(renames["ConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["ListApiDeploymentRevisionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiDeployments": t.array(t.proxy(renames["ApiDeploymentIn"])).optional(),
        }
    ).named(renames["ListApiDeploymentRevisionsResponseIn"])
    types["ListApiDeploymentRevisionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiDeployments": t.array(t.proxy(renames["ApiDeploymentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiDeploymentRevisionsResponseOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ListApiDeploymentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiDeployments": t.array(t.proxy(renames["ApiDeploymentIn"])).optional(),
        }
    ).named(renames["ListApiDeploymentsResponseIn"])
    types["ListApiDeploymentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apiDeployments": t.array(t.proxy(renames["ApiDeploymentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiDeploymentsResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ApiDeploymentIn"] = t.struct(
        {
            "apiSpecRevision": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "endpointUri": t.string().optional(),
            "displayName": t.string().optional(),
            "accessGuidance": t.string().optional(),
            "intendedAudience": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "externalChannelUri": t.string().optional(),
        }
    ).named(renames["ApiDeploymentIn"])
    types["ApiDeploymentOut"] = t.struct(
        {
            "revisionCreateTime": t.string().optional(),
            "apiSpecRevision": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "endpointUri": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "accessGuidance": t.string().optional(),
            "intendedAudience": t.string().optional(),
            "name": t.string().optional(),
            "revisionUpdateTime": t.string().optional(),
            "description": t.string().optional(),
            "revisionId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "externalChannelUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiDeploymentOut"])
    types["ConfigIn"] = t.struct({"cmekKeyName": t.string()}).named(renames["ConfigIn"])
    types["ConfigOut"] = t.struct(
        {
            "cmekKeyName": t.string(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigOut"])
    types["TagApiSpecRevisionRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["TagApiSpecRevisionRequestIn"]
    )
    types["TagApiSpecRevisionRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TagApiSpecRevisionRequestOut"])
    types["TagApiDeploymentRevisionRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["TagApiDeploymentRevisionRequestIn"]
    )
    types["TagApiDeploymentRevisionRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TagApiDeploymentRevisionRequestOut"])
    types["ListApiSpecsResponseIn"] = t.struct(
        {
            "apiSpecs": t.array(t.proxy(renames["ApiSpecIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListApiSpecsResponseIn"])
    types["ListApiSpecsResponseOut"] = t.struct(
        {
            "apiSpecs": t.array(t.proxy(renames["ApiSpecOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiSpecsResponseOut"])
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
    types["ApiSpecIn"] = t.struct(
        {
            "contents": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "mimeType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "filename": t.string().optional(),
            "name": t.string().optional(),
            "sourceUri": t.string().optional(),
        }
    ).named(renames["ApiSpecIn"])
    types["ApiSpecOut"] = t.struct(
        {
            "contents": t.string().optional(),
            "createTime": t.string().optional(),
            "hash": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "sizeBytes": t.integer().optional(),
            "revisionId": t.string().optional(),
            "mimeType": t.string().optional(),
            "revisionUpdateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "revisionCreateTime": t.string().optional(),
            "filename": t.string().optional(),
            "name": t.string().optional(),
            "sourceUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiSpecOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "data": t.string().optional(),
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "data": t.string().optional(),
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])

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
    functions["projectsLocationsInstancesGetIamPolicy"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesGet"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesTestIamPermissions"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesDelete"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesCreate"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesSetIamPolicy"] = apigeeregistry.post(
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
    functions["projectsLocationsArtifactsCreate"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsTestIamPermissions"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsSetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsList"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGet"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGetContents"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsReplaceArtifact"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsDelete"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGetIamPolicy"] = apigeeregistry.post(
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
    functions["projectsLocationsApisCreate"] = apigeeregistry.post(
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
    functions["projectsLocationsApisGet"] = apigeeregistry.post(
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
    functions["projectsLocationsApisList"] = apigeeregistry.post(
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
    functions["projectsLocationsApisDelete"] = apigeeregistry.post(
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
    functions["projectsLocationsApisPatch"] = apigeeregistry.post(
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
    functions["projectsLocationsApisSetIamPolicy"] = apigeeregistry.post(
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
    functions["projectsLocationsApisTestIamPermissions"] = apigeeregistry.post(
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
    functions["projectsLocationsApisArtifactsSetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsReplaceArtifact"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsList"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisArtifactsTestIamPermissions"
    ] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsGetContents"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsGet"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsGetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsCreate"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsDelete"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsListRevisions"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsTagRevision"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsDeleteRevision"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsDelete"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsSetIamPolicy"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsTestIamPermissions"
    ] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsGetIamPolicy"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsPatch"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsList"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsRollback"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsGet"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsCreate"] = apigeeregistry.post(
        "v1/{parent}/deployments",
        t.struct(
            {
                "apiDeploymentId": t.string(),
                "parent": t.string(),
                "apiSpecRevision": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "endpointUri": t.string().optional(),
                "displayName": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "intendedAudience": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "externalChannelUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsList"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsDelete"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsArtifactsReplaceArtifact"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsArtifactsGetContents"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsCreate"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsGet"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSetIamPolicy"] = apigeeregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsGet"] = apigeeregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsPatch"] = apigeeregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsTestIamPermissions"] = apigeeregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsCreate"] = apigeeregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsDelete"] = apigeeregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsGetIamPolicy"] = apigeeregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsList"] = apigeeregistry.get(
        "v1/{parent}/versions",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiVersionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGetIamPolicy"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsListRevisions"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsDeleteRevision"
    ] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsCreate"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsRollback"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsTagRevision"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGetContents"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsDelete"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsSetIamPolicy"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGet"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsList"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsTestIamPermissions"
    ] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsPatch"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "allowMissing": t.boolean().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "filename": t.string().optional(),
                "sourceUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiSpecOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsGetIamPolicy"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsDelete"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsCreate"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsSetIamPolicy"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsTestIamPermissions"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsGetContents"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsReplaceArtifact"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsList"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsGet"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsCreate"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsReplaceArtifact"
    ] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsGet"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsList"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsDelete"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsSetIamPolicy"
    ] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsGetContents"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsTestIamPermissions"
    ] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsGetIamPolicy"
    ] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimeSetIamPolicy"] = apigeeregistry.post(
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
    functions["projectsLocationsRuntimeGetIamPolicy"] = apigeeregistry.post(
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
    functions["projectsLocationsRuntimeTestIamPermissions"] = apigeeregistry.post(
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

    return Import(
        importer="apigeeregistry",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
