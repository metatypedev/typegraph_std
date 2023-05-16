from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_sasportal() -> Import:
    sasportal = HTTPRuntime("https://sasportal.googleapis.com/")

    renames = {
        "ErrorResponse": "_sasportal_1_ErrorResponse",
        "SasPortalTestPermissionsResponseIn": "_sasportal_2_SasPortalTestPermissionsResponseIn",
        "SasPortalTestPermissionsResponseOut": "_sasportal_3_SasPortalTestPermissionsResponseOut",
        "SasPortalMoveDeviceRequestIn": "_sasportal_4_SasPortalMoveDeviceRequestIn",
        "SasPortalMoveDeviceRequestOut": "_sasportal_5_SasPortalMoveDeviceRequestOut",
        "SasPortalUpdateSignedDeviceRequestIn": "_sasportal_6_SasPortalUpdateSignedDeviceRequestIn",
        "SasPortalUpdateSignedDeviceRequestOut": "_sasportal_7_SasPortalUpdateSignedDeviceRequestOut",
        "SasPortalInstallationParamsIn": "_sasportal_8_SasPortalInstallationParamsIn",
        "SasPortalInstallationParamsOut": "_sasportal_9_SasPortalInstallationParamsOut",
        "SasPortalSetPolicyRequestIn": "_sasportal_10_SasPortalSetPolicyRequestIn",
        "SasPortalSetPolicyRequestOut": "_sasportal_11_SasPortalSetPolicyRequestOut",
        "SasPortalDeviceMetadataIn": "_sasportal_12_SasPortalDeviceMetadataIn",
        "SasPortalDeviceMetadataOut": "_sasportal_13_SasPortalDeviceMetadataOut",
        "SasPortalDeviceAirInterfaceIn": "_sasportal_14_SasPortalDeviceAirInterfaceIn",
        "SasPortalDeviceAirInterfaceOut": "_sasportal_15_SasPortalDeviceAirInterfaceOut",
        "SasPortalDeviceConfigIn": "_sasportal_16_SasPortalDeviceConfigIn",
        "SasPortalDeviceConfigOut": "_sasportal_17_SasPortalDeviceConfigOut",
        "SasPortalCreateSignedDeviceRequestIn": "_sasportal_18_SasPortalCreateSignedDeviceRequestIn",
        "SasPortalCreateSignedDeviceRequestOut": "_sasportal_19_SasPortalCreateSignedDeviceRequestOut",
        "SasPortalDeviceGrantIn": "_sasportal_20_SasPortalDeviceGrantIn",
        "SasPortalDeviceGrantOut": "_sasportal_21_SasPortalDeviceGrantOut",
        "SasPortalValidateInstallerRequestIn": "_sasportal_22_SasPortalValidateInstallerRequestIn",
        "SasPortalValidateInstallerRequestOut": "_sasportal_23_SasPortalValidateInstallerRequestOut",
        "SasPortalListDeploymentsResponseIn": "_sasportal_24_SasPortalListDeploymentsResponseIn",
        "SasPortalListDeploymentsResponseOut": "_sasportal_25_SasPortalListDeploymentsResponseOut",
        "SasPortalOperationIn": "_sasportal_26_SasPortalOperationIn",
        "SasPortalOperationOut": "_sasportal_27_SasPortalOperationOut",
        "SasPortalCustomerIn": "_sasportal_28_SasPortalCustomerIn",
        "SasPortalCustomerOut": "_sasportal_29_SasPortalCustomerOut",
        "SasPortalGenerateSecretResponseIn": "_sasportal_30_SasPortalGenerateSecretResponseIn",
        "SasPortalGenerateSecretResponseOut": "_sasportal_31_SasPortalGenerateSecretResponseOut",
        "SasPortalDeviceModelIn": "_sasportal_32_SasPortalDeviceModelIn",
        "SasPortalDeviceModelOut": "_sasportal_33_SasPortalDeviceModelOut",
        "SasPortalAssignmentIn": "_sasportal_34_SasPortalAssignmentIn",
        "SasPortalAssignmentOut": "_sasportal_35_SasPortalAssignmentOut",
        "SasPortalGetPolicyRequestIn": "_sasportal_36_SasPortalGetPolicyRequestIn",
        "SasPortalGetPolicyRequestOut": "_sasportal_37_SasPortalGetPolicyRequestOut",
        "SasPortalDeviceIn": "_sasportal_38_SasPortalDeviceIn",
        "SasPortalDeviceOut": "_sasportal_39_SasPortalDeviceOut",
        "SasPortalGenerateSecretRequestIn": "_sasportal_40_SasPortalGenerateSecretRequestIn",
        "SasPortalGenerateSecretRequestOut": "_sasportal_41_SasPortalGenerateSecretRequestOut",
        "SasPortalMoveNodeRequestIn": "_sasportal_42_SasPortalMoveNodeRequestIn",
        "SasPortalMoveNodeRequestOut": "_sasportal_43_SasPortalMoveNodeRequestOut",
        "SasPortalDeploymentIn": "_sasportal_44_SasPortalDeploymentIn",
        "SasPortalDeploymentOut": "_sasportal_45_SasPortalDeploymentOut",
        "SasPortalFrequencyRangeIn": "_sasportal_46_SasPortalFrequencyRangeIn",
        "SasPortalFrequencyRangeOut": "_sasportal_47_SasPortalFrequencyRangeOut",
        "SasPortalTestPermissionsRequestIn": "_sasportal_48_SasPortalTestPermissionsRequestIn",
        "SasPortalTestPermissionsRequestOut": "_sasportal_49_SasPortalTestPermissionsRequestOut",
        "SasPortalSignDeviceRequestIn": "_sasportal_50_SasPortalSignDeviceRequestIn",
        "SasPortalSignDeviceRequestOut": "_sasportal_51_SasPortalSignDeviceRequestOut",
        "SasPortalListDevicesResponseIn": "_sasportal_52_SasPortalListDevicesResponseIn",
        "SasPortalListDevicesResponseOut": "_sasportal_53_SasPortalListDevicesResponseOut",
        "SasPortalDpaMoveListIn": "_sasportal_54_SasPortalDpaMoveListIn",
        "SasPortalDpaMoveListOut": "_sasportal_55_SasPortalDpaMoveListOut",
        "SasPortalEmptyIn": "_sasportal_56_SasPortalEmptyIn",
        "SasPortalEmptyOut": "_sasportal_57_SasPortalEmptyOut",
        "SasPortalValidateInstallerResponseIn": "_sasportal_58_SasPortalValidateInstallerResponseIn",
        "SasPortalValidateInstallerResponseOut": "_sasportal_59_SasPortalValidateInstallerResponseOut",
        "SasPortalNodeIn": "_sasportal_60_SasPortalNodeIn",
        "SasPortalNodeOut": "_sasportal_61_SasPortalNodeOut",
        "SasPortalMoveDeploymentRequestIn": "_sasportal_62_SasPortalMoveDeploymentRequestIn",
        "SasPortalMoveDeploymentRequestOut": "_sasportal_63_SasPortalMoveDeploymentRequestOut",
        "SasPortalNrqzValidationIn": "_sasportal_64_SasPortalNrqzValidationIn",
        "SasPortalNrqzValidationOut": "_sasportal_65_SasPortalNrqzValidationOut",
        "SasPortalProvisionDeploymentRequestIn": "_sasportal_66_SasPortalProvisionDeploymentRequestIn",
        "SasPortalProvisionDeploymentRequestOut": "_sasportal_67_SasPortalProvisionDeploymentRequestOut",
        "SasPortalListNodesResponseIn": "_sasportal_68_SasPortalListNodesResponseIn",
        "SasPortalListNodesResponseOut": "_sasportal_69_SasPortalListNodesResponseOut",
        "SasPortalChannelWithScoreIn": "_sasportal_70_SasPortalChannelWithScoreIn",
        "SasPortalChannelWithScoreOut": "_sasportal_71_SasPortalChannelWithScoreOut",
        "SasPortalPolicyIn": "_sasportal_72_SasPortalPolicyIn",
        "SasPortalPolicyOut": "_sasportal_73_SasPortalPolicyOut",
        "SasPortalProvisionDeploymentResponseIn": "_sasportal_74_SasPortalProvisionDeploymentResponseIn",
        "SasPortalProvisionDeploymentResponseOut": "_sasportal_75_SasPortalProvisionDeploymentResponseOut",
        "SasPortalStatusIn": "_sasportal_76_SasPortalStatusIn",
        "SasPortalStatusOut": "_sasportal_77_SasPortalStatusOut",
        "SasPortalListCustomersResponseIn": "_sasportal_78_SasPortalListCustomersResponseIn",
        "SasPortalListCustomersResponseOut": "_sasportal_79_SasPortalListCustomersResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SasPortalTestPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["SasPortalTestPermissionsResponseIn"])
    types["SasPortalTestPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalTestPermissionsResponseOut"])
    types["SasPortalMoveDeviceRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveDeviceRequestIn"]
    )
    types["SasPortalMoveDeviceRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeviceRequestOut"])
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
    types["SasPortalInstallationParamsIn"] = t.struct(
        {
            "longitude": t.number().optional(),
            "heightType": t.string().optional(),
            "latitude": t.number().optional(),
            "antennaGain": t.integer().optional(),
            "horizontalAccuracy": t.number().optional(),
            "antennaGainNewField": t.number().optional(),
            "antennaDowntilt": t.integer().optional(),
            "indoorDeployment": t.boolean().optional(),
            "verticalAccuracy": t.number().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "antennaModel": t.string().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "eirpCapability": t.integer().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "height": t.number().optional(),
            "antennaAzimuth": t.integer().optional(),
        }
    ).named(renames["SasPortalInstallationParamsIn"])
    types["SasPortalInstallationParamsOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "heightType": t.string().optional(),
            "latitude": t.number().optional(),
            "antennaGain": t.integer().optional(),
            "horizontalAccuracy": t.number().optional(),
            "antennaGainNewField": t.number().optional(),
            "antennaDowntilt": t.integer().optional(),
            "indoorDeployment": t.boolean().optional(),
            "verticalAccuracy": t.number().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "antennaModel": t.string().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "eirpCapability": t.integer().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "height": t.number().optional(),
            "antennaAzimuth": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalInstallationParamsOut"])
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
    types["SasPortalDeviceMetadataIn"] = t.struct(
        {
            "interferenceCoordinationGroup": t.string().optional(),
            "commonChannelGroup": t.string().optional(),
            "antennaModel": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceMetadataIn"])
    types["SasPortalDeviceMetadataOut"] = t.struct(
        {
            "nrqzValidated": t.boolean().optional(),
            "interferenceCoordinationGroup": t.string().optional(),
            "commonChannelGroup": t.string().optional(),
            "nrqzValidation": t.proxy(renames["SasPortalNrqzValidationOut"]).optional(),
            "antennaModel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceMetadataOut"])
    types["SasPortalDeviceAirInterfaceIn"] = t.struct(
        {
            "supportedSpec": t.string().optional(),
            "radioTechnology": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceAirInterfaceIn"])
    types["SasPortalDeviceAirInterfaceOut"] = t.struct(
        {
            "supportedSpec": t.string().optional(),
            "radioTechnology": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceAirInterfaceOut"])
    types["SasPortalDeviceConfigIn"] = t.struct(
        {
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsIn"]
            ).optional(),
            "isSigned": t.boolean().optional(),
            "model": t.proxy(renames["SasPortalDeviceModelIn"]).optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
            "updateTime": t.string().optional(),
            "userId": t.string().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceIn"]
            ).optional(),
            "measurementCapabilities": t.array(t.string()).optional(),
            "callSign": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceConfigIn"])
    types["SasPortalDeviceConfigOut"] = t.struct(
        {
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsOut"]
            ).optional(),
            "isSigned": t.boolean().optional(),
            "model": t.proxy(renames["SasPortalDeviceModelOut"]).optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
            "updateTime": t.string().optional(),
            "userId": t.string().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceOut"]
            ).optional(),
            "measurementCapabilities": t.array(t.string()).optional(),
            "callSign": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceConfigOut"])
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
    types["SasPortalDeviceGrantIn"] = t.struct(
        {
            "maxEirp": t.number().optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "expireTime": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListIn"])).optional(),
            "grantId": t.string().optional(),
            "channelType": t.string().optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
        }
    ).named(renames["SasPortalDeviceGrantIn"])
    types["SasPortalDeviceGrantOut"] = t.struct(
        {
            "maxEirp": t.number().optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "expireTime": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListOut"])).optional(),
            "grantId": t.string().optional(),
            "channelType": t.string().optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceGrantOut"])
    types["SasPortalValidateInstallerRequestIn"] = t.struct(
        {"installerId": t.string(), "secret": t.string(), "encodedSecret": t.string()}
    ).named(renames["SasPortalValidateInstallerRequestIn"])
    types["SasPortalValidateInstallerRequestOut"] = t.struct(
        {
            "installerId": t.string(),
            "secret": t.string(),
            "encodedSecret": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalValidateInstallerRequestOut"])
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
    types["SasPortalOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["SasPortalStatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SasPortalOperationIn"])
    types["SasPortalOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SasPortalOperationOut"])
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
    types["SasPortalGenerateSecretResponseIn"] = t.struct(
        {"secret": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretResponseIn"])
    types["SasPortalGenerateSecretResponseOut"] = t.struct(
        {
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalGenerateSecretResponseOut"])
    types["SasPortalDeviceModelIn"] = t.struct(
        {
            "firmwareVersion": t.string().optional(),
            "name": t.string().optional(),
            "softwareVersion": t.string().optional(),
            "vendor": t.string().optional(),
            "hardwareVersion": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceModelIn"])
    types["SasPortalDeviceModelOut"] = t.struct(
        {
            "firmwareVersion": t.string().optional(),
            "name": t.string().optional(),
            "softwareVersion": t.string().optional(),
            "vendor": t.string().optional(),
            "hardwareVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceModelOut"])
    types["SasPortalAssignmentIn"] = t.struct(
        {"role": t.string(), "members": t.array(t.string()).optional()}
    ).named(renames["SasPortalAssignmentIn"])
    types["SasPortalAssignmentOut"] = t.struct(
        {
            "role": t.string(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalAssignmentOut"])
    types["SasPortalGetPolicyRequestIn"] = t.struct({"resource": t.string()}).named(
        renames["SasPortalGetPolicyRequestIn"]
    )
    types["SasPortalGetPolicyRequestOut"] = t.struct(
        {"resource": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGetPolicyRequestOut"])
    types["SasPortalDeviceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantIn"])).optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeIn"])
            ).optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataIn"]).optional(),
            "serialNumber": t.string().optional(),
            "displayName": t.string().optional(),
            "fccId": t.string().optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "state": t.string().optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
        }
    ).named(renames["SasPortalDeviceIn"])
    types["SasPortalDeviceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantOut"])).optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeOut"])
            ).optional(),
            "currentChannels": t.array(
                t.proxy(renames["SasPortalChannelWithScoreOut"])
            ).optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataOut"]).optional(),
            "serialNumber": t.string().optional(),
            "displayName": t.string().optional(),
            "fccId": t.string().optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "state": t.string().optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceOut"])
    types["SasPortalGenerateSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretRequestIn"])
    types["SasPortalGenerateSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGenerateSecretRequestOut"])
    types["SasPortalMoveNodeRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveNodeRequestIn"]
    )
    types["SasPortalMoveNodeRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveNodeRequestOut"])
    types["SasPortalDeploymentIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
        }
    ).named(renames["SasPortalDeploymentIn"])
    types["SasPortalDeploymentOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "frns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeploymentOut"])
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
    types["SasPortalSignDeviceRequestIn"] = t.struct(
        {"device": t.proxy(renames["SasPortalDeviceIn"])}
    ).named(renames["SasPortalSignDeviceRequestIn"])
    types["SasPortalSignDeviceRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["SasPortalDeviceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSignDeviceRequestOut"])
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
    types["SasPortalEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SasPortalEmptyIn"]
    )
    types["SasPortalEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalEmptyOut"])
    types["SasPortalValidateInstallerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalValidateInstallerResponseIn"])
    types["SasPortalValidateInstallerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalValidateInstallerResponseOut"])
    types["SasPortalNodeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
        }
    ).named(renames["SasPortalNodeIn"])
    types["SasPortalNodeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalNodeOut"])
    types["SasPortalMoveDeploymentRequestIn"] = t.struct(
        {"destination": t.string()}
    ).named(renames["SasPortalMoveDeploymentRequestIn"])
    types["SasPortalMoveDeploymentRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeploymentRequestOut"])
    types["SasPortalNrqzValidationIn"] = t.struct(
        {
            "caseId": t.string().optional(),
            "latitude": t.number().optional(),
            "cpiId": t.string().optional(),
            "state": t.string().optional(),
            "longitude": t.number().optional(),
        }
    ).named(renames["SasPortalNrqzValidationIn"])
    types["SasPortalNrqzValidationOut"] = t.struct(
        {
            "caseId": t.string().optional(),
            "latitude": t.number().optional(),
            "cpiId": t.string().optional(),
            "state": t.string().optional(),
            "longitude": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalNrqzValidationOut"])
    types["SasPortalProvisionDeploymentRequestIn"] = t.struct(
        {
            "newDeploymentDisplayName": t.string().optional(),
            "newOrganizationDisplayName": t.string().optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentRequestIn"])
    types["SasPortalProvisionDeploymentRequestOut"] = t.struct(
        {
            "newDeploymentDisplayName": t.string().optional(),
            "newOrganizationDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentRequestOut"])
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
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["SasPortalStatusIn"])
    types["SasPortalStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalStatusOut"])
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

    functions = {}
    functions["deploymentsGet"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
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
    functions["customersProvisionDeployment"] = sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalCustomerOut"]),
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
    functions["customersPatch"] = sasportal.get(
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
    functions["customersDevicesList"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesDelete"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesMove"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesCreateSigned"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesSignDevice"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesPatch"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesUpdateSigned"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesGet"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesCreate"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
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
    functions["customersDeploymentsPatch"] = sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
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
    functions["customersDeploymentsGet"] = sasportal.delete(
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesCreate"] = sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesMove"] = sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesGet"] = sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDelete"] = sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesList"] = sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesPatch"] = sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDevicesCreateSigned"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDevicesCreate"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDevicesList"] = sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
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
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
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
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installerGenerateSecret"] = sasportal.post(
        "v1alpha1/installer:validate",
        t.struct(
            {
                "installerId": t.string(),
                "secret": t.string(),
                "encodedSecret": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalValidateInstallerResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installerValidate"] = sasportal.post(
        "v1alpha1/installer:validate",
        t.struct(
            {
                "installerId": t.string(),
                "secret": t.string(),
                "encodedSecret": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalValidateInstallerResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesTest"] = sasportal.post(
        "v1alpha1/policies:get",
        t.struct({"resource": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesSet"] = sasportal.post(
        "v1alpha1/policies:get",
        t.struct({"resource": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesGet"] = sasportal.post(
        "v1alpha1/policies:get",
        t.struct({"resource": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalPolicyOut"]),
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
    functions["nodesDevicesList"] = sasportal.post(
        "v1alpha1/{name}:signDevice",
        t.struct(
            {
                "name": t.string().optional(),
                "device": t.proxy(renames["SasPortalDeviceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesCreate"] = sasportal.post(
        "v1alpha1/{name}:signDevice",
        t.struct(
            {
                "name": t.string().optional(),
                "device": t.proxy(renames["SasPortalDeviceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesGet"] = sasportal.post(
        "v1alpha1/{name}:signDevice",
        t.struct(
            {
                "name": t.string().optional(),
                "device": t.proxy(renames["SasPortalDeviceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesPatch"] = sasportal.post(
        "v1alpha1/{name}:signDevice",
        t.struct(
            {
                "name": t.string().optional(),
                "device": t.proxy(renames["SasPortalDeviceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesDelete"] = sasportal.post(
        "v1alpha1/{name}:signDevice",
        t.struct(
            {
                "name": t.string().optional(),
                "device": t.proxy(renames["SasPortalDeviceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesCreateSigned"] = sasportal.post(
        "v1alpha1/{name}:signDevice",
        t.struct(
            {
                "name": t.string().optional(),
                "device": t.proxy(renames["SasPortalDeviceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesUpdateSigned"] = sasportal.post(
        "v1alpha1/{name}:signDevice",
        t.struct(
            {
                "name": t.string().optional(),
                "device": t.proxy(renames["SasPortalDeviceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesMove"] = sasportal.post(
        "v1alpha1/{name}:signDevice",
        t.struct(
            {
                "name": t.string().optional(),
                "device": t.proxy(renames["SasPortalDeviceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesSignDevice"] = sasportal.post(
        "v1alpha1/{name}:signDevice",
        t.struct(
            {
                "name": t.string().optional(),
                "device": t.proxy(renames["SasPortalDeviceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsList"] = sasportal.post(
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
    functions["nodesDeploymentsDelete"] = sasportal.post(
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
    functions["nodesDeploymentsGet"] = sasportal.post(
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
    functions["nodesDeploymentsPatch"] = sasportal.post(
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
    functions["nodesDeploymentsMove"] = sasportal.post(
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
    functions["nodesDeploymentsDevicesCreate"] = sasportal.post(
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
    functions["nodesDeploymentsDevicesList"] = sasportal.post(
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
    functions["nodesDeploymentsDevicesCreateSigned"] = sasportal.post(
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
    functions["nodesNodesPatch"] = sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesGet"] = sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesMove"] = sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDelete"] = sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesList"] = sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesCreate"] = sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "displayName": t.string().optional(),
                "sasUserIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesNodesCreate"] = sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDeploymentsCreate"] = sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesCreateSigned"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesList"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesCreate"] = sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "serialNumber": t.string().optional(),
                "displayName": t.string().optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="sasportal",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
