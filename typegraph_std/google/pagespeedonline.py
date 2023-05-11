from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_pagespeedonline() -> Import:
    pagespeedonline = HTTPRuntime("https://pagespeedonline.googleapis.com/")

    renames = {
        "ErrorResponse": "_pagespeedonline_1_ErrorResponse",
        "CategoryGroupV5In": "_pagespeedonline_2_CategoryGroupV5In",
        "CategoryGroupV5Out": "_pagespeedonline_3_CategoryGroupV5Out",
        "LighthouseResultV5In": "_pagespeedonline_4_LighthouseResultV5In",
        "LighthouseResultV5Out": "_pagespeedonline_5_LighthouseResultV5Out",
        "PagespeedApiLoadingExperienceV5In": "_pagespeedonline_6_PagespeedApiLoadingExperienceV5In",
        "PagespeedApiLoadingExperienceV5Out": "_pagespeedonline_7_PagespeedApiLoadingExperienceV5Out",
        "EnvironmentIn": "_pagespeedonline_8_EnvironmentIn",
        "EnvironmentOut": "_pagespeedonline_9_EnvironmentOut",
        "CategoriesIn": "_pagespeedonline_10_CategoriesIn",
        "CategoriesOut": "_pagespeedonline_11_CategoriesOut",
        "LighthouseCategoryV5In": "_pagespeedonline_12_LighthouseCategoryV5In",
        "LighthouseCategoryV5Out": "_pagespeedonline_13_LighthouseCategoryV5Out",
        "ConfigSettingsIn": "_pagespeedonline_14_ConfigSettingsIn",
        "ConfigSettingsOut": "_pagespeedonline_15_ConfigSettingsOut",
        "UserPageLoadMetricV5In": "_pagespeedonline_16_UserPageLoadMetricV5In",
        "UserPageLoadMetricV5Out": "_pagespeedonline_17_UserPageLoadMetricV5Out",
        "AuditRefsIn": "_pagespeedonline_18_AuditRefsIn",
        "AuditRefsOut": "_pagespeedonline_19_AuditRefsOut",
        "LighthouseAuditResultV5In": "_pagespeedonline_20_LighthouseAuditResultV5In",
        "LighthouseAuditResultV5Out": "_pagespeedonline_21_LighthouseAuditResultV5Out",
        "PagespeedApiPagespeedResponseV5In": "_pagespeedonline_22_PagespeedApiPagespeedResponseV5In",
        "PagespeedApiPagespeedResponseV5Out": "_pagespeedonline_23_PagespeedApiPagespeedResponseV5Out",
        "RendererFormattedStringsIn": "_pagespeedonline_24_RendererFormattedStringsIn",
        "RendererFormattedStringsOut": "_pagespeedonline_25_RendererFormattedStringsOut",
        "RuntimeErrorIn": "_pagespeedonline_26_RuntimeErrorIn",
        "RuntimeErrorOut": "_pagespeedonline_27_RuntimeErrorOut",
        "TimingIn": "_pagespeedonline_28_TimingIn",
        "TimingOut": "_pagespeedonline_29_TimingOut",
        "PagespeedVersionIn": "_pagespeedonline_30_PagespeedVersionIn",
        "PagespeedVersionOut": "_pagespeedonline_31_PagespeedVersionOut",
        "I18nIn": "_pagespeedonline_32_I18nIn",
        "I18nOut": "_pagespeedonline_33_I18nOut",
        "BucketIn": "_pagespeedonline_34_BucketIn",
        "BucketOut": "_pagespeedonline_35_BucketOut",
        "LhrEntityIn": "_pagespeedonline_36_LhrEntityIn",
        "LhrEntityOut": "_pagespeedonline_37_LhrEntityOut",
        "StackPackIn": "_pagespeedonline_38_StackPackIn",
        "StackPackOut": "_pagespeedonline_39_StackPackOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["LighthouseResultV5In"] = t.struct(
        {
            "audits": t.struct({"_": t.string().optional()}).optional(),
            "runWarnings": t.array(t.struct({"_": t.string().optional()})).optional(),
            "configSettings": t.proxy(renames["ConfigSettingsIn"]).optional(),
            "lighthouseVersion": t.string().optional(),
            "fullPageScreenshot": t.struct({"_": t.string().optional()}).optional(),
            "entities": t.array(t.proxy(renames["LhrEntityIn"])).optional(),
            "finalUrl": t.string().optional(),
            "categories": t.proxy(renames["CategoriesIn"]).optional(),
            "finalDisplayedUrl": t.string().optional(),
            "requestedUrl": t.string().optional(),
            "timing": t.proxy(renames["TimingIn"]).optional(),
            "environment": t.proxy(renames["EnvironmentIn"]).optional(),
            "i18n": t.proxy(renames["I18nIn"]).optional(),
            "fetchTime": t.string().optional(),
            "categoryGroups": t.struct({"_": t.string().optional()}).optional(),
            "stackPacks": t.array(t.proxy(renames["StackPackIn"])).optional(),
            "runtimeError": t.proxy(renames["RuntimeErrorIn"]).optional(),
            "mainDocumentUrl": t.string().optional(),
            "userAgent": t.string().optional(),
        }
    ).named(renames["LighthouseResultV5In"])
    types["LighthouseResultV5Out"] = t.struct(
        {
            "audits": t.struct({"_": t.string().optional()}).optional(),
            "runWarnings": t.array(t.struct({"_": t.string().optional()})).optional(),
            "configSettings": t.proxy(renames["ConfigSettingsOut"]).optional(),
            "lighthouseVersion": t.string().optional(),
            "fullPageScreenshot": t.struct({"_": t.string().optional()}).optional(),
            "entities": t.array(t.proxy(renames["LhrEntityOut"])).optional(),
            "finalUrl": t.string().optional(),
            "categories": t.proxy(renames["CategoriesOut"]).optional(),
            "finalDisplayedUrl": t.string().optional(),
            "requestedUrl": t.string().optional(),
            "timing": t.proxy(renames["TimingOut"]).optional(),
            "environment": t.proxy(renames["EnvironmentOut"]).optional(),
            "i18n": t.proxy(renames["I18nOut"]).optional(),
            "fetchTime": t.string().optional(),
            "categoryGroups": t.struct({"_": t.string().optional()}).optional(),
            "stackPacks": t.array(t.proxy(renames["StackPackOut"])).optional(),
            "runtimeError": t.proxy(renames["RuntimeErrorOut"]).optional(),
            "mainDocumentUrl": t.string().optional(),
            "userAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseResultV5Out"])
    types["PagespeedApiLoadingExperienceV5In"] = t.struct(
        {
            "initial_url": t.string().optional(),
            "origin_fallback": t.boolean().optional(),
            "overall_category": t.string().optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["PagespeedApiLoadingExperienceV5In"])
    types["PagespeedApiLoadingExperienceV5Out"] = t.struct(
        {
            "initial_url": t.string().optional(),
            "origin_fallback": t.boolean().optional(),
            "overall_category": t.string().optional(),
            "metrics": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedApiLoadingExperienceV5Out"])
    types["EnvironmentIn"] = t.struct(
        {
            "hostUserAgent": t.string().optional(),
            "benchmarkIndex": t.number().optional(),
            "networkUserAgent": t.string().optional(),
            "credits": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["EnvironmentIn"])
    types["EnvironmentOut"] = t.struct(
        {
            "hostUserAgent": t.string().optional(),
            "benchmarkIndex": t.number().optional(),
            "networkUserAgent": t.string().optional(),
            "credits": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnvironmentOut"])
    types["CategoriesIn"] = t.struct(
        {
            "pwa": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "accessibility": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "seo": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "best-practices": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
            "performance": t.proxy(renames["LighthouseCategoryV5In"]).optional(),
        }
    ).named(renames["CategoriesIn"])
    types["CategoriesOut"] = t.struct(
        {
            "pwa": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "accessibility": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "seo": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "best-practices": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "performance": t.proxy(renames["LighthouseCategoryV5Out"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CategoriesOut"])
    types["LighthouseCategoryV5In"] = t.struct(
        {
            "score": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "manualDescription": t.string().optional(),
            "auditRefs": t.array(t.proxy(renames["AuditRefsIn"])).optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["LighthouseCategoryV5In"])
    types["LighthouseCategoryV5Out"] = t.struct(
        {
            "score": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "manualDescription": t.string().optional(),
            "auditRefs": t.array(t.proxy(renames["AuditRefsOut"])).optional(),
            "description": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseCategoryV5Out"])
    types["ConfigSettingsIn"] = t.struct(
        {
            "locale": t.string().optional(),
            "emulatedFormFactor": t.string().optional(),
            "onlyCategories": t.struct({"_": t.string().optional()}).optional(),
            "formFactor": t.string().optional(),
            "channel": t.string().optional(),
        }
    ).named(renames["ConfigSettingsIn"])
    types["ConfigSettingsOut"] = t.struct(
        {
            "locale": t.string().optional(),
            "emulatedFormFactor": t.string().optional(),
            "onlyCategories": t.struct({"_": t.string().optional()}).optional(),
            "formFactor": t.string().optional(),
            "channel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigSettingsOut"])
    types["UserPageLoadMetricV5In"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "category": t.string().optional(),
            "percentile": t.integer().optional(),
            "median": t.integer().optional(),
            "distributions": t.array(t.proxy(renames["BucketIn"])).optional(),
            "metricId": t.string().optional(),
        }
    ).named(renames["UserPageLoadMetricV5In"])
    types["UserPageLoadMetricV5Out"] = t.struct(
        {
            "formFactor": t.string().optional(),
            "category": t.string().optional(),
            "percentile": t.integer().optional(),
            "median": t.integer().optional(),
            "distributions": t.array(t.proxy(renames["BucketOut"])).optional(),
            "metricId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserPageLoadMetricV5Out"])
    types["AuditRefsIn"] = t.struct(
        {
            "weight": t.number().optional(),
            "acronym": t.string().optional(),
            "group": t.string().optional(),
            "relevantAudits": t.array(t.string()).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AuditRefsIn"])
    types["AuditRefsOut"] = t.struct(
        {
            "weight": t.number().optional(),
            "acronym": t.string().optional(),
            "group": t.string().optional(),
            "relevantAudits": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditRefsOut"])
    types["LighthouseAuditResultV5In"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
            "id": t.string().optional(),
            "title": t.string().optional(),
            "warnings": t.struct({"_": t.string().optional()}).optional(),
            "numericUnit": t.string().optional(),
            "description": t.string().optional(),
            "displayValue": t.string().optional(),
            "explanation": t.string().optional(),
            "scoreDisplayMode": t.string().optional(),
            "numericValue": t.number().optional(),
        }
    ).named(renames["LighthouseAuditResultV5In"])
    types["LighthouseAuditResultV5Out"] = t.struct(
        {
            "details": t.struct({"_": t.string().optional()}).optional(),
            "score": t.struct({"_": t.string().optional()}).optional(),
            "errorMessage": t.string().optional(),
            "id": t.string().optional(),
            "title": t.string().optional(),
            "warnings": t.struct({"_": t.string().optional()}).optional(),
            "numericUnit": t.string().optional(),
            "description": t.string().optional(),
            "displayValue": t.string().optional(),
            "explanation": t.string().optional(),
            "scoreDisplayMode": t.string().optional(),
            "numericValue": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LighthouseAuditResultV5Out"])
    types["PagespeedApiPagespeedResponseV5In"] = t.struct(
        {
            "analysisUTCTimestamp": t.string().optional(),
            "lighthouseResult": t.proxy(renames["LighthouseResultV5In"]).optional(),
            "originLoadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5In"]
            ).optional(),
            "kind": t.string().optional(),
            "captchaResult": t.string().optional(),
            "id": t.string().optional(),
            "version": t.proxy(renames["PagespeedVersionIn"]).optional(),
            "loadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5In"]
            ).optional(),
        }
    ).named(renames["PagespeedApiPagespeedResponseV5In"])
    types["PagespeedApiPagespeedResponseV5Out"] = t.struct(
        {
            "analysisUTCTimestamp": t.string().optional(),
            "lighthouseResult": t.proxy(renames["LighthouseResultV5Out"]).optional(),
            "originLoadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5Out"]
            ).optional(),
            "kind": t.string().optional(),
            "captchaResult": t.string().optional(),
            "id": t.string().optional(),
            "version": t.proxy(renames["PagespeedVersionOut"]).optional(),
            "loadingExperience": t.proxy(
                renames["PagespeedApiLoadingExperienceV5Out"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PagespeedApiPagespeedResponseV5Out"])
    types["RendererFormattedStringsIn"] = t.struct(
        {
            "opportunitySavingsColumnLabel": t.string().optional(),
            "runtimeSettingsNetworkThrottling": t.string().optional(),
            "runtimeSettingsAxeVersion": t.string().optional(),
            "errorMissingAuditInfo": t.string().optional(),
            "dropdownCopyJSON": t.string().optional(),
            "manualAuditsGroupTitle": t.string().optional(),
            "throttlingProvided": t.string().optional(),
            "runtimeSettingsChannel": t.string().optional(),
            "runtimeSettingsUANetwork": t.string().optional(),
            "warningAuditsGroupTitle": t.string().optional(),
            "dropdownViewer": t.string().optional(),
            "showRelevantAudits": t.string().optional(),
            "runtimeSettingsUrl": t.string().optional(),
            "dropdownSaveJSON": t.string().optional(),
            "crcLongestDurationLabel": t.string().optional(),
            "footerIssue": t.string().optional(),
            "thirdPartyResourcesLabel": t.string().optional(),
            "runtimeSettingsCPUThrottling": t.string().optional(),
            "runtimeSettingsFetchTime": t.string().optional(),
            "varianceDisclaimer": t.string().optional(),
            "passedAuditsGroupTitle": t.string().optional(),
            "dropdownSaveHTML": t.string().optional(),
            "crcInitialNavigation": t.string().optional(),
            "lsPerformanceCategoryDescription": t.string().optional(),
            "runtimeSettingsBenchmark": t.string().optional(),
            "dropdownPrintExpanded": t.string().optional(),
            "runtimeSettingsTitle": t.string().optional(),
            "runtimeSettingsDevice": t.string().optional(),
            "dropdownPrintSummary": t.string().optional(),
            "auditGroupExpandTooltip": t.string().optional(),
            "runtimeMobileEmulation": t.string().optional(),
            "snippetCollapseButtonLabel": t.string().optional(),
            "viewTreemapLabel": t.string().optional(),
            "scorescaleLabel": t.string().optional(),
            "runtimeSettingsUA": t.string().optional(),
            "toplevelWarningsMessage": t.string().optional(),
            "warningHeader": t.string().optional(),
            "notApplicableAuditsGroupTitle": t.string().optional(),
            "runtimeDesktopEmulation": t.string().optional(),
            "snippetExpandButtonLabel": t.string().optional(),
            "calculatorLink": t.string().optional(),
            "labDataTitle": t.string().optional(),
            "errorLabel": t.string().optional(),
            "runtimeNoEmulation": t.string().optional(),
            "dropdownSaveGist": t.string().optional(),
            "dropdownDarkTheme": t.string().optional(),
            "runtimeUnknown": t.string().optional(),
            "opportunityResourceColumnLabel": t.string().optional(),
        }
    ).named(renames["RendererFormattedStringsIn"])
    types["RendererFormattedStringsOut"] = t.struct(
        {
            "opportunitySavingsColumnLabel": t.string().optional(),
            "runtimeSettingsNetworkThrottling": t.string().optional(),
            "runtimeSettingsAxeVersion": t.string().optional(),
            "errorMissingAuditInfo": t.string().optional(),
            "dropdownCopyJSON": t.string().optional(),
            "manualAuditsGroupTitle": t.string().optional(),
            "throttlingProvided": t.string().optional(),
            "runtimeSettingsChannel": t.string().optional(),
            "runtimeSettingsUANetwork": t.string().optional(),
            "warningAuditsGroupTitle": t.string().optional(),
            "dropdownViewer": t.string().optional(),
            "showRelevantAudits": t.string().optional(),
            "runtimeSettingsUrl": t.string().optional(),
            "dropdownSaveJSON": t.string().optional(),
            "crcLongestDurationLabel": t.string().optional(),
            "footerIssue": t.string().optional(),
            "thirdPartyResourcesLabel": t.string().optional(),
            "runtimeSettingsCPUThrottling": t.string().optional(),
            "runtimeSettingsFetchTime": t.string().optional(),
            "varianceDisclaimer": t.string().optional(),
            "passedAuditsGroupTitle": t.string().optional(),
            "dropdownSaveHTML": t.string().optional(),
            "crcInitialNavigation": t.string().optional(),
            "lsPerformanceCategoryDescription": t.string().optional(),
            "runtimeSettingsBenchmark": t.string().optional(),
            "dropdownPrintExpanded": t.string().optional(),
            "runtimeSettingsTitle": t.string().optional(),
            "runtimeSettingsDevice": t.string().optional(),
            "dropdownPrintSummary": t.string().optional(),
            "auditGroupExpandTooltip": t.string().optional(),
            "runtimeMobileEmulation": t.string().optional(),
            "snippetCollapseButtonLabel": t.string().optional(),
            "viewTreemapLabel": t.string().optional(),
            "scorescaleLabel": t.string().optional(),
            "runtimeSettingsUA": t.string().optional(),
            "toplevelWarningsMessage": t.string().optional(),
            "warningHeader": t.string().optional(),
            "notApplicableAuditsGroupTitle": t.string().optional(),
            "runtimeDesktopEmulation": t.string().optional(),
            "snippetExpandButtonLabel": t.string().optional(),
            "calculatorLink": t.string().optional(),
            "labDataTitle": t.string().optional(),
            "errorLabel": t.string().optional(),
            "runtimeNoEmulation": t.string().optional(),
            "dropdownSaveGist": t.string().optional(),
            "dropdownDarkTheme": t.string().optional(),
            "runtimeUnknown": t.string().optional(),
            "opportunityResourceColumnLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RendererFormattedStringsOut"])
    types["RuntimeErrorIn"] = t.struct(
        {"message": t.string().optional(), "code": t.string().optional()}
    ).named(renames["RuntimeErrorIn"])
    types["RuntimeErrorOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RuntimeErrorOut"])
    types["TimingIn"] = t.struct({"total": t.number().optional()}).named(
        renames["TimingIn"]
    )
    types["TimingOut"] = t.struct(
        {
            "total": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimingOut"])
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
    types["LhrEntityIn"] = t.struct(
        {
            "category": t.string().optional(),
            "name": t.string(),
            "isUnrecognized": t.boolean().optional(),
            "homepage": t.string().optional(),
            "origins": t.array(t.string()),
            "isFirstParty": t.boolean().optional(),
        }
    ).named(renames["LhrEntityIn"])
    types["LhrEntityOut"] = t.struct(
        {
            "category": t.string().optional(),
            "name": t.string(),
            "isUnrecognized": t.boolean().optional(),
            "homepage": t.string().optional(),
            "origins": t.array(t.string()),
            "isFirstParty": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LhrEntityOut"])
    types["StackPackIn"] = t.struct(
        {
            "descriptions": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "iconDataURL": t.string().optional(),
        }
    ).named(renames["StackPackIn"])
    types["StackPackOut"] = t.struct(
        {
            "descriptions": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "iconDataURL": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackPackOut"])

    functions = {}
    functions["pagespeedapiRunpagespeed"] = pagespeedonline.get(
        "pagespeedonline/v5/runPagespeed",
        t.struct(
            {
                "category": t.string().optional(),
                "strategy": t.string().optional(),
                "locale": t.string().optional(),
                "utm_source": t.string().optional(),
                "captchaToken": t.string().optional(),
                "url": t.string(),
                "utm_campaign": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PagespeedApiPagespeedResponseV5Out"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="pagespeedonline", renames=renames, types=types, functions=functions
    )
