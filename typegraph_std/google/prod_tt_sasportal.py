from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_prod_tt_sasportal() -> Import:
    prod_tt_sasportal = HTTPRuntime("https://prod-tt-sasportal.googleapis.com/")

    renames = {
        "ErrorResponse": "_prod_tt_sasportal_1_ErrorResponse",
        "SasPortalListDevicesResponseIn": "_prod_tt_sasportal_2_SasPortalListDevicesResponseIn",
        "SasPortalListDevicesResponseOut": "_prod_tt_sasportal_3_SasPortalListDevicesResponseOut",
        "SasPortalInstallationParamsIn": "_prod_tt_sasportal_4_SasPortalInstallationParamsIn",
        "SasPortalInstallationParamsOut": "_prod_tt_sasportal_5_SasPortalInstallationParamsOut",
        "SasPortalDpaMoveListIn": "_prod_tt_sasportal_6_SasPortalDpaMoveListIn",
        "SasPortalDpaMoveListOut": "_prod_tt_sasportal_7_SasPortalDpaMoveListOut",
        "SasPortalTestPermissionsRequestIn": "_prod_tt_sasportal_8_SasPortalTestPermissionsRequestIn",
        "SasPortalTestPermissionsRequestOut": "_prod_tt_sasportal_9_SasPortalTestPermissionsRequestOut",
        "SasPortalUpdateSignedDeviceRequestIn": "_prod_tt_sasportal_10_SasPortalUpdateSignedDeviceRequestIn",
        "SasPortalUpdateSignedDeviceRequestOut": "_prod_tt_sasportal_11_SasPortalUpdateSignedDeviceRequestOut",
        "SasPortalValidateInstallerRequestIn": "_prod_tt_sasportal_12_SasPortalValidateInstallerRequestIn",
        "SasPortalValidateInstallerRequestOut": "_prod_tt_sasportal_13_SasPortalValidateInstallerRequestOut",
        "SasPortalSignDeviceRequestIn": "_prod_tt_sasportal_14_SasPortalSignDeviceRequestIn",
        "SasPortalSignDeviceRequestOut": "_prod_tt_sasportal_15_SasPortalSignDeviceRequestOut",
        "SasPortalGetPolicyRequestIn": "_prod_tt_sasportal_16_SasPortalGetPolicyRequestIn",
        "SasPortalGetPolicyRequestOut": "_prod_tt_sasportal_17_SasPortalGetPolicyRequestOut",
        "SasPortalStatusIn": "_prod_tt_sasportal_18_SasPortalStatusIn",
        "SasPortalStatusOut": "_prod_tt_sasportal_19_SasPortalStatusOut",
        "SasPortalListCustomersResponseIn": "_prod_tt_sasportal_20_SasPortalListCustomersResponseIn",
        "SasPortalListCustomersResponseOut": "_prod_tt_sasportal_21_SasPortalListCustomersResponseOut",
        "SasPortalFrequencyRangeIn": "_prod_tt_sasportal_22_SasPortalFrequencyRangeIn",
        "SasPortalFrequencyRangeOut": "_prod_tt_sasportal_23_SasPortalFrequencyRangeOut",
        "SasPortalGenerateSecretRequestIn": "_prod_tt_sasportal_24_SasPortalGenerateSecretRequestIn",
        "SasPortalGenerateSecretRequestOut": "_prod_tt_sasportal_25_SasPortalGenerateSecretRequestOut",
        "SasPortalNrqzValidationIn": "_prod_tt_sasportal_26_SasPortalNrqzValidationIn",
        "SasPortalNrqzValidationOut": "_prod_tt_sasportal_27_SasPortalNrqzValidationOut",
        "SasPortalDeviceModelIn": "_prod_tt_sasportal_28_SasPortalDeviceModelIn",
        "SasPortalDeviceModelOut": "_prod_tt_sasportal_29_SasPortalDeviceModelOut",
        "SasPortalListDeploymentsResponseIn": "_prod_tt_sasportal_30_SasPortalListDeploymentsResponseIn",
        "SasPortalListDeploymentsResponseOut": "_prod_tt_sasportal_31_SasPortalListDeploymentsResponseOut",
        "SasPortalChannelWithScoreIn": "_prod_tt_sasportal_32_SasPortalChannelWithScoreIn",
        "SasPortalChannelWithScoreOut": "_prod_tt_sasportal_33_SasPortalChannelWithScoreOut",
        "SasPortalValidateInstallerResponseIn": "_prod_tt_sasportal_34_SasPortalValidateInstallerResponseIn",
        "SasPortalValidateInstallerResponseOut": "_prod_tt_sasportal_35_SasPortalValidateInstallerResponseOut",
        "SasPortalTestPermissionsResponseIn": "_prod_tt_sasportal_36_SasPortalTestPermissionsResponseIn",
        "SasPortalTestPermissionsResponseOut": "_prod_tt_sasportal_37_SasPortalTestPermissionsResponseOut",
        "SasPortalMoveDeploymentRequestIn": "_prod_tt_sasportal_38_SasPortalMoveDeploymentRequestIn",
        "SasPortalMoveDeploymentRequestOut": "_prod_tt_sasportal_39_SasPortalMoveDeploymentRequestOut",
        "SasPortalAssignmentIn": "_prod_tt_sasportal_40_SasPortalAssignmentIn",
        "SasPortalAssignmentOut": "_prod_tt_sasportal_41_SasPortalAssignmentOut",
        "SasPortalOperationIn": "_prod_tt_sasportal_42_SasPortalOperationIn",
        "SasPortalOperationOut": "_prod_tt_sasportal_43_SasPortalOperationOut",
        "SasPortalSetPolicyRequestIn": "_prod_tt_sasportal_44_SasPortalSetPolicyRequestIn",
        "SasPortalSetPolicyRequestOut": "_prod_tt_sasportal_45_SasPortalSetPolicyRequestOut",
        "SasPortalMoveDeviceRequestIn": "_prod_tt_sasportal_46_SasPortalMoveDeviceRequestIn",
        "SasPortalMoveDeviceRequestOut": "_prod_tt_sasportal_47_SasPortalMoveDeviceRequestOut",
        "SasPortalListNodesResponseIn": "_prod_tt_sasportal_48_SasPortalListNodesResponseIn",
        "SasPortalListNodesResponseOut": "_prod_tt_sasportal_49_SasPortalListNodesResponseOut",
        "SasPortalMoveNodeRequestIn": "_prod_tt_sasportal_50_SasPortalMoveNodeRequestIn",
        "SasPortalMoveNodeRequestOut": "_prod_tt_sasportal_51_SasPortalMoveNodeRequestOut",
        "SasPortalCustomerIn": "_prod_tt_sasportal_52_SasPortalCustomerIn",
        "SasPortalCustomerOut": "_prod_tt_sasportal_53_SasPortalCustomerOut",
        "SasPortalCreateSignedDeviceRequestIn": "_prod_tt_sasportal_54_SasPortalCreateSignedDeviceRequestIn",
        "SasPortalCreateSignedDeviceRequestOut": "_prod_tt_sasportal_55_SasPortalCreateSignedDeviceRequestOut",
        "SasPortalDeviceAirInterfaceIn": "_prod_tt_sasportal_56_SasPortalDeviceAirInterfaceIn",
        "SasPortalDeviceAirInterfaceOut": "_prod_tt_sasportal_57_SasPortalDeviceAirInterfaceOut",
        "SasPortalDeploymentIn": "_prod_tt_sasportal_58_SasPortalDeploymentIn",
        "SasPortalDeploymentOut": "_prod_tt_sasportal_59_SasPortalDeploymentOut",
        "SasPortalProvisionDeploymentResponseIn": "_prod_tt_sasportal_60_SasPortalProvisionDeploymentResponseIn",
        "SasPortalProvisionDeploymentResponseOut": "_prod_tt_sasportal_61_SasPortalProvisionDeploymentResponseOut",
        "SasPortalDeviceMetadataIn": "_prod_tt_sasportal_62_SasPortalDeviceMetadataIn",
        "SasPortalDeviceMetadataOut": "_prod_tt_sasportal_63_SasPortalDeviceMetadataOut",
        "SasPortalDeviceGrantIn": "_prod_tt_sasportal_64_SasPortalDeviceGrantIn",
        "SasPortalDeviceGrantOut": "_prod_tt_sasportal_65_SasPortalDeviceGrantOut",
        "SasPortalPolicyIn": "_prod_tt_sasportal_66_SasPortalPolicyIn",
        "SasPortalPolicyOut": "_prod_tt_sasportal_67_SasPortalPolicyOut",
        "SasPortalDeviceIn": "_prod_tt_sasportal_68_SasPortalDeviceIn",
        "SasPortalDeviceOut": "_prod_tt_sasportal_69_SasPortalDeviceOut",
        "SasPortalNodeIn": "_prod_tt_sasportal_70_SasPortalNodeIn",
        "SasPortalNodeOut": "_prod_tt_sasportal_71_SasPortalNodeOut",
        "SasPortalProvisionDeploymentRequestIn": "_prod_tt_sasportal_72_SasPortalProvisionDeploymentRequestIn",
        "SasPortalProvisionDeploymentRequestOut": "_prod_tt_sasportal_73_SasPortalProvisionDeploymentRequestOut",
        "SasPortalEmptyIn": "_prod_tt_sasportal_74_SasPortalEmptyIn",
        "SasPortalEmptyOut": "_prod_tt_sasportal_75_SasPortalEmptyOut",
        "SasPortalGenerateSecretResponseIn": "_prod_tt_sasportal_76_SasPortalGenerateSecretResponseIn",
        "SasPortalGenerateSecretResponseOut": "_prod_tt_sasportal_77_SasPortalGenerateSecretResponseOut",
        "SasPortalDeviceConfigIn": "_prod_tt_sasportal_78_SasPortalDeviceConfigIn",
        "SasPortalDeviceConfigOut": "_prod_tt_sasportal_79_SasPortalDeviceConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SasPortalInstallationParamsIn"] = t.struct(
        {
            "antennaAzimuth": t.integer().optional(),
            "height": t.number().optional(),
            "antennaModel": t.string().optional(),
            "verticalAccuracy": t.number().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "eirpCapability": t.integer().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "horizontalAccuracy": t.number().optional(),
            "antennaGain": t.integer().optional(),
            "indoorDeployment": t.boolean().optional(),
            "heightType": t.string().optional(),
            "latitude": t.number().optional(),
            "longitude": t.number().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "antennaGainNewField": t.number().optional(),
            "antennaDowntilt": t.integer().optional(),
        }
    ).named(renames["SasPortalInstallationParamsIn"])
    types["SasPortalInstallationParamsOut"] = t.struct(
        {
            "antennaAzimuth": t.integer().optional(),
            "height": t.number().optional(),
            "antennaModel": t.string().optional(),
            "verticalAccuracy": t.number().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "eirpCapability": t.integer().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "horizontalAccuracy": t.number().optional(),
            "antennaGain": t.integer().optional(),
            "indoorDeployment": t.boolean().optional(),
            "heightType": t.string().optional(),
            "latitude": t.number().optional(),
            "longitude": t.number().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "antennaGainNewField": t.number().optional(),
            "antennaDowntilt": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalInstallationParamsOut"])
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
    types["SasPortalTestPermissionsRequestIn"] = t.struct(
        {"resource": t.string(), "permissions": t.array(t.string()).optional()}
    ).named(renames["SasPortalTestPermissionsRequestIn"])
    types["SasPortalTestPermissionsRequestOut"] = t.struct(
        {
            "resource": t.string(),
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalTestPermissionsRequestOut"])
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
    types["SasPortalValidateInstallerRequestIn"] = t.struct(
        {"encodedSecret": t.string(), "installerId": t.string(), "secret": t.string()}
    ).named(renames["SasPortalValidateInstallerRequestIn"])
    types["SasPortalValidateInstallerRequestOut"] = t.struct(
        {
            "encodedSecret": t.string(),
            "installerId": t.string(),
            "secret": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalValidateInstallerRequestOut"])
    types["SasPortalSignDeviceRequestIn"] = t.struct(
        {"device": t.proxy(renames["SasPortalDeviceIn"])}
    ).named(renames["SasPortalSignDeviceRequestIn"])
    types["SasPortalSignDeviceRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["SasPortalDeviceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSignDeviceRequestOut"])
    types["SasPortalGetPolicyRequestIn"] = t.struct({"resource": t.string()}).named(
        renames["SasPortalGetPolicyRequestIn"]
    )
    types["SasPortalGetPolicyRequestOut"] = t.struct(
        {"resource": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGetPolicyRequestOut"])
    types["SasPortalStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["SasPortalStatusIn"])
    types["SasPortalStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalStatusOut"])
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
    types["SasPortalGenerateSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretRequestIn"])
    types["SasPortalGenerateSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGenerateSecretRequestOut"])
    types["SasPortalNrqzValidationIn"] = t.struct(
        {
            "caseId": t.string().optional(),
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "state": t.string().optional(),
            "cpiId": t.string().optional(),
        }
    ).named(renames["SasPortalNrqzValidationIn"])
    types["SasPortalNrqzValidationOut"] = t.struct(
        {
            "caseId": t.string().optional(),
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "state": t.string().optional(),
            "cpiId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalNrqzValidationOut"])
    types["SasPortalDeviceModelIn"] = t.struct(
        {
            "softwareVersion": t.string().optional(),
            "hardwareVersion": t.string().optional(),
            "vendor": t.string().optional(),
            "firmwareVersion": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceModelIn"])
    types["SasPortalDeviceModelOut"] = t.struct(
        {
            "softwareVersion": t.string().optional(),
            "hardwareVersion": t.string().optional(),
            "vendor": t.string().optional(),
            "firmwareVersion": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceModelOut"])
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
    types["SasPortalValidateInstallerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalValidateInstallerResponseIn"])
    types["SasPortalValidateInstallerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalValidateInstallerResponseOut"])
    types["SasPortalTestPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["SasPortalTestPermissionsResponseIn"])
    types["SasPortalTestPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalTestPermissionsResponseOut"])
    types["SasPortalMoveDeploymentRequestIn"] = t.struct(
        {"destination": t.string()}
    ).named(renames["SasPortalMoveDeploymentRequestIn"])
    types["SasPortalMoveDeploymentRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeploymentRequestOut"])
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
    types["SasPortalOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["SasPortalStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SasPortalOperationIn"])
    types["SasPortalOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SasPortalOperationOut"])
    types["SasPortalSetPolicyRequestIn"] = t.struct(
        {
            "resource": t.string(),
            "disableNotification": t.boolean().optional(),
            "policy": t.proxy(renames["SasPortalPolicyIn"]),
        }
    ).named(renames["SasPortalSetPolicyRequestIn"])
    types["SasPortalSetPolicyRequestOut"] = t.struct(
        {
            "resource": t.string(),
            "disableNotification": t.boolean().optional(),
            "policy": t.proxy(renames["SasPortalPolicyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSetPolicyRequestOut"])
    types["SasPortalMoveDeviceRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveDeviceRequestIn"]
    )
    types["SasPortalMoveDeviceRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeviceRequestOut"])
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
    types["SasPortalMoveNodeRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveNodeRequestIn"]
    )
    types["SasPortalMoveNodeRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveNodeRequestOut"])
    types["SasPortalCustomerIn"] = t.struct(
        {
            "sasUserIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
        }
    ).named(renames["SasPortalCustomerIn"])
    types["SasPortalCustomerOut"] = t.struct(
        {
            "sasUserIds": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "displayName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalCustomerOut"])
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
    types["SasPortalDeploymentIn"] = t.struct(
        {
            "sasUserIds": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["SasPortalDeploymentIn"])
    types["SasPortalDeploymentOut"] = t.struct(
        {
            "frns": t.array(t.string()).optional(),
            "sasUserIds": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeploymentOut"])
    types["SasPortalProvisionDeploymentResponseIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["SasPortalProvisionDeploymentResponseIn"])
    types["SasPortalProvisionDeploymentResponseOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentResponseOut"])
    types["SasPortalDeviceMetadataIn"] = t.struct(
        {
            "commonChannelGroup": t.string().optional(),
            "antennaModel": t.string().optional(),
            "interferenceCoordinationGroup": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceMetadataIn"])
    types["SasPortalDeviceMetadataOut"] = t.struct(
        {
            "nrqzValidation": t.proxy(renames["SasPortalNrqzValidationOut"]).optional(),
            "nrqzValidated": t.boolean().optional(),
            "commonChannelGroup": t.string().optional(),
            "antennaModel": t.string().optional(),
            "interferenceCoordinationGroup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceMetadataOut"])
    types["SasPortalDeviceGrantIn"] = t.struct(
        {
            "channelType": t.string().optional(),
            "grantId": t.string().optional(),
            "maxEirp": t.number().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
            "expireTime": t.string().optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListIn"])).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceGrantIn"])
    types["SasPortalDeviceGrantOut"] = t.struct(
        {
            "channelType": t.string().optional(),
            "grantId": t.string().optional(),
            "maxEirp": t.number().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "expireTime": t.string().optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListOut"])).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceGrantOut"])
    types["SasPortalPolicyIn"] = t.struct(
        {
            "assignments": t.array(
                t.proxy(renames["SasPortalAssignmentIn"])
            ).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["SasPortalPolicyIn"])
    types["SasPortalPolicyOut"] = t.struct(
        {
            "assignments": t.array(
                t.proxy(renames["SasPortalAssignmentOut"])
            ).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalPolicyOut"])
    types["SasPortalDeviceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "serialNumber": t.string().optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeIn"])
            ).optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataIn"]).optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantIn"])).optional(),
            "state": t.string().optional(),
            "fccId": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceIn"])
    types["SasPortalDeviceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "serialNumber": t.string().optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeOut"])
            ).optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataOut"]).optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantOut"])).optional(),
            "currentChannels": t.array(
                t.proxy(renames["SasPortalChannelWithScoreOut"])
            ).optional(),
            "state": t.string().optional(),
            "fccId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceOut"])
    types["SasPortalNodeIn"] = t.struct(
        {
            "sasUserIds": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SasPortalNodeIn"])
    types["SasPortalNodeOut"] = t.struct(
        {
            "sasUserIds": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalNodeOut"])
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
    types["SasPortalDeviceConfigIn"] = t.struct(
        {
            "userId": t.string().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceIn"]
            ).optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsIn"]
            ).optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
            "isSigned": t.boolean().optional(),
            "callSign": t.string().optional(),
            "updateTime": t.string().optional(),
            "measurementCapabilities": t.array(t.string()).optional(),
            "model": t.proxy(renames["SasPortalDeviceModelIn"]).optional(),
        }
    ).named(renames["SasPortalDeviceConfigIn"])
    types["SasPortalDeviceConfigOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceOut"]
            ).optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsOut"]
            ).optional(),
            "state": t.string().optional(),
            "category": t.string().optional(),
            "isSigned": t.boolean().optional(),
            "callSign": t.string().optional(),
            "updateTime": t.string().optional(),
            "measurementCapabilities": t.array(t.string()).optional(),
            "model": t.proxy(renames["SasPortalDeviceModelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceConfigOut"])

    functions = {}
    functions["customersGet"] = prod_tt_sasportal.post(
        "v1alpha1/customers:provisionDeployment",
        t.struct(
            {
                "newDeploymentDisplayName": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
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
                "newDeploymentDisplayName": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
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
                "newDeploymentDisplayName": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
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
                "newDeploymentDisplayName": t.string().optional(),
                "newOrganizationDisplayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalProvisionDeploymentResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesDelete"] = prod_tt_sasportal.post(
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
    functions["customersDevicesList"] = prod_tt_sasportal.post(
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
    functions["customersDevicesCreate"] = prod_tt_sasportal.post(
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
    functions["customersDevicesSignDevice"] = prod_tt_sasportal.post(
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
    functions["customersDevicesGet"] = prod_tt_sasportal.post(
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
    functions["customersDevicesPatch"] = prod_tt_sasportal.post(
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
    functions["customersDevicesUpdateSigned"] = prod_tt_sasportal.post(
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
    functions["customersDevicesCreateSigned"] = prod_tt_sasportal.post(
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
    functions["customersDevicesMove"] = prod_tt_sasportal.post(
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
    functions["customersDeploymentsCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsMove"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsGet"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDelete"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsPatch"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsList"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDevicesCreate"] = prod_tt_sasportal.get(
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
    functions["customersDeploymentsDevicesCreateSigned"] = prod_tt_sasportal.get(
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
    functions["customersDeploymentsDevicesList"] = prod_tt_sasportal.get(
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
                "sasUserIds": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
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
                "sasUserIds": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
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
                "encodedDevice": t.string(),
                "installerId": t.string(),
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
                "encodedDevice": t.string(),
                "installerId": t.string(),
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
                "encodedDevice": t.string(),
                "installerId": t.string(),
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
    functions["deploymentsGet"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalDeploymentOut"]),
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
    functions["policiesTest"] = prod_tt_sasportal.post(
        "v1alpha1/policies:get",
        t.struct({"resource": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesSet"] = prod_tt_sasportal.post(
        "v1alpha1/policies:get",
        t.struct({"resource": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesGet"] = prod_tt_sasportal.post(
        "v1alpha1/policies:get",
        t.struct({"resource": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalPolicyOut"]),
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
    functions["nodesNodesNodesList"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "sasUserIds": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesNodesCreate"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/nodes",
        t.struct(
            {
                "parent": t.string(),
                "sasUserIds": t.array(t.string()).optional(),
                "displayName": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesCreate"] = prod_tt_sasportal.post(
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
    functions["nodesNodesDevicesList"] = prod_tt_sasportal.post(
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
    functions["nodesNodesDevicesCreateSigned"] = prod_tt_sasportal.post(
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
    functions["nodesDeploymentsGet"] = prod_tt_sasportal.delete(
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
    functions["nodesDeploymentsMove"] = prod_tt_sasportal.delete(
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
    functions["nodesDeploymentsDelete"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDevicesList"] = prod_tt_sasportal.post(
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
    functions["nodesDeploymentsDevicesCreate"] = prod_tt_sasportal.post(
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
    functions["nodesDeploymentsDevicesCreateSigned"] = prod_tt_sasportal.post(
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

    return Import(
        importer="prod_tt_sasportal",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
