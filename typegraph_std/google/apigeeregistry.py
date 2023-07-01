from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_apigeeregistry():
    apigeeregistry = HTTPRuntime("https://apigeeregistry.googleapis.com/")

    renames = {
        "ErrorResponse": "_apigeeregistry_1_ErrorResponse",
        "PolicyIn": "_apigeeregistry_2_PolicyIn",
        "PolicyOut": "_apigeeregistry_3_PolicyOut",
        "TagApiDeploymentRevisionRequestIn": "_apigeeregistry_4_TagApiDeploymentRevisionRequestIn",
        "TagApiDeploymentRevisionRequestOut": "_apigeeregistry_5_TagApiDeploymentRevisionRequestOut",
        "ListApiSpecRevisionsResponseIn": "_apigeeregistry_6_ListApiSpecRevisionsResponseIn",
        "ListApiSpecRevisionsResponseOut": "_apigeeregistry_7_ListApiSpecRevisionsResponseOut",
        "ListApiDeploymentsResponseIn": "_apigeeregistry_8_ListApiDeploymentsResponseIn",
        "ListApiDeploymentsResponseOut": "_apigeeregistry_9_ListApiDeploymentsResponseOut",
        "ListArtifactsResponseIn": "_apigeeregistry_10_ListArtifactsResponseIn",
        "ListArtifactsResponseOut": "_apigeeregistry_11_ListArtifactsResponseOut",
        "ArtifactIn": "_apigeeregistry_12_ArtifactIn",
        "ArtifactOut": "_apigeeregistry_13_ArtifactOut",
        "ApiDeploymentIn": "_apigeeregistry_14_ApiDeploymentIn",
        "ApiDeploymentOut": "_apigeeregistry_15_ApiDeploymentOut",
        "ListApiDeploymentRevisionsResponseIn": "_apigeeregistry_16_ListApiDeploymentRevisionsResponseIn",
        "ListApiDeploymentRevisionsResponseOut": "_apigeeregistry_17_ListApiDeploymentRevisionsResponseOut",
        "TagApiSpecRevisionRequestIn": "_apigeeregistry_18_TagApiSpecRevisionRequestIn",
        "TagApiSpecRevisionRequestOut": "_apigeeregistry_19_TagApiSpecRevisionRequestOut",
        "BindingIn": "_apigeeregistry_20_BindingIn",
        "BindingOut": "_apigeeregistry_21_BindingOut",
        "OperationMetadataIn": "_apigeeregistry_22_OperationMetadataIn",
        "OperationMetadataOut": "_apigeeregistry_23_OperationMetadataOut",
        "SetIamPolicyRequestIn": "_apigeeregistry_24_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_apigeeregistry_25_SetIamPolicyRequestOut",
        "OperationIn": "_apigeeregistry_26_OperationIn",
        "OperationOut": "_apigeeregistry_27_OperationOut",
        "ListLocationsResponseIn": "_apigeeregistry_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_apigeeregistry_29_ListLocationsResponseOut",
        "StatusIn": "_apigeeregistry_30_StatusIn",
        "StatusOut": "_apigeeregistry_31_StatusOut",
        "ListApisResponseIn": "_apigeeregistry_32_ListApisResponseIn",
        "ListApisResponseOut": "_apigeeregistry_33_ListApisResponseOut",
        "ApiVersionIn": "_apigeeregistry_34_ApiVersionIn",
        "ApiVersionOut": "_apigeeregistry_35_ApiVersionOut",
        "ListApiVersionsResponseIn": "_apigeeregistry_36_ListApiVersionsResponseIn",
        "ListApiVersionsResponseOut": "_apigeeregistry_37_ListApiVersionsResponseOut",
        "EmptyIn": "_apigeeregistry_38_EmptyIn",
        "EmptyOut": "_apigeeregistry_39_EmptyOut",
        "ApiIn": "_apigeeregistry_40_ApiIn",
        "ApiOut": "_apigeeregistry_41_ApiOut",
        "BuildIn": "_apigeeregistry_42_BuildIn",
        "BuildOut": "_apigeeregistry_43_BuildOut",
        "HttpBodyIn": "_apigeeregistry_44_HttpBodyIn",
        "HttpBodyOut": "_apigeeregistry_45_HttpBodyOut",
        "ConfigIn": "_apigeeregistry_46_ConfigIn",
        "ConfigOut": "_apigeeregistry_47_ConfigOut",
        "RollbackApiSpecRequestIn": "_apigeeregistry_48_RollbackApiSpecRequestIn",
        "RollbackApiSpecRequestOut": "_apigeeregistry_49_RollbackApiSpecRequestOut",
        "RollbackApiDeploymentRequestIn": "_apigeeregistry_50_RollbackApiDeploymentRequestIn",
        "RollbackApiDeploymentRequestOut": "_apigeeregistry_51_RollbackApiDeploymentRequestOut",
        "LocationIn": "_apigeeregistry_52_LocationIn",
        "LocationOut": "_apigeeregistry_53_LocationOut",
        "ListApiSpecsResponseIn": "_apigeeregistry_54_ListApiSpecsResponseIn",
        "ListApiSpecsResponseOut": "_apigeeregistry_55_ListApiSpecsResponseOut",
        "CancelOperationRequestIn": "_apigeeregistry_56_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_apigeeregistry_57_CancelOperationRequestOut",
        "TestIamPermissionsRequestIn": "_apigeeregistry_58_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_apigeeregistry_59_TestIamPermissionsRequestOut",
        "ExprIn": "_apigeeregistry_60_ExprIn",
        "ExprOut": "_apigeeregistry_61_ExprOut",
        "ApiSpecIn": "_apigeeregistry_62_ApiSpecIn",
        "ApiSpecOut": "_apigeeregistry_63_ApiSpecOut",
        "TestIamPermissionsResponseIn": "_apigeeregistry_64_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_apigeeregistry_65_TestIamPermissionsResponseOut",
        "InstanceIn": "_apigeeregistry_66_InstanceIn",
        "InstanceOut": "_apigeeregistry_67_InstanceOut",
        "ListOperationsResponseIn": "_apigeeregistry_68_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_apigeeregistry_69_ListOperationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["TagApiDeploymentRevisionRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["TagApiDeploymentRevisionRequestIn"]
    )
    types["TagApiDeploymentRevisionRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TagApiDeploymentRevisionRequestOut"])
    types["ListApiSpecRevisionsResponseIn"] = t.struct(
        {
            "apiSpecs": t.array(t.proxy(renames["ApiSpecIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListApiSpecRevisionsResponseIn"])
    types["ListApiSpecRevisionsResponseOut"] = t.struct(
        {
            "apiSpecs": t.array(t.proxy(renames["ApiSpecOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiSpecRevisionsResponseOut"])
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
    types["ListArtifactsResponseIn"] = t.struct(
        {
            "artifacts": t.array(t.proxy(renames["ArtifactIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListArtifactsResponseIn"])
    types["ListArtifactsResponseOut"] = t.struct(
        {
            "artifacts": t.array(t.proxy(renames["ArtifactOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListArtifactsResponseOut"])
    types["ArtifactIn"] = t.struct(
        {
            "contents": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["ArtifactIn"])
    types["ArtifactOut"] = t.struct(
        {
            "sizeBytes": t.integer().optional(),
            "contents": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "hash": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactOut"])
    types["ApiDeploymentIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "apiSpecRevision": t.string().optional(),
            "intendedAudience": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "accessGuidance": t.string().optional(),
            "displayName": t.string().optional(),
            "endpointUri": t.string().optional(),
            "description": t.string().optional(),
            "externalChannelUri": t.string().optional(),
        }
    ).named(renames["ApiDeploymentIn"])
    types["ApiDeploymentOut"] = t.struct(
        {
            "revisionCreateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "revisionId": t.string().optional(),
            "apiSpecRevision": t.string().optional(),
            "createTime": t.string().optional(),
            "intendedAudience": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "accessGuidance": t.string().optional(),
            "displayName": t.string().optional(),
            "endpointUri": t.string().optional(),
            "description": t.string().optional(),
            "revisionUpdateTime": t.string().optional(),
            "externalChannelUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiDeploymentOut"])
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
    types["TagApiSpecRevisionRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["TagApiSpecRevisionRequestIn"]
    )
    types["TagApiSpecRevisionRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TagApiSpecRevisionRequestOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["PolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ListApisResponseIn"] = t.struct(
        {
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListApisResponseIn"])
    types["ListApisResponseOut"] = t.struct(
        {
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApisResponseOut"])
    types["ApiVersionIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "primarySpec": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ApiVersionIn"])
    types["ApiVersionOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "primarySpec": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiVersionOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ApiIn"] = t.struct(
        {
            "recommendedVersion": t.string().optional(),
            "description": t.string().optional(),
            "availability": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "recommendedDeployment": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "recommendedVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "availability": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "recommendedDeployment": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["BuildIn"] = t.struct({"_": t.string().optional()}).named(renames["BuildIn"])
    types["BuildOut"] = t.struct(
        {
            "commitId": t.string().optional(),
            "repo": t.string().optional(),
            "commitTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "contentType": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["ConfigIn"] = t.struct({"cmekKeyName": t.string()}).named(renames["ConfigIn"])
    types["ConfigOut"] = t.struct(
        {
            "cmekKeyName": t.string(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigOut"])
    types["RollbackApiSpecRequestIn"] = t.struct({"revisionId": t.string()}).named(
        renames["RollbackApiSpecRequestIn"]
    )
    types["RollbackApiSpecRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackApiSpecRequestOut"])
    types["RollbackApiDeploymentRequestIn"] = t.struct(
        {"revisionId": t.string()}
    ).named(renames["RollbackApiDeploymentRequestIn"])
    types["RollbackApiDeploymentRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackApiDeploymentRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["ApiSpecIn"] = t.struct(
        {
            "contents": t.string().optional(),
            "description": t.string().optional(),
            "sourceUri": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "filename": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ApiSpecIn"])
    types["ApiSpecOut"] = t.struct(
        {
            "revisionCreateTime": t.string().optional(),
            "contents": t.string().optional(),
            "description": t.string().optional(),
            "sourceUri": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sizeBytes": t.integer().optional(),
            "revisionId": t.string().optional(),
            "createTime": t.string().optional(),
            "mimeType": t.string().optional(),
            "hash": t.string().optional(),
            "filename": t.string().optional(),
            "name": t.string().optional(),
            "revisionUpdateTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiSpecOut"])
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
        {"config": t.proxy(renames["ConfigIn"]), "name": t.string().optional()}
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "config": t.proxy(renames["ConfigOut"]),
            "stateMessage": t.string().optional(),
            "state": t.string().optional(),
            "build": t.proxy(renames["BuildOut"]).optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = apigeeregistry.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = apigeeregistry.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsDelete"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsSetIamPolicy"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGetIamPolicy"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsReplaceArtifact"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGetContents"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsList"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsTestIamPermissions"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsCreate"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGet"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesCreate"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesDelete"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesGetIamPolicy"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesSetIamPolicy"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesTestIamPermissions"] = apigeeregistry.post(
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
    functions["projectsLocationsOperationsGet"] = apigeeregistry.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimeTestIamPermissions"] = apigeeregistry.get(
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
    functions["projectsLocationsRuntimeSetIamPolicy"] = apigeeregistry.get(
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
    functions["projectsLocationsRuntimeGetIamPolicy"] = apigeeregistry.get(
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
    functions["projectsLocationsApisGet"] = apigeeregistry.post(
        "v1/{parent}/apis",
        t.struct(
            {
                "parent": t.string(),
                "apiId": t.string(),
                "recommendedVersion": t.string().optional(),
                "description": t.string().optional(),
                "availability": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "recommendedDeployment": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDelete"] = apigeeregistry.post(
        "v1/{parent}/apis",
        t.struct(
            {
                "parent": t.string(),
                "apiId": t.string(),
                "recommendedVersion": t.string().optional(),
                "description": t.string().optional(),
                "availability": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "recommendedDeployment": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGetIamPolicy"] = apigeeregistry.post(
        "v1/{parent}/apis",
        t.struct(
            {
                "parent": t.string(),
                "apiId": t.string(),
                "recommendedVersion": t.string().optional(),
                "description": t.string().optional(),
                "availability": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "recommendedDeployment": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisPatch"] = apigeeregistry.post(
        "v1/{parent}/apis",
        t.struct(
            {
                "parent": t.string(),
                "apiId": t.string(),
                "recommendedVersion": t.string().optional(),
                "description": t.string().optional(),
                "availability": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "recommendedDeployment": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisSetIamPolicy"] = apigeeregistry.post(
        "v1/{parent}/apis",
        t.struct(
            {
                "parent": t.string(),
                "apiId": t.string(),
                "recommendedVersion": t.string().optional(),
                "description": t.string().optional(),
                "availability": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "recommendedDeployment": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisList"] = apigeeregistry.post(
        "v1/{parent}/apis",
        t.struct(
            {
                "parent": t.string(),
                "apiId": t.string(),
                "recommendedVersion": t.string().optional(),
                "description": t.string().optional(),
                "availability": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "recommendedDeployment": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisTestIamPermissions"] = apigeeregistry.post(
        "v1/{parent}/apis",
        t.struct(
            {
                "parent": t.string(),
                "apiId": t.string(),
                "recommendedVersion": t.string().optional(),
                "description": t.string().optional(),
                "availability": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "recommendedDeployment": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisCreate"] = apigeeregistry.post(
        "v1/{parent}/apis",
        t.struct(
            {
                "parent": t.string(),
                "apiId": t.string(),
                "recommendedVersion": t.string().optional(),
                "description": t.string().optional(),
                "availability": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "recommendedDeployment": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsDeleteRevision"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsSetIamPolicy"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsList"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsDelete"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsCreate"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsListRevisions"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsRollback"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsGet"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsGetIamPolicy"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsTestIamPermissions"
    ] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsPatch"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsTagRevision"] = apigeeregistry.post(
        "v1/{name}:tagRevision",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsArtifactsGetContents"
    ] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsArtifactsReplaceArtifact"
    ] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsGet"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsCreate"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsDelete"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsList"] = apigeeregistry.get(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListArtifactsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsGetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsGet"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsTestIamPermissions"
    ] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsList"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsCreate"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsPatch"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsDelete"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsCreate"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsGet"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsTestIamPermissions"
    ] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsGetIamPolicy"
    ] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsList"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsSetIamPolicy"
    ] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsDelete"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsReplaceArtifact"
    ] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsGetContents"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsRollback"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsDeleteRevision"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsSetIamPolicy"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsTagRevision"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsList"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGet"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGetIamPolicy"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsCreate"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsListRevisions"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsTestIamPermissions"
    ] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsPatch"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsDelete"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGetContents"] = apigeeregistry.get(
        "v1/{name}:getContents",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["HttpBodyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsList"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsCreate"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsGetContents"
    ] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsTestIamPermissions"
    ] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsGet"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsGetIamPolicy"
    ] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsDelete"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsSetIamPolicy"
    ] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsReplaceArtifact"
    ] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsGetIamPolicy"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "artifactId": t.string(),
                "parent": t.string(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsGetContents"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "artifactId": t.string(),
                "parent": t.string(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsList"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "artifactId": t.string(),
                "parent": t.string(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsDelete"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "artifactId": t.string(),
                "parent": t.string(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsSetIamPolicy"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "artifactId": t.string(),
                "parent": t.string(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsReplaceArtifact"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "artifactId": t.string(),
                "parent": t.string(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsGet"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "artifactId": t.string(),
                "parent": t.string(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsTestIamPermissions"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "artifactId": t.string(),
                "parent": t.string(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisArtifactsCreate"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "artifactId": t.string(),
                "parent": t.string(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mimeType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="apigeeregistry",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
