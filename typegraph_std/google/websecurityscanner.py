from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_websecurityscanner() -> Import:
    websecurityscanner = HTTPRuntime("https://websecurityscanner.googleapis.com/")

    renames = {
        "ErrorResponse": "_websecurityscanner_1_ErrorResponse",
        "ScanRunErrorTraceIn": "_websecurityscanner_2_ScanRunErrorTraceIn",
        "ScanRunErrorTraceOut": "_websecurityscanner_3_ScanRunErrorTraceOut",
        "ScanConfigIn": "_websecurityscanner_4_ScanConfigIn",
        "ScanConfigOut": "_websecurityscanner_5_ScanConfigOut",
        "ListScanRunsResponseIn": "_websecurityscanner_6_ListScanRunsResponseIn",
        "ListScanRunsResponseOut": "_websecurityscanner_7_ListScanRunsResponseOut",
        "ListFindingTypeStatsResponseIn": "_websecurityscanner_8_ListFindingTypeStatsResponseIn",
        "ListFindingTypeStatsResponseOut": "_websecurityscanner_9_ListFindingTypeStatsResponseOut",
        "CrawledUrlIn": "_websecurityscanner_10_CrawledUrlIn",
        "CrawledUrlOut": "_websecurityscanner_11_CrawledUrlOut",
        "HeaderIn": "_websecurityscanner_12_HeaderIn",
        "HeaderOut": "_websecurityscanner_13_HeaderOut",
        "XssIn": "_websecurityscanner_14_XssIn",
        "XssOut": "_websecurityscanner_15_XssOut",
        "FormIn": "_websecurityscanner_16_FormIn",
        "FormOut": "_websecurityscanner_17_FormOut",
        "FindingTypeStatsIn": "_websecurityscanner_18_FindingTypeStatsIn",
        "FindingTypeStatsOut": "_websecurityscanner_19_FindingTypeStatsOut",
        "ListCrawledUrlsResponseIn": "_websecurityscanner_20_ListCrawledUrlsResponseIn",
        "ListCrawledUrlsResponseOut": "_websecurityscanner_21_ListCrawledUrlsResponseOut",
        "ViolatingResourceIn": "_websecurityscanner_22_ViolatingResourceIn",
        "ViolatingResourceOut": "_websecurityscanner_23_ViolatingResourceOut",
        "GoogleAccountIn": "_websecurityscanner_24_GoogleAccountIn",
        "GoogleAccountOut": "_websecurityscanner_25_GoogleAccountOut",
        "VulnerableHeadersIn": "_websecurityscanner_26_VulnerableHeadersIn",
        "VulnerableHeadersOut": "_websecurityscanner_27_VulnerableHeadersOut",
        "FindingIn": "_websecurityscanner_28_FindingIn",
        "FindingOut": "_websecurityscanner_29_FindingOut",
        "IapCredentialIn": "_websecurityscanner_30_IapCredentialIn",
        "IapCredentialOut": "_websecurityscanner_31_IapCredentialOut",
        "CustomAccountIn": "_websecurityscanner_32_CustomAccountIn",
        "CustomAccountOut": "_websecurityscanner_33_CustomAccountOut",
        "ScanConfigErrorIn": "_websecurityscanner_34_ScanConfigErrorIn",
        "ScanConfigErrorOut": "_websecurityscanner_35_ScanConfigErrorOut",
        "AuthenticationIn": "_websecurityscanner_36_AuthenticationIn",
        "AuthenticationOut": "_websecurityscanner_37_AuthenticationOut",
        "XxeIn": "_websecurityscanner_38_XxeIn",
        "XxeOut": "_websecurityscanner_39_XxeOut",
        "EmptyIn": "_websecurityscanner_40_EmptyIn",
        "EmptyOut": "_websecurityscanner_41_EmptyOut",
        "ListFindingsResponseIn": "_websecurityscanner_42_ListFindingsResponseIn",
        "ListFindingsResponseOut": "_websecurityscanner_43_ListFindingsResponseOut",
        "StartScanRunRequestIn": "_websecurityscanner_44_StartScanRunRequestIn",
        "StartScanRunRequestOut": "_websecurityscanner_45_StartScanRunRequestOut",
        "ScanRunWarningTraceIn": "_websecurityscanner_46_ScanRunWarningTraceIn",
        "ScanRunWarningTraceOut": "_websecurityscanner_47_ScanRunWarningTraceOut",
        "ListScanConfigsResponseIn": "_websecurityscanner_48_ListScanConfigsResponseIn",
        "ListScanConfigsResponseOut": "_websecurityscanner_49_ListScanConfigsResponseOut",
        "ScheduleIn": "_websecurityscanner_50_ScheduleIn",
        "ScheduleOut": "_websecurityscanner_51_ScheduleOut",
        "StopScanRunRequestIn": "_websecurityscanner_52_StopScanRunRequestIn",
        "StopScanRunRequestOut": "_websecurityscanner_53_StopScanRunRequestOut",
        "VulnerableParametersIn": "_websecurityscanner_54_VulnerableParametersIn",
        "VulnerableParametersOut": "_websecurityscanner_55_VulnerableParametersOut",
        "OutdatedLibraryIn": "_websecurityscanner_56_OutdatedLibraryIn",
        "OutdatedLibraryOut": "_websecurityscanner_57_OutdatedLibraryOut",
        "IapTestServiceAccountInfoIn": "_websecurityscanner_58_IapTestServiceAccountInfoIn",
        "IapTestServiceAccountInfoOut": "_websecurityscanner_59_IapTestServiceAccountInfoOut",
        "ScanRunIn": "_websecurityscanner_60_ScanRunIn",
        "ScanRunOut": "_websecurityscanner_61_ScanRunOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ScanRunErrorTraceIn"] = t.struct(
        {
            "scanConfigError": t.proxy(renames["ScanConfigErrorIn"]).optional(),
            "code": t.string().optional(),
            "mostCommonHttpErrorCode": t.integer().optional(),
        }
    ).named(renames["ScanRunErrorTraceIn"])
    types["ScanRunErrorTraceOut"] = t.struct(
        {
            "scanConfigError": t.proxy(renames["ScanConfigErrorOut"]).optional(),
            "code": t.string().optional(),
            "mostCommonHttpErrorCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunErrorTraceOut"])
    types["ScanConfigIn"] = t.struct(
        {
            "displayName": t.string(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "exportToSecurityCommandCenter": t.string().optional(),
            "maxQps": t.integer().optional(),
            "schedule": t.proxy(renames["ScheduleIn"]).optional(),
            "name": t.string().optional(),
            "startingUrls": t.array(t.string()),
            "userAgent": t.string().optional(),
            "staticIpScan": t.boolean().optional(),
            "riskLevel": t.string().optional(),
            "ignoreHttpStatusErrors": t.boolean().optional(),
            "managedScan": t.boolean().optional(),
            "blacklistPatterns": t.array(t.string()).optional(),
        }
    ).named(renames["ScanConfigIn"])
    types["ScanConfigOut"] = t.struct(
        {
            "displayName": t.string(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "exportToSecurityCommandCenter": t.string().optional(),
            "maxQps": t.integer().optional(),
            "schedule": t.proxy(renames["ScheduleOut"]).optional(),
            "name": t.string().optional(),
            "startingUrls": t.array(t.string()),
            "userAgent": t.string().optional(),
            "staticIpScan": t.boolean().optional(),
            "riskLevel": t.string().optional(),
            "ignoreHttpStatusErrors": t.boolean().optional(),
            "managedScan": t.boolean().optional(),
            "blacklistPatterns": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanConfigOut"])
    types["ListScanRunsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scanRuns": t.array(t.proxy(renames["ScanRunIn"])).optional(),
        }
    ).named(renames["ListScanRunsResponseIn"])
    types["ListScanRunsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scanRuns": t.array(t.proxy(renames["ScanRunOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScanRunsResponseOut"])
    types["ListFindingTypeStatsResponseIn"] = t.struct(
        {"findingTypeStats": t.array(t.proxy(renames["FindingTypeStatsIn"])).optional()}
    ).named(renames["ListFindingTypeStatsResponseIn"])
    types["ListFindingTypeStatsResponseOut"] = t.struct(
        {
            "findingTypeStats": t.array(
                t.proxy(renames["FindingTypeStatsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFindingTypeStatsResponseOut"])
    types["CrawledUrlIn"] = t.struct(
        {
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["CrawledUrlIn"])
    types["CrawledUrlOut"] = t.struct(
        {
            "body": t.string().optional(),
            "httpMethod": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrawledUrlOut"])
    types["HeaderIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["HeaderIn"])
    types["HeaderOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeaderOut"])
    types["XssIn"] = t.struct(
        {
            "storedXssSeedingUrl": t.string().optional(),
            "attackVector": t.string().optional(),
            "errorMessage": t.string().optional(),
            "stackTraces": t.array(t.string()).optional(),
        }
    ).named(renames["XssIn"])
    types["XssOut"] = t.struct(
        {
            "storedXssSeedingUrl": t.string().optional(),
            "attackVector": t.string().optional(),
            "errorMessage": t.string().optional(),
            "stackTraces": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["XssOut"])
    types["FormIn"] = t.struct(
        {"fields": t.array(t.string()).optional(), "actionUri": t.string().optional()}
    ).named(renames["FormIn"])
    types["FormOut"] = t.struct(
        {
            "fields": t.array(t.string()).optional(),
            "actionUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormOut"])
    types["FindingTypeStatsIn"] = t.struct(
        {"findingType": t.string().optional(), "findingCount": t.integer().optional()}
    ).named(renames["FindingTypeStatsIn"])
    types["FindingTypeStatsOut"] = t.struct(
        {
            "findingType": t.string().optional(),
            "findingCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingTypeStatsOut"])
    types["ListCrawledUrlsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "crawledUrls": t.array(t.proxy(renames["CrawledUrlIn"])).optional(),
        }
    ).named(renames["ListCrawledUrlsResponseIn"])
    types["ListCrawledUrlsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "crawledUrls": t.array(t.proxy(renames["CrawledUrlOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCrawledUrlsResponseOut"])
    types["ViolatingResourceIn"] = t.struct(
        {"resourceUrl": t.string().optional(), "contentType": t.string().optional()}
    ).named(renames["ViolatingResourceIn"])
    types["ViolatingResourceOut"] = t.struct(
        {
            "resourceUrl": t.string().optional(),
            "contentType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolatingResourceOut"])
    types["GoogleAccountIn"] = t.struct(
        {"username": t.string(), "password": t.string()}
    ).named(renames["GoogleAccountIn"])
    types["GoogleAccountOut"] = t.struct(
        {
            "username": t.string(),
            "password": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAccountOut"])
    types["VulnerableHeadersIn"] = t.struct(
        {
            "missingHeaders": t.array(t.proxy(renames["HeaderIn"])).optional(),
            "headers": t.array(t.proxy(renames["HeaderIn"])).optional(),
        }
    ).named(renames["VulnerableHeadersIn"])
    types["VulnerableHeadersOut"] = t.struct(
        {
            "missingHeaders": t.array(t.proxy(renames["HeaderOut"])).optional(),
            "headers": t.array(t.proxy(renames["HeaderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerableHeadersOut"])
    types["FindingIn"] = t.struct(
        {
            "fuzzedUrl": t.string().optional(),
            "findingType": t.string().optional(),
            "xss": t.proxy(renames["XssIn"]).optional(),
            "reproductionUrl": t.string().optional(),
            "violatingResource": t.proxy(renames["ViolatingResourceIn"]).optional(),
            "frameUrl": t.string().optional(),
            "trackingId": t.string().optional(),
            "vulnerableHeaders": t.proxy(renames["VulnerableHeadersIn"]).optional(),
            "description": t.string().optional(),
            "body": t.string().optional(),
            "finalUrl": t.string().optional(),
            "name": t.string().optional(),
            "httpMethod": t.string().optional(),
            "vulnerableParameters": t.proxy(
                renames["VulnerableParametersIn"]
            ).optional(),
            "outdatedLibrary": t.proxy(renames["OutdatedLibraryIn"]).optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
        }
    ).named(renames["FindingIn"])
    types["FindingOut"] = t.struct(
        {
            "fuzzedUrl": t.string().optional(),
            "findingType": t.string().optional(),
            "xxe": t.proxy(renames["XxeOut"]).optional(),
            "xss": t.proxy(renames["XssOut"]).optional(),
            "reproductionUrl": t.string().optional(),
            "violatingResource": t.proxy(renames["ViolatingResourceOut"]).optional(),
            "frameUrl": t.string().optional(),
            "trackingId": t.string().optional(),
            "severity": t.string().optional(),
            "vulnerableHeaders": t.proxy(renames["VulnerableHeadersOut"]).optional(),
            "description": t.string().optional(),
            "body": t.string().optional(),
            "finalUrl": t.string().optional(),
            "name": t.string().optional(),
            "httpMethod": t.string().optional(),
            "vulnerableParameters": t.proxy(
                renames["VulnerableParametersOut"]
            ).optional(),
            "outdatedLibrary": t.proxy(renames["OutdatedLibraryOut"]).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingOut"])
    types["IapCredentialIn"] = t.struct(
        {
            "iapTestServiceAccountInfo": t.proxy(
                renames["IapTestServiceAccountInfoIn"]
            ).optional()
        }
    ).named(renames["IapCredentialIn"])
    types["IapCredentialOut"] = t.struct(
        {
            "iapTestServiceAccountInfo": t.proxy(
                renames["IapTestServiceAccountInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IapCredentialOut"])
    types["CustomAccountIn"] = t.struct(
        {"loginUrl": t.string(), "password": t.string(), "username": t.string()}
    ).named(renames["CustomAccountIn"])
    types["CustomAccountOut"] = t.struct(
        {
            "loginUrl": t.string(),
            "password": t.string(),
            "username": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAccountOut"])
    types["ScanConfigErrorIn"] = t.struct(
        {"code": t.string().optional(), "fieldName": t.string().optional()}
    ).named(renames["ScanConfigErrorIn"])
    types["ScanConfigErrorOut"] = t.struct(
        {
            "code": t.string().optional(),
            "fieldName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanConfigErrorOut"])
    types["AuthenticationIn"] = t.struct(
        {
            "iapCredential": t.proxy(renames["IapCredentialIn"]).optional(),
            "customAccount": t.proxy(renames["CustomAccountIn"]).optional(),
            "googleAccount": t.proxy(renames["GoogleAccountIn"]).optional(),
        }
    ).named(renames["AuthenticationIn"])
    types["AuthenticationOut"] = t.struct(
        {
            "iapCredential": t.proxy(renames["IapCredentialOut"]).optional(),
            "customAccount": t.proxy(renames["CustomAccountOut"]).optional(),
            "googleAccount": t.proxy(renames["GoogleAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationOut"])
    types["XxeIn"] = t.struct(
        {
            "payloadLocation": t.string().optional(),
            "payloadValue": t.string().optional(),
        }
    ).named(renames["XxeIn"])
    types["XxeOut"] = t.struct(
        {
            "payloadLocation": t.string().optional(),
            "payloadValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["XxeOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListFindingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "findings": t.array(t.proxy(renames["FindingIn"])).optional(),
        }
    ).named(renames["ListFindingsResponseIn"])
    types["ListFindingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "findings": t.array(t.proxy(renames["FindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFindingsResponseOut"])
    types["StartScanRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartScanRunRequestIn"]
    )
    types["StartScanRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartScanRunRequestOut"])
    types["ScanRunWarningTraceIn"] = t.struct({"code": t.string().optional()}).named(
        renames["ScanRunWarningTraceIn"]
    )
    types["ScanRunWarningTraceOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunWarningTraceOut"])
    types["ListScanConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scanConfigs": t.array(t.proxy(renames["ScanConfigIn"])).optional(),
        }
    ).named(renames["ListScanConfigsResponseIn"])
    types["ListScanConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "scanConfigs": t.array(t.proxy(renames["ScanConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScanConfigsResponseOut"])
    types["ScheduleIn"] = t.struct(
        {"scheduleTime": t.string().optional(), "intervalDurationDays": t.integer()}
    ).named(renames["ScheduleIn"])
    types["ScheduleOut"] = t.struct(
        {
            "scheduleTime": t.string().optional(),
            "intervalDurationDays": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScheduleOut"])
    types["StopScanRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopScanRunRequestIn"]
    )
    types["StopScanRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopScanRunRequestOut"])
    types["VulnerableParametersIn"] = t.struct(
        {"parameterNames": t.array(t.string()).optional()}
    ).named(renames["VulnerableParametersIn"])
    types["VulnerableParametersOut"] = t.struct(
        {
            "parameterNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerableParametersOut"])
    types["OutdatedLibraryIn"] = t.struct(
        {
            "version": t.string().optional(),
            "learnMoreUrls": t.array(t.string()).optional(),
            "libraryName": t.string().optional(),
        }
    ).named(renames["OutdatedLibraryIn"])
    types["OutdatedLibraryOut"] = t.struct(
        {
            "version": t.string().optional(),
            "learnMoreUrls": t.array(t.string()).optional(),
            "libraryName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutdatedLibraryOut"])
    types["IapTestServiceAccountInfoIn"] = t.struct(
        {"targetAudienceClientId": t.string()}
    ).named(renames["IapTestServiceAccountInfoIn"])
    types["IapTestServiceAccountInfoOut"] = t.struct(
        {
            "targetAudienceClientId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IapTestServiceAccountInfoOut"])
    types["ScanRunIn"] = t.struct(
        {
            "executionState": t.string().optional(),
            "errorTrace": t.proxy(renames["ScanRunErrorTraceIn"]).optional(),
            "urlsTestedCount": t.string().optional(),
            "endTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "resultState": t.string().optional(),
            "hasVulnerabilities": t.boolean().optional(),
            "name": t.string().optional(),
            "warningTraces": t.array(
                t.proxy(renames["ScanRunWarningTraceIn"])
            ).optional(),
            "startTime": t.string().optional(),
            "urlsCrawledCount": t.string().optional(),
        }
    ).named(renames["ScanRunIn"])
    types["ScanRunOut"] = t.struct(
        {
            "executionState": t.string().optional(),
            "errorTrace": t.proxy(renames["ScanRunErrorTraceOut"]).optional(),
            "urlsTestedCount": t.string().optional(),
            "endTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "resultState": t.string().optional(),
            "hasVulnerabilities": t.boolean().optional(),
            "name": t.string().optional(),
            "warningTraces": t.array(
                t.proxy(renames["ScanRunWarningTraceOut"])
            ).optional(),
            "startTime": t.string().optional(),
            "urlsCrawledCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunOut"])

    functions = {}
    functions["projectsScanConfigsGet"] = websecurityscanner.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsList"] = websecurityscanner.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsCreate"] = websecurityscanner.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsStart"] = websecurityscanner.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsPatch"] = websecurityscanner.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsDelete"] = websecurityscanner.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsStop"] = websecurityscanner.get(
        "v1/{parent}/scanRuns",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsGet"] = websecurityscanner.get(
        "v1/{parent}/scanRuns",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsList"] = websecurityscanner.get(
        "v1/{parent}/scanRuns",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsFindingsGet"] = websecurityscanner.get(
        "v1/{parent}/findings",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsFindingsList"] = websecurityscanner.get(
        "v1/{parent}/findings",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsScanConfigsScanRunsFindingTypeStatsList"
    ] = websecurityscanner.get(
        "v1/{parent}/findingTypeStats",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListFindingTypeStatsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsCrawledUrlsList"] = websecurityscanner.get(
        "v1/{parent}/crawledUrls",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCrawledUrlsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="websecurityscanner", renames=renames, types=types, functions=functions
    )
