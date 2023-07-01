from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_firebasedynamiclinks():
    firebasedynamiclinks = HTTPRuntime("https://firebasedynamiclinks.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasedynamiclinks_1_ErrorResponse",
        "SuffixIn": "_firebasedynamiclinks_2_SuffixIn",
        "SuffixOut": "_firebasedynamiclinks_3_SuffixOut",
        "SocialMetaTagInfoIn": "_firebasedynamiclinks_4_SocialMetaTagInfoIn",
        "SocialMetaTagInfoOut": "_firebasedynamiclinks_5_SocialMetaTagInfoOut",
        "CreateShortDynamicLinkResponseIn": "_firebasedynamiclinks_6_CreateShortDynamicLinkResponseIn",
        "CreateShortDynamicLinkResponseOut": "_firebasedynamiclinks_7_CreateShortDynamicLinkResponseOut",
        "IosInfoIn": "_firebasedynamiclinks_8_IosInfoIn",
        "IosInfoOut": "_firebasedynamiclinks_9_IosInfoOut",
        "DynamicLinkWarningIn": "_firebasedynamiclinks_10_DynamicLinkWarningIn",
        "DynamicLinkWarningOut": "_firebasedynamiclinks_11_DynamicLinkWarningOut",
        "DesktopInfoIn": "_firebasedynamiclinks_12_DesktopInfoIn",
        "DesktopInfoOut": "_firebasedynamiclinks_13_DesktopInfoOut",
        "CreateManagedShortLinkResponseIn": "_firebasedynamiclinks_14_CreateManagedShortLinkResponseIn",
        "CreateManagedShortLinkResponseOut": "_firebasedynamiclinks_15_CreateManagedShortLinkResponseOut",
        "AndroidInfoIn": "_firebasedynamiclinks_16_AndroidInfoIn",
        "AndroidInfoOut": "_firebasedynamiclinks_17_AndroidInfoOut",
        "ITunesConnectAnalyticsIn": "_firebasedynamiclinks_18_ITunesConnectAnalyticsIn",
        "ITunesConnectAnalyticsOut": "_firebasedynamiclinks_19_ITunesConnectAnalyticsOut",
        "GetIosPostInstallAttributionRequestIn": "_firebasedynamiclinks_20_GetIosPostInstallAttributionRequestIn",
        "GetIosPostInstallAttributionRequestOut": "_firebasedynamiclinks_21_GetIosPostInstallAttributionRequestOut",
        "AnalyticsInfoIn": "_firebasedynamiclinks_22_AnalyticsInfoIn",
        "AnalyticsInfoOut": "_firebasedynamiclinks_23_AnalyticsInfoOut",
        "GetIosPostInstallAttributionResponseIn": "_firebasedynamiclinks_24_GetIosPostInstallAttributionResponseIn",
        "GetIosPostInstallAttributionResponseOut": "_firebasedynamiclinks_25_GetIosPostInstallAttributionResponseOut",
        "CreateManagedShortLinkRequestIn": "_firebasedynamiclinks_26_CreateManagedShortLinkRequestIn",
        "CreateManagedShortLinkRequestOut": "_firebasedynamiclinks_27_CreateManagedShortLinkRequestOut",
        "GetIosReopenAttributionResponseIn": "_firebasedynamiclinks_28_GetIosReopenAttributionResponseIn",
        "GetIosReopenAttributionResponseOut": "_firebasedynamiclinks_29_GetIosReopenAttributionResponseOut",
        "ManagedShortLinkIn": "_firebasedynamiclinks_30_ManagedShortLinkIn",
        "ManagedShortLinkOut": "_firebasedynamiclinks_31_ManagedShortLinkOut",
        "DeviceInfoIn": "_firebasedynamiclinks_32_DeviceInfoIn",
        "DeviceInfoOut": "_firebasedynamiclinks_33_DeviceInfoOut",
        "NavigationInfoIn": "_firebasedynamiclinks_34_NavigationInfoIn",
        "NavigationInfoOut": "_firebasedynamiclinks_35_NavigationInfoOut",
        "DynamicLinkInfoIn": "_firebasedynamiclinks_36_DynamicLinkInfoIn",
        "DynamicLinkInfoOut": "_firebasedynamiclinks_37_DynamicLinkInfoOut",
        "DynamicLinkStatsIn": "_firebasedynamiclinks_38_DynamicLinkStatsIn",
        "DynamicLinkStatsOut": "_firebasedynamiclinks_39_DynamicLinkStatsOut",
        "DynamicLinkEventStatIn": "_firebasedynamiclinks_40_DynamicLinkEventStatIn",
        "DynamicLinkEventStatOut": "_firebasedynamiclinks_41_DynamicLinkEventStatOut",
        "CreateShortDynamicLinkRequestIn": "_firebasedynamiclinks_42_CreateShortDynamicLinkRequestIn",
        "CreateShortDynamicLinkRequestOut": "_firebasedynamiclinks_43_CreateShortDynamicLinkRequestOut",
        "GooglePlayAnalyticsIn": "_firebasedynamiclinks_44_GooglePlayAnalyticsIn",
        "GooglePlayAnalyticsOut": "_firebasedynamiclinks_45_GooglePlayAnalyticsOut",
        "GetIosReopenAttributionRequestIn": "_firebasedynamiclinks_46_GetIosReopenAttributionRequestIn",
        "GetIosReopenAttributionRequestOut": "_firebasedynamiclinks_47_GetIosReopenAttributionRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SuffixIn"] = t.struct(
        {"customSuffix": t.string().optional(), "option": t.string().optional()}
    ).named(renames["SuffixIn"])
    types["SuffixOut"] = t.struct(
        {
            "customSuffix": t.string().optional(),
            "option": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuffixOut"])
    types["SocialMetaTagInfoIn"] = t.struct(
        {
            "socialTitle": t.string().optional(),
            "socialImageLink": t.string().optional(),
            "socialDescription": t.string().optional(),
        }
    ).named(renames["SocialMetaTagInfoIn"])
    types["SocialMetaTagInfoOut"] = t.struct(
        {
            "socialTitle": t.string().optional(),
            "socialImageLink": t.string().optional(),
            "socialDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocialMetaTagInfoOut"])
    types["CreateShortDynamicLinkResponseIn"] = t.struct(
        {
            "shortLink": t.string().optional(),
            "warning": t.array(t.proxy(renames["DynamicLinkWarningIn"])).optional(),
            "previewLink": t.string().optional(),
        }
    ).named(renames["CreateShortDynamicLinkResponseIn"])
    types["CreateShortDynamicLinkResponseOut"] = t.struct(
        {
            "shortLink": t.string().optional(),
            "warning": t.array(t.proxy(renames["DynamicLinkWarningOut"])).optional(),
            "previewLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShortDynamicLinkResponseOut"])
    types["IosInfoIn"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "iosMinimumVersion": t.string().optional(),
            "iosIpadFallbackLink": t.string().optional(),
            "iosFallbackLink": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosCustomScheme": t.string().optional(),
            "iosIpadBundleId": t.string().optional(),
        }
    ).named(renames["IosInfoIn"])
    types["IosInfoOut"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "iosMinimumVersion": t.string().optional(),
            "iosIpadFallbackLink": t.string().optional(),
            "iosFallbackLink": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosCustomScheme": t.string().optional(),
            "iosIpadBundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosInfoOut"])
    types["DynamicLinkWarningIn"] = t.struct(
        {
            "warningCode": t.string().optional(),
            "warningDocumentLink": t.string().optional(),
            "warningMessage": t.string().optional(),
        }
    ).named(renames["DynamicLinkWarningIn"])
    types["DynamicLinkWarningOut"] = t.struct(
        {
            "warningCode": t.string().optional(),
            "warningDocumentLink": t.string().optional(),
            "warningMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkWarningOut"])
    types["DesktopInfoIn"] = t.struct(
        {"desktopFallbackLink": t.string().optional()}
    ).named(renames["DesktopInfoIn"])
    types["DesktopInfoOut"] = t.struct(
        {
            "desktopFallbackLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DesktopInfoOut"])
    types["CreateManagedShortLinkResponseIn"] = t.struct(
        {
            "previewLink": t.string().optional(),
            "warning": t.array(t.proxy(renames["DynamicLinkWarningIn"])).optional(),
            "managedShortLink": t.proxy(renames["ManagedShortLinkIn"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkResponseIn"])
    types["CreateManagedShortLinkResponseOut"] = t.struct(
        {
            "previewLink": t.string().optional(),
            "warning": t.array(t.proxy(renames["DynamicLinkWarningOut"])).optional(),
            "managedShortLink": t.proxy(renames["ManagedShortLinkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkResponseOut"])
    types["AndroidInfoIn"] = t.struct(
        {
            "androidFallbackLink": t.string().optional(),
            "androidLink": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "androidMinPackageVersionCode": t.string().optional(),
        }
    ).named(renames["AndroidInfoIn"])
    types["AndroidInfoOut"] = t.struct(
        {
            "androidFallbackLink": t.string().optional(),
            "androidLink": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "androidMinPackageVersionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidInfoOut"])
    types["ITunesConnectAnalyticsIn"] = t.struct(
        {
            "pt": t.string().optional(),
            "at": t.string().optional(),
            "mt": t.string().optional(),
            "ct": t.string().optional(),
        }
    ).named(renames["ITunesConnectAnalyticsIn"])
    types["ITunesConnectAnalyticsOut"] = t.struct(
        {
            "pt": t.string().optional(),
            "at": t.string().optional(),
            "mt": t.string().optional(),
            "ct": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ITunesConnectAnalyticsOut"])
    types["GetIosPostInstallAttributionRequestIn"] = t.struct(
        {
            "iosVersion": t.string().optional(),
            "bundleId": t.string().optional(),
            "visualStyle": t.string().optional(),
            "retrievalMethod": t.string().optional(),
            "appInstallationTime": t.string().optional(),
            "uniqueMatchLinkToCheck": t.string().optional(),
            "sdkVersion": t.string().optional(),
            "device": t.proxy(renames["DeviceInfoIn"]).optional(),
        }
    ).named(renames["GetIosPostInstallAttributionRequestIn"])
    types["GetIosPostInstallAttributionRequestOut"] = t.struct(
        {
            "iosVersion": t.string().optional(),
            "bundleId": t.string().optional(),
            "visualStyle": t.string().optional(),
            "retrievalMethod": t.string().optional(),
            "appInstallationTime": t.string().optional(),
            "uniqueMatchLinkToCheck": t.string().optional(),
            "sdkVersion": t.string().optional(),
            "device": t.proxy(renames["DeviceInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosPostInstallAttributionRequestOut"])
    types["AnalyticsInfoIn"] = t.struct(
        {
            "googlePlayAnalytics": t.proxy(renames["GooglePlayAnalyticsIn"]).optional(),
            "itunesConnectAnalytics": t.proxy(
                renames["ITunesConnectAnalyticsIn"]
            ).optional(),
        }
    ).named(renames["AnalyticsInfoIn"])
    types["AnalyticsInfoOut"] = t.struct(
        {
            "googlePlayAnalytics": t.proxy(
                renames["GooglePlayAnalyticsOut"]
            ).optional(),
            "itunesConnectAnalytics": t.proxy(
                renames["ITunesConnectAnalyticsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyticsInfoOut"])
    types["GetIosPostInstallAttributionResponseIn"] = t.struct(
        {
            "appMinimumVersion": t.string().optional(),
            "utmSource": t.string().optional(),
            "attributionConfidence": t.string().optional(),
            "matchMessage": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmMedium": t.string().optional(),
            "isStrongMatchExecutable": t.boolean().optional(),
            "externalBrowserDestinationLink": t.string().optional(),
            "utmTerm": t.string().optional(),
            "requestIpVersion": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "invitationId": t.string().optional(),
            "fallbackLink": t.string().optional(),
            "deepLink": t.string().optional(),
            "requestedLink": t.string().optional(),
            "utmContent": t.string().optional(),
        }
    ).named(renames["GetIosPostInstallAttributionResponseIn"])
    types["GetIosPostInstallAttributionResponseOut"] = t.struct(
        {
            "appMinimumVersion": t.string().optional(),
            "utmSource": t.string().optional(),
            "attributionConfidence": t.string().optional(),
            "matchMessage": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmMedium": t.string().optional(),
            "isStrongMatchExecutable": t.boolean().optional(),
            "externalBrowserDestinationLink": t.string().optional(),
            "utmTerm": t.string().optional(),
            "requestIpVersion": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "invitationId": t.string().optional(),
            "fallbackLink": t.string().optional(),
            "deepLink": t.string().optional(),
            "requestedLink": t.string().optional(),
            "utmContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosPostInstallAttributionResponseOut"])
    types["CreateManagedShortLinkRequestIn"] = t.struct(
        {
            "sdkVersion": t.string().optional(),
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "suffix": t.proxy(renames["SuffixIn"]).optional(),
            "longDynamicLink": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["CreateManagedShortLinkRequestIn"])
    types["CreateManagedShortLinkRequestOut"] = t.struct(
        {
            "sdkVersion": t.string().optional(),
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "suffix": t.proxy(renames["SuffixOut"]).optional(),
            "longDynamicLink": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkRequestOut"])
    types["GetIosReopenAttributionResponseIn"] = t.struct(
        {
            "utmTerm": t.string().optional(),
            "utmContent": t.string().optional(),
            "deepLink": t.string().optional(),
            "invitationId": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "utmSource": t.string().optional(),
            "iosMinAppVersion": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmCampaign": t.string().optional(),
        }
    ).named(renames["GetIosReopenAttributionResponseIn"])
    types["GetIosReopenAttributionResponseOut"] = t.struct(
        {
            "utmTerm": t.string().optional(),
            "utmContent": t.string().optional(),
            "deepLink": t.string().optional(),
            "invitationId": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "utmSource": t.string().optional(),
            "iosMinAppVersion": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosReopenAttributionResponseOut"])
    types["ManagedShortLinkIn"] = t.struct(
        {
            "info": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "linkName": t.string().optional(),
            "flaggedAttribute": t.array(t.string()).optional(),
            "creationTime": t.string().optional(),
            "visibility": t.string().optional(),
            "link": t.string().optional(),
        }
    ).named(renames["ManagedShortLinkIn"])
    types["ManagedShortLinkOut"] = t.struct(
        {
            "info": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "linkName": t.string().optional(),
            "flaggedAttribute": t.array(t.string()).optional(),
            "creationTime": t.string().optional(),
            "visibility": t.string().optional(),
            "link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedShortLinkOut"])
    types["DeviceInfoIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "screenResolutionWidth": t.string().optional(),
            "languageCodeRaw": t.string().optional(),
            "deviceModelName": t.string().optional(),
            "screenResolutionHeight": t.string().optional(),
            "languageCodeFromWebview": t.string().optional(),
            "timezone": t.string().optional(),
        }
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "screenResolutionWidth": t.string().optional(),
            "languageCodeRaw": t.string().optional(),
            "deviceModelName": t.string().optional(),
            "screenResolutionHeight": t.string().optional(),
            "languageCodeFromWebview": t.string().optional(),
            "timezone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceInfoOut"])
    types["NavigationInfoIn"] = t.struct(
        {"enableForcedRedirect": t.boolean().optional()}
    ).named(renames["NavigationInfoIn"])
    types["NavigationInfoOut"] = t.struct(
        {
            "enableForcedRedirect": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NavigationInfoOut"])
    types["DynamicLinkInfoIn"] = t.struct(
        {
            "link": t.string().optional(),
            "navigationInfo": t.proxy(renames["NavigationInfoIn"]).optional(),
            "dynamicLinkDomain": t.string().optional(),
            "desktopInfo": t.proxy(renames["DesktopInfoIn"]).optional(),
            "domainUriPrefix": t.string().optional(),
            "androidInfo": t.proxy(renames["AndroidInfoIn"]).optional(),
            "analyticsInfo": t.proxy(renames["AnalyticsInfoIn"]).optional(),
            "iosInfo": t.proxy(renames["IosInfoIn"]).optional(),
            "socialMetaTagInfo": t.proxy(renames["SocialMetaTagInfoIn"]).optional(),
        }
    ).named(renames["DynamicLinkInfoIn"])
    types["DynamicLinkInfoOut"] = t.struct(
        {
            "link": t.string().optional(),
            "navigationInfo": t.proxy(renames["NavigationInfoOut"]).optional(),
            "dynamicLinkDomain": t.string().optional(),
            "desktopInfo": t.proxy(renames["DesktopInfoOut"]).optional(),
            "domainUriPrefix": t.string().optional(),
            "androidInfo": t.proxy(renames["AndroidInfoOut"]).optional(),
            "analyticsInfo": t.proxy(renames["AnalyticsInfoOut"]).optional(),
            "iosInfo": t.proxy(renames["IosInfoOut"]).optional(),
            "socialMetaTagInfo": t.proxy(renames["SocialMetaTagInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkInfoOut"])
    types["DynamicLinkStatsIn"] = t.struct(
        {
            "linkEventStats": t.array(
                t.proxy(renames["DynamicLinkEventStatIn"])
            ).optional()
        }
    ).named(renames["DynamicLinkStatsIn"])
    types["DynamicLinkStatsOut"] = t.struct(
        {
            "linkEventStats": t.array(
                t.proxy(renames["DynamicLinkEventStatOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkStatsOut"])
    types["DynamicLinkEventStatIn"] = t.struct(
        {
            "event": t.string().optional(),
            "platform": t.string().optional(),
            "count": t.string().optional(),
        }
    ).named(renames["DynamicLinkEventStatIn"])
    types["DynamicLinkEventStatOut"] = t.struct(
        {
            "event": t.string().optional(),
            "platform": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkEventStatOut"])
    types["CreateShortDynamicLinkRequestIn"] = t.struct(
        {
            "suffix": t.proxy(renames["SuffixIn"]).optional(),
            "sdkVersion": t.string().optional(),
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "longDynamicLink": t.string().optional(),
        }
    ).named(renames["CreateShortDynamicLinkRequestIn"])
    types["CreateShortDynamicLinkRequestOut"] = t.struct(
        {
            "suffix": t.proxy(renames["SuffixOut"]).optional(),
            "sdkVersion": t.string().optional(),
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "longDynamicLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShortDynamicLinkRequestOut"])
    types["GooglePlayAnalyticsIn"] = t.struct(
        {
            "gclid": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmMedium": t.string().optional(),
        }
    ).named(renames["GooglePlayAnalyticsIn"])
    types["GooglePlayAnalyticsOut"] = t.struct(
        {
            "gclid": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmMedium": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayAnalyticsOut"])
    types["GetIosReopenAttributionRequestIn"] = t.struct(
        {
            "requestedLink": t.string().optional(),
            "sdkVersion": t.string().optional(),
            "bundleId": t.string().optional(),
        }
    ).named(renames["GetIosReopenAttributionRequestIn"])
    types["GetIosReopenAttributionRequestOut"] = t.struct(
        {
            "requestedLink": t.string().optional(),
            "sdkVersion": t.string().optional(),
            "bundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosReopenAttributionRequestOut"])

    functions = {}
    functions["v1ReopenAttribution"] = firebasedynamiclinks.get(
        "v1/{dynamicLink}/linkStats",
        t.struct(
            {
                "dynamicLink": t.string().optional(),
                "durationDays": t.string().optional(),
                "sdkVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DynamicLinkStatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1InstallAttribution"] = firebasedynamiclinks.get(
        "v1/{dynamicLink}/linkStats",
        t.struct(
            {
                "dynamicLink": t.string().optional(),
                "durationDays": t.string().optional(),
                "sdkVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DynamicLinkStatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetLinkStats"] = firebasedynamiclinks.get(
        "v1/{dynamicLink}/linkStats",
        t.struct(
            {
                "dynamicLink": t.string().optional(),
                "durationDays": t.string().optional(),
                "sdkVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DynamicLinkStatsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shortLinksCreate"] = firebasedynamiclinks.post(
        "v1/shortLinks",
        t.struct(
            {
                "suffix": t.proxy(renames["SuffixIn"]).optional(),
                "sdkVersion": t.string().optional(),
                "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
                "longDynamicLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateShortDynamicLinkResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedShortLinksCreate"] = firebasedynamiclinks.post(
        "v1/managedShortLinks:create",
        t.struct(
            {
                "sdkVersion": t.string().optional(),
                "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
                "suffix": t.proxy(renames["SuffixIn"]).optional(),
                "longDynamicLink": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateManagedShortLinkResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebasedynamiclinks",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
