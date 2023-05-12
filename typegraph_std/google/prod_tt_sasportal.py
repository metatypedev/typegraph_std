from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_prod_tt_sasportal() -> Import:
    prod_tt_sasportal = HTTPRuntime("https://prod-tt-sasportal.googleapis.com/")

    renames = {
        "ErrorResponse": "_prod_tt_sasportal_1_ErrorResponse",
        "SasPortalDeviceAirInterfaceIn": "_prod_tt_sasportal_2_SasPortalDeviceAirInterfaceIn",
        "SasPortalDeviceAirInterfaceOut": "_prod_tt_sasportal_3_SasPortalDeviceAirInterfaceOut",
        "SasPortalListCustomersResponseIn": "_prod_tt_sasportal_4_SasPortalListCustomersResponseIn",
        "SasPortalListCustomersResponseOut": "_prod_tt_sasportal_5_SasPortalListCustomersResponseOut",
        "SasPortalTestPermissionsResponseIn": "_prod_tt_sasportal_6_SasPortalTestPermissionsResponseIn",
        "SasPortalTestPermissionsResponseOut": "_prod_tt_sasportal_7_SasPortalTestPermissionsResponseOut",
        "SasPortalListDeploymentsResponseIn": "_prod_tt_sasportal_8_SasPortalListDeploymentsResponseIn",
        "SasPortalListDeploymentsResponseOut": "_prod_tt_sasportal_9_SasPortalListDeploymentsResponseOut",
        "SasPortalProvisionDeploymentRequestIn": "_prod_tt_sasportal_10_SasPortalProvisionDeploymentRequestIn",
        "SasPortalProvisionDeploymentRequestOut": "_prod_tt_sasportal_11_SasPortalProvisionDeploymentRequestOut",
        "SasPortalListDevicesResponseIn": "_prod_tt_sasportal_12_SasPortalListDevicesResponseIn",
        "SasPortalListDevicesResponseOut": "_prod_tt_sasportal_13_SasPortalListDevicesResponseOut",
        "SasPortalCreateSignedDeviceRequestIn": "_prod_tt_sasportal_14_SasPortalCreateSignedDeviceRequestIn",
        "SasPortalCreateSignedDeviceRequestOut": "_prod_tt_sasportal_15_SasPortalCreateSignedDeviceRequestOut",
        "SasPortalDeploymentIn": "_prod_tt_sasportal_16_SasPortalDeploymentIn",
        "SasPortalDeploymentOut": "_prod_tt_sasportal_17_SasPortalDeploymentOut",
        "SasPortalDeviceConfigIn": "_prod_tt_sasportal_18_SasPortalDeviceConfigIn",
        "SasPortalDeviceConfigOut": "_prod_tt_sasportal_19_SasPortalDeviceConfigOut",
        "SasPortalEmptyIn": "_prod_tt_sasportal_20_SasPortalEmptyIn",
        "SasPortalEmptyOut": "_prod_tt_sasportal_21_SasPortalEmptyOut",
        "SasPortalOperationIn": "_prod_tt_sasportal_22_SasPortalOperationIn",
        "SasPortalOperationOut": "_prod_tt_sasportal_23_SasPortalOperationOut",
        "SasPortalGenerateSecretResponseIn": "_prod_tt_sasportal_24_SasPortalGenerateSecretResponseIn",
        "SasPortalGenerateSecretResponseOut": "_prod_tt_sasportal_25_SasPortalGenerateSecretResponseOut",
        "SasPortalSetPolicyRequestIn": "_prod_tt_sasportal_26_SasPortalSetPolicyRequestIn",
        "SasPortalSetPolicyRequestOut": "_prod_tt_sasportal_27_SasPortalSetPolicyRequestOut",
        "SasPortalDpaMoveListIn": "_prod_tt_sasportal_28_SasPortalDpaMoveListIn",
        "SasPortalDpaMoveListOut": "_prod_tt_sasportal_29_SasPortalDpaMoveListOut",
        "SasPortalChannelWithScoreIn": "_prod_tt_sasportal_30_SasPortalChannelWithScoreIn",
        "SasPortalChannelWithScoreOut": "_prod_tt_sasportal_31_SasPortalChannelWithScoreOut",
        "SasPortalValidateInstallerResponseIn": "_prod_tt_sasportal_32_SasPortalValidateInstallerResponseIn",
        "SasPortalValidateInstallerResponseOut": "_prod_tt_sasportal_33_SasPortalValidateInstallerResponseOut",
        "SasPortalGenerateSecretRequestIn": "_prod_tt_sasportal_34_SasPortalGenerateSecretRequestIn",
        "SasPortalGenerateSecretRequestOut": "_prod_tt_sasportal_35_SasPortalGenerateSecretRequestOut",
        "SasPortalValidateInstallerRequestIn": "_prod_tt_sasportal_36_SasPortalValidateInstallerRequestIn",
        "SasPortalValidateInstallerRequestOut": "_prod_tt_sasportal_37_SasPortalValidateInstallerRequestOut",
        "SasPortalUpdateSignedDeviceRequestIn": "_prod_tt_sasportal_38_SasPortalUpdateSignedDeviceRequestIn",
        "SasPortalUpdateSignedDeviceRequestOut": "_prod_tt_sasportal_39_SasPortalUpdateSignedDeviceRequestOut",
        "SasPortalDeviceModelIn": "_prod_tt_sasportal_40_SasPortalDeviceModelIn",
        "SasPortalDeviceModelOut": "_prod_tt_sasportal_41_SasPortalDeviceModelOut",
        "SasPortalAssignmentIn": "_prod_tt_sasportal_42_SasPortalAssignmentIn",
        "SasPortalAssignmentOut": "_prod_tt_sasportal_43_SasPortalAssignmentOut",
        "SasPortalSignDeviceRequestIn": "_prod_tt_sasportal_44_SasPortalSignDeviceRequestIn",
        "SasPortalSignDeviceRequestOut": "_prod_tt_sasportal_45_SasPortalSignDeviceRequestOut",
        "SasPortalNrqzValidationIn": "_prod_tt_sasportal_46_SasPortalNrqzValidationIn",
        "SasPortalNrqzValidationOut": "_prod_tt_sasportal_47_SasPortalNrqzValidationOut",
        "SasPortalTestPermissionsRequestIn": "_prod_tt_sasportal_48_SasPortalTestPermissionsRequestIn",
        "SasPortalTestPermissionsRequestOut": "_prod_tt_sasportal_49_SasPortalTestPermissionsRequestOut",
        "SasPortalCustomerIn": "_prod_tt_sasportal_50_SasPortalCustomerIn",
        "SasPortalCustomerOut": "_prod_tt_sasportal_51_SasPortalCustomerOut",
        "SasPortalProvisionDeploymentResponseIn": "_prod_tt_sasportal_52_SasPortalProvisionDeploymentResponseIn",
        "SasPortalProvisionDeploymentResponseOut": "_prod_tt_sasportal_53_SasPortalProvisionDeploymentResponseOut",
        "SasPortalDeviceGrantIn": "_prod_tt_sasportal_54_SasPortalDeviceGrantIn",
        "SasPortalDeviceGrantOut": "_prod_tt_sasportal_55_SasPortalDeviceGrantOut",
        "SasPortalGetPolicyRequestIn": "_prod_tt_sasportal_56_SasPortalGetPolicyRequestIn",
        "SasPortalGetPolicyRequestOut": "_prod_tt_sasportal_57_SasPortalGetPolicyRequestOut",
        "SasPortalMoveDeploymentRequestIn": "_prod_tt_sasportal_58_SasPortalMoveDeploymentRequestIn",
        "SasPortalMoveDeploymentRequestOut": "_prod_tt_sasportal_59_SasPortalMoveDeploymentRequestOut",
        "SasPortalPolicyIn": "_prod_tt_sasportal_60_SasPortalPolicyIn",
        "SasPortalPolicyOut": "_prod_tt_sasportal_61_SasPortalPolicyOut",
        "SasPortalListNodesResponseIn": "_prod_tt_sasportal_62_SasPortalListNodesResponseIn",
        "SasPortalListNodesResponseOut": "_prod_tt_sasportal_63_SasPortalListNodesResponseOut",
        "SasPortalMoveNodeRequestIn": "_prod_tt_sasportal_64_SasPortalMoveNodeRequestIn",
        "SasPortalMoveNodeRequestOut": "_prod_tt_sasportal_65_SasPortalMoveNodeRequestOut",
        "SasPortalDeviceMetadataIn": "_prod_tt_sasportal_66_SasPortalDeviceMetadataIn",
        "SasPortalDeviceMetadataOut": "_prod_tt_sasportal_67_SasPortalDeviceMetadataOut",
        "SasPortalMoveDeviceRequestIn": "_prod_tt_sasportal_68_SasPortalMoveDeviceRequestIn",
        "SasPortalMoveDeviceRequestOut": "_prod_tt_sasportal_69_SasPortalMoveDeviceRequestOut",
        "SasPortalNodeIn": "_prod_tt_sasportal_70_SasPortalNodeIn",
        "SasPortalNodeOut": "_prod_tt_sasportal_71_SasPortalNodeOut",
        "SasPortalInstallationParamsIn": "_prod_tt_sasportal_72_SasPortalInstallationParamsIn",
        "SasPortalInstallationParamsOut": "_prod_tt_sasportal_73_SasPortalInstallationParamsOut",
        "SasPortalStatusIn": "_prod_tt_sasportal_74_SasPortalStatusIn",
        "SasPortalStatusOut": "_prod_tt_sasportal_75_SasPortalStatusOut",
        "SasPortalFrequencyRangeIn": "_prod_tt_sasportal_76_SasPortalFrequencyRangeIn",
        "SasPortalFrequencyRangeOut": "_prod_tt_sasportal_77_SasPortalFrequencyRangeOut",
        "SasPortalDeviceIn": "_prod_tt_sasportal_78_SasPortalDeviceIn",
        "SasPortalDeviceOut": "_prod_tt_sasportal_79_SasPortalDeviceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["SasPortalTestPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["SasPortalTestPermissionsResponseIn"])
    types["SasPortalTestPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalTestPermissionsResponseOut"])
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
    types["SasPortalDeviceConfigIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsIn"]
            ).optional(),
            "measurementCapabilities": t.array(t.string()).optional(),
            "category": t.string().optional(),
            "isSigned": t.boolean().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceIn"]
            ).optional(),
            "model": t.proxy(renames["SasPortalDeviceModelIn"]).optional(),
            "state": t.string().optional(),
            "userId": t.string().optional(),
            "callSign": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceConfigIn"])
    types["SasPortalDeviceConfigOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "installationParams": t.proxy(
                renames["SasPortalInstallationParamsOut"]
            ).optional(),
            "measurementCapabilities": t.array(t.string()).optional(),
            "category": t.string().optional(),
            "isSigned": t.boolean().optional(),
            "airInterface": t.proxy(
                renames["SasPortalDeviceAirInterfaceOut"]
            ).optional(),
            "model": t.proxy(renames["SasPortalDeviceModelOut"]).optional(),
            "state": t.string().optional(),
            "userId": t.string().optional(),
            "callSign": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceConfigOut"])
    types["SasPortalEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["SasPortalEmptyIn"]
    )
    types["SasPortalEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalEmptyOut"])
    types["SasPortalOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["SasPortalStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SasPortalOperationIn"])
    types["SasPortalOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SasPortalOperationOut"])
    types["SasPortalGenerateSecretResponseIn"] = t.struct(
        {"secret": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretResponseIn"])
    types["SasPortalGenerateSecretResponseOut"] = t.struct(
        {
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalGenerateSecretResponseOut"])
    types["SasPortalSetPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["SasPortalPolicyIn"]),
            "resource": t.string(),
            "disableNotification": t.boolean().optional(),
        }
    ).named(renames["SasPortalSetPolicyRequestIn"])
    types["SasPortalSetPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["SasPortalPolicyOut"]),
            "resource": t.string(),
            "disableNotification": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSetPolicyRequestOut"])
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
    types["SasPortalChannelWithScoreIn"] = t.struct(
        {
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
            "score": t.number().optional(),
        }
    ).named(renames["SasPortalChannelWithScoreIn"])
    types["SasPortalChannelWithScoreOut"] = t.struct(
        {
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalChannelWithScoreOut"])
    types["SasPortalValidateInstallerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalValidateInstallerResponseIn"])
    types["SasPortalValidateInstallerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalValidateInstallerResponseOut"])
    types["SasPortalGenerateSecretRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["SasPortalGenerateSecretRequestIn"])
    types["SasPortalGenerateSecretRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGenerateSecretRequestOut"])
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
    types["SasPortalDeviceModelIn"] = t.struct(
        {
            "firmwareVersion": t.string().optional(),
            "softwareVersion": t.string().optional(),
            "name": t.string().optional(),
            "hardwareVersion": t.string().optional(),
            "vendor": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceModelIn"])
    types["SasPortalDeviceModelOut"] = t.struct(
        {
            "firmwareVersion": t.string().optional(),
            "softwareVersion": t.string().optional(),
            "name": t.string().optional(),
            "hardwareVersion": t.string().optional(),
            "vendor": t.string().optional(),
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
    types["SasPortalSignDeviceRequestIn"] = t.struct(
        {"device": t.proxy(renames["SasPortalDeviceIn"])}
    ).named(renames["SasPortalSignDeviceRequestIn"])
    types["SasPortalSignDeviceRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["SasPortalDeviceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalSignDeviceRequestOut"])
    types["SasPortalNrqzValidationIn"] = t.struct(
        {
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "caseId": t.string().optional(),
            "state": t.string().optional(),
            "cpiId": t.string().optional(),
        }
    ).named(renames["SasPortalNrqzValidationIn"])
    types["SasPortalNrqzValidationOut"] = t.struct(
        {
            "longitude": t.number().optional(),
            "latitude": t.number().optional(),
            "caseId": t.string().optional(),
            "state": t.string().optional(),
            "cpiId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalNrqzValidationOut"])
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
    types["SasPortalProvisionDeploymentResponseIn"] = t.struct(
        {"errorMessage": t.string().optional()}
    ).named(renames["SasPortalProvisionDeploymentResponseIn"])
    types["SasPortalProvisionDeploymentResponseOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalProvisionDeploymentResponseOut"])
    types["SasPortalDeviceGrantIn"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "state": t.string().optional(),
            "channelType": t.string().optional(),
            "maxEirp": t.number().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListIn"])).optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeIn"]).optional(),
            "grantId": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceGrantIn"])
    types["SasPortalDeviceGrantOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "state": t.string().optional(),
            "channelType": t.string().optional(),
            "maxEirp": t.number().optional(),
            "moveList": t.array(t.proxy(renames["SasPortalDpaMoveListOut"])).optional(),
            "lastHeartbeatTransmitExpireTime": t.string().optional(),
            "suspensionReason": t.array(t.string()).optional(),
            "frequencyRange": t.proxy(renames["SasPortalFrequencyRangeOut"]).optional(),
            "grantId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceGrantOut"])
    types["SasPortalGetPolicyRequestIn"] = t.struct({"resource": t.string()}).named(
        renames["SasPortalGetPolicyRequestIn"]
    )
    types["SasPortalGetPolicyRequestOut"] = t.struct(
        {"resource": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["SasPortalGetPolicyRequestOut"])
    types["SasPortalMoveDeploymentRequestIn"] = t.struct(
        {"destination": t.string()}
    ).named(renames["SasPortalMoveDeploymentRequestIn"])
    types["SasPortalMoveDeploymentRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeploymentRequestOut"])
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
    types["SasPortalListNodesResponseIn"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["SasPortalNodeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SasPortalListNodesResponseIn"])
    types["SasPortalListNodesResponseOut"] = t.struct(
        {
            "nodes": t.array(t.proxy(renames["SasPortalNodeOut"])).optional(),
            "nextPageToken": t.string().optional(),
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
    types["SasPortalDeviceMetadataIn"] = t.struct(
        {
            "interferenceCoordinationGroup": t.string().optional(),
            "antennaModel": t.string().optional(),
            "commonChannelGroup": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceMetadataIn"])
    types["SasPortalDeviceMetadataOut"] = t.struct(
        {
            "nrqzValidated": t.boolean().optional(),
            "interferenceCoordinationGroup": t.string().optional(),
            "nrqzValidation": t.proxy(renames["SasPortalNrqzValidationOut"]).optional(),
            "antennaModel": t.string().optional(),
            "commonChannelGroup": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceMetadataOut"])
    types["SasPortalMoveDeviceRequestIn"] = t.struct({"destination": t.string()}).named(
        renames["SasPortalMoveDeviceRequestIn"]
    )
    types["SasPortalMoveDeviceRequestOut"] = t.struct(
        {
            "destination": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalMoveDeviceRequestOut"])
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
    types["SasPortalInstallationParamsIn"] = t.struct(
        {
            "antennaAzimuth": t.integer().optional(),
            "longitude": t.number().optional(),
            "eirpCapability": t.integer().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "latitude": t.number().optional(),
            "antennaGain": t.integer().optional(),
            "indoorDeployment": t.boolean().optional(),
            "height": t.number().optional(),
            "antennaGainNewField": t.number().optional(),
            "verticalAccuracy": t.number().optional(),
            "antennaModel": t.string().optional(),
            "antennaDowntilt": t.integer().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "heightType": t.string().optional(),
            "horizontalAccuracy": t.number().optional(),
        }
    ).named(renames["SasPortalInstallationParamsIn"])
    types["SasPortalInstallationParamsOut"] = t.struct(
        {
            "antennaAzimuth": t.integer().optional(),
            "longitude": t.number().optional(),
            "eirpCapability": t.integer().optional(),
            "antennaBeamwidth": t.integer().optional(),
            "eirpCapabilityNewField": t.number().optional(),
            "latitude": t.number().optional(),
            "antennaGain": t.integer().optional(),
            "indoorDeployment": t.boolean().optional(),
            "height": t.number().optional(),
            "antennaGainNewField": t.number().optional(),
            "verticalAccuracy": t.number().optional(),
            "antennaModel": t.string().optional(),
            "antennaDowntilt": t.integer().optional(),
            "cpeCbsdIndication": t.boolean().optional(),
            "heightType": t.string().optional(),
            "horizontalAccuracy": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalInstallationParamsOut"])
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
    types["SasPortalDeviceIn"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "name": t.string().optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "displayName": t.string().optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataIn"]).optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantIn"])).optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
            "fccId": t.string().optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeIn"])
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["SasPortalDeviceIn"])
    types["SasPortalDeviceOut"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "currentChannels": t.array(
                t.proxy(renames["SasPortalChannelWithScoreOut"])
            ).optional(),
            "name": t.string().optional(),
            "activeConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "displayName": t.string().optional(),
            "deviceMetadata": t.proxy(renames["SasPortalDeviceMetadataOut"]).optional(),
            "grants": t.array(t.proxy(renames["SasPortalDeviceGrantOut"])).optional(),
            "preloadedConfig": t.proxy(renames["SasPortalDeviceConfigOut"]).optional(),
            "fccId": t.string().optional(),
            "grantRangeAllowlists": t.array(
                t.proxy(renames["SasPortalFrequencyRangeOut"])
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SasPortalDeviceOut"])

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
    functions["customersPatch"] = prod_tt_sasportal.get(
        "v1alpha1/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersProvisionDeployment"] = prod_tt_sasportal.get(
        "v1alpha1/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersGet"] = prod_tt_sasportal.get(
        "v1alpha1/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersList"] = prod_tt_sasportal.get(
        "v1alpha1/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesPatch"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesMove"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesCreateSigned"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesSignDevice"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesUpdateSigned"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesDelete"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesGet"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesList"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsList"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsPatch"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsMove"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsCreate"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsGet"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDeploymentsDelete"] = prod_tt_sasportal.delete(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalEmptyOut"]),
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
    functions["customersNodesList"] = prod_tt_sasportal.get(
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
    functions["customersNodesMove"] = prod_tt_sasportal.get(
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
    functions["customersNodesCreate"] = prod_tt_sasportal.get(
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
    functions["customersNodesNodesCreate"] = prod_tt_sasportal.get(
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
    functions["customersNodesNodesList"] = prod_tt_sasportal.get(
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
    functions["policiesGet"] = prod_tt_sasportal.post(
        "v1alpha1/policies:set",
        t.struct(
            {
                "policy": t.proxy(renames["SasPortalPolicyIn"]),
                "resource": t.string(),
                "disableNotification": t.boolean().optional(),
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
                "policy": t.proxy(renames["SasPortalPolicyIn"]),
                "resource": t.string(),
                "disableNotification": t.boolean().optional(),
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
                "policy": t.proxy(renames["SasPortalPolicyIn"]),
                "resource": t.string(),
                "disableNotification": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
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
    functions["nodesDeploymentsPatch"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsGet"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDelete"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsMove"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsList"] = prod_tt_sasportal.get(
        "v1alpha1/{parent}/deployments",
        t.struct(
            {
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListDeploymentsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesDeploymentsDevicesCreateSigned"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "serialNumber": t.string().optional(),
                "name": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "displayName": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "state": t.string().optional(),
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
                "name": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "displayName": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "state": t.string().optional(),
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
                "name": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "displayName": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "state": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalDeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDelete"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesMove"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesList"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesCreate"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesPatch"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesGet"] = prod_tt_sasportal.get(
        "v1alpha1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SasPortalNodeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["nodesNodesDevicesList"] = prod_tt_sasportal.post(
        "v1alpha1/{parent}/devices",
        t.struct(
            {
                "parent": t.string(),
                "serialNumber": t.string().optional(),
                "name": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "displayName": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "state": t.string().optional(),
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
                "name": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "displayName": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "state": t.string().optional(),
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
                "name": t.string().optional(),
                "activeConfig": t.proxy(renames["SasPortalDeviceConfigIn"]).optional(),
                "displayName": t.string().optional(),
                "deviceMetadata": t.proxy(
                    renames["SasPortalDeviceMetadataIn"]
                ).optional(),
                "grants": t.array(
                    t.proxy(renames["SasPortalDeviceGrantIn"])
                ).optional(),
                "preloadedConfig": t.proxy(
                    renames["SasPortalDeviceConfigIn"]
                ).optional(),
                "fccId": t.string().optional(),
                "grantRangeAllowlists": t.array(
                    t.proxy(renames["SasPortalFrequencyRangeIn"])
                ).optional(),
                "state": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SasPortalListNodesResponseOut"]),
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
    functions["nodesDevicesMove"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesList"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesUpdateSigned"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesSignDevice"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesCreate"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesDelete"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesGet"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesPatch"] = prod_tt_sasportal.post(
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
    functions["nodesDevicesCreateSigned"] = prod_tt_sasportal.post(
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
    functions["deploymentsDevicesGet"] = prod_tt_sasportal.post(
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
    functions["deploymentsDevicesMove"] = prod_tt_sasportal.post(
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
    functions["deploymentsDevicesDelete"] = prod_tt_sasportal.post(
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
    functions["deploymentsDevicesPatch"] = prod_tt_sasportal.post(
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
    functions["deploymentsDevicesUpdateSigned"] = prod_tt_sasportal.post(
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
    functions["deploymentsDevicesSignDevice"] = prod_tt_sasportal.post(
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

    return Import(
        importer="prod_tt_sasportal",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
