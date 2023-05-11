from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_firebasedynamiclinks() -> Import:
    firebasedynamiclinks = HTTPRuntime("https://firebasedynamiclinks.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasedynamiclinks_1_ErrorResponse",
        "DynamicLinkWarningIn": "_firebasedynamiclinks_2_DynamicLinkWarningIn",
        "DynamicLinkWarningOut": "_firebasedynamiclinks_3_DynamicLinkWarningOut",
        "ITunesConnectAnalyticsIn": "_firebasedynamiclinks_4_ITunesConnectAnalyticsIn",
        "ITunesConnectAnalyticsOut": "_firebasedynamiclinks_5_ITunesConnectAnalyticsOut",
        "GetIosPostInstallAttributionRequestIn": "_firebasedynamiclinks_6_GetIosPostInstallAttributionRequestIn",
        "GetIosPostInstallAttributionRequestOut": "_firebasedynamiclinks_7_GetIosPostInstallAttributionRequestOut",
        "CreateManagedShortLinkResponseIn": "_firebasedynamiclinks_8_CreateManagedShortLinkResponseIn",
        "CreateManagedShortLinkResponseOut": "_firebasedynamiclinks_9_CreateManagedShortLinkResponseOut",
        "CreateManagedShortLinkRequestIn": "_firebasedynamiclinks_10_CreateManagedShortLinkRequestIn",
        "CreateManagedShortLinkRequestOut": "_firebasedynamiclinks_11_CreateManagedShortLinkRequestOut",
        "ManagedShortLinkIn": "_firebasedynamiclinks_12_ManagedShortLinkIn",
        "ManagedShortLinkOut": "_firebasedynamiclinks_13_ManagedShortLinkOut",
        "AnalyticsInfoIn": "_firebasedynamiclinks_14_AnalyticsInfoIn",
        "AnalyticsInfoOut": "_firebasedynamiclinks_15_AnalyticsInfoOut",
        "DeviceInfoIn": "_firebasedynamiclinks_16_DeviceInfoIn",
        "DeviceInfoOut": "_firebasedynamiclinks_17_DeviceInfoOut",
        "DesktopInfoIn": "_firebasedynamiclinks_18_DesktopInfoIn",
        "DesktopInfoOut": "_firebasedynamiclinks_19_DesktopInfoOut",
        "GetIosReopenAttributionRequestIn": "_firebasedynamiclinks_20_GetIosReopenAttributionRequestIn",
        "GetIosReopenAttributionRequestOut": "_firebasedynamiclinks_21_GetIosReopenAttributionRequestOut",
        "SocialMetaTagInfoIn": "_firebasedynamiclinks_22_SocialMetaTagInfoIn",
        "SocialMetaTagInfoOut": "_firebasedynamiclinks_23_SocialMetaTagInfoOut",
        "NavigationInfoIn": "_firebasedynamiclinks_24_NavigationInfoIn",
        "NavigationInfoOut": "_firebasedynamiclinks_25_NavigationInfoOut",
        "IosInfoIn": "_firebasedynamiclinks_26_IosInfoIn",
        "IosInfoOut": "_firebasedynamiclinks_27_IosInfoOut",
        "CreateShortDynamicLinkRequestIn": "_firebasedynamiclinks_28_CreateShortDynamicLinkRequestIn",
        "CreateShortDynamicLinkRequestOut": "_firebasedynamiclinks_29_CreateShortDynamicLinkRequestOut",
        "AndroidInfoIn": "_firebasedynamiclinks_30_AndroidInfoIn",
        "AndroidInfoOut": "_firebasedynamiclinks_31_AndroidInfoOut",
        "DynamicLinkEventStatIn": "_firebasedynamiclinks_32_DynamicLinkEventStatIn",
        "DynamicLinkEventStatOut": "_firebasedynamiclinks_33_DynamicLinkEventStatOut",
        "DynamicLinkStatsIn": "_firebasedynamiclinks_34_DynamicLinkStatsIn",
        "DynamicLinkStatsOut": "_firebasedynamiclinks_35_DynamicLinkStatsOut",
        "GetIosReopenAttributionResponseIn": "_firebasedynamiclinks_36_GetIosReopenAttributionResponseIn",
        "GetIosReopenAttributionResponseOut": "_firebasedynamiclinks_37_GetIosReopenAttributionResponseOut",
        "GetIosPostInstallAttributionResponseIn": "_firebasedynamiclinks_38_GetIosPostInstallAttributionResponseIn",
        "GetIosPostInstallAttributionResponseOut": "_firebasedynamiclinks_39_GetIosPostInstallAttributionResponseOut",
        "GooglePlayAnalyticsIn": "_firebasedynamiclinks_40_GooglePlayAnalyticsIn",
        "GooglePlayAnalyticsOut": "_firebasedynamiclinks_41_GooglePlayAnalyticsOut",
        "CreateShortDynamicLinkResponseIn": "_firebasedynamiclinks_42_CreateShortDynamicLinkResponseIn",
        "CreateShortDynamicLinkResponseOut": "_firebasedynamiclinks_43_CreateShortDynamicLinkResponseOut",
        "SuffixIn": "_firebasedynamiclinks_44_SuffixIn",
        "SuffixOut": "_firebasedynamiclinks_45_SuffixOut",
        "DynamicLinkInfoIn": "_firebasedynamiclinks_46_DynamicLinkInfoIn",
        "DynamicLinkInfoOut": "_firebasedynamiclinks_47_DynamicLinkInfoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DynamicLinkWarningIn"] = t.struct(
        {
            "warningDocumentLink": t.string().optional(),
            "warningCode": t.string().optional(),
            "warningMessage": t.string().optional(),
        }
    ).named(renames["DynamicLinkWarningIn"])
    types["DynamicLinkWarningOut"] = t.struct(
        {
            "warningDocumentLink": t.string().optional(),
            "warningCode": t.string().optional(),
            "warningMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkWarningOut"])
    types["ITunesConnectAnalyticsIn"] = t.struct(
        {
            "at": t.string().optional(),
            "pt": t.string().optional(),
            "ct": t.string().optional(),
            "mt": t.string().optional(),
        }
    ).named(renames["ITunesConnectAnalyticsIn"])
    types["ITunesConnectAnalyticsOut"] = t.struct(
        {
            "at": t.string().optional(),
            "pt": t.string().optional(),
            "ct": t.string().optional(),
            "mt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ITunesConnectAnalyticsOut"])
    types["GetIosPostInstallAttributionRequestIn"] = t.struct(
        {
            "device": t.proxy(renames["DeviceInfoIn"]).optional(),
            "iosVersion": t.string().optional(),
            "visualStyle": t.string().optional(),
            "bundleId": t.string().optional(),
            "appInstallationTime": t.string().optional(),
            "uniqueMatchLinkToCheck": t.string().optional(),
            "retrievalMethod": t.string().optional(),
            "sdkVersion": t.string().optional(),
        }
    ).named(renames["GetIosPostInstallAttributionRequestIn"])
    types["GetIosPostInstallAttributionRequestOut"] = t.struct(
        {
            "device": t.proxy(renames["DeviceInfoOut"]).optional(),
            "iosVersion": t.string().optional(),
            "visualStyle": t.string().optional(),
            "bundleId": t.string().optional(),
            "appInstallationTime": t.string().optional(),
            "uniqueMatchLinkToCheck": t.string().optional(),
            "retrievalMethod": t.string().optional(),
            "sdkVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosPostInstallAttributionRequestOut"])
    types["CreateManagedShortLinkResponseIn"] = t.struct(
        {
            "managedShortLink": t.proxy(renames["ManagedShortLinkIn"]).optional(),
            "warning": t.array(t.proxy(renames["DynamicLinkWarningIn"])).optional(),
            "previewLink": t.string().optional(),
        }
    ).named(renames["CreateManagedShortLinkResponseIn"])
    types["CreateManagedShortLinkResponseOut"] = t.struct(
        {
            "managedShortLink": t.proxy(renames["ManagedShortLinkOut"]).optional(),
            "warning": t.array(t.proxy(renames["DynamicLinkWarningOut"])).optional(),
            "previewLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkResponseOut"])
    types["CreateManagedShortLinkRequestIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "sdkVersion": t.string().optional(),
            "longDynamicLink": t.string().optional(),
            "suffix": t.proxy(renames["SuffixIn"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkRequestIn"])
    types["CreateManagedShortLinkRequestOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "sdkVersion": t.string().optional(),
            "longDynamicLink": t.string().optional(),
            "suffix": t.proxy(renames["SuffixOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateManagedShortLinkRequestOut"])
    types["ManagedShortLinkIn"] = t.struct(
        {
            "link": t.string().optional(),
            "visibility": t.string().optional(),
            "creationTime": t.string().optional(),
            "info": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "flaggedAttribute": t.array(t.string()).optional(),
            "linkName": t.string().optional(),
        }
    ).named(renames["ManagedShortLinkIn"])
    types["ManagedShortLinkOut"] = t.struct(
        {
            "link": t.string().optional(),
            "visibility": t.string().optional(),
            "creationTime": t.string().optional(),
            "info": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "flaggedAttribute": t.array(t.string()).optional(),
            "linkName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedShortLinkOut"])
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
    types["DeviceInfoIn"] = t.struct(
        {
            "screenResolutionWidth": t.string().optional(),
            "deviceModelName": t.string().optional(),
            "timezone": t.string().optional(),
            "languageCodeFromWebview": t.string().optional(),
            "languageCodeRaw": t.string().optional(),
            "languageCode": t.string().optional(),
            "screenResolutionHeight": t.string().optional(),
        }
    ).named(renames["DeviceInfoIn"])
    types["DeviceInfoOut"] = t.struct(
        {
            "screenResolutionWidth": t.string().optional(),
            "deviceModelName": t.string().optional(),
            "timezone": t.string().optional(),
            "languageCodeFromWebview": t.string().optional(),
            "languageCodeRaw": t.string().optional(),
            "languageCode": t.string().optional(),
            "screenResolutionHeight": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceInfoOut"])
    types["DesktopInfoIn"] = t.struct(
        {"desktopFallbackLink": t.string().optional()}
    ).named(renames["DesktopInfoIn"])
    types["DesktopInfoOut"] = t.struct(
        {
            "desktopFallbackLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DesktopInfoOut"])
    types["GetIosReopenAttributionRequestIn"] = t.struct(
        {
            "sdkVersion": t.string().optional(),
            "bundleId": t.string().optional(),
            "requestedLink": t.string().optional(),
        }
    ).named(renames["GetIosReopenAttributionRequestIn"])
    types["GetIosReopenAttributionRequestOut"] = t.struct(
        {
            "sdkVersion": t.string().optional(),
            "bundleId": t.string().optional(),
            "requestedLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosReopenAttributionRequestOut"])
    types["SocialMetaTagInfoIn"] = t.struct(
        {
            "socialTitle": t.string().optional(),
            "socialDescription": t.string().optional(),
            "socialImageLink": t.string().optional(),
        }
    ).named(renames["SocialMetaTagInfoIn"])
    types["SocialMetaTagInfoOut"] = t.struct(
        {
            "socialTitle": t.string().optional(),
            "socialDescription": t.string().optional(),
            "socialImageLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocialMetaTagInfoOut"])
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
            "iosIpadFallbackLink": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "iosCustomScheme": t.string().optional(),
            "iosMinimumVersion": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosIpadBundleId": t.string().optional(),
            "iosFallbackLink": t.string().optional(),
        }
    ).named(renames["IosInfoIn"])
    types["IosInfoOut"] = t.struct(
        {
            "iosIpadFallbackLink": t.string().optional(),
            "iosBundleId": t.string().optional(),
            "iosCustomScheme": t.string().optional(),
            "iosMinimumVersion": t.string().optional(),
            "iosAppStoreId": t.string().optional(),
            "iosIpadBundleId": t.string().optional(),
            "iosFallbackLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosInfoOut"])
    types["CreateShortDynamicLinkRequestIn"] = t.struct(
        {
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
            "sdkVersion": t.string().optional(),
            "suffix": t.proxy(renames["SuffixIn"]).optional(),
            "longDynamicLink": t.string().optional(),
        }
    ).named(renames["CreateShortDynamicLinkRequestIn"])
    types["CreateShortDynamicLinkRequestOut"] = t.struct(
        {
            "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoOut"]).optional(),
            "sdkVersion": t.string().optional(),
            "suffix": t.proxy(renames["SuffixOut"]).optional(),
            "longDynamicLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShortDynamicLinkRequestOut"])
    types["AndroidInfoIn"] = t.struct(
        {
            "androidPackageName": t.string().optional(),
            "androidLink": t.string().optional(),
            "androidMinPackageVersionCode": t.string().optional(),
            "androidFallbackLink": t.string().optional(),
        }
    ).named(renames["AndroidInfoIn"])
    types["AndroidInfoOut"] = t.struct(
        {
            "androidPackageName": t.string().optional(),
            "androidLink": t.string().optional(),
            "androidMinPackageVersionCode": t.string().optional(),
            "androidFallbackLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidInfoOut"])
    types["DynamicLinkEventStatIn"] = t.struct(
        {
            "event": t.string().optional(),
            "count": t.string().optional(),
            "platform": t.string().optional(),
        }
    ).named(renames["DynamicLinkEventStatIn"])
    types["DynamicLinkEventStatOut"] = t.struct(
        {
            "event": t.string().optional(),
            "count": t.string().optional(),
            "platform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkEventStatOut"])
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
    types["GetIosReopenAttributionResponseIn"] = t.struct(
        {
            "iosMinAppVersion": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "invitationId": t.string().optional(),
            "deepLink": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmTerm": t.string().optional(),
        }
    ).named(renames["GetIosReopenAttributionResponseIn"])
    types["GetIosReopenAttributionResponseOut"] = t.struct(
        {
            "iosMinAppVersion": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "invitationId": t.string().optional(),
            "deepLink": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmTerm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosReopenAttributionResponseOut"])
    types["GetIosPostInstallAttributionResponseIn"] = t.struct(
        {
            "isStrongMatchExecutable": t.boolean().optional(),
            "externalBrowserDestinationLink": t.string().optional(),
            "invitationId": t.string().optional(),
            "deepLink": t.string().optional(),
            "utmContent": t.string().optional(),
            "matchMessage": t.string().optional(),
            "requestedLink": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmMedium": t.string().optional(),
            "attributionConfidence": t.string().optional(),
            "utmTerm": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "appMinimumVersion": t.string().optional(),
            "fallbackLink": t.string().optional(),
            "requestIpVersion": t.string().optional(),
        }
    ).named(renames["GetIosPostInstallAttributionResponseIn"])
    types["GetIosPostInstallAttributionResponseOut"] = t.struct(
        {
            "isStrongMatchExecutable": t.boolean().optional(),
            "externalBrowserDestinationLink": t.string().optional(),
            "invitationId": t.string().optional(),
            "deepLink": t.string().optional(),
            "utmContent": t.string().optional(),
            "matchMessage": t.string().optional(),
            "requestedLink": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmMedium": t.string().optional(),
            "attributionConfidence": t.string().optional(),
            "utmTerm": t.string().optional(),
            "resolvedLink": t.string().optional(),
            "appMinimumVersion": t.string().optional(),
            "fallbackLink": t.string().optional(),
            "requestIpVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIosPostInstallAttributionResponseOut"])
    types["GooglePlayAnalyticsIn"] = t.struct(
        {
            "gclid": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmCampaign": t.string().optional(),
        }
    ).named(renames["GooglePlayAnalyticsIn"])
    types["GooglePlayAnalyticsOut"] = t.struct(
        {
            "gclid": t.string().optional(),
            "utmSource": t.string().optional(),
            "utmTerm": t.string().optional(),
            "utmContent": t.string().optional(),
            "utmMedium": t.string().optional(),
            "utmCampaign": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GooglePlayAnalyticsOut"])
    types["CreateShortDynamicLinkResponseIn"] = t.struct(
        {
            "warning": t.array(t.proxy(renames["DynamicLinkWarningIn"])).optional(),
            "previewLink": t.string().optional(),
            "shortLink": t.string().optional(),
        }
    ).named(renames["CreateShortDynamicLinkResponseIn"])
    types["CreateShortDynamicLinkResponseOut"] = t.struct(
        {
            "warning": t.array(t.proxy(renames["DynamicLinkWarningOut"])).optional(),
            "previewLink": t.string().optional(),
            "shortLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateShortDynamicLinkResponseOut"])
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
    types["DynamicLinkInfoIn"] = t.struct(
        {
            "link": t.string().optional(),
            "analyticsInfo": t.proxy(renames["AnalyticsInfoIn"]).optional(),
            "androidInfo": t.proxy(renames["AndroidInfoIn"]).optional(),
            "navigationInfo": t.proxy(renames["NavigationInfoIn"]).optional(),
            "domainUriPrefix": t.string().optional(),
            "iosInfo": t.proxy(renames["IosInfoIn"]).optional(),
            "dynamicLinkDomain": t.string().optional(),
            "desktopInfo": t.proxy(renames["DesktopInfoIn"]).optional(),
            "socialMetaTagInfo": t.proxy(renames["SocialMetaTagInfoIn"]).optional(),
        }
    ).named(renames["DynamicLinkInfoIn"])
    types["DynamicLinkInfoOut"] = t.struct(
        {
            "link": t.string().optional(),
            "analyticsInfo": t.proxy(renames["AnalyticsInfoOut"]).optional(),
            "androidInfo": t.proxy(renames["AndroidInfoOut"]).optional(),
            "navigationInfo": t.proxy(renames["NavigationInfoOut"]).optional(),
            "domainUriPrefix": t.string().optional(),
            "iosInfo": t.proxy(renames["IosInfoOut"]).optional(),
            "dynamicLinkDomain": t.string().optional(),
            "desktopInfo": t.proxy(renames["DesktopInfoOut"]).optional(),
            "socialMetaTagInfo": t.proxy(renames["SocialMetaTagInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicLinkInfoOut"])

    functions = {}
    functions["managedShortLinksCreate"] = firebasedynamiclinks.post(
        "v1/managedShortLinks:create",
        t.struct(
            {
                "name": t.string().optional(),
                "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
                "sdkVersion": t.string().optional(),
                "longDynamicLink": t.string().optional(),
                "suffix": t.proxy(renames["SuffixIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateManagedShortLinkResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1GetLinkStats"] = firebasedynamiclinks.post(
        "v1/installAttribution",
        t.struct(
            {
                "device": t.proxy(renames["DeviceInfoIn"]).optional(),
                "iosVersion": t.string().optional(),
                "visualStyle": t.string().optional(),
                "bundleId": t.string().optional(),
                "appInstallationTime": t.string().optional(),
                "uniqueMatchLinkToCheck": t.string().optional(),
                "retrievalMethod": t.string().optional(),
                "sdkVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetIosPostInstallAttributionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1ReopenAttribution"] = firebasedynamiclinks.post(
        "v1/installAttribution",
        t.struct(
            {
                "device": t.proxy(renames["DeviceInfoIn"]).optional(),
                "iosVersion": t.string().optional(),
                "visualStyle": t.string().optional(),
                "bundleId": t.string().optional(),
                "appInstallationTime": t.string().optional(),
                "uniqueMatchLinkToCheck": t.string().optional(),
                "retrievalMethod": t.string().optional(),
                "sdkVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetIosPostInstallAttributionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["v1InstallAttribution"] = firebasedynamiclinks.post(
        "v1/installAttribution",
        t.struct(
            {
                "device": t.proxy(renames["DeviceInfoIn"]).optional(),
                "iosVersion": t.string().optional(),
                "visualStyle": t.string().optional(),
                "bundleId": t.string().optional(),
                "appInstallationTime": t.string().optional(),
                "uniqueMatchLinkToCheck": t.string().optional(),
                "retrievalMethod": t.string().optional(),
                "sdkVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GetIosPostInstallAttributionResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["shortLinksCreate"] = firebasedynamiclinks.post(
        "v1/shortLinks",
        t.struct(
            {
                "dynamicLinkInfo": t.proxy(renames["DynamicLinkInfoIn"]).optional(),
                "sdkVersion": t.string().optional(),
                "suffix": t.proxy(renames["SuffixIn"]).optional(),
                "longDynamicLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CreateShortDynamicLinkResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebasedynamiclinks",
        renames=renames,
        types=types,
        functions=functions,
    )
