from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_deploymentmanager() -> Import:
    deploymentmanager = HTTPRuntime("https://deploymentmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_deploymentmanager_1_ErrorResponse",
        "DeploymentIn": "_deploymentmanager_2_DeploymentIn",
        "DeploymentOut": "_deploymentmanager_3_DeploymentOut",
        "DeploymentsStopRequestIn": "_deploymentmanager_4_DeploymentsStopRequestIn",
        "DeploymentsStopRequestOut": "_deploymentmanager_5_DeploymentsStopRequestOut",
        "ResourcesListResponseIn": "_deploymentmanager_6_ResourcesListResponseIn",
        "ResourcesListResponseOut": "_deploymentmanager_7_ResourcesListResponseOut",
        "AuditConfigIn": "_deploymentmanager_8_AuditConfigIn",
        "AuditConfigOut": "_deploymentmanager_9_AuditConfigOut",
        "TestPermissionsResponseIn": "_deploymentmanager_10_TestPermissionsResponseIn",
        "TestPermissionsResponseOut": "_deploymentmanager_11_TestPermissionsResponseOut",
        "TypeIn": "_deploymentmanager_12_TypeIn",
        "TypeOut": "_deploymentmanager_13_TypeOut",
        "DeploymentUpdateIn": "_deploymentmanager_14_DeploymentUpdateIn",
        "DeploymentUpdateOut": "_deploymentmanager_15_DeploymentUpdateOut",
        "ImportFileIn": "_deploymentmanager_16_ImportFileIn",
        "ImportFileOut": "_deploymentmanager_17_ImportFileOut",
        "ManifestsListResponseIn": "_deploymentmanager_18_ManifestsListResponseIn",
        "ManifestsListResponseOut": "_deploymentmanager_19_ManifestsListResponseOut",
        "DeploymentLabelEntryIn": "_deploymentmanager_20_DeploymentLabelEntryIn",
        "DeploymentLabelEntryOut": "_deploymentmanager_21_DeploymentLabelEntryOut",
        "OperationIn": "_deploymentmanager_22_OperationIn",
        "OperationOut": "_deploymentmanager_23_OperationOut",
        "ExprIn": "_deploymentmanager_24_ExprIn",
        "ExprOut": "_deploymentmanager_25_ExprOut",
        "ManifestIn": "_deploymentmanager_26_ManifestIn",
        "ManifestOut": "_deploymentmanager_27_ManifestOut",
        "ResourceAccessControlIn": "_deploymentmanager_28_ResourceAccessControlIn",
        "ResourceAccessControlOut": "_deploymentmanager_29_ResourceAccessControlOut",
        "ResourceIn": "_deploymentmanager_30_ResourceIn",
        "ResourceOut": "_deploymentmanager_31_ResourceOut",
        "GlobalSetPolicyRequestIn": "_deploymentmanager_32_GlobalSetPolicyRequestIn",
        "GlobalSetPolicyRequestOut": "_deploymentmanager_33_GlobalSetPolicyRequestOut",
        "ConfigFileIn": "_deploymentmanager_34_ConfigFileIn",
        "ConfigFileOut": "_deploymentmanager_35_ConfigFileOut",
        "DeploymentUpdateLabelEntryIn": "_deploymentmanager_36_DeploymentUpdateLabelEntryIn",
        "DeploymentUpdateLabelEntryOut": "_deploymentmanager_37_DeploymentUpdateLabelEntryOut",
        "PolicyIn": "_deploymentmanager_38_PolicyIn",
        "PolicyOut": "_deploymentmanager_39_PolicyOut",
        "TypesListResponseIn": "_deploymentmanager_40_TypesListResponseIn",
        "TypesListResponseOut": "_deploymentmanager_41_TypesListResponseOut",
        "OperationsListResponseIn": "_deploymentmanager_42_OperationsListResponseIn",
        "OperationsListResponseOut": "_deploymentmanager_43_OperationsListResponseOut",
        "DeploymentsCancelPreviewRequestIn": "_deploymentmanager_44_DeploymentsCancelPreviewRequestIn",
        "DeploymentsCancelPreviewRequestOut": "_deploymentmanager_45_DeploymentsCancelPreviewRequestOut",
        "ResourceUpdateIn": "_deploymentmanager_46_ResourceUpdateIn",
        "ResourceUpdateOut": "_deploymentmanager_47_ResourceUpdateOut",
        "BindingIn": "_deploymentmanager_48_BindingIn",
        "BindingOut": "_deploymentmanager_49_BindingOut",
        "TargetConfigurationIn": "_deploymentmanager_50_TargetConfigurationIn",
        "TargetConfigurationOut": "_deploymentmanager_51_TargetConfigurationOut",
        "TestPermissionsRequestIn": "_deploymentmanager_52_TestPermissionsRequestIn",
        "TestPermissionsRequestOut": "_deploymentmanager_53_TestPermissionsRequestOut",
        "AuditLogConfigIn": "_deploymentmanager_54_AuditLogConfigIn",
        "AuditLogConfigOut": "_deploymentmanager_55_AuditLogConfigOut",
        "DeploymentsListResponseIn": "_deploymentmanager_56_DeploymentsListResponseIn",
        "DeploymentsListResponseOut": "_deploymentmanager_57_DeploymentsListResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DeploymentIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["DeploymentLabelEntryIn"])).optional(),
            "updateTime": t.string().optional(),
            "id": t.string(),
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
            "fingerprint": t.string().optional(),
            "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
            "insertTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "manifest": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["DeploymentLabelEntryOut"])).optional(),
            "updateTime": t.string().optional(),
            "id": t.string(),
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "target": t.proxy(renames["TargetConfigurationOut"]).optional(),
            "fingerprint": t.string().optional(),
            "update": t.proxy(renames["DeploymentUpdateOut"]).optional(),
            "insertTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "manifest": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
    types["DeploymentsStopRequestIn"] = t.struct(
        {"fingerprint": t.string().optional()}
    ).named(renames["DeploymentsStopRequestIn"])
    types["DeploymentsStopRequestOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentsStopRequestOut"])
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
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "id": t.string(),
            "selfLink": t.string().optional(),
            "insertTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "id": t.string(),
            "selfLink": t.string().optional(),
            "insertTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["DeploymentUpdateIn"] = t.struct(
        {
            "description": t.string().optional(),
            "manifest": t.string().optional(),
            "labels": t.array(
                t.proxy(renames["DeploymentUpdateLabelEntryIn"])
            ).optional(),
        }
    ).named(renames["DeploymentUpdateIn"])
    types["DeploymentUpdateOut"] = t.struct(
        {
            "description": t.string().optional(),
            "manifest": t.string().optional(),
            "labels": t.array(
                t.proxy(renames["DeploymentUpdateLabelEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentUpdateOut"])
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
    types["ManifestsListResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "manifests": t.array(t.proxy(renames["ManifestIn"])).optional(),
        }
    ).named(renames["ManifestsListResponseIn"])
    types["ManifestsListResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "manifests": t.array(t.proxy(renames["ManifestOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManifestsListResponseOut"])
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
    types["OperationIn"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "progress": t.integer().optional(),
            "zone": t.string().optional(),
            "kind": t.string().optional(),
            "httpErrorMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "operationType": t.string().optional(),
            "description": t.string().optional(),
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
                        "code": t.string().optional(),
                        "message": t.string().optional(),
                    }
                )
            ).optional(),
            "operationGroupId": t.string().optional(),
            "creationTimestamp": t.string().optional(),
            "statusMessage": t.string().optional(),
            "user": t.string().optional(),
            "clientOperationId": t.string().optional(),
            "targetLink": t.string().optional(),
            "targetId": t.string().optional(),
            "insertTime": t.string().optional(),
            "error": t.struct(
                {
                    "errors": t.array(
                        t.struct(
                            {
                                "code": t.string().optional(),
                                "location": t.string().optional(),
                                "message": t.string().optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "id": t.string().optional(),
            "region": t.string().optional(),
            "status": t.string().optional(),
            "httpErrorStatusCode": t.integer().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "selfLink": t.string().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "progress": t.integer().optional(),
            "zone": t.string().optional(),
            "kind": t.string().optional(),
            "httpErrorMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "operationType": t.string().optional(),
            "description": t.string().optional(),
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
                        "code": t.string().optional(),
                        "message": t.string().optional(),
                    }
                )
            ).optional(),
            "operationGroupId": t.string().optional(),
            "creationTimestamp": t.string().optional(),
            "statusMessage": t.string().optional(),
            "user": t.string().optional(),
            "clientOperationId": t.string().optional(),
            "targetLink": t.string().optional(),
            "targetId": t.string().optional(),
            "insertTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "id": t.string().optional(),
            "region": t.string().optional(),
            "status": t.string().optional(),
            "httpErrorStatusCode": t.integer().optional(),
        }
    ).named(renames["OperationOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ManifestIn"] = t.struct(
        {
            "manifestSizeBytes": t.string().optional(),
            "imports": t.array(t.proxy(renames["ImportFileIn"])).optional(),
            "insertTime": t.string().optional(),
            "expandedConfig": t.string().optional(),
            "selfLink": t.string().optional(),
            "layout": t.string().optional(),
            "name": t.string().optional(),
            "config": t.proxy(renames["ConfigFileIn"]).optional(),
            "id": t.string(),
            "manifestSizeLimitBytes": t.string().optional(),
        }
    ).named(renames["ManifestIn"])
    types["ManifestOut"] = t.struct(
        {
            "manifestSizeBytes": t.string().optional(),
            "imports": t.array(t.proxy(renames["ImportFileOut"])).optional(),
            "insertTime": t.string().optional(),
            "expandedConfig": t.string().optional(),
            "selfLink": t.string().optional(),
            "layout": t.string().optional(),
            "name": t.string().optional(),
            "config": t.proxy(renames["ConfigFileOut"]).optional(),
            "id": t.string(),
            "manifestSizeLimitBytes": t.string().optional(),
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
    types["ResourceIn"] = t.struct(
        {
            "finalProperties": t.string().optional(),
            "insertTime": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlIn"]).optional(),
            "properties": t.string().optional(),
            "manifest": t.string().optional(),
            "type": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "message": t.string().optional(),
                        "code": t.string().optional(),
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
            "updateTime": t.string().optional(),
            "url": t.string().optional(),
            "id": t.string(),
            "update": t.proxy(renames["ResourceUpdateIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "finalProperties": t.string().optional(),
            "insertTime": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlOut"]).optional(),
            "properties": t.string().optional(),
            "manifest": t.string().optional(),
            "type": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "message": t.string().optional(),
                        "code": t.string().optional(),
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
            "updateTime": t.string().optional(),
            "url": t.string().optional(),
            "id": t.string(),
            "update": t.proxy(renames["ResourceUpdateOut"]).optional(),
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
    types["ConfigFileIn"] = t.struct({"content": t.string().optional()}).named(
        renames["ConfigFileIn"]
    )
    types["ConfigFileOut"] = t.struct(
        {
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigFileOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["DeploymentsCancelPreviewRequestIn"] = t.struct(
        {"fingerprint": t.string().optional()}
    ).named(renames["DeploymentsCancelPreviewRequestIn"])
    types["DeploymentsCancelPreviewRequestOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentsCancelPreviewRequestOut"])
    types["ResourceUpdateIn"] = t.struct(
        {
            "accessControl": t.proxy(renames["ResourceAccessControlIn"]).optional(),
            "intent": t.string().optional(),
            "properties": t.string().optional(),
            "state": t.string().optional(),
            "finalProperties": t.string().optional(),
            "manifest": t.string().optional(),
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
        }
    ).named(renames["ResourceUpdateIn"])
    types["ResourceUpdateOut"] = t.struct(
        {
            "accessControl": t.proxy(renames["ResourceAccessControlOut"]).optional(),
            "intent": t.string().optional(),
            "properties": t.string().optional(),
            "state": t.string().optional(),
            "finalProperties": t.string().optional(),
            "manifest": t.string().optional(),
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
        }
    ).named(renames["ResourceUpdateOut"])
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
    types["TestPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestPermissionsRequestIn"])
    types["TestPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestPermissionsRequestOut"])
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

    functions = {}
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
    functions["manifestsGet"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/manifests",
        t.struct(
            {
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "deployment": t.string().optional(),
                "orderBy": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "deployment": t.string().optional(),
                "orderBy": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManifestsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsStop"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsCancelPreview"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsUpdate"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsSetIamPolicy"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsTestIamPermissions"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDelete"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsGet"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsInsert"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsPatch"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsGetIamPolicy"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{resource}/getIamPolicy",
        t.struct(
            {
                "project": t.string().optional(),
                "resource": t.string().optional(),
                "optionsRequestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["typesList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/types",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TypesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourcesGet"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/resources",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "deployment": t.string().optional(),
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourcesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["resourcesList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments/{deployment}/resources",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "deployment": t.string().optional(),
                "project": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ResourcesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="deploymentmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
