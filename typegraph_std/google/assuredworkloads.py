from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_assuredworkloads() -> Import:
    assuredworkloads = HTTPRuntime("https://assuredworkloads.googleapis.com/")

    renames = {
        "ErrorResponse": "_assuredworkloads_1_ErrorResponse",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn": "_assuredworkloads_2_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut": "_assuredworkloads_3_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsOut",
        "GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn": "_assuredworkloads_4_GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn",
        "GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut": "_assuredworkloads_5_GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn": "_assuredworkloads_6_GoogleCloudAssuredworkloadsV1WorkloadResourceInfoIn",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut": "_assuredworkloads_7_GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut",
        "GoogleProtobufEmptyIn": "_assuredworkloads_8_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_assuredworkloads_9_GoogleProtobufEmptyOut",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn": "_assuredworkloads_10_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestIn",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut": "_assuredworkloads_11_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequestOut",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn": "_assuredworkloads_12_GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestIn",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut": "_assuredworkloads_13_GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequestOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn": "_assuredworkloads_14_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut": "_assuredworkloads_15_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsoleOut",
        "GoogleRpcStatusIn": "_assuredworkloads_16_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_assuredworkloads_17_GoogleRpcStatusOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationIn": "_assuredworkloads_18_GoogleCloudAssuredworkloadsV1ViolationRemediationIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationOut": "_assuredworkloads_19_GoogleCloudAssuredworkloadsV1ViolationRemediationOut",
        "GoogleLongrunningListOperationsResponseIn": "_assuredworkloads_20_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_assuredworkloads_21_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn": "_assuredworkloads_22_GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut": "_assuredworkloads_23_GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn": "_assuredworkloads_24_GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn",
        "GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut": "_assuredworkloads_25_GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut",
        "GoogleCloudAssuredworkloadsV1ViolationIn": "_assuredworkloads_26_GoogleCloudAssuredworkloadsV1ViolationIn",
        "GoogleCloudAssuredworkloadsV1ViolationOut": "_assuredworkloads_27_GoogleCloudAssuredworkloadsV1ViolationOut",
        "GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn": "_assuredworkloads_28_GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataIn",
        "GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut": "_assuredworkloads_29_GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadataOut",
        "GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn": "_assuredworkloads_30_GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn",
        "GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut": "_assuredworkloads_31_GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut",
        "GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn": "_assuredworkloads_32_GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut": "_assuredworkloads_33_GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut",
        "GoogleCloudAssuredworkloadsV1WorkloadIn": "_assuredworkloads_34_GoogleCloudAssuredworkloadsV1WorkloadIn",
        "GoogleCloudAssuredworkloadsV1WorkloadOut": "_assuredworkloads_35_GoogleCloudAssuredworkloadsV1WorkloadOut",
        "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn": "_assuredworkloads_36_GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn",
        "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut": "_assuredworkloads_37_GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut",
        "GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn": "_assuredworkloads_38_GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseIn",
        "GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut": "_assuredworkloads_39_GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn": "_assuredworkloads_40_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn",
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut": "_assuredworkloads_41_GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut",
        "GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn": "_assuredworkloads_42_GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn",
        "GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut": "_assuredworkloads_43_GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut",
        "GoogleLongrunningOperationIn": "_assuredworkloads_44_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_assuredworkloads_45_GoogleLongrunningOperationOut",
        "GoogleCloudAssuredworkloadsV1ListViolationsResponseIn": "_assuredworkloads_46_GoogleCloudAssuredworkloadsV1ListViolationsResponseIn",
        "GoogleCloudAssuredworkloadsV1ListViolationsResponseOut": "_assuredworkloads_47_GoogleCloudAssuredworkloadsV1ListViolationsResponseOut",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn": "_assuredworkloads_48_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn",
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut": "_assuredworkloads_49_GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut",
        "GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn": "_assuredworkloads_50_GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn",
        "GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut": "_assuredworkloads_51_GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "partnerPermissions": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"]
            ),
            "updateMask": t.string(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestIn"])
    types["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "partnerPermissions": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"]
            ),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequestOut"])
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
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
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"] = t.struct(
        {
            "resourceId": t.string().optional(),
            "displayName": t.string().optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"] = t.struct(
        {
            "resourceId": t.string().optional(),
            "displayName": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"])
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseIn"])
    types["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponseOut"])
    types["GoogleCloudAssuredworkloadsV1ViolationIn"] = t.struct(
        {
            "acknowledgementTime": t.string().optional(),
            "acknowledged": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationIn"])
    types["GoogleCloudAssuredworkloadsV1ViolationOut"] = t.struct(
        {
            "category": t.string().optional(),
            "exceptionAuditLogLink": t.string().optional(),
            "orgPolicyConstraint": t.string().optional(),
            "acknowledgementTime": t.string().optional(),
            "nonCompliantOrgPolicy": t.string().optional(),
            "beginTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "resolveTime": t.string().optional(),
            "acknowledged": t.boolean().optional(),
            "description": t.string().optional(),
            "auditLogLink": t.string().optional(),
            "remediation": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1ViolationRemediationOut"]
            ).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ViolationOut"])
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
    types["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn"] = t.struct(
        {
            "workloads": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseIn"])
    types["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"] = t.struct(
        {
            "workloads": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"] = t.struct(
        {
            "serviceAccessApprover": t.boolean().optional(),
            "dataLogsViewer": t.boolean().optional(),
            "remediateFolderViolations": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"] = t.struct(
        {
            "serviceAccessApprover": t.boolean().optional(),
            "dataLogsViewer": t.boolean().optional(),
            "remediateFolderViolations": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissionsOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadIn"] = t.struct(
        {
            "complianceRegime": t.string(),
            "etag": t.string().optional(),
            "billingAccount": t.string().optional(),
            "name": t.string().optional(),
            "resourceSettings": t.array(
                t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsIn"]
                )
            ).optional(),
            "displayName": t.string(),
            "partner": t.string().optional(),
            "provisionedResourcesParent": t.string().optional(),
            "violationNotificationsEnabled": t.boolean().optional(),
            "ekmProvisioningResponse": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"
                ]
            ).optional(),
            "kmsSettings": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn"]
            ).optional(),
            "enableSovereignControls": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadOut"] = t.struct(
        {
            "complianceRegime": t.string(),
            "etag": t.string().optional(),
            "billingAccount": t.string().optional(),
            "createTime": t.string().optional(),
            "saaEnrollmentResponse": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponseOut"]
            ).optional(),
            "name": t.string().optional(),
            "complianceStatus": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut"]
            ).optional(),
            "resourceSettings": t.array(
                t.proxy(
                    renames["GoogleCloudAssuredworkloadsV1WorkloadResourceSettingsOut"]
                )
            ).optional(),
            "displayName": t.string(),
            "partner": t.string().optional(),
            "provisionedResourcesParent": t.string().optional(),
            "violationNotificationsEnabled": t.boolean().optional(),
            "ekmProvisioningResponse": t.proxy(
                renames[
                    "GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"
                ]
            ).optional(),
            "kmsSettings": t.proxy(
                renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut"]
            ).optional(),
            "kajEnrollmentState": t.string().optional(),
            "enableSovereignControls": t.boolean().optional(),
            "compliantButDisallowedServices": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resources": t.array(
                t.proxy(renames["GoogleCloudAssuredworkloadsV1WorkloadResourceInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadOut"])
    types["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"] = t.struct(
        {
            "ekmProvisioningErrorMapping": t.string().optional(),
            "ekmProvisioningErrorDomain": t.string().optional(),
            "ekmProvisioningState": t.string().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"] = t.struct(
        {
            "ekmProvisioningErrorMapping": t.string().optional(),
            "ekmProvisioningErrorDomain": t.string().optional(),
            "ekmProvisioningState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponseOut"])
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
    types["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseIn"])
    types[
        "GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponseOut"]
    )
    types["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn"] = t.struct(
        {"rotationPeriod": t.string(), "nextRotationTime": t.string()}
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut"] = t.struct(
        {
            "rotationPeriod": t.string(),
            "nextRotationTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadKMSSettingsOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn"
    ] = t.struct(
        {
            "gcloudCommands": t.array(t.string()).optional(),
            "steps": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
        }
    ).named(
        renames["GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudIn"]
    )
    types[
        "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut"
    ] = t.struct(
        {
            "gcloudCommands": t.array(t.string()).optional(),
            "steps": t.array(t.string()).optional(),
            "additionalLinks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloudOut"
        ]
    )
    types["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn"] = t.struct(
        {
            "activeViolationCount": t.integer().optional(),
            "acknowledgedViolationCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusIn"])
    types["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut"] = t.struct(
        {
            "activeViolationCount": t.integer().optional(),
            "acknowledgedViolationCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudAssuredworkloadsV1WorkloadComplianceStatusOut"])

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
    functions["organizationsLocationsWorkloadsGet"] = assuredworkloads.get(
        "v1/{parent}/workloads",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsWorkloadsRestrictAllowedResources"
    ] = assuredworkloads.get(
        "v1/{parent}/workloads",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudAssuredworkloadsV1ListWorkloadsResponseOut"]),
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
    functions["organizationsLocationsWorkloadsViolationsList"] = assuredworkloads.get(
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

    return Import(
        importer="assuredworkloads", renames=renames, types=types, functions=functions
    )
