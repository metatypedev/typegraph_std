from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    MoneyIn: t.typedef = ...
    MoneyOut: t.typedef = ...
    SkuIn: t.typedef = ...
    SkuOut: t.typedef = ...
    ListSkusResponseIn: t.typedef = ...
    ListSkusResponseOut: t.typedef = ...
    AuditLogConfigIn: t.typedef = ...
    AuditLogConfigOut: t.typedef = ...
    ServiceIn: t.typedef = ...
    ServiceOut: t.typedef = ...
    PricingInfoIn: t.typedef = ...
    PricingInfoOut: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    PricingExpressionIn: t.typedef = ...
    PricingExpressionOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    ListServicesResponseIn: t.typedef = ...
    ListServicesResponseOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    ListBillingAccountsResponseIn: t.typedef = ...
    ListBillingAccountsResponseOut: t.typedef = ...
    GeoTaxonomyIn: t.typedef = ...
    GeoTaxonomyOut: t.typedef = ...
    TierRateIn: t.typedef = ...
    TierRateOut: t.typedef = ...
    AggregationInfoIn: t.typedef = ...
    AggregationInfoOut: t.typedef = ...
    CategoryIn: t.typedef = ...
    CategoryOut: t.typedef = ...
    AuditConfigIn: t.typedef = ...
    AuditConfigOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    BillingAccountIn: t.typedef = ...
    BillingAccountOut: t.typedef = ...
    ListProjectBillingInfoResponseIn: t.typedef = ...
    ListProjectBillingInfoResponseOut: t.typedef = ...
    ProjectBillingInfoIn: t.typedef = ...
    ProjectBillingInfoOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...

class FuncList:
    billingAccountsSetIamPolicy: t.func = ...
    billingAccountsGet: t.func = ...
    billingAccountsPatch: t.func = ...
    billingAccountsGetIamPolicy: t.func = ...
    billingAccountsList: t.func = ...
    billingAccountsTestIamPermissions: t.func = ...
    billingAccountsCreate: t.func = ...
    billingAccountsProjectsList: t.func = ...
    servicesList: t.func = ...
    servicesSkusList: t.func = ...
    projectsUpdateBillingInfo: t.func = ...
    projectsGetBillingInfo: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_cloudbilling() -> Import: ...
