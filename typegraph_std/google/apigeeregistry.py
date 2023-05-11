from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_apigeeregistry() -> Import:
    apigeeregistry = HTTPRuntime("https://apigeeregistry.googleapis.com/")

    renames = {
        "ErrorResponse": "_apigeeregistry_1_ErrorResponse",
        "ListArtifactsResponseIn": "_apigeeregistry_2_ListArtifactsResponseIn",
        "ListArtifactsResponseOut": "_apigeeregistry_3_ListArtifactsResponseOut",
        "ListApiSpecsResponseIn": "_apigeeregistry_4_ListApiSpecsResponseIn",
        "ListApiSpecsResponseOut": "_apigeeregistry_5_ListApiSpecsResponseOut",
        "StatusIn": "_apigeeregistry_6_StatusIn",
        "StatusOut": "_apigeeregistry_7_StatusOut",
        "OperationMetadataIn": "_apigeeregistry_8_OperationMetadataIn",
        "OperationMetadataOut": "_apigeeregistry_9_OperationMetadataOut",
        "TestIamPermissionsRequestIn": "_apigeeregistry_10_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_apigeeregistry_11_TestIamPermissionsRequestOut",
        "BindingIn": "_apigeeregistry_12_BindingIn",
        "BindingOut": "_apigeeregistry_13_BindingOut",
        "EmptyIn": "_apigeeregistry_14_EmptyIn",
        "EmptyOut": "_apigeeregistry_15_EmptyOut",
        "OperationIn": "_apigeeregistry_16_OperationIn",
        "OperationOut": "_apigeeregistry_17_OperationOut",
        "ExprIn": "_apigeeregistry_18_ExprIn",
        "ExprOut": "_apigeeregistry_19_ExprOut",
        "PolicyIn": "_apigeeregistry_20_PolicyIn",
        "PolicyOut": "_apigeeregistry_21_PolicyOut",
        "RollbackApiSpecRequestIn": "_apigeeregistry_22_RollbackApiSpecRequestIn",
        "RollbackApiSpecRequestOut": "_apigeeregistry_23_RollbackApiSpecRequestOut",
        "ListApiDeploymentRevisionsResponseIn": "_apigeeregistry_24_ListApiDeploymentRevisionsResponseIn",
        "ListApiDeploymentRevisionsResponseOut": "_apigeeregistry_25_ListApiDeploymentRevisionsResponseOut",
        "ApiIn": "_apigeeregistry_26_ApiIn",
        "ApiOut": "_apigeeregistry_27_ApiOut",
        "ApiDeploymentIn": "_apigeeregistry_28_ApiDeploymentIn",
        "ApiDeploymentOut": "_apigeeregistry_29_ApiDeploymentOut",
        "ListApiVersionsResponseIn": "_apigeeregistry_30_ListApiVersionsResponseIn",
        "ListApiVersionsResponseOut": "_apigeeregistry_31_ListApiVersionsResponseOut",
        "ApiVersionIn": "_apigeeregistry_32_ApiVersionIn",
        "ApiVersionOut": "_apigeeregistry_33_ApiVersionOut",
        "ConfigIn": "_apigeeregistry_34_ConfigIn",
        "ConfigOut": "_apigeeregistry_35_ConfigOut",
        "LocationIn": "_apigeeregistry_36_LocationIn",
        "LocationOut": "_apigeeregistry_37_LocationOut",
        "InstanceIn": "_apigeeregistry_38_InstanceIn",
        "InstanceOut": "_apigeeregistry_39_InstanceOut",
        "TagApiSpecRevisionRequestIn": "_apigeeregistry_40_TagApiSpecRevisionRequestIn",
        "TagApiSpecRevisionRequestOut": "_apigeeregistry_41_TagApiSpecRevisionRequestOut",
        "ListApiDeploymentsResponseIn": "_apigeeregistry_42_ListApiDeploymentsResponseIn",
        "ListApiDeploymentsResponseOut": "_apigeeregistry_43_ListApiDeploymentsResponseOut",
        "BuildIn": "_apigeeregistry_44_BuildIn",
        "BuildOut": "_apigeeregistry_45_BuildOut",
        "ApiSpecIn": "_apigeeregistry_46_ApiSpecIn",
        "ApiSpecOut": "_apigeeregistry_47_ApiSpecOut",
        "ArtifactIn": "_apigeeregistry_48_ArtifactIn",
        "ArtifactOut": "_apigeeregistry_49_ArtifactOut",
        "ListApiSpecRevisionsResponseIn": "_apigeeregistry_50_ListApiSpecRevisionsResponseIn",
        "ListApiSpecRevisionsResponseOut": "_apigeeregistry_51_ListApiSpecRevisionsResponseOut",
        "RollbackApiDeploymentRequestIn": "_apigeeregistry_52_RollbackApiDeploymentRequestIn",
        "RollbackApiDeploymentRequestOut": "_apigeeregistry_53_RollbackApiDeploymentRequestOut",
        "CancelOperationRequestIn": "_apigeeregistry_54_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_apigeeregistry_55_CancelOperationRequestOut",
        "HttpBodyIn": "_apigeeregistry_56_HttpBodyIn",
        "HttpBodyOut": "_apigeeregistry_57_HttpBodyOut",
        "TestIamPermissionsResponseIn": "_apigeeregistry_58_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_apigeeregistry_59_TestIamPermissionsResponseOut",
        "ListLocationsResponseIn": "_apigeeregistry_60_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_apigeeregistry_61_ListLocationsResponseOut",
        "TagApiDeploymentRevisionRequestIn": "_apigeeregistry_62_TagApiDeploymentRevisionRequestIn",
        "TagApiDeploymentRevisionRequestOut": "_apigeeregistry_63_TagApiDeploymentRevisionRequestOut",
        "ListOperationsResponseIn": "_apigeeregistry_64_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_apigeeregistry_65_ListOperationsResponseOut",
        "ListApisResponseIn": "_apigeeregistry_66_ListApisResponseIn",
        "ListApisResponseOut": "_apigeeregistry_67_ListApisResponseOut",
        "SetIamPolicyRequestIn": "_apigeeregistry_68_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_apigeeregistry_69_SetIamPolicyRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "cancellationRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["RollbackApiSpecRequestIn"] = t.struct({"revisionId": t.string()}).named(
        renames["RollbackApiSpecRequestIn"]
    )
    types["RollbackApiSpecRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackApiSpecRequestOut"])
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
    types["ApiIn"] = t.struct(
        {
            "recommendedDeployment": t.string().optional(),
            "recommendedVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "availability": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "recommendedDeployment": t.string().optional(),
            "recommendedVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "availability": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["ApiDeploymentIn"] = t.struct(
        {
            "accessGuidance": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "intendedAudience": t.string().optional(),
            "externalChannelUri": t.string().optional(),
            "apiSpecRevision": t.string().optional(),
            "endpointUri": t.string().optional(),
        }
    ).named(renames["ApiDeploymentIn"])
    types["ApiDeploymentOut"] = t.struct(
        {
            "revisionId": t.string().optional(),
            "accessGuidance": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "revisionCreateTime": t.string().optional(),
            "revisionUpdateTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "intendedAudience": t.string().optional(),
            "externalChannelUri": t.string().optional(),
            "apiSpecRevision": t.string().optional(),
            "endpointUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiDeploymentOut"])
    types["ListApiVersionsResponseIn"] = t.struct(
        {
            "apiVersions": t.array(t.proxy(renames["ApiVersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListApiVersionsResponseIn"])
    types["ListApiVersionsResponseOut"] = t.struct(
        {
            "apiVersions": t.array(t.proxy(renames["ApiVersionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListApiVersionsResponseOut"])
    types["ApiVersionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "primarySpec": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ApiVersionIn"])
    types["ApiVersionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "primarySpec": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiVersionOut"])
    types["ConfigIn"] = t.struct({"cmekKeyName": t.string()}).named(renames["ConfigIn"])
    types["ConfigOut"] = t.struct(
        {
            "location": t.string().optional(),
            "cmekKeyName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["InstanceIn"] = t.struct(
        {"config": t.proxy(renames["ConfigIn"]), "name": t.string().optional()}
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "build": t.proxy(renames["BuildOut"]).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "config": t.proxy(renames["ConfigOut"]),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["TagApiSpecRevisionRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["TagApiSpecRevisionRequestIn"]
    )
    types["TagApiSpecRevisionRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TagApiSpecRevisionRequestOut"])
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
    types["BuildIn"] = t.struct({"_": t.string().optional()}).named(renames["BuildIn"])
    types["BuildOut"] = t.struct(
        {
            "commitTime": t.string().optional(),
            "commitId": t.string().optional(),
            "repo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildOut"])
    types["ApiSpecIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mimeType": t.string().optional(),
            "filename": t.string().optional(),
            "contents": t.string().optional(),
            "description": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "sourceUri": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApiSpecIn"])
    types["ApiSpecOut"] = t.struct(
        {
            "revisionCreateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hash": t.string().optional(),
            "revisionId": t.string().optional(),
            "mimeType": t.string().optional(),
            "filename": t.string().optional(),
            "contents": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "revisionUpdateTime": t.string().optional(),
            "sizeBytes": t.integer().optional(),
            "sourceUri": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiSpecOut"])
    types["ArtifactIn"] = t.struct(
        {
            "name": t.string().optional(),
            "mimeType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "contents": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ArtifactIn"])
    types["ArtifactOut"] = t.struct(
        {
            "name": t.string().optional(),
            "mimeType": t.string().optional(),
            "hash": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "contents": t.string().optional(),
            "sizeBytes": t.integer().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ArtifactOut"])
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
    types["RollbackApiDeploymentRequestIn"] = t.struct(
        {"revisionId": t.string()}
    ).named(renames["RollbackApiDeploymentRequestIn"])
    types["RollbackApiDeploymentRequestOut"] = t.struct(
        {
            "revisionId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RollbackApiDeploymentRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["HttpBodyIn"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
        }
    ).named(renames["HttpBodyIn"])
    types["HttpBodyOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpBodyOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["TagApiDeploymentRevisionRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["TagApiDeploymentRevisionRequestIn"]
    )
    types["TagApiDeploymentRevisionRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["TagApiDeploymentRevisionRequestOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
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
    functions["projectsLocationsGet"] = apigeeregistry.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsApisCreate"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisTestIamPermissions"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisPatch"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGet"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisList"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisGetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisSetIamPolicy"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDelete"] = apigeeregistry.delete(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "force": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsCreate"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsGet"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsDelete"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsTestIamPermissions"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsPatch"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSetIamPolicy"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsList"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsGetIamPolicy"] = apigeeregistry.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
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
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsTestIamPermissions"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsSetIamPolicy"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsList"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsArtifactsReplaceArtifact"
    ] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsDelete"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsGetContents"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsCreate"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsArtifactsGet"] = apigeeregistry.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsSetIamPolicy"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsPatch"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGetContents"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsRollback"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsList"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsDeleteRevision"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsCreate"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsTagRevision"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsTestIamPermissions"
    ] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsDelete"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGet"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsGetIamPolicy"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsListRevisions"] = apigeeregistry.get(
        "v1/{name}:listRevisions",
        t.struct(
            {
                "name": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListApiSpecRevisionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsReplaceArtifact"
    ] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "parent": t.string(),
                "artifactId": t.string(),
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsGetContents"
    ] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "parent": t.string(),
                "artifactId": t.string(),
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsSetIamPolicy"
    ] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "parent": t.string(),
                "artifactId": t.string(),
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsDelete"
    ] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "parent": t.string(),
                "artifactId": t.string(),
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsTestIamPermissions"
    ] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "parent": t.string(),
                "artifactId": t.string(),
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsGet"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "parent": t.string(),
                "artifactId": t.string(),
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsGetIamPolicy"
    ] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "parent": t.string(),
                "artifactId": t.string(),
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisVersionsSpecsArtifactsList"] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "parent": t.string(),
                "artifactId": t.string(),
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisVersionsSpecsArtifactsCreate"
    ] = apigeeregistry.post(
        "v1/{parent}/artifacts",
        t.struct(
            {
                "parent": t.string(),
                "artifactId": t.string(),
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
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
    functions["projectsLocationsApisDeploymentsGetIamPolicy"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsCreate"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsRollback"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsTagRevision"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsGet"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsList"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsSetIamPolicy"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsDelete"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsDeleteRevision"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsListRevisions"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsApisDeploymentsTestIamPermissions"
    ] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsPatch"] = apigeeregistry.patch(
        "v1/{name}",
        t.struct(
            {
                "allowMissing": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "accessGuidance": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "intendedAudience": t.string().optional(),
                "externalChannelUri": t.string().optional(),
                "apiSpecRevision": t.string().optional(),
                "endpointUri": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApiDeploymentOut"]),
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
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
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
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
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
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApisDeploymentsArtifactsGet"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
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
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
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
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = apigeeregistry.post(
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
    functions["projectsLocationsOperationsGet"] = apigeeregistry.post(
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
    functions["projectsLocationsOperationsList"] = apigeeregistry.post(
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
    functions["projectsLocationsOperationsCancel"] = apigeeregistry.post(
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
    functions["projectsLocationsInstancesCreate"] = apigeeregistry.delete(
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
    functions["projectsLocationsInstancesTestIamPermissions"] = apigeeregistry.delete(
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
    functions["projectsLocationsInstancesGet"] = apigeeregistry.delete(
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
    functions["projectsLocationsArtifactsSetIamPolicy"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsTestIamPermissions"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsList"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsDelete"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGetContents"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsCreate"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGet"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsGetIamPolicy"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsArtifactsReplaceArtifact"] = apigeeregistry.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "mimeType": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "contents": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ArtifactOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="apigeeregistry", renames=renames, types=types, functions=functions
    )
