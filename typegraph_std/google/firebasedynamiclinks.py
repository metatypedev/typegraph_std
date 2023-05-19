from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_firebasedynamiclinks() -> Import:
    firebasedynamiclinks = HTTPRuntime("https://firebasedynamiclinks.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasedynamiclinks_1_ErrorResponse",
        "ITunesConnectAnalyticsIn": "_firebasedynamiclinks_2_ITunesConnectAnalyticsIn",
        "ITunesConnectAnalyticsOut": "_firebasedynamiclinks_3_ITunesConnectAnalyticsOut",
        "ManagedShortLinkIn": "_firebasedynamiclinks_4_ManagedShortLinkIn",
        "ManagedShortLinkOut": "_firebasedynamiclinks_5_ManagedShortLinkOut",
        "SocialMetaTagInfoIn": "_firebasedynamiclinks_6_SocialMetaTagInfoIn",
        "SocialMetaTagInfoOut": "_firebasedynamiclinks_7_SocialMetaTagInfoOut",
        "CreateShortDynamicLinkRequestIn": "_firebasedynamiclinks_8_CreateShortDynamicLinkRequestIn",
        "CreateShortDynamicLinkRequestOut": "_firebasedynamiclinks_9_CreateShortDynamicLinkRequestOut",
        "GetIosPostInstallAttributionRequestIn": "_firebasedynamiclinks_10_GetIosPostInstallAttributionRequestIn",
        "GetIosPostInstallAttributionRequestOut": "_firebasedynamiclinks_11_GetIosPostInstallAttributionRequestOut",
        "DynamicLinkStatsIn": "_firebasedynamiclinks_12_DynamicLinkStatsIn",
        "DynamicLinkStatsOut": "_firebasedynamiclinks_13_DynamicLinkStatsOut",
        "CreateManagedShortLinkRequestIn": "_firebasedynamiclinks_14_CreateManagedShortLinkRequestIn",
        "CreateManagedShortLinkRequestOut": "_firebasedynamiclinks_15_CreateManagedShortLinkRequestOut",
        "CreateShortDynamicLinkResponseIn": "_firebasedynamiclinks_16_CreateShortDynamicLinkResponseIn",
        "CreateShortDynamicLinkResponseOut": "_firebasedynamiclinks_17_CreateShortDynamicLinkResponseOut",
        "DesktopInfoIn": "_firebasedynamiclinks_18_DesktopInfoIn",
        "DesktopInfoOut": "_firebasedynamiclinks_19_DesktopInfoOut",
        "GooglePlayAnalyticsIn": "_firebasedynamiclinks_20_GooglePlayAnalyticsIn",
        "GooglePlayAnalyticsOut": "_firebasedynamiclinks_21_GooglePlayAnalyticsOut",
        "DynamicLinkInfoIn": "_firebasedynamiclinks_22_DynamicLinkInfoIn",
        "DynamicLinkInfoOut": "_firebasedynamiclinks_23_DynamicLinkInfoOut",
        "AndroidInfoIn": "_firebasedynamiclinks_24_AndroidInfoIn",
        "AndroidInfoOut": "_firebasedynamiclinks_25_AndroidInfoOut",
        "CreateManagedShortLinkResponseIn": "_firebasedynamiclinks_26_CreateManagedShortLinkResponseIn",
        "CreateManagedShortLinkResponseOut": "_firebasedynamiclinks_27_CreateManagedShortLinkResponseOut",
        "GetIosReopenAttributionRequestIn": "_firebasedynamiclinks_28_GetIosReopenAttributionRequestIn",
        "GetIosReopenAttributionRequestOut": "_firebasedynamiclinks_29_GetIosReopenAttributionRequestOut",
        "NavigationInfoIn": "_firebasedynamiclinks_30_NavigationInfoIn",
        "NavigationInfoOut": "_firebasedynamiclinks_31_NavigationInfoOut",
        "IosInfoIn": "_firebasedynamiclinks_32_IosInfoIn",
        "IosInfoOut": "_firebasedynamiclinks_33_IosInfoOut",
        "SuffixIn": "_firebasedynamiclinks_34_SuffixIn",
        "SuffixOut": "_firebasedynamiclinks_35_SuffixOut",
        "DynamicLinkEventStatIn": "_firebasedynamiclinks_36_DynamicLinkEventStatIn",
        "DynamicLinkEventStatOut": "_firebasedynamiclinks_37_DynamicLinkEventStatOut",
        "DynamicLinkWarningIn": "_firebasedynamiclinks_38_DynamicLinkWarningIn",
        "DynamicLinkWarningOut": "_firebasedynamiclinks_39_DynamicLinkWarningOut",
        "GetIosReopenAttributionResponseIn": "_firebasedynamiclinks_40_GetIosReopenAttributionResponseIn",
        "GetIosReopenAttributionResponseOut": "_firebasedynamiclinks_41_GetIosReopenAttributionResponseOut",
        "AnalyticsInfoIn": "_firebasedynamiclinks_42_AnalyticsInfoIn",
        "AnalyticsInfoOut": "_firebasedynamiclinks_43_AnalyticsInfoOut",
        "GetIosPostInstallAttributionResponseIn": "_firebasedynamiclinks_44_GetIosPostInstallAttributionResponseIn",
        "GetIosPostInstallAttributionResponseOut": "_firebasedynamiclinks_45_GetIosPostInstallAttributionResponseOut",
        "DeviceInfoIn": "_firebasedynamiclinks_46_DeviceInfoIn",
        "DeviceInfoOut": "_firebasedynamiclinks_47_DeviceInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ITunesConnectAnalyticsIn"] = t.struct(
        {
            "ct": t.string().optional(),
            "mt": t.string().optional(),
            "at": t.string().optional(),
            "pt": t.string().optional(),
        }
    ).named(renames["ITunesConnectAnalyticsIn"])
    types["ITunesConnectAnalyticsOut"] = t.struct(
        {
            "ct": t.string().optional(),
            "mt": t.string().optional(),
            "at": t.string().optional(),
            "pt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ITunesConnectAnalyticsOut"])
    types["ManagedShortLinkIn"] = t.struct(
        {
            "visibility": t.string().optional(),
            "info": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "link": t.string().optional(),
            "flaggedAttribute": t.array(t.string()).optional(),
            "creationTime": t.string().optional(),
            "linkName": t.string().optional(),
        }
    ).named(renames["ManagedShortLinkIn"])
    types["ManagedShortLinkOut"] = t.struct(
        {
            "visibility": t.string().optional(),
            "info": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "link": t.string().optional(),
            "flaggedAttribute": t.array(t.string()).optional(),
            "creationTime": t.string().optional(),
            "linkName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedShortLinkOut"])
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
    types["CreateShortDynamicLinkRequestIn"] = t.struct(
        {
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "suffix": t.proxy(renames["SuffixIn"]).optional(),
            "longDynamicLink": t.string().optional(),
            "sdkVersion": t.string().optional(),
        }
    ).named(renames["CreateShortDynamicLinkRequestIn"])
    types["CreateShortDynamicLinkRequestOut"] = t.struct(
        {
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "suffix": t.proxy(renames["SuffixOut"]).optional(),
            "longDynamicLink": t.string().optional(),
            "sdkVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShortDynamicLinkRequestOut"])
    types["GetIosPostInstallAttributionRequestIn"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "device": t.proxy(renames["DeviceInfoIn"]).optional(),
            "visualStyle": t.string().optional(),
            "appInstallationTime": t.string().optional(),
            "retrievalMethod": t.string().optional(),
            "sdkVersion": t.string().optional(),
            "iosVersion": t.string().optional(),
            "uniqueMatchLinkToCheck": t.string().optional(),
        }
    ).named(renames["GetIosPostInstallAttributionRequestIn"])
    types["GetIosPostInstallAttributionRequestOut"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "device": t.proxy(renames["DeviceInfoOut"]).optional(),
            "visualStyle": t.string().optional(),
            "appInstallationTime": t.string().optional(),
            "retrievalMethod": t.string().optional(),
            "sdkVersion": t.string().optional(),
            "iosVersion": t.string().optional(),
            "uniqueMatchLinkToCheck": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosPostInstallAttributionRequestOut"])
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
    types["CreateManagedShortLinkRequestIn"] = t.struct(
        {
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "name": t.string().optional(),
            "suffix": t.proxy(renames["SuffixIn"]).optional(),
            "sdkVersion": t.string().optional(),
            "longDynamicLink": t.string().optional(),
        }
    ).named(renames["CreateManagedShortLinkRequestIn"])
    types["CreateManagedShortLinkRequestOut"] = t.struct(
        {
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "name": t.string().optional(),
            "suffix": t.proxy(renames["SuffixOut"]).optional(),
            "sdkVersion": t.string().optional(),
            "longDynamicLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkRequestOut"])
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
    types["DesktopInfoIn"] = t.struct(
        {"desktopFallbackLink": t.string().optional()}
    ).named(renames["DesktopInfoIn"])
    types["DesktopInfoOut"] = t.struct(
        {
            "desktopFallbackLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DesktopInfoOut"])
    types["GooglePlayAnalyticsIn"] = t.struct(
        {
            "utmMedium": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmTerm": t.string().optional(),
            "gclid": t.string().optional(),
            "utmContent": t.string().optional(),
        }
    ).named(renames["GooglePlayAnalyticsIn"])
    types["GooglePlayAnalyticsOut"] = t.struct(
        {
            "utmMedium": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmTerm": t.string().optional(),
            "gclid": t.string().optional(),
            "utmContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayAnalyticsOut"])
    types["DynamicLinkInfoIn"] = t.struct(
        {
            "domainUriPrefix": t.string().optional(),
            "link": t.string().optional(),
            "desktopInfo": t.proxy(renames["DesktopInfoIn"]).optional(),
            "socialMetaTagInfo": t.proxy(renames["SocialMetaTagInfoIn"]).optional(),
            "androidInfo": t.proxy(renames["AndroidInfoIn"]).optional(),
            "analyticsInfo": t.proxy(renames["AnalyticsInfoIn"]).optional(),
            "iosInfo": t.proxy(renames["IosInfoIn"]).optional(),
            "navigationInfo": t.proxy(renames["NavigationInfoIn"]).optional(),
            "dynamicLinkDomain": t.string().optional(),
        }
    ).named(renames["DynamicLinkInfoIn"])
    types["DynamicLinkInfoOut"] = t.struct(
        {
            "domainUriPrefix": t.string().optional(),
            "link": t.string().optional(),
            "desktopInfo": t.proxy(renames["DesktopInfoOut"]).optional(),
            "socialMetaTagInfo": t.proxy(renames["SocialMetaTagInfoOut"]).optional(),
            "androidInfo": t.proxy(renames["AndroidInfoOut"]).optional(),
            "analyticsInfo": t.proxy(renames["AnalyticsInfoOut"]).optional(),
            "iosInfo": t.proxy(renames["IosInfoOut"]).optional(),
            "navigationInfo": t.proxy(renames["NavigationInfoOut"]).optional(),
            "dynamicLinkDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkInfoOut"])
    types["AndroidInfoIn"] = t.struct(
        {
            "androidPackageName": t.string().optional(),
            "androidLink": t.string().optional(),
            "androidFallbackLink": t.string().optional(),
            "androidMinPackageVersionCode": t.string().optional(),
        }
    ).named(renames["AndroidInfoIn"])
    types["AndroidInfoOut"] = t.struct(
        {
            "androidPackageName": t.string().optional(),
            "androidLink": t.string().optional(),
            "androidFallbackLink": t.string().optional(),
            "androidMinPackageVersionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidInfoOut"])
    types["CreateManagedShortLinkResponseIn"] = t.struct(
        {
            "warning": t.array(t.proxy(renames["DynamicLinkWarningIn"])).optional(),
            "managedShortLink": t.proxy(renames["ManagedShortLinkIn"]).optional(),
            "previewLink": t.string().optional(),
        }
    ).named(renames["CreateManagedShortLinkResponseIn"])
    types["CreateManagedShortLinkResponseOut"] = t.struct(
        {
            "warning": t.array(t.proxy(renames["DynamicLinkWarningOut"])).optional(),
            "managedShortLink": t.proxy(renames["ManagedShortLinkOut"]).optional(),
            "previewLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkResponseOut"])
    types["GetIosReopenAttributionRequestIn"] = t.struct(
        {
            "sdkVersion": t.string().optional(),
            "requestedLink": t.string().optional(),
            "bundleId": t.string().optional(),
        }
    ).named(renames["GetIosReopenAttributionRequestIn"])
    types["GetIosReopenAttributionRequestOut"] = t.struct(
        {
            "sdkVersion": t.string().optional(),
            "requestedLink": t.string().optional(),
            "bundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosReopenAttributionRequestOut"])
    types["NavigationInfoIn"] = t.struct(
        {"enableForcedRedirect": t.boolean().optional()}
    ).named(renames["NavigationInfoIn"])
    types["NavigationInfoOut"] = t.struct(
        {
            "enableForcedRedirect": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NavigationInfoOut"])
    types["IosInfoIn"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "iosIpadBundleId": t.string().optional(),
            "iosIpadFallbackLink": t.string().optional(),
            "iosMinimumVersion": t.string().optional(),
            "iosFallbackLink": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosCustomScheme": t.string().optional(),
        }
    ).named(renames["IosInfoIn"])
    types["IosInfoOut"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "iosIpadBundleId": t.string().optional(),
            "iosIpadFallbackLink": t.string().optional(),
            "iosMinimumVersion": t.string().optional(),
            "iosFallbackLink": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosCustomScheme": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosInfoOut"])
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
    types["DynamicLinkEventStatIn"] = t.struct(
        {
            "platform": t.string().optional(),
            "event": t.string().optional(),
            "count": t.string().optional(),
        }
    ).named(renames["DynamicLinkEventStatIn"])
    types["DynamicLinkEventStatOut"] = t.struct(
        {
            "platform": t.string().optional(),
            "event": t.string().optional(),
            "count": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkEventStatOut"])
    types["DynamicLinkWarningIn"] = t.struct(
        {
            "warningDocumentLink": t.string().optional(),
            "warningMessage": t.string().optional(),
            "warningCode": t.string().optional(),
        }
    ).named(renames["DynamicLinkWarningIn"])
    types["DynamicLinkWarningOut"] = t.struct(
        {
            "warningDocumentLink": t.string().optional(),
            "warningMessage": t.string().optional(),
            "warningCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkWarningOut"])
    types["GetIosReopenAttributionResponseIn"] = t.struct(
        {
            "deepLink": t.string().optional(),
            "utmTerm": t.string().optional(),
            "invitationId": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmMedium": t.string().optional(),
            "iosMinAppVersion": t.string().optional(),
            "utmSource": t.string().optional(),
            "resolvedLink": t.string().optional(),
        }
    ).named(renames["GetIosReopenAttributionResponseIn"])
    types["GetIosReopenAttributionResponseOut"] = t.struct(
        {
            "deepLink": t.string().optional(),
            "utmTerm": t.string().optional(),
            "invitationId": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmMedium": t.string().optional(),
            "iosMinAppVersion": t.string().optional(),
            "utmSource": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosReopenAttributionResponseOut"])
    types["AnalyticsInfoIn"] = t.struct(
        {
            "itunesConnectAnalytics": t.proxy(
                renames["ITunesConnectAnalyticsIn"]
            ).optional(),
            "googlePlayAnalytics": t.proxy(renames["GooglePlayAnalyticsIn"]).optional(),
        }
    ).named(renames["AnalyticsInfoIn"])
    types["AnalyticsInfoOut"] = t.struct(
        {
            "itunesConnectAnalytics": t.proxy(
                renames["ITunesConnectAnalyticsOut"]
            ).optional(),
            "googlePlayAnalytics": t.proxy(
                renames["GooglePlayAnalyticsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyticsInfoOut"])
    types["GetIosPostInstallAttributionResponseIn"] = t.struct(
        {
            "utmContent": t.string().optional(),
            "invitationId": t.string().optional(),
            "externalBrowserDestinationLink": t.string().optional(),
            "requestedLink": t.string().optional(),
            "utmSource": t.string().optional(),
            "appMinimumVersion": t.string().optional(),
            "fallbackLink": t.string().optional(),
            "utmMedium": t.string().optional(),
            "requestIpVersion": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "deepLink": t.string().optional(),
            "attributionConfidence": t.string().optional(),
            "matchMessage": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "isStrongMatchExecutable": t.boolean().optional(),
        }
    ).named(renames["GetIosPostInstallAttributionResponseIn"])
    types["GetIosPostInstallAttributionResponseOut"] = t.struct(
        {
            "utmContent": t.string().optional(),
            "invitationId": t.string().optional(),
            "externalBrowserDestinationLink": t.string().optional(),
            "requestedLink": t.string().optional(),
            "utmSource": t.string().optional(),
            "appMinimumVersion": t.string().optional(),
            "fallbackLink": t.string().optional(),
            "utmMedium": t.string().optional(),
            "requestIpVersion": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "deepLink": t.string().optional(),
            "attributionConfidence": t.string().optional(),
            "matchMessage": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "isStrongMatchExecutable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosPostInstallAttributionResponseOut"])
    types["DeviceInfoIn"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "languageCodeRaw": t.string().optional(),
            "screenResolutionWidth": t.string().optional(),
            "timezone": t.string().optional(),
            "screenResolutionHeight": t.string().optional(),
            "deviceModelName": t.string().optional(),
            "languageCodeFromWebview": t.string().optional(),
        }
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "languageCode": t.string().optional(),
            "languageCodeRaw": t.string().optional(),
            "screenResolutionWidth": t.string().optional(),
            "timezone": t.string().optional(),
            "screenResolutionHeight": t.string().optional(),
            "deviceModelName": t.string().optional(),
            "languageCodeFromWebview": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceInfoOut"])

    functions = {}
    functions["shortLinksCreate"] = firebasedynamiclinks.post(
        "v1/shortLinks",
        t.struct(
            {
                "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
                "suffix": t.proxy(renames["SuffixIn"]).optional(),
                "longDynamicLink": t.string().optional(),
                "sdkVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateShortDynamicLinkResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetLinkStats"] = firebasedynamiclinks.post(
        "v1/reopenAttribution",
        t.struct(
            {
                "sdkVersion": t.string().optional(),
                "requestedLink": t.string().optional(),
                "bundleId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetIosReopenAttributionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1InstallAttribution"] = firebasedynamiclinks.post(
        "v1/reopenAttribution",
        t.struct(
            {
                "sdkVersion": t.string().optional(),
                "requestedLink": t.string().optional(),
                "bundleId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetIosReopenAttributionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1ReopenAttribution"] = firebasedynamiclinks.post(
        "v1/reopenAttribution",
        t.struct(
            {
                "sdkVersion": t.string().optional(),
                "requestedLink": t.string().optional(),
                "bundleId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetIosReopenAttributionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedShortLinksCreate"] = firebasedynamiclinks.post(
        "v1/managedShortLinks:create",
        t.struct(
            {
                "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
                "name": t.string().optional(),
                "suffix": t.proxy(renames["SuffixIn"]).optional(),
                "sdkVersion": t.string().optional(),
                "longDynamicLink": t.string().optional(),
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
