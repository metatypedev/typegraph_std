from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_pagespeedonline() -> Import:
    pagespeedonline = HTTPRuntime("https://pagespeedonline.googleapis.com/")

    renames = {
        "ErrorResponse": "_pagespeedonline_1_ErrorResponse",
        "TimingIn": "_pagespeedonline_2_TimingIn",
        "TimingOut": "_pagespeedonline_3_TimingOut",
        "StackPackIn": "_pagespeedonline_4_StackPackIn",
        "StackPackOut": "_pagespeedonline_5_StackPackOut",
        "ConfigSettingsIn": "_pagespeedonline_6_ConfigSettingsIn",
        "ConfigSettingsOut": "_pagespeedonline_7_ConfigSettingsOut",
        "PagespeedApiPagespeedResponseV5In": "_pagespeedonline_8_PagespeedApiPagespeedResponseV5In",
        "PagespeedApiPagespeedResponseV5Out": "_pagespeedonline_9_PagespeedApiPagespeedResponseV5Out",
        "BucketIn": "_pagespeedonline_10_BucketIn",
        "BucketOut": "_pagespeedonline_11_BucketOut",
        "LighthouseResultV5In": "_pagespeedonline_12_LighthouseResultV5In",
        "LighthouseResultV5Out": "_pagespeedonline_13_LighthouseResultV5Out",
        "UserPageLoadMetricV5In": "_pagespeedonline_14_UserPageLoadMetricV5In",
        "UserPageLoadMetricV5Out": "_pagespeedonline_15_UserPageLoadMetricV5Out",
        "PagespeedApiLoadingExperienceV5In": "_pagespeedonline_16_PagespeedApiLoadingExperienceV5In",
        "PagespeedApiLoadingExperienceV5Out": "_pagespeedonline_17_PagespeedApiLoadingExperienceV5Out",
        "AuditRefsIn": "_pagespeedonline_18_AuditRefsIn",
        "AuditRefsOut": "_pagespeedonline_19_AuditRefsOut",
        "I18nIn": "_pagespeedonline_20_I18nIn",
        "I18nOut": "_pagespeedonline_21_I18nOut",
        "LighthouseCategoryV5In": "_pagespeedonline_22_LighthouseCategoryV5In",
        "LighthouseCategoryV5Out": "_pagespeedonline_23_LighthouseCategoryV5Out",
        "RendererFormattedStringsIn": "_pagespeedonline_24_RendererFormattedStringsIn",
        "RendererFormattedStringsOut": "_pagespeedonline_25_RendererFormattedStringsOut",
        "CategoriesIn": "_pagespeedonline_26_CategoriesIn",
        "CategoriesOut": "_pagespeedonline_27_CategoriesOut",
        "RuntimeErrorIn": "_pagespeedonline_28_RuntimeErrorIn",
        "RuntimeErrorOut": "_pagespeedonline_29_RuntimeErrorOut",
        "PagespeedVersionIn": "_pagespeedonline_30_PagespeedVersionIn",
        "PagespeedVersionOut": "_pagespeedonline_31_PagespeedVersionOut",
        "LighthouseAuditResultV5In": "_pagespeedonline_32_LighthouseAuditResultV5In",
        "LighthouseAuditResultV5Out": "_pagespeedonline_33_LighthouseAuditResultV5Out",
        "LhrEntityIn": "_pagespeedonline_34_LhrEntityIn",
        "LhrEntityOut": "_pagespeedonline_35_LhrEntityOut",
        "CategoryGroupV5In": "_pagespeedonline_36_CategoryGroupV5In",
        "CategoryGroupV5Out": "_pagespeedonline_37_CategoryGroupV5Out",
        "EnvironmentIn": "_pagespeedonline_38_EnvironmentIn",
        "EnvironmentOut": "_pagespeedonline_39_EnvironmentOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TimingIn"] = t.struct({"total": t.number().optional()}).named(
        renames["TimingIn"]
    )
    types["TimingOut"] = t.struct(
        {
            "total": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimingOut"])
    types["StackPackIn"] = t.struct(
        {
            "title": t.string().optional(),
            "iconDataURL": t.string().optional(),
            "descriptions": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["StackPackIn"])
    types["StackPackOut"] = t.struct(
        {
            "title": t.string().optional(),
            "iconDataURL": t.string().optional(),
            "descriptions": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackPackOut"])
    types["ConfigSettingsIn"] = t.struct(
        {
            "channel": t.string().optional(),
            "onlyCategories": t.struct({"_": t.string().optional()}).optional(),
            "locale": t.string().optional(),
            "formFactor": t.string().optional(),
            "emulatedFormFactor": t.string().optional(),
        }
    ).named(renames["ConfigSettingsIn"])
    types["ConfigSettingsOut"] = t.struct(
        {
            "channel": t.string().optional(),
            "onlyCategories": t.struct({"_": t.string().optional()}).optional(),
            "locale": t.string().optional(),
            "formFactor": t.string().optional(),
            "emulatedFormFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigSettingsOut"])
    types["PagespeedApiPagespeedResponseV5In"] = t.struct(
        {
            "id": t.string().optional(),
            "lighthouseResult": t.proxy(renames["LighthouseResultV5In"]).optional(),
            "captchaResult": t.string().optional(),
            "analysisUTCTimestamp": t.string().optional(),
            "originLoadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5In"]
            ).optional(),
            "kind": t.string().optional(),
            "version": t.proxy(renames["PagespeedVersionIn"]).optional(),
            "loadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5In"]
            ).optional(),
        }
    ).named(renames["PagespeedApiPagespeedResponseV5In"])
    types["PagespeedApiPagespeedResponseV5Out"] = t.struct(
        {
            "id": t.string().optional(),
            "lighthouseResult": t.proxy(renames["LighthouseResultV5Out"]).optional(),
            "captchaResult": t.string().optional(),
            "analysisUTCTimestamp": t.string().optional(),
            "originLoadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5Out"]
            ).optional(),
            "kind": t.string().optional(),
            "version": t.proxy(renames["PagespeedVersionOut"]).optional(),
            "loadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5Out"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedApiPagespeedResponseV5Out"])
    types["BucketIn"] = t.struct(
        {
            "min": t.integer().optional(),
            "max": t.integer().optional(),
            "proportion": t.number().optional(),
        }
    ).named(renames["BucketIn"])
    types["BucketOut"] = t.struct(
        {
            "min": t.integer().optional(),
            "max": t.integer().optional(),
            "proportion": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOut"])
    types["LighthouseResultV5In"] = t.struct(
        {
            "requestedUrl": t.string().optional(),
            "runWarnings": t.array(t.struct({"_": t.string().optional()})).optional(),
            "fetchTime": t.string().optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "userAgent": t.string().optional(),
            "runtimeError": t.proxy(renames["RuntimeErrorIn"]).optional(),
            "timing": t.proxy(renames["TimingIn"]).optional(),
            "audits": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "fullPageScreenshot": t.struct({"_": t.string().optional()}).optional(),
            "stackPacks": t.array(t.proxy(renames["StackPackIn"])).optional(),
            "mainDocumentUrl": t.string().optional(),
            "finalUrl": t.string().optional(),
            "configSettings": t.proxy(renames["ConfigSettingsIn"]).optional(),
            "finalDisplayedUrl": t.string().optional(),
            "lighthouseVersion": t.string().optional(),
            "i18n": t.proxy(renames["I18nIn"]).optional(),
            "entities": t.array(t.proxy(renames["LhrEntityIn"])).optional(),
            "categoryGroups": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LighthouseResultV5In"])
    types["LighthouseResultV5Out"] = t.struct(
        {
            "requestedUrl": t.string().optional(),
            "runWarnings": t.array(t.struct({"_": t.string().optional()})).optional(),
            "fetchTime": t.string().optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "userAgent": t.string().optional(),
            "runtimeError": t.proxy(renames["RuntimeErrorOut"]).optional(),
            "timing": t.proxy(renames["TimingOut"]).optional(),
            "audits": t.struct({"_": t.string().optional()}).optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "fullPageScreenshot": t.struct({"_": t.string().optional()}).optional(),
            "stackPacks": t.array(t.proxy(renames["StackPackOut"])).optional(),
            "mainDocumentUrl": t.string().optional(),
            "finalUrl": t.string().optional(),
            "configSettings": t.proxy(renames["ConfigSettingsOut"]).optional(),
            "finalDisplayedUrl": t.string().optional(),
            "lighthouseVersion": t.string().optional(),
            "i18n": t.proxy(renames["I18nOut"]).optional(),
            "entities": t.array(t.proxy(renames["LhrEntityOut"])).optional(),
            "categoryGroups": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseResultV5Out"])
    types["UserPageLoadMetricV5In"] = t.struct(
        {
            "distributions": t.array(t.proxy(renames["BucketIn"])).optional(),
            "metricId": t.string().optional(),
            "percentile": t.integer().optional(),
            "median": t.integer().optional(),
            "category": t.string().optional(),
            "formFactor": t.string().optional(),
        }
    ).named(renames["UserPageLoadMetricV5In"])
    types["UserPageLoadMetricV5Out"] = t.struct(
        {
            "distributions": t.array(t.proxy(renames["BucketOut"])).optional(),
            "metricId": t.string().optional(),
            "percentile": t.integer().optional(),
            "median": t.integer().optional(),
            "category": t.string().optional(),
            "formFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPageLoadMetricV5Out"])
    types["PagespeedApiLoadingExperienceV5In"] = t.struct(
        {
            "initial_url": t.string().optional(),
            "origin_fallback": t.boolean().optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "overall_category": t.string().optional(),
        }
    ).named(renames["PagespeedApiLoadingExperienceV5In"])
    types["PagespeedApiLoadingExperienceV5Out"] = t.struct(
        {
            "initial_url": t.string().optional(),
            "origin_fallback": t.boolean().optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "overall_category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedApiLoadingExperienceV5Out"])
    types["AuditRefsIn"] = t.struct(
        {
            "acronym": t.string().optional(),
            "weight": t.number().optional(),
            "relevantAudits": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "group": t.string().optional(),
        }
    ).named(renames["AuditRefsIn"])
    types["AuditRefsOut"] = t.struct(
        {
            "acronym": t.string().optional(),
            "weight": t.number().optional(),
            "relevantAudits": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "group": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditRefsOut"])
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
    types["LighthouseCategoryV5In"] = t.struct(
        {
            "description": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "manualDescription": t.string().optional(),
            "auditRefs": t.array(t.proxy(renames["AuditRefsIn"])).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["LighthouseCategoryV5In"])
    types["LighthouseCategoryV5Out"] = t.struct(
        {
            "description": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "manualDescription": t.string().optional(),
            "auditRefs": t.array(t.proxy(renames["AuditRefsOut"])).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseCategoryV5Out"])
    types["RendererFormattedStringsIn"] = t.struct(
        {
            "dropdownViewer": t.string().optional(),
            "footerIssue": t.string().optional(),
            "opportunityResourceColumnLabel": t.string().optional(),
            "lsPerformanceCategoryDescription": t.string().optional(),
            "dropdownPrintSummary": t.string().optional(),
            "dropdownSaveJSON": t.string().optional(),
            "runtimeSettingsFetchTime": t.string().optional(),
            "throttlingProvided": t.string().optional(),
            "errorLabel": t.string().optional(),
            "runtimeSettingsNetworkThrottling": t.string().optional(),
            "runtimeSettingsChannel": t.string().optional(),
            "warningHeader": t.string().optional(),
            "dropdownPrintExpanded": t.string().optional(),
            "toplevelWarningsMessage": t.string().optional(),
            "auditGroupExpandTooltip": t.string().optional(),
            "runtimeSettingsUANetwork": t.string().optional(),
            "crcInitialNavigation": t.string().optional(),
            "varianceDisclaimer": t.string().optional(),
            "opportunitySavingsColumnLabel": t.string().optional(),
            "runtimeUnknown": t.string().optional(),
            "dropdownCopyJSON": t.string().optional(),
            "runtimeSettingsAxeVersion": t.string().optional(),
            "warningAuditsGroupTitle": t.string().optional(),
            "runtimeNoEmulation": t.string().optional(),
            "runtimeMobileEmulation": t.string().optional(),
            "dropdownDarkTheme": t.string().optional(),
            "labDataTitle": t.string().optional(),
            "runtimeSettingsCPUThrottling": t.string().optional(),
            "runtimeSettingsUrl": t.string().optional(),
            "runtimeSettingsDevice": t.string().optional(),
            "errorMissingAuditInfo": t.string().optional(),
            "runtimeDesktopEmulation": t.string().optional(),
            "dropdownSaveHTML": t.string().optional(),
            "dropdownSaveGist": t.string().optional(),
            "crcLongestDurationLabel": t.string().optional(),
            "snippetCollapseButtonLabel": t.string().optional(),
            "viewTreemapLabel": t.string().optional(),
            "notApplicableAuditsGroupTitle": t.string().optional(),
            "runtimeSettingsUA": t.string().optional(),
            "showRelevantAudits": t.string().optional(),
            "scorescaleLabel": t.string().optional(),
            "runtimeSettingsTitle": t.string().optional(),
            "snippetExpandButtonLabel": t.string().optional(),
            "thirdPartyResourcesLabel": t.string().optional(),
            "passedAuditsGroupTitle": t.string().optional(),
            "calculatorLink": t.string().optional(),
            "manualAuditsGroupTitle": t.string().optional(),
            "runtimeSettingsBenchmark": t.string().optional(),
        }
    ).named(renames["RendererFormattedStringsIn"])
    types["RendererFormattedStringsOut"] = t.struct(
        {
            "dropdownViewer": t.string().optional(),
            "footerIssue": t.string().optional(),
            "opportunityResourceColumnLabel": t.string().optional(),
            "lsPerformanceCategoryDescription": t.string().optional(),
            "dropdownPrintSummary": t.string().optional(),
            "dropdownSaveJSON": t.string().optional(),
            "runtimeSettingsFetchTime": t.string().optional(),
            "throttlingProvided": t.string().optional(),
            "errorLabel": t.string().optional(),
            "runtimeSettingsNetworkThrottling": t.string().optional(),
            "runtimeSettingsChannel": t.string().optional(),
            "warningHeader": t.string().optional(),
            "dropdownPrintExpanded": t.string().optional(),
            "toplevelWarningsMessage": t.string().optional(),
            "auditGroupExpandTooltip": t.string().optional(),
            "runtimeSettingsUANetwork": t.string().optional(),
            "crcInitialNavigation": t.string().optional(),
            "varianceDisclaimer": t.string().optional(),
            "opportunitySavingsColumnLabel": t.string().optional(),
            "runtimeUnknown": t.string().optional(),
            "dropdownCopyJSON": t.string().optional(),
            "runtimeSettingsAxeVersion": t.string().optional(),
            "warningAuditsGroupTitle": t.string().optional(),
            "runtimeNoEmulation": t.string().optional(),
            "runtimeMobileEmulation": t.string().optional(),
            "dropdownDarkTheme": t.string().optional(),
            "labDataTitle": t.string().optional(),
            "runtimeSettingsCPUThrottling": t.string().optional(),
            "runtimeSettingsUrl": t.string().optional(),
            "runtimeSettingsDevice": t.string().optional(),
            "errorMissingAuditInfo": t.string().optional(),
            "runtimeDesktopEmulation": t.string().optional(),
            "dropdownSaveHTML": t.string().optional(),
            "dropdownSaveGist": t.string().optional(),
            "crcLongestDurationLabel": t.string().optional(),
            "snippetCollapseButtonLabel": t.string().optional(),
            "viewTreemapLabel": t.string().optional(),
            "notApplicableAuditsGroupTitle": t.string().optional(),
            "runtimeSettingsUA": t.string().optional(),
            "showRelevantAudits": t.string().optional(),
            "scorescaleLabel": t.string().optional(),
            "runtimeSettingsTitle": t.string().optional(),
            "snippetExpandButtonLabel": t.string().optional(),
            "thirdPartyResourcesLabel": t.string().optional(),
            "passedAuditsGroupTitle": t.string().optional(),
            "calculatorLink": t.string().optional(),
            "manualAuditsGroupTitle": t.string().optional(),
            "runtimeSettingsBenchmark": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RendererFormattedStringsOut"])
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
    types["PagespeedVersionIn"] = t.struct(
        {"minor": t.string().optional(), "major": t.string().optional()}
    ).named(renames["PagespeedVersionIn"])
    types["PagespeedVersionOut"] = t.struct(
        {
            "minor": t.string().optional(),
            "major": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedVersionOut"])
    types["LighthouseAuditResultV5In"] = t.struct(
        {
            "scoreDisplayMode": t.string().optional(),
            "displayValue": t.string().optional(),
            "id": t.string().optional(),
            "title": t.string().optional(),
            "numericUnit": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
            "numericValue": t.number().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "warnings": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "explanation": t.string().optional(),
        }
    ).named(renames["LighthouseAuditResultV5In"])
    types["LighthouseAuditResultV5Out"] = t.struct(
        {
            "scoreDisplayMode": t.string().optional(),
            "displayValue": t.string().optional(),
            "id": t.string().optional(),
            "title": t.string().optional(),
            "numericUnit": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
            "numericValue": t.number().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "warnings": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "explanation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseAuditResultV5Out"])
    types["LhrEntityIn"] = t.struct(
        {
            "name": t.string(),
            "origins": t.array(t.string()),
            "isFirstParty": t.boolean().optional(),
            "isUnrecognized": t.boolean().optional(),
            "category": t.string().optional(),
            "homepage": t.string().optional(),
        }
    ).named(renames["LhrEntityIn"])
    types["LhrEntityOut"] = t.struct(
        {
            "name": t.string(),
            "origins": t.array(t.string()),
            "isFirstParty": t.boolean().optional(),
            "isUnrecognized": t.boolean().optional(),
            "category": t.string().optional(),
            "homepage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LhrEntityOut"])
    types["CategoryGroupV5In"] = t.struct(
        {"title": t.string().optional(), "description": t.string().optional()}
    ).named(renames["CategoryGroupV5In"])
    types["CategoryGroupV5Out"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoryGroupV5Out"])
    types["EnvironmentIn"] = t.struct(
        {
            "benchmarkIndex": t.number().optional(),
            "credits": t.struct({"_": t.string().optional()}).optional(),
            "networkUserAgent": t.string().optional(),
            "hostUserAgent": t.string().optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "benchmarkIndex": t.number().optional(),
            "credits": t.struct({"_": t.string().optional()}).optional(),
            "networkUserAgent": t.string().optional(),
            "hostUserAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])

    functions = {}
    functions["pagespeedapiRunpagespeed"] = pagespeedonline.get(
        "pagespeedonline/v5/runPagespeed",
        t.struct(
            {
                "url": t.string(),
                "captchaToken": t.string().optional(),
                "utm_campaign": t.string().optional(),
                "locale": t.string().optional(),
                "strategy": t.string().optional(),
                "category": t.string().optional(),
                "utm_source": t.string().optional(),
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
