from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    NetworkReportSpecSortConditionIn: t.typedef = ...
    NetworkReportSpecSortConditionOut: t.typedef = ...
    DateRangeIn: t.typedef = ...
    DateRangeOut: t.typedef = ...
    ListAdUnitsResponseIn: t.typedef = ...
    ListAdUnitsResponseOut: t.typedef = ...
    ListPublisherAccountsResponseIn: t.typedef = ...
    ListPublisherAccountsResponseOut: t.typedef = ...
    LocalizationSettingsIn: t.typedef = ...
    LocalizationSettingsOut: t.typedef = ...
    ReportFooterIn: t.typedef = ...
    ReportFooterOut: t.typedef = ...
    GenerateMediationReportRequestIn: t.typedef = ...
    GenerateMediationReportRequestOut: t.typedef = ...
    GenerateNetworkReportResponseIn: t.typedef = ...
    GenerateNetworkReportResponseOut: t.typedef = ...
    ListAppsResponseIn: t.typedef = ...
    ListAppsResponseOut: t.typedef = ...
    AppLinkedAppInfoIn: t.typedef = ...
    AppLinkedAppInfoOut: t.typedef = ...
    PublisherAccountIn: t.typedef = ...
    PublisherAccountOut: t.typedef = ...
    MediationReportSpecSortConditionIn: t.typedef = ...
    MediationReportSpecSortConditionOut: t.typedef = ...
    GenerateMediationReportResponseIn: t.typedef = ...
    GenerateMediationReportResponseOut: t.typedef = ...
    ReportHeaderIn: t.typedef = ...
    ReportHeaderOut: t.typedef = ...
    AppIn: t.typedef = ...
    AppOut: t.typedef = ...
    StringListIn: t.typedef = ...
    StringListOut: t.typedef = ...
    AppManualAppInfoIn: t.typedef = ...
    AppManualAppInfoOut: t.typedef = ...
    GenerateNetworkReportRequestIn: t.typedef = ...
    GenerateNetworkReportRequestOut: t.typedef = ...
    DateIn: t.typedef = ...
    DateOut: t.typedef = ...
    AdUnitIn: t.typedef = ...
    AdUnitOut: t.typedef = ...
    ReportWarningIn: t.typedef = ...
    ReportWarningOut: t.typedef = ...
    ReportRowMetricValueIn: t.typedef = ...
    ReportRowMetricValueOut: t.typedef = ...
    ReportRowIn: t.typedef = ...
    ReportRowOut: t.typedef = ...
    ReportRowDimensionValueIn: t.typedef = ...
    ReportRowDimensionValueOut: t.typedef = ...
    NetworkReportSpecIn: t.typedef = ...
    NetworkReportSpecOut: t.typedef = ...
    MediationReportSpecIn: t.typedef = ...
    MediationReportSpecOut: t.typedef = ...
    NetworkReportSpecDimensionFilterIn: t.typedef = ...
    NetworkReportSpecDimensionFilterOut: t.typedef = ...
    MediationReportSpecDimensionFilterIn: t.typedef = ...
    MediationReportSpecDimensionFilterOut: t.typedef = ...

class FuncList:
    accountsGet: t.func = ...
    accountsList: t.func = ...
    accountsAdUnitsList: t.func = ...
    accountsMediationReportGenerate: t.func = ...
    accountsNetworkReportGenerate: t.func = ...
    accountsAppsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_admob() -> Import: ...