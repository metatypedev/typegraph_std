from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudfunctions() -> Import:
    cloudfunctions = HTTPRuntime("https://cloudfunctions.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudfunctions_1_ErrorResponse",
        "FunctionIn": "_cloudfunctions_2_FunctionIn",
        "FunctionOut": "_cloudfunctions_3_FunctionOut",
        "BuildConfigIn": "_cloudfunctions_4_BuildConfigIn",
        "BuildConfigOut": "_cloudfunctions_5_BuildConfigOut",
        "GoogleCloudFunctionsV2alphaStateMessageIn": "_cloudfunctions_6_GoogleCloudFunctionsV2alphaStateMessageIn",
        "GoogleCloudFunctionsV2alphaStateMessageOut": "_cloudfunctions_7_GoogleCloudFunctionsV2alphaStateMessageOut",
        "GoogleCloudFunctionsV2alphaStageIn": "_cloudfunctions_8_GoogleCloudFunctionsV2alphaStageIn",
        "GoogleCloudFunctionsV2alphaStageOut": "_cloudfunctions_9_GoogleCloudFunctionsV2alphaStageOut",
        "ListOperationsResponseIn": "_cloudfunctions_10_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudfunctions_11_ListOperationsResponseOut",
        "AuditConfigIn": "_cloudfunctions_12_AuditConfigIn",
        "AuditConfigOut": "_cloudfunctions_13_AuditConfigOut",
        "SecretVersionIn": "_cloudfunctions_14_SecretVersionIn",
        "SecretVersionOut": "_cloudfunctions_15_SecretVersionOut",
        "StatusIn": "_cloudfunctions_16_StatusIn",
        "StatusOut": "_cloudfunctions_17_StatusOut",
        "GoogleCloudFunctionsV2OperationMetadataIn": "_cloudfunctions_18_GoogleCloudFunctionsV2OperationMetadataIn",
        "GoogleCloudFunctionsV2OperationMetadataOut": "_cloudfunctions_19_GoogleCloudFunctionsV2OperationMetadataOut",
        "StorageSourceIn": "_cloudfunctions_20_StorageSourceIn",
        "StorageSourceOut": "_cloudfunctions_21_StorageSourceOut",
        "OperationMetadataV1In": "_cloudfunctions_22_OperationMetadataV1In",
        "OperationMetadataV1Out": "_cloudfunctions_23_OperationMetadataV1Out",
        "SourceIn": "_cloudfunctions_24_SourceIn",
        "SourceOut": "_cloudfunctions_25_SourceOut",
        "AuditLogConfigIn": "_cloudfunctions_26_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudfunctions_27_AuditLogConfigOut",
        "ServiceConfigIn": "_cloudfunctions_28_ServiceConfigIn",
        "ServiceConfigOut": "_cloudfunctions_29_ServiceConfigOut",
        "SetIamPolicyRequestIn": "_cloudfunctions_30_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudfunctions_31_SetIamPolicyRequestOut",
        "SecretVolumeIn": "_cloudfunctions_32_SecretVolumeIn",
        "SecretVolumeOut": "_cloudfunctions_33_SecretVolumeOut",
        "OperationIn": "_cloudfunctions_34_OperationIn",
        "OperationOut": "_cloudfunctions_35_OperationOut",
        "GoogleCloudFunctionsV2StageIn": "_cloudfunctions_36_GoogleCloudFunctionsV2StageIn",
        "GoogleCloudFunctionsV2StageOut": "_cloudfunctions_37_GoogleCloudFunctionsV2StageOut",
        "ExprIn": "_cloudfunctions_38_ExprIn",
        "ExprOut": "_cloudfunctions_39_ExprOut",
        "SecretEnvVarIn": "_cloudfunctions_40_SecretEnvVarIn",
        "SecretEnvVarOut": "_cloudfunctions_41_SecretEnvVarOut",
        "GenerateDownloadUrlRequestIn": "_cloudfunctions_42_GenerateDownloadUrlRequestIn",
        "GenerateDownloadUrlRequestOut": "_cloudfunctions_43_GenerateDownloadUrlRequestOut",
        "LocationIn": "_cloudfunctions_44_LocationIn",
        "LocationOut": "_cloudfunctions_45_LocationOut",
        "BindingIn": "_cloudfunctions_46_BindingIn",
        "BindingOut": "_cloudfunctions_47_BindingOut",
        "SourceProvenanceIn": "_cloudfunctions_48_SourceProvenanceIn",
        "SourceProvenanceOut": "_cloudfunctions_49_SourceProvenanceOut",
        "GenerateDownloadUrlResponseIn": "_cloudfunctions_50_GenerateDownloadUrlResponseIn",
        "GenerateDownloadUrlResponseOut": "_cloudfunctions_51_GenerateDownloadUrlResponseOut",
        "EventTriggerIn": "_cloudfunctions_52_EventTriggerIn",
        "EventTriggerOut": "_cloudfunctions_53_EventTriggerOut",
        "GoogleCloudFunctionsV2betaStateMessageIn": "_cloudfunctions_54_GoogleCloudFunctionsV2betaStateMessageIn",
        "GoogleCloudFunctionsV2betaStateMessageOut": "_cloudfunctions_55_GoogleCloudFunctionsV2betaStateMessageOut",
        "RepoSourceIn": "_cloudfunctions_56_RepoSourceIn",
        "RepoSourceOut": "_cloudfunctions_57_RepoSourceOut",
        "ListLocationsResponseIn": "_cloudfunctions_58_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudfunctions_59_ListLocationsResponseOut",
        "RuntimeIn": "_cloudfunctions_60_RuntimeIn",
        "RuntimeOut": "_cloudfunctions_61_RuntimeOut",
        "GenerateUploadUrlRequestIn": "_cloudfunctions_62_GenerateUploadUrlRequestIn",
        "GenerateUploadUrlRequestOut": "_cloudfunctions_63_GenerateUploadUrlRequestOut",
        "ListRuntimesResponseIn": "_cloudfunctions_64_ListRuntimesResponseIn",
        "ListRuntimesResponseOut": "_cloudfunctions_65_ListRuntimesResponseOut",
        "TestIamPermissionsRequestIn": "_cloudfunctions_66_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudfunctions_67_TestIamPermissionsRequestOut",
        "GenerateUploadUrlResponseIn": "_cloudfunctions_68_GenerateUploadUrlResponseIn",
        "GenerateUploadUrlResponseOut": "_cloudfunctions_69_GenerateUploadUrlResponseOut",
        "EventFilterIn": "_cloudfunctions_70_EventFilterIn",
        "EventFilterOut": "_cloudfunctions_71_EventFilterOut",
        "GoogleCloudFunctionsV2alphaOperationMetadataIn": "_cloudfunctions_72_GoogleCloudFunctionsV2alphaOperationMetadataIn",
        "GoogleCloudFunctionsV2alphaOperationMetadataOut": "_cloudfunctions_73_GoogleCloudFunctionsV2alphaOperationMetadataOut",
        "GoogleCloudFunctionsV2StateMessageIn": "_cloudfunctions_74_GoogleCloudFunctionsV2StateMessageIn",
        "GoogleCloudFunctionsV2StateMessageOut": "_cloudfunctions_75_GoogleCloudFunctionsV2StateMessageOut",
        "TestIamPermissionsResponseIn": "_cloudfunctions_76_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudfunctions_77_TestIamPermissionsResponseOut",
        "ListFunctionsResponseIn": "_cloudfunctions_78_ListFunctionsResponseIn",
        "ListFunctionsResponseOut": "_cloudfunctions_79_ListFunctionsResponseOut",
        "PolicyIn": "_cloudfunctions_80_PolicyIn",
        "PolicyOut": "_cloudfunctions_81_PolicyOut",
        "GoogleCloudFunctionsV2betaStageIn": "_cloudfunctions_82_GoogleCloudFunctionsV2betaStageIn",
        "GoogleCloudFunctionsV2betaStageOut": "_cloudfunctions_83_GoogleCloudFunctionsV2betaStageOut",
        "GoogleCloudFunctionsV2betaOperationMetadataIn": "_cloudfunctions_84_GoogleCloudFunctionsV2betaOperationMetadataIn",
        "GoogleCloudFunctionsV2betaOperationMetadataOut": "_cloudfunctions_85_GoogleCloudFunctionsV2betaOperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FunctionIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
            "serviceConfig": t.proxy(renames["ServiceConfigIn"]).optional(),
            "name": t.string().optional(),
            "buildConfig": t.proxy(renames["BuildConfigIn"]).optional(),
            "environment": t.string().optional(),
            "eventTrigger": t.proxy(renames["EventTriggerIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["FunctionIn"])
    types["FunctionOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "kmsKeyName": t.string().optional(),
            "serviceConfig": t.proxy(renames["ServiceConfigOut"]).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "buildConfig": t.proxy(renames["BuildConfigOut"]).optional(),
            "environment": t.string().optional(),
            "eventTrigger": t.proxy(renames["EventTriggerOut"]).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionOut"])
    types["BuildConfigIn"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "dockerRegistry": t.string().optional(),
            "runtime": t.string().optional(),
            "dockerRepository": t.string().optional(),
        }
    ).named(renames["BuildConfigIn"])
    types["BuildConfigOut"] = t.struct(
        {
            "workerPool": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "dockerRegistry": t.string().optional(),
            "runtime": t.string().optional(),
            "build": t.string().optional(),
            "dockerRepository": t.string().optional(),
            "sourceProvenance": t.proxy(renames["SourceProvenanceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildConfigOut"])
    types["GoogleCloudFunctionsV2alphaStateMessageIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStateMessageIn"])
    types["GoogleCloudFunctionsV2alphaStateMessageOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStateMessageOut"])
    types["GoogleCloudFunctionsV2alphaStageIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "message": t.string().optional(),
            "resourceUri": t.string().optional(),
            "state": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStateMessageIn"])
            ).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStageIn"])
    types["GoogleCloudFunctionsV2alphaStageOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "message": t.string().optional(),
            "resourceUri": t.string().optional(),
            "state": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStateMessageOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStageOut"])
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
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["GoogleCloudFunctionsV2OperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StageIn"])
            ).optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2OperationMetadataIn"])
    types["GoogleCloudFunctionsV2OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StageOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2OperationMetadataOut"])
    types["StorageSourceIn"] = t.struct(
        {
            "bucket": t.string().optional(),
            "object": t.string().optional(),
            "generation": t.string().optional(),
        }
    ).named(renames["StorageSourceIn"])
    types["StorageSourceOut"] = t.struct(
        {
            "bucket": t.string().optional(),
            "object": t.string().optional(),
            "generation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorageSourceOut"])
    types["OperationMetadataV1In"] = t.struct(
        {
            "buildId": t.string().optional(),
            "target": t.string().optional(),
            "versionId": t.string().optional(),
            "sourceToken": t.string().optional(),
            "buildName": t.string().optional(),
            "updateTime": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["OperationMetadataV1In"])
    types["OperationMetadataV1Out"] = t.struct(
        {
            "buildId": t.string().optional(),
            "target": t.string().optional(),
            "versionId": t.string().optional(),
            "sourceToken": t.string().optional(),
            "buildName": t.string().optional(),
            "updateTime": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Out"])
    types["SourceIn"] = t.struct(
        {
            "storageSource": t.proxy(renames["StorageSourceIn"]).optional(),
            "repoSource": t.proxy(renames["RepoSourceIn"]).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "storageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "repoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["ServiceConfigIn"] = t.struct(
        {
            "availableMemory": t.string().optional(),
            "timeoutSeconds": t.integer().optional(),
            "securityLevel": t.string().optional(),
            "vpcConnectorEgressSettings": t.string().optional(),
            "maxInstanceCount": t.integer().optional(),
            "vpcConnector": t.string().optional(),
            "allTrafficOnLatestRevision": t.boolean().optional(),
            "serviceAccountEmail": t.string().optional(),
            "ingressSettings": t.string().optional(),
            "secretVolumes": t.array(t.proxy(renames["SecretVolumeIn"])).optional(),
            "availableCpu": t.string().optional(),
            "minInstanceCount": t.integer().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "secretEnvironmentVariables": t.array(
                t.proxy(renames["SecretEnvVarIn"])
            ).optional(),
        }
    ).named(renames["ServiceConfigIn"])
    types["ServiceConfigOut"] = t.struct(
        {
            "availableMemory": t.string().optional(),
            "timeoutSeconds": t.integer().optional(),
            "revision": t.string().optional(),
            "securityLevel": t.string().optional(),
            "vpcConnectorEgressSettings": t.string().optional(),
            "maxInstanceCount": t.integer().optional(),
            "vpcConnector": t.string().optional(),
            "allTrafficOnLatestRevision": t.boolean().optional(),
            "serviceAccountEmail": t.string().optional(),
            "ingressSettings": t.string().optional(),
            "secretVolumes": t.array(t.proxy(renames["SecretVolumeOut"])).optional(),
            "service": t.string().optional(),
            "availableCpu": t.string().optional(),
            "minInstanceCount": t.integer().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "uri": t.string().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "secretEnvironmentVariables": t.array(
                t.proxy(renames["SecretEnvVarOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConfigOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["SecretVolumeIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "mountPath": t.string().optional(),
            "versions": t.array(t.proxy(renames["SecretVersionIn"])).optional(),
            "secret": t.string().optional(),
        }
    ).named(renames["SecretVolumeIn"])
    types["SecretVolumeOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "mountPath": t.string().optional(),
            "versions": t.array(t.proxy(renames["SecretVersionOut"])).optional(),
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVolumeOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleCloudFunctionsV2StageIn"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "message": t.string().optional(),
            "resourceUri": t.string().optional(),
            "resource": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StageIn"])
    types["GoogleCloudFunctionsV2StageOut"] = t.struct(
        {
            "state": t.string().optional(),
            "name": t.string().optional(),
            "message": t.string().optional(),
            "resourceUri": t.string().optional(),
            "resource": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StageOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["SecretEnvVarIn"] = t.struct(
        {
            "secret": t.string().optional(),
            "key": t.string().optional(),
            "version": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SecretEnvVarIn"])
    types["SecretEnvVarOut"] = t.struct(
        {
            "secret": t.string().optional(),
            "key": t.string().optional(),
            "version": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretEnvVarOut"])
    types["GenerateDownloadUrlRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateDownloadUrlRequestIn"])
    types["GenerateDownloadUrlRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateDownloadUrlRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["GenerateDownloadUrlResponseIn"] = t.struct(
        {"downloadUrl": t.string().optional()}
    ).named(renames["GenerateDownloadUrlResponseIn"])
    types["GenerateDownloadUrlResponseOut"] = t.struct(
        {
            "downloadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateDownloadUrlResponseOut"])
    types["EventTriggerIn"] = t.struct(
        {
            "triggerRegion": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional(),
            "channel": t.string().optional(),
            "retryPolicy": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "eventType": t.string(),
        }
    ).named(renames["EventTriggerIn"])
    types["EventTriggerOut"] = t.struct(
        {
            "trigger": t.string().optional(),
            "triggerRegion": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "channel": t.string().optional(),
            "retryPolicy": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "eventType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTriggerOut"])
    types["GoogleCloudFunctionsV2betaStateMessageIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStateMessageIn"])
    types["GoogleCloudFunctionsV2betaStateMessageOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "type": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStateMessageOut"])
    types["RepoSourceIn"] = t.struct(
        {
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "tagName": t.string().optional(),
            "invertRegex": t.boolean().optional(),
        }
    ).named(renames["RepoSourceIn"])
    types["RepoSourceOut"] = t.struct(
        {
            "dir": t.string().optional(),
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "tagName": t.string().optional(),
            "invertRegex": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoSourceOut"])
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
    types["RuntimeIn"] = t.struct(
        {
            "environment": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "stage": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["RuntimeIn"])
    types["RuntimeOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "warnings": t.array(t.string()).optional(),
            "stage": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeOut"])
    types["GenerateUploadUrlRequestIn"] = t.struct(
        {"kmsKeyName": t.string().optional()}
    ).named(renames["GenerateUploadUrlRequestIn"])
    types["GenerateUploadUrlRequestOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateUploadUrlRequestOut"])
    types["ListRuntimesResponseIn"] = t.struct(
        {"runtimes": t.array(t.proxy(renames["RuntimeIn"])).optional()}
    ).named(renames["ListRuntimesResponseIn"])
    types["ListRuntimesResponseOut"] = t.struct(
        {
            "runtimes": t.array(t.proxy(renames["RuntimeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRuntimesResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GenerateUploadUrlResponseIn"] = t.struct(
        {
            "storageSource": t.proxy(renames["StorageSourceIn"]).optional(),
            "uploadUrl": t.string().optional(),
        }
    ).named(renames["GenerateUploadUrlResponseIn"])
    types["GenerateUploadUrlResponseOut"] = t.struct(
        {
            "storageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "uploadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateUploadUrlResponseOut"])
    types["EventFilterIn"] = t.struct(
        {
            "value": t.string(),
            "attribute": t.string(),
            "operator": t.string().optional(),
        }
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "value": t.string(),
            "attribute": t.string(),
            "operator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
    types["GoogleCloudFunctionsV2alphaOperationMetadataIn"] = t.struct(
        {
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStageIn"])
            ).optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "apiVersion": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaOperationMetadataIn"])
    types["GoogleCloudFunctionsV2alphaOperationMetadataOut"] = t.struct(
        {
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStageOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "verb": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaOperationMetadataOut"])
    types["GoogleCloudFunctionsV2StateMessageIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StateMessageIn"])
    types["GoogleCloudFunctionsV2StateMessageOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StateMessageOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GoogleCloudFunctionsV2betaStageIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "resourceUri": t.string().optional(),
            "name": t.string().optional(),
            "message": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStateMessageIn"])
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStageIn"])
    types["GoogleCloudFunctionsV2betaStageOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "resourceUri": t.string().optional(),
            "name": t.string().optional(),
            "message": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStateMessageOut"])
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStageOut"])
    types["GoogleCloudFunctionsV2betaOperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStageIn"])
            ).optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "cancelRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaOperationMetadataIn"])
    types["GoogleCloudFunctionsV2betaOperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStageOut"])
            ).optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "cancelRequested": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaOperationMetadataOut"])

    functions = {}
    functions["projectsLocationsList"] = cloudfunctions.get(
        "v2/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsPatch"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsGenerateDownloadUrl"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsDelete"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsGet"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsGenerateUploadUrl"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsSetIamPolicy"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsTestIamPermissions"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsGetIamPolicy"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsCreate"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsList"] = cloudfunctions.get(
        "v2/{parent}/functions",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFunctionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = cloudfunctions.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = cloudfunctions.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
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

    return Import(
        importer="cloudfunctions",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
