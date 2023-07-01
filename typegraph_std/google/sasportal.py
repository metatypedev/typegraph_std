from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_sasportal():
    sasportal = HTTPRuntime("https://sasportal.googleapis.com/")

    renames = {
        "ErrorResponse": "_sasportal_1_ErrorResponse",
        "SasPortalDeviceIn": "_sasportal_2_SasPortalDeviceIn",
        "SasPortalDeviceOut": "_sasportal_3_SasPortalDeviceOut",
        "SasPortalNodeIn": "_sasportal_4_SasPortalNodeIn",
        "SasPortalNodeOut": "_sasportal_5_SasPortalNodeOut",
        "SasPortalDeploymentAssociationIn": "_sasportal_6_SasPortalDeploymentAssociationIn",
        "SasPortalDeploymentAssociationOut": "_sasportal_7_SasPortalDeploymentAssociationOut",
        "SasPortalListCustomersResponseIn": "_sasportal_8_SasPortalListCustomersResponseIn",
        "SasPortalListCustomersResponseOut": "_sasportal_9_SasPortalListCustomersResponseOut",
        "SasPortalGetPolicyRequestIn": "_sasportal_10_SasPortalGetPolicyRequestIn",
        "SasPortalGetPolicyRequestOut": "_sasportal_11_SasPortalGetPolicyRequestOut",
        "SasPortalDeviceAirInterfaceIn": "_sasportal_12_SasPortalDeviceAirInterfaceIn",
        "SasPortalDeviceAirInterfaceOut": "_sasportal_13_SasPortalDeviceAirInterfaceOut",
        "SasPortalPolicyIn": "_sasportal_14_SasPortalPolicyIn",
        "SasPortalPolicyOut": "_sasportal_15_SasPortalPolicyOut",
        "SasPortalValidateInstallerRequestIn": "_sasportal_16_SasPortalValidateInstallerRequestIn",
        "SasPortalValidateInstallerRequestOut": "_sasportal_17_SasPortalValidateInstallerRequestOut",
        "SasPortalUpdateSignedDeviceRequestIn": "_sasportal_18_SasPortalUpdateSignedDeviceRequestIn",
        "SasPortalUpdateSignedDeviceRequestOut": "_sasportal_19_SasPortalUpdateSignedDeviceRequestOut",
        "SasPortalMigrateOrganizationMetadataIn": "_sasportal_20_SasPortalMigrateOrganizationMetadataIn",
        "SasPortalMigrateOrganizationMetadataOut": "_sasportal_21_SasPortalMigrateOrganizationMetadataOut",
        "SasPortalTestPermissionsResponseIn": "_sasportal_22_SasPortalTestPermissionsResponseIn",
        "SasPortalTestPermissionsResponseOut": "_sasportal_23_SasPortalTestPermissionsResponseOut",
        "SasPortalValidateInstallerResponseIn": "_sasportal_24_SasPortalValidateInstallerResponseIn",
        "SasPortalValidateInstallerResponseOut": "_sasportal_25_SasPortalValidateInstallerResponseOut",
        "SasPortalDpaMoveListIn": "_sasportal_26_SasPortalDpaMoveListIn",
        "SasPortalDpaMoveListOut": "_sasportal_27_SasPortalDpaMoveListOut",
        "SasPortalDeviceConfigIn": "_sasportal_28_SasPortalDeviceConfigIn",
        "SasPortalDeviceConfigOut": "_sasportal_29_SasPortalDeviceConfigOut",
        "SasPortalInstallationParamsIn": "_sasportal_30_SasPortalInstallationParamsIn",
        "SasPortalInstallationParamsOut": "_sasportal_31_SasPortalInstallationParamsOut",
        "SasPortalDeploymentIn": "_sasportal_32_SasPortalDeploymentIn",
        "SasPortalDeploymentOut": "_sasportal_33_SasPortalDeploymentOut",
        "SasPortalMoveDeviceRequestIn": "_sasportal_34_SasPortalMoveDeviceRequestIn",
        "SasPortalMoveDeviceRequestOut": "_sasportal_35_SasPortalMoveDeviceRequestOut",
        "SasPortalDeviceGrantIn": "_sasportal_36_SasPortalDeviceGrantIn",
        "SasPortalDeviceGrantOut": "_sasportal_37_SasPortalDeviceGrantOut",
        "SasPortalGenerateSecretResponseIn": "_sasportal_38_SasPortalGenerateSecretResponseIn",
        "SasPortalGenerateSecretResponseOut": "_sasportal_39_SasPortalGenerateSecretResponseOut",
        "SasPortalFrequencyRangeIn": "_sasportal_40_SasPortalFrequencyRangeIn",
        "SasPortalFrequencyRangeOut": "_sasportal_41_SasPortalFrequencyRangeOut",
        "SasPortalMoveDeploymentRequestIn": "_sasportal_42_SasPortalMoveDeploymentRequestIn",
        "SasPortalMoveDeploymentRequestOut": "_sasportal_43_SasPortalMoveDeploymentRequestOut",
        "SasPortalListDevicesResponseIn": "_sasportal_44_SasPortalListDevicesResponseIn",
        "SasPortalListDevicesResponseOut": "_sasportal_45_SasPortalListDevicesResponseOut",
        "SasPortalCheckHasProvisionedDeploymentResponseIn": "_sasportal_46_SasPortalCheckHasProvisionedDeploymentResponseIn",
        "SasPortalCheckHasProvisionedDeploymentResponseOut": "_sasportal_47_SasPortalCheckHasProvisionedDeploymentResponseOut",
        "SasPortalDeviceModelIn": "_sasportal_48_SasPortalDeviceModelIn",
        "SasPortalDeviceModelOut": "_sasportal_49_SasPortalDeviceModelOut",
        "SasPortalNrqzValidationIn": "_sasportal_50_SasPortalNrqzValidationIn",
        "SasPortalNrqzValidationOut": "_sasportal_51_SasPortalNrqzValidationOut",
        "SasPortalMigrateOrganizationResponseIn": "_sasportal_52_SasPortalMigrateOrganizationResponseIn",
        "SasPortalMigrateOrganizationResponseOut": "_sasportal_53_SasPortalMigrateOrganizationResponseOut",
        "SasPortalGenerateSecretRequestIn": "_sasportal_54_SasPortalGenerateSecretRequestIn",
        "SasPortalGenerateSecretRequestOut": "_sasportal_55_SasPortalGenerateSecretRequestOut",
        "SasPortalSetPolicyRequestIn": "_sasportal_56_SasPortalSetPolicyRequestIn",
        "SasPortalSetPolicyRequestOut": "_sasportal_57_SasPortalSetPolicyRequestOut",
        "SasPortalChannelWithScoreIn": "_sasportal_58_SasPortalChannelWithScoreIn",
        "SasPortalChannelWithScoreOut": "_sasportal_59_SasPortalChannelWithScoreOut",
        "SasPortalAssignmentIn": "_sasportal_60_SasPortalAssignmentIn",
        "SasPortalAssignmentOut": "_sasportal_61_SasPortalAssignmentOut",
        "SasPortalMigrateOrganizationRequestIn": "_sasportal_62_SasPortalMigrateOrganizationRequestIn",
        "SasPortalMigrateOrganizationRequestOut": "_sasportal_63_SasPortalMigrateOrganizationRequestOut",
        "SasPortalListNodesResponseIn": "_sasportal_64_SasPortalListNodesResponseIn",
        "SasPortalListNodesResponseOut": "_sasportal_65_SasPortalListNodesResponseOut",
        "SasPortalListDeploymentsResponseIn": "_sasportal_66_SasPortalListDeploymentsResponseIn",
        "SasPortalListDeploymentsResponseOut": "_sasportal_67_SasPortalListDeploymentsResponseOut",
        "SasPortalSignDeviceRequestIn": "_sasportal_68_SasPortalSignDeviceRequestIn",
        "SasPortalSignDeviceRequestOut": "_sasportal_69_SasPortalSignDeviceRequestOut",
        "SasPortalDeviceMetadataIn": "_sasportal_70_SasPortalDeviceMetadataIn",
        "SasPortalDeviceMetadataOut": "_sasportal_71_SasPortalDeviceMetadataOut",
        "SasPortalCustomerIn": "_sasportal_72_SasPortalCustomerIn",
        "SasPortalCustomerOut": "_sasportal_73_SasPortalCustomerOut",
        "SasPortalMoveNodeRequestIn": "_sasportal_74_SasPortalMoveNodeRequestIn",
        "SasPortalMoveNodeRequestOut": "_sasportal_75_SasPortalMoveNodeRequestOut",
        "SasPortalEmptyIn": "_sasportal_76_SasPortalEmptyIn",
        "SasPortalEmptyOut": "_sasportal_77_SasPortalEmptyOut",
        "SasPortalTestPermissionsRequestIn": "_sasportal_78_SasPortalTestPermissionsRequestIn",
        "SasPortalTestPermissionsRequestOut": "_sasportal_79_SasPortalTestPermissionsRequestOut",
        "SasPortalCreateSignedDeviceRequestIn": "_sasportal_80_SasPortalCreateSignedDeviceRequestIn",
        "SasPortalCreateSignedDeviceRequestOut": "_sasportal_81_SasPortalCreateSignedDeviceRequestOut",
        "SasPortalProvisionDeploymentRequestIn": "_sasportal_82_SasPortalProvisionDeploymentRequestIn",
        "SasPortalProvisionDeploymentRequestOut": "_sasportal_83_SasPortalProvisionDeploymentRequestOut",
        "SasPortalOperationIn": "_sasportal_84_SasPortalOperationIn",
        "SasPortalOperationOut": "_sasportal_85_SasPortalOperationOut",
        "SasPortalProvisionDeploymentResponseIn": "_sasportal_86_SasPortalProvisionDeploymentResponseIn",
        "SasPortalProvisionDeploymentResponseOut": "_sasportal_87_SasPortalProvisionDeploymentResponseOut",
        "SasPortalStatusIn": "_sasportal_88_SasPortalStatusIn",
        "SasPortalStatusOut": "_sasportal_89_SasPortalStatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SasPortalDeviceIn"] = t.struct(
        {
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeIn"])
            ).optional(),
            "displayName": t.string().optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "serialNumber": t.string().optional(),
            "fccId": t.string().optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantIn"])).optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataIn"]).optional(),
        }
    ).named(renames["SasPortalDeviceIn"])
    types["SasPortalDeviceOut"] = t.struct(
        {
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "currentChannels": t.array(
                t.proxy(renames["SasPortalChannelWithScoreOut"])
            ).optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "serialNumber": t.string().optional(),
            "fccId": t.string().optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantOut"])).optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceOut"])
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
    types["SasPortalListCustomersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customers": t.array(t.proxy(renames["SasPortalCustomerIn"])).optional(),
        }
    ).named(renames["SasPortalListCustomersResponseIn"])
    types["SasPortalListCustomersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customers": t.array(t.proxy(renames["SasPortalCustomerOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalListCustomersResponseOut"])
    types["SasPortalGetPolicyRequestIn"] = t.struct({"resource": t.string()}).named(
        renames["SasPortalGetPolicyRequestIn"]
    )
    types["SasPortalGetPolicyRequestOut"] = t.struct(
        {"resource": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGetPolicyRequestOut"])
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
    types["SasPortalUpdateSignedDeviceRequestIn"] = t.struct(
        {"installerId": t.string(), "encodedDevice": t.string()}
    ).named(renames["SasPortalUpdateSignedDeviceRequestIn"])
    types["SasPortalUpdateSignedDeviceRequestOut"] = t.struct(
        {
            "installerId": t.string(),
            "encodedDevice": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalUpdateSignedDeviceRequestOut"])
    types["SasPortalMigrateOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalMigrateOrganizationMetadataIn"])
    types["SasPortalMigrateOrganizationMetadataOut"] = t.struct(
        {
            "operationState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMigrateOrganizationMetadataOut"])
    types["SasPortalTestPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["SasPortalTestPermissionsResponseIn"])
    types["SasPortalTestPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalTestPermissionsResponseOut"])
    types["SasPortalValidateInstallerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalValidateInstallerResponseIn"])
    types["SasPortalValidateInstallerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalValidateInstallerResponseOut"])
    types["SasPortalDpaMoveListIn"] = t.struct(
        {
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
            "dpaId": t.string().optional(),
        }
    ).named(renames["SasPortalDpaMoveListIn"])
    types["SasPortalDpaMoveListOut"] = t.struct(
        {
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "dpaId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDpaMoveListOut"])
    types["SasPortalDeviceConfigIn"] = t.struct(
        {
            "measurementCapabilities": t.array(t.string()).optional(),
            "model": t.proxy(renames["SasPortalDeviceModelIn"]).optional(),
            "category": t.string().optional(),
            "callSign": t.string().optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsIn"]
            ).optional(),
            "state": t.string().optional(),
            "userId": t.string().optional(),
            "updateTime": t.string().optional(),
            "isSigned": t.boolean().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceIn"]
            ).optional(),
        }
    ).named(renames["SasPortalDeviceConfigIn"])
    types["SasPortalDeviceConfigOut"] = t.struct(
        {
            "measurementCapabilities": t.array(t.string()).optional(),
            "model": t.proxy(renames["SasPortalDeviceModelOut"]).optional(),
            "category": t.string().optional(),
            "callSign": t.string().optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsOut"]
            ).optional(),
            "state": t.string().optional(),
            "userId": t.string().optional(),
            "updateTime": t.string().optional(),
            "isSigned": t.boolean().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceConfigOut"])
    types["SasPortalInstallationParamsIn"] = t.struct(
        {
            "horizontalAccuracy": t.number().optional(),
            "indoorDeployment": t.boolean().optional(),
            "latitude": t.number().optional(),
            "eirpCapability": t.integer().optional(),
            "heightType": t.string().optional(),
            "verticalAccuracy": t.number().optional(),
            "antennaModel": t.string().optional(),
            "longitude": t.number().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "height": t.number().optional(),
            "antennaGain": t.integer().optional(),
            "antennaDowntilt": t.integer().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "antennaAzimuth": t.integer().optional(),
            "antennaGainNewField": t.number().optional(),
        }
    ).named(renames["SasPortalInstallationParamsIn"])
    types["SasPortalInstallationParamsOut"] = t.struct(
        {
            "horizontalAccuracy": t.number().optional(),
            "indoorDeployment": t.boolean().optional(),
            "latitude": t.number().optional(),
            "eirpCapability": t.integer().optional(),
            "heightType": t.string().optional(),
            "verticalAccuracy": t.number().optional(),
            "antennaModel": t.string().optional(),
            "longitude": t.number().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "height": t.number().optional(),
            "antennaGain": t.integer().optional(),
            "antennaDowntilt": t.integer().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "antennaAzimuth": t.integer().optional(),
            "antennaGainNewField": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalInstallationParamsOut"])
    types["SasPortalDeploymentIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
        }
    ).named(renames["SasPortalDeploymentIn"])
    types["SasPortalDeploymentOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "frns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeploymentOut"])
    types["SasPortalMoveDeviceRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveDeviceRequestIn"]
    )
    types["SasPortalMoveDeviceRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeviceRequestOut"])
    types["SasPortalDeviceGrantIn"] = t.struct(
        {
            "suspensionReason": t.array(t.string()).optional(),
            "channelType": t.string().optional(),
            "maxEirp": t.number().optional(),
            "expireTime": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListIn"])).optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "state": t.string().optional(),
            "grantId": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceGrantIn"])
    types["SasPortalDeviceGrantOut"] = t.struct(
        {
            "suspensionReason": t.array(t.string()).optional(),
            "channelType": t.string().optional(),
            "maxEirp": t.number().optional(),
            "expireTime": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListOut"])).optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "state": t.string().optional(),
            "grantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceGrantOut"])
    types["SasPortalGenerateSecretResponseIn"] = t.struct(
        {"secret": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretResponseIn"])
    types["SasPortalGenerateSecretResponseOut"] = t.struct(
        {
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalGenerateSecretResponseOut"])
    types["SasPortalFrequencyRangeIn"] = t.struct(
        {
            "lowFrequencyMhz": t.number().optional(),
            "highFrequencyMhz": t.number().optional(),
        }
    ).named(renames["SasPortalFrequencyRangeIn"])
    types["SasPortalFrequencyRangeOut"] = t.struct(
        {
            "lowFrequencyMhz": t.number().optional(),
            "highFrequencyMhz": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalFrequencyRangeOut"])
    types["SasPortalMoveDeploymentRequestIn"] = t.struct(
        {"destination": t.string()}
    ).named(renames["SasPortalMoveDeploymentRequestIn"])
    types["SasPortalMoveDeploymentRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeploymentRequestOut"])
    types["SasPortalListDevicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["SasPortalDeviceIn"])).optional(),
        }
    ).named(renames["SasPortalListDevicesResponseIn"])
    types["SasPortalListDevicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["SasPortalDeviceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalListDevicesResponseOut"])
    types["SasPortalCheckHasProvisionedDeploymentResponseIn"] = t.struct(
        {"hasProvisionedDeployment": t.boolean().optional()}
    ).named(renames["SasPortalCheckHasProvisionedDeploymentResponseIn"])
    types["SasPortalCheckHasProvisionedDeploymentResponseOut"] = t.struct(
        {
            "hasProvisionedDeployment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalCheckHasProvisionedDeploymentResponseOut"])
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
    types["SasPortalNrqzValidationIn"] = t.struct(
        {
            "longitude": t.number().optional(),
            "state": t.string().optional(),
            "caseId": t.string().optional(),
            "cpiId": t.string().optional(),
            "latitude": t.number().optional(),
        }
    ).named(renames["SasPortalNrqzValidationIn"])
    types["SasPortalNrqzValidationOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "state": t.string().optional(),
            "caseId": t.string().optional(),
            "cpiId": t.string().optional(),
            "latitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalNrqzValidationOut"])
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
    types["SasPortalGenerateSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretRequestIn"])
    types["SasPortalGenerateSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGenerateSecretRequestOut"])
    types["SasPortalSetPolicyRequestIn"] = t.struct(
        {
            "disableNotification": t.boolean().optional(),
            "policy": t.proxy(renames["SasPortalPolicyIn"]),
            "resource": t.string(),
        }
    ).named(renames["SasPortalSetPolicyRequestIn"])
    types["SasPortalSetPolicyRequestOut"] = t.struct(
        {
            "disableNotification": t.boolean().optional(),
            "policy": t.proxy(renames["SasPortalPolicyOut"]),
            "resource": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSetPolicyRequestOut"])
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
    types["SasPortalMigrateOrganizationRequestIn"] = t.struct(
        {"organizationId": t.string()}
    ).named(renames["SasPortalMigrateOrganizationRequestIn"])
    types["SasPortalMigrateOrganizationRequestOut"] = t.struct(
        {
            "organizationId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMigrateOrganizationRequestOut"])
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
    types["SasPortalListDeploymentsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deployments": t.array(
                t.proxy(renames["SasPortalDeploymentIn"])
            ).optional(),
        }
    ).named(renames["SasPortalListDeploymentsResponseIn"])
    types["SasPortalListDeploymentsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "deployments": t.array(
                t.proxy(renames["SasPortalDeploymentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalListDeploymentsResponseOut"])
    types["SasPortalSignDeviceRequestIn"] = t.struct(
        {"device": t.proxy(renames["SasPortalDeviceIn"])}
    ).named(renames["SasPortalSignDeviceRequestIn"])
    types["SasPortalSignDeviceRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["SasPortalDeviceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSignDeviceRequestOut"])
    types["SasPortalDeviceMetadataIn"] = t.struct(
        {
            "interferenceCoordinationGroup": t.string().optional(),
            "commonChannelGroup": t.string().optional(),
            "antennaModel": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceMetadataIn"])
    types["SasPortalDeviceMetadataOut"] = t.struct(
        {
            "interferenceCoordinationGroup": t.string().optional(),
            "commonChannelGroup": t.string().optional(),
            "nrqzValidated": t.boolean().optional(),
            "antennaModel": t.string().optional(),
            "nrqzValidation": t.proxy(renames["SasPortalNrqzValidationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceMetadataOut"])
    types["SasPortalCustomerIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "displayName": t.string(),
        }
    ).named(renames["SasPortalCustomerIn"])
    types["SasPortalCustomerOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalCustomerOut"])
    types["SasPortalMoveNodeRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveNodeRequestIn"]
    )
    types["SasPortalMoveNodeRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveNodeRequestOut"])
    types["SasPortalEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SasPortalEmptyIn"]
    )
    types["SasPortalEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalEmptyOut"])
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
    types["SasPortalCreateSignedDeviceRequestIn"] = t.struct(
        {"encodedDevice": t.string(), "installerId": t.string()}
    ).named(renames["SasPortalCreateSignedDeviceRequestIn"])
    types["SasPortalCreateSignedDeviceRequestOut"] = t.struct(
        {
            "encodedDevice": t.string(),
            "installerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalCreateSignedDeviceRequestOut"])
    types["SasPortalProvisionDeploymentRequestIn"] = t.struct(
        {
            "newOrganizationDisplayName": t.string().optional(),
            "newDeploymentDisplayName": t.string().optional(),
            "organizationId": t.string().optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentRequestIn"])
    types["SasPortalProvisionDeploymentRequestOut"] = t.struct(
        {
            "newOrganizationDisplayName": t.string().optional(),
            "newDeploymentDisplayName": t.string().optional(),
            "organizationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentRequestOut"])
    types["SasPortalOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["SasPortalStatusIn"]).optional(),
        }
    ).named(renames["SasPortalOperationIn"])
    types["SasPortalOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalOperationOut"])
    types["SasPortalProvisionDeploymentResponseIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["SasPortalProvisionDeploymentResponseIn"])
    types["SasPortalProvisionDeploymentResponseOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentResponseOut"])
    types["SasPortalStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["SasPortalStatusIn"])
    types["SasPortalStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalStatusOut"])

    functions = {}
    functions["policiesGet"] = sasportal.post(
        "v1alpha1/policies:set",
        t.struct(
            {
                "disableNotification": t.boolean().optional(),
                "policy": t.proxy(renames["SasPortalPolicyIn"]),
                "resource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesTest"] = sasportal.post(
        "v1alpha1/policies:set",
        t.struct(
            {
                "disableNotification": t.boolean().optional(),
                "policy": t.proxy(renames["SasPortalPolicyIn"]),
                "resource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesSet"] = sasportal.post(
        "v1alpha1/policies:set",
        t.struct(
            {
                "disableNotification": t.boolean().optional(),
                "policy": t.proxy(renames["SasPortalPolicyIn"]),
                "resource": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersList"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalCustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersCheckHasProvisionedDeployment"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalCustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersPatch"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalCustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersProvisionDeployment"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalCustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersMigrateOrganization"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalCustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersGet"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalCustomerOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsList"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsCreate"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsPatch"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsMove"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsGet"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDelete"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDevicesCreateSigned"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDevicesCreate"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDevicesList"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesList"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesMove"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesCreate"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesPatch"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesGet"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDelete"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDevicesList"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "fccId": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "state": t.string().optional(),
                "name": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDevicesCreateSigned"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "fccId": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "state": t.string().optional(),
                "name": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDevicesCreate"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "fccId": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "state": t.string().optional(),
                "name": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDeploymentsList"] = sasportal.post(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDeploymentsCreate"] = sasportal.post(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesNodesList"] = sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesNodesCreate"] = sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesGet"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesCreate"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesList"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesPatch"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesSignDevice"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesUpdateSigned"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesMove"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesDelete"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesCreateSigned"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installerValidate"] = sasportal.post(
        "v1alpha1/installer:generateSecret",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalGenerateSecretResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installerGenerateSecret"] = sasportal.post(
        "v1alpha1/installer:generateSecret",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalGenerateSecretResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsGet"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesPatch"] = sasportal.post(
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
    functions["deploymentsDevicesSignDevice"] = sasportal.post(
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
    functions["deploymentsDevicesDelete"] = sasportal.post(
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
    functions["deploymentsDevicesGet"] = sasportal.post(
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
    functions["deploymentsDevicesUpdateSigned"] = sasportal.post(
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
    functions["deploymentsDevicesMove"] = sasportal.post(
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
    functions["nodesGet"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDelete"] = sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsGet"] = sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsPatch"] = sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsMove"] = sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsList"] = sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDevicesCreateSigned"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDevicesCreate"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDevicesList"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesUpdateSigned"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesSignDevice"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesCreateSigned"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesDelete"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesPatch"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesCreate"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesMove"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesGet"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesList"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDelete"] = sasportal.post(
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
    functions["nodesNodesCreate"] = sasportal.post(
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
    functions["nodesNodesGet"] = sasportal.post(
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
    functions["nodesNodesPatch"] = sasportal.post(
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
    functions["nodesNodesList"] = sasportal.post(
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
    functions["nodesNodesMove"] = sasportal.post(
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
    functions["nodesNodesNodesCreate"] = sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesNodesList"] = sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesCreate"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesList"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesCreateSigned"] = sasportal.post(
        "v1alpha1/{parent}/devices:createSigned",
        t.struct(
            {
                "parent": t.string(),
                "encodedDevice": t.string(),
                "installerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDeploymentsCreate"] = sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDeploymentsList"] = sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sasportal",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
