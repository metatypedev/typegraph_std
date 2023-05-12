from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_androiddeviceprovisioning() -> Import:
    androiddeviceprovisioning = HTTPRuntime(
        "https://androiddeviceprovisioning.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_androiddeviceprovisioning_1_ErrorResponse",
        "DpcIn": "_androiddeviceprovisioning_2_DpcIn",
        "DpcOut": "_androiddeviceprovisioning_3_DpcOut",
        "ClaimDeviceResponseIn": "_androiddeviceprovisioning_4_ClaimDeviceResponseIn",
        "ClaimDeviceResponseOut": "_androiddeviceprovisioning_5_ClaimDeviceResponseOut",
        "ClaimDevicesRequestIn": "_androiddeviceprovisioning_6_ClaimDevicesRequestIn",
        "ClaimDevicesRequestOut": "_androiddeviceprovisioning_7_ClaimDevicesRequestOut",
        "ListVendorCustomersResponseIn": "_androiddeviceprovisioning_8_ListVendorCustomersResponseIn",
        "ListVendorCustomersResponseOut": "_androiddeviceprovisioning_9_ListVendorCustomersResponseOut",
        "DevicesLongRunningOperationResponseIn": "_androiddeviceprovisioning_10_DevicesLongRunningOperationResponseIn",
        "DevicesLongRunningOperationResponseOut": "_androiddeviceprovisioning_11_DevicesLongRunningOperationResponseOut",
        "EmptyIn": "_androiddeviceprovisioning_12_EmptyIn",
        "EmptyOut": "_androiddeviceprovisioning_13_EmptyOut",
        "ListCustomersResponseIn": "_androiddeviceprovisioning_14_ListCustomersResponseIn",
        "ListCustomersResponseOut": "_androiddeviceprovisioning_15_ListCustomersResponseOut",
        "PartnerUnclaimIn": "_androiddeviceprovisioning_16_PartnerUnclaimIn",
        "PartnerUnclaimOut": "_androiddeviceprovisioning_17_PartnerUnclaimOut",
        "DevicesLongRunningOperationMetadataIn": "_androiddeviceprovisioning_18_DevicesLongRunningOperationMetadataIn",
        "DevicesLongRunningOperationMetadataOut": "_androiddeviceprovisioning_19_DevicesLongRunningOperationMetadataOut",
        "ListVendorsResponseIn": "_androiddeviceprovisioning_20_ListVendorsResponseIn",
        "ListVendorsResponseOut": "_androiddeviceprovisioning_21_ListVendorsResponseOut",
        "FindDevicesByOwnerRequestIn": "_androiddeviceprovisioning_22_FindDevicesByOwnerRequestIn",
        "FindDevicesByOwnerRequestOut": "_androiddeviceprovisioning_23_FindDevicesByOwnerRequestOut",
        "UpdateDeviceMetadataInBatchRequestIn": "_androiddeviceprovisioning_24_UpdateDeviceMetadataInBatchRequestIn",
        "UpdateDeviceMetadataInBatchRequestOut": "_androiddeviceprovisioning_25_UpdateDeviceMetadataInBatchRequestOut",
        "UpdateDeviceMetadataRequestIn": "_androiddeviceprovisioning_26_UpdateDeviceMetadataRequestIn",
        "UpdateDeviceMetadataRequestOut": "_androiddeviceprovisioning_27_UpdateDeviceMetadataRequestOut",
        "FindDevicesByDeviceIdentifierResponseIn": "_androiddeviceprovisioning_28_FindDevicesByDeviceIdentifierResponseIn",
        "FindDevicesByDeviceIdentifierResponseOut": "_androiddeviceprovisioning_29_FindDevicesByDeviceIdentifierResponseOut",
        "CustomerListCustomersResponseIn": "_androiddeviceprovisioning_30_CustomerListCustomersResponseIn",
        "CustomerListCustomersResponseOut": "_androiddeviceprovisioning_31_CustomerListCustomersResponseOut",
        "DeviceMetadataIn": "_androiddeviceprovisioning_32_DeviceMetadataIn",
        "DeviceMetadataOut": "_androiddeviceprovisioning_33_DeviceMetadataOut",
        "CustomerListConfigurationsResponseIn": "_androiddeviceprovisioning_34_CustomerListConfigurationsResponseIn",
        "CustomerListConfigurationsResponseOut": "_androiddeviceprovisioning_35_CustomerListConfigurationsResponseOut",
        "DeviceIn": "_androiddeviceprovisioning_36_DeviceIn",
        "DeviceOut": "_androiddeviceprovisioning_37_DeviceOut",
        "UnclaimDevicesRequestIn": "_androiddeviceprovisioning_38_UnclaimDevicesRequestIn",
        "UnclaimDevicesRequestOut": "_androiddeviceprovisioning_39_UnclaimDevicesRequestOut",
        "CustomerRemoveConfigurationRequestIn": "_androiddeviceprovisioning_40_CustomerRemoveConfigurationRequestIn",
        "CustomerRemoveConfigurationRequestOut": "_androiddeviceprovisioning_41_CustomerRemoveConfigurationRequestOut",
        "CustomerListDpcsResponseIn": "_androiddeviceprovisioning_42_CustomerListDpcsResponseIn",
        "CustomerListDpcsResponseOut": "_androiddeviceprovisioning_43_CustomerListDpcsResponseOut",
        "CustomerApplyConfigurationRequestIn": "_androiddeviceprovisioning_44_CustomerApplyConfigurationRequestIn",
        "CustomerApplyConfigurationRequestOut": "_androiddeviceprovisioning_45_CustomerApplyConfigurationRequestOut",
        "DeviceClaimIn": "_androiddeviceprovisioning_46_DeviceClaimIn",
        "DeviceClaimOut": "_androiddeviceprovisioning_47_DeviceClaimOut",
        "FindDevicesByDeviceIdentifierRequestIn": "_androiddeviceprovisioning_48_FindDevicesByDeviceIdentifierRequestIn",
        "FindDevicesByDeviceIdentifierRequestOut": "_androiddeviceprovisioning_49_FindDevicesByDeviceIdentifierRequestOut",
        "FindDevicesByOwnerResponseIn": "_androiddeviceprovisioning_50_FindDevicesByOwnerResponseIn",
        "FindDevicesByOwnerResponseOut": "_androiddeviceprovisioning_51_FindDevicesByOwnerResponseOut",
        "PerDeviceStatusInBatchIn": "_androiddeviceprovisioning_52_PerDeviceStatusInBatchIn",
        "PerDeviceStatusInBatchOut": "_androiddeviceprovisioning_53_PerDeviceStatusInBatchOut",
        "DeviceIdentifierIn": "_androiddeviceprovisioning_54_DeviceIdentifierIn",
        "DeviceIdentifierOut": "_androiddeviceprovisioning_55_DeviceIdentifierOut",
        "DeviceReferenceIn": "_androiddeviceprovisioning_56_DeviceReferenceIn",
        "DeviceReferenceOut": "_androiddeviceprovisioning_57_DeviceReferenceOut",
        "ClaimDeviceRequestIn": "_androiddeviceprovisioning_58_ClaimDeviceRequestIn",
        "ClaimDeviceRequestOut": "_androiddeviceprovisioning_59_ClaimDeviceRequestOut",
        "PartnerClaimIn": "_androiddeviceprovisioning_60_PartnerClaimIn",
        "PartnerClaimOut": "_androiddeviceprovisioning_61_PartnerClaimOut",
        "OperationPerDeviceIn": "_androiddeviceprovisioning_62_OperationPerDeviceIn",
        "OperationPerDeviceOut": "_androiddeviceprovisioning_63_OperationPerDeviceOut",
        "CustomerListDevicesResponseIn": "_androiddeviceprovisioning_64_CustomerListDevicesResponseIn",
        "CustomerListDevicesResponseOut": "_androiddeviceprovisioning_65_CustomerListDevicesResponseOut",
        "UpdateMetadataArgumentsIn": "_androiddeviceprovisioning_66_UpdateMetadataArgumentsIn",
        "UpdateMetadataArgumentsOut": "_androiddeviceprovisioning_67_UpdateMetadataArgumentsOut",
        "UnclaimDeviceRequestIn": "_androiddeviceprovisioning_68_UnclaimDeviceRequestIn",
        "UnclaimDeviceRequestOut": "_androiddeviceprovisioning_69_UnclaimDeviceRequestOut",
        "StatusIn": "_androiddeviceprovisioning_70_StatusIn",
        "StatusOut": "_androiddeviceprovisioning_71_StatusOut",
        "GoogleWorkspaceAccountIn": "_androiddeviceprovisioning_72_GoogleWorkspaceAccountIn",
        "GoogleWorkspaceAccountOut": "_androiddeviceprovisioning_73_GoogleWorkspaceAccountOut",
        "CustomerUnclaimDeviceRequestIn": "_androiddeviceprovisioning_74_CustomerUnclaimDeviceRequestIn",
        "CustomerUnclaimDeviceRequestOut": "_androiddeviceprovisioning_75_CustomerUnclaimDeviceRequestOut",
        "CreateCustomerRequestIn": "_androiddeviceprovisioning_76_CreateCustomerRequestIn",
        "CreateCustomerRequestOut": "_androiddeviceprovisioning_77_CreateCustomerRequestOut",
        "ConfigurationIn": "_androiddeviceprovisioning_78_ConfigurationIn",
        "ConfigurationOut": "_androiddeviceprovisioning_79_ConfigurationOut",
        "CompanyIn": "_androiddeviceprovisioning_80_CompanyIn",
        "CompanyOut": "_androiddeviceprovisioning_81_CompanyOut",
        "OperationIn": "_androiddeviceprovisioning_82_OperationIn",
        "OperationOut": "_androiddeviceprovisioning_83_OperationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DpcIn"] = t.struct({"_": t.string().optional()}).named(renames["DpcIn"])
    types["DpcOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "dpcName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DpcOut"])
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
    types["ClaimDevicesRequestIn"] = t.struct(
        {"claims": t.array(t.proxy(renames["PartnerClaimIn"]))}
    ).named(renames["ClaimDevicesRequestIn"])
    types["ClaimDevicesRequestOut"] = t.struct(
        {
            "claims": t.array(t.proxy(renames["PartnerClaimOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClaimDevicesRequestOut"])
    types["ListVendorCustomersResponseIn"] = t.struct(
        {
            "customers": t.array(t.proxy(renames["CompanyIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVendorCustomersResponseIn"])
    types["ListVendorCustomersResponseOut"] = t.struct(
        {
            "customers": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVendorCustomersResponseOut"])
    types["DevicesLongRunningOperationResponseIn"] = t.struct(
        {
            "successCount": t.integer().optional(),
            "perDeviceStatus": t.array(
                t.proxy(renames["OperationPerDeviceIn"])
            ).optional(),
        }
    ).named(renames["DevicesLongRunningOperationResponseIn"])
    types["DevicesLongRunningOperationResponseOut"] = t.struct(
        {
            "successCount": t.integer().optional(),
            "perDeviceStatus": t.array(
                t.proxy(renames["OperationPerDeviceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicesLongRunningOperationResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["PartnerUnclaimIn"] = t.struct(
        {
            "deviceId": t.string(),
            "vacationModeDays": t.integer().optional(),
            "vacationModeExpireTime": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "sectionType": t.string(),
        }
    ).named(renames["PartnerUnclaimIn"])
    types["PartnerUnclaimOut"] = t.struct(
        {
            "deviceId": t.string(),
            "vacationModeDays": t.integer().optional(),
            "vacationModeExpireTime": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "sectionType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerUnclaimOut"])
    types["DevicesLongRunningOperationMetadataIn"] = t.struct(
        {
            "processingStatus": t.string().optional(),
            "progress": t.integer().optional(),
            "devicesCount": t.integer().optional(),
        }
    ).named(renames["DevicesLongRunningOperationMetadataIn"])
    types["DevicesLongRunningOperationMetadataOut"] = t.struct(
        {
            "processingStatus": t.string().optional(),
            "progress": t.integer().optional(),
            "devicesCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicesLongRunningOperationMetadataOut"])
    types["ListVendorsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "vendors": t.array(t.proxy(renames["CompanyIn"])).optional(),
        }
    ).named(renames["ListVendorsResponseIn"])
    types["ListVendorsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "vendors": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVendorsResponseOut"])
    types["FindDevicesByOwnerRequestIn"] = t.struct(
        {
            "limit": t.string(),
            "pageToken": t.string().optional(),
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.array(t.string()).optional(),
            "customerId": t.array(t.string()).optional(),
        }
    ).named(renames["FindDevicesByOwnerRequestIn"])
    types["FindDevicesByOwnerRequestOut"] = t.struct(
        {
            "limit": t.string(),
            "pageToken": t.string().optional(),
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.array(t.string()).optional(),
            "customerId": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByOwnerRequestOut"])
    types["UpdateDeviceMetadataInBatchRequestIn"] = t.struct(
        {"updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"]))}
    ).named(renames["UpdateDeviceMetadataInBatchRequestIn"])
    types["UpdateDeviceMetadataInBatchRequestOut"] = t.struct(
        {
            "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeviceMetadataInBatchRequestOut"])
    types["UpdateDeviceMetadataRequestIn"] = t.struct(
        {"deviceMetadata": t.proxy(renames["DeviceMetadataIn"])}
    ).named(renames["UpdateDeviceMetadataRequestIn"])
    types["UpdateDeviceMetadataRequestOut"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeviceMetadataRequestOut"])
    types["FindDevicesByDeviceIdentifierResponseIn"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierResponseIn"])
    types["FindDevicesByDeviceIdentifierResponseOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "totalSize": t.integer().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierResponseOut"])
    types["CustomerListCustomersResponseIn"] = t.struct(
        {
            "customers": t.array(t.proxy(renames["CompanyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CustomerListCustomersResponseIn"])
    types["CustomerListCustomersResponseOut"] = t.struct(
        {
            "customers": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListCustomersResponseOut"])
    types["DeviceMetadataIn"] = t.struct(
        {"entries": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["DeviceMetadataIn"])
    types["DeviceMetadataOut"] = t.struct(
        {
            "entries": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceMetadataOut"])
    types["CustomerListConfigurationsResponseIn"] = t.struct(
        {"configurations": t.array(t.proxy(renames["ConfigurationIn"])).optional()}
    ).named(renames["CustomerListConfigurationsResponseIn"])
    types["CustomerListConfigurationsResponseOut"] = t.struct(
        {
            "configurations": t.array(t.proxy(renames["ConfigurationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListConfigurationsResponseOut"])
    types["DeviceIn"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]).optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
            "configuration": t.string().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]).optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "claims": t.array(t.proxy(renames["DeviceClaimOut"])).optional(),
            "configuration": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["UnclaimDevicesRequestIn"] = t.struct(
        {"unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"]))}
    ).named(renames["UnclaimDevicesRequestIn"])
    types["UnclaimDevicesRequestOut"] = t.struct(
        {
            "unclaims": t.array(t.proxy(renames["PartnerUnclaimOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnclaimDevicesRequestOut"])
    types["CustomerRemoveConfigurationRequestIn"] = t.struct(
        {"device": t.proxy(renames["DeviceReferenceIn"])}
    ).named(renames["CustomerRemoveConfigurationRequestIn"])
    types["CustomerRemoveConfigurationRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["DeviceReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerRemoveConfigurationRequestOut"])
    types["CustomerListDpcsResponseIn"] = t.struct(
        {"dpcs": t.array(t.proxy(renames["DpcIn"])).optional()}
    ).named(renames["CustomerListDpcsResponseIn"])
    types["CustomerListDpcsResponseOut"] = t.struct(
        {
            "dpcs": t.array(t.proxy(renames["DpcOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListDpcsResponseOut"])
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
    types["DeviceClaimIn"] = t.struct(
        {
            "vacationModeStartTime": t.string().optional(),
            "vacationModeExpireTime": t.string().optional(),
            "ownerCompanyId": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "additionalService": t.string().optional(),
            "resellerId": t.string().optional(),
        }
    ).named(renames["DeviceClaimIn"])
    types["DeviceClaimOut"] = t.struct(
        {
            "vacationModeStartTime": t.string().optional(),
            "vacationModeExpireTime": t.string().optional(),
            "sectionType": t.string().optional(),
            "ownerCompanyId": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "additionalService": t.string().optional(),
            "resellerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceClaimOut"])
    types["FindDevicesByDeviceIdentifierRequestIn"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "limit": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
        }
    ).named(renames["FindDevicesByDeviceIdentifierRequestIn"])
    types["FindDevicesByDeviceIdentifierRequestOut"] = t.struct(
        {
            "pageToken": t.string().optional(),
            "limit": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierRequestOut"])
    types["FindDevicesByOwnerResponseIn"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["FindDevicesByOwnerResponseIn"])
    types["FindDevicesByOwnerResponseOut"] = t.struct(
        {
            "totalSize": t.integer().optional(),
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByOwnerResponseOut"])
    types["PerDeviceStatusInBatchIn"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "errorMessage": t.string().optional(),
            "errorIdentifier": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["PerDeviceStatusInBatchIn"])
    types["PerDeviceStatusInBatchOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "errorMessage": t.string().optional(),
            "errorIdentifier": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerDeviceStatusInBatchOut"])
    types["DeviceIdentifierIn"] = t.struct(
        {
            "meid": t.string().optional(),
            "imei": t.string().optional(),
            "manufacturer": t.string().optional(),
            "model": t.string().optional(),
            "deviceType": t.string().optional(),
            "serialNumber": t.string().optional(),
            "chromeOsAttestedDeviceId": t.string().optional(),
        }
    ).named(renames["DeviceIdentifierIn"])
    types["DeviceIdentifierOut"] = t.struct(
        {
            "meid": t.string().optional(),
            "imei": t.string().optional(),
            "manufacturer": t.string().optional(),
            "model": t.string().optional(),
            "deviceType": t.string().optional(),
            "serialNumber": t.string().optional(),
            "chromeOsAttestedDeviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIdentifierOut"])
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
    types["ClaimDeviceRequestIn"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "googleWorkspaceCustomerId": t.string().optional(),
            "customerId": t.string().optional(),
            "preProvisioningToken": t.string().optional(),
            "sectionType": t.string(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
            "simlockProfileId": t.string().optional(),
        }
    ).named(renames["ClaimDeviceRequestIn"])
    types["ClaimDeviceRequestOut"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "googleWorkspaceCustomerId": t.string().optional(),
            "customerId": t.string().optional(),
            "preProvisioningToken": t.string().optional(),
            "sectionType": t.string(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "simlockProfileId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClaimDeviceRequestOut"])
    types["PartnerClaimIn"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
            "simlockProfileId": t.string().optional(),
            "customerId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "preProvisioningToken": t.string().optional(),
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.string().optional(),
        }
    ).named(renames["PartnerClaimIn"])
    types["PartnerClaimOut"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "simlockProfileId": t.string().optional(),
            "customerId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "preProvisioningToken": t.string().optional(),
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerClaimOut"])
    types["OperationPerDeviceIn"] = t.struct(
        {
            "updateMetadata": t.proxy(renames["UpdateMetadataArgumentsIn"]).optional(),
            "result": t.proxy(renames["PerDeviceStatusInBatchIn"]).optional(),
            "claim": t.proxy(renames["PartnerClaimIn"]).optional(),
            "unclaim": t.proxy(renames["PartnerUnclaimIn"]).optional(),
        }
    ).named(renames["OperationPerDeviceIn"])
    types["OperationPerDeviceOut"] = t.struct(
        {
            "updateMetadata": t.proxy(renames["UpdateMetadataArgumentsOut"]).optional(),
            "result": t.proxy(renames["PerDeviceStatusInBatchOut"]).optional(),
            "claim": t.proxy(renames["PartnerClaimOut"]).optional(),
            "unclaim": t.proxy(renames["PartnerUnclaimOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationPerDeviceOut"])
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
    types["UnclaimDeviceRequestIn"] = t.struct(
        {
            "sectionType": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "deviceId": t.string(),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeDays": t.integer().optional(),
        }
    ).named(renames["UnclaimDeviceRequestIn"])
    types["UnclaimDeviceRequestOut"] = t.struct(
        {
            "sectionType": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "deviceId": t.string(),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnclaimDeviceRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["CustomerUnclaimDeviceRequestIn"] = t.struct(
        {"device": t.proxy(renames["DeviceReferenceIn"])}
    ).named(renames["CustomerUnclaimDeviceRequestIn"])
    types["CustomerUnclaimDeviceRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["DeviceReferenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerUnclaimDeviceRequestOut"])
    types["CreateCustomerRequestIn"] = t.struct(
        {"customer": t.proxy(renames["CompanyIn"])}
    ).named(renames["CreateCustomerRequestIn"])
    types["CreateCustomerRequestOut"] = t.struct(
        {
            "customer": t.proxy(renames["CompanyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCustomerRequestOut"])
    types["ConfigurationIn"] = t.struct(
        {
            "configurationName": t.string(),
            "dpcResourcePath": t.string(),
            "contactEmail": t.string(),
            "forcedResetTime": t.string().optional(),
            "companyName": t.string(),
            "dpcExtras": t.string().optional(),
            "contactPhone": t.string(),
            "customMessage": t.string().optional(),
            "isDefault": t.boolean(),
        }
    ).named(renames["ConfigurationIn"])
    types["ConfigurationOut"] = t.struct(
        {
            "configurationName": t.string(),
            "dpcResourcePath": t.string(),
            "configurationId": t.string().optional(),
            "contactEmail": t.string(),
            "forcedResetTime": t.string().optional(),
            "companyName": t.string(),
            "dpcExtras": t.string().optional(),
            "contactPhone": t.string(),
            "customMessage": t.string().optional(),
            "isDefault": t.boolean(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigurationOut"])
    types["CompanyIn"] = t.struct(
        {
            "ownerEmails": t.array(t.string()),
            "languageCode": t.string().optional(),
            "skipWelcomeEmail": t.boolean().optional(),
            "companyName": t.string(),
            "adminEmails": t.array(t.string()).optional(),
        }
    ).named(renames["CompanyIn"])
    types["CompanyOut"] = t.struct(
        {
            "ownerEmails": t.array(t.string()),
            "languageCode": t.string().optional(),
            "companyId": t.string().optional(),
            "googleWorkspaceAccount": t.proxy(
                renames["GoogleWorkspaceAccountOut"]
            ).optional(),
            "termsStatus": t.string().optional(),
            "name": t.string().optional(),
            "skipWelcomeEmail": t.boolean().optional(),
            "companyName": t.string(),
            "adminEmails": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CompanyOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])

    functions = {}
    functions["operationsGet"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
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
    functions["customersConfigurationsPatch"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsDelete"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsList"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsCreate"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersConfigurationsGet"] = androiddeviceprovisioning.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ConfigurationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesUnclaim"] = androiddeviceprovisioning.post(
        "v1/{parent}/devices:removeConfiguration",
        t.struct(
            {
                "parent": t.string(),
                "device": t.proxy(renames["DeviceReferenceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesApplyConfiguration"] = androiddeviceprovisioning.post(
        "v1/{parent}/devices:removeConfiguration",
        t.struct(
            {
                "parent": t.string(),
                "device": t.proxy(renames["DeviceReferenceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesList"] = androiddeviceprovisioning.post(
        "v1/{parent}/devices:removeConfiguration",
        t.struct(
            {
                "parent": t.string(),
                "device": t.proxy(renames["DeviceReferenceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesGet"] = androiddeviceprovisioning.post(
        "v1/{parent}/devices:removeConfiguration",
        t.struct(
            {
                "parent": t.string(),
                "device": t.proxy(renames["DeviceReferenceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["customersDevicesRemoveConfiguration"] = androiddeviceprovisioning.post(
        "v1/{parent}/devices:removeConfiguration",
        t.struct(
            {
                "parent": t.string(),
                "device": t.proxy(renames["DeviceReferenceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVendorCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUpdateMetadataAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:claimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "claims": t.array(t.proxy(renames["PartnerClaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesFindByOwner"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:claimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "claims": t.array(t.proxy(renames["PartnerClaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesFindByIdentifier"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:claimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "claims": t.array(t.proxy(renames["PartnerClaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesMetadata"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:claimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "claims": t.array(t.proxy(renames["PartnerClaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUnclaimAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:claimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "claims": t.array(t.proxy(renames["PartnerClaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUnclaim"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:claimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "claims": t.array(t.proxy(renames["PartnerClaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesClaim"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:claimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "claims": t.array(t.proxy(renames["PartnerClaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesGet"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:claimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "claims": t.array(t.proxy(renames["PartnerClaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesClaimAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:claimAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "claims": t.array(t.proxy(renames["PartnerClaimIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersCustomersCreate"] = androiddeviceprovisioning.get(
        "v1/partners/{partnerId}/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersCustomersList"] = androiddeviceprovisioning.get(
        "v1/partners/{partnerId}/customers",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "partnerId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCustomersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="androiddeviceprovisioning",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
