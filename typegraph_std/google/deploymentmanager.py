from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_deploymentmanager() -> Import:
    deploymentmanager = HTTPRuntime("https://deploymentmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_deploymentmanager_1_ErrorResponse",
        "OperationsListResponseIn": "_deploymentmanager_2_OperationsListResponseIn",
        "OperationsListResponseOut": "_deploymentmanager_3_OperationsListResponseOut",
        "ManifestsListResponseIn": "_deploymentmanager_4_ManifestsListResponseIn",
        "ManifestsListResponseOut": "_deploymentmanager_5_ManifestsListResponseOut",
        "DeploymentUpdateLabelEntryIn": "_deploymentmanager_6_DeploymentUpdateLabelEntryIn",
        "DeploymentUpdateLabelEntryOut": "_deploymentmanager_7_DeploymentUpdateLabelEntryOut",
        "AuditConfigIn": "_deploymentmanager_8_AuditConfigIn",
        "AuditConfigOut": "_deploymentmanager_9_AuditConfigOut",
        "ExprIn": "_deploymentmanager_10_ExprIn",
        "ExprOut": "_deploymentmanager_11_ExprOut",
        "DeploymentIn": "_deploymentmanager_12_DeploymentIn",
        "DeploymentOut": "_deploymentmanager_13_DeploymentOut",
        "DeploymentsCancelPreviewRequestIn": "_deploymentmanager_14_DeploymentsCancelPreviewRequestIn",
        "DeploymentsCancelPreviewRequestOut": "_deploymentmanager_15_DeploymentsCancelPreviewRequestOut",
        "DeploymentsListResponseIn": "_deploymentmanager_16_DeploymentsListResponseIn",
        "DeploymentsListResponseOut": "_deploymentmanager_17_DeploymentsListResponseOut",
        "TypesListResponseIn": "_deploymentmanager_18_TypesListResponseIn",
        "TypesListResponseOut": "_deploymentmanager_19_TypesListResponseOut",
        "ManifestIn": "_deploymentmanager_20_ManifestIn",
        "ManifestOut": "_deploymentmanager_21_ManifestOut",
        "ResourceAccessControlIn": "_deploymentmanager_22_ResourceAccessControlIn",
        "ResourceAccessControlOut": "_deploymentmanager_23_ResourceAccessControlOut",
        "TestPermissionsRequestIn": "_deploymentmanager_24_TestPermissionsRequestIn",
        "TestPermissionsRequestOut": "_deploymentmanager_25_TestPermissionsRequestOut",
        "ConfigFileIn": "_deploymentmanager_26_ConfigFileIn",
        "ConfigFileOut": "_deploymentmanager_27_ConfigFileOut",
        "TargetConfigurationIn": "_deploymentmanager_28_TargetConfigurationIn",
        "TargetConfigurationOut": "_deploymentmanager_29_TargetConfigurationOut",
        "OperationIn": "_deploymentmanager_30_OperationIn",
        "OperationOut": "_deploymentmanager_31_OperationOut",
        "TestPermissionsResponseIn": "_deploymentmanager_32_TestPermissionsResponseIn",
        "TestPermissionsResponseOut": "_deploymentmanager_33_TestPermissionsResponseOut",
        "DeploymentsStopRequestIn": "_deploymentmanager_34_DeploymentsStopRequestIn",
        "DeploymentsStopRequestOut": "_deploymentmanager_35_DeploymentsStopRequestOut",
        "PolicyIn": "_deploymentmanager_36_PolicyIn",
        "PolicyOut": "_deploymentmanager_37_PolicyOut",
        "DeploymentUpdateIn": "_deploymentmanager_38_DeploymentUpdateIn",
        "DeploymentUpdateOut": "_deploymentmanager_39_DeploymentUpdateOut",
        "ResourcesListResponseIn": "_deploymentmanager_40_ResourcesListResponseIn",
        "ResourcesListResponseOut": "_deploymentmanager_41_ResourcesListResponseOut",
        "TypeIn": "_deploymentmanager_42_TypeIn",
        "TypeOut": "_deploymentmanager_43_TypeOut",
        "DeploymentLabelEntryIn": "_deploymentmanager_44_DeploymentLabelEntryIn",
        "DeploymentLabelEntryOut": "_deploymentmanager_45_DeploymentLabelEntryOut",
        "ImportFileIn": "_deploymentmanager_46_ImportFileIn",
        "ImportFileOut": "_deploymentmanager_47_ImportFileOut",
        "ResourceUpdateIn": "_deploymentmanager_48_ResourceUpdateIn",
        "ResourceUpdateOut": "_deploymentmanager_49_ResourceUpdateOut",
        "ResourceIn": "_deploymentmanager_50_ResourceIn",
        "ResourceOut": "_deploymentmanager_51_ResourceOut",
        "GlobalSetPolicyRequestIn": "_deploymentmanager_52_GlobalSetPolicyRequestIn",
        "GlobalSetPolicyRequestOut": "_deploymentmanager_53_GlobalSetPolicyRequestOut",
        "AuditLogConfigIn": "_deploymentmanager_54_AuditLogConfigIn",
        "AuditLogConfigOut": "_deploymentmanager_55_AuditLogConfigOut",
        "BindingIn": "_deploymentmanager_56_BindingIn",
        "BindingOut": "_deploymentmanager_57_BindingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OperationsListResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["OperationsListResponseIn"])
    types["OperationsListResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationsListResponseOut"])
    types["ManifestsListResponseIn"] = t.struct(
        {
            "manifests": t.array(t.proxy(renames["ManifestIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ManifestsListResponseIn"])
    types["ManifestsListResponseOut"] = t.struct(
        {
            "manifests": t.array(t.proxy(renames["ManifestOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManifestsListResponseOut"])
    types["DeploymentUpdateLabelEntryIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["DeploymentUpdateLabelEntryIn"])
    types["DeploymentUpdateLabelEntryOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentUpdateLabelEntryOut"])
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
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["DeploymentIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "insertTime": t.string().optional(),
            "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "id": t.string(),
            "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
            "fingerprint": t.string().optional(),
            "description": t.string().optional(),
            "manifest": t.string().optional(),
            "labels": t.array(t.proxy(renames["DeploymentLabelEntryIn"])).optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "insertTime": t.string().optional(),
            "update": t.proxy(renames["DeploymentUpdateOut"]).optional(),
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "id": t.string(),
            "target": t.proxy(renames["TargetConfigurationOut"]).optional(),
            "fingerprint": t.string().optional(),
            "description": t.string().optional(),
            "manifest": t.string().optional(),
            "labels": t.array(t.proxy(renames["DeploymentLabelEntryOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
    types["DeploymentsCancelPreviewRequestIn"] = t.struct(
        {"fingerprint": t.string().optional()}
    ).named(renames["DeploymentsCancelPreviewRequestIn"])
    types["DeploymentsCancelPreviewRequestOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentsCancelPreviewRequestOut"])
    types["DeploymentsListResponseIn"] = t.struct(
        {
            "deployments": t.array(t.proxy(renames["DeploymentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["DeploymentsListResponseIn"])
    types["DeploymentsListResponseOut"] = t.struct(
        {
            "deployments": t.array(t.proxy(renames["DeploymentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentsListResponseOut"])
    types["TypesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
        }
    ).named(renames["TypesListResponseIn"])
    types["TypesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypesListResponseOut"])
    types["ManifestIn"] = t.struct(
        {
            "manifestSizeLimitBytes": t.string().optional(),
            "manifestSizeBytes": t.string().optional(),
            "insertTime": t.string().optional(),
            "id": t.string(),
            "imports": t.array(t.proxy(renames["ImportFileIn"])).optional(),
            "config": t.proxy(renames["ConfigFileIn"]).optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "expandedConfig": t.string().optional(),
            "layout": t.string().optional(),
        }
    ).named(renames["ManifestIn"])
    types["ManifestOut"] = t.struct(
        {
            "manifestSizeLimitBytes": t.string().optional(),
            "manifestSizeBytes": t.string().optional(),
            "insertTime": t.string().optional(),
            "id": t.string(),
            "imports": t.array(t.proxy(renames["ImportFileOut"])).optional(),
            "config": t.proxy(renames["ConfigFileOut"]).optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "expandedConfig": t.string().optional(),
            "layout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManifestOut"])
    types["ResourceAccessControlIn"] = t.struct(
        {"gcpIamPolicy": t.string().optional()}
    ).named(renames["ResourceAccessControlIn"])
    types["ResourceAccessControlOut"] = t.struct(
        {
            "gcpIamPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceAccessControlOut"])
    types["TestPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestPermissionsRequestIn"])
    types["TestPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestPermissionsRequestOut"])
    types["ConfigFileIn"] = t.struct({"content": t.string().optional()}).named(
        renames["ConfigFileIn"]
    )
    types["ConfigFileOut"] = t.struct(
        {
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigFileOut"])
    types["TargetConfigurationIn"] = t.struct(
        {
            "imports": t.array(t.proxy(renames["ImportFileIn"])).optional(),
            "config": t.proxy(renames["ConfigFileIn"]).optional(),
        }
    ).named(renames["TargetConfigurationIn"])
    types["TargetConfigurationOut"] = t.struct(
        {
            "imports": t.array(t.proxy(renames["ImportFileOut"])).optional(),
            "config": t.proxy(renames["ConfigFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetConfigurationOut"])
    types["OperationIn"] = t.struct(
        {
            "id": t.string().optional(),
            "statusMessage": t.string().optional(),
            "region": t.string().optional(),
            "operationType": t.string().optional(),
            "status": t.string().optional(),
            "startTime": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "data": t.array(
                            t.struct(
                                {
                                    "key": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "message": t.string().optional(),
                        "code": t.string().optional(),
                    }
                )
            ).optional(),
            "progress": t.integer().optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "user": t.string().optional(),
            "insertTime": t.string().optional(),
            "zone": t.string().optional(),
            "operationGroupId": t.string().optional(),
            "error": t.struct(
                {
                    "errors": t.array(
                        t.struct(
                            {
                                "location": t.string().optional(),
                                "code": t.string().optional(),
                                "message": t.string().optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "clientOperationId": t.string().optional(),
            "targetId": t.string().optional(),
            "httpErrorMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "targetLink": t.string().optional(),
            "creationTimestamp": t.string().optional(),
            "httpErrorStatusCode": t.integer().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "id": t.string().optional(),
            "statusMessage": t.string().optional(),
            "region": t.string().optional(),
            "operationType": t.string().optional(),
            "status": t.string().optional(),
            "startTime": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "data": t.array(
                            t.struct(
                                {
                                    "key": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "message": t.string().optional(),
                        "code": t.string().optional(),
                    }
                )
            ).optional(),
            "progress": t.integer().optional(),
            "kind": t.string().optional(),
            "selfLink": t.string().optional(),
            "user": t.string().optional(),
            "insertTime": t.string().optional(),
            "zone": t.string().optional(),
            "operationGroupId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "clientOperationId": t.string().optional(),
            "targetId": t.string().optional(),
            "httpErrorMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "targetLink": t.string().optional(),
            "creationTimestamp": t.string().optional(),
            "httpErrorStatusCode": t.integer().optional(),
        }
    ).named(renames["OperationOut"])
    types["TestPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestPermissionsResponseIn"])
    types["TestPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestPermissionsResponseOut"])
    types["DeploymentsStopRequestIn"] = t.struct(
        {"fingerprint": t.string().optional()}
    ).named(renames["DeploymentsStopRequestIn"])
    types["DeploymentsStopRequestOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentsStopRequestOut"])
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
    types["DeploymentUpdateIn"] = t.struct(
        {
            "manifest": t.string().optional(),
            "labels": t.array(
                t.proxy(renames["DeploymentUpdateLabelEntryIn"])
            ).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["DeploymentUpdateIn"])
    types["DeploymentUpdateOut"] = t.struct(
        {
            "manifest": t.string().optional(),
            "labels": t.array(
                t.proxy(renames["DeploymentUpdateLabelEntryOut"])
            ).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentUpdateOut"])
    types["ResourcesListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["ResourceIn"])).optional(),
        }
    ).named(renames["ResourcesListResponseIn"])
    types["ResourcesListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "resources": t.array(t.proxy(renames["ResourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesListResponseOut"])
    types["TypeIn"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "id": t.string(),
            "name": t.string().optional(),
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "insertTime": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "id": t.string(),
            "name": t.string().optional(),
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "insertTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["DeploymentLabelEntryIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["DeploymentLabelEntryIn"])
    types["DeploymentLabelEntryOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentLabelEntryOut"])
    types["ImportFileIn"] = t.struct(
        {"content": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ImportFileIn"])
    types["ImportFileOut"] = t.struct(
        {
            "content": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportFileOut"])
    types["ResourceUpdateIn"] = t.struct(
        {
            "intent": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "code": t.string().optional(),
                        "message": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "key": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                    }
                )
            ).optional(),
            "finalProperties": t.string().optional(),
            "manifest": t.string().optional(),
            "error": t.struct(
                {
                    "errors": t.array(
                        t.struct(
                            {
                                "message": t.string().optional(),
                                "location": t.string().optional(),
                                "code": t.string().optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "properties": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ResourceUpdateIn"])
    types["ResourceUpdateOut"] = t.struct(
        {
            "intent": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "code": t.string().optional(),
                        "message": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "key": t.string().optional(),
                                    "value": t.string().optional(),
                                }
                            )
                        ).optional(),
                    }
                )
            ).optional(),
            "finalProperties": t.string().optional(),
            "manifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "properties": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlOut"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ResourceUpdateOut"])
    types["ResourceIn"] = t.struct(
        {
            "manifest": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "code": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "value": t.string().optional(),
                                    "key": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "message": t.string().optional(),
                    }
                )
            ).optional(),
            "insertTime": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string(),
            "url": t.string().optional(),
            "update": t.proxy(renames["ResourceUpdateIn"]).optional(),
            "properties": t.string().optional(),
            "finalProperties": t.string().optional(),
            "updateTime": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "manifest": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "code": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "value": t.string().optional(),
                                    "key": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "message": t.string().optional(),
                    }
                )
            ).optional(),
            "insertTime": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string(),
            "url": t.string().optional(),
            "update": t.proxy(renames["ResourceUpdateOut"]).optional(),
            "properties": t.string().optional(),
            "finalProperties": t.string().optional(),
            "updateTime": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["GlobalSetPolicyRequestIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["GlobalSetPolicyRequestIn"])
    types["GlobalSetPolicyRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlobalSetPolicyRequestOut"])
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
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])

    functions = {}
    functions["manifestsGet"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/manifests",
        t.struct(
            {
                "filter": t.string().optional(),
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "maxResults": t.integer().optional(),
                "deployment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManifestsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["manifestsList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/manifests",
        t.struct(
            {
                "filter": t.string().optional(),
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "maxResults": t.integer().optional(),
                "deployment": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManifestsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/operations/{operation}",
        t.struct(
            {
                "operation": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/operations/{operation}",
        t.struct(
            {
                "operation": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["typesList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/types",
        t.struct(
            {
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TypesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourcesList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/resources/{resource}",
        t.struct(
            {
                "project": t.string().optional(),
                "deployment": t.string().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourcesGet"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/resources/{resource}",
        t.struct(
            {
                "project": t.string().optional(),
                "deployment": t.string().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsTestIamPermissions"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsGet"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsSetIamPolicy"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsGetIamPolicy"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsInsert"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsStop"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDelete"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsUpdate"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsPatch"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsCancelPreview"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="deploymentmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
