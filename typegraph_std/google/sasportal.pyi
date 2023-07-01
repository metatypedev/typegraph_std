from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    SasPortalDeviceIn: t.typedef = ...
    SasPortalDeviceOut: t.typedef = ...
    SasPortalNodeIn: t.typedef = ...
    SasPortalNodeOut: t.typedef = ...
    SasPortalDeploymentAssociationIn: t.typedef = ...
    SasPortalDeploymentAssociationOut: t.typedef = ...
    SasPortalListCustomersResponseIn: t.typedef = ...
    SasPortalListCustomersResponseOut: t.typedef = ...
    SasPortalGetPolicyRequestIn: t.typedef = ...
    SasPortalGetPolicyRequestOut: t.typedef = ...
    SasPortalDeviceAirInterfaceIn: t.typedef = ...
    SasPortalDeviceAirInterfaceOut: t.typedef = ...
    SasPortalPolicyIn: t.typedef = ...
    SasPortalPolicyOut: t.typedef = ...
    SasPortalValidateInstallerRequestIn: t.typedef = ...
    SasPortalValidateInstallerRequestOut: t.typedef = ...
    SasPortalUpdateSignedDeviceRequestIn: t.typedef = ...
    SasPortalUpdateSignedDeviceRequestOut: t.typedef = ...
    SasPortalMigrateOrganizationMetadataIn: t.typedef = ...
    SasPortalMigrateOrganizationMetadataOut: t.typedef = ...
    SasPortalTestPermissionsResponseIn: t.typedef = ...
    SasPortalTestPermissionsResponseOut: t.typedef = ...
    SasPortalValidateInstallerResponseIn: t.typedef = ...
    SasPortalValidateInstallerResponseOut: t.typedef = ...
    SasPortalDpaMoveListIn: t.typedef = ...
    SasPortalDpaMoveListOut: t.typedef = ...
    SasPortalDeviceConfigIn: t.typedef = ...
    SasPortalDeviceConfigOut: t.typedef = ...
    SasPortalInstallationParamsIn: t.typedef = ...
    SasPortalInstallationParamsOut: t.typedef = ...
    SasPortalDeploymentIn: t.typedef = ...
    SasPortalDeploymentOut: t.typedef = ...
    SasPortalMoveDeviceRequestIn: t.typedef = ...
    SasPortalMoveDeviceRequestOut: t.typedef = ...
    SasPortalDeviceGrantIn: t.typedef = ...
    SasPortalDeviceGrantOut: t.typedef = ...
    SasPortalGenerateSecretResponseIn: t.typedef = ...
    SasPortalGenerateSecretResponseOut: t.typedef = ...
    SasPortalFrequencyRangeIn: t.typedef = ...
    SasPortalFrequencyRangeOut: t.typedef = ...
    SasPortalMoveDeploymentRequestIn: t.typedef = ...
    SasPortalMoveDeploymentRequestOut: t.typedef = ...
    SasPortalListDevicesResponseIn: t.typedef = ...
    SasPortalListDevicesResponseOut: t.typedef = ...
    SasPortalCheckHasProvisionedDeploymentResponseIn: t.typedef = ...
    SasPortalCheckHasProvisionedDeploymentResponseOut: t.typedef = ...
    SasPortalDeviceModelIn: t.typedef = ...
    SasPortalDeviceModelOut: t.typedef = ...
    SasPortalNrqzValidationIn: t.typedef = ...
    SasPortalNrqzValidationOut: t.typedef = ...
    SasPortalMigrateOrganizationResponseIn: t.typedef = ...
    SasPortalMigrateOrganizationResponseOut: t.typedef = ...
    SasPortalGenerateSecretRequestIn: t.typedef = ...
    SasPortalGenerateSecretRequestOut: t.typedef = ...
    SasPortalSetPolicyRequestIn: t.typedef = ...
    SasPortalSetPolicyRequestOut: t.typedef = ...
    SasPortalChannelWithScoreIn: t.typedef = ...
    SasPortalChannelWithScoreOut: t.typedef = ...
    SasPortalAssignmentIn: t.typedef = ...
    SasPortalAssignmentOut: t.typedef = ...
    SasPortalMigrateOrganizationRequestIn: t.typedef = ...
    SasPortalMigrateOrganizationRequestOut: t.typedef = ...
    SasPortalListNodesResponseIn: t.typedef = ...
    SasPortalListNodesResponseOut: t.typedef = ...
    SasPortalListDeploymentsResponseIn: t.typedef = ...
    SasPortalListDeploymentsResponseOut: t.typedef = ...
    SasPortalSignDeviceRequestIn: t.typedef = ...
    SasPortalSignDeviceRequestOut: t.typedef = ...
    SasPortalDeviceMetadataIn: t.typedef = ...
    SasPortalDeviceMetadataOut: t.typedef = ...
    SasPortalCustomerIn: t.typedef = ...
    SasPortalCustomerOut: t.typedef = ...
    SasPortalMoveNodeRequestIn: t.typedef = ...
    SasPortalMoveNodeRequestOut: t.typedef = ...
    SasPortalEmptyIn: t.typedef = ...
    SasPortalEmptyOut: t.typedef = ...
    SasPortalTestPermissionsRequestIn: t.typedef = ...
    SasPortalTestPermissionsRequestOut: t.typedef = ...
    SasPortalCreateSignedDeviceRequestIn: t.typedef = ...
    SasPortalCreateSignedDeviceRequestOut: t.typedef = ...
    SasPortalProvisionDeploymentRequestIn: t.typedef = ...
    SasPortalProvisionDeploymentRequestOut: t.typedef = ...
    SasPortalOperationIn: t.typedef = ...
    SasPortalOperationOut: t.typedef = ...
    SasPortalProvisionDeploymentResponseIn: t.typedef = ...
    SasPortalProvisionDeploymentResponseOut: t.typedef = ...
    SasPortalStatusIn: t.typedef = ...
    SasPortalStatusOut: t.typedef = ...

