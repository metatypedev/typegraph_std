from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_websecurityscanner() -> Import:
    websecurityscanner = HTTPRuntime("https://websecurityscanner.googleapis.com/")

    renames = {
        "ErrorResponse": "_websecurityscanner_1_ErrorResponse",
        "ListScanRunsResponseIn": "_websecurityscanner_2_ListScanRunsResponseIn",
        "ListScanRunsResponseOut": "_websecurityscanner_3_ListScanRunsResponseOut",
        "XssIn": "_websecurityscanner_4_XssIn",
        "XssOut": "_websecurityscanner_5_XssOut",
        "FindingIn": "_websecurityscanner_6_FindingIn",
        "FindingOut": "_websecurityscanner_7_FindingOut",
        "ScheduleIn": "_websecurityscanner_8_ScheduleIn",
        "ScheduleOut": "_websecurityscanner_9_ScheduleOut",
        "IapTestServiceAccountInfoIn": "_websecurityscanner_10_IapTestServiceAccountInfoIn",
        "IapTestServiceAccountInfoOut": "_websecurityscanner_11_IapTestServiceAccountInfoOut",
        "EmptyIn": "_websecurityscanner_12_EmptyIn",
        "EmptyOut": "_websecurityscanner_13_EmptyOut",
        "StopScanRunRequestIn": "_websecurityscanner_14_StopScanRunRequestIn",
        "StopScanRunRequestOut": "_websecurityscanner_15_StopScanRunRequestOut",
        "IapCredentialIn": "_websecurityscanner_16_IapCredentialIn",
        "IapCredentialOut": "_websecurityscanner_17_IapCredentialOut",
        "StartScanRunRequestIn": "_websecurityscanner_18_StartScanRunRequestIn",
        "StartScanRunRequestOut": "_websecurityscanner_19_StartScanRunRequestOut",
        "ScanConfigErrorIn": "_websecurityscanner_20_ScanConfigErrorIn",
        "ScanConfigErrorOut": "_websecurityscanner_21_ScanConfigErrorOut",
        "HeaderIn": "_websecurityscanner_22_HeaderIn",
        "HeaderOut": "_websecurityscanner_23_HeaderOut",
        "ScanRunErrorTraceIn": "_websecurityscanner_24_ScanRunErrorTraceIn",
        "ScanRunErrorTraceOut": "_websecurityscanner_25_ScanRunErrorTraceOut",
        "ListScanConfigsResponseIn": "_websecurityscanner_26_ListScanConfigsResponseIn",
        "ListScanConfigsResponseOut": "_websecurityscanner_27_ListScanConfigsResponseOut",
        "VulnerableHeadersIn": "_websecurityscanner_28_VulnerableHeadersIn",
        "VulnerableHeadersOut": "_websecurityscanner_29_VulnerableHeadersOut",
        "FindingTypeStatsIn": "_websecurityscanner_30_FindingTypeStatsIn",
        "FindingTypeStatsOut": "_websecurityscanner_31_FindingTypeStatsOut",
        "XxeIn": "_websecurityscanner_32_XxeIn",
        "XxeOut": "_websecurityscanner_33_XxeOut",
        "CrawledUrlIn": "_websecurityscanner_34_CrawledUrlIn",
        "CrawledUrlOut": "_websecurityscanner_35_CrawledUrlOut",
        "ListCrawledUrlsResponseIn": "_websecurityscanner_36_ListCrawledUrlsResponseIn",
        "ListCrawledUrlsResponseOut": "_websecurityscanner_37_ListCrawledUrlsResponseOut",
        "VulnerableParametersIn": "_websecurityscanner_38_VulnerableParametersIn",
        "VulnerableParametersOut": "_websecurityscanner_39_VulnerableParametersOut",
        "ScanRunWarningTraceIn": "_websecurityscanner_40_ScanRunWarningTraceIn",
        "ScanRunWarningTraceOut": "_websecurityscanner_41_ScanRunWarningTraceOut",
        "ListFindingsResponseIn": "_websecurityscanner_42_ListFindingsResponseIn",
        "ListFindingsResponseOut": "_websecurityscanner_43_ListFindingsResponseOut",
        "ViolatingResourceIn": "_websecurityscanner_44_ViolatingResourceIn",
        "ViolatingResourceOut": "_websecurityscanner_45_ViolatingResourceOut",
        "GoogleAccountIn": "_websecurityscanner_46_GoogleAccountIn",
        "GoogleAccountOut": "_websecurityscanner_47_GoogleAccountOut",
        "ScanRunIn": "_websecurityscanner_48_ScanRunIn",
        "ScanRunOut": "_websecurityscanner_49_ScanRunOut",
        "ScanConfigIn": "_websecurityscanner_50_ScanConfigIn",
        "ScanConfigOut": "_websecurityscanner_51_ScanConfigOut",
        "FormIn": "_websecurityscanner_52_FormIn",
        "FormOut": "_websecurityscanner_53_FormOut",
        "CustomAccountIn": "_websecurityscanner_54_CustomAccountIn",
        "CustomAccountOut": "_websecurityscanner_55_CustomAccountOut",
        "AuthenticationIn": "_websecurityscanner_56_AuthenticationIn",
        "AuthenticationOut": "_websecurityscanner_57_AuthenticationOut",
        "OutdatedLibraryIn": "_websecurityscanner_58_OutdatedLibraryIn",
        "OutdatedLibraryOut": "_websecurityscanner_59_OutdatedLibraryOut",
        "ListFindingTypeStatsResponseIn": "_websecurityscanner_60_ListFindingTypeStatsResponseIn",
        "ListFindingTypeStatsResponseOut": "_websecurityscanner_61_ListFindingTypeStatsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["XssIn"] = t.struct(
        {
            "storedXssSeedingUrl": t.string().optional(),
            "stackTraces": t.array(t.string()).optional(),
            "errorMessage": t.string().optional(),
            "attackVector": t.string().optional(),
        }
    ).named(renames["XssIn"])
    types["XssOut"] = t.struct(
        {
            "storedXssSeedingUrl": t.string().optional(),
            "stackTraces": t.array(t.string()).optional(),
            "errorMessage": t.string().optional(),
            "attackVector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["XssOut"])
    types["FindingIn"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "frameUrl": t.string().optional(),
            "violatingResource": t.proxy(renames["ViolatingResourceIn"]).optional(),
            "reproductionUrl": t.string().optional(),
            "outdatedLibrary": t.proxy(renames["OutdatedLibraryIn"]).optional(),
            "findingType": t.string().optional(),
            "name": t.string().optional(),
            "finalUrl": t.string().optional(),
            "body": t.string().optional(),
            "vulnerableHeaders": t.proxy(renames["VulnerableHeadersIn"]).optional(),
            "vulnerableParameters": t.proxy(
                renames["VulnerableParametersIn"]
            ).optional(),
            "fuzzedUrl": t.string().optional(),
            "description": t.string().optional(),
            "form": t.proxy(renames["FormIn"]).optional(),
            "xss": t.proxy(renames["XssIn"]).optional(),
            "trackingId": t.string().optional(),
        }
    ).named(renames["FindingIn"])
    types["FindingOut"] = t.struct(
        {
            "httpMethod": t.string().optional(),
            "frameUrl": t.string().optional(),
            "violatingResource": t.proxy(renames["ViolatingResourceOut"]).optional(),
            "reproductionUrl": t.string().optional(),
            "outdatedLibrary": t.proxy(renames["OutdatedLibraryOut"]).optional(),
            "findingType": t.string().optional(),
            "name": t.string().optional(),
            "finalUrl": t.string().optional(),
            "body": t.string().optional(),
            "vulnerableHeaders": t.proxy(renames["VulnerableHeadersOut"]).optional(),
            "vulnerableParameters": t.proxy(
                renames["VulnerableParametersOut"]
            ).optional(),
            "severity": t.string().optional(),
            "fuzzedUrl": t.string().optional(),
            "description": t.string().optional(),
            "xxe": t.proxy(renames["XxeOut"]).optional(),
            "form": t.proxy(renames["FormOut"]).optional(),
            "xss": t.proxy(renames["XssOut"]).optional(),
            "trackingId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FindingOut"])
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
    types["IapTestServiceAccountInfoIn"] = t.struct(
        {"targetAudienceClientId": t.string()}
    ).named(renames["IapTestServiceAccountInfoIn"])
    types["IapTestServiceAccountInfoOut"] = t.struct(
        {
            "targetAudienceClientId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IapTestServiceAccountInfoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["StopScanRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopScanRunRequestIn"]
    )
    types["StopScanRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopScanRunRequestOut"])
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
    types["StartScanRunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartScanRunRequestIn"]
    )
    types["StartScanRunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartScanRunRequestOut"])
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
    types["ScanRunErrorTraceIn"] = t.struct(
        {
            "code": t.string().optional(),
            "scanConfigError": t.proxy(renames["ScanConfigErrorIn"]).optional(),
            "mostCommonHttpErrorCode": t.integer().optional(),
        }
    ).named(renames["ScanRunErrorTraceIn"])
    types["ScanRunErrorTraceOut"] = t.struct(
        {
            "code": t.string().optional(),
            "scanConfigError": t.proxy(renames["ScanConfigErrorOut"]).optional(),
            "mostCommonHttpErrorCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunErrorTraceOut"])
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
    types["VulnerableHeadersIn"] = t.struct(
        {
            "headers": t.array(t.proxy(renames["HeaderIn"])).optional(),
            "missingHeaders": t.array(t.proxy(renames["HeaderIn"])).optional(),
        }
    ).named(renames["VulnerableHeadersIn"])
    types["VulnerableHeadersOut"] = t.struct(
        {
            "headers": t.array(t.proxy(renames["HeaderOut"])).optional(),
            "missingHeaders": t.array(t.proxy(renames["HeaderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerableHeadersOut"])
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
    types["XxeIn"] = t.struct(
        {
            "payloadValue": t.string().optional(),
            "payloadLocation": t.string().optional(),
        }
    ).named(renames["XxeIn"])
    types["XxeOut"] = t.struct(
        {
            "payloadValue": t.string().optional(),
            "payloadLocation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["XxeOut"])
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
    types["VulnerableParametersIn"] = t.struct(
        {"parameterNames": t.array(t.string()).optional()}
    ).named(renames["VulnerableParametersIn"])
    types["VulnerableParametersOut"] = t.struct(
        {
            "parameterNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VulnerableParametersOut"])
    types["ScanRunWarningTraceIn"] = t.struct({"code": t.string().optional()}).named(
        renames["ScanRunWarningTraceIn"]
    )
    types["ScanRunWarningTraceOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunWarningTraceOut"])
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
    types["ScanRunIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "urlsCrawledCount": t.string().optional(),
            "resultState": t.string().optional(),
            "executionState": t.string().optional(),
            "hasVulnerabilities": t.boolean().optional(),
            "name": t.string().optional(),
            "errorTrace": t.proxy(renames["ScanRunErrorTraceIn"]).optional(),
            "warningTraces": t.array(
                t.proxy(renames["ScanRunWarningTraceIn"])
            ).optional(),
            "endTime": t.string().optional(),
            "urlsTestedCount": t.string().optional(),
            "progressPercent": t.integer().optional(),
        }
    ).named(renames["ScanRunIn"])
    types["ScanRunOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "urlsCrawledCount": t.string().optional(),
            "resultState": t.string().optional(),
            "executionState": t.string().optional(),
            "hasVulnerabilities": t.boolean().optional(),
            "name": t.string().optional(),
            "errorTrace": t.proxy(renames["ScanRunErrorTraceOut"]).optional(),
            "warningTraces": t.array(
                t.proxy(renames["ScanRunWarningTraceOut"])
            ).optional(),
            "endTime": t.string().optional(),
            "urlsTestedCount": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanRunOut"])
    types["ScanConfigIn"] = t.struct(
        {
            "displayName": t.string(),
            "schedule": t.proxy(renames["ScheduleIn"]).optional(),
            "exportToSecurityCommandCenter": t.string().optional(),
            "managedScan": t.boolean().optional(),
            "name": t.string().optional(),
            "blacklistPatterns": t.array(t.string()).optional(),
            "userAgent": t.string().optional(),
            "startingUrls": t.array(t.string()),
            "ignoreHttpStatusErrors": t.boolean().optional(),
            "riskLevel": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "staticIpScan": t.boolean().optional(),
            "maxQps": t.integer().optional(),
        }
    ).named(renames["ScanConfigIn"])
    types["ScanConfigOut"] = t.struct(
        {
            "displayName": t.string(),
            "schedule": t.proxy(renames["ScheduleOut"]).optional(),
            "exportToSecurityCommandCenter": t.string().optional(),
            "managedScan": t.boolean().optional(),
            "name": t.string().optional(),
            "blacklistPatterns": t.array(t.string()).optional(),
            "userAgent": t.string().optional(),
            "startingUrls": t.array(t.string()),
            "ignoreHttpStatusErrors": t.boolean().optional(),
            "riskLevel": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "staticIpScan": t.boolean().optional(),
            "maxQps": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScanConfigOut"])
    types["FormIn"] = t.struct(
        {"actionUri": t.string().optional(), "fields": t.array(t.string()).optional()}
    ).named(renames["FormIn"])
    types["FormOut"] = t.struct(
        {
            "actionUri": t.string().optional(),
            "fields": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FormOut"])
    types["CustomAccountIn"] = t.struct(
        {"password": t.string(), "loginUrl": t.string(), "username": t.string()}
    ).named(renames["CustomAccountIn"])
    types["CustomAccountOut"] = t.struct(
        {
            "password": t.string(),
            "loginUrl": t.string(),
            "username": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomAccountOut"])
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
    types["OutdatedLibraryIn"] = t.struct(
        {
            "libraryName": t.string().optional(),
            "version": t.string().optional(),
            "learnMoreUrls": t.array(t.string()).optional(),
        }
    ).named(renames["OutdatedLibraryIn"])
    types["OutdatedLibraryOut"] = t.struct(
        {
            "libraryName": t.string().optional(),
            "version": t.string().optional(),
            "learnMoreUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OutdatedLibraryOut"])
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

    functions = {}
    functions["projectsScanConfigsGet"] = websecurityscanner.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsList"] = websecurityscanner.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsDelete"] = websecurityscanner.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsPatch"] = websecurityscanner.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsCreate"] = websecurityscanner.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsStart"] = websecurityscanner.post(
        "v1/{name}:start",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ScanRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsList"] = websecurityscanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ScanRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsStop"] = websecurityscanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ScanRunOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsScanConfigsScanRunsGet"] = websecurityscanner.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ScanRunOut"]),
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
    functions["projectsScanConfigsScanRunsFindingsGet"] = websecurityscanner.get(
        "v1/{parent}/findings",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListFindingsResponseOut"]),
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

    return Import(
        importer="websecurityscanner",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
