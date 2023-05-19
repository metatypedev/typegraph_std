from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_androiddeviceprovisioning() -> Import:
    androiddeviceprovisioning = HTTPRuntime(
        "https://androiddeviceprovisioning.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_androiddeviceprovisioning_1_ErrorResponse",
        "ClaimDeviceRequestIn": "_androiddeviceprovisioning_2_ClaimDeviceRequestIn",
        "ClaimDeviceRequestOut": "_androiddeviceprovisioning_3_ClaimDeviceRequestOut",
        "UpdateDeviceMetadataInBatchRequestIn": "_androiddeviceprovisioning_4_UpdateDeviceMetadataInBatchRequestIn",
        "UpdateDeviceMetadataInBatchRequestOut": "_androiddeviceprovisioning_5_UpdateDeviceMetadataInBatchRequestOut",
        "CustomerListCustomersResponseIn": "_androiddeviceprovisioning_6_CustomerListCustomersResponseIn",
        "CustomerListCustomersResponseOut": "_androiddeviceprovisioning_7_CustomerListCustomersResponseOut",
        "GoogleWorkspaceAccountIn": "_androiddeviceprovisioning_8_GoogleWorkspaceAccountIn",
        "GoogleWorkspaceAccountOut": "_androiddeviceprovisioning_9_GoogleWorkspaceAccountOut",
        "UpdateMetadataArgumentsIn": "_androiddeviceprovisioning_10_UpdateMetadataArgumentsIn",
        "UpdateMetadataArgumentsOut": "_androiddeviceprovisioning_11_UpdateMetadataArgumentsOut",
        "CustomerUnclaimDeviceRequestIn": "_androiddeviceprovisioning_12_CustomerUnclaimDeviceRequestIn",
        "CustomerUnclaimDeviceRequestOut": "_androiddeviceprovisioning_13_CustomerUnclaimDeviceRequestOut",
        "DpcIn": "_androiddeviceprovisioning_14_DpcIn",
        "DpcOut": "_androiddeviceprovisioning_15_DpcOut",
        "CustomerApplyConfigurationRequestIn": "_androiddeviceprovisioning_16_CustomerApplyConfigurationRequestIn",
        "CustomerApplyConfigurationRequestOut": "_androiddeviceprovisioning_17_CustomerApplyConfigurationRequestOut",
        "DeviceIn": "_androiddeviceprovisioning_18_DeviceIn",
        "DeviceOut": "_androiddeviceprovisioning_19_DeviceOut",
        "FindDevicesByDeviceIdentifierResponseIn": "_androiddeviceprovisioning_20_FindDevicesByDeviceIdentifierResponseIn",
        "FindDevicesByDeviceIdentifierResponseOut": "_androiddeviceprovisioning_21_FindDevicesByDeviceIdentifierResponseOut",
        "FindDevicesByDeviceIdentifierRequestIn": "_androiddeviceprovisioning_22_FindDevicesByDeviceIdentifierRequestIn",
        "FindDevicesByDeviceIdentifierRequestOut": "_androiddeviceprovisioning_23_FindDevicesByDeviceIdentifierRequestOut",
        "DeviceMetadataIn": "_androiddeviceprovisioning_24_DeviceMetadataIn",
        "DeviceMetadataOut": "_androiddeviceprovisioning_25_DeviceMetadataOut",
        "DeviceClaimIn": "_androiddeviceprovisioning_26_DeviceClaimIn",
        "DeviceClaimOut": "_androiddeviceprovisioning_27_DeviceClaimOut",
        "CustomerListConfigurationsResponseIn": "_androiddeviceprovisioning_28_CustomerListConfigurationsResponseIn",
        "CustomerListConfigurationsResponseOut": "_androiddeviceprovisioning_29_CustomerListConfigurationsResponseOut",
        "FindDevicesByOwnerResponseIn": "_androiddeviceprovisioning_30_FindDevicesByOwnerResponseIn",
        "FindDevicesByOwnerResponseOut": "_androiddeviceprovisioning_31_FindDevicesByOwnerResponseOut",
        "CustomerListDpcsResponseIn": "_androiddeviceprovisioning_32_CustomerListDpcsResponseIn",
        "CustomerListDpcsResponseOut": "_androiddeviceprovisioning_33_CustomerListDpcsResponseOut",
        "ClaimDevicesRequestIn": "_androiddeviceprovisioning_34_ClaimDevicesRequestIn",
        "ClaimDevicesRequestOut": "_androiddeviceprovisioning_35_ClaimDevicesRequestOut",
        "OperationIn": "_androiddeviceprovisioning_36_OperationIn",
        "OperationOut": "_androiddeviceprovisioning_37_OperationOut",
        "CustomerListDevicesResponseIn": "_androiddeviceprovisioning_38_CustomerListDevicesResponseIn",
        "CustomerListDevicesResponseOut": "_androiddeviceprovisioning_39_CustomerListDevicesResponseOut",
        "UnclaimDeviceRequestIn": "_androiddeviceprovisioning_40_UnclaimDeviceRequestIn",
        "UnclaimDeviceRequestOut": "_androiddeviceprovisioning_41_UnclaimDeviceRequestOut",
        "ClaimDeviceResponseIn": "_androiddeviceprovisioning_42_ClaimDeviceResponseIn",
        "ClaimDeviceResponseOut": "_androiddeviceprovisioning_43_ClaimDeviceResponseOut",
        "UpdateDeviceMetadataRequestIn": "_androiddeviceprovisioning_44_UpdateDeviceMetadataRequestIn",
        "UpdateDeviceMetadataRequestOut": "_androiddeviceprovisioning_45_UpdateDeviceMetadataRequestOut",
        "OperationPerDeviceIn": "_androiddeviceprovisioning_46_OperationPerDeviceIn",
        "OperationPerDeviceOut": "_androiddeviceprovisioning_47_OperationPerDeviceOut",
        "DeviceReferenceIn": "_androiddeviceprovisioning_48_DeviceReferenceIn",
        "DeviceReferenceOut": "_androiddeviceprovisioning_49_DeviceReferenceOut",
        "ListVendorCustomersResponseIn": "_androiddeviceprovisioning_50_ListVendorCustomersResponseIn",
        "ListVendorCustomersResponseOut": "_androiddeviceprovisioning_51_ListVendorCustomersResponseOut",
        "EmptyIn": "_androiddeviceprovisioning_52_EmptyIn",
        "EmptyOut": "_androiddeviceprovisioning_53_EmptyOut",
        "ListVendorsResponseIn": "_androiddeviceprovisioning_54_ListVendorsResponseIn",
        "ListVendorsResponseOut": "_androiddeviceprovisioning_55_ListVendorsResponseOut",
        "DevicesLongRunningOperationMetadataIn": "_androiddeviceprovisioning_56_DevicesLongRunningOperationMetadataIn",
        "DevicesLongRunningOperationMetadataOut": "_androiddeviceprovisioning_57_DevicesLongRunningOperationMetadataOut",
        "PartnerClaimIn": "_androiddeviceprovisioning_58_PartnerClaimIn",
        "PartnerClaimOut": "_androiddeviceprovisioning_59_PartnerClaimOut",
        "ConfigurationIn": "_androiddeviceprovisioning_60_ConfigurationIn",
        "ConfigurationOut": "_androiddeviceprovisioning_61_ConfigurationOut",
        "FindDevicesByOwnerRequestIn": "_androiddeviceprovisioning_62_FindDevicesByOwnerRequestIn",
        "FindDevicesByOwnerRequestOut": "_androiddeviceprovisioning_63_FindDevicesByOwnerRequestOut",
        "PerDeviceStatusInBatchIn": "_androiddeviceprovisioning_64_PerDeviceStatusInBatchIn",
        "PerDeviceStatusInBatchOut": "_androiddeviceprovisioning_65_PerDeviceStatusInBatchOut",
        "PartnerUnclaimIn": "_androiddeviceprovisioning_66_PartnerUnclaimIn",
        "PartnerUnclaimOut": "_androiddeviceprovisioning_67_PartnerUnclaimOut",
        "UnclaimDevicesRequestIn": "_androiddeviceprovisioning_68_UnclaimDevicesRequestIn",
        "UnclaimDevicesRequestOut": "_androiddeviceprovisioning_69_UnclaimDevicesRequestOut",
        "DeviceIdentifierIn": "_androiddeviceprovisioning_70_DeviceIdentifierIn",
        "DeviceIdentifierOut": "_androiddeviceprovisioning_71_DeviceIdentifierOut",
        "StatusIn": "_androiddeviceprovisioning_72_StatusIn",
        "StatusOut": "_androiddeviceprovisioning_73_StatusOut",
        "CreateCustomerRequestIn": "_androiddeviceprovisioning_74_CreateCustomerRequestIn",
        "CreateCustomerRequestOut": "_androiddeviceprovisioning_75_CreateCustomerRequestOut",
        "DevicesLongRunningOperationResponseIn": "_androiddeviceprovisioning_76_DevicesLongRunningOperationResponseIn",
        "DevicesLongRunningOperationResponseOut": "_androiddeviceprovisioning_77_DevicesLongRunningOperationResponseOut",
        "ListCustomersResponseIn": "_androiddeviceprovisioning_78_ListCustomersResponseIn",
        "ListCustomersResponseOut": "_androiddeviceprovisioning_79_ListCustomersResponseOut",
        "CompanyIn": "_androiddeviceprovisioning_80_CompanyIn",
        "CompanyOut": "_androiddeviceprovisioning_81_CompanyOut",
        "CustomerRemoveConfigurationRequestIn": "_androiddeviceprovisioning_82_CustomerRemoveConfigurationRequestIn",
        "CustomerRemoveConfigurationRequestOut": "_androiddeviceprovisioning_83_CustomerRemoveConfigurationRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ClaimDeviceRequestIn"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
            "sectionType": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "customerId": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "simlockProfileId": t.string().optional(),
            "preProvisioningToken": t.string().optional(),
        }
    ).named(renames["ClaimDeviceRequestIn"])
    types["ClaimDeviceRequestOut"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "sectionType": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "customerId": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "simlockProfileId": t.string().optional(),
            "preProvisioningToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClaimDeviceRequestOut"])
    types["UpdateDeviceMetadataInBatchRequestIn"] = t.struct(
        {"updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"]))}
    ).named(renames["UpdateDeviceMetadataInBatchRequestIn"])
    types["UpdateDeviceMetadataInBatchRequestOut"] = t.struct(
        {
            "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeviceMetadataInBatchRequestOut"])
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
    types["UpdateMetadataArgumentsIn"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
            "deviceId": t.string(),
        }
    ).named(renames["UpdateMetadataArgumentsIn"])
    types["UpdateMetadataArgumentsOut"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "deviceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateMetadataArgumentsOut"])
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
            "name": t.string().optional(),
            "dpcName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DpcOut"])
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
    types["DeviceIn"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]).optional(),
            "configuration": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]).optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]).optional(),
            "configuration": t.string().optional(),
            "deviceId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]).optional(),
            "claims": t.array(t.proxy(renames["DeviceClaimOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["FindDevicesByDeviceIdentifierResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierResponseIn"])
    types["FindDevicesByDeviceIdentifierResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierResponseOut"])
    types["FindDevicesByDeviceIdentifierRequestIn"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "limit": t.string(),
            "pageToken": t.string().optional(),
        }
    ).named(renames["FindDevicesByDeviceIdentifierRequestIn"])
    types["FindDevicesByDeviceIdentifierRequestOut"] = t.struct(
        {
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "limit": t.string(),
            "pageToken": t.string().optional(),
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
    types["DeviceClaimIn"] = t.struct(
        {
            "ownerCompanyId": t.string().optional(),
            "resellerId": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "additionalService": t.string().optional(),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeStartTime": t.string().optional(),
        }
    ).named(renames["DeviceClaimIn"])
    types["DeviceClaimOut"] = t.struct(
        {
            "ownerCompanyId": t.string().optional(),
            "resellerId": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "sectionType": t.string().optional(),
            "additionalService": t.string().optional(),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeStartTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceClaimOut"])
    types["CustomerListConfigurationsResponseIn"] = t.struct(
        {"configurations": t.array(t.proxy(renames["ConfigurationIn"])).optional()}
    ).named(renames["CustomerListConfigurationsResponseIn"])
    types["CustomerListConfigurationsResponseOut"] = t.struct(
        {
            "configurations": t.array(t.proxy(renames["ConfigurationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListConfigurationsResponseOut"])
    types["FindDevicesByOwnerResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
        }
    ).named(renames["FindDevicesByOwnerResponseIn"])
    types["FindDevicesByOwnerResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByOwnerResponseOut"])
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
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["CustomerListDevicesResponseIn"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["CustomerListDevicesResponseIn"])
    types["CustomerListDevicesResponseOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomerListDevicesResponseOut"])
    types["UnclaimDeviceRequestIn"] = t.struct(
        {
            "vacationModeExpireTime": t.string().optional(),
            "deviceId": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "sectionType": t.string(),
            "vacationModeDays": t.integer().optional(),
        }
    ).named(renames["UnclaimDeviceRequestIn"])
    types["UnclaimDeviceRequestOut"] = t.struct(
        {
            "vacationModeExpireTime": t.string().optional(),
            "deviceId": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "sectionType": t.string(),
            "vacationModeDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnclaimDeviceRequestOut"])
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
    types["UpdateDeviceMetadataRequestIn"] = t.struct(
        {"deviceMetadata": t.proxy(renames["DeviceMetadataIn"])}
    ).named(renames["UpdateDeviceMetadataRequestIn"])
    types["UpdateDeviceMetadataRequestOut"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDeviceMetadataRequestOut"])
    types["OperationPerDeviceIn"] = t.struct(
        {
            "claim": t.proxy(renames["PartnerClaimIn"]).optional(),
            "unclaim": t.proxy(renames["PartnerUnclaimIn"]).optional(),
            "updateMetadata": t.proxy(renames["UpdateMetadataArgumentsIn"]).optional(),
            "result": t.proxy(renames["PerDeviceStatusInBatchIn"]).optional(),
        }
    ).named(renames["OperationPerDeviceIn"])
    types["OperationPerDeviceOut"] = t.struct(
        {
            "claim": t.proxy(renames["PartnerClaimOut"]).optional(),
            "unclaim": t.proxy(renames["PartnerUnclaimOut"]).optional(),
            "updateMetadata": t.proxy(renames["UpdateMetadataArgumentsOut"]).optional(),
            "result": t.proxy(renames["PerDeviceStatusInBatchOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationPerDeviceOut"])
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
    types["ListVendorCustomersResponseIn"] = t.struct(
        {
            "customers": t.array(t.proxy(renames["CompanyIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
        }
    ).named(renames["ListVendorCustomersResponseIn"])
    types["ListVendorCustomersResponseOut"] = t.struct(
        {
            "customers": t.array(t.proxy(renames["CompanyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "totalSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVendorCustomersResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["DevicesLongRunningOperationMetadataIn"] = t.struct(
        {
            "progress": t.integer().optional(),
            "devicesCount": t.integer().optional(),
            "processingStatus": t.string().optional(),
        }
    ).named(renames["DevicesLongRunningOperationMetadataIn"])
    types["DevicesLongRunningOperationMetadataOut"] = t.struct(
        {
            "progress": t.integer().optional(),
            "devicesCount": t.integer().optional(),
            "processingStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicesLongRunningOperationMetadataOut"])
    types["PartnerClaimIn"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataIn"]),
            "sectionType": t.string(),
            "preProvisioningToken": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "customerId": t.string().optional(),
            "simlockProfileId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
        }
    ).named(renames["PartnerClaimIn"])
    types["PartnerClaimOut"] = t.struct(
        {
            "deviceMetadata": t.proxy(renames["DeviceMetadataOut"]),
            "sectionType": t.string(),
            "preProvisioningToken": t.string().optional(),
            "googleWorkspaceCustomerId": t.string().optional(),
            "customerId": t.string().optional(),
            "simlockProfileId": t.string().optional(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerClaimOut"])
    types["ConfigurationIn"] = t.struct(
        {
            "contactEmail": t.string(),
            "forcedResetTime": t.string().optional(),
            "contactPhone": t.string(),
            "isDefault": t.boolean(),
            "configurationName": t.string(),
            "companyName": t.string(),
            "dpcExtras": t.string().optional(),
            "dpcResourcePath": t.string(),
            "customMessage": t.string().optional(),
        }
    ).named(renames["ConfigurationIn"])
    types["ConfigurationOut"] = t.struct(
        {
            "contactEmail": t.string(),
            "forcedResetTime": t.string().optional(),
            "contactPhone": t.string(),
            "configurationId": t.string().optional(),
            "name": t.string().optional(),
            "isDefault": t.boolean(),
            "configurationName": t.string(),
            "companyName": t.string(),
            "dpcExtras": t.string().optional(),
            "dpcResourcePath": t.string(),
            "customMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigurationOut"])
    types["FindDevicesByOwnerRequestIn"] = t.struct(
        {
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.array(t.string()).optional(),
            "customerId": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "limit": t.string(),
        }
    ).named(renames["FindDevicesByOwnerRequestIn"])
    types["FindDevicesByOwnerRequestOut"] = t.struct(
        {
            "sectionType": t.string(),
            "googleWorkspaceCustomerId": t.array(t.string()).optional(),
            "customerId": t.array(t.string()).optional(),
            "pageToken": t.string().optional(),
            "limit": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindDevicesByOwnerRequestOut"])
    types["PerDeviceStatusInBatchIn"] = t.struct(
        {
            "errorIdentifier": t.string().optional(),
            "errorMessage": t.string().optional(),
            "status": t.string().optional(),
            "deviceId": t.string().optional(),
        }
    ).named(renames["PerDeviceStatusInBatchIn"])
    types["PerDeviceStatusInBatchOut"] = t.struct(
        {
            "errorIdentifier": t.string().optional(),
            "errorMessage": t.string().optional(),
            "status": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerDeviceStatusInBatchOut"])
    types["PartnerUnclaimIn"] = t.struct(
        {
            "sectionType": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierIn"]),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeDays": t.integer().optional(),
            "deviceId": t.string(),
        }
    ).named(renames["PartnerUnclaimIn"])
    types["PartnerUnclaimOut"] = t.struct(
        {
            "sectionType": t.string(),
            "deviceIdentifier": t.proxy(renames["DeviceIdentifierOut"]),
            "vacationModeExpireTime": t.string().optional(),
            "vacationModeDays": t.integer().optional(),
            "deviceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartnerUnclaimOut"])
    types["UnclaimDevicesRequestIn"] = t.struct(
        {"unclaims": t.array(t.proxy(renames["PartnerUnclaimIn"]))}
    ).named(renames["UnclaimDevicesRequestIn"])
    types["UnclaimDevicesRequestOut"] = t.struct(
        {
            "unclaims": t.array(t.proxy(renames["PartnerUnclaimOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UnclaimDevicesRequestOut"])
    types["DeviceIdentifierIn"] = t.struct(
        {
            "manufacturer": t.string().optional(),
            "deviceType": t.string().optional(),
            "model": t.string().optional(),
            "imei": t.string().optional(),
            "meid": t.string().optional(),
            "chromeOsAttestedDeviceId": t.string().optional(),
            "serialNumber": t.string().optional(),
        }
    ).named(renames["DeviceIdentifierIn"])
    types["DeviceIdentifierOut"] = t.struct(
        {
            "manufacturer": t.string().optional(),
            "deviceType": t.string().optional(),
            "model": t.string().optional(),
            "imei": t.string().optional(),
            "meid": t.string().optional(),
            "chromeOsAttestedDeviceId": t.string().optional(),
            "serialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceIdentifierOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["CreateCustomerRequestIn"] = t.struct(
        {"customer": t.proxy(renames["CompanyIn"])}
    ).named(renames["CreateCustomerRequestIn"])
    types["CreateCustomerRequestOut"] = t.struct(
        {
            "customer": t.proxy(renames["CompanyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateCustomerRequestOut"])
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
    types["CompanyIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "adminEmails": t.array(t.string()).optional(),
            "companyName": t.string(),
            "skipWelcomeEmail": t.boolean().optional(),
            "ownerEmails": t.array(t.string()),
        }
    ).named(renames["CompanyIn"])
    types["CompanyOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "adminEmails": t.array(t.string()).optional(),
            "companyName": t.string(),
            "skipWelcomeEmail": t.boolean().optional(),
            "name": t.string().optional(),
            "googleWorkspaceAccount": t.proxy(
                renames["GoogleWorkspaceAccountOut"]
            ).optional(),
            "termsStatus": t.string().optional(),
            "ownerEmails": t.array(t.string()),
            "companyId": t.string().optional(),
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

    functions = {}
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
    functions["customersDevicesApplyConfiguration"] = androiddeviceprovisioning.post(
        "v1/{parent}/devices:unclaim",
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
        "v1/{parent}/devices:unclaim",
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
        "v1/{parent}/devices:unclaim",
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
        "v1/{parent}/devices:unclaim",
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
    functions["customersDevicesUnclaim"] = androiddeviceprovisioning.post(
        "v1/{parent}/devices:unclaim",
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
    functions["customersDpcsList"] = androiddeviceprovisioning.get(
        "v1/{parent}/dpcs",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["CustomerListDpcsResponseOut"]),
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
    functions["customersConfigurationsPatch"] = androiddeviceprovisioning.get(
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
    functions["customersConfigurationsDelete"] = androiddeviceprovisioning.get(
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
    functions["partnersDevicesUnclaim"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:updateMetadataAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesFindByOwner"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:updateMetadataAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesMetadata"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:updateMetadataAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesClaim"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:updateMetadataAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesFindByIdentifier"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:updateMetadataAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesGet"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:updateMetadataAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesClaimAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:updateMetadataAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUnclaimAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:updateMetadataAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersDevicesUpdateMetadataAsync"] = androiddeviceprovisioning.post(
        "v1/partners/{partnerId}/devices:updateMetadataAsync",
        t.struct(
            {
                "partnerId": t.string(),
                "updates": t.array(t.proxy(renames["UpdateMetadataArgumentsIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["partnersVendorsList"] = androiddeviceprovisioning.get(
        "v1/{parent}/vendors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListVendorCustomersResponseOut"]),
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
