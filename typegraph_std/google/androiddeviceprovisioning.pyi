from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    DpcIn: t.typedef = ...
    DpcOut: t.typedef = ...
    ClaimDeviceResponseIn: t.typedef = ...
    ClaimDeviceResponseOut: t.typedef = ...
    ClaimDevicesRequestIn: t.typedef = ...
    ClaimDevicesRequestOut: t.typedef = ...
    ListVendorCustomersResponseIn: t.typedef = ...
    ListVendorCustomersResponseOut: t.typedef = ...
    DevicesLongRunningOperationResponseIn: t.typedef = ...
    DevicesLongRunningOperationResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ListCustomersResponseIn: t.typedef = ...
    ListCustomersResponseOut: t.typedef = ...
    PartnerUnclaimIn: t.typedef = ...
    PartnerUnclaimOut: t.typedef = ...
    DevicesLongRunningOperationMetadataIn: t.typedef = ...
    DevicesLongRunningOperationMetadataOut: t.typedef = ...
    ListVendorsResponseIn: t.typedef = ...
    ListVendorsResponseOut: t.typedef = ...
    FindDevicesByOwnerRequestIn: t.typedef = ...
    FindDevicesByOwnerRequestOut: t.typedef = ...
    UpdateDeviceMetadataInBatchRequestIn: t.typedef = ...
    UpdateDeviceMetadataInBatchRequestOut: t.typedef = ...
    UpdateDeviceMetadataRequestIn: t.typedef = ...
    UpdateDeviceMetadataRequestOut: t.typedef = ...
    FindDevicesByDeviceIdentifierResponseIn: t.typedef = ...
    FindDevicesByDeviceIdentifierResponseOut: t.typedef = ...
    CustomerListCustomersResponseIn: t.typedef = ...
    CustomerListCustomersResponseOut: t.typedef = ...
    DeviceMetadataIn: t.typedef = ...
    DeviceMetadataOut: t.typedef = ...
    CustomerListConfigurationsResponseIn: t.typedef = ...
    CustomerListConfigurationsResponseOut: t.typedef = ...
    DeviceIn: t.typedef = ...
    DeviceOut: t.typedef = ...
    UnclaimDevicesRequestIn: t.typedef = ...
    UnclaimDevicesRequestOut: t.typedef = ...
    CustomerRemoveConfigurationRequestIn: t.typedef = ...
    CustomerRemoveConfigurationRequestOut: t.typedef = ...
    CustomerListDpcsResponseIn: t.typedef = ...
    CustomerListDpcsResponseOut: t.typedef = ...
    CustomerApplyConfigurationRequestIn: t.typedef = ...
    CustomerApplyConfigurationRequestOut: t.typedef = ...
    DeviceClaimIn: t.typedef = ...
    DeviceClaimOut: t.typedef = ...
    FindDevicesByDeviceIdentifierRequestIn: t.typedef = ...
    FindDevicesByDeviceIdentifierRequestOut: t.typedef = ...
    FindDevicesByOwnerResponseIn: t.typedef = ...
    FindDevicesByOwnerResponseOut: t.typedef = ...
    PerDeviceStatusInBatchIn: t.typedef = ...
    PerDeviceStatusInBatchOut: t.typedef = ...
    DeviceIdentifierIn: t.typedef = ...
    DeviceIdentifierOut: t.typedef = ...
    DeviceReferenceIn: t.typedef = ...
    DeviceReferenceOut: t.typedef = ...
    ClaimDeviceRequestIn: t.typedef = ...
    ClaimDeviceRequestOut: t.typedef = ...
    PartnerClaimIn: t.typedef = ...
    PartnerClaimOut: t.typedef = ...
    OperationPerDeviceIn: t.typedef = ...
    OperationPerDeviceOut: t.typedef = ...
    CustomerListDevicesResponseIn: t.typedef = ...
    CustomerListDevicesResponseOut: t.typedef = ...
    UpdateMetadataArgumentsIn: t.typedef = ...
    UpdateMetadataArgumentsOut: t.typedef = ...
    UnclaimDeviceRequestIn: t.typedef = ...
    UnclaimDeviceRequestOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    GoogleWorkspaceAccountIn: t.typedef = ...
    GoogleWorkspaceAccountOut: t.typedef = ...
    CustomerUnclaimDeviceRequestIn: t.typedef = ...
    CustomerUnclaimDeviceRequestOut: t.typedef = ...
    CreateCustomerRequestIn: t.typedef = ...
    CreateCustomerRequestOut: t.typedef = ...
    ConfigurationIn: t.typedef = ...
    ConfigurationOut: t.typedef = ...
    CompanyIn: t.typedef = ...
    CompanyOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...

class FuncList:
    operationsGet: t.func = ...
    customersList: t.func = ...
    customersDpcsList: t.func = ...
    customersConfigurationsPatch: t.func = ...
    customersConfigurationsDelete: t.func = ...
    customersConfigurationsList: t.func = ...
    customersConfigurationsCreate: t.func = ...
    customersConfigurationsGet: t.func = ...
    customersDevicesUnclaim: t.func = ...
    customersDevicesApplyConfiguration: t.func = ...
    customersDevicesList: t.func = ...
    customersDevicesGet: t.func = ...
    customersDevicesRemoveConfiguration: t.func = ...
    partnersVendorsList: t.func = ...
    partnersVendorsCustomersList: t.func = ...
    partnersDevicesUpdateMetadataAsync: t.func = ...
    partnersDevicesFindByOwner: t.func = ...
    partnersDevicesFindByIdentifier: t.func = ...
    partnersDevicesMetadata: t.func = ...
    partnersDevicesUnclaimAsync: t.func = ...
    partnersDevicesUnclaim: t.func = ...
    partnersDevicesClaim: t.func = ...
    partnersDevicesGet: t.func = ...
    partnersDevicesClaimAsync: t.func = ...
    partnersCustomersCreate: t.func = ...
    partnersCustomersList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_androiddeviceprovisioning() -> Import: ...
