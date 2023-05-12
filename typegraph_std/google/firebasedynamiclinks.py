from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_firebasedynamiclinks() -> Import:
    firebasedynamiclinks = HTTPRuntime("https://firebasedynamiclinks.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasedynamiclinks_1_ErrorResponse",
        "ITunesConnectAnalyticsIn": "_firebasedynamiclinks_2_ITunesConnectAnalyticsIn",
        "ITunesConnectAnalyticsOut": "_firebasedynamiclinks_3_ITunesConnectAnalyticsOut",
        "CreateManagedShortLinkResponseIn": "_firebasedynamiclinks_4_CreateManagedShortLinkResponseIn",
        "CreateManagedShortLinkResponseOut": "_firebasedynamiclinks_5_CreateManagedShortLinkResponseOut",
        "GetIosReopenAttributionResponseIn": "_firebasedynamiclinks_6_GetIosReopenAttributionResponseIn",
        "GetIosReopenAttributionResponseOut": "_firebasedynamiclinks_7_GetIosReopenAttributionResponseOut",
        "CreateManagedShortLinkRequestIn": "_firebasedynamiclinks_8_CreateManagedShortLinkRequestIn",
        "CreateManagedShortLinkRequestOut": "_firebasedynamiclinks_9_CreateManagedShortLinkRequestOut",
        "IosInfoIn": "_firebasedynamiclinks_10_IosInfoIn",
        "IosInfoOut": "_firebasedynamiclinks_11_IosInfoOut",
        "DynamicLinkInfoIn": "_firebasedynamiclinks_12_DynamicLinkInfoIn",
        "DynamicLinkInfoOut": "_firebasedynamiclinks_13_DynamicLinkInfoOut",
        "GetIosPostInstallAttributionRequestIn": "_firebasedynamiclinks_14_GetIosPostInstallAttributionRequestIn",
        "GetIosPostInstallAttributionRequestOut": "_firebasedynamiclinks_15_GetIosPostInstallAttributionRequestOut",
        "DeviceInfoIn": "_firebasedynamiclinks_16_DeviceInfoIn",
        "DeviceInfoOut": "_firebasedynamiclinks_17_DeviceInfoOut",
        "SuffixIn": "_firebasedynamiclinks_18_SuffixIn",
        "SuffixOut": "_firebasedynamiclinks_19_SuffixOut",
        "ManagedShortLinkIn": "_firebasedynamiclinks_20_ManagedShortLinkIn",
        "ManagedShortLinkOut": "_firebasedynamiclinks_21_ManagedShortLinkOut",
        "DesktopInfoIn": "_firebasedynamiclinks_22_DesktopInfoIn",
        "DesktopInfoOut": "_firebasedynamiclinks_23_DesktopInfoOut",
        "AndroidInfoIn": "_firebasedynamiclinks_24_AndroidInfoIn",
        "AndroidInfoOut": "_firebasedynamiclinks_25_AndroidInfoOut",
        "AnalyticsInfoIn": "_firebasedynamiclinks_26_AnalyticsInfoIn",
        "AnalyticsInfoOut": "_firebasedynamiclinks_27_AnalyticsInfoOut",
        "DynamicLinkEventStatIn": "_firebasedynamiclinks_28_DynamicLinkEventStatIn",
        "DynamicLinkEventStatOut": "_firebasedynamiclinks_29_DynamicLinkEventStatOut",
        "CreateShortDynamicLinkRequestIn": "_firebasedynamiclinks_30_CreateShortDynamicLinkRequestIn",
        "CreateShortDynamicLinkRequestOut": "_firebasedynamiclinks_31_CreateShortDynamicLinkRequestOut",
        "DynamicLinkWarningIn": "_firebasedynamiclinks_32_DynamicLinkWarningIn",
        "DynamicLinkWarningOut": "_firebasedynamiclinks_33_DynamicLinkWarningOut",
        "SocialMetaTagInfoIn": "_firebasedynamiclinks_34_SocialMetaTagInfoIn",
        "SocialMetaTagInfoOut": "_firebasedynamiclinks_35_SocialMetaTagInfoOut",
        "DynamicLinkStatsIn": "_firebasedynamiclinks_36_DynamicLinkStatsIn",
        "DynamicLinkStatsOut": "_firebasedynamiclinks_37_DynamicLinkStatsOut",
        "GetIosPostInstallAttributionResponseIn": "_firebasedynamiclinks_38_GetIosPostInstallAttributionResponseIn",
        "GetIosPostInstallAttributionResponseOut": "_firebasedynamiclinks_39_GetIosPostInstallAttributionResponseOut",
        "GetIosReopenAttributionRequestIn": "_firebasedynamiclinks_40_GetIosReopenAttributionRequestIn",
        "GetIosReopenAttributionRequestOut": "_firebasedynamiclinks_41_GetIosReopenAttributionRequestOut",
        "CreateShortDynamicLinkResponseIn": "_firebasedynamiclinks_42_CreateShortDynamicLinkResponseIn",
        "CreateShortDynamicLinkResponseOut": "_firebasedynamiclinks_43_CreateShortDynamicLinkResponseOut",
        "NavigationInfoIn": "_firebasedynamiclinks_44_NavigationInfoIn",
        "NavigationInfoOut": "_firebasedynamiclinks_45_NavigationInfoOut",
        "GooglePlayAnalyticsIn": "_firebasedynamiclinks_46_GooglePlayAnalyticsIn",
        "GooglePlayAnalyticsOut": "_firebasedynamiclinks_47_GooglePlayAnalyticsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ITunesConnectAnalyticsIn"] = t.struct(
        {
            "ct": t.string().optional(),
            "pt": t.string().optional(),
            "mt": t.string().optional(),
            "at": t.string().optional(),
        }
    ).named(renames["ITunesConnectAnalyticsIn"])
    types["ITunesConnectAnalyticsOut"] = t.struct(
        {
            "ct": t.string().optional(),
            "pt": t.string().optional(),
            "mt": t.string().optional(),
            "at": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ITunesConnectAnalyticsOut"])
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
    types["GetIosReopenAttributionResponseIn"] = t.struct(
        {
            "utmContent": t.string().optional(),
            "deepLink": t.string().optional(),
            "iosMinAppVersion": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmMedium": t.string().optional(),
            "invitationId": t.string().optional(),
            "utmTerm": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "utmSource": t.string().optional(),
        }
    ).named(renames["GetIosReopenAttributionResponseIn"])
    types["GetIosReopenAttributionResponseOut"] = t.struct(
        {
            "utmContent": t.string().optional(),
            "deepLink": t.string().optional(),
            "iosMinAppVersion": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmMedium": t.string().optional(),
            "invitationId": t.string().optional(),
            "utmTerm": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "utmSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosReopenAttributionResponseOut"])
    types["CreateManagedShortLinkRequestIn"] = t.struct(
        {
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "sdkVersion": t.string().optional(),
            "longDynamicLink": t.string().optional(),
            "name": t.string().optional(),
            "suffix": t.proxy(renames["SuffixIn"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkRequestIn"])
    types["CreateManagedShortLinkRequestOut"] = t.struct(
        {
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "sdkVersion": t.string().optional(),
            "longDynamicLink": t.string().optional(),
            "name": t.string().optional(),
            "suffix": t.proxy(renames["SuffixOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkRequestOut"])
    types["IosInfoIn"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "iosIpadBundleId": t.string().optional(),
            "iosFallbackLink": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosCustomScheme": t.string().optional(),
            "iosMinimumVersion": t.string().optional(),
            "iosIpadFallbackLink": t.string().optional(),
        }
    ).named(renames["IosInfoIn"])
    types["IosInfoOut"] = t.struct(
        {
            "iosBundleId": t.string().optional(),
            "iosIpadBundleId": t.string().optional(),
            "iosFallbackLink": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosCustomScheme": t.string().optional(),
            "iosMinimumVersion": t.string().optional(),
            "iosIpadFallbackLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosInfoOut"])
    types["DynamicLinkInfoIn"] = t.struct(
        {
            "socialMetaTagInfo": t.proxy(renames["SocialMetaTagInfoIn"]).optional(),
            "domainUriPrefix": t.string().optional(),
            "dynamicLinkDomain": t.string().optional(),
            "navigationInfo": t.proxy(renames["NavigationInfoIn"]).optional(),
            "androidInfo": t.proxy(renames["AndroidInfoIn"]).optional(),
            "link": t.string().optional(),
            "iosInfo": t.proxy(renames["IosInfoIn"]).optional(),
            "desktopInfo": t.proxy(renames["DesktopInfoIn"]).optional(),
            "analyticsInfo": t.proxy(renames["AnalyticsInfoIn"]).optional(),
        }
    ).named(renames["DynamicLinkInfoIn"])
    types["DynamicLinkInfoOut"] = t.struct(
        {
            "socialMetaTagInfo": t.proxy(renames["SocialMetaTagInfoOut"]).optional(),
            "domainUriPrefix": t.string().optional(),
            "dynamicLinkDomain": t.string().optional(),
            "navigationInfo": t.proxy(renames["NavigationInfoOut"]).optional(),
            "androidInfo": t.proxy(renames["AndroidInfoOut"]).optional(),
            "link": t.string().optional(),
            "iosInfo": t.proxy(renames["IosInfoOut"]).optional(),
            "desktopInfo": t.proxy(renames["DesktopInfoOut"]).optional(),
            "analyticsInfo": t.proxy(renames["AnalyticsInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkInfoOut"])
    types["GetIosPostInstallAttributionRequestIn"] = t.struct(
        {
            "device": t.proxy(renames["DeviceInfoIn"]).optional(),
            "sdkVersion": t.string().optional(),
            "uniqueMatchLinkToCheck": t.string().optional(),
            "visualStyle": t.string().optional(),
            "appInstallationTime": t.string().optional(),
            "bundleId": t.string().optional(),
            "iosVersion": t.string().optional(),
            "retrievalMethod": t.string().optional(),
        }
    ).named(renames["GetIosPostInstallAttributionRequestIn"])
    types["GetIosPostInstallAttributionRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["DeviceInfoOut"]).optional(),
            "sdkVersion": t.string().optional(),
            "uniqueMatchLinkToCheck": t.string().optional(),
            "visualStyle": t.string().optional(),
            "appInstallationTime": t.string().optional(),
            "bundleId": t.string().optional(),
            "iosVersion": t.string().optional(),
            "retrievalMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosPostInstallAttributionRequestOut"])
    types["DeviceInfoIn"] = t.struct(
        {
            "languageCodeFromWebview": t.string().optional(),
            "timezone": t.string().optional(),
            "languageCodeRaw": t.string().optional(),
            "languageCode": t.string().optional(),
            "screenResolutionWidth": t.string().optional(),
            "screenResolutionHeight": t.string().optional(),
            "deviceModelName": t.string().optional(),
        }
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "languageCodeFromWebview": t.string().optional(),
            "timezone": t.string().optional(),
            "languageCodeRaw": t.string().optional(),
            "languageCode": t.string().optional(),
            "screenResolutionWidth": t.string().optional(),
            "screenResolutionHeight": t.string().optional(),
            "deviceModelName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceInfoOut"])
    types["SuffixIn"] = t.struct(
        {"option": t.string().optional(), "customSuffix": t.string().optional()}
    ).named(renames["SuffixIn"])
    types["SuffixOut"] = t.struct(
        {
            "option": t.string().optional(),
            "customSuffix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SuffixOut"])
    types["ManagedShortLinkIn"] = t.struct(
        {
            "creationTime": t.string().optional(),
            "info": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "flaggedAttribute": t.array(t.string()).optional(),
            "linkName": t.string().optional(),
            "visibility": t.string().optional(),
            "link": t.string().optional(),
        }
    ).named(renames["ManagedShortLinkIn"])
    types["ManagedShortLinkOut"] = t.struct(
        {
            "creationTime": t.string().optional(),
            "info": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "flaggedAttribute": t.array(t.string()).optional(),
            "linkName": t.string().optional(),
            "visibility": t.string().optional(),
            "link": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedShortLinkOut"])
    types["DesktopInfoIn"] = t.struct(
        {"desktopFallbackLink": t.string().optional()}
    ).named(renames["DesktopInfoIn"])
    types["DesktopInfoOut"] = t.struct(
        {
            "desktopFallbackLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DesktopInfoOut"])
    types["AndroidInfoIn"] = t.struct(
        {
            "androidMinPackageVersionCode": t.string().optional(),
            "androidFallbackLink": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "androidLink": t.string().optional(),
        }
    ).named(renames["AndroidInfoIn"])
    types["AndroidInfoOut"] = t.struct(
        {
            "androidMinPackageVersionCode": t.string().optional(),
            "androidFallbackLink": t.string().optional(),
            "androidPackageName": t.string().optional(),
            "androidLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidInfoOut"])
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
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "sdkVersion": t.string().optional(),
            "longDynamicLink": t.string().optional(),
            "suffix": t.proxy(renames["SuffixIn"]).optional(),
        }
    ).named(renames["CreateShortDynamicLinkRequestIn"])
    types["CreateShortDynamicLinkRequestOut"] = t.struct(
        {
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "sdkVersion": t.string().optional(),
            "longDynamicLink": t.string().optional(),
            "suffix": t.proxy(renames["SuffixOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShortDynamicLinkRequestOut"])
    types["DynamicLinkWarningIn"] = t.struct(
        {
            "warningMessage": t.string().optional(),
            "warningCode": t.string().optional(),
            "warningDocumentLink": t.string().optional(),
        }
    ).named(renames["DynamicLinkWarningIn"])
    types["DynamicLinkWarningOut"] = t.struct(
        {
            "warningMessage": t.string().optional(),
            "warningCode": t.string().optional(),
            "warningDocumentLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkWarningOut"])
    types["SocialMetaTagInfoIn"] = t.struct(
        {
            "socialDescription": t.string().optional(),
            "socialImageLink": t.string().optional(),
            "socialTitle": t.string().optional(),
        }
    ).named(renames["SocialMetaTagInfoIn"])
    types["SocialMetaTagInfoOut"] = t.struct(
        {
            "socialDescription": t.string().optional(),
            "socialImageLink": t.string().optional(),
            "socialTitle": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocialMetaTagInfoOut"])
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
    types["GetIosPostInstallAttributionResponseIn"] = t.struct(
        {
            "requestedLink": t.string().optional(),
            "deepLink": t.string().optional(),
            "attributionConfidence": t.string().optional(),
            "invitationId": t.string().optional(),
            "externalBrowserDestinationLink": t.string().optional(),
            "requestIpVersion": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "fallbackLink": t.string().optional(),
            "utmSource": t.string().optional(),
            "isStrongMatchExecutable": t.boolean().optional(),
            "matchMessage": t.string().optional(),
            "appMinimumVersion": t.string().optional(),
        }
    ).named(renames["GetIosPostInstallAttributionResponseIn"])
    types["GetIosPostInstallAttributionResponseOut"] = t.struct(
        {
            "requestedLink": t.string().optional(),
            "deepLink": t.string().optional(),
            "attributionConfidence": t.string().optional(),
            "invitationId": t.string().optional(),
            "externalBrowserDestinationLink": t.string().optional(),
            "requestIpVersion": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "fallbackLink": t.string().optional(),
            "utmSource": t.string().optional(),
            "isStrongMatchExecutable": t.boolean().optional(),
            "matchMessage": t.string().optional(),
            "appMinimumVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosPostInstallAttributionResponseOut"])
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
    types["CreateShortDynamicLinkResponseIn"] = t.struct(
        {
            "previewLink": t.string().optional(),
            "shortLink": t.string().optional(),
            "warning": t.array(t.proxy(renames["DynamicLinkWarningIn"])).optional(),
        }
    ).named(renames["CreateShortDynamicLinkResponseIn"])
    types["CreateShortDynamicLinkResponseOut"] = t.struct(
        {
            "previewLink": t.string().optional(),
            "shortLink": t.string().optional(),
            "warning": t.array(t.proxy(renames["DynamicLinkWarningOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShortDynamicLinkResponseOut"])
    types["NavigationInfoIn"] = t.struct(
        {"enableForcedRedirect": t.boolean().optional()}
    ).named(renames["NavigationInfoIn"])
    types["NavigationInfoOut"] = t.struct(
        {
            "enableForcedRedirect": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NavigationInfoOut"])
    types["GooglePlayAnalyticsIn"] = t.struct(
        {
            "gclid": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmCampaign": t.string().optional(),
        }
    ).named(renames["GooglePlayAnalyticsIn"])
    types["GooglePlayAnalyticsOut"] = t.struct(
        {
            "gclid": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayAnalyticsOut"])

    functions = {}
    functions["managedShortLinksCreate"] = firebasedynamiclinks.post(
        "v1/managedShortLinks:create",
        t.struct(
            {
                "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
                "sdkVersion": t.string().optional(),
                "longDynamicLink": t.string().optional(),
                "name": t.string().optional(),
                "suffix": t.proxy(renames["SuffixIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateManagedShortLinkResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shortLinksCreate"] = firebasedynamiclinks.post(
        "v1/shortLinks",
        t.struct(
            {
                "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
                "sdkVersion": t.string().optional(),
                "longDynamicLink": t.string().optional(),
                "suffix": t.proxy(renames["SuffixIn"]).optional(),
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

    return Import(
        importer="firebasedynamiclinks",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
