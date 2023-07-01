from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    FindingIn: t.typedef = ...
    FindingOut: t.typedef = ...
    ListScanRunsResponseIn: t.typedef = ...
    ListScanRunsResponseOut: t.typedef = ...
    ScanConfigErrorIn: t.typedef = ...
    ScanConfigErrorOut: t.typedef = ...
    XxeIn: t.typedef = ...
    XxeOut: t.typedef = ...
    IapCredentialIn: t.typedef = ...
    IapCredentialOut: t.typedef = ...
    ScanRunIn: t.typedef = ...
    ScanRunOut: t.typedef = ...
    CrawledUrlIn: t.typedef = ...
    CrawledUrlOut: t.typedef = ...
    FindingTypeStatsIn: t.typedef = ...
    FindingTypeStatsOut: t.typedef = ...
    ScanRunErrorTraceIn: t.typedef = ...
    ScanRunErrorTraceOut: t.typedef = ...
    HeaderIn: t.typedef = ...
    HeaderOut: t.typedef = ...
    FormIn: t.typedef = ...
    FormOut: t.typedef = ...
    IapTestServiceAccountInfoIn: t.typedef = ...
    IapTestServiceAccountInfoOut: t.typedef = ...
    ListCrawledUrlsResponseIn: t.typedef = ...
    ListCrawledUrlsResponseOut: t.typedef = ...
    VulnerableParametersIn: t.typedef = ...
    VulnerableParametersOut: t.typedef = ...
    OutdatedLibraryIn: t.typedef = ...
    OutdatedLibraryOut: t.typedef = ...
    ListScanConfigsResponseIn: t.typedef = ...
    ListScanConfigsResponseOut: t.typedef = ...
    GoogleAccountIn: t.typedef = ...
    GoogleAccountOut: t.typedef = ...
    VulnerableHeadersIn: t.typedef = ...
    VulnerableHeadersOut: t.typedef = ...
    ListFindingTypeStatsResponseIn: t.typedef = ...
    ListFindingTypeStatsResponseOut: t.typedef = ...
    ViolatingResourceIn: t.typedef = ...
    ViolatingResourceOut: t.typedef = ...
    ListFindingsResponseIn: t.typedef = ...
    ListFindingsResponseOut: t.typedef = ...
    AuthenticationIn: t.typedef = ...
    AuthenticationOut: t.typedef = ...
    CustomAccountIn: t.typedef = ...
    CustomAccountOut: t.typedef = ...
    ScanConfigIn: t.typedef = ...
    ScanConfigOut: t.typedef = ...
    XssIn: t.typedef = ...
    XssOut: t.typedef = ...
    StartScanRunRequestIn: t.typedef = ...
    StartScanRunRequestOut: t.typedef = ...
    ScheduleIn: t.typedef = ...
    ScheduleOut: t.typedef = ...
    ScanRunWarningTraceIn: t.typedef = ...
    ScanRunWarningTraceOut: t.typedef = ...
    StopScanRunRequestIn: t.typedef = ...
    StopScanRunRequestOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...

class FuncList:
    projectsScanConfigsList: t.func = ...
    projectsScanConfigsCreate: t.func = ...
    projectsScanConfigsGet: t.func = ...
    projectsScanConfigsPatch: t.func = ...
    projectsScanConfigsStart: t.func = ...
    projectsScanConfigsDelete: t.func = ...
    projectsScanConfigsScanRunsGet: t.func = ...
    projectsScanConfigsScanRunsStop: t.func = ...
    projectsScanConfigsScanRunsList: t.func = ...
    projectsScanConfigsScanRunsCrawledUrlsList: t.func = ...
    projectsScanConfigsScanRunsFindingsList: t.func = ...
    projectsScanConfigsScanRunsFindingsGet: t.func = ...
    projectsScanConfigsScanRunsFindingTypeStatsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_websecurityscanner() -> Import: ...
