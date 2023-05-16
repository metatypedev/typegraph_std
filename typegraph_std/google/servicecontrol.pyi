from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    StatusIn: t.typedef = ...
    StatusOut: t.typedef = ...
    PeerIn: t.typedef = ...
    PeerOut: t.typedef = ...
    AuthIn: t.typedef = ...
    AuthOut: t.typedef = ...
    AttributeContextIn: t.typedef = ...
    AttributeContextOut: t.typedef = ...
    ServiceAccountDelegationInfoIn: t.typedef = ...
    ServiceAccountDelegationInfoOut: t.typedef = ...
    ReportResponseIn: t.typedef = ...
    ReportResponseOut: t.typedef = ...
    AuthorizationInfoIn: t.typedef = ...
    AuthorizationInfoOut: t.typedef = ...
    ThirdPartyPrincipalIn: t.typedef = ...
    ThirdPartyPrincipalOut: t.typedef = ...
    ResourceIn: t.typedef = ...
    ResourceOut: t.typedef = ...
    ResourceLocationIn: t.typedef = ...
    ResourceLocationOut: t.typedef = ...
    V2LogEntrySourceLocationIn: t.typedef = ...
    V2LogEntrySourceLocationOut: t.typedef = ...
    FirstPartyPrincipalIn: t.typedef = ...
    FirstPartyPrincipalOut: t.typedef = ...
    RequestIn: t.typedef = ...
    RequestOut: t.typedef = ...
    CheckResponseIn: t.typedef = ...
    CheckResponseOut: t.typedef = ...
    ReportRequestIn: t.typedef = ...
    ReportRequestOut: t.typedef = ...
    AuthenticationInfoIn: t.typedef = ...
    AuthenticationInfoOut: t.typedef = ...
    ResponseIn: t.typedef = ...
    ResponseOut: t.typedef = ...
    V2LogEntryOperationIn: t.typedef = ...
    V2LogEntryOperationOut: t.typedef = ...
    RequestMetadataIn: t.typedef = ...
    RequestMetadataOut: t.typedef = ...
    CheckRequestIn: t.typedef = ...
    CheckRequestOut: t.typedef = ...
    OrgPolicyViolationInfoIn: t.typedef = ...
    OrgPolicyViolationInfoOut: t.typedef = ...
    V2HttpRequestIn: t.typedef = ...
    V2HttpRequestOut: t.typedef = ...
    ResourceInfoIn: t.typedef = ...
    ResourceInfoOut: t.typedef = ...
    ApiIn: t.typedef = ...
    ApiOut: t.typedef = ...
    SpanContextIn: t.typedef = ...
    SpanContextOut: t.typedef = ...
    ViolationInfoIn: t.typedef = ...
    ViolationInfoOut: t.typedef = ...
    AuditLogIn: t.typedef = ...
    AuditLogOut: t.typedef = ...
    PolicyViolationInfoIn: t.typedef = ...
    PolicyViolationInfoOut: t.typedef = ...
    V2LogEntryIn: t.typedef = ...
    V2LogEntryOut: t.typedef = ...

class FuncList:
    servicesReport: t.func = ...
    servicesCheck: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_servicecontrol() -> Import: ...
