from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_prod_tt_sasportal() -> Import:
    prod_tt_sasportal = HTTPRuntime("https://prod-tt-sasportal.googleapis.com/")

    renames = {
        "ErrorResponse": "_prod_tt_sasportal_1_ErrorResponse",
        "SasPortalDeviceConfigIn": "_prod_tt_sasportal_2_SasPortalDeviceConfigIn",
        "SasPortalDeviceConfigOut": "_prod_tt_sasportal_3_SasPortalDeviceConfigOut",
        "SasPortalStatusIn": "_prod_tt_sasportal_4_SasPortalStatusIn",
        "SasPortalStatusOut": "_prod_tt_sasportal_5_SasPortalStatusOut",
        "SasPortalListDeploymentsResponseIn": "_prod_tt_sasportal_6_SasPortalListDeploymentsResponseIn",
        "SasPortalListDeploymentsResponseOut": "_prod_tt_sasportal_7_SasPortalListDeploymentsResponseOut",
        "SasPortalListNodesResponseIn": "_prod_tt_sasportal_8_SasPortalListNodesResponseIn",
        "SasPortalListNodesResponseOut": "_prod_tt_sasportal_9_SasPortalListNodesResponseOut",
        "SasPortalInstallationParamsIn": "_prod_tt_sasportal_10_SasPortalInstallationParamsIn",
        "SasPortalInstallationParamsOut": "_prod_tt_sasportal_11_SasPortalInstallationParamsOut",
        "SasPortalDeviceGrantIn": "_prod_tt_sasportal_12_SasPortalDeviceGrantIn",
        "SasPortalDeviceGrantOut": "_prod_tt_sasportal_13_SasPortalDeviceGrantOut",
        "SasPortalDeviceIn": "_prod_tt_sasportal_14_SasPortalDeviceIn",
        "SasPortalDeviceOut": "_prod_tt_sasportal_15_SasPortalDeviceOut",
        "SasPortalMoveDeviceRequestIn": "_prod_tt_sasportal_16_SasPortalMoveDeviceRequestIn",
        "SasPortalMoveDeviceRequestOut": "_prod_tt_sasportal_17_SasPortalMoveDeviceRequestOut",
        "SasPortalCreateSignedDeviceRequestIn": "_prod_tt_sasportal_18_SasPortalCreateSignedDeviceRequestIn",
        "SasPortalCreateSignedDeviceRequestOut": "_prod_tt_sasportal_19_SasPortalCreateSignedDeviceRequestOut",
        "SasPortalSignDeviceRequestIn": "_prod_tt_sasportal_20_SasPortalSignDeviceRequestIn",
        "SasPortalSignDeviceRequestOut": "_prod_tt_sasportal_21_SasPortalSignDeviceRequestOut",
        "SasPortalCustomerIn": "_prod_tt_sasportal_22_SasPortalCustomerIn",
        "SasPortalCustomerOut": "_prod_tt_sasportal_23_SasPortalCustomerOut",
        "SasPortalGenerateSecretRequestIn": "_prod_tt_sasportal_24_SasPortalGenerateSecretRequestIn",
        "SasPortalGenerateSecretRequestOut": "_prod_tt_sasportal_25_SasPortalGenerateSecretRequestOut",
        "SasPortalGenerateSecretResponseIn": "_prod_tt_sasportal_26_SasPortalGenerateSecretResponseIn",
        "SasPortalGenerateSecretResponseOut": "_prod_tt_sasportal_27_SasPortalGenerateSecretResponseOut",
        "SasPortalMoveDeploymentRequestIn": "_prod_tt_sasportal_28_SasPortalMoveDeploymentRequestIn",
        "SasPortalMoveDeploymentRequestOut": "_prod_tt_sasportal_29_SasPortalMoveDeploymentRequestOut",
        "SasPortalValidateInstallerResponseIn": "_prod_tt_sasportal_30_SasPortalValidateInstallerResponseIn",
        "SasPortalValidateInstallerResponseOut": "_prod_tt_sasportal_31_SasPortalValidateInstallerResponseOut",
        "SasPortalNodeIn": "_prod_tt_sasportal_32_SasPortalNodeIn",
        "SasPortalNodeOut": "_prod_tt_sasportal_33_SasPortalNodeOut",
        "SasPortalDeviceAirInterfaceIn": "_prod_tt_sasportal_34_SasPortalDeviceAirInterfaceIn",
        "SasPortalDeviceAirInterfaceOut": "_prod_tt_sasportal_35_SasPortalDeviceAirInterfaceOut",
        "SasPortalProvisionDeploymentResponseIn": "_prod_tt_sasportal_36_SasPortalProvisionDeploymentResponseIn",
        "SasPortalProvisionDeploymentResponseOut": "_prod_tt_sasportal_37_SasPortalProvisionDeploymentResponseOut",
        "SasPortalMoveNodeRequestIn": "_prod_tt_sasportal_38_SasPortalMoveNodeRequestIn",
        "SasPortalMoveNodeRequestOut": "_prod_tt_sasportal_39_SasPortalMoveNodeRequestOut",
        "SasPortalTestPermissionsResponseIn": "_prod_tt_sasportal_40_SasPortalTestPermissionsResponseIn",
        "SasPortalTestPermissionsResponseOut": "_prod_tt_sasportal_41_SasPortalTestPermissionsResponseOut",
        "SasPortalFrequencyRangeIn": "_prod_tt_sasportal_42_SasPortalFrequencyRangeIn",
        "SasPortalFrequencyRangeOut": "_prod_tt_sasportal_43_SasPortalFrequencyRangeOut",
        "SasPortalDeviceMetadataIn": "_prod_tt_sasportal_44_SasPortalDeviceMetadataIn",
        "SasPortalDeviceMetadataOut": "_prod_tt_sasportal_45_SasPortalDeviceMetadataOut",
        "SasPortalListDevicesResponseIn": "_prod_tt_sasportal_46_SasPortalListDevicesResponseIn",
        "SasPortalListDevicesResponseOut": "_prod_tt_sasportal_47_SasPortalListDevicesResponseOut",
        "SasPortalGetPolicyRequestIn": "_prod_tt_sasportal_48_SasPortalGetPolicyRequestIn",
        "SasPortalGetPolicyRequestOut": "_prod_tt_sasportal_49_SasPortalGetPolicyRequestOut",
        "SasPortalProvisionDeploymentRequestIn": "_prod_tt_sasportal_50_SasPortalProvisionDeploymentRequestIn",
        "SasPortalProvisionDeploymentRequestOut": "_prod_tt_sasportal_51_SasPortalProvisionDeploymentRequestOut",
        "SasPortalEmptyIn": "_prod_tt_sasportal_52_SasPortalEmptyIn",
        "SasPortalEmptyOut": "_prod_tt_sasportal_53_SasPortalEmptyOut",
        "SasPortalDeviceModelIn": "_prod_tt_sasportal_54_SasPortalDeviceModelIn",
        "SasPortalDeviceModelOut": "_prod_tt_sasportal_55_SasPortalDeviceModelOut",
        "SasPortalDeploymentIn": "_prod_tt_sasportal_56_SasPortalDeploymentIn",
        "SasPortalDeploymentOut": "_prod_tt_sasportal_57_SasPortalDeploymentOut",
        "SasPortalUpdateSignedDeviceRequestIn": "_prod_tt_sasportal_58_SasPortalUpdateSignedDeviceRequestIn",
        "SasPortalUpdateSignedDeviceRequestOut": "_prod_tt_sasportal_59_SasPortalUpdateSignedDeviceRequestOut",
        "SasPortalOperationIn": "_prod_tt_sasportal_60_SasPortalOperationIn",
        "SasPortalOperationOut": "_prod_tt_sasportal_61_SasPortalOperationOut",
        "SasPortalSetPolicyRequestIn": "_prod_tt_sasportal_62_SasPortalSetPolicyRequestIn",
        "SasPortalSetPolicyRequestOut": "_prod_tt_sasportal_63_SasPortalSetPolicyRequestOut",
        "SasPortalChannelWithScoreIn": "_prod_tt_sasportal_64_SasPortalChannelWithScoreIn",
        "SasPortalChannelWithScoreOut": "_prod_tt_sasportal_65_SasPortalChannelWithScoreOut",
        "SasPortalValidateInstallerRequestIn": "_prod_tt_sasportal_66_SasPortalValidateInstallerRequestIn",
        "SasPortalValidateInstallerRequestOut": "_prod_tt_sasportal_67_SasPortalValidateInstallerRequestOut",
        "SasPortalDpaMoveListIn": "_prod_tt_sasportal_68_SasPortalDpaMoveListIn",
        "SasPortalDpaMoveListOut": "_prod_tt_sasportal_69_SasPortalDpaMoveListOut",
        "SasPortalNrqzValidationIn": "_prod_tt_sasportal_70_SasPortalNrqzValidationIn",
        "SasPortalNrqzValidationOut": "_prod_tt_sasportal_71_SasPortalNrqzValidationOut",
        "SasPortalListCustomersResponseIn": "_prod_tt_sasportal_72_SasPortalListCustomersResponseIn",
        "SasPortalListCustomersResponseOut": "_prod_tt_sasportal_73_SasPortalListCustomersResponseOut",
        "SasPortalAssignmentIn": "_prod_tt_sasportal_74_SasPortalAssignmentIn",
        "SasPortalAssignmentOut": "_prod_tt_sasportal_75_SasPortalAssignmentOut",
        "SasPortalPolicyIn": "_prod_tt_sasportal_76_SasPortalPolicyIn",
        "SasPortalPolicyOut": "_prod_tt_sasportal_77_SasPortalPolicyOut",
        "SasPortalTestPermissionsRequestIn": "_prod_tt_sasportal_78_SasPortalTestPermissionsRequestIn",
        "SasPortalTestPermissionsRequestOut": "_prod_tt_sasportal_79_SasPortalTestPermissionsRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SasPortalDeviceConfigIn"] = t.struct(
        {
            "measurementCapabilities": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "userId": t.string().optional(),
            "category": t.string().optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsIn"]
            ).optional(),
            "model": t.proxy(renames["SasPortalDeviceModelIn"]).optional(),
            "callSign": t.string().optional(),
            "isSigned": t.boolean().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceIn"]
            ).optional(),
        }
    ).named(renames["SasPortalDeviceConfigIn"])
    types["SasPortalDeviceConfigOut"] = t.struct(
        {
            "measurementCapabilities": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "userId": t.string().optional(),
            "category": t.string().optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsOut"]
            ).optional(),
            "model": t.proxy(renames["SasPortalDeviceModelOut"]).optional(),
            "callSign": t.string().optional(),
            "isSigned": t.boolean().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceConfigOut"])
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
    types["SasPortalInstallationParamsIn"] = t.struct(
        {
            "antennaDowntilt": t.integer().optional(),
            "eirpCapability": t.integer().optional(),
            "longitude": t.number().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "antennaModel": t.string().optional(),
            "verticalAccuracy": t.number().optional(),
            "latitude": t.number().optional(),
            "horizontalAccuracy": t.number().optional(),
            "heightType": t.string().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "antennaGain": t.integer().optional(),
            "antennaGainNewField": t.number().optional(),
            "height": t.number().optional(),
            "antennaAzimuth": t.integer().optional(),
            "indoorDeployment": t.boolean().optional(),
        }
    ).named(renames["SasPortalInstallationParamsIn"])
    types["SasPortalInstallationParamsOut"] = t.struct(
        {
            "antennaDowntilt": t.integer().optional(),
            "eirpCapability": t.integer().optional(),
            "longitude": t.number().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "antennaModel": t.string().optional(),
            "verticalAccuracy": t.number().optional(),
            "latitude": t.number().optional(),
            "horizontalAccuracy": t.number().optional(),
            "heightType": t.string().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "antennaGain": t.integer().optional(),
            "antennaGainNewField": t.number().optional(),
            "height": t.number().optional(),
            "antennaAzimuth": t.integer().optional(),
            "indoorDeployment": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalInstallationParamsOut"])
    types["SasPortalDeviceGrantIn"] = t.struct(
        {
            "grantId": t.string().optional(),
            "channelType": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListIn"])).optional(),
            "state": t.string().optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "maxEirp": t.number().optional(),
            "expireTime": t.string().optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
            "suspensionReason": t.array(t.string()).optional(),
        }
    ).named(renames["SasPortalDeviceGrantIn"])
    types["SasPortalDeviceGrantOut"] = t.struct(
        {
            "grantId": t.string().optional(),
            "channelType": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListOut"])).optional(),
            "state": t.string().optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "maxEirp": t.number().optional(),
            "expireTime": t.string().optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceGrantOut"])
    types["SasPortalDeviceIn"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataIn"]).optional(),
            "fccId": t.string().optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantIn"])).optional(),
            "state": t.string().optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeIn"])
            ).optional(),
        }
    ).named(renames["SasPortalDeviceIn"])
    types["SasPortalDeviceOut"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "currentChannels": t.array(
                t.proxy(renames["SasPortalChannelWithScoreOut"])
            ).optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataOut"]).optional(),
            "fccId": t.string().optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantOut"])).optional(),
            "state": t.string().optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceOut"])
    types["SasPortalMoveDeviceRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveDeviceRequestIn"]
    )
    types["SasPortalMoveDeviceRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeviceRequestOut"])
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
    types["SasPortalSignDeviceRequestIn"] = t.struct(
        {"device": t.proxy(renames["SasPortalDeviceIn"])}
    ).named(renames["SasPortalSignDeviceRequestIn"])
    types["SasPortalSignDeviceRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["SasPortalDeviceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSignDeviceRequestOut"])
    types["SasPortalCustomerIn"] = t.struct(
        {
            "displayName": t.string(),
            "sasUserIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SasPortalCustomerIn"])
    types["SasPortalCustomerOut"] = t.struct(
        {
            "displayName": t.string(),
            "sasUserIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalCustomerOut"])
    types["SasPortalGenerateSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretRequestIn"])
    types["SasPortalGenerateSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGenerateSecretRequestOut"])
    types["SasPortalGenerateSecretResponseIn"] = t.struct(
        {"secret": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretResponseIn"])
    types["SasPortalGenerateSecretResponseOut"] = t.struct(
        {
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalGenerateSecretResponseOut"])
    types["SasPortalMoveDeploymentRequestIn"] = t.struct(
        {"destination": t.string()}
    ).named(renames["SasPortalMoveDeploymentRequestIn"])
    types["SasPortalMoveDeploymentRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeploymentRequestOut"])
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
    types["SasPortalProvisionDeploymentResponseIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["SasPortalProvisionDeploymentResponseIn"])
    types["SasPortalProvisionDeploymentResponseOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentResponseOut"])
    types["SasPortalMoveNodeRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveNodeRequestIn"]
    )
    types["SasPortalMoveNodeRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveNodeRequestOut"])
    types["SasPortalTestPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["SasPortalTestPermissionsResponseIn"])
    types["SasPortalTestPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalTestPermissionsResponseOut"])
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
    types["SasPortalDeviceMetadataIn"] = t.struct(
        {
            "interferenceCoordinationGroup": t.string().optional(),
            "antennaModel": t.string().optional(),
            "commonChannelGroup": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceMetadataIn"])
    types["SasPortalDeviceMetadataOut"] = t.struct(
        {
            "interferenceCoordinationGroup": t.string().optional(),
            "nrqzValidated": t.boolean().optional(),
            "antennaModel": t.string().optional(),
            "nrqzValidation": t.proxy(renames["SasPortalNrqzValidationOut"]).optional(),
            "commonChannelGroup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceMetadataOut"])
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
    types["SasPortalGetPolicyRequestIn"] = t.struct({"resource": t.string()}).named(
        renames["SasPortalGetPolicyRequestIn"]
    )
    types["SasPortalGetPolicyRequestOut"] = t.struct(
        {"resource": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGetPolicyRequestOut"])
    types["SasPortalProvisionDeploymentRequestIn"] = t.struct(
        {
            "newOrganizationDisplayName": t.string().optional(),
            "newDeploymentDisplayName": t.string().optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentRequestIn"])
    types["SasPortalProvisionDeploymentRequestOut"] = t.struct(
        {
            "newOrganizationDisplayName": t.string().optional(),
            "newDeploymentDisplayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentRequestOut"])
    types["SasPortalEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SasPortalEmptyIn"]
    )
    types["SasPortalEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalEmptyOut"])
    types["SasPortalDeviceModelIn"] = t.struct(
        {
            "vendor": t.string().optional(),
            "softwareVersion": t.string().optional(),
            "hardwareVersion": t.string().optional(),
            "firmwareVersion": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceModelIn"])
    types["SasPortalDeviceModelOut"] = t.struct(
        {
            "vendor": t.string().optional(),
            "softwareVersion": t.string().optional(),
            "hardwareVersion": t.string().optional(),
            "firmwareVersion": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceModelOut"])
    types["SasPortalDeploymentIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
        }
    ).named(renames["SasPortalDeploymentIn"])
    types["SasPortalDeploymentOut"] = t.struct(
        {
            "frns": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeploymentOut"])
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
    types["SasPortalOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["SasPortalStatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SasPortalOperationIn"])
    types["SasPortalOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SasPortalOperationOut"])
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
    types["SasPortalValidateInstallerRequestIn"] = t.struct(
        {"secret": t.string(), "installerId": t.string(), "encodedSecret": t.string()}
    ).named(renames["SasPortalValidateInstallerRequestIn"])
    types["SasPortalValidateInstallerRequestOut"] = t.struct(
        {
            "secret": t.string(),
            "installerId": t.string(),
            "encodedSecret": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalValidateInstallerRequestOut"])
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
    types["SasPortalNrqzValidationIn"] = t.struct(
        {
            "caseId": t.string().optional(),
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "cpiId": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["SasPortalNrqzValidationIn"])
    types["SasPortalNrqzValidationOut"] = t.struct(
        {
            "caseId": t.string().optional(),
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "cpiId": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalNrqzValidationOut"])
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
    functions["nodesGet"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDevicesUpdateSigned"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesGet"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesPatch"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesList"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesCreate"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesCreateSigned"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesDelete"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesMove"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesSignDevice"] = prod_tt_sasportal.post(
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
    functions["nodesNodesDeploymentsList"] = prod_tt_sasportal.post(
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
    functions["nodesNodesDeploymentsCreate"] = prod_tt_sasportal.post(
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
    functions["nodesNodesDevicesList"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["nodesNodesDevicesCreateSigned"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["nodesNodesNodesCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsMove"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsList"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsPatch"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsGet"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDelete"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDevicesCreateSigned"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["nodesDeploymentsDevicesList"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["nodesDeploymentsDevicesCreate"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["deploymentsGet"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesMove"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesUpdateSigned"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesPatch"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesSignDevice"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesGet"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["deploymentsDevicesDelete"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesGet"] = prod_tt_sasportal.post(
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
    functions["policiesTest"] = prod_tt_sasportal.post(
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
    functions["policiesSet"] = prod_tt_sasportal.post(
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
    functions["customersList"] = prod_tt_sasportal.post(
        "v1alpha1/customers:provisionDeployment",
        t.struct(
            {
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
                "newOrganizationDisplayName": t.string().optional(),
                "newDeploymentDisplayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalProvisionDeploymentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesMove"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesPatch"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesGet"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesDelete"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesList"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersNodesNodesList"] = prod_tt_sasportal.post(
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
    functions["customersNodesNodesCreate"] = prod_tt_sasportal.post(
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
    functions["customersNodesDevicesList"] = prod_tt_sasportal.post(
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
    functions["customersNodesDevicesCreate"] = prod_tt_sasportal.post(
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
    functions["customersNodesDevicesCreateSigned"] = prod_tt_sasportal.post(
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
    functions["customersNodesDeploymentsList"] = prod_tt_sasportal.post(
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
    functions["customersNodesDeploymentsCreate"] = prod_tt_sasportal.post(
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
    functions["customersDevicesUpdateSigned"] = prod_tt_sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["customersDevicesSignDevice"] = prod_tt_sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["customersDevicesDelete"] = prod_tt_sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["customersDevicesCreate"] = prod_tt_sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["customersDevicesCreateSigned"] = prod_tt_sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["customersDevicesGet"] = prod_tt_sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["customersDevicesList"] = prod_tt_sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["customersDevicesMove"] = prod_tt_sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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
    functions["customersDevicesPatch"] = prod_tt_sasportal.patch(
        "v1alpha1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "serialNumber": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "displayName": t.string().optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "state": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
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

    return Import(
        importer="prod_tt_sasportal", renames=renames, types=types, functions=functions
    )
