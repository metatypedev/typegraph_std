from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudfunctions():
    cloudfunctions = HTTPRuntime("https://cloudfunctions.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudfunctions_1_ErrorResponse",
        "ExprIn": "_cloudfunctions_2_ExprIn",
        "ExprOut": "_cloudfunctions_3_ExprOut",
        "StatusIn": "_cloudfunctions_4_StatusIn",
        "StatusOut": "_cloudfunctions_5_StatusOut",
        "AuditLogConfigIn": "_cloudfunctions_6_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudfunctions_7_AuditLogConfigOut",
        "EventTriggerIn": "_cloudfunctions_8_EventTriggerIn",
        "EventTriggerOut": "_cloudfunctions_9_EventTriggerOut",
        "SecretEnvVarIn": "_cloudfunctions_10_SecretEnvVarIn",
        "SecretEnvVarOut": "_cloudfunctions_11_SecretEnvVarOut",
        "StorageSourceIn": "_cloudfunctions_12_StorageSourceIn",
        "StorageSourceOut": "_cloudfunctions_13_StorageSourceOut",
        "ServiceConfigIn": "_cloudfunctions_14_ServiceConfigIn",
        "ServiceConfigOut": "_cloudfunctions_15_ServiceConfigOut",
        "GoogleCloudFunctionsV2alphaOperationMetadataIn": "_cloudfunctions_16_GoogleCloudFunctionsV2alphaOperationMetadataIn",
        "GoogleCloudFunctionsV2alphaOperationMetadataOut": "_cloudfunctions_17_GoogleCloudFunctionsV2alphaOperationMetadataOut",
        "BindingIn": "_cloudfunctions_18_BindingIn",
        "BindingOut": "_cloudfunctions_19_BindingOut",
        "PolicyIn": "_cloudfunctions_20_PolicyIn",
        "PolicyOut": "_cloudfunctions_21_PolicyOut",
        "TestIamPermissionsRequestIn": "_cloudfunctions_22_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudfunctions_23_TestIamPermissionsRequestOut",
        "ListFunctionsResponseIn": "_cloudfunctions_24_ListFunctionsResponseIn",
        "ListFunctionsResponseOut": "_cloudfunctions_25_ListFunctionsResponseOut",
        "GoogleCloudFunctionsV2alphaLocationMetadataIn": "_cloudfunctions_26_GoogleCloudFunctionsV2alphaLocationMetadataIn",
        "GoogleCloudFunctionsV2alphaLocationMetadataOut": "_cloudfunctions_27_GoogleCloudFunctionsV2alphaLocationMetadataOut",
        "GoogleCloudFunctionsV2betaStageIn": "_cloudfunctions_28_GoogleCloudFunctionsV2betaStageIn",
        "GoogleCloudFunctionsV2betaStageOut": "_cloudfunctions_29_GoogleCloudFunctionsV2betaStageOut",
        "ListLocationsResponseIn": "_cloudfunctions_30_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudfunctions_31_ListLocationsResponseOut",
        "SourceIn": "_cloudfunctions_32_SourceIn",
        "SourceOut": "_cloudfunctions_33_SourceOut",
        "SecretVersionIn": "_cloudfunctions_34_SecretVersionIn",
        "SecretVersionOut": "_cloudfunctions_35_SecretVersionOut",
        "GoogleCloudFunctionsV2alphaStateMessageIn": "_cloudfunctions_36_GoogleCloudFunctionsV2alphaStateMessageIn",
        "GoogleCloudFunctionsV2alphaStateMessageOut": "_cloudfunctions_37_GoogleCloudFunctionsV2alphaStateMessageOut",
        "GenerateDownloadUrlRequestIn": "_cloudfunctions_38_GenerateDownloadUrlRequestIn",
        "GenerateDownloadUrlRequestOut": "_cloudfunctions_39_GenerateDownloadUrlRequestOut",
        "SourceProvenanceIn": "_cloudfunctions_40_SourceProvenanceIn",
        "SourceProvenanceOut": "_cloudfunctions_41_SourceProvenanceOut",
        "GoogleCloudFunctionsV2betaLocationMetadataIn": "_cloudfunctions_42_GoogleCloudFunctionsV2betaLocationMetadataIn",
        "GoogleCloudFunctionsV2betaLocationMetadataOut": "_cloudfunctions_43_GoogleCloudFunctionsV2betaLocationMetadataOut",
        "ListRuntimesResponseIn": "_cloudfunctions_44_ListRuntimesResponseIn",
        "ListRuntimesResponseOut": "_cloudfunctions_45_ListRuntimesResponseOut",
        "SecretVolumeIn": "_cloudfunctions_46_SecretVolumeIn",
        "SecretVolumeOut": "_cloudfunctions_47_SecretVolumeOut",
        "TestIamPermissionsResponseIn": "_cloudfunctions_48_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudfunctions_49_TestIamPermissionsResponseOut",
        "OperationMetadataV1In": "_cloudfunctions_50_OperationMetadataV1In",
        "OperationMetadataV1Out": "_cloudfunctions_51_OperationMetadataV1Out",
        "GoogleCloudFunctionsV2betaOperationMetadataIn": "_cloudfunctions_52_GoogleCloudFunctionsV2betaOperationMetadataIn",
        "GoogleCloudFunctionsV2betaOperationMetadataOut": "_cloudfunctions_53_GoogleCloudFunctionsV2betaOperationMetadataOut",
        "OperationIn": "_cloudfunctions_54_OperationIn",
        "OperationOut": "_cloudfunctions_55_OperationOut",
        "RuntimeIn": "_cloudfunctions_56_RuntimeIn",
        "RuntimeOut": "_cloudfunctions_57_RuntimeOut",
        "LocationIn": "_cloudfunctions_58_LocationIn",
        "LocationOut": "_cloudfunctions_59_LocationOut",
        "RepoSourceIn": "_cloudfunctions_60_RepoSourceIn",
        "RepoSourceOut": "_cloudfunctions_61_RepoSourceOut",
        "GenerateUploadUrlRequestIn": "_cloudfunctions_62_GenerateUploadUrlRequestIn",
        "GenerateUploadUrlRequestOut": "_cloudfunctions_63_GenerateUploadUrlRequestOut",
        "AuditConfigIn": "_cloudfunctions_64_AuditConfigIn",
        "AuditConfigOut": "_cloudfunctions_65_AuditConfigOut",
        "ListOperationsResponseIn": "_cloudfunctions_66_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudfunctions_67_ListOperationsResponseOut",
        "GoogleCloudFunctionsV2alphaStageIn": "_cloudfunctions_68_GoogleCloudFunctionsV2alphaStageIn",
        "GoogleCloudFunctionsV2alphaStageOut": "_cloudfunctions_69_GoogleCloudFunctionsV2alphaStageOut",
        "GoogleCloudFunctionsV2betaStateMessageIn": "_cloudfunctions_70_GoogleCloudFunctionsV2betaStateMessageIn",
        "GoogleCloudFunctionsV2betaStateMessageOut": "_cloudfunctions_71_GoogleCloudFunctionsV2betaStateMessageOut",
        "GoogleCloudFunctionsV2StageIn": "_cloudfunctions_72_GoogleCloudFunctionsV2StageIn",
        "GoogleCloudFunctionsV2StageOut": "_cloudfunctions_73_GoogleCloudFunctionsV2StageOut",
        "EventFilterIn": "_cloudfunctions_74_EventFilterIn",
        "EventFilterOut": "_cloudfunctions_75_EventFilterOut",
        "SetIamPolicyRequestIn": "_cloudfunctions_76_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudfunctions_77_SetIamPolicyRequestOut",
        "BuildConfigIn": "_cloudfunctions_78_BuildConfigIn",
        "BuildConfigOut": "_cloudfunctions_79_BuildConfigOut",
        "GoogleCloudFunctionsV2LocationMetadataIn": "_cloudfunctions_80_GoogleCloudFunctionsV2LocationMetadataIn",
        "GoogleCloudFunctionsV2LocationMetadataOut": "_cloudfunctions_81_GoogleCloudFunctionsV2LocationMetadataOut",
        "FunctionIn": "_cloudfunctions_82_FunctionIn",
        "FunctionOut": "_cloudfunctions_83_FunctionOut",
        "GenerateDownloadUrlResponseIn": "_cloudfunctions_84_GenerateDownloadUrlResponseIn",
        "GenerateDownloadUrlResponseOut": "_cloudfunctions_85_GenerateDownloadUrlResponseOut",
        "GoogleCloudFunctionsV2OperationMetadataIn": "_cloudfunctions_86_GoogleCloudFunctionsV2OperationMetadataIn",
        "GoogleCloudFunctionsV2OperationMetadataOut": "_cloudfunctions_87_GoogleCloudFunctionsV2OperationMetadataOut",
        "GoogleCloudFunctionsV2StateMessageIn": "_cloudfunctions_88_GoogleCloudFunctionsV2StateMessageIn",
        "GoogleCloudFunctionsV2StateMessageOut": "_cloudfunctions_89_GoogleCloudFunctionsV2StateMessageOut",
        "GenerateUploadUrlResponseIn": "_cloudfunctions_90_GenerateUploadUrlResponseIn",
        "GenerateUploadUrlResponseOut": "_cloudfunctions_91_GenerateUploadUrlResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["EventTriggerIn"] = t.struct(
        {
            "eventType": t.string(),
            "retryPolicy": t.string().optional(),
            "triggerRegion": t.string().optional(),
            "channel": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional(),
            "pubsubTopic": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
        }
    ).named(renames["EventTriggerIn"])
    types["EventTriggerOut"] = t.struct(
        {
            "eventType": t.string(),
            "retryPolicy": t.string().optional(),
            "triggerRegion": t.string().optional(),
            "channel": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "trigger": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTriggerOut"])
    types["SecretEnvVarIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "key": t.string().optional(),
            "secret": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["SecretEnvVarIn"])
    types["SecretEnvVarOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "key": t.string().optional(),
            "secret": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretEnvVarOut"])
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
    types["ServiceConfigIn"] = t.struct(
        {
            "availableMemory": t.string().optional(),
            "vpcConnector": t.string().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "timeoutSeconds": t.integer().optional(),
            "secretVolumes": t.array(t.proxy(renames["SecretVolumeIn"])).optional(),
            "secretEnvironmentVariables": t.array(
                t.proxy(renames["SecretEnvVarIn"])
            ).optional(),
            "vpcConnectorEgressSettings": t.string().optional(),
            "allTrafficOnLatestRevision": t.boolean().optional(),
            "ingressSettings": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "securityLevel": t.string().optional(),
            "availableCpu": t.string().optional(),
            "minInstanceCount": t.integer().optional(),
            "maxInstanceCount": t.integer().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ServiceConfigIn"])
    types["ServiceConfigOut"] = t.struct(
        {
            "availableMemory": t.string().optional(),
            "vpcConnector": t.string().optional(),
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "timeoutSeconds": t.integer().optional(),
            "secretVolumes": t.array(t.proxy(renames["SecretVolumeOut"])).optional(),
            "secretEnvironmentVariables": t.array(
                t.proxy(renames["SecretEnvVarOut"])
            ).optional(),
            "vpcConnectorEgressSettings": t.string().optional(),
            "allTrafficOnLatestRevision": t.boolean().optional(),
            "ingressSettings": t.string().optional(),
            "revision": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "securityLevel": t.string().optional(),
            "service": t.string().optional(),
            "availableCpu": t.string().optional(),
            "minInstanceCount": t.integer().optional(),
            "maxInstanceCount": t.integer().optional(),
            "uri": t.string().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConfigOut"])
    types["GoogleCloudFunctionsV2alphaOperationMetadataIn"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStageIn"])
            ).optional(),
            "apiVersion": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaOperationMetadataIn"])
    types["GoogleCloudFunctionsV2alphaOperationMetadataOut"] = t.struct(
        {
            "cancelRequested": t.boolean().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStageOut"])
            ).optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaOperationMetadataOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["ListFunctionsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "functions": t.array(t.proxy(renames["FunctionIn"])).optional(),
        }
    ).named(renames["ListFunctionsResponseIn"])
    types["ListFunctionsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "functions": t.array(t.proxy(renames["FunctionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFunctionsResponseOut"])
    types["GoogleCloudFunctionsV2alphaLocationMetadataIn"] = t.struct(
        {"environments": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudFunctionsV2alphaLocationMetadataIn"])
    types["GoogleCloudFunctionsV2alphaLocationMetadataOut"] = t.struct(
        {
            "environments": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaLocationMetadataOut"])
    types["GoogleCloudFunctionsV2betaStageIn"] = t.struct(
        {
            "state": t.string().optional(),
            "resourceUri": t.string().optional(),
            "name": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStateMessageIn"])
            ).optional(),
            "message": t.string().optional(),
            "resource": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStageIn"])
    types["GoogleCloudFunctionsV2betaStageOut"] = t.struct(
        {
            "state": t.string().optional(),
            "resourceUri": t.string().optional(),
            "name": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStateMessageOut"])
            ).optional(),
            "message": t.string().optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStageOut"])
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
    types["SourceIn"] = t.struct(
        {
            "gitUri": t.string().optional(),
            "repoSource": t.proxy(renames["RepoSourceIn"]).optional(),
            "storageSource": t.proxy(renames["StorageSourceIn"]).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "gitUri": t.string().optional(),
            "repoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "storageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
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
    types["GoogleCloudFunctionsV2alphaStateMessageIn"] = t.struct(
        {
            "type": t.string().optional(),
            "severity": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStateMessageIn"])
    types["GoogleCloudFunctionsV2alphaStateMessageOut"] = t.struct(
        {
            "type": t.string().optional(),
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStateMessageOut"])
    types["GenerateDownloadUrlRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateDownloadUrlRequestIn"])
    types["GenerateDownloadUrlRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateDownloadUrlRequestOut"])
    types["SourceProvenanceIn"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(renames["StorageSourceIn"]).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceIn"]).optional(),
            "gitUri": t.string().optional(),
        }
    ).named(renames["SourceProvenanceIn"])
    types["SourceProvenanceOut"] = t.struct(
        {
            "resolvedStorageSource": t.proxy(renames["StorageSourceOut"]).optional(),
            "resolvedRepoSource": t.proxy(renames["RepoSourceOut"]).optional(),
            "gitUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceProvenanceOut"])
    types["GoogleCloudFunctionsV2betaLocationMetadataIn"] = t.struct(
        {"environments": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudFunctionsV2betaLocationMetadataIn"])
    types["GoogleCloudFunctionsV2betaLocationMetadataOut"] = t.struct(
        {
            "environments": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaLocationMetadataOut"])
    types["ListRuntimesResponseIn"] = t.struct(
        {"runtimes": t.array(t.proxy(renames["RuntimeIn"])).optional()}
    ).named(renames["ListRuntimesResponseIn"])
    types["ListRuntimesResponseOut"] = t.struct(
        {
            "runtimes": t.array(t.proxy(renames["RuntimeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRuntimesResponseOut"])
    types["SecretVolumeIn"] = t.struct(
        {
            "mountPath": t.string().optional(),
            "projectId": t.string().optional(),
            "versions": t.array(t.proxy(renames["SecretVersionIn"])).optional(),
            "secret": t.string().optional(),
        }
    ).named(renames["SecretVolumeIn"])
    types["SecretVolumeOut"] = t.struct(
        {
            "mountPath": t.string().optional(),
            "projectId": t.string().optional(),
            "versions": t.array(t.proxy(renames["SecretVersionOut"])).optional(),
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVolumeOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["OperationMetadataV1In"] = t.struct(
        {
            "sourceToken": t.string().optional(),
            "versionId": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "buildName": t.string().optional(),
            "buildId": t.string().optional(),
            "target": t.string().optional(),
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["OperationMetadataV1In"])
    types["OperationMetadataV1Out"] = t.struct(
        {
            "sourceToken": t.string().optional(),
            "versionId": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "buildName": t.string().optional(),
            "buildId": t.string().optional(),
            "target": t.string().optional(),
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Out"])
    types["GoogleCloudFunctionsV2betaOperationMetadataIn"] = t.struct(
        {
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStageIn"])
            ).optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaOperationMetadataIn"])
    types["GoogleCloudFunctionsV2betaOperationMetadataOut"] = t.struct(
        {
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStageOut"])
            ).optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaOperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["RuntimeIn"] = t.struct(
        {
            "warnings": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "stage": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RuntimeIn"])
    types["RuntimeOut"] = t.struct(
        {
            "warnings": t.array(t.string()).optional(),
            "environment": t.string().optional(),
            "stage": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["RepoSourceIn"] = t.struct(
        {
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
            "tagName": t.string().optional(),
            "repoName": t.string().optional(),
            "dir": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["RepoSourceIn"])
    types["RepoSourceOut"] = t.struct(
        {
            "commitSha": t.string().optional(),
            "branchName": t.string().optional(),
            "tagName": t.string().optional(),
            "repoName": t.string().optional(),
            "dir": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoSourceOut"])
    types["GenerateUploadUrlRequestIn"] = t.struct(
        {"kmsKeyName": t.string().optional()}
    ).named(renames["GenerateUploadUrlRequestIn"])
    types["GenerateUploadUrlRequestOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateUploadUrlRequestOut"])
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
    types["GoogleCloudFunctionsV2alphaStageIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "message": t.string().optional(),
            "resourceUri": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStateMessageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStageIn"])
    types["GoogleCloudFunctionsV2alphaStageOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "message": t.string().optional(),
            "resourceUri": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStateMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStageOut"])
    types["GoogleCloudFunctionsV2betaStateMessageIn"] = t.struct(
        {
            "type": t.string().optional(),
            "message": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStateMessageIn"])
    types["GoogleCloudFunctionsV2betaStateMessageOut"] = t.struct(
        {
            "type": t.string().optional(),
            "message": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStateMessageOut"])
    types["GoogleCloudFunctionsV2StageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
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
            "name": t.string().optional(),
            "state": t.string().optional(),
            "message": t.string().optional(),
            "resourceUri": t.string().optional(),
            "resource": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StageOut"])
    types["EventFilterIn"] = t.struct(
        {
            "value": t.string(),
            "operator": t.string().optional(),
            "attribute": t.string(),
        }
    ).named(renames["EventFilterIn"])
    types["EventFilterOut"] = t.struct(
        {
            "value": t.string(),
            "operator": t.string().optional(),
            "attribute": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventFilterOut"])
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
    types["BuildConfigIn"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "runtime": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "dockerRegistry": t.string().optional(),
            "workerPool": t.string().optional(),
            "dockerRepository": t.string().optional(),
        }
    ).named(renames["BuildConfigIn"])
    types["BuildConfigOut"] = t.struct(
        {
            "entryPoint": t.string().optional(),
            "build": t.string().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "sourceProvenance": t.proxy(renames["SourceProvenanceOut"]).optional(),
            "runtime": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "dockerRegistry": t.string().optional(),
            "workerPool": t.string().optional(),
            "dockerRepository": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildConfigOut"])
    types["GoogleCloudFunctionsV2LocationMetadataIn"] = t.struct(
        {"environments": t.array(t.string()).optional()}
    ).named(renames["GoogleCloudFunctionsV2LocationMetadataIn"])
    types["GoogleCloudFunctionsV2LocationMetadataOut"] = t.struct(
        {
            "environments": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2LocationMetadataOut"])
    types["FunctionIn"] = t.struct(
        {
            "environment": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "buildConfig": t.proxy(renames["BuildConfigIn"]).optional(),
            "kmsKeyName": t.string().optional(),
            "eventTrigger": t.proxy(renames["EventTriggerIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "serviceConfig": t.proxy(renames["ServiceConfigIn"]).optional(),
        }
    ).named(renames["FunctionIn"])
    types["FunctionOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "buildConfig": t.proxy(renames["BuildConfigOut"]).optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageOut"])
            ).optional(),
            "kmsKeyName": t.string().optional(),
            "eventTrigger": t.proxy(renames["EventTriggerOut"]).optional(),
            "name": t.string().optional(),
            "url": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "satisfiesPzs": t.boolean().optional(),
            "serviceConfig": t.proxy(renames["ServiceConfigOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionOut"])
    types["GenerateDownloadUrlResponseIn"] = t.struct(
        {"downloadUrl": t.string().optional()}
    ).named(renames["GenerateDownloadUrlResponseIn"])
    types["GenerateDownloadUrlResponseOut"] = t.struct(
        {
            "downloadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateDownloadUrlResponseOut"])
    types["GoogleCloudFunctionsV2OperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StageIn"])
            ).optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "statusDetail": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2OperationMetadataIn"])
    types["GoogleCloudFunctionsV2OperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StageOut"])
            ).optional(),
            "apiVersion": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2OperationMetadataOut"])
    types["GoogleCloudFunctionsV2StateMessageIn"] = t.struct(
        {
            "type": t.string().optional(),
            "message": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StateMessageIn"])
    types["GoogleCloudFunctionsV2StateMessageOut"] = t.struct(
        {
            "type": t.string().optional(),
            "message": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StateMessageOut"])
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

    functions = {}
    functions["projectsLocationsList"] = cloudfunctions.get(
        "v2/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsFunctionsGet"] = cloudfunctions.post(
        "v2/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
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
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRuntimesList"] = cloudfunctions.get(
        "v2/{parent}/runtimes",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
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
