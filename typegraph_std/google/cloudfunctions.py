from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudfunctions() -> Import:
    cloudfunctions = HTTPRuntime("https://cloudfunctions.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudfunctions_1_ErrorResponse",
        "ListOperationsResponseIn": "_cloudfunctions_2_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudfunctions_3_ListOperationsResponseOut",
        "AuditLogConfigIn": "_cloudfunctions_4_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudfunctions_5_AuditLogConfigOut",
        "AuditConfigIn": "_cloudfunctions_6_AuditConfigIn",
        "AuditConfigOut": "_cloudfunctions_7_AuditConfigOut",
        "ListRuntimesResponseIn": "_cloudfunctions_8_ListRuntimesResponseIn",
        "ListRuntimesResponseOut": "_cloudfunctions_9_ListRuntimesResponseOut",
        "LocationIn": "_cloudfunctions_10_LocationIn",
        "LocationOut": "_cloudfunctions_11_LocationOut",
        "TestIamPermissionsResponseIn": "_cloudfunctions_12_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudfunctions_13_TestIamPermissionsResponseOut",
        "GoogleCloudFunctionsV2alphaStateMessageIn": "_cloudfunctions_14_GoogleCloudFunctionsV2alphaStateMessageIn",
        "GoogleCloudFunctionsV2alphaStateMessageOut": "_cloudfunctions_15_GoogleCloudFunctionsV2alphaStateMessageOut",
        "GenerateUploadUrlRequestIn": "_cloudfunctions_16_GenerateUploadUrlRequestIn",
        "GenerateUploadUrlRequestOut": "_cloudfunctions_17_GenerateUploadUrlRequestOut",
        "GoogleCloudFunctionsV2alphaStageIn": "_cloudfunctions_18_GoogleCloudFunctionsV2alphaStageIn",
        "GoogleCloudFunctionsV2alphaStageOut": "_cloudfunctions_19_GoogleCloudFunctionsV2alphaStageOut",
        "ListFunctionsResponseIn": "_cloudfunctions_20_ListFunctionsResponseIn",
        "ListFunctionsResponseOut": "_cloudfunctions_21_ListFunctionsResponseOut",
        "StorageSourceIn": "_cloudfunctions_22_StorageSourceIn",
        "StorageSourceOut": "_cloudfunctions_23_StorageSourceOut",
        "PolicyIn": "_cloudfunctions_24_PolicyIn",
        "PolicyOut": "_cloudfunctions_25_PolicyOut",
        "BuildConfigIn": "_cloudfunctions_26_BuildConfigIn",
        "BuildConfigOut": "_cloudfunctions_27_BuildConfigOut",
        "GenerateDownloadUrlResponseIn": "_cloudfunctions_28_GenerateDownloadUrlResponseIn",
        "GenerateDownloadUrlResponseOut": "_cloudfunctions_29_GenerateDownloadUrlResponseOut",
        "GoogleCloudFunctionsV2betaStageIn": "_cloudfunctions_30_GoogleCloudFunctionsV2betaStageIn",
        "GoogleCloudFunctionsV2betaStageOut": "_cloudfunctions_31_GoogleCloudFunctionsV2betaStageOut",
        "GenerateDownloadUrlRequestIn": "_cloudfunctions_32_GenerateDownloadUrlRequestIn",
        "GenerateDownloadUrlRequestOut": "_cloudfunctions_33_GenerateDownloadUrlRequestOut",
        "GoogleCloudFunctionsV2betaStateMessageIn": "_cloudfunctions_34_GoogleCloudFunctionsV2betaStateMessageIn",
        "GoogleCloudFunctionsV2betaStateMessageOut": "_cloudfunctions_35_GoogleCloudFunctionsV2betaStateMessageOut",
        "GoogleCloudFunctionsV2OperationMetadataIn": "_cloudfunctions_36_GoogleCloudFunctionsV2OperationMetadataIn",
        "GoogleCloudFunctionsV2OperationMetadataOut": "_cloudfunctions_37_GoogleCloudFunctionsV2OperationMetadataOut",
        "OperationMetadataV1In": "_cloudfunctions_38_OperationMetadataV1In",
        "OperationMetadataV1Out": "_cloudfunctions_39_OperationMetadataV1Out",
        "FunctionIn": "_cloudfunctions_40_FunctionIn",
        "FunctionOut": "_cloudfunctions_41_FunctionOut",
        "ExprIn": "_cloudfunctions_42_ExprIn",
        "ExprOut": "_cloudfunctions_43_ExprOut",
        "BindingIn": "_cloudfunctions_44_BindingIn",
        "BindingOut": "_cloudfunctions_45_BindingOut",
        "GoogleCloudFunctionsV2StageIn": "_cloudfunctions_46_GoogleCloudFunctionsV2StageIn",
        "GoogleCloudFunctionsV2StageOut": "_cloudfunctions_47_GoogleCloudFunctionsV2StageOut",
        "SourceIn": "_cloudfunctions_48_SourceIn",
        "SourceOut": "_cloudfunctions_49_SourceOut",
        "SourceProvenanceIn": "_cloudfunctions_50_SourceProvenanceIn",
        "SourceProvenanceOut": "_cloudfunctions_51_SourceProvenanceOut",
        "ListLocationsResponseIn": "_cloudfunctions_52_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudfunctions_53_ListLocationsResponseOut",
        "SecretVersionIn": "_cloudfunctions_54_SecretVersionIn",
        "SecretVersionOut": "_cloudfunctions_55_SecretVersionOut",
        "SecretEnvVarIn": "_cloudfunctions_56_SecretEnvVarIn",
        "SecretEnvVarOut": "_cloudfunctions_57_SecretEnvVarOut",
        "ServiceConfigIn": "_cloudfunctions_58_ServiceConfigIn",
        "ServiceConfigOut": "_cloudfunctions_59_ServiceConfigOut",
        "GoogleCloudFunctionsV2betaOperationMetadataIn": "_cloudfunctions_60_GoogleCloudFunctionsV2betaOperationMetadataIn",
        "GoogleCloudFunctionsV2betaOperationMetadataOut": "_cloudfunctions_61_GoogleCloudFunctionsV2betaOperationMetadataOut",
        "EventFilterIn": "_cloudfunctions_62_EventFilterIn",
        "EventFilterOut": "_cloudfunctions_63_EventFilterOut",
        "TestIamPermissionsRequestIn": "_cloudfunctions_64_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudfunctions_65_TestIamPermissionsRequestOut",
        "SetIamPolicyRequestIn": "_cloudfunctions_66_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudfunctions_67_SetIamPolicyRequestOut",
        "SecretVolumeIn": "_cloudfunctions_68_SecretVolumeIn",
        "SecretVolumeOut": "_cloudfunctions_69_SecretVolumeOut",
        "GenerateUploadUrlResponseIn": "_cloudfunctions_70_GenerateUploadUrlResponseIn",
        "GenerateUploadUrlResponseOut": "_cloudfunctions_71_GenerateUploadUrlResponseOut",
        "RepoSourceIn": "_cloudfunctions_72_RepoSourceIn",
        "RepoSourceOut": "_cloudfunctions_73_RepoSourceOut",
        "OperationIn": "_cloudfunctions_74_OperationIn",
        "OperationOut": "_cloudfunctions_75_OperationOut",
        "EventTriggerIn": "_cloudfunctions_76_EventTriggerIn",
        "EventTriggerOut": "_cloudfunctions_77_EventTriggerOut",
        "StatusIn": "_cloudfunctions_78_StatusIn",
        "StatusOut": "_cloudfunctions_79_StatusOut",
        "RuntimeIn": "_cloudfunctions_80_RuntimeIn",
        "RuntimeOut": "_cloudfunctions_81_RuntimeOut",
        "GoogleCloudFunctionsV2alphaOperationMetadataIn": "_cloudfunctions_82_GoogleCloudFunctionsV2alphaOperationMetadataIn",
        "GoogleCloudFunctionsV2alphaOperationMetadataOut": "_cloudfunctions_83_GoogleCloudFunctionsV2alphaOperationMetadataOut",
        "GoogleCloudFunctionsV2StateMessageIn": "_cloudfunctions_84_GoogleCloudFunctionsV2StateMessageIn",
        "GoogleCloudFunctionsV2StateMessageOut": "_cloudfunctions_85_GoogleCloudFunctionsV2StateMessageOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["ListRuntimesResponseIn"] = t.struct(
        {"runtimes": t.array(t.proxy(renames["RuntimeIn"])).optional()}
    ).named(renames["ListRuntimesResponseIn"])
    types["ListRuntimesResponseOut"] = t.struct(
        {
            "runtimes": t.array(t.proxy(renames["RuntimeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRuntimesResponseOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["GoogleCloudFunctionsV2alphaStateMessageIn"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStateMessageIn"])
    types["GoogleCloudFunctionsV2alphaStateMessageOut"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStateMessageOut"])
    types["GenerateUploadUrlRequestIn"] = t.struct(
        {"kmsKeyName": t.string().optional()}
    ).named(renames["GenerateUploadUrlRequestIn"])
    types["GenerateUploadUrlRequestOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateUploadUrlRequestOut"])
    types["GoogleCloudFunctionsV2alphaStageIn"] = t.struct(
        {
            "message": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStateMessageIn"])
            ).optional(),
            "name": t.string().optional(),
            "resourceUri": t.string().optional(),
            "resource": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStageIn"])
    types["GoogleCloudFunctionsV2alphaStageOut"] = t.struct(
        {
            "message": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStateMessageOut"])
            ).optional(),
            "name": t.string().optional(),
            "resourceUri": t.string().optional(),
            "resource": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStageOut"])
    types["ListFunctionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "functions": t.array(t.proxy(renames["FunctionIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListFunctionsResponseIn"])
    types["ListFunctionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "functions": t.array(t.proxy(renames["FunctionOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFunctionsResponseOut"])
    types["StorageSourceIn"] = t.struct(
        {
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
        }
    ).named(renames["StorageSourceIn"])
    types["StorageSourceOut"] = t.struct(
        {
            "object": t.string().optional(),
            "bucket": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorageSourceOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["BuildConfigIn"] = t.struct(
        {
            "dockerRegistry": t.string().optional(),
            "dockerRepository": t.string().optional(),
            "workerPool": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "runtime": t.string().optional(),
            "entryPoint": t.string().optional(),
        }
    ).named(renames["BuildConfigIn"])
    types["BuildConfigOut"] = t.struct(
        {
            "dockerRegistry": t.string().optional(),
            "dockerRepository": t.string().optional(),
            "build": t.string().optional(),
            "workerPool": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "sourceProvenance": t.proxy(renames["SourceProvenanceOut"]).optional(),
            "runtime": t.string().optional(),
            "entryPoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildConfigOut"])
    types["GenerateDownloadUrlResponseIn"] = t.struct(
        {"downloadUrl": t.string().optional()}
    ).named(renames["GenerateDownloadUrlResponseIn"])
    types["GenerateDownloadUrlResponseOut"] = t.struct(
        {
            "downloadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateDownloadUrlResponseOut"])
    types["GoogleCloudFunctionsV2betaStageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "message": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "resourceUri": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStateMessageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStageIn"])
    types["GoogleCloudFunctionsV2betaStageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "message": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "resourceUri": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStateMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStageOut"])
    types["GenerateDownloadUrlRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateDownloadUrlRequestIn"])
    types["GenerateDownloadUrlRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateDownloadUrlRequestOut"])
    types["GoogleCloudFunctionsV2betaStateMessageIn"] = t.struct(
        {
            "type": t.string().optional(),
            "severity": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStateMessageIn"])
    types["GoogleCloudFunctionsV2betaStateMessageOut"] = t.struct(
        {
            "type": t.string().optional(),
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStateMessageOut"])
    types["GoogleCloudFunctionsV2OperationMetadataIn"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StageIn"])
            ).optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusDetail": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2OperationMetadataIn"])
    types["GoogleCloudFunctionsV2OperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StageOut"])
            ).optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2OperationMetadataOut"])
    types["OperationMetadataV1In"] = t.struct(
        {
            "request": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "buildName": t.string().optional(),
            "sourceToken": t.string().optional(),
            "updateTime": t.string().optional(),
            "buildId": t.string().optional(),
            "target": t.string().optional(),
            "versionId": t.string().optional(),
        }
    ).named(renames["OperationMetadataV1In"])
    types["OperationMetadataV1Out"] = t.struct(
        {
            "request": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "buildName": t.string().optional(),
            "sourceToken": t.string().optional(),
            "updateTime": t.string().optional(),
            "buildId": t.string().optional(),
            "target": t.string().optional(),
            "versionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Out"])
    types["FunctionIn"] = t.struct(
        {
            "buildConfig": t.proxy(renames["BuildConfigIn"]).optional(),
            "description": t.string().optional(),
            "environment": t.string().optional(),
            "eventTrigger": t.proxy(renames["EventTriggerIn"]).optional(),
            "name": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceConfig": t.proxy(renames["ServiceConfigIn"]).optional(),
        }
    ).named(renames["FunctionIn"])
    types["FunctionOut"] = t.struct(
        {
            "buildConfig": t.proxy(renames["BuildConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "environment": t.string().optional(),
            "eventTrigger": t.proxy(renames["EventTriggerOut"]).optional(),
            "name": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceConfig": t.proxy(renames["ServiceConfigOut"]).optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["GoogleCloudFunctionsV2StageIn"] = t.struct(
        {
            "message": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "resourceUri": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StageIn"])
    types["GoogleCloudFunctionsV2StageOut"] = t.struct(
        {
            "message": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "resource": t.string().optional(),
            "resourceUri": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StageOut"])
    types["SourceIn"] = t.struct(
        {
            "repoSource": t.proxy(renames["RepoSourceIn"]).optional(),
            "storageSource": t.proxy(renames["StorageSourceIn"]).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "repoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "storageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["SourceProvenanceIn"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(renames["StorageSourceIn"]).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceIn"]).optional(),
        }
    ).named(renames["SourceProvenanceIn"])
    types["SourceProvenanceOut"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceProvenanceOut"])
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
    types["SecretVersionIn"] = t.struct(
        {"path": t.string().optional(), "version": t.string().optional()}
    ).named(renames["SecretVersionIn"])
    types["SecretVersionOut"] = t.struct(
        {
            "path": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVersionOut"])
    types["SecretEnvVarIn"] = t.struct(
        {
            "key": t.string().optional(),
            "version": t.string().optional(),
            "secret": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SecretEnvVarIn"])
    types["SecretEnvVarOut"] = t.struct(
        {
            "key": t.string().optional(),
            "version": t.string().optional(),
            "secret": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretEnvVarOut"])
    types["ServiceConfigIn"] = t.struct(
        {
            "minInstanceCount": t.integer().optional(),
            "allTrafficOnLatestRevision": t.boolean().optional(),
            "availableCpu": t.string().optional(),
            "secretEnvironmentVariables": t.array(
                t.proxy(renames["SecretEnvVarIn"])
            ).optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "timeoutSeconds": t.integer().optional(),
            "securityLevel": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "ingressSettings": t.string().optional(),
            "vpcConnector": t.string().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "availableMemory": t.string().optional(),
            "maxInstanceCount": t.integer().optional(),
            "vpcConnectorEgressSettings": t.string().optional(),
            "secretVolumes": t.array(t.proxy(renames["SecretVolumeIn"])).optional(),
        }
    ).named(renames["ServiceConfigIn"])
    types["ServiceConfigOut"] = t.struct(
        {
            "minInstanceCount": t.integer().optional(),
            "allTrafficOnLatestRevision": t.boolean().optional(),
            "availableCpu": t.string().optional(),
            "secretEnvironmentVariables": t.array(
                t.proxy(renames["SecretEnvVarOut"])
            ).optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "timeoutSeconds": t.integer().optional(),
            "securityLevel": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "ingressSettings": t.string().optional(),
            "vpcConnector": t.string().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string().optional(),
            "availableMemory": t.string().optional(),
            "revision": t.string().optional(),
            "maxInstanceCount": t.integer().optional(),
            "vpcConnectorEgressSettings": t.string().optional(),
            "service": t.string().optional(),
            "secretVolumes": t.array(t.proxy(renames["SecretVolumeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConfigOut"])
    types["GoogleCloudFunctionsV2betaOperationMetadataIn"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStageIn"])
            ).optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaOperationMetadataIn"])
    types["GoogleCloudFunctionsV2betaOperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStageOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaOperationMetadataOut"])
    types["EventFilterIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "value": t.string(),
            "attribute": t.string(),
        }
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "value": t.string(),
            "attribute": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["SecretVolumeIn"] = t.struct(
        {
            "secret": t.string().optional(),
            "mountPath": t.string().optional(),
            "versions": t.array(t.proxy(renames["SecretVersionIn"])).optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SecretVolumeIn"])
    types["SecretVolumeOut"] = t.struct(
        {
            "secret": t.string().optional(),
            "mountPath": t.string().optional(),
            "versions": t.array(t.proxy(renames["SecretVersionOut"])).optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVolumeOut"])
    types["GenerateUploadUrlResponseIn"] = t.struct(
        {
            "uploadUrl": t.string().optional(),
            "storageSource": t.proxy(renames["StorageSourceIn"]).optional(),
        }
    ).named(renames["GenerateUploadUrlResponseIn"])
    types["GenerateUploadUrlResponseOut"] = t.struct(
        {
            "uploadUrl": t.string().optional(),
            "storageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateUploadUrlResponseOut"])
    types["RepoSourceIn"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "repoName": t.string().optional(),
            "tagName": t.string().optional(),
            "projectId": t.string().optional(),
            "commitSha": t.string().optional(),
            "dir": t.string().optional(),
            "branchName": t.string().optional(),
        }
    ).named(renames["RepoSourceIn"])
    types["RepoSourceOut"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "repoName": t.string().optional(),
            "tagName": t.string().optional(),
            "projectId": t.string().optional(),
            "commitSha": t.string().optional(),
            "dir": t.string().optional(),
            "branchName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoSourceOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["EventTriggerIn"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "eventType": t.string(),
            "channel": t.string().optional(),
            "retryPolicy": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional(),
            "triggerRegion": t.string().optional(),
        }
    ).named(renames["EventTriggerIn"])
    types["EventTriggerOut"] = t.struct(
        {
            "pubsubTopic": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "eventType": t.string(),
            "channel": t.string().optional(),
            "retryPolicy": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "trigger": t.string().optional(),
            "triggerRegion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTriggerOut"])
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
    types["RuntimeIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "stage": t.string().optional(),
            "environment": t.string().optional(),
        }
    ).named(renames["RuntimeIn"])
    types["RuntimeOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "stage": t.string().optional(),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeOut"])
    types["GoogleCloudFunctionsV2alphaOperationMetadataIn"] = t.struct(
        {
            "statusDetail": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStageIn"])
            ).optional(),
            "apiVersion": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaOperationMetadataIn"])
    types["GoogleCloudFunctionsV2alphaOperationMetadataOut"] = t.struct(
        {
            "statusDetail": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStageOut"])
            ).optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaOperationMetadataOut"])
    types["GoogleCloudFunctionsV2StateMessageIn"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StateMessageIn"])
    types["GoogleCloudFunctionsV2StateMessageOut"] = t.struct(
        {
            "message": t.string().optional(),
            "type": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StateMessageOut"])

    functions = {}
    functions["projectsLocationsList"] = cloudfunctions.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = cloudfunctions.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = cloudfunctions.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimesList"] = cloudfunctions.get(
        "v2/{parent}/runtimes",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListRuntimesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsGet"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsDelete"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsGenerateUploadUrl"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsCreate"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsList"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsGetIamPolicy"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsPatch"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsTestIamPermissions"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsGenerateDownloadUrl"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsSetIamPolicy"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudfunctions",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
