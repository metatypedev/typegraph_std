from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ListCertificateMapsResponseIn: t.typedef = ...
    ListCertificateMapsResponseOut: t.typedef = ...
    LocationIn: t.typedef = ...
    LocationOut: t.typedef = ...
    OperationMetadataIn: t.typedef = ...
    OperationMetadataOut: t.typedef = ...
    CertificateIssuanceConfigIn: t.typedef = ...
    CertificateIssuanceConfigOut: t.typedef = ...
    ListCertificateIssuanceConfigsResponseIn: t.typedef = ...
    ListCertificateIssuanceConfigsResponseOut: t.typedef = ...
    OperationIn: t.typedef = ...
    OperationOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    CertificateMapIn: t.typedef = ...
    CertificateMapOut: t.typedef = ...
    ListOperationsResponseIn: t.typedef = ...
    ListOperationsResponseOut: t.typedef = ...
    SelfManagedCertificateIn: t.typedef = ...
    SelfManagedCertificateOut: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    CertificateAuthorityConfigIn: t.typedef = ...
    CertificateAuthorityConfigOut: t.typedef = ...
    CancelOperationRequestIn: t.typedef = ...
    CancelOperationRequestOut: t.typedef = ...
    IpConfigIn: t.typedef = ...
    IpConfigOut: t.typedef = ...
    ListLocationsResponseIn: t.typedef = ...
    ListLocationsResponseOut: t.typedef = ...
    AuthorizationAttemptInfoIn: t.typedef = ...
    AuthorizationAttemptInfoOut: t.typedef = ...
    ManagedCertificateIn: t.typedef = ...
    ManagedCertificateOut: t.typedef = ...
    ProvisioningIssueIn: t.typedef = ...
    ProvisioningIssueOut: t.typedef = ...
    CertificateAuthorityServiceConfigIn: t.typedef = ...
    CertificateAuthorityServiceConfigOut: t.typedef = ...
    TrustStoreIn: t.typedef = ...
    TrustStoreOut: t.typedef = ...
    DnsAuthorizationIn: t.typedef = ...
    DnsAuthorizationOut: t.typedef = ...
    CertificateIn: t.typedef = ...
    CertificateOut: t.typedef = ...
    DnsResourceRecordIn: t.typedef = ...
    DnsResourceRecordOut: t.typedef = ...
    TrustAnchorIn: t.typedef = ...
    TrustAnchorOut: t.typedef = ...
    ListCertificateMapEntriesResponseIn: t.typedef = ...
    ListCertificateMapEntriesResponseOut: t.typedef = ...
    ListCertificatesResponseIn: t.typedef = ...
    ListCertificatesResponseOut: t.typedef = ...
    CertificateMapEntryIn: t.typedef = ...
    CertificateMapEntryOut: t.typedef = ...
    ListTrustConfigsResponseIn: t.typedef = ...
    ListTrustConfigsResponseOut: t.typedef = ...
    TrustConfigIn: t.typedef = ...
    TrustConfigOut: t.typedef = ...
    IntermediateCAIn: t.typedef = ...
    IntermediateCAOut: t.typedef = ...
    GclbTargetIn: t.typedef = ...
    GclbTargetOut: t.typedef = ...
    ListDnsAuthorizationsResponseIn: t.typedef = ...
    ListDnsAuthorizationsResponseOut: t.typedef = ...

class FuncList:
    projectsLocationsList: t.func = ...
    projectsLocationsGet: t.func = ...
    projectsLocationsOperationsList: t.func = ...
    projectsLocationsOperationsGet: t.func = ...
    projectsLocationsOperationsDelete: t.func = ...
    projectsLocationsOperationsCancel: t.func = ...
    projectsLocationsCertificateIssuanceConfigsCreate: t.func = ...
    projectsLocationsCertificateIssuanceConfigsList: t.func = ...
    projectsLocationsCertificateIssuanceConfigsDelete: t.func = ...
    projectsLocationsCertificateIssuanceConfigsGet: t.func = ...
    projectsLocationsTrustConfigsList: t.func = ...
    projectsLocationsTrustConfigsPatch: t.func = ...
    projectsLocationsTrustConfigsDelete: t.func = ...
    projectsLocationsTrustConfigsCreate: t.func = ...
    projectsLocationsTrustConfigsGet: t.func = ...
    projectsLocationsDnsAuthorizationsDelete: t.func = ...
    projectsLocationsDnsAuthorizationsList: t.func = ...
    projectsLocationsDnsAuthorizationsCreate: t.func = ...
    projectsLocationsDnsAuthorizationsPatch: t.func = ...
    projectsLocationsDnsAuthorizationsGet: t.func = ...
    projectsLocationsCertificateMapsCreate: t.func = ...
    projectsLocationsCertificateMapsGet: t.func = ...
    projectsLocationsCertificateMapsList: t.func = ...
    projectsLocationsCertificateMapsDelete: t.func = ...
    projectsLocationsCertificateMapsPatch: t.func = ...
    projectsLocationsCertificateMapsCertificateMapEntriesGet: t.func = ...
    projectsLocationsCertificateMapsCertificateMapEntriesCreate: t.func = ...
    projectsLocationsCertificateMapsCertificateMapEntriesDelete: t.func = ...
    projectsLocationsCertificateMapsCertificateMapEntriesPatch: t.func = ...
    projectsLocationsCertificateMapsCertificateMapEntriesList: t.func = ...
    projectsLocationsCertificatesPatch: t.func = ...
    projectsLocationsCertificatesList: t.func = ...
    projectsLocationsCertificatesGet: t.func = ...
    projectsLocationsCertificatesDelete: t.func = ...
    projectsLocationsCertificatesCreate: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_certificatemanager() -> Import: ...