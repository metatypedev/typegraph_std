from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_prod_tt_sasportal():
    prod_tt_sasportal = HTTPRuntime("https://prod-tt-sasportal.googleapis.com/")

    renames = {
        "ErrorResponse": "_prod_tt_sasportal_1_ErrorResponse",
        "SasPortalChannelWithScoreIn": "_prod_tt_sasportal_2_SasPortalChannelWithScoreIn",
        "SasPortalChannelWithScoreOut": "_prod_tt_sasportal_3_SasPortalChannelWithScoreOut",
        "SasPortalListDevicesResponseIn": "_prod_tt_sasportal_4_SasPortalListDevicesResponseIn",
        "SasPortalListDevicesResponseOut": "_prod_tt_sasportal_5_SasPortalListDevicesResponseOut",
        "SasPortalTestPermissionsResponseIn": "_prod_tt_sasportal_6_SasPortalTestPermissionsResponseIn",
        "SasPortalTestPermissionsResponseOut": "_prod_tt_sasportal_7_SasPortalTestPermissionsResponseOut",
        "SasPortalDeploymentAssociationIn": "_prod_tt_sasportal_8_SasPortalDeploymentAssociationIn",
        "SasPortalDeploymentAssociationOut": "_prod_tt_sasportal_9_SasPortalDeploymentAssociationOut",
        "SasPortalGetPolicyRequestIn": "_prod_tt_sasportal_10_SasPortalGetPolicyRequestIn",
        "SasPortalGetPolicyRequestOut": "_prod_tt_sasportal_11_SasPortalGetPolicyRequestOut",
        "SasPortalTestPermissionsRequestIn": "_prod_tt_sasportal_12_SasPortalTestPermissionsRequestIn",
        "SasPortalTestPermissionsRequestOut": "_prod_tt_sasportal_13_SasPortalTestPermissionsRequestOut",
        "SasPortalDpaMoveListIn": "_prod_tt_sasportal_14_SasPortalDpaMoveListIn",
        "SasPortalDpaMoveListOut": "_prod_tt_sasportal_15_SasPortalDpaMoveListOut",
        "SasPortalPolicyIn": "_prod_tt_sasportal_16_SasPortalPolicyIn",
        "SasPortalPolicyOut": "_prod_tt_sasportal_17_SasPortalPolicyOut",
        "SasPortalSignDeviceRequestIn": "_prod_tt_sasportal_18_SasPortalSignDeviceRequestIn",
        "SasPortalSignDeviceRequestOut": "_prod_tt_sasportal_19_SasPortalSignDeviceRequestOut",
        "SasPortalNodeIn": "_prod_tt_sasportal_20_SasPortalNodeIn",
        "SasPortalNodeOut": "_prod_tt_sasportal_21_SasPortalNodeOut",
        "SasPortalProvisionDeploymentResponseIn": "_prod_tt_sasportal_22_SasPortalProvisionDeploymentResponseIn",
        "SasPortalProvisionDeploymentResponseOut": "_prod_tt_sasportal_23_SasPortalProvisionDeploymentResponseOut",
        "SasPortalGenerateSecretRequestIn": "_prod_tt_sasportal_24_SasPortalGenerateSecretRequestIn",
        "SasPortalGenerateSecretRequestOut": "_prod_tt_sasportal_25_SasPortalGenerateSecretRequestOut",
        "SasPortalDeviceIn": "_prod_tt_sasportal_26_SasPortalDeviceIn",
        "SasPortalDeviceOut": "_prod_tt_sasportal_27_SasPortalDeviceOut",
        "SasPortalCustomerIn": "_prod_tt_sasportal_28_SasPortalCustomerIn",
        "SasPortalCustomerOut": "_prod_tt_sasportal_29_SasPortalCustomerOut",
        "SasPortalListNodesResponseIn": "_prod_tt_sasportal_30_SasPortalListNodesResponseIn",
        "SasPortalListNodesResponseOut": "_prod_tt_sasportal_31_SasPortalListNodesResponseOut",
        "SasPortalDeviceModelIn": "_prod_tt_sasportal_32_SasPortalDeviceModelIn",
        "SasPortalDeviceModelOut": "_prod_tt_sasportal_33_SasPortalDeviceModelOut",
        "SasPortalFrequencyRangeIn": "_prod_tt_sasportal_34_SasPortalFrequencyRangeIn",
        "SasPortalFrequencyRangeOut": "_prod_tt_sasportal_35_SasPortalFrequencyRangeOut",
        "SasPortalAssignmentIn": "_prod_tt_sasportal_36_SasPortalAssignmentIn",
        "SasPortalAssignmentOut": "_prod_tt_sasportal_37_SasPortalAssignmentOut",
        "SasPortalDeviceConfigIn": "_prod_tt_sasportal_38_SasPortalDeviceConfigIn",
        "SasPortalDeviceConfigOut": "_prod_tt_sasportal_39_SasPortalDeviceConfigOut",
        "SasPortalCheckHasProvisionedDeploymentResponseIn": "_prod_tt_sasportal_40_SasPortalCheckHasProvisionedDeploymentResponseIn",
        "SasPortalCheckHasProvisionedDeploymentResponseOut": "_prod_tt_sasportal_41_SasPortalCheckHasProvisionedDeploymentResponseOut",
        "SasPortalProvisionDeploymentRequestIn": "_prod_tt_sasportal_42_SasPortalProvisionDeploymentRequestIn",
        "SasPortalProvisionDeploymentRequestOut": "_prod_tt_sasportal_43_SasPortalProvisionDeploymentRequestOut",
        "SasPortalCreateSignedDeviceRequestIn": "_prod_tt_sasportal_44_SasPortalCreateSignedDeviceRequestIn",
        "SasPortalCreateSignedDeviceRequestOut": "_prod_tt_sasportal_45_SasPortalCreateSignedDeviceRequestOut",
        "SasPortalDeviceMetadataIn": "_prod_tt_sasportal_46_SasPortalDeviceMetadataIn",
        "SasPortalDeviceMetadataOut": "_prod_tt_sasportal_47_SasPortalDeviceMetadataOut",
        "SasPortalMigrateOrganizationResponseIn": "_prod_tt_sasportal_48_SasPortalMigrateOrganizationResponseIn",
        "SasPortalMigrateOrganizationResponseOut": "_prod_tt_sasportal_49_SasPortalMigrateOrganizationResponseOut",
        "SasPortalNrqzValidationIn": "_prod_tt_sasportal_50_SasPortalNrqzValidationIn",
        "SasPortalNrqzValidationOut": "_prod_tt_sasportal_51_SasPortalNrqzValidationOut",
        "SasPortalValidateInstallerResponseIn": "_prod_tt_sasportal_52_SasPortalValidateInstallerResponseIn",
        "SasPortalValidateInstallerResponseOut": "_prod_tt_sasportal_53_SasPortalValidateInstallerResponseOut",
        "SasPortalUpdateSignedDeviceRequestIn": "_prod_tt_sasportal_54_SasPortalUpdateSignedDeviceRequestIn",
        "SasPortalUpdateSignedDeviceRequestOut": "_prod_tt_sasportal_55_SasPortalUpdateSignedDeviceRequestOut",
        "SasPortalListCustomersResponseIn": "_prod_tt_sasportal_56_SasPortalListCustomersResponseIn",
        "SasPortalListCustomersResponseOut": "_prod_tt_sasportal_57_SasPortalListCustomersResponseOut",
        "SasPortalMigrateOrganizationRequestIn": "_prod_tt_sasportal_58_SasPortalMigrateOrganizationRequestIn",
        "SasPortalMigrateOrganizationRequestOut": "_prod_tt_sasportal_59_SasPortalMigrateOrganizationRequestOut",
        "SasPortalMoveDeviceRequestIn": "_prod_tt_sasportal_60_SasPortalMoveDeviceRequestIn",
        "SasPortalMoveDeviceRequestOut": "_prod_tt_sasportal_61_SasPortalMoveDeviceRequestOut",
        "SasPortalMoveNodeRequestIn": "_prod_tt_sasportal_62_SasPortalMoveNodeRequestIn",
        "SasPortalMoveNodeRequestOut": "_prod_tt_sasportal_63_SasPortalMoveNodeRequestOut",
        "SasPortalInstallationParamsIn": "_prod_tt_sasportal_64_SasPortalInstallationParamsIn",
        "SasPortalInstallationParamsOut": "_prod_tt_sasportal_65_SasPortalInstallationParamsOut",
        "SasPortalSetPolicyRequestIn": "_prod_tt_sasportal_66_SasPortalSetPolicyRequestIn",
        "SasPortalSetPolicyRequestOut": "_prod_tt_sasportal_67_SasPortalSetPolicyRequestOut",
        "SasPortalOperationIn": "_prod_tt_sasportal_68_SasPortalOperationIn",
        "SasPortalOperationOut": "_prod_tt_sasportal_69_SasPortalOperationOut",
        "SasPortalDeviceGrantIn": "_prod_tt_sasportal_70_SasPortalDeviceGrantIn",
        "SasPortalDeviceGrantOut": "_prod_tt_sasportal_71_SasPortalDeviceGrantOut",
        "SasPortalListDeploymentsResponseIn": "_prod_tt_sasportal_72_SasPortalListDeploymentsResponseIn",
        "SasPortalListDeploymentsResponseOut": "_prod_tt_sasportal_73_SasPortalListDeploymentsResponseOut",
        "SasPortalValidateInstallerRequestIn": "_prod_tt_sasportal_74_SasPortalValidateInstallerRequestIn",
        "SasPortalValidateInstallerRequestOut": "_prod_tt_sasportal_75_SasPortalValidateInstallerRequestOut",
        "SasPortalMoveDeploymentRequestIn": "_prod_tt_sasportal_76_SasPortalMoveDeploymentRequestIn",
        "SasPortalMoveDeploymentRequestOut": "_prod_tt_sasportal_77_SasPortalMoveDeploymentRequestOut",
        "SasPortalStatusIn": "_prod_tt_sasportal_78_SasPortalStatusIn",
        "SasPortalStatusOut": "_prod_tt_sasportal_79_SasPortalStatusOut",
        "SasPortalMigrateOrganizationMetadataIn": "_prod_tt_sasportal_80_SasPortalMigrateOrganizationMetadataIn",
        "SasPortalMigrateOrganizationMetadataOut": "_prod_tt_sasportal_81_SasPortalMigrateOrganizationMetadataOut",
        "SasPortalEmptyIn": "_prod_tt_sasportal_82_SasPortalEmptyIn",
        "SasPortalEmptyOut": "_prod_tt_sasportal_83_SasPortalEmptyOut",
        "SasPortalGenerateSecretResponseIn": "_prod_tt_sasportal_84_SasPortalGenerateSecretResponseIn",
        "SasPortalGenerateSecretResponseOut": "_prod_tt_sasportal_85_SasPortalGenerateSecretResponseOut",
        "SasPortalDeploymentIn": "_prod_tt_sasportal_86_SasPortalDeploymentIn",
        "SasPortalDeploymentOut": "_prod_tt_sasportal_87_SasPortalDeploymentOut",
        "SasPortalDeviceAirInterfaceIn": "_prod_tt_sasportal_88_SasPortalDeviceAirInterfaceIn",
        "SasPortalDeviceAirInterfaceOut": "_prod_tt_sasportal_89_SasPortalDeviceAirInterfaceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SasPortalChannelWithScoreIn"] = t.struct(
        {
            "score": t.number().optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
        }
    ).named(renames["SasPortalChannelWithScoreIn"])
    types["SasPortalChannelWithScoreOut"] = t.struct(
        {
            "score": t.number().optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalChannelWithScoreOut"])
    types["SasPortalListDevicesResponseIn"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["SasPortalDeviceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SasPortalListDevicesResponseIn"])
    types["SasPortalListDevicesResponseOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["SasPortalDeviceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalListDevicesResponseOut"])
    types["SasPortalTestPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["SasPortalTestPermissionsResponseIn"])
    types["SasPortalTestPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalTestPermissionsResponseOut"])
    types["SasPortalDeploymentAssociationIn"] = t.struct(
        {"gcpProjectId": t.string().optional(), "userId": t.string().optional()}
    ).named(renames["SasPortalDeploymentAssociationIn"])
    types["SasPortalDeploymentAssociationOut"] = t.struct(
        {
            "gcpProjectId": t.string().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeploymentAssociationOut"])
    types["SasPortalGetPolicyRequestIn"] = t.struct({"resource": t.string()}).named(
        renames["SasPortalGetPolicyRequestIn"]
    )
    types["SasPortalGetPolicyRequestOut"] = t.struct(
        {"resource": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGetPolicyRequestOut"])
    types["SasPortalTestPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional(), "resource": t.string()}
    ).named(renames["SasPortalTestPermissionsRequestIn"])
    types["SasPortalTestPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "resource": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalTestPermissionsRequestOut"])
    types["SasPortalDpaMoveListIn"] = t.struct(
        {
            "dpaId": t.string().optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
        }
    ).named(renames["SasPortalDpaMoveListIn"])
    types["SasPortalDpaMoveListOut"] = t.struct(
        {
            "dpaId": t.string().optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDpaMoveListOut"])
    types["SasPortalPolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "assignments": t.array(
                t.proxy(renames["SasPortalAssignmentIn"])
            ).optional(),
        }
    ).named(renames["SasPortalPolicyIn"])
    types["SasPortalPolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "assignments": t.array(
                t.proxy(renames["SasPortalAssignmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalPolicyOut"])
    types["SasPortalSignDeviceRequestIn"] = t.struct(
        {"device": t.proxy(renames["SasPortalDeviceIn"])}
    ).named(renames["SasPortalSignDeviceRequestIn"])
    types["SasPortalSignDeviceRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["SasPortalDeviceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSignDeviceRequestOut"])
    types["SasPortalNodeIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SasPortalNodeIn"])
    types["SasPortalNodeOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalNodeOut"])
    types["SasPortalProvisionDeploymentResponseIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["SasPortalProvisionDeploymentResponseIn"])
    types["SasPortalProvisionDeploymentResponseOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentResponseOut"])
    types["SasPortalGenerateSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretRequestIn"])
    types["SasPortalGenerateSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGenerateSecretRequestOut"])
    types["SasPortalDeviceIn"] = t.struct(
        {
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantIn"])).optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataIn"]).optional(),
            "name": t.string().optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "state": t.string().optional(),
            "fccId": t.string().optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "serialNumber": t.string().optional(),
            "displayName": t.string().optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeIn"])
            ).optional(),
        }
    ).named(renames["SasPortalDeviceIn"])
    types["SasPortalDeviceOut"] = t.struct(
        {
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantOut"])).optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataOut"]).optional(),
            "name": t.string().optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "state": t.string().optional(),
            "fccId": t.string().optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "serialNumber": t.string().optional(),
            "displayName": t.string().optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeOut"])
            ).optional(),
            "currentChannels": t.array(
                t.proxy(renames["SasPortalChannelWithScoreOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceOut"])
    types["SasPortalCustomerIn"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
        }
    ).named(renames["SasPortalCustomerIn"])
    types["SasPortalCustomerOut"] = t.struct(
        {
            "displayName": t.string(),
            "name": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalCustomerOut"])
    types["SasPortalListNodesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "nodes": t.array(t.proxy(renames["SasPortalNodeIn"])).optional(),
        }
    ).named(renames["SasPortalListNodesResponseIn"])
    types["SasPortalListNodesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "nodes": t.array(t.proxy(renames["SasPortalNodeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalListNodesResponseOut"])
    types["SasPortalDeviceModelIn"] = t.struct(
        {
            "vendor": t.string().optional(),
            "softwareVersion": t.string().optional(),
            "firmwareVersion": t.string().optional(),
            "name": t.string().optional(),
            "hardwareVersion": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceModelIn"])
    types["SasPortalDeviceModelOut"] = t.struct(
        {
            "vendor": t.string().optional(),
            "softwareVersion": t.string().optional(),
            "firmwareVersion": t.string().optional(),
            "name": t.string().optional(),
            "hardwareVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceModelOut"])
    types["SasPortalFrequencyRangeIn"] = t.struct(
        {
            "highFrequencyMhz": t.number().optional(),
            "lowFrequencyMhz": t.number().optional(),
        }
    ).named(renames["SasPortalFrequencyRangeIn"])
    types["SasPortalFrequencyRangeOut"] = t.struct(
        {
            "highFrequencyMhz": t.number().optional(),
            "lowFrequencyMhz": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalFrequencyRangeOut"])
    types["SasPortalAssignmentIn"] = t.struct(
        {"members": t.array(t.string()).optional(), "role": t.string()}
    ).named(renames["SasPortalAssignmentIn"])
    types["SasPortalAssignmentOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalAssignmentOut"])
    types["SasPortalDeviceConfigIn"] = t.struct(
        {
            "callSign": t.string().optional(),
            "updateTime": t.string().optional(),
            "measurementCapabilities": t.array(t.string()).optional(),
            "isSigned": t.boolean().optional(),
            "category": t.string().optional(),
            "model": t.proxy(renames["SasPortalDeviceModelIn"]).optional(),
            "state": t.string().optional(),
            "userId": t.string().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceIn"]
            ).optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsIn"]
            ).optional(),
        }
    ).named(renames["SasPortalDeviceConfigIn"])
    types["SasPortalDeviceConfigOut"] = t.struct(
        {
            "callSign": t.string().optional(),
            "updateTime": t.string().optional(),
            "measurementCapabilities": t.array(t.string()).optional(),
            "isSigned": t.boolean().optional(),
            "category": t.string().optional(),
            "model": t.proxy(renames["SasPortalDeviceModelOut"]).optional(),
            "state": t.string().optional(),
            "userId": t.string().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceOut"]
            ).optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceConfigOut"])
    types["SasPortalCheckHasProvisionedDeploymentResponseIn"] = t.struct(
        {"hasProvisionedDeployment": t.boolean().optional()}
    ).named(renames["SasPortalCheckHasProvisionedDeploymentResponseIn"])
    types["SasPortalCheckHasProvisionedDeploymentResponseOut"] = t.struct(
        {
            "hasProvisionedDeployment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalCheckHasProvisionedDeploymentResponseOut"])
    types["SasPortalProvisionDeploymentRequestIn"] = t.struct(
        {
            "organizationId": t.string().optional(),
            "newOrganizationDisplayName": t.string().optional(),
            "newDeploymentDisplayName": t.string().optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentRequestIn"])
    types["SasPortalProvisionDeploymentRequestOut"] = t.struct(
        {
            "organizationId": t.string().optional(),
            "newOrganizationDisplayName": t.string().optional(),
            "newDeploymentDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentRequestOut"])
    types["SasPortalCreateSignedDeviceRequestIn"] = t.struct(
        {"installerId": t.string(), "encodedDevice": t.string()}
    ).named(renames["SasPortalCreateSignedDeviceRequestIn"])
    types["SasPortalCreateSignedDeviceRequestOut"] = t.struct(
        {
            "installerId": t.string(),
            "encodedDevice": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalCreateSignedDeviceRequestOut"])
    types["SasPortalDeviceMetadataIn"] = t.struct(
        {
            "antennaModel": t.string().optional(),
            "commonChannelGroup": t.string().optional(),
            "interferenceCoordinationGroup": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceMetadataIn"])
    types["SasPortalDeviceMetadataOut"] = t.struct(
        {
            "antennaModel": t.string().optional(),
            "commonChannelGroup": t.string().optional(),
            "interferenceCoordinationGroup": t.string().optional(),
            "nrqzValidated": t.boolean().optional(),
            "nrqzValidation": t.proxy(renames["SasPortalNrqzValidationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceMetadataOut"])
    types["SasPortalMigrateOrganizationResponseIn"] = t.struct(
        {
            "deploymentAssociation": t.array(
                t.proxy(renames["SasPortalDeploymentAssociationIn"])
            ).optional()
        }
    ).named(renames["SasPortalMigrateOrganizationResponseIn"])
    types["SasPortalMigrateOrganizationResponseOut"] = t.struct(
        {
            "deploymentAssociation": t.array(
                t.proxy(renames["SasPortalDeploymentAssociationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMigrateOrganizationResponseOut"])
    types["SasPortalNrqzValidationIn"] = t.struct(
        {
            "longitude": t.number().optional(),
            "state": t.string().optional(),
            "cpiId": t.string().optional(),
            "latitude": t.number().optional(),
            "caseId": t.string().optional(),
        }
    ).named(renames["SasPortalNrqzValidationIn"])
    types["SasPortalNrqzValidationOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "state": t.string().optional(),
            "cpiId": t.string().optional(),
            "latitude": t.number().optional(),
            "caseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalNrqzValidationOut"])
    types["SasPortalValidateInstallerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalValidateInstallerResponseIn"])
    types["SasPortalValidateInstallerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalValidateInstallerResponseOut"])
    types["SasPortalUpdateSignedDeviceRequestIn"] = t.struct(
        {"encodedDevice": t.string(), "installerId": t.string()}
    ).named(renames["SasPortalUpdateSignedDeviceRequestIn"])
    types["SasPortalUpdateSignedDeviceRequestOut"] = t.struct(
        {
            "encodedDevice": t.string(),
            "installerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalUpdateSignedDeviceRequestOut"])
    types["SasPortalListCustomersResponseIn"] = t.struct(
        {
            "customers": t.array(t.proxy(renames["SasPortalCustomerIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SasPortalListCustomersResponseIn"])
    types["SasPortalListCustomersResponseOut"] = t.struct(
        {
            "customers": t.array(t.proxy(renames["SasPortalCustomerOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalListCustomersResponseOut"])
    types["SasPortalMigrateOrganizationRequestIn"] = t.struct(
        {"organizationId": t.string()}
    ).named(renames["SasPortalMigrateOrganizationRequestIn"])
    types["SasPortalMigrateOrganizationRequestOut"] = t.struct(
        {
            "organizationId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMigrateOrganizationRequestOut"])
    types["SasPortalMoveDeviceRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveDeviceRequestIn"]
    )
    types["SasPortalMoveDeviceRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeviceRequestOut"])
    types["SasPortalMoveNodeRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveNodeRequestIn"]
    )
    types["SasPortalMoveNodeRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveNodeRequestOut"])
    types["SasPortalInstallationParamsIn"] = t.struct(
        {
            "antennaGainNewField": t.number().optional(),
            "longitude": t.number().optional(),
            "antennaDowntilt": t.integer().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "latitude": t.number().optional(),
            "heightType": t.string().optional(),
            "antennaModel": t.string().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "indoorDeployment": t.boolean().optional(),
            "antennaAzimuth": t.integer().optional(),
            "height": t.number().optional(),
            "eirpCapability": t.integer().optional(),
            "antennaGain": t.integer().optional(),
            "verticalAccuracy": t.number().optional(),
            "horizontalAccuracy": t.number().optional(),
        }
    ).named(renames["SasPortalInstallationParamsIn"])
    types["SasPortalInstallationParamsOut"] = t.struct(
        {
            "antennaGainNewField": t.number().optional(),
            "longitude": t.number().optional(),
            "antennaDowntilt": t.integer().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "latitude": t.number().optional(),
            "heightType": t.string().optional(),
            "antennaModel": t.string().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "indoorDeployment": t.boolean().optional(),
            "antennaAzimuth": t.integer().optional(),
            "height": t.number().optional(),
            "eirpCapability": t.integer().optional(),
            "antennaGain": t.integer().optional(),
            "verticalAccuracy": t.number().optional(),
            "horizontalAccuracy": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalInstallationParamsOut"])
    types["SasPortalSetPolicyRequestIn"] = t.struct(
        {
            "resource": t.string(),
            "policy": t.proxy(renames["SasPortalPolicyIn"]),
            "disableNotification": t.boolean().optional(),
        }
    ).named(renames["SasPortalSetPolicyRequestIn"])
    types["SasPortalSetPolicyRequestOut"] = t.struct(
        {
            "resource": t.string(),
            "policy": t.proxy(renames["SasPortalPolicyOut"]),
            "disableNotification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSetPolicyRequestOut"])
    types["SasPortalOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["SasPortalStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["SasPortalOperationIn"])
    types["SasPortalOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["SasPortalOperationOut"])
    types["SasPortalDeviceGrantIn"] = t.struct(
        {
            "maxEirp": t.number().optional(),
            "state": t.string().optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "channelType": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListIn"])).optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
            "grantId": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceGrantIn"])
    types["SasPortalDeviceGrantOut"] = t.struct(
        {
            "maxEirp": t.number().optional(),
            "state": t.string().optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "expireTime": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "channelType": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListOut"])).optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "grantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceGrantOut"])
    types["SasPortalListDeploymentsResponseIn"] = t.struct(
        {
            "deployments": t.array(
                t.proxy(renames["SasPortalDeploymentIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SasPortalListDeploymentsResponseIn"])
    types["SasPortalListDeploymentsResponseOut"] = t.struct(
        {
            "deployments": t.array(
                t.proxy(renames["SasPortalDeploymentOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalListDeploymentsResponseOut"])
    types["SasPortalValidateInstallerRequestIn"] = t.struct(
        {"encodedSecret": t.string(), "secret": t.string(), "installerId": t.string()}
    ).named(renames["SasPortalValidateInstallerRequestIn"])
    types["SasPortalValidateInstallerRequestOut"] = t.struct(
        {
            "encodedSecret": t.string(),
            "secret": t.string(),
            "installerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalValidateInstallerRequestOut"])
    types["SasPortalMoveDeploymentRequestIn"] = t.struct(
        {"destination": t.string()}
    ).named(renames["SasPortalMoveDeploymentRequestIn"])
    types["SasPortalMoveDeploymentRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeploymentRequestOut"])
    types["SasPortalStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["SasPortalStatusIn"])
    types["SasPortalStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalStatusOut"])
    types["SasPortalMigrateOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalMigrateOrganizationMetadataIn"])
    types["SasPortalMigrateOrganizationMetadataOut"] = t.struct(
        {
            "operationState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMigrateOrganizationMetadataOut"])
    types["SasPortalEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SasPortalEmptyIn"]
    )
    types["SasPortalEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalEmptyOut"])
    types["SasPortalGenerateSecretResponseIn"] = t.struct(
        {"secret": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretResponseIn"])
    types["SasPortalGenerateSecretResponseOut"] = t.struct(
        {
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalGenerateSecretResponseOut"])
    types["SasPortalDeploymentIn"] = t.struct(
        {
            "sasUserIds": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["SasPortalDeploymentIn"])
    types["SasPortalDeploymentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "frns": t.array(t.string()).optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeploymentOut"])
    types["SasPortalDeviceAirInterfaceIn"] = t.struct(
        {
            "radioTechnology": t.string().optional(),
            "supportedSpec": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceAirInterfaceIn"])
    types["SasPortalDeviceAirInterfaceOut"] = t.struct(
        {
            "radioTechnology": t.string().optional(),
            "supportedSpec": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceAirInterfaceOut"])

    functions = {}
    functions["installerValidate"] = prod_tt_sasportal.post(
        "v1alpha1/installer:generateSecret",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalGenerateSecretResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installerGenerateSecret"] = prod_tt_sasportal.post(
        "v1alpha1/installer:generateSecret",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalGenerateSecretResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersCheckHasProvisionedDeployment"] = prod_tt_sasportal.post(
        "v1alpha1/customers:provisionDeployment",
        t.struct(
            {
                "organizationId": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
                "newDeploymentDisplayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalProvisionDeploymentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPatch"] = prod_tt_sasportal.post(
        "v1alpha1/customers:provisionDeployment",
        t.struct(
            {
                "organizationId": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
                "newDeploymentDisplayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalProvisionDeploymentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersList"] = prod_tt_sasportal.post(
        "v1alpha1/customers:provisionDeployment",
        t.struct(
            {
                "organizationId": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
                "newDeploymentDisplayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalProvisionDeploymentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersMigrateOrganization"] = prod_tt_sasportal.post(
        "v1alpha1/customers:provisionDeployment",
        t.struct(
            {
                "organizationId": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
                "newDeploymentDisplayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalProvisionDeploymentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersGet"] = prod_tt_sasportal.post(
        "v1alpha1/customers:provisionDeployment",
        t.struct(
            {
                "organizationId": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
                "newDeploymentDisplayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalProvisionDeploymentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersProvisionDeployment"] = prod_tt_sasportal.post(
        "v1alpha1/customers:provisionDeployment",
        t.struct(
            {
                "organizationId": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
                "newDeploymentDisplayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalProvisionDeploymentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDelete"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesPatch"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesList"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesMove"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesGet"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDevicesCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDevicesCreateSigned"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDevicesList"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDeploymentsList"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "sasUserIds": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDeploymentsCreate"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "sasUserIds": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesNodesCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesNodesList"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesPatch"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesGet"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesCreateSigned"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesMove"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesList"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesSignDevice"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesUpdateSigned"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesCreate"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesDelete"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsCreate"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDelete"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsList"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsGet"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsPatch"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsMove"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDevicesList"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "installerId": t.string(),
                "encodedDevice": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDevicesCreate"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "installerId": t.string(),
                "encodedDevice": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDevicesCreateSigned"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "installerId": t.string(),
                "encodedDevice": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsGet"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesSignDevice"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesPatch"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesUpdateSigned"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesGet"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesDelete"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesMove"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesGet"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesUpdateSigned"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesList"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesGet"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesSignDevice"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesCreate"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesCreateSigned"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesDelete"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesPatch"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesMove"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDelete"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsPatch"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsMove"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsList"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsGet"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDevicesCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDevicesCreateSigned"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDevicesList"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesCreate"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDelete"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesGet"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesList"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesPatch"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesMove"] = prod_tt_sasportal.post(
        "v1alpha1/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destination": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesCreateSigned"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "name": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "fccId": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesList"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "name": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "fccId": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesCreate"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "name": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "fccId": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDeploymentsList"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "sasUserIds": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDeploymentsCreate"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "sasUserIds": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesNodesCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesNodesList"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesGet"] = prod_tt_sasportal.post(
        "v1alpha1/policies:test",
        t.struct(
            {
                "permissions": t.array(t.string()).optional(),
                "resource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalTestPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesSet"] = prod_tt_sasportal.post(
        "v1alpha1/policies:test",
        t.struct(
            {
                "permissions": t.array(t.string()).optional(),
                "resource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalTestPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesTest"] = prod_tt_sasportal.post(
        "v1alpha1/policies:test",
        t.struct(
            {
                "permissions": t.array(t.string()).optional(),
                "resource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalTestPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="prod_tt_sasportal",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
