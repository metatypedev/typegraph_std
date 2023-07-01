from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_assuredworkloads():
    assuredworkloads = HTTPRuntime("https://assuredworkloads.googleapis.com/")

    renames = {
        "ErrorResponse": "_assuredworkloads_1_ErrorResponse",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn": "_assuredworkloads_2_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut": "_assuredworkloads_3_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut",
        "GoogleProtobufEmptyIn": "_assuredworkloads_4_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_assuredworkloads_5_GoogleProtobufEmptyOut",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn": "_assuredworkloads_6_GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut": "_assuredworkloads_7_GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut",
        "GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn": "_assuredworkloads_8_GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn",
        "GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut": "_assuredworkloads_9_GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn": "_assuredworkloads_10_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut": "_assuredworkloads_11_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut",
        "GoogleCloudAssuredworkloadsV1ViolationIn": "_assuredworkloads_12_GoogleCloudAssuredworkloadsV1ViolationIn",
        "GoogleCloudAssuredworkloadsV1ViolationOut": "_assuredworkloads_13_GoogleCloudAssuredworkloadsV1ViolationOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn": "_assuredworkloads_14_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut": "_assuredworkloads_15_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationIn": "_assuredworkloads_16_GoogleCloudAssuredworkloadsV1ViolationRemediationIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationOut": "_assuredworkloads_17_GoogleCloudAssuredworkloadsV1ViolationRemediationOut",
        "GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn": "_assuredworkloads_18_GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut": "_assuredworkloads_19_GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn": "_assuredworkloads_20_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut": "_assuredworkloads_21_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn": "_assuredworkloads_22_GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut": "_assuredworkloads_23_GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn": "_assuredworkloads_24_GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut": "_assuredworkloads_25_GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut",
        "GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn": "_assuredworkloads_26_GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn",
        "GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut": "_assuredworkloads_27_GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn": "_assuredworkloads_28_GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut": "_assuredworkloads_29_GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut",
        "GoogleCloudAssuredworkloadsV1WorkloadIn": "_assuredworkloads_30_GoogleCloudAssuredworkloadsV1WorkloadIn",
        "GoogleCloudAssuredworkloadsV1WorkloadOut": "_assuredworkloads_31_GoogleCloudAssuredworkloadsV1WorkloadOut",
        "GoogleLongrunningOperationIn": "_assuredworkloads_32_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_assuredworkloads_33_GoogleLongrunningOperationOut",
        "GoogleRpcStatusIn": "_assuredworkloads_34_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_assuredworkloads_35_GoogleRpcStatusOut",
        "GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn": "_assuredworkloads_36_GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn",
        "GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut": "_assuredworkloads_37_GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut",
        "GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn": "_assuredworkloads_38_GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn",
        "GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut": "_assuredworkloads_39_GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut",
        "GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn": "_assuredworkloads_40_GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn",
        "GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut": "_assuredworkloads_41_GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut",
        "GoogleLongrunningListOperationsResponseIn": "_assuredworkloads_42_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_assuredworkloads_43_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn": "_assuredworkloads_44_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut": "_assuredworkloads_45_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut",
        "GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn": "_assuredworkloads_46_GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut": "_assuredworkloads_47_GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut",
        "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn": "_assuredworkloads_48_GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn",
        "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut": "_assuredworkloads_49_GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut",
        "GoogleCloudAssuredworkloadsV1ListViolationsResponseIn": "_assuredworkloads_50_GoogleCloudAssuredworkloadsV1ListViolationsResponseIn",
        "GoogleCloudAssuredworkloadsV1ListViolationsResponseOut": "_assuredworkloads_51_GoogleCloudAssuredworkloadsV1ListViolationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn"])
    types[
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
    )
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn"] = t.struct(
        {"resourceId": t.string().optional(), "resourceType": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut"] = t.struct(
        {
            "resourceId": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut"])
    types["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
            "complianceRegime": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn"])
    types["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
            "complianceRegime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut"])
    types["GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn"] = t.struct(
        {
            "gcloudInstructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn"
                ]
            ).optional(),
            "consoleInstructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn"])
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut"
    ] = t.struct(
        {
            "gcloudInstructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut"
                ]
            ).optional(),
            "consoleInstructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut"]
    )
    types["GoogleCloudAssuredworkloadsV1ViolationIn"] = t.struct(
        {
            "acknowledgementTime": t.string().optional(),
            "acknowledged": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationIn"])
    types["GoogleCloudAssuredworkloadsV1ViolationOut"] = t.struct(
        {
            "remediation": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1ViolationRemediationOut"]
            ).optional(),
            "category": t.string().optional(),
            "exceptionAuditLogLink": t.string().optional(),
            "auditLogLink": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "acknowledgementTime": t.string().optional(),
            "description": t.string().optional(),
            "state": t.string().optional(),
            "acknowledged": t.boolean().optional(),
            "beginTime": t.string().optional(),
            "resolveTime": t.string().optional(),
            "nonCompliantOrgPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationOut"])
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn"
    ] = t.struct(
        {
            "additionalLinks": t.array(t.string()).optional(),
            "consoleUris": t.array(t.string()).optional(),
            "steps": t.array(t.string()).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn"
        ]
    )
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut"
    ] = t.struct(
        {
            "additionalLinks": t.array(t.string()).optional(),
            "consoleUris": t.array(t.string()).optional(),
            "steps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut"
        ]
    )
    types["GoogleCloudAssuredworkloadsV1ViolationRemediationIn"] = t.struct(
        {
            "compliantValues": t.array(t.string()).optional(),
            "instructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn"
                ]
            ),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationRemediationIn"])
    types["GoogleCloudAssuredworkloadsV1ViolationRemediationOut"] = t.struct(
        {
            "remediationType": t.string().optional(),
            "compliantValues": t.array(t.string()).optional(),
            "instructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationRemediationOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"] = t.struct(
        {
            "remediateFolderViolations": t.boolean().optional(),
            "dataLogsViewer": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"] = t.struct(
        {
            "remediateFolderViolations": t.boolean().optional(),
            "dataLogsViewer": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"])
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn"
    ] = t.struct(
        {
            "gcloudCommands": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
            "steps": t.array(t.string()).optional(),
        }
    ).named(
        renames["GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn"]
    )
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut"
    ] = t.struct(
        {
            "gcloudCommands": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
            "steps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut"
        ]
    )
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn"])
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "displayName": t.string().optional(),
            "resourceId": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "displayName": t.string().optional(),
            "resourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn"] = t.struct(
        {
            "setupErrors": t.array(t.string()).optional(),
            "setupStatus": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut"] = t.struct(
        {
            "setupErrors": t.array(t.string()).optional(),
            "setupStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut"])
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn"] = t.struct(
        {"comment": t.string(), "nonCompliantOrgPolicy": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn"])
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut"] = t.struct(
        {
            "comment": t.string(),
            "nonCompliantOrgPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string(),
            "partner": t.string().optional(),
            "violationNotificationsEnabled": t.boolean().optional(),
            "ekmProvisioningResponse": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"
                ]
            ).optional(),
            "kmsSettings": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn"]
            ).optional(),
            "resourceSettings": t.array(
                t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"]
                )
            ).optional(),
            "etag": t.string().optional(),
            "billingAccount": t.string().optional(),
            "complianceRegime": t.string(),
            "provisionedResourcesParent": t.string().optional(),
            "partnerPermissions": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
            ).optional(),
            "enableSovereignControls": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut"])
            ).optional(),
            "displayName": t.string(),
            "partner": t.string().optional(),
            "violationNotificationsEnabled": t.boolean().optional(),
            "ekmProvisioningResponse": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"
                ]
            ).optional(),
            "kmsSettings": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut"]
            ).optional(),
            "saaEnrollmentResponse": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut"]
            ).optional(),
            "resourceSettings": t.array(
                t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"]
                )
            ).optional(),
            "kajEnrollmentState": t.string().optional(),
            "etag": t.string().optional(),
            "billingAccount": t.string().optional(),
            "complianceRegime": t.string(),
            "compliantButDisallowedServices": t.array(t.string()).optional(),
            "provisionedResourcesParent": t.string().optional(),
            "partnerPermissions": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "enableSovereignControls": t.boolean().optional(),
            "complianceStatus": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workloads": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn"])
    types["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "workloads": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn"] = t.struct(
        {
            "acknowledgedViolationCount": t.integer().optional(),
            "activeViolationCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut"] = t.struct(
        {
            "acknowledgedViolationCount": t.integer().optional(),
            "activeViolationCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut"])
    types["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn"] = t.struct(
        {
            "updateMask": t.string(),
            "etag": t.string().optional(),
            "partnerPermissions": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
            ),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn"])
    types["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "etag": t.string().optional(),
            "partnerPermissions": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn"] = t.struct(
        {"restrictionType": t.string()}
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn"])
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut"] = t.struct(
        {
            "restrictionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn"] = t.struct(
        {"nextRotationTime": t.string(), "rotationPeriod": t.string()}
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut"] = t.struct(
        {
            "nextRotationTime": t.string(),
            "rotationPeriod": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"] = t.struct(
        {
            "ekmProvisioningState": t.string().optional(),
            "ekmProvisioningErrorDomain": t.string().optional(),
            "ekmProvisioningErrorMapping": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"] = t.struct(
        {
            "ekmProvisioningState": t.string().optional(),
            "ekmProvisioningErrorDomain": t.string().optional(),
            "ekmProvisioningErrorMapping": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"])
    types["GoogleCloudAssuredworkloadsV1ListViolationsResponseIn"] = t.struct(
        {
            "violations": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1ViolationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ListViolationsResponseIn"])
    types["GoogleCloudAssuredworkloadsV1ListViolationsResponseOut"] = t.struct(
        {
            "violations": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1ViolationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ListViolationsResponseOut"])

    functions = {}
    functions["organizationsLocationsOperationsList"] = assuredworkloads.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsGet"] = assuredworkloads.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsWorkloadsMutatePartnerPermissions"
    ] = assuredworkloads.post(
        "v1/{name}:restrictAllowedResources",
        t.struct(
            {
                "name": t.string(),
                "restrictionType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsGet"] = assuredworkloads.post(
        "v1/{name}:restrictAllowedResources",
        t.struct(
            {
                "name": t.string(),
                "restrictionType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsCreate"] = assuredworkloads.post(
        "v1/{name}:restrictAllowedResources",
        t.struct(
            {
                "name": t.string(),
                "restrictionType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsDelete"] = assuredworkloads.post(
        "v1/{name}:restrictAllowedResources",
        t.struct(
            {
                "name": t.string(),
                "restrictionType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsList"] = assuredworkloads.post(
        "v1/{name}:restrictAllowedResources",
        t.struct(
            {
                "name": t.string(),
                "restrictionType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsPatch"] = assuredworkloads.post(
        "v1/{name}:restrictAllowedResources",
        t.struct(
            {
                "name": t.string(),
                "restrictionType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsWorkloadsRestrictAllowedResources"
    ] = assuredworkloads.post(
        "v1/{name}:restrictAllowedResources",
        t.struct(
            {
                "name": t.string(),
                "restrictionType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsWorkloadsViolationsAcknowledge"
    ] = assuredworkloads.get(
        "v1/{parent}/violations",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "interval.endTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "interval.startTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListViolationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsViolationsGet"] = assuredworkloads.get(
        "v1/{parent}/violations",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "interval.endTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "interval.startTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListViolationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsViolationsList"] = assuredworkloads.get(
        "v1/{parent}/violations",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "interval.endTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "interval.startTime": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListViolationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="assuredworkloads",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
