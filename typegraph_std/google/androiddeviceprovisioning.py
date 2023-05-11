from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_androiddeviceprovisioning() -> Import:
    androiddeviceprovisioning = HTTPRuntime(
        "https://androiddeviceprovisioning.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_androiddeviceprovisioning_1_ErrorResponse",
        "CustomerListCustomersResponseIn": "_androiddeviceprovisioning_2_CustomerListCustomersResponseIn",
        "CustomerListCustomersResponseOut": "_androiddeviceprovisioning_3_CustomerListCustomersResponseOut",
        "DeviceReferenceIn": "_androiddeviceprovisioning_4_DeviceReferenceIn",
        "DeviceReferenceOut": "_androiddeviceprovisioning_5_DeviceReferenceOut",
        "FindDevicesByOwnerRequestIn": "_androiddeviceprovisioning_6_FindDevicesByOwnerRequestIn",
        "FindDevicesByOwnerRequestOut": "_androiddeviceprovisioning_7_FindDevicesByOwnerRequestOut",
        "ClaimDeviceRequestIn": "_androiddeviceprovisioning_8_ClaimDeviceRequestIn",
        "ClaimDeviceRequestOut": "_androiddeviceprovisioning_9_ClaimDeviceRequestOut",
        "PartnerClaimIn": "_androiddeviceprovisioning_10_PartnerClaimIn",
        "PartnerClaimOut": "_androiddeviceprovisioning_11_PartnerClaimOut",
        "CreateCustomerRequestIn": "_androiddeviceprovisioning_12_CreateCustomerRequestIn",
        "CreateCustomerRequestOut": "_androiddeviceprovisioning_13_CreateCustomerRequestOut",
        "GoogleWorkspaceAccountIn": "_androiddeviceprovisioning_14_GoogleWorkspaceAccountIn",
        "GoogleWorkspaceAccountOut": "_androiddeviceprovisioning_15_GoogleWorkspaceAccountOut",
        "CustomerListDpcsResponseIn": "_androiddeviceprovisioning_16_CustomerListDpcsResponseIn",
        "CustomerListDpcsResponseOut": "_androiddeviceprovisioning_17_CustomerListDpcsResponseOut",
        "ClaimDevicesRequestIn": "_androiddeviceprovisioning_18_ClaimDevicesRequestIn",
        "ClaimDevicesRequestOut": "_androiddeviceprovisioning_19_ClaimDevicesRequestOut",
        "ClaimDeviceResponseIn": "_androiddeviceprovisioning_20_ClaimDeviceResponseIn",
        "ClaimDeviceResponseOut": "_androiddeviceprovisioning_21_ClaimDeviceResponseOut",
        "CustomerListConfigurationsResponseIn": "_androiddeviceprovisioning_22_CustomerListConfigurationsResponseIn",
        "CustomerListConfigurationsResponseOut": "_androiddeviceprovisioning_23_CustomerListConfigurationsResponseOut",
        "ListCustomersResponseIn": "_androiddeviceprovisioning_24_ListCustomersResponseIn",
        "ListCustomersResponseOut": "_androiddeviceprovisioning_25_ListCustomersResponseOut",
        "UpdateMetadataArgumentsIn": "_androiddeviceprovisioning_26_UpdateMetadataArgumentsIn",
        "UpdateMetadataArgumentsOut": "_androiddeviceprovisioning_27_UpdateMetadataArgumentsOut",
        "FindDevicesByOwnerResponseIn": "_androiddeviceprovisioning_28_FindDevicesByOwnerResponseIn",
        "FindDevicesByOwnerResponseOut": "_androiddeviceprovisioning_29_FindDevicesByOwnerResponseOut",
        "CustomerListDevicesResponseIn": "_androiddeviceprovisioning_30_CustomerListDevicesResponseIn",
        "CustomerListDevicesResponseOut": "_androiddeviceprovisioning_31_CustomerListDevicesResponseOut",
        "FindDevicesByDeviceIdentifierRequestIn": "_androiddeviceprovisioning_32_FindDevicesByDeviceIdentifierRequestIn",
        "FindDevicesByDeviceIdentifierRequestOut": "_androiddeviceprovisioning_33_FindDevicesByDeviceIdentifierRequestOut",
        "DeviceMetadataIn": "_androiddeviceprovisioning_34_DeviceMetadataIn",
        "DeviceMetadataOut": "_androiddeviceprovisioning_35_DeviceMetadataOut",
        "UnclaimDeviceRequestIn": "_androiddeviceprovisioning_36_UnclaimDeviceRequestIn",
        "UnclaimDeviceRequestOut": "_androiddeviceprovisioning_37_UnclaimDeviceRequestOut",
        "DeviceIdentifierIn": "_androiddeviceprovisioning_38_DeviceIdentifierIn",
        "DeviceIdentifierOut": "_androiddeviceprovisioning_39_DeviceIdentifierOut",
        "DevicesLongRunningOperationResponseIn": "_androiddeviceprovisioning_40_DevicesLongRunningOperationResponseIn",
        "DevicesLongRunningOperationResponseOut": "_androiddeviceprovisioning_41_DevicesLongRunningOperationResponseOut",
        "UpdateDeviceMetadataInBatchRequestIn": "_androiddeviceprovisioning_42_UpdateDeviceMetadataInBatchRequestIn",
        "UpdateDeviceMetadataInBatchRequestOut": "_androiddeviceprovisioning_43_UpdateDeviceMetadataInBatchRequestOut",
        "CustomerRemoveConfigurationRequestIn": "_androiddeviceprovisioning_44_CustomerRemoveConfigurationRequestIn",
        "CustomerRemoveConfigurationRequestOut": "_androiddeviceprovisioning_45_CustomerRemoveConfigurationRequestOut",
        "ConfigurationIn": "_androiddeviceprovisioning_46_ConfigurationIn",
        "ConfigurationOut": "_androiddeviceprovisioning_47_ConfigurationOut",
        "CustomerUnclaimDeviceRequestIn": "_androiddeviceprovisioning_48_CustomerUnclaimDeviceRequestIn",
        "CustomerUnclaimDeviceRequestOut": "_androiddeviceprovisioning_49_CustomerUnclaimDeviceRequestOut",
        "CustomerApplyConfigurationRequestIn": "_androiddeviceprovisioning_50_CustomerApplyConfigurationRequestIn",
        "CustomerApplyConfigurationRequestOut": "_androiddeviceprovisioning_51_CustomerApplyConfigurationRequestOut",
        "UnclaimDevicesRequestIn": "_androiddeviceprovisioning_52_UnclaimDevicesRequestIn",
        "UnclaimDevicesRequestOut": "_androiddeviceprovisioning_53_UnclaimDevicesRequestOut",
        "ListVendorCustomersResponseIn": "_androiddeviceprovisioning_54_ListVendorCustomersResponseIn",
        "ListVendorCustomersResponseOut": "_androiddeviceprovisioning_55_ListVendorCustomersResponseOut",
        "FindDevicesByDeviceIdentifierResponseIn": "_androiddeviceprovisioning_56_FindDevicesByDeviceIdentifierResponseIn",
        "FindDevicesByDeviceIdentifierResponseOut": "_androiddeviceprovisioning_57_FindDevicesByDeviceIdentifierResponseOut",
        "OperationPerDeviceIn": "_androiddeviceprovisioning_58_OperationPerDeviceIn",
        "OperationPerDeviceOut": "_androiddeviceprovisioning_59_OperationPerDeviceOut",
        "DeviceIn": "_androiddeviceprovisioning_60_DeviceIn",
        "DeviceOut": "_androiddeviceprovisioning_61_DeviceOut",
        "DeviceClaimIn": "_androiddeviceprovisioning_62_DeviceClaimIn",
        "DeviceClaimOut": "_androiddeviceprovisioning_63_DeviceClaimOut",
        "EmptyIn": "_androiddeviceprovisioning_64_EmptyIn",
        "EmptyOut": "_androiddeviceprovisioning_65_EmptyOut",
        "UpdateDeviceMetadataRequestIn": "_androiddeviceprovisioning_66_UpdateDeviceMetadataRequestIn",
        "UpdateDeviceMetadataRequestOut": "_androiddeviceprovisioning_67_UpdateDeviceMetadataRequestOut",
        "DpcIn": "_androiddeviceprovisioning_68_DpcIn",
        "DpcOut": "_androiddeviceprovisioning_69_DpcOut",
        "CompanyIn": "_androiddeviceprovisioning_70_CompanyIn",
        "CompanyOut": "_androiddeviceprovisioning_71_CompanyOut",
        "ListVendorsResponseIn": "_androiddeviceprovisioning_72_ListVendorsResponseIn",
        "ListVendorsResponseOut": "_androiddeviceprovisioning_73_ListVendorsResponseOut",
        "PerDeviceStatusInBatchIn": "_androiddeviceprovisioning_74_PerDeviceStatusInBatchIn",
        "PerDeviceStatusInBatchOut": "_androiddeviceprovisioning_75_PerDeviceStatusInBatchOut",
        "OperationIn": "_androiddeviceprovisioning_76_OperationIn",
        "OperationOut": "_androiddeviceprovisioning_77_OperationOut",
        "PartnerUnclaimIn": "_androiddeviceprovisioning_78_PartnerUnclaimIn",
        "PartnerUnclaimOut": "_androiddeviceprovisioning_79_PartnerUnclaimOut",
        "DevicesLongRunningOperationMetadataIn": "_androiddeviceprovisioning_80_DevicesLongRunningOperationMetadataIn",
        "DevicesLongRunningOperationMetadataOut": "_androiddeviceprovisioning_81_DevicesLongRunningOperationMetadataOut",
        "StatusIn": "_androiddeviceprovisioning_82_StatusIn",
        "StatusOut": "_androiddeviceprovisioning_83_StatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["DeviceReferenceIn"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]).optional(),
            "deviceId": t.string().optional(),
        }
    ).named(renames["DeviceReferenceIn"])
    types["DeviceReferenceOut"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]).optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceReferenceOut"])
    types["FindDevicesByOwnerRequestIn"] = t.struct(
        {
            "googleWorkspaceCustomerId": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "sectionType": t.string(),
            "customerId": t.array(t.string()).optional(),
            "limit": t.string(),
        }
    ).named(renames["FindDevicesByOwnerRequestIn"])
    types["FindDevicesByOwnerRequestOut"] = t.struct(
        {
            "googleWorkspaceCustomerId": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "sectionType": t.string(),
            "customerId": t.array(t.string()).optional(),
            "limit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByOwnerRequestOut"])
    types["ClaimDeviceRequestIn"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
            "sectionType": t.string(),
            "simlockProfileId": t.string().optional(),
            "customerId": t.string().optional(),
            "preProvisioningToken": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
        }
    ).named(renames["ClaimDeviceRequestIn"])
    types["ClaimDeviceRequestOut"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "sectionType": t.string(),
            "simlockProfileId": t.string().optional(),
            "customerId": t.string().optional(),
            "preProvisioningToken": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClaimDeviceRequestOut"])
    types["PartnerClaimIn"] = t.struct(
        {
            "preProvisioningToken": t.string().optional(),
            "simlockProfileId": t.string().optional(),
            "customerId": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.string().optional(),
        }
    ).named(renames["PartnerClaimIn"])
    types["PartnerClaimOut"] = t.struct(
        {
            "preProvisioningToken": t.string().optional(),
            "simlockProfileId": t.string().optional(),
            "customerId": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerClaimOut"])
    types["CreateCustomerRequestIn"] = t.struct(
        {"customer": t.proxy(renames["CompanyIn"])}
    ).named(renames["CreateCustomerRequestIn"])
    types["CreateCustomerRequestOut"] = t.struct(
        {
            "customer": t.proxy(renames["CompanyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCustomerRequestOut"])
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
    types["CustomerListDpcsResponseIn"] = t.struct(
        {"dpcs": t.array(t.proxy(renames["DpcIn"])).optional()}
    ).named(renames["CustomerListDpcsResponseIn"])
    types["CustomerListDpcsResponseOut"] = t.struct(
        {
            "dpcs": t.array(t.proxy(renames["DpcOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListDpcsResponseOut"])
    types["ClaimDevicesRequestIn"] = t.struct(
        {"claims": t.array(t.proxy(renames["PartnerClaimIn"]))}
    ).named(renames["ClaimDevicesRequestIn"])
    types["ClaimDevicesRequestOut"] = t.struct(
        {
            "claims": t.array(t.proxy(renames["PartnerClaimOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClaimDevicesRequestOut"])
    types["ClaimDeviceResponseIn"] = t.struct(
        {"deviceId": t.string().optional(), "deviceName": t.string().optional()}
    ).named(renames["ClaimDeviceResponseIn"])
    types["ClaimDeviceResponseOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "deviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClaimDeviceResponseOut"])
    types["CustomerListConfigurationsResponseIn"] = t.struct(
        {"configurations": t.array(t.proxy(renames["ConfigurationIn"])).optional()}
    ).named(renames["CustomerListConfigurationsResponseIn"])
    types["CustomerListConfigurationsResponseOut"] = t.struct(
        {
            "configurations": t.array(t.proxy(renames["ConfigurationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListConfigurationsResponseOut"])
    types["ListCustomersResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "customers": t.array(t.proxy(renames["CompanyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCustomersResponseIn"])
    types["ListCustomersResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "customers": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCustomersResponseOut"])
    types["UpdateMetadataArgumentsIn"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "deviceId": t.string(),
        }
    ).named(renames["UpdateMetadataArgumentsIn"])
    types["UpdateMetadataArgumentsOut"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "deviceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateMetadataArgumentsOut"])
    types["FindDevicesByOwnerResponseIn"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["FindDevicesByOwnerResponseIn"])
    types["FindDevicesByOwnerResponseOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByOwnerResponseOut"])
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
    types["FindDevicesByDeviceIdentifierRequestIn"] = t.struct(
        {
            "limit": t.string(),
            "pageToken": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
        }
    ).named(renames["FindDevicesByDeviceIdentifierRequestIn"])
    types["FindDevicesByDeviceIdentifierRequestOut"] = t.struct(
        {
            "limit": t.string(),
            "pageToken": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierRequestOut"])
    types["DeviceMetadataIn"] = t.struct(
        {"entries": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["DeviceMetadataIn"])
    types["DeviceMetadataOut"] = t.struct(
        {
            "entries": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMetadataOut"])
    types["UnclaimDeviceRequestIn"] = t.struct(
        {
            "sectionType": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeDays": t.integer().optional(),
            "deviceId": t.string(),
        }
    ).named(renames["UnclaimDeviceRequestIn"])
    types["UnclaimDeviceRequestOut"] = t.struct(
        {
            "sectionType": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeDays": t.integer().optional(),
            "deviceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnclaimDeviceRequestOut"])
    types["DeviceIdentifierIn"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "imei": t.string().optional(),
            "serialNumber": t.string().optional(),
            "model": t.string().optional(),
            "chromeOsAttestedDeviceId": t.string().optional(),
            "manufacturer": t.string().optional(),
            "meid": t.string().optional(),
        }
    ).named(renames["DeviceIdentifierIn"])
    types["DeviceIdentifierOut"] = t.struct(
        {
            "deviceType": t.string().optional(),
            "imei": t.string().optional(),
            "serialNumber": t.string().optional(),
            "model": t.string().optional(),
            "chromeOsAttestedDeviceId": t.string().optional(),
            "manufacturer": t.string().optional(),
            "meid": t.string().optional(),
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
    types["UpdateDeviceMetadataInBatchRequestIn"] = t.struct(
        {"updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"]))}
    ).named(renames["UpdateDeviceMetadataInBatchRequestIn"])
    types["UpdateDeviceMetadataInBatchRequestOut"] = t.struct(
        {
            "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeviceMetadataInBatchRequestOut"])
    types["CustomerRemoveConfigurationRequestIn"] = t.struct(
        {"device": t.proxy(renames["DeviceReferenceIn"])}
    ).named(renames["CustomerRemoveConfigurationRequestIn"])
    types["CustomerRemoveConfigurationRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["DeviceReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerRemoveConfigurationRequestOut"])
    types["ConfigurationIn"] = t.struct(
        {
            "customMessage": t.string().optional(),
            "configurationName": t.string(),
            "companyName": t.string(),
            "isDefault": t.boolean(),
            "dpcExtras": t.string().optional(),
            "dpcResourcePath": t.string(),
            "contactPhone": t.string(),
            "forcedResetTime": t.string().optional(),
            "contactEmail": t.string(),
        }
    ).named(renames["ConfigurationIn"])
    types["ConfigurationOut"] = t.struct(
        {
            "customMessage": t.string().optional(),
            "name": t.string().optional(),
            "configurationName": t.string(),
            "companyName": t.string(),
            "isDefault": t.boolean(),
            "configurationId": t.string().optional(),
            "dpcExtras": t.string().optional(),
            "dpcResourcePath": t.string(),
            "contactPhone": t.string(),
            "forcedResetTime": t.string().optional(),
            "contactEmail": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigurationOut"])
    types["CustomerUnclaimDeviceRequestIn"] = t.struct(
        {"device": t.proxy(renames["DeviceReferenceIn"])}
    ).named(renames["CustomerUnclaimDeviceRequestIn"])
    types["CustomerUnclaimDeviceRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["DeviceReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerUnclaimDeviceRequestOut"])
    types["CustomerApplyConfigurationRequestIn"] = t.struct(
        {"configuration": t.string(), "device": t.proxy(renames["DeviceReferenceIn"])}
    ).named(renames["CustomerApplyConfigurationRequestIn"])
    types["CustomerApplyConfigurationRequestOut"] = t.struct(
        {
            "configuration": t.string(),
            "device": t.proxy(renames["DeviceReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerApplyConfigurationRequestOut"])
    types["UnclaimDevicesRequestIn"] = t.struct(
        {"unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"]))}
    ).named(renames["UnclaimDevicesRequestIn"])
    types["UnclaimDevicesRequestOut"] = t.struct(
        {
            "unclaims": t.array(t.proxy(renames["PartnerUnclaimOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnclaimDevicesRequestOut"])
    types["ListVendorCustomersResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "customers": t.array(t.proxy(renames["CompanyIn"])).optional(),
        }
    ).named(renames["ListVendorCustomersResponseIn"])
    types["ListVendorCustomersResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "customers": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVendorCustomersResponseOut"])
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
    types["OperationPerDeviceIn"] = t.struct(
        {
            "unclaim": t.proxy(renames["PartnerUnclaimIn"]).optional(),
            "result": t.proxy(renames["PerDeviceStatusInBatchIn"]).optional(),
            "claim": t.proxy(renames["PartnerClaimIn"]).optional(),
            "updateMetadata": t.proxy(renames["UpdateMetadataArgumentsIn"]).optional(),
        }
    ).named(renames["OperationPerDeviceIn"])
    types["OperationPerDeviceOut"] = t.struct(
        {
            "unclaim": t.proxy(renames["PartnerUnclaimOut"]).optional(),
            "result": t.proxy(renames["PerDeviceStatusInBatchOut"]).optional(),
            "claim": t.proxy(renames["PartnerClaimOut"]).optional(),
            "updateMetadata": t.proxy(renames["UpdateMetadataArgumentsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationPerDeviceOut"])
    types["DeviceIn"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]).optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
            "configuration": t.string().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]).optional(),
            "deviceId": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "claims": t.array(t.proxy(renames["DeviceClaimOut"])).optional(),
            "name": t.string().optional(),
            "configuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["DeviceClaimIn"] = t.struct(
        {
            "vacationModeExpireTime": t.string().optional(),
            "additionalService": t.string().optional(),
            "ownerCompanyId": t.string().optional(),
            "resellerId": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "vacationModeStartTime": t.string().optional(),
        }
    ).named(renames["DeviceClaimIn"])
    types["DeviceClaimOut"] = t.struct(
        {
            "vacationModeExpireTime": t.string().optional(),
            "additionalService": t.string().optional(),
            "ownerCompanyId": t.string().optional(),
            "resellerId": t.string().optional(),
            "sectionType": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "vacationModeStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceClaimOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UpdateDeviceMetadataRequestIn"] = t.struct(
        {"deviceMetadata": t.proxy(renames["DeviceMetadataIn"])}
    ).named(renames["UpdateDeviceMetadataRequestIn"])
    types["UpdateDeviceMetadataRequestOut"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeviceMetadataRequestOut"])
    types["DpcIn"] = t.struct({"_": t.string().optional()}).named(renames["DpcIn"])
    types["DpcOut"] = t.struct(
        {
            "dpcName": t.string().optional(),
            "name": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DpcOut"])
    types["CompanyIn"] = t.struct(
        {
            "adminEmails": t.array(t.string()).optional(),
            "ownerEmails": t.array(t.string()),
            "companyName": t.string(),
            "languageCode": t.string().optional(),
            "skipWelcomeEmail": t.boolean().optional(),
        }
    ).named(renames["CompanyIn"])
    types["CompanyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "adminEmails": t.array(t.string()).optional(),
            "ownerEmails": t.array(t.string()),
            "companyName": t.string(),
            "languageCode": t.string().optional(),
            "termsStatus": t.string().optional(),
            "companyId": t.string().optional(),
            "googleWorkspaceAccount": t.proxy(
                renames["GoogleWorkspaceAccountOut"]
            ).optional(),
            "skipWelcomeEmail": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompanyOut"])
    types["ListVendorsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "vendors": t.array(t.proxy(renames["CompanyIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListVendorsResponseIn"])
    types["ListVendorsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "vendors": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVendorsResponseOut"])
    types["PerDeviceStatusInBatchIn"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "errorMessage": t.string().optional(),
            "status": t.string().optional(),
            "errorIdentifier": t.string().optional(),
        }
    ).named(renames["PerDeviceStatusInBatchIn"])
    types["PerDeviceStatusInBatchOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "errorMessage": t.string().optional(),
            "status": t.string().optional(),
            "errorIdentifier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerDeviceStatusInBatchOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["PartnerUnclaimIn"] = t.struct(
        {
            "sectionType": t.string(),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeDays": t.integer().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "deviceId": t.string(),
        }
    ).named(renames["PartnerUnclaimIn"])
    types["PartnerUnclaimOut"] = t.struct(
        {
            "sectionType": t.string(),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeDays": t.integer().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "deviceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerUnclaimOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])

    functions = {}
    functions["operationsGet"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVendorCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesFindByOwner"] = androiddeviceprovisioning.post(
        "v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata",
        t.struct(
            {
                "deviceId": t.string(),
                "metadataOwnerId": t.string(),
                "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesFindByIdentifier"] = androiddeviceprovisioning.post(
        "v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata",
        t.struct(
            {
                "deviceId": t.string(),
                "metadataOwnerId": t.string(),
                "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesClaim"] = androiddeviceprovisioning.post(
        "v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata",
        t.struct(
            {
                "deviceId": t.string(),
                "metadataOwnerId": t.string(),
                "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesGet"] = androiddeviceprovisioning.post(
        "v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata",
        t.struct(
            {
                "deviceId": t.string(),
                "metadataOwnerId": t.string(),
                "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUpdateMetadataAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata",
        t.struct(
            {
                "deviceId": t.string(),
                "metadataOwnerId": t.string(),
                "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUnclaimAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata",
        t.struct(
            {
                "deviceId": t.string(),
                "metadataOwnerId": t.string(),
                "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUnclaim"] = androiddeviceprovisioning.post(
        "v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata",
        t.struct(
            {
                "deviceId": t.string(),
                "metadataOwnerId": t.string(),
                "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesClaimAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata",
        t.struct(
            {
                "deviceId": t.string(),
                "metadataOwnerId": t.string(),
                "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesMetadata"] = androiddeviceprovisioning.post(
        "v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata",
        t.struct(
            {
                "deviceId": t.string(),
                "metadataOwnerId": t.string(),
                "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceMetadataOut"]),
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
    functions["customersDevicesList"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesApplyConfiguration"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesUnclaim"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesRemoveConfiguration"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesGet"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsGet"] = androiddeviceprovisioning.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsCreate"] = androiddeviceprovisioning.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsPatch"] = androiddeviceprovisioning.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsList"] = androiddeviceprovisioning.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsDelete"] = androiddeviceprovisioning.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
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

    return Import(
        importer="androiddeviceprovisioning",
        renames=renames,
        types=types,
        functions=functions,
    )
