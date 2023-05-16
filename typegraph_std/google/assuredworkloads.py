from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_assuredworkloads() -> Import:
    assuredworkloads = HTTPRuntime("https://assuredworkloads.googleapis.com/")

    renames = {
        "ErrorResponse": "_assuredworkloads_1_ErrorResponse",
        "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn": "_assuredworkloads_2_GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn",
        "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut": "_assuredworkloads_3_GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut",
        "GoogleCloudAssuredworkloadsV1WorkloadIn": "_assuredworkloads_4_GoogleCloudAssuredworkloadsV1WorkloadIn",
        "GoogleCloudAssuredworkloadsV1WorkloadOut": "_assuredworkloads_5_GoogleCloudAssuredworkloadsV1WorkloadOut",
        "GoogleCloudAssuredworkloadsV1ViolationIn": "_assuredworkloads_6_GoogleCloudAssuredworkloadsV1ViolationIn",
        "GoogleCloudAssuredworkloadsV1ViolationOut": "_assuredworkloads_7_GoogleCloudAssuredworkloadsV1ViolationOut",
        "GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn": "_assuredworkloads_8_GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut": "_assuredworkloads_9_GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationIn": "_assuredworkloads_10_GoogleCloudAssuredworkloadsV1ViolationRemediationIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationOut": "_assuredworkloads_11_GoogleCloudAssuredworkloadsV1ViolationRemediationOut",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn": "_assuredworkloads_12_GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut": "_assuredworkloads_13_GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut",
        "GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn": "_assuredworkloads_14_GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut": "_assuredworkloads_15_GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut",
        "GoogleLongrunningListOperationsResponseIn": "_assuredworkloads_16_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_assuredworkloads_17_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn": "_assuredworkloads_18_GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn",
        "GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut": "_assuredworkloads_19_GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn": "_assuredworkloads_20_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut": "_assuredworkloads_21_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn": "_assuredworkloads_22_GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut": "_assuredworkloads_23_GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut",
        "GoogleCloudAssuredworkloadsV1ListViolationsResponseIn": "_assuredworkloads_24_GoogleCloudAssuredworkloadsV1ListViolationsResponseIn",
        "GoogleCloudAssuredworkloadsV1ListViolationsResponseOut": "_assuredworkloads_25_GoogleCloudAssuredworkloadsV1ListViolationsResponseOut",
        "GoogleProtobufEmptyIn": "_assuredworkloads_26_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_assuredworkloads_27_GoogleProtobufEmptyOut",
        "GoogleLongrunningOperationIn": "_assuredworkloads_28_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_assuredworkloads_29_GoogleLongrunningOperationOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn": "_assuredworkloads_30_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut": "_assuredworkloads_31_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut",
        "GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn": "_assuredworkloads_32_GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn",
        "GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut": "_assuredworkloads_33_GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut",
        "GoogleRpcStatusIn": "_assuredworkloads_34_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_assuredworkloads_35_GoogleRpcStatusOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn": "_assuredworkloads_36_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut": "_assuredworkloads_37_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn": "_assuredworkloads_38_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut": "_assuredworkloads_39_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn": "_assuredworkloads_40_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut": "_assuredworkloads_41_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn": "_assuredworkloads_42_GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut": "_assuredworkloads_43_GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut",
        "GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn": "_assuredworkloads_44_GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn",
        "GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut": "_assuredworkloads_45_GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut",
        "GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn": "_assuredworkloads_46_GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn",
        "GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut": "_assuredworkloads_47_GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn": "_assuredworkloads_48_GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut": "_assuredworkloads_49_GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut",
        "GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn": "_assuredworkloads_50_GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn",
        "GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut": "_assuredworkloads_51_GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"] = t.struct(
        {
            "ekmProvisioningState": t.string().optional(),
            "ekmProvisioningErrorMapping": t.string().optional(),
            "ekmProvisioningErrorDomain": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"] = t.struct(
        {
            "ekmProvisioningState": t.string().optional(),
            "ekmProvisioningErrorMapping": t.string().optional(),
            "ekmProvisioningErrorDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadIn"] = t.struct(
        {
            "partner": t.string().optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceSettings": t.array(
                t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"]
                )
            ).optional(),
            "kmsSettings": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn"]
            ).optional(),
            "complianceRegime": t.string(),
            "billingAccount": t.string().optional(),
            "enableSovereignControls": t.boolean().optional(),
            "etag": t.string().optional(),
            "violationNotificationsEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "ekmProvisioningResponse": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"
                ]
            ).optional(),
            "provisionedResourcesParent": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadOut"] = t.struct(
        {
            "partner": t.string().optional(),
            "displayName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceSettings": t.array(
                t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"]
                )
            ).optional(),
            "kajEnrollmentState": t.string().optional(),
            "kmsSettings": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut"]
            ).optional(),
            "saaEnrollmentResponse": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut"]
            ).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut"])
            ).optional(),
            "complianceRegime": t.string(),
            "billingAccount": t.string().optional(),
            "enableSovereignControls": t.boolean().optional(),
            "etag": t.string().optional(),
            "violationNotificationsEnabled": t.boolean().optional(),
            "compliantButDisallowedServices": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "ekmProvisioningResponse": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"
                ]
            ).optional(),
            "provisionedResourcesParent": t.string().optional(),
            "createTime": t.string().optional(),
            "complianceStatus": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"])
    types["GoogleCloudAssuredworkloadsV1ViolationIn"] = t.struct(
        {
            "acknowledged": t.boolean().optional(),
            "acknowledgementTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationIn"])
    types["GoogleCloudAssuredworkloadsV1ViolationOut"] = t.struct(
        {
            "exceptionAuditLogLink": t.string().optional(),
            "nonCompliantOrgPolicy": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "beginTime": t.string().optional(),
            "orgPolicyConstraint": t.string().optional(),
            "auditLogLink": t.string().optional(),
            "resolveTime": t.string().optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
            "acknowledged": t.boolean().optional(),
            "remediation": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1ViolationRemediationOut"]
            ).optional(),
            "acknowledgementTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationOut"])
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
    types["GoogleCloudAssuredworkloadsV1ViolationRemediationIn"] = t.struct(
        {
            "instructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn"
                ]
            ),
            "compliantValues": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationRemediationIn"])
    types["GoogleCloudAssuredworkloadsV1ViolationRemediationOut"] = t.struct(
        {
            "remediationType": t.string().optional(),
            "instructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut"
                ]
            ),
            "compliantValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationRemediationOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "resourceId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "resourceId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"] = t.struct(
        {
            "dataLogsViewer": t.boolean().optional(),
            "serviceAccessApprover": t.boolean().optional(),
            "remediateFolderViolations": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"] = t.struct(
        {
            "dataLogsViewer": t.boolean().optional(),
            "serviceAccessApprover": t.boolean().optional(),
            "remediateFolderViolations": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"])
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
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn"] = t.struct(
        {"restrictionType": t.string()}
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn"])
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut"] = t.struct(
        {
            "restrictionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut"])
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn"])
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn"
    ] = t.struct(
        {
            "steps": t.array(t.string()).optional(),
            "gcloudCommands": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
        }
    ).named(
        renames["GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn"]
    )
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut"
    ] = t.struct(
        {
            "steps": t.array(t.string()).optional(),
            "gcloudCommands": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut"
        ]
    )
    types["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn"] = t.struct(
        {
            "complianceRegime": t.string().optional(),
            "parent": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn"])
    types["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut"] = t.struct(
        {
            "complianceRegime": t.string().optional(),
            "parent": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn"
    ] = t.struct(
        {
            "consoleUris": t.array(t.string()).optional(),
            "steps": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
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
            "consoleUris": t.array(t.string()).optional(),
            "steps": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut"
        ]
    )
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn"])
    types[
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
    )
    types["GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn"] = t.struct(
        {
            "consoleInstructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn"
                ]
            ).optional(),
            "gcloudInstructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn"
                ]
            ).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn"])
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut"
    ] = t.struct(
        {
            "consoleInstructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut"
                ]
            ).optional(),
            "gcloudInstructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut"]
    )
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn"] = t.struct(
        {"nonCompliantOrgPolicy": t.string().optional(), "comment": t.string()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn"])
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut"] = t.struct(
        {
            "nonCompliantOrgPolicy": t.string().optional(),
            "comment": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn"] = t.struct(
        {
            "setupStatus": t.string().optional(),
            "setupErrors": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut"] = t.struct(
        {
            "setupStatus": t.string().optional(),
            "setupErrors": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut"])
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

    functions = {}
    functions[
        "organizationsLocationsWorkloadsRestrictAllowedResources"
    ] = assuredworkloads.get(
        "v1/{parent}/workloads",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsDelete"] = assuredworkloads.get(
        "v1/{parent}/workloads",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsGet"] = assuredworkloads.get(
        "v1/{parent}/workloads",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsPatch"] = assuredworkloads.get(
        "v1/{parent}/workloads",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsCreate"] = assuredworkloads.get(
        "v1/{parent}/workloads",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsWorkloadsMutatePartnerPermissions"
    ] = assuredworkloads.get(
        "v1/{parent}/workloads",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsList"] = assuredworkloads.get(
        "v1/{parent}/workloads",
        t.struct(
            {
                "filter": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsViolationsList"] = assuredworkloads.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ViolationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsWorkloadsViolationsAcknowledge"
    ] = assuredworkloads.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ViolationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsViolationsGet"] = assuredworkloads.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ViolationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsGet"] = assuredworkloads.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsList"] = assuredworkloads.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="assuredworkloads",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
