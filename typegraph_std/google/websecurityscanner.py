from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_websecurityscanner():
    websecurityscanner = HTTPRuntime("https://websecurityscanner.googleapis.com/")

    renames = {
        "ErrorResponse": "_websecurityscanner_1_ErrorResponse",
        "FindingIn": "_websecurityscanner_2_FindingIn",
        "FindingOut": "_websecurityscanner_3_FindingOut",
        "ListScanRunsResponseIn": "_websecurityscanner_4_ListScanRunsResponseIn",
        "ListScanRunsResponseOut": "_websecurityscanner_5_ListScanRunsResponseOut",
        "ScanConfigErrorIn": "_websecurityscanner_6_ScanConfigErrorIn",
        "ScanConfigErrorOut": "_websecurityscanner_7_ScanConfigErrorOut",
        "XxeIn": "_websecurityscanner_8_XxeIn",
        "XxeOut": "_websecurityscanner_9_XxeOut",
        "IapCredentialIn": "_websecurityscanner_10_IapCredentialIn",
        "IapCredentialOut": "_websecurityscanner_11_IapCredentialOut",
        "ScanRunIn": "_websecurityscanner_12_ScanRunIn",
        "ScanRunOut": "_websecurityscanner_13_ScanRunOut",
        "CrawledUrlIn": "_websecurityscanner_14_CrawledUrlIn",
        "CrawledUrlOut": "_websecurityscanner_15_CrawledUrlOut",
        "FindingTypeStatsIn": "_websecurityscanner_16_FindingTypeStatsIn",
        "FindingTypeStatsOut": "_websecurityscanner_17_FindingTypeStatsOut",
        "ScanRunErrorTraceIn": "_websecurityscanner_18_ScanRunErrorTraceIn",
        "ScanRunErrorTraceOut": "_websecurityscanner_19_ScanRunErrorTraceOut",
        "HeaderIn": "_websecurityscanner_20_HeaderIn",
        "HeaderOut": "_websecurityscanner_21_HeaderOut",
        "FormIn": "_websecurityscanner_22_FormIn",
        "FormOut": "_websecurityscanner_23_FormOut",
        "IapTestServiceAccountInfoIn": "_websecurityscanner_24_IapTestServiceAccountInfoIn",
        "IapTestServiceAccountInfoOut": "_websecurityscanner_25_IapTestServiceAccountInfoOut",
        "ListCrawledUrlsResponseIn": "_websecurityscanner_26_ListCrawledUrlsResponseIn",
        "ListCrawledUrlsResponseOut": "_websecurityscanner_27_ListCrawledUrlsResponseOut",
        "VulnerableParametersIn": "_websecurityscanner_28_VulnerableParametersIn",
        "VulnerableParametersOut": "_websecurityscanner_29_VulnerableParametersOut",
        "OutdatedLibraryIn": "_websecurityscanner_30_OutdatedLibraryIn",
        "OutdatedLibraryOut": "_websecurityscanner_31_OutdatedLibraryOut",
        "ListScanConfigsResponseIn": "_websecurityscanner_32_ListScanConfigsResponseIn",
        "ListScanConfigsResponseOut": "_websecurityscanner_33_ListScanConfigsResponseOut",
        "GoogleAccountIn": "_websecurityscanner_34_GoogleAccountIn",
        "GoogleAccountOut": "_websecurityscanner_35_GoogleAccountOut",
        "VulnerableHeadersIn": "_websecurityscanner_36_VulnerableHeadersIn",
        "VulnerableHeadersOut": "_websecurityscanner_37_VulnerableHeadersOut",
        "ListFindingTypeStatsResponseIn": "_websecurityscanner_38_ListFindingTypeStatsResponseIn",
        "ListFindingTypeStatsResponseOut": "_websecurityscanner_39_ListFindingTypeStatsResponseOut",
        "ViolatingResourceIn": "_websecurityscanner_40_ViolatingResourceIn",
        "ViolatingResourceOut": "_websecurityscanner_41_ViolatingResourceOut",
        "ListFindingsResponseIn": "_websecurityscanner_42_ListFindingsResponseIn",
        "ListFindingsResponseOut": "_websecurityscanner_43_ListFindingsResponseOut",
        "AuthenticationIn": "_websecurityscanner_44_AuthenticationIn",
        "AuthenticationOut": "_websecurityscanner_45_AuthenticationOut",
        "CustomAccountIn": "_websecurityscanner_46_CustomAccountIn",
        "CustomAccountOut": "_websecurityscanner_47_CustomAccountOut",
        "ScanConfigIn": "_websecurityscanner_48_ScanConfigIn",
        "ScanConfigOut": "_websecurityscanner_49_ScanConfigOut",
        "XssIn": "_websecurityscanner_50_XssIn",
        "XssOut": "_websecurityscanner_51_XssOut",
        "StartScanRunRequestIn": "_websecurityscanner_52_StartScanRunRequestIn",
        "StartScanRunRequestOut": "_websecurityscanner_53_StartScanRunRequestOut",
        "ScheduleIn": "_websecurityscanner_54_ScheduleIn",
        "ScheduleOut": "_websecurityscanner_55_ScheduleOut",
        "ScanRunWarningTraceIn": "_websecurityscanner_56_ScanRunWarningTraceIn",
        "ScanRunWarningTraceOut": "_websecurityscanner_57_ScanRunWarningTraceOut",
        "StopScanRunRequestIn": "_websecurityscanner_58_StopScanRunRequestIn",
        "StopScanRunRequestOut": "_websecurityscanner_59_StopScanRunRequestOut",
        "EmptyIn": "_websecurityscanner_60_EmptyIn",
        "EmptyOut": "_websecurityscanner_61_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FindingIn"] = t.struct(
        {
            "findingType": t.string().optional(),
            "reproductionUrl": t.string().optional(),
            "name": t.string().optional(),
            "violatingResource": t.proxy(renames["ViolatingResourceIn"]).optional(),
            "vulnerableParameters": t.proxy(
                renames["VulnerableParametersIn"]
            ).optional(),
            "frameUrl": t.string().optional(),
            "finalUrl": t.string().optional(),
            "vulnerableHeaders": t.proxy(renames["VulnerableHeadersIn"]).optional(),
            "description": t.string().optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
            "fuzzedUrl": t.string().optional(),
            "outdatedLibrary": t.proxy(renames["OutdatedLibraryIn"]).optional(),
            "xss": t.proxy(renames["XssIn"]).optional(),
            "httpMethod": t.string().optional(),
            "body": t.string().optional(),
            "trackingId": t.string().optional(),
        }
    ).named(renames["FindingIn"])
    types["FindingOut"] = t.struct(
        {
            "findingType": t.string().optional(),
            "reproductionUrl": t.string().optional(),
            "name": t.string().optional(),
            "violatingResource": t.proxy(renames["ViolatingResourceOut"]).optional(),
            "vulnerableParameters": t.proxy(
                renames["VulnerableParametersOut"]
            ).optional(),
            "frameUrl": t.string().optional(),
            "finalUrl": t.string().optional(),
            "vulnerableHeaders": t.proxy(renames["VulnerableHeadersOut"]).optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "xxe": t.proxy(renames["XxeOut"]).optional(),
            "fuzzedUrl": t.string().optional(),
            "outdatedLibrary": t.proxy(renames["OutdatedLibraryOut"]).optional(),
            "xss": t.proxy(renames["XssOut"]).optional(),
            "httpMethod": t.string().optional(),
            "body": t.string().optional(),
            "trackingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingOut"])
    types["ListScanRunsResponseIn"] = t.struct(
        {
            "scanRuns": t.array(t.proxy(renames["ScanRunIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListScanRunsResponseIn"])
    types["ListScanRunsResponseOut"] = t.struct(
        {
            "scanRuns": t.array(t.proxy(renames["ScanRunOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListScanRunsResponseOut"])
    types["ScanConfigErrorIn"] = t.struct(
        {"fieldName": t.string().optional(), "code": t.string().optional()}
    ).named(renames["ScanConfigErrorIn"])
    types["ScanConfigErrorOut"] = t.struct(
        {
            "fieldName": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanConfigErrorOut"])
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
    types["ScanRunIn"] = t.struct(
        {
            "resultState": t.string().optional(),
            "errorTrace": t.proxy(renames["ScanRunErrorTraceIn"]).optional(),
            "name": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "executionState": t.string().optional(),
            "urlsTestedCount": t.string().optional(),
            "hasVulnerabilities": t.boolean().optional(),
            "startTime": t.string().optional(),
            "warningTraces": t.array(
                t.proxy(renames["ScanRunWarningTraceIn"])
            ).optional(),
            "urlsCrawledCount": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["ScanRunIn"])
    types["ScanRunOut"] = t.struct(
        {
            "resultState": t.string().optional(),
            "errorTrace": t.proxy(renames["ScanRunErrorTraceOut"]).optional(),
            "name": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "executionState": t.string().optional(),
            "urlsTestedCount": t.string().optional(),
            "hasVulnerabilities": t.boolean().optional(),
            "startTime": t.string().optional(),
            "warningTraces": t.array(
                t.proxy(renames["ScanRunWarningTraceOut"])
            ).optional(),
            "urlsCrawledCount": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunOut"])
    types["CrawledUrlIn"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "url": t.string().optional(),
            "body": t.string().optional(),
        }
    ).named(renames["CrawledUrlIn"])
    types["CrawledUrlOut"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "url": t.string().optional(),
            "body": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrawledUrlOut"])
    types["FindingTypeStatsIn"] = t.struct(
        {"findingCount": t.integer().optional(), "findingType": t.string().optional()}
    ).named(renames["FindingTypeStatsIn"])
    types["FindingTypeStatsOut"] = t.struct(
        {
            "findingCount": t.integer().optional(),
            "findingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingTypeStatsOut"])
    types["ScanRunErrorTraceIn"] = t.struct(
        {
            "code": t.string().optional(),
            "mostCommonHttpErrorCode": t.integer().optional(),
            "scanConfigError": t.proxy(renames["ScanConfigErrorIn"]).optional(),
        }
    ).named(renames["ScanRunErrorTraceIn"])
    types["ScanRunErrorTraceOut"] = t.struct(
        {
            "code": t.string().optional(),
            "mostCommonHttpErrorCode": t.integer().optional(),
            "scanConfigError": t.proxy(renames["ScanConfigErrorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunErrorTraceOut"])
    types["HeaderIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["HeaderIn"])
    types["HeaderOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HeaderOut"])
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
    types["IapTestServiceAccountInfoIn"] = t.struct(
        {"targetAudienceClientId": t.string()}
    ).named(renames["IapTestServiceAccountInfoIn"])
    types["IapTestServiceAccountInfoOut"] = t.struct(
        {
            "targetAudienceClientId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IapTestServiceAccountInfoOut"])
    types["ListCrawledUrlsResponseIn"] = t.struct(
        {
            "crawledUrls": t.array(t.proxy(renames["CrawledUrlIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListCrawledUrlsResponseIn"])
    types["ListCrawledUrlsResponseOut"] = t.struct(
        {
            "crawledUrls": t.array(t.proxy(renames["CrawledUrlOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCrawledUrlsResponseOut"])
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
            "libraryName": t.string().optional(),
            "learnMoreUrls": t.array(t.string()).optional(),
        }
    ).named(renames["OutdatedLibraryIn"])
    types["OutdatedLibraryOut"] = t.struct(
        {
            "version": t.string().optional(),
            "libraryName": t.string().optional(),
            "learnMoreUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutdatedLibraryOut"])
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
    types["GoogleAccountIn"] = t.struct(
        {"password": t.string(), "username": t.string()}
    ).named(renames["GoogleAccountIn"])
    types["GoogleAccountOut"] = t.struct(
        {
            "password": t.string(),
            "username": t.string(),
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
    types["ViolatingResourceIn"] = t.struct(
        {"contentType": t.string().optional(), "resourceUrl": t.string().optional()}
    ).named(renames["ViolatingResourceIn"])
    types["ViolatingResourceOut"] = t.struct(
        {
            "contentType": t.string().optional(),
            "resourceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolatingResourceOut"])
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
    types["CustomAccountIn"] = t.struct(
        {"loginUrl": t.string(), "username": t.string(), "password": t.string()}
    ).named(renames["CustomAccountIn"])
    types["CustomAccountOut"] = t.struct(
        {
            "loginUrl": t.string(),
            "username": t.string(),
            "password": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAccountOut"])
    types["ScanConfigIn"] = t.struct(
        {
            "schedule": t.proxy(renames["ScheduleIn"]).optional(),
            "userAgent": t.string().optional(),
            "startingUrls": t.array(t.string()),
            "blacklistPatterns": t.array(t.string()).optional(),
            "displayName": t.string(),
            "exportToSecurityCommandCenter": t.string().optional(),
            "ignoreHttpStatusErrors": t.boolean().optional(),
            "managedScan": t.boolean().optional(),
            "riskLevel": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "staticIpScan": t.boolean().optional(),
            "maxQps": t.integer().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ScanConfigIn"])
    types["ScanConfigOut"] = t.struct(
        {
            "schedule": t.proxy(renames["ScheduleOut"]).optional(),
            "userAgent": t.string().optional(),
            "startingUrls": t.array(t.string()),
            "blacklistPatterns": t.array(t.string()).optional(),
            "displayName": t.string(),
            "exportToSecurityCommandCenter": t.string().optional(),
            "ignoreHttpStatusErrors": t.boolean().optional(),
            "managedScan": t.boolean().optional(),
            "riskLevel": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "staticIpScan": t.boolean().optional(),
            "maxQps": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanConfigOut"])
    types["XssIn"] = t.struct(
        {
            "stackTraces": t.array(t.string()).optional(),
            "errorMessage": t.string().optional(),
            "storedXssSeedingUrl": t.string().optional(),
            "attackVector": t.string().optional(),
        }
    ).named(renames["XssIn"])
    types["XssOut"] = t.struct(
        {
            "stackTraces": t.array(t.string()).optional(),
            "errorMessage": t.string().optional(),
            "storedXssSeedingUrl": t.string().optional(),
            "attackVector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["XssOut"])
    types["StartScanRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartScanRunRequestIn"]
    )
    types["StartScanRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartScanRunRequestOut"])
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
    types["ScanRunWarningTraceIn"] = t.struct({"code": t.string().optional()}).named(
        renames["ScanRunWarningTraceIn"]
    )
    types["ScanRunWarningTraceOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunWarningTraceOut"])
    types["StopScanRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopScanRunRequestIn"]
    )
    types["StopScanRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopScanRunRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

    functions = {}
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
    functions["projectsScanConfigsGet"] = websecurityscanner.delete(
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
    functions["projectsScanConfigsStart"] = websecurityscanner.delete(
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
    functions["projectsScanConfigsScanRunsGet"] = websecurityscanner.get(
        "v1/{parent}/scanRuns",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsStop"] = websecurityscanner.get(
        "v1/{parent}/scanRuns",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanRunsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsCrawledUrlsList"] = websecurityscanner.get(
        "v1/{parent}/crawledUrls",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCrawledUrlsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsFindingsList"] = websecurityscanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FindingOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsFindingsGet"] = websecurityscanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FindingOut"]),
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

    return Import(
        importer="websecurityscanner",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
