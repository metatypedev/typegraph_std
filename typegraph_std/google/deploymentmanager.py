from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_deploymentmanager() -> Import:
    deploymentmanager = HTTPRuntime("https://deploymentmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_deploymentmanager_1_ErrorResponse",
        "AuditConfigIn": "_deploymentmanager_2_AuditConfigIn",
        "AuditConfigOut": "_deploymentmanager_3_AuditConfigOut",
        "DeploymentUpdateIn": "_deploymentmanager_4_DeploymentUpdateIn",
        "DeploymentUpdateOut": "_deploymentmanager_5_DeploymentUpdateOut",
        "OperationIn": "_deploymentmanager_6_OperationIn",
        "OperationOut": "_deploymentmanager_7_OperationOut",
        "TypeIn": "_deploymentmanager_8_TypeIn",
        "TypeOut": "_deploymentmanager_9_TypeOut",
        "OperationsListResponseIn": "_deploymentmanager_10_OperationsListResponseIn",
        "OperationsListResponseOut": "_deploymentmanager_11_OperationsListResponseOut",
        "PolicyIn": "_deploymentmanager_12_PolicyIn",
        "PolicyOut": "_deploymentmanager_13_PolicyOut",
        "ResourceIn": "_deploymentmanager_14_ResourceIn",
        "ResourceOut": "_deploymentmanager_15_ResourceOut",
        "DeploymentsCancelPreviewRequestIn": "_deploymentmanager_16_DeploymentsCancelPreviewRequestIn",
        "DeploymentsCancelPreviewRequestOut": "_deploymentmanager_17_DeploymentsCancelPreviewRequestOut",
        "ConfigFileIn": "_deploymentmanager_18_ConfigFileIn",
        "ConfigFileOut": "_deploymentmanager_19_ConfigFileOut",
        "TargetConfigurationIn": "_deploymentmanager_20_TargetConfigurationIn",
        "TargetConfigurationOut": "_deploymentmanager_21_TargetConfigurationOut",
        "ResourceUpdateIn": "_deploymentmanager_22_ResourceUpdateIn",
        "ResourceUpdateOut": "_deploymentmanager_23_ResourceUpdateOut",
        "TypesListResponseIn": "_deploymentmanager_24_TypesListResponseIn",
        "TypesListResponseOut": "_deploymentmanager_25_TypesListResponseOut",
        "DeploymentUpdateLabelEntryIn": "_deploymentmanager_26_DeploymentUpdateLabelEntryIn",
        "DeploymentUpdateLabelEntryOut": "_deploymentmanager_27_DeploymentUpdateLabelEntryOut",
        "ResourceAccessControlIn": "_deploymentmanager_28_ResourceAccessControlIn",
        "ResourceAccessControlOut": "_deploymentmanager_29_ResourceAccessControlOut",
        "ResourcesListResponseIn": "_deploymentmanager_30_ResourcesListResponseIn",
        "ResourcesListResponseOut": "_deploymentmanager_31_ResourcesListResponseOut",
        "ManifestIn": "_deploymentmanager_32_ManifestIn",
        "ManifestOut": "_deploymentmanager_33_ManifestOut",
        "ImportFileIn": "_deploymentmanager_34_ImportFileIn",
        "ImportFileOut": "_deploymentmanager_35_ImportFileOut",
        "DeploymentsListResponseIn": "_deploymentmanager_36_DeploymentsListResponseIn",
        "DeploymentsListResponseOut": "_deploymentmanager_37_DeploymentsListResponseOut",
        "BindingIn": "_deploymentmanager_38_BindingIn",
        "BindingOut": "_deploymentmanager_39_BindingOut",
        "AuditLogConfigIn": "_deploymentmanager_40_AuditLogConfigIn",
        "AuditLogConfigOut": "_deploymentmanager_41_AuditLogConfigOut",
        "DeploymentIn": "_deploymentmanager_42_DeploymentIn",
        "DeploymentOut": "_deploymentmanager_43_DeploymentOut",
        "DeploymentsStopRequestIn": "_deploymentmanager_44_DeploymentsStopRequestIn",
        "DeploymentsStopRequestOut": "_deploymentmanager_45_DeploymentsStopRequestOut",
        "GlobalSetPolicyRequestIn": "_deploymentmanager_46_GlobalSetPolicyRequestIn",
        "GlobalSetPolicyRequestOut": "_deploymentmanager_47_GlobalSetPolicyRequestOut",
        "ExprIn": "_deploymentmanager_48_ExprIn",
        "ExprOut": "_deploymentmanager_49_ExprOut",
        "ManifestsListResponseIn": "_deploymentmanager_50_ManifestsListResponseIn",
        "ManifestsListResponseOut": "_deploymentmanager_51_ManifestsListResponseOut",
        "TestPermissionsRequestIn": "_deploymentmanager_52_TestPermissionsRequestIn",
        "TestPermissionsRequestOut": "_deploymentmanager_53_TestPermissionsRequestOut",
        "DeploymentLabelEntryIn": "_deploymentmanager_54_DeploymentLabelEntryIn",
        "DeploymentLabelEntryOut": "_deploymentmanager_55_DeploymentLabelEntryOut",
        "TestPermissionsResponseIn": "_deploymentmanager_56_TestPermissionsResponseIn",
        "TestPermissionsResponseOut": "_deploymentmanager_57_TestPermissionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["DeploymentUpdateIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.array(
                t.proxy(renames["DeploymentUpdateLabelEntryIn"])
            ).optional(),
            "manifest": t.string().optional(),
        }
    ).named(renames["DeploymentUpdateIn"])
    types["DeploymentUpdateOut"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.array(
                t.proxy(renames["DeploymentUpdateLabelEntryOut"])
            ).optional(),
            "manifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentUpdateOut"])
    types["OperationIn"] = t.struct(
        {
            "progress": t.integer().optional(),
            "status": t.string().optional(),
            "description": t.string().optional(),
            "creationTimestamp": t.string().optional(),
            "httpErrorStatusCode": t.integer().optional(),
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
            "httpErrorMessage": t.string().optional(),
            "statusMessage": t.string().optional(),
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
            "selfLink": t.string().optional(),
            "clientOperationId": t.string().optional(),
            "targetLink": t.string().optional(),
            "endTime": t.string().optional(),
            "user": t.string().optional(),
            "name": t.string().optional(),
            "operationGroupId": t.string().optional(),
            "zone": t.string().optional(),
            "operationType": t.string().optional(),
            "insertTime": t.string().optional(),
            "startTime": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "targetId": t.string().optional(),
            "region": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "progress": t.integer().optional(),
            "status": t.string().optional(),
            "description": t.string().optional(),
            "creationTimestamp": t.string().optional(),
            "httpErrorStatusCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "httpErrorMessage": t.string().optional(),
            "statusMessage": t.string().optional(),
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
            "selfLink": t.string().optional(),
            "clientOperationId": t.string().optional(),
            "targetLink": t.string().optional(),
            "endTime": t.string().optional(),
            "user": t.string().optional(),
            "name": t.string().optional(),
            "operationGroupId": t.string().optional(),
            "zone": t.string().optional(),
            "operationType": t.string().optional(),
            "insertTime": t.string().optional(),
            "startTime": t.string().optional(),
            "kind": t.string().optional(),
            "id": t.string().optional(),
            "targetId": t.string().optional(),
            "region": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["TypeIn"] = t.struct(
        {
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "selfLink": t.string().optional(),
            "id": t.string(),
            "insertTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "selfLink": t.string().optional(),
            "id": t.string(),
            "insertTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ResourceIn"] = t.struct(
        {
            "properties": t.string().optional(),
            "name": t.string().optional(),
            "insertTime": t.string().optional(),
            "url": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlIn"]).optional(),
            "type": t.string().optional(),
            "finalProperties": t.string().optional(),
            "update": t.proxy(renames["ResourceUpdateIn"]).optional(),
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
            "id": t.string(),
            "updateTime": t.string().optional(),
            "manifest": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "properties": t.string().optional(),
            "name": t.string().optional(),
            "insertTime": t.string().optional(),
            "url": t.string().optional(),
            "accessControl": t.proxy(renames["ResourceAccessControlOut"]).optional(),
            "type": t.string().optional(),
            "finalProperties": t.string().optional(),
            "update": t.proxy(renames["ResourceUpdateOut"]).optional(),
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
            "id": t.string(),
            "updateTime": t.string().optional(),
            "manifest": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["DeploymentsCancelPreviewRequestIn"] = t.struct(
        {"fingerprint": t.string().optional()}
    ).named(renames["DeploymentsCancelPreviewRequestIn"])
    types["DeploymentsCancelPreviewRequestOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentsCancelPreviewRequestOut"])
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
    types["ResourceUpdateIn"] = t.struct(
        {
            "accessControl": t.proxy(renames["ResourceAccessControlIn"]).optional(),
            "intent": t.string().optional(),
            "properties": t.string().optional(),
            "state": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "code": t.string().optional(),
                        "message": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "value": t.string().optional(),
                                    "key": t.string().optional(),
                                }
                            )
                        ).optional(),
                    }
                )
            ).optional(),
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
            "manifest": t.string().optional(),
            "finalProperties": t.string().optional(),
        }
    ).named(renames["ResourceUpdateIn"])
    types["ResourceUpdateOut"] = t.struct(
        {
            "accessControl": t.proxy(renames["ResourceAccessControlOut"]).optional(),
            "intent": t.string().optional(),
            "properties": t.string().optional(),
            "state": t.string().optional(),
            "warnings": t.array(
                t.struct(
                    {
                        "code": t.string().optional(),
                        "message": t.string().optional(),
                        "data": t.array(
                            t.struct(
                                {
                                    "value": t.string().optional(),
                                    "key": t.string().optional(),
                                }
                            )
                        ).optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "manifest": t.string().optional(),
            "finalProperties": t.string().optional(),
        }
    ).named(renames["ResourceUpdateOut"])
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
    types["ResourceAccessControlIn"] = t.struct(
        {"gcpIamPolicy": t.string().optional()}
    ).named(renames["ResourceAccessControlIn"])
    types["ResourceAccessControlOut"] = t.struct(
        {
            "gcpIamPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceAccessControlOut"])
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
    types["ManifestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string(),
            "layout": t.string().optional(),
            "manifestSizeBytes": t.string().optional(),
            "expandedConfig": t.string().optional(),
            "imports": t.array(t.proxy(renames["ImportFileIn"])).optional(),
            "manifestSizeLimitBytes": t.string().optional(),
            "config": t.proxy(renames["ConfigFileIn"]).optional(),
            "insertTime": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["ManifestIn"])
    types["ManifestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string(),
            "layout": t.string().optional(),
            "manifestSizeBytes": t.string().optional(),
            "expandedConfig": t.string().optional(),
            "imports": t.array(t.proxy(renames["ImportFileOut"])).optional(),
            "manifestSizeLimitBytes": t.string().optional(),
            "config": t.proxy(renames["ConfigFileOut"]).optional(),
            "insertTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManifestOut"])
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
    types["DeploymentIn"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "labels": t.array(t.proxy(renames["DeploymentLabelEntryIn"])).optional(),
            "manifest": t.string().optional(),
            "id": t.string(),
            "insertTime": t.string().optional(),
            "operation": t.proxy(renames["OperationIn"]).optional(),
            "target": t.proxy(renames["TargetConfigurationIn"]).optional(),
            "update": t.proxy(renames["DeploymentUpdateIn"]).optional(),
            "selfLink": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "fingerprint": t.string().optional(),
            "labels": t.array(t.proxy(renames["DeploymentLabelEntryOut"])).optional(),
            "manifest": t.string().optional(),
            "id": t.string(),
            "insertTime": t.string().optional(),
            "operation": t.proxy(renames["OperationOut"]).optional(),
            "target": t.proxy(renames["TargetConfigurationOut"]).optional(),
            "update": t.proxy(renames["DeploymentUpdateOut"]).optional(),
            "selfLink": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
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
    types["TestPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestPermissionsRequestIn"])
    types["TestPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestPermissionsRequestOut"])
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
    types["TestPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestPermissionsResponseIn"])
    types["TestPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestPermissionsResponseOut"])

    functions = {}
    functions["typesList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/types",
        t.struct(
            {
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "project": t.string().optional(),
                "orderBy": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TypesListResponseOut"]),
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
    functions["deploymentsInsert"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsTestIamPermissions"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/deployments",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "maxResults": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeploymentsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/operations",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = deploymentmanager.get(
        "deploymentmanager/v2/projects/{project}/global/operations",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "project": t.string().optional(),
                "filter": t.string().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="deploymentmanager", renames=renames, types=types, functions=functions
    )
