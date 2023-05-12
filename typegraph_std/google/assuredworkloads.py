from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_assuredworkloads() -> Import:
    assuredworkloads = HTTPRuntime("https://assuredworkloads.googleapis.com/")

    renames = {
        "ErrorResponse": "_assuredworkloads_1_ErrorResponse",
        "GoogleLongrunningOperationIn": "_assuredworkloads_2_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_assuredworkloads_3_GoogleLongrunningOperationOut",
        "GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn": "_assuredworkloads_4_GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut": "_assuredworkloads_5_GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn": "_assuredworkloads_6_GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut": "_assuredworkloads_7_GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn": "_assuredworkloads_8_GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut": "_assuredworkloads_9_GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn": "_assuredworkloads_10_GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut": "_assuredworkloads_11_GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut",
        "GoogleCloudAssuredworkloadsV1WorkloadIn": "_assuredworkloads_12_GoogleCloudAssuredworkloadsV1WorkloadIn",
        "GoogleCloudAssuredworkloadsV1WorkloadOut": "_assuredworkloads_13_GoogleCloudAssuredworkloadsV1WorkloadOut",
        "GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn": "_assuredworkloads_14_GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut": "_assuredworkloads_15_GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut",
        "GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn": "_assuredworkloads_16_GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn",
        "GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut": "_assuredworkloads_17_GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn": "_assuredworkloads_18_GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut": "_assuredworkloads_19_GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut",
        "GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn": "_assuredworkloads_20_GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn",
        "GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut": "_assuredworkloads_21_GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut",
        "GoogleLongrunningListOperationsResponseIn": "_assuredworkloads_22_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_assuredworkloads_23_GoogleLongrunningListOperationsResponseOut",
        "GoogleProtobufEmptyIn": "_assuredworkloads_24_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_assuredworkloads_25_GoogleProtobufEmptyOut",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn": "_assuredworkloads_26_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut": "_assuredworkloads_27_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn": "_assuredworkloads_28_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut": "_assuredworkloads_29_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut",
        "GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn": "_assuredworkloads_30_GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn",
        "GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut": "_assuredworkloads_31_GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn": "_assuredworkloads_32_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut": "_assuredworkloads_33_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut",
        "GoogleCloudAssuredworkloadsV1ViolationIn": "_assuredworkloads_34_GoogleCloudAssuredworkloadsV1ViolationIn",
        "GoogleCloudAssuredworkloadsV1ViolationOut": "_assuredworkloads_35_GoogleCloudAssuredworkloadsV1ViolationOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn": "_assuredworkloads_36_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut": "_assuredworkloads_37_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn": "_assuredworkloads_38_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut": "_assuredworkloads_39_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut",
        "GoogleRpcStatusIn": "_assuredworkloads_40_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_assuredworkloads_41_GoogleRpcStatusOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationIn": "_assuredworkloads_42_GoogleCloudAssuredworkloadsV1ViolationRemediationIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationOut": "_assuredworkloads_43_GoogleCloudAssuredworkloadsV1ViolationRemediationOut",
        "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn": "_assuredworkloads_44_GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn",
        "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut": "_assuredworkloads_45_GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut",
        "GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn": "_assuredworkloads_46_GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn",
        "GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut": "_assuredworkloads_47_GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut",
        "GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn": "_assuredworkloads_48_GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn",
        "GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut": "_assuredworkloads_49_GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut",
        "GoogleCloudAssuredworkloadsV1ListViolationsResponseIn": "_assuredworkloads_50_GoogleCloudAssuredworkloadsV1ListViolationsResponseIn",
        "GoogleCloudAssuredworkloadsV1ListViolationsResponseOut": "_assuredworkloads_51_GoogleCloudAssuredworkloadsV1ListViolationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn"] = t.struct(
        {"resourceType": t.string().optional(), "resourceId": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "resourceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut"])
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
            "partner": t.string().optional(),
            "enableSovereignControls": t.boolean().optional(),
            "violationNotificationsEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "provisionedResourcesParent": t.string().optional(),
            "kmsSettings": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn"]
            ).optional(),
            "billingAccount": t.string().optional(),
            "ekmProvisioningResponse": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"
                ]
            ).optional(),
            "complianceRegime": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceSettings": t.array(
                t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"]
                )
            ).optional(),
            "etag": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadOut"] = t.struct(
        {
            "kajEnrollmentState": t.string().optional(),
            "saaEnrollmentResponse": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut"]
            ).optional(),
            "partner": t.string().optional(),
            "enableSovereignControls": t.boolean().optional(),
            "violationNotificationsEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "provisionedResourcesParent": t.string().optional(),
            "kmsSettings": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut"]
            ).optional(),
            "compliantButDisallowedServices": t.array(t.string()).optional(),
            "complianceStatus": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "billingAccount": t.string().optional(),
            "ekmProvisioningResponse": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"
                ]
            ).optional(),
            "complianceRegime": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut"])
            ).optional(),
            "resourceSettings": t.array(
                t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"]
                )
            ).optional(),
            "etag": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"])
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
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn"])
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut"])
    types["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "updateMask": t.string(),
            "partnerPermissions": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
            ),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn"])
    types["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "updateMask": t.string(),
            "partnerPermissions": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn"] = t.struct(
        {"restrictionType": t.string()}
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn"])
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut"] = t.struct(
        {
            "restrictionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut"])
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn"])
    types[
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
    )
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
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn"
    ] = t.struct(
        {
            "consoleUris": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
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
            "consoleUris": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
            "steps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut"
        ]
    )
    types["GoogleCloudAssuredworkloadsV1ViolationIn"] = t.struct(
        {
            "acknowledgementTime": t.string().optional(),
            "acknowledged": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationIn"])
    types["GoogleCloudAssuredworkloadsV1ViolationOut"] = t.struct(
        {
            "description": t.string().optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
            "beginTime": t.string().optional(),
            "remediation": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1ViolationRemediationOut"]
            ).optional(),
            "nonCompliantOrgPolicy": t.string().optional(),
            "auditLogLink": t.string().optional(),
            "name": t.string().optional(),
            "resolveTime": t.string().optional(),
            "acknowledgementTime": t.string().optional(),
            "exceptionAuditLogLink": t.string().optional(),
            "orgPolicyConstraint": t.string().optional(),
            "acknowledged": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
            "instructions": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut"
                ]
            ),
            "remediationType": t.string().optional(),
            "compliantValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationRemediationOut"])
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
    types["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "parent": t.string().optional(),
            "complianceRegime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn"])
    types["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "parent": t.string().optional(),
            "complianceRegime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut"])
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
    functions[
        "organizationsLocationsWorkloadsRestrictAllowedResources"
    ] = assuredworkloads.patch(
        "v1/{name}:mutatePartnerPermissions",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "updateMask": t.string(),
                "partnerPermissions": t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsGet"] = assuredworkloads.patch(
        "v1/{name}:mutatePartnerPermissions",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "updateMask": t.string(),
                "partnerPermissions": t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsPatch"] = assuredworkloads.patch(
        "v1/{name}:mutatePartnerPermissions",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "updateMask": t.string(),
                "partnerPermissions": t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsDelete"] = assuredworkloads.patch(
        "v1/{name}:mutatePartnerPermissions",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "updateMask": t.string(),
                "partnerPermissions": t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsList"] = assuredworkloads.patch(
        "v1/{name}:mutatePartnerPermissions",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "updateMask": t.string(),
                "partnerPermissions": t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsWorkloadsCreate"] = assuredworkloads.patch(
        "v1/{name}:mutatePartnerPermissions",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "updateMask": t.string(),
                "partnerPermissions": t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsWorkloadsMutatePartnerPermissions"
    ] = assuredworkloads.patch(
        "v1/{name}:mutatePartnerPermissions",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "updateMask": t.string(),
                "partnerPermissions": t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsWorkloadsViolationsAcknowledge"
    ] = assuredworkloads.get(
        "v1/{parent}/violations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "interval.endTime": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "interval.endTime": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "interval.startTime": t.string().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "interval.endTime": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListViolationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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

    return Import(
        importer="assuredworkloads",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
