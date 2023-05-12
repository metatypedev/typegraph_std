from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    DestinationIn: t.typedef = ...
    DestinationOut: t.typedef = ...
    UrlListIn: t.typedef = ...
    UrlListOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    GoogleCloudNetworksecurityV1CertificateProviderIn: t.typedef = ...
    GoogleCloudNetworksecurityV1CertificateProviderOut: t.typedef = ...
    GoogleIamV1TestIamPermissionsRequestIn: t.typedef = ...
    GoogleIamV1TestIamPermissionsRequestOut: t.typedef = ...
    GoogleCloudNetworksecurityV1GrpcEndpointIn: t.typedef = ...
    GoogleCloudNetworksecurityV1GrpcEndpointOut: t.typedef = ...
    ListClientTlsPoliciesResponseIn: t.typedef = ...
    ListClientTlsPoliciesResponseOut: t.typedef = ...
    GoogleIamV1SetIamPolicyRequestIn: t.typedef = ...
    GoogleIamV1SetIamPolicyRequestOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    TlsInspectionPolicyIn: t.typedef = ...
    TlsInspectionPolicyOut: t.typedef = ...
    ClientTlsPolicyIn: t.typedef = ...
    ClientTlsPolicyOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    ListTlsInspectionPoliciesResponseIn: t.typedef = ...
    ListTlsInspectionPoliciesResponseOut: t.typedef = ...
    MTLSPolicyIn: t.typedef = ...
    MTLSPolicyOut: t.typedef = ...
    ListUrlListsResponseIn: t.typedef = ...
    ListUrlListsResponseOut: t.typedef = ...
    HttpHeaderMatchIn: t.typedef = ...
    HttpHeaderMatchOut: t.typedef = ...
    GoogleIamV1TestIamPermissionsResponseIn: t.typedef = ...
    GoogleIamV1TestIamPermissionsResponseOut: t.typedef = ...
    ServerTlsPolicyIn: t.typedef = ...
    ServerTlsPolicyOut: t.typedef = ...
    GoogleIamV1BindingIn: t.typedef = ...
    GoogleIamV1BindingOut: t.typedef = ...
    GoogleIamV1AuditLogConfigIn: t.typedef = ...
    GoogleIamV1AuditLogConfigOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    GatewaySecurityPolicyRuleIn: t.typedef = ...
    GatewaySecurityPolicyRuleOut: t.typedef = ...
    GatewaySecurityPolicyIn: t.typedef = ...
    GatewaySecurityPolicyOut: t.typedef = ...
    ListGatewaySecurityPolicyRulesResponseIn: t.typedef = ...
    ListGatewaySecurityPolicyRulesResponseOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    ListServerTlsPoliciesResponseIn: t.typedef = ...
    ListServerTlsPoliciesResponseOut: t.typedef = ...
    ValidationCAIn: t.typedef = ...
    ValidationCAOut: t.typedef = ...
    ListAuthorizationPoliciesResponseIn: t.typedef = ...
    ListAuthorizationPoliciesResponseOut: t.typedef = ...
    ListGatewaySecurityPoliciesResponseIn: t.typedef = ...
    ListGatewaySecurityPoliciesResponseOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    GoogleIamV1AuditConfigIn: t.typedef = ...
    GoogleIamV1AuditConfigOut: t.typedef = ...
    AuthorizationPolicyIn: t.typedef = ...
    AuthorizationPolicyOut: t.typedef = ...
    CertificateProviderInstanceIn: t.typedef = ...
    CertificateProviderInstanceOut: t.typedef = ...
    GoogleIamV1PolicyIn: t.typedef = ...
    GoogleIamV1PolicyOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    SourceIn: t.typedef = ...
    SourceOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    RuleIn: t.typedef = ...
    RuleOut: t.typedef = ...

class FuncList:
    projectsLocationsGet: t.func = ...
    projectsLocationsList: t.func = ...
    projectsLocationsUrlListsCreate: t.func = ...
    projectsLocationsUrlListsList: t.func = ...
    projectsLocationsUrlListsDelete: t.func = ...
    projectsLocationsUrlListsGet: t.func = ...
    projectsLocationsUrlListsPatch: t.func = ...
    projectsLocationsServerTlsPoliciesGet: t.func = ...
    projectsLocationsServerTlsPoliciesCreate: t.func = ...
    projectsLocationsServerTlsPoliciesTestIamPermissions: t.func = ...
    projectsLocationsServerTlsPoliciesGetIamPolicy: t.func = ...
    projectsLocationsServerTlsPoliciesList: t.func = ...
    projectsLocationsServerTlsPoliciesDelete: t.func = ...
    projectsLocationsServerTlsPoliciesSetIamPolicy: t.func = ...
    projectsLocationsServerTlsPoliciesPatch: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsAuthorizationPoliciesGet: t.func = ...
    projectsLocationsAuthorizationPoliciesCreate: t.func = ...
    projectsLocationsAuthorizationPoliciesDelete: t.func = ...
    projectsLocationsAuthorizationPoliciesList: t.func = ...
    projectsLocationsAuthorizationPoliciesGetIamPolicy: t.func = ...
    projectsLocationsAuthorizationPoliciesSetIamPolicy: t.func = ...
    projectsLocationsAuthorizationPoliciesTestIamPermissions: t.func = ...
    projectsLocationsAuthorizationPoliciesPatch: t.func = ...
    projectsLocationsTlsInspectionPoliciesGet: t.func = ...
    projectsLocationsTlsInspectionPoliciesDelete: t.func = ...
    projectsLocationsTlsInspectionPoliciesList: t.func = ...
    projectsLocationsTlsInspectionPoliciesCreate: t.func = ...
    projectsLocationsTlsInspectionPoliciesPatch: t.func = ...
    projectsLocationsClientTlsPoliciesTestIamPermissions: t.func = ...
    projectsLocationsClientTlsPoliciesGet: t.func = ...
    projectsLocationsClientTlsPoliciesGetIamPolicy: t.func = ...
    projectsLocationsClientTlsPoliciesList: t.func = ...
    projectsLocationsClientTlsPoliciesSetIamPolicy: t.func = ...
    projectsLocationsClientTlsPoliciesCreate: t.func = ...
    projectsLocationsClientTlsPoliciesPatch: t.func = ...
    projectsLocationsClientTlsPoliciesDelete: t.func = ...
    projectsLocationsGatewaySecurityPoliciesDelete: t.func = ...
    projectsLocationsGatewaySecurityPoliciesList: t.func = ...
    projectsLocationsGatewaySecurityPoliciesPatch: t.func = ...
    projectsLocationsGatewaySecurityPoliciesGet: t.func = ...
    projectsLocationsGatewaySecurityPoliciesCreate: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesList: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesDelete: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesGet: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesPatch: t.func = ...
    projectsLocationsGatewaySecurityPoliciesRulesCreate: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_networksecurity() -> Import: ...
