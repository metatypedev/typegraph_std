from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_pagespeedonline():
    pagespeedonline = HTTPRuntime("https://pagespeedonline.googleapis.com/")

    renames = {
        "ErrorResponse": "_pagespeedonline_1_ErrorResponse",
        "LighthouseAuditResultV5In": "_pagespeedonline_2_LighthouseAuditResultV5In",
        "LighthouseAuditResultV5Out": "_pagespeedonline_3_LighthouseAuditResultV5Out",
        "PagespeedApiPagespeedResponseV5In": "_pagespeedonline_4_PagespeedApiPagespeedResponseV5In",
        "PagespeedApiPagespeedResponseV5Out": "_pagespeedonline_5_PagespeedApiPagespeedResponseV5Out",
        "I18nIn": "_pagespeedonline_6_I18nIn",
        "I18nOut": "_pagespeedonline_7_I18nOut",
        "LighthouseResultV5In": "_pagespeedonline_8_LighthouseResultV5In",
        "LighthouseResultV5Out": "_pagespeedonline_9_LighthouseResultV5Out",
        "RuntimeErrorIn": "_pagespeedonline_10_RuntimeErrorIn",
        "RuntimeErrorOut": "_pagespeedonline_11_RuntimeErrorOut",
        "PagespeedApiLoadingExperienceV5In": "_pagespeedonline_12_PagespeedApiLoadingExperienceV5In",
        "PagespeedApiLoadingExperienceV5Out": "_pagespeedonline_13_PagespeedApiLoadingExperienceV5Out",
        "CategoryGroupV5In": "_pagespeedonline_14_CategoryGroupV5In",
        "CategoryGroupV5Out": "_pagespeedonline_15_CategoryGroupV5Out",
        "ConfigSettingsIn": "_pagespeedonline_16_ConfigSettingsIn",
        "ConfigSettingsOut": "_pagespeedonline_17_ConfigSettingsOut",
        "TimingIn": "_pagespeedonline_18_TimingIn",
        "TimingOut": "_pagespeedonline_19_TimingOut",
        "EnvironmentIn": "_pagespeedonline_20_EnvironmentIn",
        "EnvironmentOut": "_pagespeedonline_21_EnvironmentOut",
        "PagespeedVersionIn": "_pagespeedonline_22_PagespeedVersionIn",
        "PagespeedVersionOut": "_pagespeedonline_23_PagespeedVersionOut",
        "BucketIn": "_pagespeedonline_24_BucketIn",
        "BucketOut": "_pagespeedonline_25_BucketOut",
        "LighthouseCategoryV5In": "_pagespeedonline_26_LighthouseCategoryV5In",
        "LighthouseCategoryV5Out": "_pagespeedonline_27_LighthouseCategoryV5Out",
        "CategoriesIn": "_pagespeedonline_28_CategoriesIn",
        "CategoriesOut": "_pagespeedonline_29_CategoriesOut",
        "StackPackIn": "_pagespeedonline_30_StackPackIn",
        "StackPackOut": "_pagespeedonline_31_StackPackOut",
        "LhrEntityIn": "_pagespeedonline_32_LhrEntityIn",
        "LhrEntityOut": "_pagespeedonline_33_LhrEntityOut",
        "UserPageLoadMetricV5In": "_pagespeedonline_34_UserPageLoadMetricV5In",
        "UserPageLoadMetricV5Out": "_pagespeedonline_35_UserPageLoadMetricV5Out",
        "RendererFormattedStringsIn": "_pagespeedonline_36_RendererFormattedStringsIn",
        "RendererFormattedStringsOut": "_pagespeedonline_37_RendererFormattedStringsOut",
        "AuditRefsIn": "_pagespeedonline_38_AuditRefsIn",
        "AuditRefsOut": "_pagespeedonline_39_AuditRefsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LighthouseAuditResultV5In"] = t.struct(
        {
            "displayValue": t.string().optional(),
            "numericUnit": t.string().optional(),
            "id": t.string().optional(),
            "scoreDisplayMode": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
            "numericValue": t.number().optional(),
            "explanation": t.string().optional(),
            "title": t.string().optional(),
            "warnings": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LighthouseAuditResultV5In"])
    types["LighthouseAuditResultV5Out"] = t.struct(
        {
            "displayValue": t.string().optional(),
            "numericUnit": t.string().optional(),
            "id": t.string().optional(),
            "scoreDisplayMode": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "details": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
            "numericValue": t.number().optional(),
            "explanation": t.string().optional(),
            "title": t.string().optional(),
            "warnings": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseAuditResultV5Out"])
    types["PagespeedApiPagespeedResponseV5In"] = t.struct(
        {
            "lighthouseResult": t.proxy(renames["LighthouseResultV5In"]).optional(),
            "analysisUTCTimestamp": t.string().optional(),
            "version": t.proxy(renames["PagespeedVersionIn"]).optional(),
            "kind": t.string().optional(),
            "captchaResult": t.string().optional(),
            "originLoadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5In"]
            ).optional(),
            "loadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5In"]
            ).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PagespeedApiPagespeedResponseV5In"])
    types["PagespeedApiPagespeedResponseV5Out"] = t.struct(
        {
            "lighthouseResult": t.proxy(renames["LighthouseResultV5Out"]).optional(),
            "analysisUTCTimestamp": t.string().optional(),
            "version": t.proxy(renames["PagespeedVersionOut"]).optional(),
            "kind": t.string().optional(),
            "captchaResult": t.string().optional(),
            "originLoadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5Out"]
            ).optional(),
            "loadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5Out"]
            ).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedApiPagespeedResponseV5Out"])
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
    types["LighthouseResultV5In"] = t.struct(
        {
            "runtimeError": t.proxy(renames["RuntimeErrorIn"]).optional(),
            "fetchTime": t.string().optional(),
            "categoryGroups": t.struct({"_": t.string().optional()}).optional(),
            "audits": t.struct({"_": t.string().optional()}).optional(),
            "entities": t.array(t.proxy(renames["LhrEntityIn"])).optional(),
            "i18n": t.proxy(renames["I18nIn"]).optional(),
            "userAgent": t.string().optional(),
            "runWarnings": t.array(t.struct({"_": t.string().optional()})).optional(),
            "timing": t.proxy(renames["TimingIn"]).optional(),
            "lighthouseVersion": t.string().optional(),
            "finalUrl": t.string().optional(),
            "configSettings": t.proxy(renames["ConfigSettingsIn"]).optional(),
            "mainDocumentUrl": t.string().optional(),
            "fullPageScreenshot": t.struct({"_": t.string().optional()}).optional(),
            "stackPacks": t.array(t.proxy(renames["StackPackIn"])).optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "finalDisplayedUrl": t.string().optional(),
            "requestedUrl": t.string().optional(),
        }
    ).named(renames["LighthouseResultV5In"])
    types["LighthouseResultV5Out"] = t.struct(
        {
            "runtimeError": t.proxy(renames["RuntimeErrorOut"]).optional(),
            "fetchTime": t.string().optional(),
            "categoryGroups": t.struct({"_": t.string().optional()}).optional(),
            "audits": t.struct({"_": t.string().optional()}).optional(),
            "entities": t.array(t.proxy(renames["LhrEntityOut"])).optional(),
            "i18n": t.proxy(renames["I18nOut"]).optional(),
            "userAgent": t.string().optional(),
            "runWarnings": t.array(t.struct({"_": t.string().optional()})).optional(),
            "timing": t.proxy(renames["TimingOut"]).optional(),
            "lighthouseVersion": t.string().optional(),
            "finalUrl": t.string().optional(),
            "configSettings": t.proxy(renames["ConfigSettingsOut"]).optional(),
            "mainDocumentUrl": t.string().optional(),
            "fullPageScreenshot": t.struct({"_": t.string().optional()}).optional(),
            "stackPacks": t.array(t.proxy(renames["StackPackOut"])).optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "finalDisplayedUrl": t.string().optional(),
            "requestedUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseResultV5Out"])
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
    types["PagespeedApiLoadingExperienceV5In"] = t.struct(
        {
            "overall_category": t.string().optional(),
            "id": t.string().optional(),
            "origin_fallback": t.boolean().optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "initial_url": t.string().optional(),
        }
    ).named(renames["PagespeedApiLoadingExperienceV5In"])
    types["PagespeedApiLoadingExperienceV5Out"] = t.struct(
        {
            "overall_category": t.string().optional(),
            "id": t.string().optional(),
            "origin_fallback": t.boolean().optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "initial_url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedApiLoadingExperienceV5Out"])
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
            "onlyCategories": t.struct({"_": t.string().optional()}).optional(),
            "emulatedFormFactor": t.string().optional(),
            "locale": t.string().optional(),
            "channel": t.string().optional(),
            "formFactor": t.string().optional(),
        }
    ).named(renames["ConfigSettingsIn"])
    types["ConfigSettingsOut"] = t.struct(
        {
            "onlyCategories": t.struct({"_": t.string().optional()}).optional(),
            "emulatedFormFactor": t.string().optional(),
            "locale": t.string().optional(),
            "channel": t.string().optional(),
            "formFactor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigSettingsOut"])
    types["TimingIn"] = t.struct({"total": t.number().optional()}).named(
        renames["TimingIn"]
    )
    types["TimingOut"] = t.struct(
        {
            "total": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimingOut"])
    types["EnvironmentIn"] = t.struct(
        {
            "networkUserAgent": t.string().optional(),
            "credits": t.struct({"_": t.string().optional()}).optional(),
            "benchmarkIndex": t.number().optional(),
            "hostUserAgent": t.string().optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "networkUserAgent": t.string().optional(),
            "credits": t.struct({"_": t.string().optional()}).optional(),
            "benchmarkIndex": t.number().optional(),
            "hostUserAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
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
    types["LighthouseCategoryV5In"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "manualDescription": t.string().optional(),
            "id": t.string().optional(),
            "auditRefs": t.array(t.proxy(renames["AuditRefsIn"])).optional(),
        }
    ).named(renames["LighthouseCategoryV5In"])
    types["LighthouseCategoryV5Out"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "manualDescription": t.string().optional(),
            "id": t.string().optional(),
            "auditRefs": t.array(t.proxy(renames["AuditRefsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseCategoryV5Out"])
    types["CategoriesIn"] = t.struct(
        {
            "accessibility": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "best-practices": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "pwa": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "performance": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "seo": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
        }
    ).named(renames["CategoriesIn"])
    types["CategoriesOut"] = t.struct(
        {
            "accessibility": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "best-practices": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "pwa": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "performance": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "seo": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoriesOut"])
    types["StackPackIn"] = t.struct(
        {
            "title": t.string().optional(),
            "descriptions": t.struct({"_": t.string().optional()}).optional(),
            "iconDataURL": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["StackPackIn"])
    types["StackPackOut"] = t.struct(
        {
            "title": t.string().optional(),
            "descriptions": t.struct({"_": t.string().optional()}).optional(),
            "iconDataURL": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackPackOut"])
    types["LhrEntityIn"] = t.struct(
        {
            "homepage": t.string().optional(),
            "origins": t.array(t.string()),
            "category": t.string().optional(),
            "isFirstParty": t.boolean().optional(),
            "isUnrecognized": t.boolean().optional(),
            "name": t.string(),
        }
    ).named(renames["LhrEntityIn"])
    types["LhrEntityOut"] = t.struct(
        {
            "homepage": t.string().optional(),
            "origins": t.array(t.string()),
            "category": t.string().optional(),
            "isFirstParty": t.boolean().optional(),
            "isUnrecognized": t.boolean().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LhrEntityOut"])
    types["UserPageLoadMetricV5In"] = t.struct(
        {
            "distributions": t.array(t.proxy(renames["BucketIn"])).optional(),
            "formFactor": t.string().optional(),
            "median": t.integer().optional(),
            "category": t.string().optional(),
            "metricId": t.string().optional(),
            "percentile": t.integer().optional(),
        }
    ).named(renames["UserPageLoadMetricV5In"])
    types["UserPageLoadMetricV5Out"] = t.struct(
        {
            "distributions": t.array(t.proxy(renames["BucketOut"])).optional(),
            "formFactor": t.string().optional(),
            "median": t.integer().optional(),
            "category": t.string().optional(),
            "metricId": t.string().optional(),
            "percentile": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPageLoadMetricV5Out"])
    types["RendererFormattedStringsIn"] = t.struct(
        {
            "dropdownSaveJSON": t.string().optional(),
            "runtimeSettingsNetworkThrottling": t.string().optional(),
            "snippetExpandButtonLabel": t.string().optional(),
            "runtimeNoEmulation": t.string().optional(),
            "dropdownPrintSummary": t.string().optional(),
            "opportunityResourceColumnLabel": t.string().optional(),
            "crcInitialNavigation": t.string().optional(),
            "warningHeader": t.string().optional(),
            "snippetCollapseButtonLabel": t.string().optional(),
            "runtimeSettingsAxeVersion": t.string().optional(),
            "runtimeSettingsUANetwork": t.string().optional(),
            "scorescaleLabel": t.string().optional(),
            "dropdownDarkTheme": t.string().optional(),
            "runtimeSettingsUA": t.string().optional(),
            "dropdownSaveHTML": t.string().optional(),
            "labDataTitle": t.string().optional(),
            "auditGroupExpandTooltip": t.string().optional(),
            "notApplicableAuditsGroupTitle": t.string().optional(),
            "errorLabel": t.string().optional(),
            "warningAuditsGroupTitle": t.string().optional(),
            "dropdownViewer": t.string().optional(),
            "viewTreemapLabel": t.string().optional(),
            "runtimeSettingsBenchmark": t.string().optional(),
            "varianceDisclaimer": t.string().optional(),
            "runtimeDesktopEmulation": t.string().optional(),
            "toplevelWarningsMessage": t.string().optional(),
            "thirdPartyResourcesLabel": t.string().optional(),
            "runtimeMobileEmulation": t.string().optional(),
            "opportunitySavingsColumnLabel": t.string().optional(),
            "runtimeSettingsDevice": t.string().optional(),
            "runtimeSettingsFetchTime": t.string().optional(),
            "runtimeSettingsUrl": t.string().optional(),
            "dropdownPrintExpanded": t.string().optional(),
            "showRelevantAudits": t.string().optional(),
            "passedAuditsGroupTitle": t.string().optional(),
            "calculatorLink": t.string().optional(),
            "runtimeUnknown": t.string().optional(),
            "lsPerformanceCategoryDescription": t.string().optional(),
            "throttlingProvided": t.string().optional(),
            "footerIssue": t.string().optional(),
            "crcLongestDurationLabel": t.string().optional(),
            "runtimeSettingsChannel": t.string().optional(),
            "runtimeSettingsTitle": t.string().optional(),
            "runtimeSettingsCPUThrottling": t.string().optional(),
            "dropdownSaveGist": t.string().optional(),
            "errorMissingAuditInfo": t.string().optional(),
            "manualAuditsGroupTitle": t.string().optional(),
            "dropdownCopyJSON": t.string().optional(),
        }
    ).named(renames["RendererFormattedStringsIn"])
    types["RendererFormattedStringsOut"] = t.struct(
        {
            "dropdownSaveJSON": t.string().optional(),
            "runtimeSettingsNetworkThrottling": t.string().optional(),
            "snippetExpandButtonLabel": t.string().optional(),
            "runtimeNoEmulation": t.string().optional(),
            "dropdownPrintSummary": t.string().optional(),
            "opportunityResourceColumnLabel": t.string().optional(),
            "crcInitialNavigation": t.string().optional(),
            "warningHeader": t.string().optional(),
            "snippetCollapseButtonLabel": t.string().optional(),
            "runtimeSettingsAxeVersion": t.string().optional(),
            "runtimeSettingsUANetwork": t.string().optional(),
            "scorescaleLabel": t.string().optional(),
            "dropdownDarkTheme": t.string().optional(),
            "runtimeSettingsUA": t.string().optional(),
            "dropdownSaveHTML": t.string().optional(),
            "labDataTitle": t.string().optional(),
            "auditGroupExpandTooltip": t.string().optional(),
            "notApplicableAuditsGroupTitle": t.string().optional(),
            "errorLabel": t.string().optional(),
            "warningAuditsGroupTitle": t.string().optional(),
            "dropdownViewer": t.string().optional(),
            "viewTreemapLabel": t.string().optional(),
            "runtimeSettingsBenchmark": t.string().optional(),
            "varianceDisclaimer": t.string().optional(),
            "runtimeDesktopEmulation": t.string().optional(),
            "toplevelWarningsMessage": t.string().optional(),
            "thirdPartyResourcesLabel": t.string().optional(),
            "runtimeMobileEmulation": t.string().optional(),
            "opportunitySavingsColumnLabel": t.string().optional(),
            "runtimeSettingsDevice": t.string().optional(),
            "runtimeSettingsFetchTime": t.string().optional(),
            "runtimeSettingsUrl": t.string().optional(),
            "dropdownPrintExpanded": t.string().optional(),
            "showRelevantAudits": t.string().optional(),
            "passedAuditsGroupTitle": t.string().optional(),
            "calculatorLink": t.string().optional(),
            "runtimeUnknown": t.string().optional(),
            "lsPerformanceCategoryDescription": t.string().optional(),
            "throttlingProvided": t.string().optional(),
            "footerIssue": t.string().optional(),
            "crcLongestDurationLabel": t.string().optional(),
            "runtimeSettingsChannel": t.string().optional(),
            "runtimeSettingsTitle": t.string().optional(),
            "runtimeSettingsCPUThrottling": t.string().optional(),
            "dropdownSaveGist": t.string().optional(),
            "errorMissingAuditInfo": t.string().optional(),
            "manualAuditsGroupTitle": t.string().optional(),
            "dropdownCopyJSON": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RendererFormattedStringsOut"])
    types["AuditRefsIn"] = t.struct(
        {
            "acronym": t.string().optional(),
            "relevantAudits": t.array(t.string()).optional(),
            "weight": t.number().optional(),
            "group": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AuditRefsIn"])
    types["AuditRefsOut"] = t.struct(
        {
            "acronym": t.string().optional(),
            "relevantAudits": t.array(t.string()).optional(),
            "weight": t.number().optional(),
            "group": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditRefsOut"])

    functions = {}
    functions["pagespeedapiRunpagespeed"] = pagespeedonline.get(
        "pagespeedonline/v5/runPagespeed",
        t.struct(
            {
                "url": t.string(),
                "strategy": t.string().optional(),
                "locale": t.string().optional(),
                "category": t.string().optional(),
                "utm_campaign": t.string().optional(),
                "utm_source": t.string().optional(),
                "captchaToken": t.string().optional(),
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