class FuncList:
    policiesGet: t.func = ...
    policiesTest: t.func = ...
    policiesSet: t.func = ...
    customersList: t.func = ...
    customersCheckHasProvisionedDeployment: t.func = ...
    customersPatch: t.func = ...
    customersProvisionDeployment: t.func = ...
    customersMigrateOrganization: t.func = ...
    customersGet: t.func = ...
    customersDeploymentsList: t.func = ...
    customersDeploymentsCreate: t.func = ...
    customersDeploymentsPatch: t.func = ...
    customersDeploymentsMove: t.func = ...
    customersDeploymentsGet: t.func = ...
    customersDeploymentsDelete: t.func = ...
    customersDeploymentsDevicesCreateSigned: t.func = ...
    customersDeploymentsDevicesCreate: t.func = ...
    customersDeploymentsDevicesList: t.func = ...
    customersNodesList: t.func = ...
    customersNodesMove: t.func = ...
    customersNodesCreate: t.func = ...
    customersNodesPatch: t.func = ...
    customersNodesGet: t.func = ...
    customersNodesDelete: t.func = ...
    customersNodesDevicesList: t.func = ...
    customersNodesDevicesCreateSigned: t.func = ...
    customersNodesDevicesCreate: t.func = ...
    customersNodesDeploymentsList: t.func = ...
    customersNodesDeploymentsCreate: t.func = ...
    customersNodesNodesList: t.func = ...
    customersNodesNodesCreate: t.func = ...
    customersDevicesGet: t.func = ...
    customersDevicesCreate: t.func = ...
    customersDevicesList: t.func = ...
    customersDevicesPatch: t.func = ...
    customersDevicesSignDevice: t.func = ...
    customersDevicesUpdateSigned: t.func = ...
    customersDevicesMove: t.func = ...
    customersDevicesDelete: t.func = ...
    customersDevicesCreateSigned: t.func = ...
    installerValidate: t.func = ...
    installerGenerateSecret: t.func = ...
    deploymentsGet: t.func = ...
    deploymentsDevicesPatch: t.func = ...
    deploymentsDevicesSignDevice: t.func = ...
    deploymentsDevicesDelete: t.func = ...
    deploymentsDevicesGet: t.func = ...
    deploymentsDevicesUpdateSigned: t.func = ...
    deploymentsDevicesMove: t.func = ...
    nodesGet: t.func = ...
    nodesDeploymentsDelete: t.func = ...
    nodesDeploymentsGet: t.func = ...
    nodesDeploymentsPatch: t.func = ...
    nodesDeploymentsMove: t.func = ...
    nodesDeploymentsList: t.func = ...
    nodesDeploymentsDevicesCreateSigned: t.func = ...
    nodesDeploymentsDevicesCreate: t.func = ...
    nodesDeploymentsDevicesList: t.func = ...
    nodesDevicesUpdateSigned: t.func = ...
    nodesDevicesSignDevice: t.func = ...
    nodesDevicesCreateSigned: t.func = ...
    nodesDevicesDelete: t.func = ...
    nodesDevicesPatch: t.func = ...
    nodesDevicesCreate: t.func = ...
    nodesDevicesMove: t.func = ...
    nodesDevicesGet: t.func = ...
    nodesDevicesList: t.func = ...
    nodesNodesDelete: t.func = ...
    nodesNodesCreate: t.func = ...
    nodesNodesGet: t.func = ...
    nodesNodesPatch: t.func = ...
    nodesNodesList: t.func = ...
    nodesNodesMove: t.func = ...
    nodesNodesNodesCreate: t.func = ...
    nodesNodesNodesList: t.func = ...
    nodesNodesDevicesCreate: t.func = ...
    nodesNodesDevicesList: t.func = ...
    nodesNodesDevicesCreateSigned: t.func = ...
    nodesNodesDeploymentsCreate: t.func = ...
    nodesNodesDeploymentsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_sasportal() -> Import: ...
