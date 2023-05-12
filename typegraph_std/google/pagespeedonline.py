from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_pagespeedonline() -> Import:
    pagespeedonline = HTTPRuntime("https://pagespeedonline.googleapis.com/")

    renames = {
        "ErrorResponse": "_pagespeedonline_1_ErrorResponse",
        "LighthouseCategoryV5In": "_pagespeedonline_2_LighthouseCategoryV5In",
        "LighthouseCategoryV5Out": "_pagespeedonline_3_LighthouseCategoryV5Out",
        "TimingIn": "_pagespeedonline_4_TimingIn",
        "TimingOut": "_pagespeedonline_5_TimingOut",
        "PagespeedApiLoadingExperienceV5In": "_pagespeedonline_6_PagespeedApiLoadingExperienceV5In",
        "PagespeedApiLoadingExperienceV5Out": "_pagespeedonline_7_PagespeedApiLoadingExperienceV5Out",
        "LighthouseAuditResultV5In": "_pagespeedonline_8_LighthouseAuditResultV5In",
        "LighthouseAuditResultV5Out": "_pagespeedonline_9_LighthouseAuditResultV5Out",
        "PagespeedApiPagespeedResponseV5In": "_pagespeedonline_10_PagespeedApiPagespeedResponseV5In",
        "PagespeedApiPagespeedResponseV5Out": "_pagespeedonline_11_PagespeedApiPagespeedResponseV5Out",
        "CategoriesIn": "_pagespeedonline_12_CategoriesIn",
        "CategoriesOut": "_pagespeedonline_13_CategoriesOut",
        "AuditRefsIn": "_pagespeedonline_14_AuditRefsIn",
        "AuditRefsOut": "_pagespeedonline_15_AuditRefsOut",
        "StackPackIn": "_pagespeedonline_16_StackPackIn",
        "StackPackOut": "_pagespeedonline_17_StackPackOut",
        "CategoryGroupV5In": "_pagespeedonline_18_CategoryGroupV5In",
        "CategoryGroupV5Out": "_pagespeedonline_19_CategoryGroupV5Out",
        "ConfigSettingsIn": "_pagespeedonline_20_ConfigSettingsIn",
        "ConfigSettingsOut": "_pagespeedonline_21_ConfigSettingsOut",
        "PagespeedVersionIn": "_pagespeedonline_22_PagespeedVersionIn",
        "PagespeedVersionOut": "_pagespeedonline_23_PagespeedVersionOut",
        "RuntimeErrorIn": "_pagespeedonline_24_RuntimeErrorIn",
        "RuntimeErrorOut": "_pagespeedonline_25_RuntimeErrorOut",
        "I18nIn": "_pagespeedonline_26_I18nIn",
        "I18nOut": "_pagespeedonline_27_I18nOut",
        "BucketIn": "_pagespeedonline_28_BucketIn",
        "BucketOut": "_pagespeedonline_29_BucketOut",
        "EnvironmentIn": "_pagespeedonline_30_EnvironmentIn",
        "EnvironmentOut": "_pagespeedonline_31_EnvironmentOut",
        "LhrEntityIn": "_pagespeedonline_32_LhrEntityIn",
        "LhrEntityOut": "_pagespeedonline_33_LhrEntityOut",
        "RendererFormattedStringsIn": "_pagespeedonline_34_RendererFormattedStringsIn",
        "RendererFormattedStringsOut": "_pagespeedonline_35_RendererFormattedStringsOut",
        "LighthouseResultV5In": "_pagespeedonline_36_LighthouseResultV5In",
        "LighthouseResultV5Out": "_pagespeedonline_37_LighthouseResultV5Out",
        "UserPageLoadMetricV5In": "_pagespeedonline_38_UserPageLoadMetricV5In",
        "UserPageLoadMetricV5Out": "_pagespeedonline_39_UserPageLoadMetricV5Out",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LighthouseCategoryV5In"] = t.struct(
        {
            "manualDescription": t.string().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "auditRefs": t.array(t.proxy(renames["AuditRefsIn"])).optional(),
        }
    ).named(renames["LighthouseCategoryV5In"])
    types["LighthouseCategoryV5Out"] = t.struct(
        {
            "manualDescription": t.string().optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "auditRefs": t.array(t.proxy(renames["AuditRefsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseCategoryV5Out"])
    types["TimingIn"] = t.struct({"total": t.number().optional()}).named(
        renames["TimingIn"]
    )
    types["TimingOut"] = t.struct(
        {
            "total": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimingOut"])
    types["PagespeedApiLoadingExperienceV5In"] = t.struct(
        {
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "initial_url": t.string().optional(),
            "origin_fallback": t.boolean().optional(),
            "overall_category": t.string().optional(),
        }
    ).named(renames["PagespeedApiLoadingExperienceV5In"])
    types["PagespeedApiLoadingExperienceV5Out"] = t.struct(
        {
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "initial_url": t.string().optional(),
            "origin_fallback": t.boolean().optional(),
            "overall_category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedApiLoadingExperienceV5Out"])
    types["LighthouseAuditResultV5In"] = t.struct(
        {
            "explanation": t.string().optional(),
            "numericUnit": t.string().optional(),
            "displayValue": t.string().optional(),
            "numericValue": t.number().optional(),
            "description": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
            "scoreDisplayMode": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "warnings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LighthouseAuditResultV5In"])
    types["LighthouseAuditResultV5Out"] = t.struct(
        {
            "explanation": t.string().optional(),
            "numericUnit": t.string().optional(),
            "displayValue": t.string().optional(),
            "numericValue": t.number().optional(),
            "description": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
            "scoreDisplayMode": t.string().optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "warnings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseAuditResultV5Out"])
    types["PagespeedApiPagespeedResponseV5In"] = t.struct(
        {
            "loadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5In"]
            ).optional(),
            "captchaResult": t.string().optional(),
            "originLoadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5In"]
            ).optional(),
            "kind": t.string().optional(),
            "lighthouseResult": t.proxy(renames["LighthouseResultV5In"]).optional(),
            "analysisUTCTimestamp": t.string().optional(),
            "version": t.proxy(renames["PagespeedVersionIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PagespeedApiPagespeedResponseV5In"])
    types["PagespeedApiPagespeedResponseV5Out"] = t.struct(
        {
            "loadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5Out"]
            ).optional(),
            "captchaResult": t.string().optional(),
            "originLoadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5Out"]
            ).optional(),
            "kind": t.string().optional(),
            "lighthouseResult": t.proxy(renames["LighthouseResultV5Out"]).optional(),
            "analysisUTCTimestamp": t.string().optional(),
            "version": t.proxy(renames["PagespeedVersionOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedApiPagespeedResponseV5Out"])
    types["CategoriesIn"] = t.struct(
        {
            "best-practices": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "pwa": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "seo": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "accessibility": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "performance": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
        }
    ).named(renames["CategoriesIn"])
    types["CategoriesOut"] = t.struct(
        {
            "best-practices": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "pwa": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "seo": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "accessibility": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "performance": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoriesOut"])
    types["AuditRefsIn"] = t.struct(
        {
            "relevantAudits": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "group": t.string().optional(),
            "acronym": t.string().optional(),
            "weight": t.number().optional(),
        }
    ).named(renames["AuditRefsIn"])
    types["AuditRefsOut"] = t.struct(
        {
            "relevantAudits": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "group": t.string().optional(),
            "acronym": t.string().optional(),
            "weight": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditRefsOut"])
    types["StackPackIn"] = t.struct(
        {
            "descriptions": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "iconDataURL": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["StackPackIn"])
    types["StackPackOut"] = t.struct(
        {
            "descriptions": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "iconDataURL": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackPackOut"])
    types["CategoryGroupV5In"] = t.struct(
        {"description": t.string().optional(), "title": t.string().optional()}
    ).named(renames["CategoryGroupV5In"])
    types["CategoryGroupV5Out"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryGroupV5Out"])
    types["ConfigSettingsIn"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "locale": t.string().optional(),
            "emulatedFormFactor": t.string().optional(),
            "channel": t.string().optional(),
            "onlyCategories": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ConfigSettingsIn"])
    types["ConfigSettingsOut"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "locale": t.string().optional(),
            "emulatedFormFactor": t.string().optional(),
            "channel": t.string().optional(),
            "onlyCategories": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigSettingsOut"])
    types["PagespeedVersionIn"] = t.struct(
        {"major": t.string().optional(), "minor": t.string().optional()}
    ).named(renames["PagespeedVersionIn"])
    types["PagespeedVersionOut"] = t.struct(
        {
            "major": t.string().optional(),
            "minor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedVersionOut"])
    types["RuntimeErrorIn"] = t.struct(
        {"code": t.string().optional(), "message": t.string().optional()}
    ).named(renames["RuntimeErrorIn"])
    types["RuntimeErrorOut"] = t.struct(
        {
            "code": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeErrorOut"])
    types["I18nIn"] = t.struct(
        {
            "rendererFormattedStrings": t.proxy(
                renames["RendererFormattedStringsIn"]
            ).optional()
        }
    ).named(renames["I18nIn"])
    types["I18nOut"] = t.struct(
        {
            "rendererFormattedStrings": t.proxy(
                renames["RendererFormattedStringsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["I18nOut"])
    types["BucketIn"] = t.struct(
        {
            "min": t.integer().optional(),
            "proportion": t.number().optional(),
            "max": t.integer().optional(),
        }
    ).named(renames["BucketIn"])
    types["BucketOut"] = t.struct(
        {
            "min": t.integer().optional(),
            "proportion": t.number().optional(),
            "max": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "credits": t.struct({"_": t.string().optional()}).optional(),
            "networkUserAgent": t.string().optional(),
            "benchmarkIndex": t.number().optional(),
            "hostUserAgent": t.string().optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "credits": t.struct({"_": t.string().optional()}).optional(),
            "networkUserAgent": t.string().optional(),
            "benchmarkIndex": t.number().optional(),
            "hostUserAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["LhrEntityIn"] = t.struct(
        {
            "category": t.string().optional(),
            "origins": t.array(t.string()),
            "name": t.string(),
            "isFirstParty": t.boolean().optional(),
            "homepage": t.string().optional(),
            "isUnrecognized": t.boolean().optional(),
        }
    ).named(renames["LhrEntityIn"])
    types["LhrEntityOut"] = t.struct(
        {
            "category": t.string().optional(),
            "origins": t.array(t.string()),
            "name": t.string(),
            "isFirstParty": t.boolean().optional(),
            "homepage": t.string().optional(),
            "isUnrecognized": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LhrEntityOut"])
    types["RendererFormattedStringsIn"] = t.struct(
        {
            "calculatorLink": t.string().optional(),
            "runtimeSettingsFetchTime": t.string().optional(),
            "scorescaleLabel": t.string().optional(),
            "dropdownSaveHTML": t.string().optional(),
            "runtimeSettingsUANetwork": t.string().optional(),
            "errorMissingAuditInfo": t.string().optional(),
            "runtimeMobileEmulation": t.string().optional(),
            "runtimeSettingsUrl": t.string().optional(),
            "thirdPartyResourcesLabel": t.string().optional(),
            "snippetExpandButtonLabel": t.string().optional(),
            "footerIssue": t.string().optional(),
            "snippetCollapseButtonLabel": t.string().optional(),
            "dropdownViewer": t.string().optional(),
            "runtimeNoEmulation": t.string().optional(),
            "lsPerformanceCategoryDescription": t.string().optional(),
            "varianceDisclaimer": t.string().optional(),
            "notApplicableAuditsGroupTitle": t.string().optional(),
            "dropdownDarkTheme": t.string().optional(),
            "runtimeSettingsDevice": t.string().optional(),
            "dropdownSaveJSON": t.string().optional(),
            "runtimeSettingsTitle": t.string().optional(),
            "runtimeSettingsChannel": t.string().optional(),
            "dropdownSaveGist": t.string().optional(),
            "passedAuditsGroupTitle": t.string().optional(),
            "runtimeSettingsAxeVersion": t.string().optional(),
            "warningAuditsGroupTitle": t.string().optional(),
            "crcLongestDurationLabel": t.string().optional(),
            "opportunityResourceColumnLabel": t.string().optional(),
            "runtimeSettingsNetworkThrottling": t.string().optional(),
            "runtimeSettingsCPUThrottling": t.string().optional(),
            "runtimeUnknown": t.string().optional(),
            "dropdownPrintSummary": t.string().optional(),
            "viewTreemapLabel": t.string().optional(),
            "warningHeader": t.string().optional(),
            "dropdownPrintExpanded": t.string().optional(),
            "crcInitialNavigation": t.string().optional(),
            "throttlingProvided": t.string().optional(),
            "runtimeDesktopEmulation": t.string().optional(),
            "dropdownCopyJSON": t.string().optional(),
            "toplevelWarningsMessage": t.string().optional(),
            "runtimeSettingsUA": t.string().optional(),
            "runtimeSettingsBenchmark": t.string().optional(),
            "opportunitySavingsColumnLabel": t.string().optional(),
            "manualAuditsGroupTitle": t.string().optional(),
            "auditGroupExpandTooltip": t.string().optional(),
            "labDataTitle": t.string().optional(),
            "errorLabel": t.string().optional(),
            "showRelevantAudits": t.string().optional(),
        }
    ).named(renames["RendererFormattedStringsIn"])
    types["RendererFormattedStringsOut"] = t.struct(
        {
            "calculatorLink": t.string().optional(),
            "runtimeSettingsFetchTime": t.string().optional(),
            "scorescaleLabel": t.string().optional(),
            "dropdownSaveHTML": t.string().optional(),
            "runtimeSettingsUANetwork": t.string().optional(),
            "errorMissingAuditInfo": t.string().optional(),
            "runtimeMobileEmulation": t.string().optional(),
            "runtimeSettingsUrl": t.string().optional(),
            "thirdPartyResourcesLabel": t.string().optional(),
            "snippetExpandButtonLabel": t.string().optional(),
            "footerIssue": t.string().optional(),
            "snippetCollapseButtonLabel": t.string().optional(),
            "dropdownViewer": t.string().optional(),
            "runtimeNoEmulation": t.string().optional(),
            "lsPerformanceCategoryDescription": t.string().optional(),
            "varianceDisclaimer": t.string().optional(),
            "notApplicableAuditsGroupTitle": t.string().optional(),
            "dropdownDarkTheme": t.string().optional(),
            "runtimeSettingsDevice": t.string().optional(),
            "dropdownSaveJSON": t.string().optional(),
            "runtimeSettingsTitle": t.string().optional(),
            "runtimeSettingsChannel": t.string().optional(),
            "dropdownSaveGist": t.string().optional(),
            "passedAuditsGroupTitle": t.string().optional(),
            "runtimeSettingsAxeVersion": t.string().optional(),
            "warningAuditsGroupTitle": t.string().optional(),
            "crcLongestDurationLabel": t.string().optional(),
            "opportunityResourceColumnLabel": t.string().optional(),
            "runtimeSettingsNetworkThrottling": t.string().optional(),
            "runtimeSettingsCPUThrottling": t.string().optional(),
            "runtimeUnknown": t.string().optional(),
            "dropdownPrintSummary": t.string().optional(),
            "viewTreemapLabel": t.string().optional(),
            "warningHeader": t.string().optional(),
            "dropdownPrintExpanded": t.string().optional(),
            "crcInitialNavigation": t.string().optional(),
            "throttlingProvided": t.string().optional(),
            "runtimeDesktopEmulation": t.string().optional(),
            "dropdownCopyJSON": t.string().optional(),
            "toplevelWarningsMessage": t.string().optional(),
            "runtimeSettingsUA": t.string().optional(),
            "runtimeSettingsBenchmark": t.string().optional(),
            "opportunitySavingsColumnLabel": t.string().optional(),
            "manualAuditsGroupTitle": t.string().optional(),
            "auditGroupExpandTooltip": t.string().optional(),
            "labDataTitle": t.string().optional(),
            "errorLabel": t.string().optional(),
            "showRelevantAudits": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RendererFormattedStringsOut"])
    types["LighthouseResultV5In"] = t.struct(
        {
            "stackPacks": t.array(t.proxy(renames["StackPackIn"])).optional(),
            "i18n": t.proxy(renames["I18nIn"]).optional(),
            "timing": t.proxy(renames["TimingIn"]).optional(),
            "userAgent": t.string().optional(),
            "mainDocumentUrl": t.string().optional(),
            "lighthouseVersion": t.string().optional(),
            "audits": t.struct({"_": t.string().optional()}).optional(),
            "requestedUrl": t.string().optional(),
            "configSettings": t.proxy(renames["ConfigSettingsIn"]).optional(),
            "finalUrl": t.string().optional(),
            "fullPageScreenshot": t.struct({"_": t.string().optional()}).optional(),
            "finalDisplayedUrl": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "categoryGroups": t.struct({"_": t.string().optional()}).optional(),
            "entities": t.array(t.proxy(renames["LhrEntityIn"])).optional(),
            "fetchTime": t.string().optional(),
            "runtimeError": t.proxy(renames["RuntimeErrorIn"]).optional(),
            "runWarnings": t.array(t.struct({"_": t.string().optional()})).optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
        }
    ).named(renames["LighthouseResultV5In"])
    types["LighthouseResultV5Out"] = t.struct(
        {
            "stackPacks": t.array(t.proxy(renames["StackPackOut"])).optional(),
            "i18n": t.proxy(renames["I18nOut"]).optional(),
            "timing": t.proxy(renames["TimingOut"]).optional(),
            "userAgent": t.string().optional(),
            "mainDocumentUrl": t.string().optional(),
            "lighthouseVersion": t.string().optional(),
            "audits": t.struct({"_": t.string().optional()}).optional(),
            "requestedUrl": t.string().optional(),
            "configSettings": t.proxy(renames["ConfigSettingsOut"]).optional(),
            "finalUrl": t.string().optional(),
            "fullPageScreenshot": t.struct({"_": t.string().optional()}).optional(),
            "finalDisplayedUrl": t.string().optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "categoryGroups": t.struct({"_": t.string().optional()}).optional(),
            "entities": t.array(t.proxy(renames["LhrEntityOut"])).optional(),
            "fetchTime": t.string().optional(),
            "runtimeError": t.proxy(renames["RuntimeErrorOut"]).optional(),
            "runWarnings": t.array(t.struct({"_": t.string().optional()})).optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseResultV5Out"])
    types["UserPageLoadMetricV5In"] = t.struct(
        {
            "percentile": t.integer().optional(),
            "distributions": t.array(t.proxy(renames["BucketIn"])).optional(),
            "formFactor": t.string().optional(),
            "category": t.string().optional(),
            "metricId": t.string().optional(),
            "median": t.integer().optional(),
        }
    ).named(renames["UserPageLoadMetricV5In"])
    types["UserPageLoadMetricV5Out"] = t.struct(
        {
            "percentile": t.integer().optional(),
            "distributions": t.array(t.proxy(renames["BucketOut"])).optional(),
            "formFactor": t.string().optional(),
            "category": t.string().optional(),
            "metricId": t.string().optional(),
            "median": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPageLoadMetricV5Out"])

    functions = {}
    functions["pagespeedapiRunpagespeed"] = pagespeedonline.get(
        "pagespeedonline/v5/runPagespeed",
        t.struct(
            {
                "utm_campaign": t.string().optional(),
                "strategy": t.string().optional(),
                "utm_source": t.string().optional(),
                "captchaToken": t.string().optional(),
                "category": t.string().optional(),
                "locale": t.string().optional(),
                "url": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PagespeedApiPagespeedResponseV5Out"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="pagespeedonline",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
