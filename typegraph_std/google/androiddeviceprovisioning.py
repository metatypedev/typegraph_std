from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_androiddeviceprovisioning():
    androiddeviceprovisioning = HTTPRuntime(
        "https://androiddeviceprovisioning.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_androiddeviceprovisioning_1_ErrorResponse",
        "UpdateDeviceMetadataRequestIn": "_androiddeviceprovisioning_2_UpdateDeviceMetadataRequestIn",
        "UpdateDeviceMetadataRequestOut": "_androiddeviceprovisioning_3_UpdateDeviceMetadataRequestOut",
        "UnclaimDevicesRequestIn": "_androiddeviceprovisioning_4_UnclaimDevicesRequestIn",
        "UnclaimDevicesRequestOut": "_androiddeviceprovisioning_5_UnclaimDevicesRequestOut",
        "DeviceReferenceIn": "_androiddeviceprovisioning_6_DeviceReferenceIn",
        "DeviceReferenceOut": "_androiddeviceprovisioning_7_DeviceReferenceOut",
        "CustomerListConfigurationsResponseIn": "_androiddeviceprovisioning_8_CustomerListConfigurationsResponseIn",
        "CustomerListConfigurationsResponseOut": "_androiddeviceprovisioning_9_CustomerListConfigurationsResponseOut",
        "CustomerListCustomersResponseIn": "_androiddeviceprovisioning_10_CustomerListCustomersResponseIn",
        "CustomerListCustomersResponseOut": "_androiddeviceprovisioning_11_CustomerListCustomersResponseOut",
        "FindDevicesByDeviceIdentifierRequestIn": "_androiddeviceprovisioning_12_FindDevicesByDeviceIdentifierRequestIn",
        "FindDevicesByDeviceIdentifierRequestOut": "_androiddeviceprovisioning_13_FindDevicesByDeviceIdentifierRequestOut",
        "ClaimDevicesRequestIn": "_androiddeviceprovisioning_14_ClaimDevicesRequestIn",
        "ClaimDevicesRequestOut": "_androiddeviceprovisioning_15_ClaimDevicesRequestOut",
        "ClaimDeviceRequestIn": "_androiddeviceprovisioning_16_ClaimDeviceRequestIn",
        "ClaimDeviceRequestOut": "_androiddeviceprovisioning_17_ClaimDeviceRequestOut",
        "CustomerUnclaimDeviceRequestIn": "_androiddeviceprovisioning_18_CustomerUnclaimDeviceRequestIn",
        "CustomerUnclaimDeviceRequestOut": "_androiddeviceprovisioning_19_CustomerUnclaimDeviceRequestOut",
        "DpcIn": "_androiddeviceprovisioning_20_DpcIn",
        "DpcOut": "_androiddeviceprovisioning_21_DpcOut",
        "DeviceClaimIn": "_androiddeviceprovisioning_22_DeviceClaimIn",
        "DeviceClaimOut": "_androiddeviceprovisioning_23_DeviceClaimOut",
        "OperationIn": "_androiddeviceprovisioning_24_OperationIn",
        "OperationOut": "_androiddeviceprovisioning_25_OperationOut",
        "OperationPerDeviceIn": "_androiddeviceprovisioning_26_OperationPerDeviceIn",
        "OperationPerDeviceOut": "_androiddeviceprovisioning_27_OperationPerDeviceOut",
        "UnclaimDeviceRequestIn": "_androiddeviceprovisioning_28_UnclaimDeviceRequestIn",
        "UnclaimDeviceRequestOut": "_androiddeviceprovisioning_29_UnclaimDeviceRequestOut",
        "FindDevicesByOwnerRequestIn": "_androiddeviceprovisioning_30_FindDevicesByOwnerRequestIn",
        "FindDevicesByOwnerRequestOut": "_androiddeviceprovisioning_31_FindDevicesByOwnerRequestOut",
        "StatusIn": "_androiddeviceprovisioning_32_StatusIn",
        "StatusOut": "_androiddeviceprovisioning_33_StatusOut",
        "ClaimDeviceResponseIn": "_androiddeviceprovisioning_34_ClaimDeviceResponseIn",
        "ClaimDeviceResponseOut": "_androiddeviceprovisioning_35_ClaimDeviceResponseOut",
        "EmptyIn": "_androiddeviceprovisioning_36_EmptyIn",
        "EmptyOut": "_androiddeviceprovisioning_37_EmptyOut",
        "UpdateDeviceMetadataInBatchRequestIn": "_androiddeviceprovisioning_38_UpdateDeviceMetadataInBatchRequestIn",
        "UpdateDeviceMetadataInBatchRequestOut": "_androiddeviceprovisioning_39_UpdateDeviceMetadataInBatchRequestOut",
        "FindDevicesByDeviceIdentifierResponseIn": "_androiddeviceprovisioning_40_FindDevicesByDeviceIdentifierResponseIn",
        "FindDevicesByDeviceIdentifierResponseOut": "_androiddeviceprovisioning_41_FindDevicesByDeviceIdentifierResponseOut",
        "FindDevicesByOwnerResponseIn": "_androiddeviceprovisioning_42_FindDevicesByOwnerResponseIn",
        "FindDevicesByOwnerResponseOut": "_androiddeviceprovisioning_43_FindDevicesByOwnerResponseOut",
        "ConfigurationIn": "_androiddeviceprovisioning_44_ConfigurationIn",
        "ConfigurationOut": "_androiddeviceprovisioning_45_ConfigurationOut",
        "ListCustomersResponseIn": "_androiddeviceprovisioning_46_ListCustomersResponseIn",
        "ListCustomersResponseOut": "_androiddeviceprovisioning_47_ListCustomersResponseOut",
        "ListVendorCustomersResponseIn": "_androiddeviceprovisioning_48_ListVendorCustomersResponseIn",
        "ListVendorCustomersResponseOut": "_androiddeviceprovisioning_49_ListVendorCustomersResponseOut",
        "ListVendorsResponseIn": "_androiddeviceprovisioning_50_ListVendorsResponseIn",
        "ListVendorsResponseOut": "_androiddeviceprovisioning_51_ListVendorsResponseOut",
        "CustomerApplyConfigurationRequestIn": "_androiddeviceprovisioning_52_CustomerApplyConfigurationRequestIn",
        "CustomerApplyConfigurationRequestOut": "_androiddeviceprovisioning_53_CustomerApplyConfigurationRequestOut",
        "PartnerUnclaimIn": "_androiddeviceprovisioning_54_PartnerUnclaimIn",
        "PartnerUnclaimOut": "_androiddeviceprovisioning_55_PartnerUnclaimOut",
        "UpdateMetadataArgumentsIn": "_androiddeviceprovisioning_56_UpdateMetadataArgumentsIn",
        "UpdateMetadataArgumentsOut": "_androiddeviceprovisioning_57_UpdateMetadataArgumentsOut",
        "DeviceIdentifierIn": "_androiddeviceprovisioning_58_DeviceIdentifierIn",
        "DeviceIdentifierOut": "_androiddeviceprovisioning_59_DeviceIdentifierOut",
        "DevicesLongRunningOperationResponseIn": "_androiddeviceprovisioning_60_DevicesLongRunningOperationResponseIn",
        "DevicesLongRunningOperationResponseOut": "_androiddeviceprovisioning_61_DevicesLongRunningOperationResponseOut",
        "PartnerClaimIn": "_androiddeviceprovisioning_62_PartnerClaimIn",
        "PartnerClaimOut": "_androiddeviceprovisioning_63_PartnerClaimOut",
        "CustomerListDpcsResponseIn": "_androiddeviceprovisioning_64_CustomerListDpcsResponseIn",
        "CustomerListDpcsResponseOut": "_androiddeviceprovisioning_65_CustomerListDpcsResponseOut",
        "DeviceIn": "_androiddeviceprovisioning_66_DeviceIn",
        "DeviceOut": "_androiddeviceprovisioning_67_DeviceOut",
        "PerDeviceStatusInBatchIn": "_androiddeviceprovisioning_68_PerDeviceStatusInBatchIn",
        "PerDeviceStatusInBatchOut": "_androiddeviceprovisioning_69_PerDeviceStatusInBatchOut",
        "CompanyIn": "_androiddeviceprovisioning_70_CompanyIn",
        "CompanyOut": "_androiddeviceprovisioning_71_CompanyOut",
        "CustomerRemoveConfigurationRequestIn": "_androiddeviceprovisioning_72_CustomerRemoveConfigurationRequestIn",
        "CustomerRemoveConfigurationRequestOut": "_androiddeviceprovisioning_73_CustomerRemoveConfigurationRequestOut",
        "DevicesLongRunningOperationMetadataIn": "_androiddeviceprovisioning_74_DevicesLongRunningOperationMetadataIn",
        "DevicesLongRunningOperationMetadataOut": "_androiddeviceprovisioning_75_DevicesLongRunningOperationMetadataOut",
        "GoogleWorkspaceAccountIn": "_androiddeviceprovisioning_76_GoogleWorkspaceAccountIn",
        "GoogleWorkspaceAccountOut": "_androiddeviceprovisioning_77_GoogleWorkspaceAccountOut",
        "CustomerListDevicesResponseIn": "_androiddeviceprovisioning_78_CustomerListDevicesResponseIn",
        "CustomerListDevicesResponseOut": "_androiddeviceprovisioning_79_CustomerListDevicesResponseOut",
        "CreateCustomerRequestIn": "_androiddeviceprovisioning_80_CreateCustomerRequestIn",
        "CreateCustomerRequestOut": "_androiddeviceprovisioning_81_CreateCustomerRequestOut",
        "DeviceMetadataIn": "_androiddeviceprovisioning_82_DeviceMetadataIn",
        "DeviceMetadataOut": "_androiddeviceprovisioning_83_DeviceMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["UpdateDeviceMetadataRequestIn"] = t.struct(
        {"deviceMetadata": t.proxy(renames["DeviceMetadataIn"])}
    ).named(renames["UpdateDeviceMetadataRequestIn"])
    types["UpdateDeviceMetadataRequestOut"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeviceMetadataRequestOut"])
    types["UnclaimDevicesRequestIn"] = t.struct(
        {"unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"]))}
    ).named(renames["UnclaimDevicesRequestIn"])
    types["UnclaimDevicesRequestOut"] = t.struct(
        {
            "unclaims": t.array(t.proxy(renames["PartnerUnclaimOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnclaimDevicesRequestOut"])
    types["DeviceReferenceIn"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]).optional(),
        }
    ).named(renames["DeviceReferenceIn"])
    types["DeviceReferenceOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceReferenceOut"])
    types["CustomerListConfigurationsResponseIn"] = t.struct(
        {"configurations": t.array(t.proxy(renames["ConfigurationIn"])).optional()}
    ).named(renames["CustomerListConfigurationsResponseIn"])
    types["CustomerListConfigurationsResponseOut"] = t.struct(
        {
            "configurations": t.array(t.proxy(renames["ConfigurationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListConfigurationsResponseOut"])
    types["CustomerListCustomersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customers": t.array(t.proxy(renames["CompanyIn"])).optional(),
        }
    ).named(renames["CustomerListCustomersResponseIn"])
    types["CustomerListCustomersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customers": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListCustomersResponseOut"])
    types["FindDevicesByDeviceIdentifierRequestIn"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "pageToken": t.string().optional(),
            "limit": t.string(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierRequestIn"])
    types["FindDevicesByDeviceIdentifierRequestOut"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "pageToken": t.string().optional(),
            "limit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierRequestOut"])
    types["ClaimDevicesRequestIn"] = t.struct(
        {"claims": t.array(t.proxy(renames["PartnerClaimIn"]))}
    ).named(renames["ClaimDevicesRequestIn"])
    types["ClaimDevicesRequestOut"] = t.struct(
        {
            "claims": t.array(t.proxy(renames["PartnerClaimOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClaimDevicesRequestOut"])
    types["ClaimDeviceRequestIn"] = t.struct(
        {
            "customerId": t.string().optional(),
            "simlockProfileId": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "sectionType": t.string(),
            "preProvisioningToken": t.string().optional(),
        }
    ).named(renames["ClaimDeviceRequestIn"])
    types["ClaimDeviceRequestOut"] = t.struct(
        {
            "customerId": t.string().optional(),
            "simlockProfileId": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "sectionType": t.string(),
            "preProvisioningToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClaimDeviceRequestOut"])
    types["CustomerUnclaimDeviceRequestIn"] = t.struct(
        {"device": t.proxy(renames["DeviceReferenceIn"])}
    ).named(renames["CustomerUnclaimDeviceRequestIn"])
    types["CustomerUnclaimDeviceRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["DeviceReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerUnclaimDeviceRequestOut"])
    types["DpcIn"] = t.struct({"_": t.string().optional()}).named(renames["DpcIn"])
    types["DpcOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "dpcName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DpcOut"])
    types["DeviceClaimIn"] = t.struct(
        {
            "vacationModeStartTime": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "ownerCompanyId": t.string().optional(),
            "additionalService": t.string().optional(),
            "vacationModeExpireTime": t.string().optional(),
            "resellerId": t.string().optional(),
        }
    ).named(renames["DeviceClaimIn"])
    types["DeviceClaimOut"] = t.struct(
        {
            "vacationModeStartTime": t.string().optional(),
            "sectionType": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "ownerCompanyId": t.string().optional(),
            "additionalService": t.string().optional(),
            "vacationModeExpireTime": t.string().optional(),
            "resellerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceClaimOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["OperationPerDeviceIn"] = t.struct(
        {
            "unclaim": t.proxy(renames["PartnerUnclaimIn"]).optional(),
            "claim": t.proxy(renames["PartnerClaimIn"]).optional(),
            "result": t.proxy(renames["PerDeviceStatusInBatchIn"]).optional(),
            "updateMetadata": t.proxy(renames["UpdateMetadataArgumentsIn"]).optional(),
        }
    ).named(renames["OperationPerDeviceIn"])
    types["OperationPerDeviceOut"] = t.struct(
        {
            "unclaim": t.proxy(renames["PartnerUnclaimOut"]).optional(),
            "claim": t.proxy(renames["PartnerClaimOut"]).optional(),
            "result": t.proxy(renames["PerDeviceStatusInBatchOut"]).optional(),
            "updateMetadata": t.proxy(renames["UpdateMetadataArgumentsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationPerDeviceOut"])
    types["UnclaimDeviceRequestIn"] = t.struct(
        {
            "vacationModeExpireTime": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "sectionType": t.string(),
            "deviceId": t.string(),
            "vacationModeDays": t.integer().optional(),
        }
    ).named(renames["UnclaimDeviceRequestIn"])
    types["UnclaimDeviceRequestOut"] = t.struct(
        {
            "vacationModeExpireTime": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "sectionType": t.string(),
            "deviceId": t.string(),
            "vacationModeDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnclaimDeviceRequestOut"])
    types["FindDevicesByOwnerRequestIn"] = t.struct(
        {
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "customerId": t.array(t.string()).optional(),
            "limit": t.string(),
        }
    ).named(renames["FindDevicesByOwnerRequestIn"])
    types["FindDevicesByOwnerRequestOut"] = t.struct(
        {
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "customerId": t.array(t.string()).optional(),
            "limit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByOwnerRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ClaimDeviceResponseIn"] = t.struct(
        {"deviceName": t.string().optional(), "deviceId": t.string().optional()}
    ).named(renames["ClaimDeviceResponseIn"])
    types["ClaimDeviceResponseOut"] = t.struct(
        {
            "deviceName": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClaimDeviceResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UpdateDeviceMetadataInBatchRequestIn"] = t.struct(
        {"updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"]))}
    ).named(renames["UpdateDeviceMetadataInBatchRequestIn"])
    types["UpdateDeviceMetadataInBatchRequestOut"] = t.struct(
        {
            "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeviceMetadataInBatchRequestOut"])
    types["FindDevicesByDeviceIdentifierResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierResponseIn"])
    types["FindDevicesByDeviceIdentifierResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierResponseOut"])
    types["FindDevicesByOwnerResponseIn"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["FindDevicesByOwnerResponseIn"])
    types["FindDevicesByOwnerResponseOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByOwnerResponseOut"])
    types["ConfigurationIn"] = t.struct(
        {
            "companyName": t.string(),
            "contactPhone": t.string(),
            "dpcResourcePath": t.string(),
            "customMessage": t.string().optional(),
            "configurationName": t.string(),
            "contactEmail": t.string(),
            "dpcExtras": t.string().optional(),
            "isDefault": t.boolean(),
            "forcedResetTime": t.string().optional(),
        }
    ).named(renames["ConfigurationIn"])
    types["ConfigurationOut"] = t.struct(
        {
            "companyName": t.string(),
            "configurationId": t.string().optional(),
            "name": t.string().optional(),
            "contactPhone": t.string(),
            "dpcResourcePath": t.string(),
            "customMessage": t.string().optional(),
            "configurationName": t.string(),
            "contactEmail": t.string(),
            "dpcExtras": t.string().optional(),
            "isDefault": t.boolean(),
            "forcedResetTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigurationOut"])
    types["ListCustomersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "customers": t.array(t.proxy(renames["CompanyIn"])).optional(),
        }
    ).named(renames["ListCustomersResponseIn"])
    types["ListCustomersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "customers": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomersResponseOut"])
    types["ListVendorCustomersResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "customers": t.array(t.proxy(renames["CompanyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVendorCustomersResponseIn"])
    types["ListVendorCustomersResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "customers": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVendorCustomersResponseOut"])
    types["ListVendorsResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "vendors": t.array(t.proxy(renames["CompanyIn"])).optional(),
        }
    ).named(renames["ListVendorsResponseIn"])
    types["ListVendorsResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "vendors": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVendorsResponseOut"])
    types["CustomerApplyConfigurationRequestIn"] = t.struct(
        {"device": t.proxy(renames["DeviceReferenceIn"]), "configuration": t.string()}
    ).named(renames["CustomerApplyConfigurationRequestIn"])
    types["CustomerApplyConfigurationRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["DeviceReferenceOut"]),
            "configuration": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerApplyConfigurationRequestOut"])
    types["PartnerUnclaimIn"] = t.struct(
        {
            "vacationModeExpireTime": t.string().optional(),
            "deviceId": t.string(),
            "sectionType": t.string(),
            "vacationModeDays": t.integer().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
        }
    ).named(renames["PartnerUnclaimIn"])
    types["PartnerUnclaimOut"] = t.struct(
        {
            "vacationModeExpireTime": t.string().optional(),
            "deviceId": t.string(),
            "sectionType": t.string(),
            "vacationModeDays": t.integer().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerUnclaimOut"])
    types["UpdateMetadataArgumentsIn"] = t.struct(
        {
            "deviceId": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
        }
    ).named(renames["UpdateMetadataArgumentsIn"])
    types["UpdateMetadataArgumentsOut"] = t.struct(
        {
            "deviceId": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateMetadataArgumentsOut"])
    types["DeviceIdentifierIn"] = t.struct(
        {
            "model": t.string().optional(),
            "meid": t.string().optional(),
            "serialNumber": t.string().optional(),
            "deviceType": t.string().optional(),
            "chromeOsAttestedDeviceId": t.string().optional(),
            "imei": t.string().optional(),
            "manufacturer": t.string().optional(),
        }
    ).named(renames["DeviceIdentifierIn"])
    types["DeviceIdentifierOut"] = t.struct(
        {
            "model": t.string().optional(),
            "meid": t.string().optional(),
            "serialNumber": t.string().optional(),
            "deviceType": t.string().optional(),
            "chromeOsAttestedDeviceId": t.string().optional(),
            "imei": t.string().optional(),
            "manufacturer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIdentifierOut"])
    types["DevicesLongRunningOperationResponseIn"] = t.struct(
        {
            "perDeviceStatus": t.array(
                t.proxy(renames["OperationPerDeviceIn"])
            ).optional(),
            "successCount": t.integer().optional(),
        }
    ).named(renames["DevicesLongRunningOperationResponseIn"])
    types["DevicesLongRunningOperationResponseOut"] = t.struct(
        {
            "perDeviceStatus": t.array(
                t.proxy(renames["OperationPerDeviceOut"])
            ).optional(),
            "successCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicesLongRunningOperationResponseOut"])
    types["PartnerClaimIn"] = t.struct(
        {
            "sectionType": t.string(),
            "simlockProfileId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "googleWorkspaceCustomerId": t.string().optional(),
            "customerId": t.string().optional(),
            "preProvisioningToken": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
        }
    ).named(renames["PartnerClaimIn"])
    types["PartnerClaimOut"] = t.struct(
        {
            "sectionType": t.string(),
            "simlockProfileId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "googleWorkspaceCustomerId": t.string().optional(),
            "customerId": t.string().optional(),
            "preProvisioningToken": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerClaimOut"])
    types["CustomerListDpcsResponseIn"] = t.struct(
        {"dpcs": t.array(t.proxy(renames["DpcIn"])).optional()}
    ).named(renames["CustomerListDpcsResponseIn"])
    types["CustomerListDpcsResponseOut"] = t.struct(
        {
            "dpcs": t.array(t.proxy(renames["DpcOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListDpcsResponseOut"])
    types["DeviceIn"] = t.struct(
        {
            "configuration": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]).optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "claims": t.array(t.proxy(renames["DeviceClaimOut"])).optional(),
            "name": t.string().optional(),
            "configuration": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]).optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["PerDeviceStatusInBatchIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "deviceId": t.string().optional(),
            "errorIdentifier": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["PerDeviceStatusInBatchIn"])
    types["PerDeviceStatusInBatchOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "deviceId": t.string().optional(),
            "errorIdentifier": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerDeviceStatusInBatchOut"])
    types["CompanyIn"] = t.struct(
        {
            "skipWelcomeEmail": t.boolean().optional(),
            "languageCode": t.string().optional(),
            "companyName": t.string(),
            "ownerEmails": t.array(t.string()),
            "adminEmails": t.array(t.string()).optional(),
        }
    ).named(renames["CompanyIn"])
    types["CompanyOut"] = t.struct(
        {
            "skipWelcomeEmail": t.boolean().optional(),
            "googleWorkspaceAccount": t.proxy(
                renames["GoogleWorkspaceAccountOut"]
            ).optional(),
            "languageCode": t.string().optional(),
            "companyName": t.string(),
            "name": t.string().optional(),
            "ownerEmails": t.array(t.string()),
            "companyId": t.string().optional(),
            "termsStatus": t.string().optional(),
            "adminEmails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompanyOut"])
    types["CustomerRemoveConfigurationRequestIn"] = t.struct(
        {"device": t.proxy(renames["DeviceReferenceIn"])}
    ).named(renames["CustomerRemoveConfigurationRequestIn"])
    types["CustomerRemoveConfigurationRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["DeviceReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerRemoveConfigurationRequestOut"])
    types["DevicesLongRunningOperationMetadataIn"] = t.struct(
        {
            "devicesCount": t.integer().optional(),
            "processingStatus": t.string().optional(),
            "progress": t.integer().optional(),
        }
    ).named(renames["DevicesLongRunningOperationMetadataIn"])
    types["DevicesLongRunningOperationMetadataOut"] = t.struct(
        {
            "devicesCount": t.integer().optional(),
            "processingStatus": t.string().optional(),
            "progress": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicesLongRunningOperationMetadataOut"])
    types["GoogleWorkspaceAccountIn"] = t.struct({"customerId": t.string()}).named(
        renames["GoogleWorkspaceAccountIn"]
    )
    types["GoogleWorkspaceAccountOut"] = t.struct(
        {
            "preProvisioningTokens": t.array(t.string()).optional(),
            "customerId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleWorkspaceAccountOut"])
    types["CustomerListDevicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
        }
    ).named(renames["CustomerListDevicesResponseIn"])
    types["CustomerListDevicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListDevicesResponseOut"])
    types["CreateCustomerRequestIn"] = t.struct(
        {"customer": t.proxy(renames["CompanyIn"])}
    ).named(renames["CreateCustomerRequestIn"])
    types["CreateCustomerRequestOut"] = t.struct(
        {
            "customer": t.proxy(renames["CompanyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCustomerRequestOut"])
    types["DeviceMetadataIn"] = t.struct(
        {"entries": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["DeviceMetadataIn"])
    types["DeviceMetadataOut"] = t.struct(
        {
            "entries": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMetadataOut"])

    functions = {}
    functions["partnersDevicesFindByOwner"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:unclaimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesGet"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:unclaimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesFindByIdentifier"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:unclaimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesClaimAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:unclaimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUpdateMetadataAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:unclaimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesClaim"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:unclaimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesMetadata"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:unclaimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUnclaim"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:unclaimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUnclaimAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:unclaimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersCustomersList"] = androiddeviceprovisioning.post(
        "v1/{parent}/customers",
        t.struct(
            {
                "parent": t.string(),
                "customer": t.proxy(renames["CompanyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CompanyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersCustomersCreate"] = androiddeviceprovisioning.post(
        "v1/{parent}/customers",
        t.struct(
            {
                "parent": t.string(),
                "customer": t.proxy(renames["CompanyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CompanyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersVendorsList"] = androiddeviceprovisioning.get(
        "v1/{parent}/vendors",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVendorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersVendorsCustomersList"] = androiddeviceprovisioning.get(
        "v1/{parent}/customers",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVendorCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersList"] = androiddeviceprovisioning.get(
        "v1/customers",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDpcsList"] = androiddeviceprovisioning.get(
        "v1/{parent}/dpcs",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerListDpcsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesGet"] = androiddeviceprovisioning.get(
        "v1/{parent}/devices",
        t.struct(
            {
                "pageSize": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesRemoveConfiguration"] = androiddeviceprovisioning.get(
        "v1/{parent}/devices",
        t.struct(
            {
                "pageSize": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesUnclaim"] = androiddeviceprovisioning.get(
        "v1/{parent}/devices",
        t.struct(
            {
                "pageSize": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesApplyConfiguration"] = androiddeviceprovisioning.get(
        "v1/{parent}/devices",
        t.struct(
            {
                "pageSize": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesList"] = androiddeviceprovisioning.get(
        "v1/{parent}/devices",
        t.struct(
            {
                "pageSize": t.string().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CustomerListDevicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsDelete"] = androiddeviceprovisioning.get(
        "v1/{parent}/configurations",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerListConfigurationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsCreate"] = androiddeviceprovisioning.get(
        "v1/{parent}/configurations",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerListConfigurationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsGet"] = androiddeviceprovisioning.get(
        "v1/{parent}/configurations",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerListConfigurationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsPatch"] = androiddeviceprovisioning.get(
        "v1/{parent}/configurations",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerListConfigurationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsList"] = androiddeviceprovisioning.get(
        "v1/{parent}/configurations",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerListConfigurationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="androiddeviceprovisioning",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
