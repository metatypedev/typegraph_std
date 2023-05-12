from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_websecurityscanner() -> Import:
    websecurityscanner = HTTPRuntime("https://websecurityscanner.googleapis.com/")

    renames = {
        "ErrorResponse": "_websecurityscanner_1_ErrorResponse",
        "XxeIn": "_websecurityscanner_2_XxeIn",
        "XxeOut": "_websecurityscanner_3_XxeOut",
        "VulnerableParametersIn": "_websecurityscanner_4_VulnerableParametersIn",
        "VulnerableParametersOut": "_websecurityscanner_5_VulnerableParametersOut",
        "OutdatedLibraryIn": "_websecurityscanner_6_OutdatedLibraryIn",
        "OutdatedLibraryOut": "_websecurityscanner_7_OutdatedLibraryOut",
        "CustomAccountIn": "_websecurityscanner_8_CustomAccountIn",
        "CustomAccountOut": "_websecurityscanner_9_CustomAccountOut",
        "ViolatingResourceIn": "_websecurityscanner_10_ViolatingResourceIn",
        "ViolatingResourceOut": "_websecurityscanner_11_ViolatingResourceOut",
        "ScanConfigErrorIn": "_websecurityscanner_12_ScanConfigErrorIn",
        "ScanConfigErrorOut": "_websecurityscanner_13_ScanConfigErrorOut",
        "CrawledUrlIn": "_websecurityscanner_14_CrawledUrlIn",
        "CrawledUrlOut": "_websecurityscanner_15_CrawledUrlOut",
        "ScanRunWarningTraceIn": "_websecurityscanner_16_ScanRunWarningTraceIn",
        "ScanRunWarningTraceOut": "_websecurityscanner_17_ScanRunWarningTraceOut",
        "StopScanRunRequestIn": "_websecurityscanner_18_StopScanRunRequestIn",
        "StopScanRunRequestOut": "_websecurityscanner_19_StopScanRunRequestOut",
        "HeaderIn": "_websecurityscanner_20_HeaderIn",
        "HeaderOut": "_websecurityscanner_21_HeaderOut",
        "ScanConfigIn": "_websecurityscanner_22_ScanConfigIn",
        "ScanConfigOut": "_websecurityscanner_23_ScanConfigOut",
        "EmptyIn": "_websecurityscanner_24_EmptyIn",
        "EmptyOut": "_websecurityscanner_25_EmptyOut",
        "ListFindingsResponseIn": "_websecurityscanner_26_ListFindingsResponseIn",
        "ListFindingsResponseOut": "_websecurityscanner_27_ListFindingsResponseOut",
        "XssIn": "_websecurityscanner_28_XssIn",
        "XssOut": "_websecurityscanner_29_XssOut",
        "ScanRunErrorTraceIn": "_websecurityscanner_30_ScanRunErrorTraceIn",
        "ScanRunErrorTraceOut": "_websecurityscanner_31_ScanRunErrorTraceOut",
        "ListScanRunsResponseIn": "_websecurityscanner_32_ListScanRunsResponseIn",
        "ListScanRunsResponseOut": "_websecurityscanner_33_ListScanRunsResponseOut",
        "AuthenticationIn": "_websecurityscanner_34_AuthenticationIn",
        "AuthenticationOut": "_websecurityscanner_35_AuthenticationOut",
        "ListCrawledUrlsResponseIn": "_websecurityscanner_36_ListCrawledUrlsResponseIn",
        "ListCrawledUrlsResponseOut": "_websecurityscanner_37_ListCrawledUrlsResponseOut",
        "GoogleAccountIn": "_websecurityscanner_38_GoogleAccountIn",
        "GoogleAccountOut": "_websecurityscanner_39_GoogleAccountOut",
        "ScanRunIn": "_websecurityscanner_40_ScanRunIn",
        "ScanRunOut": "_websecurityscanner_41_ScanRunOut",
        "ListFindingTypeStatsResponseIn": "_websecurityscanner_42_ListFindingTypeStatsResponseIn",
        "ListFindingTypeStatsResponseOut": "_websecurityscanner_43_ListFindingTypeStatsResponseOut",
        "FormIn": "_websecurityscanner_44_FormIn",
        "FormOut": "_websecurityscanner_45_FormOut",
        "ScheduleIn": "_websecurityscanner_46_ScheduleIn",
        "ScheduleOut": "_websecurityscanner_47_ScheduleOut",
        "IapCredentialIn": "_websecurityscanner_48_IapCredentialIn",
        "IapCredentialOut": "_websecurityscanner_49_IapCredentialOut",
        "IapTestServiceAccountInfoIn": "_websecurityscanner_50_IapTestServiceAccountInfoIn",
        "IapTestServiceAccountInfoOut": "_websecurityscanner_51_IapTestServiceAccountInfoOut",
        "VulnerableHeadersIn": "_websecurityscanner_52_VulnerableHeadersIn",
        "VulnerableHeadersOut": "_websecurityscanner_53_VulnerableHeadersOut",
        "FindingIn": "_websecurityscanner_54_FindingIn",
        "FindingOut": "_websecurityscanner_55_FindingOut",
        "FindingTypeStatsIn": "_websecurityscanner_56_FindingTypeStatsIn",
        "FindingTypeStatsOut": "_websecurityscanner_57_FindingTypeStatsOut",
        "ListScanConfigsResponseIn": "_websecurityscanner_58_ListScanConfigsResponseIn",
        "ListScanConfigsResponseOut": "_websecurityscanner_59_ListScanConfigsResponseOut",
        "StartScanRunRequestIn": "_websecurityscanner_60_StartScanRunRequestIn",
        "StartScanRunRequestOut": "_websecurityscanner_61_StartScanRunRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "learnMoreUrls": t.array(t.string()).optional(),
            "libraryName": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["OutdatedLibraryIn"])
    types["OutdatedLibraryOut"] = t.struct(
        {
            "learnMoreUrls": t.array(t.string()).optional(),
            "libraryName": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutdatedLibraryOut"])
    types["CustomAccountIn"] = t.struct(
        {"username": t.string(), "password": t.string(), "loginUrl": t.string()}
    ).named(renames["CustomAccountIn"])
    types["CustomAccountOut"] = t.struct(
        {
            "username": t.string(),
            "password": t.string(),
            "loginUrl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAccountOut"])
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
    types["CrawledUrlIn"] = t.struct(
        {
            "url": t.string().optional(),
            "httpMethod": t.string().optional(),
            "body": t.string().optional(),
        }
    ).named(renames["CrawledUrlIn"])
    types["CrawledUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "httpMethod": t.string().optional(),
            "body": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrawledUrlOut"])
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
    types["ScanConfigIn"] = t.struct(
        {
            "name": t.string().optional(),
            "riskLevel": t.string().optional(),
            "staticIpScan": t.boolean().optional(),
            "managedScan": t.boolean().optional(),
            "displayName": t.string(),
            "schedule": t.proxy(renames["ScheduleIn"]).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "userAgent": t.string().optional(),
            "blacklistPatterns": t.array(t.string()).optional(),
            "ignoreHttpStatusErrors": t.boolean().optional(),
            "startingUrls": t.array(t.string()),
            "maxQps": t.integer().optional(),
            "exportToSecurityCommandCenter": t.string().optional(),
        }
    ).named(renames["ScanConfigIn"])
    types["ScanConfigOut"] = t.struct(
        {
            "name": t.string().optional(),
            "riskLevel": t.string().optional(),
            "staticIpScan": t.boolean().optional(),
            "managedScan": t.boolean().optional(),
            "displayName": t.string(),
            "schedule": t.proxy(renames["ScheduleOut"]).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "userAgent": t.string().optional(),
            "blacklistPatterns": t.array(t.string()).optional(),
            "ignoreHttpStatusErrors": t.boolean().optional(),
            "startingUrls": t.array(t.string()),
            "maxQps": t.integer().optional(),
            "exportToSecurityCommandCenter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanConfigOut"])
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
    types["XssIn"] = t.struct(
        {
            "attackVector": t.string().optional(),
            "storedXssSeedingUrl": t.string().optional(),
            "stackTraces": t.array(t.string()).optional(),
            "errorMessage": t.string().optional(),
        }
    ).named(renames["XssIn"])
    types["XssOut"] = t.struct(
        {
            "attackVector": t.string().optional(),
            "storedXssSeedingUrl": t.string().optional(),
            "stackTraces": t.array(t.string()).optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["XssOut"])
    types["ScanRunErrorTraceIn"] = t.struct(
        {
            "scanConfigError": t.proxy(renames["ScanConfigErrorIn"]).optional(),
            "mostCommonHttpErrorCode": t.integer().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ScanRunErrorTraceIn"])
    types["ScanRunErrorTraceOut"] = t.struct(
        {
            "scanConfigError": t.proxy(renames["ScanConfigErrorOut"]).optional(),
            "mostCommonHttpErrorCode": t.integer().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunErrorTraceOut"])
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
    types["AuthenticationIn"] = t.struct(
        {
            "customAccount": t.proxy(renames["CustomAccountIn"]).optional(),
            "iapCredential": t.proxy(renames["IapCredentialIn"]).optional(),
            "googleAccount": t.proxy(renames["GoogleAccountIn"]).optional(),
        }
    ).named(renames["AuthenticationIn"])
    types["AuthenticationOut"] = t.struct(
        {
            "customAccount": t.proxy(renames["CustomAccountOut"]).optional(),
            "iapCredential": t.proxy(renames["IapCredentialOut"]).optional(),
            "googleAccount": t.proxy(renames["GoogleAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationOut"])
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
    types["ScanRunIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "resultState": t.string().optional(),
            "name": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "urlsTestedCount": t.string().optional(),
            "warningTraces": t.array(
                t.proxy(renames["ScanRunWarningTraceIn"])
            ).optional(),
            "executionState": t.string().optional(),
            "hasVulnerabilities": t.boolean().optional(),
            "errorTrace": t.proxy(renames["ScanRunErrorTraceIn"]).optional(),
            "urlsCrawledCount": t.string().optional(),
        }
    ).named(renames["ScanRunIn"])
    types["ScanRunOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "resultState": t.string().optional(),
            "name": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "urlsTestedCount": t.string().optional(),
            "warningTraces": t.array(
                t.proxy(renames["ScanRunWarningTraceOut"])
            ).optional(),
            "executionState": t.string().optional(),
            "hasVulnerabilities": t.boolean().optional(),
            "errorTrace": t.proxy(renames["ScanRunErrorTraceOut"]).optional(),
            "urlsCrawledCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunOut"])
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
    types["IapTestServiceAccountInfoIn"] = t.struct(
        {"targetAudienceClientId": t.string()}
    ).named(renames["IapTestServiceAccountInfoIn"])
    types["IapTestServiceAccountInfoOut"] = t.struct(
        {
            "targetAudienceClientId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IapTestServiceAccountInfoOut"])
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
            "vulnerableParameters": t.proxy(
                renames["VulnerableParametersIn"]
            ).optional(),
            "finalUrl": t.string().optional(),
            "description": t.string().optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
            "findingType": t.string().optional(),
            "name": t.string().optional(),
            "violatingResource": t.proxy(renames["ViolatingResourceIn"]).optional(),
            "fuzzedUrl": t.string().optional(),
            "httpMethod": t.string().optional(),
            "trackingId": t.string().optional(),
            "frameUrl": t.string().optional(),
            "reproductionUrl": t.string().optional(),
            "outdatedLibrary": t.proxy(renames["OutdatedLibraryIn"]).optional(),
            "body": t.string().optional(),
            "vulnerableHeaders": t.proxy(renames["VulnerableHeadersIn"]).optional(),
            "xss": t.proxy(renames["XssIn"]).optional(),
        }
    ).named(renames["FindingIn"])
    types["FindingOut"] = t.struct(
        {
            "vulnerableParameters": t.proxy(
                renames["VulnerableParametersOut"]
            ).optional(),
            "finalUrl": t.string().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "findingType": t.string().optional(),
            "name": t.string().optional(),
            "violatingResource": t.proxy(renames["ViolatingResourceOut"]).optional(),
            "fuzzedUrl": t.string().optional(),
            "httpMethod": t.string().optional(),
            "trackingId": t.string().optional(),
            "frameUrl": t.string().optional(),
            "reproductionUrl": t.string().optional(),
            "xxe": t.proxy(renames["XxeOut"]).optional(),
            "outdatedLibrary": t.proxy(renames["OutdatedLibraryOut"]).optional(),
            "body": t.string().optional(),
            "vulnerableHeaders": t.proxy(renames["VulnerableHeadersOut"]).optional(),
            "xss": t.proxy(renames["XssOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingOut"])
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
    types["StartScanRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartScanRunRequestIn"]
    )
    types["StartScanRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartScanRunRequestOut"])

    functions = {}
    functions["projectsScanConfigsCreate"] = websecurityscanner.get(
        "v1/{parent}/scanConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsPatch"] = websecurityscanner.get(
        "v1/{parent}/scanConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsStart"] = websecurityscanner.get(
        "v1/{parent}/scanConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsGet"] = websecurityscanner.get(
        "v1/{parent}/scanConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsDelete"] = websecurityscanner.get(
        "v1/{parent}/scanConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsList"] = websecurityscanner.get(
        "v1/{parent}/scanConfigs",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListScanConfigsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsGet"] = websecurityscanner.get(
        "v1/{parent}/scanRuns",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageToken": t.string().optional(),
                "parent": t.string(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
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
