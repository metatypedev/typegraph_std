from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    XxeIn: t.typedef = ...
    XxeOut: t.typedef = ...
    VulnerableParametersIn: t.typedef = ...
    VulnerableParametersOut: t.typedef = ...
    OutdatedLibraryIn: t.typedef = ...
    OutdatedLibraryOut: t.typedef = ...
    CustomAccountIn: t.typedef = ...
    CustomAccountOut: t.typedef = ...
    ViolatingResourceIn: t.typedef = ...
    ViolatingResourceOut: t.typedef = ...
    ScanConfigErrorIn: t.typedef = ...
    ScanConfigErrorOut: t.typedef = ...
    CrawledUrlIn: t.typedef = ...
    CrawledUrlOut: t.typedef = ...
    ScanRunWarningTraceIn: t.typedef = ...
    ScanRunWarningTraceOut: t.typedef = ...
    StopScanRunRequestIn: t.typedef = ...
    StopScanRunRequestOut: t.typedef = ...
    HeaderIn: t.typedef = ...
    HeaderOut: t.typedef = ...
    ScanConfigIn: t.typedef = ...
    ScanConfigOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ListFindingsResponseIn: t.typedef = ...
    ListFindingsResponseOut: t.typedef = ...
    XssIn: t.typedef = ...
    XssOut: t.typedef = ...
    ScanRunErrorTraceIn: t.typedef = ...
    ScanRunErrorTraceOut: t.typedef = ...
    ListScanRunsResponseIn: t.typedef = ...
    ListScanRunsResponseOut: t.typedef = ...
    AuthenticationIn: t.typedef = ...
    AuthenticationOut: t.typedef = ...
    ListCrawledUrlsResponseIn: t.typedef = ...
    ListCrawledUrlsResponseOut: t.typedef = ...
    GoogleAccountIn: t.typedef = ...
    GoogleAccountOut: t.typedef = ...
    ScanRunIn: t.typedef = ...
    ScanRunOut: t.typedef = ...
    ListFindingTypeStatsResponseIn: t.typedef = ...
    ListFindingTypeStatsResponseOut: t.typedef = ...
    FormIn: t.typedef = ...
    FormOut: t.typedef = ...
    ScheduleIn: t.typedef = ...
    ScheduleOut: t.typedef = ...
    IapCredentialIn: t.typedef = ...
    IapCredentialOut: t.typedef = ...
    IapTestServiceAccountInfoIn: t.typedef = ...
    IapTestServiceAccountInfoOut: t.typedef = ...
    VulnerableHeadersIn: t.typedef = ...
    VulnerableHeadersOut: t.typedef = ...
    FindingIn: t.typedef = ...
    FindingOut: t.typedef = ...
    FindingTypeStatsIn: t.typedef = ...
    FindingTypeStatsOut: t.typedef = ...
    ListScanConfigsResponseIn: t.typedef = ...
    ListScanConfigsResponseOut: t.typedef = ...
    StartScanRunRequestIn: t.typedef = ...
    StartScanRunRequestOut: t.typedef = ...

class FuncList:
    projectsScanConfigsCreate: t.func = ...
    projectsScanConfigsPatch: t.func = ...
    projectsScanConfigsStart: t.func = ...
    projectsScanConfigsGet: t.func = ...
    projectsScanConfigsDelete: t.func = ...
    projectsScanConfigsList: t.func = ...
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