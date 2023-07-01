from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    MediationReportSpecIn: t.typedef = ...
    MediationReportSpecOut: t.typedef = ...
    GenerateMediationReportResponseIn: t.typedef = ...
    GenerateMediationReportResponseOut: t.typedef = ...
    GenerateMediationReportRequestIn: t.typedef = ...
    GenerateMediationReportRequestOut: t.typedef = ...
    DateRangeIn: t.typedef = ...
    DateRangeOut: t.typedef = ...
    StringListIn: t.typedef = ...
    StringListOut: t.typedef = ...
    ListAdUnitsResponseIn: t.typedef = ...
    ListAdUnitsResponseOut: t.typedef = ...
    LocalizationSettingsIn: t.typedef = ...
    LocalizationSettingsOut: t.typedef = ...
    DateIn: t.typedef = ...
    DateOut: t.typedef = ...
    MediationReportSpecDimensionFilterIn: t.typedef = ...
    MediationReportSpecDimensionFilterOut: t.typedef = ...
    MediationReportSpecSortConditionIn: t.typedef = ...
    MediationReportSpecSortConditionOut: t.typedef = ...
    AppIn: t.typedef = ...
    AppOut: t.typedef = ...
    ReportRowMetricValueIn: t.typedef = ...
    ReportRowMetricValueOut: t.typedef = ...
    NetworkReportSpecIn: t.typedef = ...
    NetworkReportSpecOut: t.typedef = ...
    AppManualAppInfoIn: t.typedef = ...
    AppManualAppInfoOut: t.typedef = ...
    ListPublisherAccountsResponseIn: t.typedef = ...
    ListPublisherAccountsResponseOut: t.typedef = ...
    ReportWarningIn: t.typedef = ...
    ReportWarningOut: t.typedef = ...
    GenerateNetworkReportRequestIn: t.typedef = ...
    GenerateNetworkReportRequestOut: t.typedef = ...
    PublisherAccountIn: t.typedef = ...
    PublisherAccountOut: t.typedef = ...
    NetworkReportSpecSortConditionIn: t.typedef = ...
    NetworkReportSpecSortConditionOut: t.typedef = ...
    GenerateNetworkReportResponseIn: t.typedef = ...
    GenerateNetworkReportResponseOut: t.typedef = ...
    ReportFooterIn: t.typedef = ...
    ReportFooterOut: t.typedef = ...
    NetworkReportSpecDimensionFilterIn: t.typedef = ...
    NetworkReportSpecDimensionFilterOut: t.typedef = ...
    ReportHeaderIn: t.typedef = ...
    ReportHeaderOut: t.typedef = ...
    AdUnitIn: t.typedef = ...
    AdUnitOut: t.typedef = ...
    AppLinkedAppInfoIn: t.typedef = ...
    AppLinkedAppInfoOut: t.typedef = ...
    ReportRowIn: t.typedef = ...
    ReportRowOut: t.typedef = ...
    ReportRowDimensionValueIn: t.typedef = ...
    ReportRowDimensionValueOut: t.typedef = ...
    ListAppsResponseIn: t.typedef = ...
    ListAppsResponseOut: t.typedef = ...

class FuncList:
    accountsGet: t.func = ...
    accountsList: t.func = ...
    accountsMediationReportGenerate: t.func = ...
    accountsAdUnitsList: t.func = ...
    accountsNetworkReportGenerate: t.func = ...
    accountsAppsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_admob() -> Import: ...
