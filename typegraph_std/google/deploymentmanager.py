from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_deploymentmanager():
    deploymentmanager = HTTPRuntime("https://deploymentmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_deploymentmanager_1_ErrorResponse",
        "ResourceUpdateIn": "_deploymentmanager_2_ResourceUpdateIn",
        "ResourceUpdateOut": "_deploymentmanager_3_ResourceUpdateOut",
        "DeploymentIn": "_deploymentmanager_4_DeploymentIn",
        "DeploymentOut": "_deploymentmanager_5_DeploymentOut",
        "ManifestsListResponseIn": "_deploymentmanager_6_ManifestsListResponseIn",
        "ManifestsListResponseOut": "_deploymentmanager_7_ManifestsListResponseOut",
        "DeploymentUpdateIn": "_deploymentmanager_8_DeploymentUpdateIn",
        "DeploymentUpdateOut": "_deploymentmanager_9_DeploymentUpdateOut",
        "DeploymentsStopRequestIn": "_deploymentmanager_10_DeploymentsStopRequestIn",
        "DeploymentsStopRequestOut": "_deploymentmanager_11_DeploymentsStopRequestOut",
        "ConfigFileIn": "_deploymentmanager_12_ConfigFileIn",
        "ConfigFileOut": "_deploymentmanager_13_ConfigFileOut",
        "ResourceAccessControlIn": "_deploymentmanager_14_ResourceAccessControlIn",
        "ResourceAccessControlOut": "_deploymentmanager_15_ResourceAccessControlOut",
        "OperationsListResponseIn": "_deploymentmanager_16_OperationsListResponseIn",
        "OperationsListResponseOut": "_deploymentmanager_17_OperationsListResponseOut",
        "TargetConfigurationIn": "_deploymentmanager_18_TargetConfigurationIn",
        "TargetConfigurationOut": "_deploymentmanager_19_TargetConfigurationOut",
        "DeploymentLabelEntryIn": "_deploymentmanager_20_DeploymentLabelEntryIn",
        "DeploymentLabelEntryOut": "_deploymentmanager_21_DeploymentLabelEntryOut",
        "BindingIn": "_deploymentmanager_22_BindingIn",
        "BindingOut": "_deploymentmanager_23_BindingOut",
        "AuditConfigIn": "_deploymentmanager_24_AuditConfigIn",
        "AuditConfigOut": "_deploymentmanager_25_AuditConfigOut",
        "TypesListResponseIn": "_deploymentmanager_26_TypesListResponseIn",
        "TypesListResponseOut": "_deploymentmanager_27_TypesListResponseOut",
        "ResourceIn": "_deploymentmanager_28_ResourceIn",
        "ResourceOut": "_deploymentmanager_29_ResourceOut",
        "GlobalSetPolicyRequestIn": "_deploymentmanager_30_GlobalSetPolicyRequestIn",
        "GlobalSetPolicyRequestOut": "_deploymentmanager_31_GlobalSetPolicyRequestOut",
        "PolicyIn": "_deploymentmanager_32_PolicyIn",
        "PolicyOut": "_deploymentmanager_33_PolicyOut",
        "ExprIn": "_deploymentmanager_34_ExprIn",
        "ExprOut": "_deploymentmanager_35_ExprOut",
        "DeploymentsListResponseIn": "_deploymentmanager_36_DeploymentsListResponseIn",
        "DeploymentsListResponseOut": "_deploymentmanager_37_DeploymentsListResponseOut",
        "DeploymentUpdateLabelEntryIn": "_deploymentmanager_38_DeploymentUpdateLabelEntryIn",
        "DeploymentUpdateLabelEntryOut": "_deploymentmanager_39_DeploymentUpdateLabelEntryOut",
        "ManifestIn": "_deploymentmanager_40_ManifestIn",
        "ManifestOut": "_deploymentmanager_41_ManifestOut",
        "TestPermissionsRequestIn": "_deploymentmanager_42_TestPermissionsRequestIn",
        "TestPermissionsRequestOut": "_deploymentmanager_43_TestPermissionsRequestOut",
        "TestPermissionsResponseIn": "_deploymentmanager_44_TestPermissionsResponseIn",
        "TestPermissionsResponseOut": "_deploymentmanager_45_TestPermissionsResponseOut",
        "TypeIn": "_deploymentmanager_46_TypeIn",
        "TypeOut": "_deploymentmanager_47_TypeOut",
        "OperationIn": "_deploymentmanager_48_OperationIn",
        "OperationOut": "_deploymentmanager_49_OperationOut",
        "ResourcesListResponseIn": "_deploymentmanager_50_ResourcesListResponseIn",
        "ResourcesListResponseOut": "_deploymentmanager_51_ResourcesListResponseOut",
        "DeploymentsCancelPreviewRequestIn": "_deploymentmanager_52_DeploymentsCancelPreviewRequestIn",
        "DeploymentsCancelPreviewRequestOut": "_deploymentmanager_53_DeploymentsCancelPreviewRequestOut",
        "ImportFileIn": "_deploymentmanager_54_ImportFileIn",
        "ImportFileOut": "_deploymentmanager_55_ImportFileOut",
        "AuditLogConfigIn": "_deploymentmanager_56_AuditLogConfigIn",
        "AuditLogConfigOut": "_deploymentmanager_57_AuditLogConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ResourceUpdateIn"] = t.struct(
        {
            "state": t.string().optional(),
            "intent": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlIn"]).optional(),
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
            "properties": t.string().optional(),
            "manifest": t.string().optional(),
        }
    ).named(renames["ResourceUpdateIn"])
    types["ResourceUpdateOut"] = t.struct(
        {
            "state": t.string().optional(),
            "intent": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
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
            "properties": t.string().optional(),
            "manifest": t.string().optional(),
        }
    ).named(renames["ResourceUpdateOut"])
    types["DeploymentIn"] = t.struct(
        {
            "manifest": t.string().optional(),
            "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
            "insertTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "fingerprint": t.string().optional(),
            "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
            "selfLink": t.string().optional(),
            "labels": t.array(t.proxy(renames["DeploymentLabelEntryIn"])).optional(),
            "id": t.string(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "manifest": t.string().optional(),
            "target": t.proxy(renames["TargetConfigurationOut"]).optional(),
            "insertTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "fingerprint": t.string().optional(),
            "update": t.proxy(renames["DeploymentUpdateOut"]).optional(),
            "selfLink": t.string().optional(),
            "labels": t.array(t.proxy(renames["DeploymentLabelEntryOut"])).optional(),
            "id": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
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
    types["DeploymentUpdateIn"] = t.struct(
        {
            "labels": t.array(
                t.proxy(renames["DeploymentUpdateLabelEntryIn"])
            ).optional(),
            "manifest": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["DeploymentUpdateIn"])
    types["DeploymentUpdateOut"] = t.struct(
        {
            "labels": t.array(
                t.proxy(renames["DeploymentUpdateLabelEntryOut"])
            ).optional(),
            "manifest": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentUpdateOut"])
    types["DeploymentsStopRequestIn"] = t.struct(
        {"fingerprint": t.string().optional()}
    ).named(renames["DeploymentsStopRequestIn"])
    types["DeploymentsStopRequestOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentsStopRequestOut"])
    types["ConfigFileIn"] = t.struct({"content": t.string().optional()}).named(
        renames["ConfigFileIn"]
    )
    types["ConfigFileOut"] = t.struct(
        {
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigFileOut"])
    types["ResourceAccessControlIn"] = t.struct(
        {"gcpIamPolicy": t.string().optional()}
    ).named(renames["ResourceAccessControlIn"])
    types["ResourceAccessControlOut"] = t.struct(
        {
            "gcpIamPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceAccessControlOut"])
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
    types["TargetConfigurationIn"] = t.struct(
        {
            "config": t.proxy(renames["ConfigFileIn"]).optional(),
            "imports": t.array(t.proxy(renames["ImportFileIn"])).optional(),
        }
    ).named(renames["TargetConfigurationIn"])
    types["TargetConfigurationOut"] = t.struct(
        {
            "config": t.proxy(renames["ConfigFileOut"]).optional(),
            "imports": t.array(t.proxy(renames["ImportFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetConfigurationOut"])
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
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["ResourceIn"] = t.struct(
        {
            "warnings": t.array(
                t.struct(
                    {
                        "message": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "value": t.string().optional(),
                                    "key": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "code": t.string().optional(),
                    }
                )
            ).optional(),
            "name": t.string().optional(),
            "id": t.string(),
            "manifest": t.string().optional(),
            "update": t.proxy(renames["ResourceUpdateIn"]).optional(),
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
            "insertTime": t.string().optional(),
            "url": t.string().optional(),
            "finalProperties": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlIn"]).optional(),
            "properties": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "warnings": t.array(
                t.struct(
                    {
                        "message": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "value": t.string().optional(),
                                    "key": t.string().optional(),
                                }
                            )
                        ).optional(),
                        "code": t.string().optional(),
                    }
                )
            ).optional(),
            "name": t.string().optional(),
            "id": t.string(),
            "manifest": t.string().optional(),
            "update": t.proxy(renames["ResourceUpdateOut"]).optional(),
            "updateTime": t.string().optional(),
            "type": t.string().optional(),
            "insertTime": t.string().optional(),
            "url": t.string().optional(),
            "finalProperties": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlOut"]).optional(),
            "properties": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["GlobalSetPolicyRequestIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GlobalSetPolicyRequestIn"])
    types["GlobalSetPolicyRequestOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlobalSetPolicyRequestOut"])
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["DeploymentsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deployments": t.array(t.proxy(renames["DeploymentIn"])).optional(),
        }
    ).named(renames["DeploymentsListResponseIn"])
    types["DeploymentsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deployments": t.array(t.proxy(renames["DeploymentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentsListResponseOut"])
    types["DeploymentUpdateLabelEntryIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["DeploymentUpdateLabelEntryIn"])
    types["DeploymentUpdateLabelEntryOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentUpdateLabelEntryOut"])
    types["ManifestIn"] = t.struct(
        {
            "manifestSizeLimitBytes": t.string().optional(),
            "expandedConfig": t.string().optional(),
            "imports": t.array(t.proxy(renames["ImportFileIn"])).optional(),
            "insertTime": t.string().optional(),
            "manifestSizeBytes": t.string().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "id": t.string(),
            "layout": t.string().optional(),
            "config": t.proxy(renames["ConfigFileIn"]).optional(),
        }
    ).named(renames["ManifestIn"])
    types["ManifestOut"] = t.struct(
        {
            "manifestSizeLimitBytes": t.string().optional(),
            "expandedConfig": t.string().optional(),
            "imports": t.array(t.proxy(renames["ImportFileOut"])).optional(),
            "insertTime": t.string().optional(),
            "manifestSizeBytes": t.string().optional(),
            "name": t.string().optional(),
            "selfLink": t.string().optional(),
            "id": t.string(),
            "layout": t.string().optional(),
            "config": t.proxy(renames["ConfigFileOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManifestOut"])
    types["TestPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestPermissionsRequestIn"])
    types["TestPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestPermissionsRequestOut"])
    types["TestPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestPermissionsResponseIn"])
    types["TestPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestPermissionsResponseOut"])
    types["TypeIn"] = t.struct(
        {
            "insertTime": t.string().optional(),
            "id": t.string(),
            "selfLink": t.string().optional(),
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "insertTime": t.string().optional(),
            "id": t.string(),
            "selfLink": t.string().optional(),
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["OperationIn"] = t.struct(
        {
            "id": t.string().optional(),
            "selfLink": t.string().optional(),
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
            "httpErrorStatusCode": t.integer().optional(),
            "description": t.string().optional(),
            "startTime": t.string().optional(),
            "clientOperationId": t.string().optional(),
            "operationType": t.string().optional(),
            "progress": t.integer().optional(),
            "endTime": t.string().optional(),
            "targetId": t.string().optional(),
            "statusMessage": t.string().optional(),
            "operationGroupId": t.string().optional(),
            "name": t.string().optional(),
            "creationTimestamp": t.string().optional(),
            "region": t.string().optional(),
            "targetLink": t.string().optional(),
            "httpErrorMessage": t.string().optional(),
            "user": t.string().optional(),
            "error": t.struct(
                {
                    "errors": t.array(
                        t.struct(
                            {
                                "message": t.string().optional(),
                                "code": t.string().optional(),
                                "location": t.string().optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "status": t.string().optional(),
            "zone": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "id": t.string().optional(),
            "selfLink": t.string().optional(),
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
            "httpErrorStatusCode": t.integer().optional(),
            "description": t.string().optional(),
            "startTime": t.string().optional(),
            "clientOperationId": t.string().optional(),
            "operationType": t.string().optional(),
            "progress": t.integer().optional(),
            "endTime": t.string().optional(),
            "targetId": t.string().optional(),
            "statusMessage": t.string().optional(),
            "operationGroupId": t.string().optional(),
            "name": t.string().optional(),
            "creationTimestamp": t.string().optional(),
            "region": t.string().optional(),
            "targetLink": t.string().optional(),
            "httpErrorMessage": t.string().optional(),
            "user": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "status": t.string().optional(),
            "zone": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["ResourcesListResponseIn"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ResourceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ResourcesListResponseIn"])
    types["ResourcesListResponseOut"] = t.struct(
        {
            "resources": t.array(t.proxy(renames["ResourceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesListResponseOut"])
    types["DeploymentsCancelPreviewRequestIn"] = t.struct(
        {"fingerprint": t.string().optional()}
    ).named(renames["DeploymentsCancelPreviewRequestIn"])
    types["DeploymentsCancelPreviewRequestOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentsCancelPreviewRequestOut"])
    types["ImportFileIn"] = t.struct(
        {"name": t.string().optional(), "content": t.string().optional()}
    ).named(renames["ImportFileIn"])
    types["ImportFileOut"] = t.struct(
        {
            "name": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportFileOut"])
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

    functions = {}
    functions["resourcesList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/resources/{resource}",
        t.struct(
            {
                "deployment": t.string().optional(),
                "resource": t.string().optional(),
                "project": t.string().optional(),
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
                "deployment": t.string().optional(),
                "resource": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["typesList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/types",
        t.struct(
            {
                "filter": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TypesListResponseOut"]),
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
    functions["deploymentsCancelPreview"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsStop"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsPatch"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDelete"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsInsert"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsGetIamPolicy"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsSetIamPolicy"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsGet"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsTestIamPermissions"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsList"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsUpdate"] = deploymentmanager.put(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}",
        t.struct(
            {
                "preview": t.boolean().optional(),
                "deletePolicy": t.string().optional(),
                "project": t.string().optional(),
                "createPolicy": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
                "insertTime": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "updateTime": t.string().optional(),
                "operation": t.proxy(renames["OperationIn"]).optional(),
                "fingerprint": t.string().optional(),
                "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
                "selfLink": t.string().optional(),
                "labels": t.array(
                    t.proxy(renames["DeploymentLabelEntryIn"])
                ).optional(),
                "id": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["manifestsList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/manifests/{manifest}",
        t.struct(
            {
                "project": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManifestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["manifestsGet"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/manifests/{manifest}",
        t.struct(
            {
                "project": t.string().optional(),
                "deployment": t.string().optional(),
                "manifest": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManifestOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="deploymentmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
