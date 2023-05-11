from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudfunctions() -> Import:
    cloudfunctions = HTTPRuntime("https://cloudfunctions.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudfunctions_1_ErrorResponse",
        "GoogleCloudFunctionsV2betaStageIn": "_cloudfunctions_2_GoogleCloudFunctionsV2betaStageIn",
        "GoogleCloudFunctionsV2betaStageOut": "_cloudfunctions_3_GoogleCloudFunctionsV2betaStageOut",
        "AuditLogConfigIn": "_cloudfunctions_4_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudfunctions_5_AuditLogConfigOut",
        "BindingIn": "_cloudfunctions_6_BindingIn",
        "BindingOut": "_cloudfunctions_7_BindingOut",
        "EventFilterIn": "_cloudfunctions_8_EventFilterIn",
        "EventFilterOut": "_cloudfunctions_9_EventFilterOut",
        "ExprIn": "_cloudfunctions_10_ExprIn",
        "ExprOut": "_cloudfunctions_11_ExprOut",
        "ListFunctionsResponseIn": "_cloudfunctions_12_ListFunctionsResponseIn",
        "ListFunctionsResponseOut": "_cloudfunctions_13_ListFunctionsResponseOut",
        "StorageSourceIn": "_cloudfunctions_14_StorageSourceIn",
        "StorageSourceOut": "_cloudfunctions_15_StorageSourceOut",
        "GoogleCloudFunctionsV2alphaOperationMetadataIn": "_cloudfunctions_16_GoogleCloudFunctionsV2alphaOperationMetadataIn",
        "GoogleCloudFunctionsV2alphaOperationMetadataOut": "_cloudfunctions_17_GoogleCloudFunctionsV2alphaOperationMetadataOut",
        "StatusIn": "_cloudfunctions_18_StatusIn",
        "StatusOut": "_cloudfunctions_19_StatusOut",
        "GenerateDownloadUrlResponseIn": "_cloudfunctions_20_GenerateDownloadUrlResponseIn",
        "GenerateDownloadUrlResponseOut": "_cloudfunctions_21_GenerateDownloadUrlResponseOut",
        "BuildConfigIn": "_cloudfunctions_22_BuildConfigIn",
        "BuildConfigOut": "_cloudfunctions_23_BuildConfigOut",
        "SourceIn": "_cloudfunctions_24_SourceIn",
        "SourceOut": "_cloudfunctions_25_SourceOut",
        "OperationMetadataV1In": "_cloudfunctions_26_OperationMetadataV1In",
        "OperationMetadataV1Out": "_cloudfunctions_27_OperationMetadataV1Out",
        "ListRuntimesResponseIn": "_cloudfunctions_28_ListRuntimesResponseIn",
        "ListRuntimesResponseOut": "_cloudfunctions_29_ListRuntimesResponseOut",
        "RuntimeIn": "_cloudfunctions_30_RuntimeIn",
        "RuntimeOut": "_cloudfunctions_31_RuntimeOut",
        "GoogleCloudFunctionsV2betaOperationMetadataIn": "_cloudfunctions_32_GoogleCloudFunctionsV2betaOperationMetadataIn",
        "GoogleCloudFunctionsV2betaOperationMetadataOut": "_cloudfunctions_33_GoogleCloudFunctionsV2betaOperationMetadataOut",
        "GoogleCloudFunctionsV2StageIn": "_cloudfunctions_34_GoogleCloudFunctionsV2StageIn",
        "GoogleCloudFunctionsV2StageOut": "_cloudfunctions_35_GoogleCloudFunctionsV2StageOut",
        "GoogleCloudFunctionsV2StateMessageIn": "_cloudfunctions_36_GoogleCloudFunctionsV2StateMessageIn",
        "GoogleCloudFunctionsV2StateMessageOut": "_cloudfunctions_37_GoogleCloudFunctionsV2StateMessageOut",
        "GenerateUploadUrlRequestIn": "_cloudfunctions_38_GenerateUploadUrlRequestIn",
        "GenerateUploadUrlRequestOut": "_cloudfunctions_39_GenerateUploadUrlRequestOut",
        "SetIamPolicyRequestIn": "_cloudfunctions_40_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudfunctions_41_SetIamPolicyRequestOut",
        "AuditConfigIn": "_cloudfunctions_42_AuditConfigIn",
        "AuditConfigOut": "_cloudfunctions_43_AuditConfigOut",
        "GoogleCloudFunctionsV2OperationMetadataIn": "_cloudfunctions_44_GoogleCloudFunctionsV2OperationMetadataIn",
        "GoogleCloudFunctionsV2OperationMetadataOut": "_cloudfunctions_45_GoogleCloudFunctionsV2OperationMetadataOut",
        "SecretEnvVarIn": "_cloudfunctions_46_SecretEnvVarIn",
        "SecretEnvVarOut": "_cloudfunctions_47_SecretEnvVarOut",
        "SecretVolumeIn": "_cloudfunctions_48_SecretVolumeIn",
        "SecretVolumeOut": "_cloudfunctions_49_SecretVolumeOut",
        "TestIamPermissionsRequestIn": "_cloudfunctions_50_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudfunctions_51_TestIamPermissionsRequestOut",
        "GoogleCloudFunctionsV2alphaStageIn": "_cloudfunctions_52_GoogleCloudFunctionsV2alphaStageIn",
        "GoogleCloudFunctionsV2alphaStageOut": "_cloudfunctions_53_GoogleCloudFunctionsV2alphaStageOut",
        "GenerateUploadUrlResponseIn": "_cloudfunctions_54_GenerateUploadUrlResponseIn",
        "GenerateUploadUrlResponseOut": "_cloudfunctions_55_GenerateUploadUrlResponseOut",
        "RepoSourceIn": "_cloudfunctions_56_RepoSourceIn",
        "RepoSourceOut": "_cloudfunctions_57_RepoSourceOut",
        "GoogleCloudFunctionsV2betaStateMessageIn": "_cloudfunctions_58_GoogleCloudFunctionsV2betaStateMessageIn",
        "GoogleCloudFunctionsV2betaStateMessageOut": "_cloudfunctions_59_GoogleCloudFunctionsV2betaStateMessageOut",
        "ServiceConfigIn": "_cloudfunctions_60_ServiceConfigIn",
        "ServiceConfigOut": "_cloudfunctions_61_ServiceConfigOut",
        "ListOperationsResponseIn": "_cloudfunctions_62_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_cloudfunctions_63_ListOperationsResponseOut",
        "SecretVersionIn": "_cloudfunctions_64_SecretVersionIn",
        "SecretVersionOut": "_cloudfunctions_65_SecretVersionOut",
        "GenerateDownloadUrlRequestIn": "_cloudfunctions_66_GenerateDownloadUrlRequestIn",
        "GenerateDownloadUrlRequestOut": "_cloudfunctions_67_GenerateDownloadUrlRequestOut",
        "TestIamPermissionsResponseIn": "_cloudfunctions_68_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudfunctions_69_TestIamPermissionsResponseOut",
        "OperationIn": "_cloudfunctions_70_OperationIn",
        "OperationOut": "_cloudfunctions_71_OperationOut",
        "EventTriggerIn": "_cloudfunctions_72_EventTriggerIn",
        "EventTriggerOut": "_cloudfunctions_73_EventTriggerOut",
        "PolicyIn": "_cloudfunctions_74_PolicyIn",
        "PolicyOut": "_cloudfunctions_75_PolicyOut",
        "GoogleCloudFunctionsV2alphaStateMessageIn": "_cloudfunctions_76_GoogleCloudFunctionsV2alphaStateMessageIn",
        "GoogleCloudFunctionsV2alphaStateMessageOut": "_cloudfunctions_77_GoogleCloudFunctionsV2alphaStateMessageOut",
        "SourceProvenanceIn": "_cloudfunctions_78_SourceProvenanceIn",
        "SourceProvenanceOut": "_cloudfunctions_79_SourceProvenanceOut",
        "FunctionIn": "_cloudfunctions_80_FunctionIn",
        "FunctionOut": "_cloudfunctions_81_FunctionOut",
        "LocationIn": "_cloudfunctions_82_LocationIn",
        "LocationOut": "_cloudfunctions_83_LocationOut",
        "ListLocationsResponseIn": "_cloudfunctions_84_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_cloudfunctions_85_ListLocationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudFunctionsV2betaStageIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "message": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStateMessageIn"])
            ).optional(),
            "state": t.string().optional(),
            "resourceUri": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStageIn"])
    types["GoogleCloudFunctionsV2betaStageOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "message": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStateMessageOut"])
            ).optional(),
            "state": t.string().optional(),
            "resourceUri": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStageOut"])
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
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ListFunctionsResponseIn"] = t.struct(
        {
            "functions": t.array(t.proxy(renames["FunctionIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFunctionsResponseIn"])
    types["ListFunctionsResponseOut"] = t.struct(
        {
            "functions": t.array(t.proxy(renames["FunctionOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
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
    types["GoogleCloudFunctionsV2alphaOperationMetadataIn"] = t.struct(
        {
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStageIn"])
            ).optional(),
            "statusDetail": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaOperationMetadataIn"])
    types["GoogleCloudFunctionsV2alphaOperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStageOut"])
            ).optional(),
            "statusDetail": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "endTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaOperationMetadataOut"])
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
    types["GenerateDownloadUrlResponseIn"] = t.struct(
        {"downloadUrl": t.string().optional()}
    ).named(renames["GenerateDownloadUrlResponseIn"])
    types["GenerateDownloadUrlResponseOut"] = t.struct(
        {
            "downloadUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateDownloadUrlResponseOut"])
    types["BuildConfigIn"] = t.struct(
        {
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "source": t.proxy(renames["SourceIn"]).optional(),
            "runtime": t.string().optional(),
            "dockerRegistry": t.string().optional(),
            "dockerRepository": t.string().optional(),
            "workerPool": t.string().optional(),
        }
    ).named(renames["BuildConfigIn"])
    types["BuildConfigOut"] = t.struct(
        {
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "entryPoint": t.string().optional(),
            "source": t.proxy(renames["SourceOut"]).optional(),
            "sourceProvenance": t.proxy(renames["SourceProvenanceOut"]).optional(),
            "build": t.string().optional(),
            "runtime": t.string().optional(),
            "dockerRegistry": t.string().optional(),
            "dockerRepository": t.string().optional(),
            "workerPool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildConfigOut"])
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
    types["OperationMetadataV1In"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "buildId": t.string().optional(),
            "versionId": t.string().optional(),
            "sourceToken": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "target": t.string().optional(),
            "buildName": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["OperationMetadataV1In"])
    types["OperationMetadataV1Out"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "buildId": t.string().optional(),
            "versionId": t.string().optional(),
            "sourceToken": t.string().optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "target": t.string().optional(),
            "buildName": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Out"])
    types["ListRuntimesResponseIn"] = t.struct(
        {"runtimes": t.array(t.proxy(renames["RuntimeIn"])).optional()}
    ).named(renames["ListRuntimesResponseIn"])
    types["ListRuntimesResponseOut"] = t.struct(
        {
            "runtimes": t.array(t.proxy(renames["RuntimeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRuntimesResponseOut"])
    types["RuntimeIn"] = t.struct(
        {
            "warnings": t.array(t.string()).optional(),
            "stage": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "environment": t.string().optional(),
        }
    ).named(renames["RuntimeIn"])
    types["RuntimeOut"] = t.struct(
        {
            "warnings": t.array(t.string()).optional(),
            "stage": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeOut"])
    types["GoogleCloudFunctionsV2betaOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStageIn"])
            ).optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaOperationMetadataIn"])
    types["GoogleCloudFunctionsV2betaOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2betaStageOut"])
            ).optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaOperationMetadataOut"])
    types["GoogleCloudFunctionsV2StageIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "name": t.string().optional(),
            "resourceUri": t.string().optional(),
            "message": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageIn"])
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StageIn"])
    types["GoogleCloudFunctionsV2StageOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "name": t.string().optional(),
            "resourceUri": t.string().optional(),
            "message": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageOut"])
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2StageOut"])
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
    types["GenerateUploadUrlRequestIn"] = t.struct(
        {"kmsKeyName": t.string().optional()}
    ).named(renames["GenerateUploadUrlRequestIn"])
    types["GenerateUploadUrlRequestOut"] = t.struct(
        {
            "kmsKeyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateUploadUrlRequestOut"])
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
    types["GoogleCloudFunctionsV2OperationMetadataIn"] = t.struct(
        {
            "verb": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StageIn"])
            ).optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2OperationMetadataIn"])
    types["GoogleCloudFunctionsV2OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "stages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StageOut"])
            ).optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "cancelRequested": t.boolean().optional(),
            "requestResource": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2OperationMetadataOut"])
    types["SecretEnvVarIn"] = t.struct(
        {
            "version": t.string().optional(),
            "secret": t.string().optional(),
            "key": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["SecretEnvVarIn"])
    types["SecretEnvVarOut"] = t.struct(
        {
            "version": t.string().optional(),
            "secret": t.string().optional(),
            "key": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretEnvVarOut"])
    types["SecretVolumeIn"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["SecretVersionIn"])).optional(),
            "mountPath": t.string().optional(),
            "projectId": t.string().optional(),
            "secret": t.string().optional(),
        }
    ).named(renames["SecretVolumeIn"])
    types["SecretVolumeOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["SecretVersionOut"])).optional(),
            "mountPath": t.string().optional(),
            "projectId": t.string().optional(),
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVolumeOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GoogleCloudFunctionsV2alphaStageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "message": t.string().optional(),
            "state": t.string().optional(),
            "resourceUri": t.string().optional(),
            "resource": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStateMessageIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStageIn"])
    types["GoogleCloudFunctionsV2alphaStageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "message": t.string().optional(),
            "state": t.string().optional(),
            "resourceUri": t.string().optional(),
            "resource": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2alphaStateMessageOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStageOut"])
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
    types["RepoSourceIn"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "branchName": t.string().optional(),
            "commitSha": t.string().optional(),
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "tagName": t.string().optional(),
            "dir": t.string().optional(),
        }
    ).named(renames["RepoSourceIn"])
    types["RepoSourceOut"] = t.struct(
        {
            "invertRegex": t.boolean().optional(),
            "branchName": t.string().optional(),
            "commitSha": t.string().optional(),
            "projectId": t.string().optional(),
            "repoName": t.string().optional(),
            "tagName": t.string().optional(),
            "dir": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RepoSourceOut"])
    types["GoogleCloudFunctionsV2betaStateMessageIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStateMessageIn"])
    types["GoogleCloudFunctionsV2betaStateMessageOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2betaStateMessageOut"])
    types["ServiceConfigIn"] = t.struct(
        {
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "secretVolumes": t.array(t.proxy(renames["SecretVolumeIn"])).optional(),
            "availableMemory": t.string().optional(),
            "ingressSettings": t.string().optional(),
            "secretEnvironmentVariables": t.array(
                t.proxy(renames["SecretEnvVarIn"])
            ).optional(),
            "vpcConnector": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "securityLevel": t.string().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "timeoutSeconds": t.integer().optional(),
            "vpcConnectorEgressSettings": t.string().optional(),
            "maxInstanceCount": t.integer().optional(),
            "minInstanceCount": t.integer().optional(),
            "allTrafficOnLatestRevision": t.boolean().optional(),
            "availableCpu": t.string().optional(),
        }
    ).named(renames["ServiceConfigIn"])
    types["ServiceConfigOut"] = t.struct(
        {
            "maxInstanceRequestConcurrency": t.integer().optional(),
            "secretVolumes": t.array(t.proxy(renames["SecretVolumeOut"])).optional(),
            "availableMemory": t.string().optional(),
            "revision": t.string().optional(),
            "ingressSettings": t.string().optional(),
            "secretEnvironmentVariables": t.array(
                t.proxy(renames["SecretEnvVarOut"])
            ).optional(),
            "vpcConnector": t.string().optional(),
            "uri": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "service": t.string().optional(),
            "securityLevel": t.string().optional(),
            "environmentVariables": t.struct({"_": t.string().optional()}).optional(),
            "timeoutSeconds": t.integer().optional(),
            "vpcConnectorEgressSettings": t.string().optional(),
            "maxInstanceCount": t.integer().optional(),
            "minInstanceCount": t.integer().optional(),
            "allTrafficOnLatestRevision": t.boolean().optional(),
            "availableCpu": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceConfigOut"])
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
    types["SecretVersionIn"] = t.struct(
        {"version": t.string().optional(), "path": t.string().optional()}
    ).named(renames["SecretVersionIn"])
    types["SecretVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecretVersionOut"])
    types["GenerateDownloadUrlRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GenerateDownloadUrlRequestIn"])
    types["GenerateDownloadUrlRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GenerateDownloadUrlRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["EventTriggerIn"] = t.struct(
        {
            "retryPolicy": t.string().optional(),
            "channel": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "eventType": t.string(),
            "triggerRegion": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterIn"])).optional(),
            "serviceAccountEmail": t.string().optional(),
        }
    ).named(renames["EventTriggerIn"])
    types["EventTriggerOut"] = t.struct(
        {
            "retryPolicy": t.string().optional(),
            "channel": t.string().optional(),
            "pubsubTopic": t.string().optional(),
            "eventType": t.string(),
            "triggerRegion": t.string().optional(),
            "eventFilters": t.array(t.proxy(renames["EventFilterOut"])).optional(),
            "trigger": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EventTriggerOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["GoogleCloudFunctionsV2alphaStateMessageIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStateMessageIn"])
    types["GoogleCloudFunctionsV2alphaStateMessageOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudFunctionsV2alphaStateMessageOut"])
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
    types["FunctionIn"] = t.struct(
        {
            "environment": t.string().optional(),
            "buildConfig": t.proxy(renames["BuildConfigIn"]).optional(),
            "kmsKeyName": t.string().optional(),
            "eventTrigger": t.proxy(renames["EventTriggerIn"]).optional(),
            "serviceConfig": t.proxy(renames["ServiceConfigIn"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["FunctionIn"])
    types["FunctionOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "stateMessages": t.array(
                t.proxy(renames["GoogleCloudFunctionsV2StateMessageOut"])
            ).optional(),
            "buildConfig": t.proxy(renames["BuildConfigOut"]).optional(),
            "kmsKeyName": t.string().optional(),
            "eventTrigger": t.proxy(renames["EventTriggerOut"]).optional(),
            "serviceConfig": t.proxy(renames["ServiceConfigOut"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FunctionOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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

    functions = {}
    functions["projectsLocationsList"] = cloudfunctions.get(
        "v2/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsFunctionsDelete"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsFunctionsPatch"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsFunctionsGenerateDownloadUrl"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsFunctionsCreate"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsFunctionsGet"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsFunctionsList"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsFunctionsGenerateUploadUrl"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsFunctionsSetIamPolicy"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsFunctionsGetIamPolicy"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsFunctionsTestIamPermissions"] = cloudfunctions.post(
        "v2/{resource}:testIamPermissions",
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
    functions["projectsLocationsOperationsGet"] = cloudfunctions.get(
        "v2/{name}/operations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string(),
                "name": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string(),
                "name": t.string().optional(),
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

    return Import(
        importer="cloudfunctions", renames=renames, types=types, functions=functions
    )
