from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ValidationCAIn: t.typedef = ...
    ValidationCAOut: t.typedef = ...
    ListServerTlsPoliciesResponseIn: t.typedef = ...
    ListServerTlsPoliciesResponseOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    ListTlsInspectionPoliciesResponseIn: t.typedef = ...
    ListTlsInspectionPoliciesResponseOut: t.typedef = ...
    MTLSPolicyIn: t.typedef = ...
    MTLSPolicyOut: t.typedef = ...
    ListGatewaySecurityPoliciesResponseIn: t.typedef = ...
    ListGatewaySecurityPoliciesResponseOut: t.typedef = ...
    SourceIn: t.typedef = ...
    SourceOut: t.typedef = ...
    GoogleIamV1SetIamPolicyRequestIn: t.typedef = ...
    GoogleIamV1SetIamPolicyRequestOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    GoogleCloudNetworksecurityV1CertificateProviderIn: t.typedef = ...
    GoogleCloudNetworksecurityV1CertificateProviderOut: t.typedef = ...
    TlsInspectionPolicyIn: t.typedef = ...
    TlsInspectionPolicyOut: t.typedef = ...
    ListClientTlsPoliciesResponseIn: t.typedef = ...
    ListClientTlsPoliciesResponseOut: t.typedef = ...
    AuthorizationPolicyIn: t.typedef = ...
    AuthorizationPolicyOut: t.typedef = ...
    ClientTlsPolicyIn: t.typedef = ...
    ClientTlsPolicyOut: t.typedef = ...
    UrlListIn: t.typedef = ...
    UrlListOut: t.typedef = ...
    ListAuthorizationPoliciesResponseIn: t.typedef = ...
    ListAuthorizationPoliciesResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    ListGatewaySecurityPolicyRulesResponseIn: t.typedef = ...
    ListGatewaySecurityPolicyRulesResponseOut: t.typedef = ...
    DestinationIn: t.typedef = ...
    DestinationOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    GatewaySecurityPolicyRuleIn: t.typedef = ...
    GatewaySecurityPolicyRuleOut: t.typedef = ...
    ServerTlsPolicyIn: t.typedef = ...
    ServerTlsPolicyOut: t.typedef = ...
    HttpHeaderMatchIn: t.typedef = ...
    HttpHeaderMatchOut: t.typedef = ...
    GoogleIamV1BindingIn: t.typedef = ...
    GoogleIamV1BindingOut: t.typedef = ...
    GoogleCloudNetworksecurityV1GrpcEndpointIn: t.typedef = ...
    GoogleCloudNetworksecurityV1GrpcEndpointOut: t.typedef = ...
    GoogleIamV1AuditLogConfigIn: t.typedef = ...
    GoogleIamV1AuditLogConfigOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    GoogleIamV1PolicyIn: t.typedef = ...
    GoogleIamV1PolicyOut: t.typedef = ...
    RuleIn: t.typedef = ...
    RuleOut: t.typedef = ...
    ListUrlListsResponseIn: t.typedef = ...
    ListUrlListsResponseOut: t.typedef = ...
    GoogleIamV1TestIamPermissionsResponseIn: t.typedef = ...
    GoogleIamV1TestIamPermissionsResponseOut: t.typedef = ...
    CertificateProviderInstanceIn: t.typedef = ...
    CertificateProviderInstanceOut: t.typedef = ...
    GatewaySecurityPolicyIn: t.typedef = ...
    GatewaySecurityPolicyOut: t.typedef = ...
    GoogleIamV1AuditConfigIn: t.typedef = ...
    GoogleIamV1AuditConfigOut: t.typedef = ...
    GoogleIamV1TestIamPermissionsRequestIn: t.typedef = ...
    GoogleIamV1TestIamPermissionsRequestOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsAuthorizationPoliciesCreate: t.func = ...
    projectsLocationsAuthorizationPoliciesPatch: t.func = ...
    projectsLocationsAuthorizationPoliciesDelete: t.func = ...
    projectsLocationsAuthorizationPoliciesSetIamPolicy: t.func = ...
    projectsLocationsAuthorizationPoliciesTestIamPermissions: t.func = ...
    projectsLocationsAuthorizationPoliciesList: t.func = ...
    projectsLocationsAuthorizationPoliciesGetIamPolicy: t.func = ...
    projectsLocationsAuthorizationPoliciesGet: t.func = ...
    projectsLocationsTlsInspectionPoliciesPatch: t.func = ...
    projectsLocationsTlsInspectionPoliciesCreate: t.func = ...
    projectsLocationsTlsInspectionPoliciesDelete: t.func = ...
    projectsLocationsTlsInspectionPoliciesList: t.func = ...
    projectsLocationsTlsInspectionPoliciesGet: t.func = ...
    projectsLocationsUrlListsGet: t.func = ...
    projectsLocationsUrlListsDelete: t.func = ...
    projectsLocationsUrlListsList: t.func = ...
    projectsLocationsUrlListsCreate: t.func = ...
    projectsLocationsUrlListsPatch: t.func = ...
    projectsLocationsGatewaySecurityPoliciesCreate: t.func = ...
    projectsLocationsGatewaySecurityPoliciesPatch: t.func = ...
    projectsLocationsGatewaySecurityPoliciesDelete: t.func = ...
    projectsLocationsGatewaySecurityPoliciesGet: t.func = ...
    projectsLocationsGatewaySecurityPoliciesList: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesPatch: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesList: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesCreate: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesGet: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesDelete: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsClientTlsPoliciesGetIamPolicy: t.func = ...
    projectsLocationsClientTlsPoliciesCreate: t.func = ...
    projectsLocationsClientTlsPoliciesGet: t.func = ...
    projectsLocationsClientTlsPoliciesPatch: t.func = ...
    projectsLocationsClientTlsPoliciesSetIamPolicy: t.func = ...
    projectsLocationsClientTlsPoliciesList: t.func = ...
    projectsLocationsClientTlsPoliciesTestIamPermissions: t.func = ...
    projectsLocationsClientTlsPoliciesDelete: t.func = ...
    projectsLocationsServerTlsPoliciesSetIamPolicy: t.func = ...
    projectsLocationsServerTlsPoliciesCreate: t.func = ...
    projectsLocationsServerTlsPoliciesDelete: t.func = ...
    projectsLocationsServerTlsPoliciesGet: t.func = ...
    projectsLocationsServerTlsPoliciesTestIamPermissions: t.func = ...
    projectsLocationsServerTlsPoliciesList: t.func = ...
    projectsLocationsServerTlsPoliciesPatch: t.func = ...
    projectsLocationsServerTlsPoliciesGetIamPolicy: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_networksecurity() -> Import: ...
