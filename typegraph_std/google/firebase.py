from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_firebase() -> Import:
    firebase = HTTPRuntime("https://firebase.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebase_1_ErrorResponse",
        "RemoveWebAppRequestIn": "_firebase_2_RemoveWebAppRequestIn",
        "RemoveWebAppRequestOut": "_firebase_3_RemoveWebAppRequestOut",
        "AnalyticsDetailsIn": "_firebase_4_AnalyticsDetailsIn",
        "AnalyticsDetailsOut": "_firebase_5_AnalyticsDetailsOut",
        "ListFirebaseProjectsResponseIn": "_firebase_6_ListFirebaseProjectsResponseIn",
        "ListFirebaseProjectsResponseOut": "_firebase_7_ListFirebaseProjectsResponseOut",
        "ProjectInfoIn": "_firebase_8_ProjectInfoIn",
        "ProjectInfoOut": "_firebase_9_ProjectInfoOut",
        "AddFirebaseRequestIn": "_firebase_10_AddFirebaseRequestIn",
        "AddFirebaseRequestOut": "_firebase_11_AddFirebaseRequestOut",
        "RemoveIosAppRequestIn": "_firebase_12_RemoveIosAppRequestIn",
        "RemoveIosAppRequestOut": "_firebase_13_RemoveIosAppRequestOut",
        "AndroidAppIn": "_firebase_14_AndroidAppIn",
        "AndroidAppOut": "_firebase_15_AndroidAppOut",
        "RemoveAndroidAppRequestIn": "_firebase_16_RemoveAndroidAppRequestIn",
        "RemoveAndroidAppRequestOut": "_firebase_17_RemoveAndroidAppRequestOut",
        "AddGoogleAnalyticsRequestIn": "_firebase_18_AddGoogleAnalyticsRequestIn",
        "AddGoogleAnalyticsRequestOut": "_firebase_19_AddGoogleAnalyticsRequestOut",
        "ListAndroidAppsResponseIn": "_firebase_20_ListAndroidAppsResponseIn",
        "ListAndroidAppsResponseOut": "_firebase_21_ListAndroidAppsResponseOut",
        "SearchFirebaseAppsResponseIn": "_firebase_22_SearchFirebaseAppsResponseIn",
        "SearchFirebaseAppsResponseOut": "_firebase_23_SearchFirebaseAppsResponseOut",
        "FirebaseAppInfoIn": "_firebase_24_FirebaseAppInfoIn",
        "FirebaseAppInfoOut": "_firebase_25_FirebaseAppInfoOut",
        "AndroidAppConfigIn": "_firebase_26_AndroidAppConfigIn",
        "AndroidAppConfigOut": "_firebase_27_AndroidAppConfigOut",
        "LocationIn": "_firebase_28_LocationIn",
        "LocationOut": "_firebase_29_LocationOut",
        "RemoveAnalyticsRequestIn": "_firebase_30_RemoveAnalyticsRequestIn",
        "RemoveAnalyticsRequestOut": "_firebase_31_RemoveAnalyticsRequestOut",
        "DefaultResourcesIn": "_firebase_32_DefaultResourcesIn",
        "DefaultResourcesOut": "_firebase_33_DefaultResourcesOut",
        "ListAvailableProjectsResponseIn": "_firebase_34_ListAvailableProjectsResponseIn",
        "ListAvailableProjectsResponseOut": "_firebase_35_ListAvailableProjectsResponseOut",
        "IosAppIn": "_firebase_36_IosAppIn",
        "IosAppOut": "_firebase_37_IosAppOut",
        "WebAppIn": "_firebase_38_WebAppIn",
        "WebAppOut": "_firebase_39_WebAppOut",
        "StreamMappingIn": "_firebase_40_StreamMappingIn",
        "StreamMappingOut": "_firebase_41_StreamMappingOut",
        "AdminSdkConfigIn": "_firebase_42_AdminSdkConfigIn",
        "AdminSdkConfigOut": "_firebase_43_AdminSdkConfigOut",
        "FinalizeDefaultLocationRequestIn": "_firebase_44_FinalizeDefaultLocationRequestIn",
        "FinalizeDefaultLocationRequestOut": "_firebase_45_FinalizeDefaultLocationRequestOut",
        "IosAppConfigIn": "_firebase_46_IosAppConfigIn",
        "IosAppConfigOut": "_firebase_47_IosAppConfigOut",
        "FirebaseProjectIn": "_firebase_48_FirebaseProjectIn",
        "FirebaseProjectOut": "_firebase_49_FirebaseProjectOut",
        "AnalyticsPropertyIn": "_firebase_50_AnalyticsPropertyIn",
        "AnalyticsPropertyOut": "_firebase_51_AnalyticsPropertyOut",
        "UndeleteAndroidAppRequestIn": "_firebase_52_UndeleteAndroidAppRequestIn",
        "UndeleteAndroidAppRequestOut": "_firebase_53_UndeleteAndroidAppRequestOut",
        "ListShaCertificatesResponseIn": "_firebase_54_ListShaCertificatesResponseIn",
        "ListShaCertificatesResponseOut": "_firebase_55_ListShaCertificatesResponseOut",
        "ListWebAppsResponseIn": "_firebase_56_ListWebAppsResponseIn",
        "ListWebAppsResponseOut": "_firebase_57_ListWebAppsResponseOut",
        "ShaCertificateIn": "_firebase_58_ShaCertificateIn",
        "ShaCertificateOut": "_firebase_59_ShaCertificateOut",
        "UndeleteWebAppRequestIn": "_firebase_60_UndeleteWebAppRequestIn",
        "UndeleteWebAppRequestOut": "_firebase_61_UndeleteWebAppRequestOut",
        "EmptyIn": "_firebase_62_EmptyIn",
        "EmptyOut": "_firebase_63_EmptyOut",
        "ListIosAppsResponseIn": "_firebase_64_ListIosAppsResponseIn",
        "ListIosAppsResponseOut": "_firebase_65_ListIosAppsResponseOut",
        "ListAvailableLocationsResponseIn": "_firebase_66_ListAvailableLocationsResponseIn",
        "ListAvailableLocationsResponseOut": "_firebase_67_ListAvailableLocationsResponseOut",
        "StatusIn": "_firebase_68_StatusIn",
        "StatusOut": "_firebase_69_StatusOut",
        "UndeleteIosAppRequestIn": "_firebase_70_UndeleteIosAppRequestIn",
        "UndeleteIosAppRequestOut": "_firebase_71_UndeleteIosAppRequestOut",
        "MessageSetIn": "_firebase_72_MessageSetIn",
        "MessageSetOut": "_firebase_73_MessageSetOut",
        "ProductMetadataIn": "_firebase_74_ProductMetadataIn",
        "ProductMetadataOut": "_firebase_75_ProductMetadataOut",
        "OperationIn": "_firebase_76_OperationIn",
        "OperationOut": "_firebase_77_OperationOut",
        "WebAppConfigIn": "_firebase_78_WebAppConfigIn",
        "WebAppConfigOut": "_firebase_79_WebAppConfigOut",
        "StatusProtoIn": "_firebase_80_StatusProtoIn",
        "StatusProtoOut": "_firebase_81_StatusProtoOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RemoveWebAppRequestIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
        }
    ).named(renames["RemoveWebAppRequestIn"])
    types["RemoveWebAppRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveWebAppRequestOut"])
    types["AnalyticsDetailsIn"] = t.struct(
        {
            "streamMappings": t.array(t.proxy(renames["StreamMappingIn"])).optional(),
            "analyticsProperty": t.proxy(renames["AnalyticsPropertyIn"]).optional(),
        }
    ).named(renames["AnalyticsDetailsIn"])
    types["AnalyticsDetailsOut"] = t.struct(
        {
            "streamMappings": t.array(t.proxy(renames["StreamMappingOut"])).optional(),
            "analyticsProperty": t.proxy(renames["AnalyticsPropertyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyticsDetailsOut"])
    types["ListFirebaseProjectsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["FirebaseProjectIn"])).optional(),
        }
    ).named(renames["ListFirebaseProjectsResponseIn"])
    types["ListFirebaseProjectsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "results": t.array(t.proxy(renames["FirebaseProjectOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFirebaseProjectsResponseOut"])
    types["ProjectInfoIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "project": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ProjectInfoIn"])
    types["ProjectInfoOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "project": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectInfoOut"])
    types["AddFirebaseRequestIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["AddFirebaseRequestIn"])
    types["AddFirebaseRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFirebaseRequestOut"])
    types["RemoveIosAppRequestIn"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["RemoveIosAppRequestIn"])
    types["RemoveIosAppRequestOut"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveIosAppRequestOut"])
    types["AndroidAppIn"] = t.struct(
        {
            "apiKeyId": t.string().optional(),
            "sha256Hashes": t.array(t.string()).optional(),
            "sha1Hashes": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AndroidAppIn"])
    types["AndroidAppOut"] = t.struct(
        {
            "apiKeyId": t.string().optional(),
            "sha256Hashes": t.array(t.string()).optional(),
            "sha1Hashes": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "displayName": t.string().optional(),
            "projectId": t.string().optional(),
            "appId": t.string().optional(),
            "etag": t.string().optional(),
            "expireTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppOut"])
    types["RemoveAndroidAppRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "immediate": t.boolean().optional(),
        }
    ).named(renames["RemoveAndroidAppRequestIn"])
    types["RemoveAndroidAppRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "immediate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveAndroidAppRequestOut"])
    types["AddGoogleAnalyticsRequestIn"] = t.struct(
        {
            "analyticsPropertyId": t.string().optional(),
            "analyticsAccountId": t.string().optional(),
        }
    ).named(renames["AddGoogleAnalyticsRequestIn"])
    types["AddGoogleAnalyticsRequestOut"] = t.struct(
        {
            "analyticsPropertyId": t.string().optional(),
            "analyticsAccountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddGoogleAnalyticsRequestOut"])
    types["ListAndroidAppsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["AndroidAppIn"])).optional(),
        }
    ).named(renames["ListAndroidAppsResponseIn"])
    types["ListAndroidAppsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["AndroidAppOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAndroidAppsResponseOut"])
    types["SearchFirebaseAppsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["FirebaseAppInfoIn"])).optional(),
        }
    ).named(renames["SearchFirebaseAppsResponseIn"])
    types["SearchFirebaseAppsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["FirebaseAppInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchFirebaseAppsResponseOut"])
    types["FirebaseAppInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "platform": t.string().optional(),
            "apiKeyId": t.string().optional(),
        }
    ).named(renames["FirebaseAppInfoIn"])
    types["FirebaseAppInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
            "displayName": t.string().optional(),
            "namespace": t.string().optional(),
            "appId": t.string().optional(),
            "state": t.string().optional(),
            "platform": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirebaseAppInfoOut"])
    types["AndroidAppConfigIn"] = t.struct(
        {
            "configFilename": t.string().optional(),
            "configFileContents": t.string().optional(),
        }
    ).named(renames["AndroidAppConfigIn"])
    types["AndroidAppConfigOut"] = t.struct(
        {
            "configFilename": t.string().optional(),
            "configFileContents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppConfigOut"])
    types["LocationIn"] = t.struct(
        {
            "type": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "type": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["RemoveAnalyticsRequestIn"] = t.struct(
        {"analyticsPropertyId": t.string().optional()}
    ).named(renames["RemoveAnalyticsRequestIn"])
    types["RemoveAnalyticsRequestOut"] = t.struct(
        {
            "analyticsPropertyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveAnalyticsRequestOut"])
    types["DefaultResourcesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DefaultResourcesIn"]
    )
    types["DefaultResourcesOut"] = t.struct(
        {
            "hostingSite": t.string().optional(),
            "storageBucket": t.string().optional(),
            "realtimeDatabaseInstance": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultResourcesOut"])
    types["ListAvailableProjectsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "projectInfo": t.array(t.proxy(renames["ProjectInfoIn"])).optional(),
        }
    ).named(renames["ListAvailableProjectsResponseIn"])
    types["ListAvailableProjectsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "projectInfo": t.array(t.proxy(renames["ProjectInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAvailableProjectsResponseOut"])
    types["IosAppIn"] = t.struct(
        {
            "apiKeyId": t.string().optional(),
            "teamId": t.string().optional(),
            "appStoreId": t.string().optional(),
            "bundleId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["IosAppIn"])
    types["IosAppOut"] = t.struct(
        {
            "apiKeyId": t.string().optional(),
            "appId": t.string().optional(),
            "teamId": t.string().optional(),
            "appStoreId": t.string().optional(),
            "bundleId": t.string().optional(),
            "projectId": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "expireTime": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppOut"])
    types["WebAppIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "appUrls": t.array(t.string()).optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "state": t.string().optional(),
            "projectId": t.string().optional(),
            "appId": t.string().optional(),
            "expireTime": t.string().optional(),
            "webId": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "appUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
    types["StreamMappingIn"] = t.struct(
        {
            "app": t.string().optional(),
            "measurementId": t.string().optional(),
            "streamId": t.string().optional(),
        }
    ).named(renames["StreamMappingIn"])
    types["StreamMappingOut"] = t.struct(
        {
            "app": t.string().optional(),
            "measurementId": t.string().optional(),
            "streamId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamMappingOut"])
    types["AdminSdkConfigIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "databaseURL": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["AdminSdkConfigIn"])
    types["AdminSdkConfigOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "databaseURL": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminSdkConfigOut"])
    types["FinalizeDefaultLocationRequestIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["FinalizeDefaultLocationRequestIn"])
    types["FinalizeDefaultLocationRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FinalizeDefaultLocationRequestOut"])
    types["IosAppConfigIn"] = t.struct(
        {
            "configFilename": t.string().optional(),
            "configFileContents": t.string().optional(),
        }
    ).named(renames["IosAppConfigIn"])
    types["IosAppConfigOut"] = t.struct(
        {
            "configFilename": t.string().optional(),
            "configFileContents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppConfigOut"])
    types["FirebaseProjectIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["FirebaseProjectIn"])
    types["FirebaseProjectOut"] = t.struct(
        {
            "projectNumber": t.string().optional(),
            "state": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "resources": t.proxy(renames["DefaultResourcesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirebaseProjectOut"])
    types["AnalyticsPropertyIn"] = t.struct(
        {"displayName": t.string().optional(), "id": t.string().optional()}
    ).named(renames["AnalyticsPropertyIn"])
    types["AnalyticsPropertyOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "analyticsAccountId": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyticsPropertyOut"])
    types["UndeleteAndroidAppRequestIn"] = t.struct(
        {"etag": t.string().optional(), "validateOnly": t.boolean().optional()}
    ).named(renames["UndeleteAndroidAppRequestIn"])
    types["UndeleteAndroidAppRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteAndroidAppRequestOut"])
    types["ListShaCertificatesResponseIn"] = t.struct(
        {"certificates": t.array(t.proxy(renames["ShaCertificateIn"])).optional()}
    ).named(renames["ListShaCertificatesResponseIn"])
    types["ListShaCertificatesResponseOut"] = t.struct(
        {
            "certificates": t.array(t.proxy(renames["ShaCertificateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListShaCertificatesResponseOut"])
    types["ListWebAppsResponseIn"] = t.struct(
        {
            "apps": t.array(t.proxy(renames["WebAppIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListWebAppsResponseIn"])
    types["ListWebAppsResponseOut"] = t.struct(
        {
            "apps": t.array(t.proxy(renames["WebAppOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWebAppsResponseOut"])
    types["ShaCertificateIn"] = t.struct(
        {
            "name": t.string().optional(),
            "certType": t.string().optional(),
            "shaHash": t.string().optional(),
        }
    ).named(renames["ShaCertificateIn"])
    types["ShaCertificateOut"] = t.struct(
        {
            "name": t.string().optional(),
            "certType": t.string().optional(),
            "shaHash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShaCertificateOut"])
    types["UndeleteWebAppRequestIn"] = t.struct(
        {"etag": t.string().optional(), "validateOnly": t.boolean().optional()}
    ).named(renames["UndeleteWebAppRequestIn"])
    types["UndeleteWebAppRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteWebAppRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListIosAppsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["IosAppIn"])).optional(),
        }
    ).named(renames["ListIosAppsResponseIn"])
    types["ListIosAppsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["IosAppOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListIosAppsResponseOut"])
    types["ListAvailableLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAvailableLocationsResponseIn"])
    types["ListAvailableLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAvailableLocationsResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["UndeleteIosAppRequestIn"] = t.struct(
        {"validateOnly": t.boolean().optional(), "etag": t.string().optional()}
    ).named(renames["UndeleteIosAppRequestIn"])
    types["UndeleteIosAppRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteIosAppRequestOut"])
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
    types["ProductMetadataIn"] = t.struct(
        {"warningMessages": t.array(t.string()).optional()}
    ).named(renames["ProductMetadataIn"])
    types["ProductMetadataOut"] = t.struct(
        {
            "warningMessages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["WebAppConfigIn"] = t.struct(
        {
            "appId": t.string().optional(),
            "locationId": t.string().optional(),
            "measurementId": t.string().optional(),
            "messagingSenderId": t.string().optional(),
            "projectId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "apiKey": t.string().optional(),
            "databaseURL": t.string().optional(),
            "authDomain": t.string().optional(),
        }
    ).named(renames["WebAppConfigIn"])
    types["WebAppConfigOut"] = t.struct(
        {
            "appId": t.string().optional(),
            "locationId": t.string().optional(),
            "measurementId": t.string().optional(),
            "messagingSenderId": t.string().optional(),
            "projectId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "apiKey": t.string().optional(),
            "databaseURL": t.string().optional(),
            "authDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppConfigOut"])
    types["StatusProtoIn"] = t.struct(
        {
            "space": t.string().optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "canonicalCode": t.integer().optional(),
            "messageSet": t.proxy(renames["MessageSetIn"]).optional(),
        }
    ).named(renames["StatusProtoIn"])
    types["StatusProtoOut"] = t.struct(
        {
            "space": t.string().optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "canonicalCode": t.integer().optional(),
            "messageSet": t.proxy(renames["MessageSetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusProtoOut"])

    functions = {}
    functions["projectsGetAdminSdkConfig"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsList"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAddFirebase"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatch"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRemoveAnalytics"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSearchApps"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAddGoogleAnalytics"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetAnalyticsDetails"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsPatch"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsUndelete"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsList"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsCreate"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsGet"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsRemove"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsGetConfig"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAvailableLocationsList"] = firebase.get(
        "v1beta1/{parent}/availableLocations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAvailableLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsGetConfig"] = firebase.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiKeyId": t.string().optional(),
                "sha256Hashes": t.array(t.string()).optional(),
                "sha1Hashes": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AndroidAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsRemove"] = firebase.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiKeyId": t.string().optional(),
                "sha256Hashes": t.array(t.string()).optional(),
                "sha1Hashes": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AndroidAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsUndelete"] = firebase.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiKeyId": t.string().optional(),
                "sha256Hashes": t.array(t.string()).optional(),
                "sha1Hashes": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AndroidAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsGet"] = firebase.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiKeyId": t.string().optional(),
                "sha256Hashes": t.array(t.string()).optional(),
                "sha1Hashes": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AndroidAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsList"] = firebase.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiKeyId": t.string().optional(),
                "sha256Hashes": t.array(t.string()).optional(),
                "sha1Hashes": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AndroidAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsCreate"] = firebase.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiKeyId": t.string().optional(),
                "sha256Hashes": t.array(t.string()).optional(),
                "sha1Hashes": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AndroidAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsPatch"] = firebase.patch(
        "v1beta1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "apiKeyId": t.string().optional(),
                "sha256Hashes": t.array(t.string()).optional(),
                "sha1Hashes": t.array(t.string()).optional(),
                "packageName": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AndroidAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsShaCreate"] = firebase.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsShaList"] = firebase.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsShaDelete"] = firebase.delete(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDefaultLocationFinalize"] = firebase.post(
        "v1beta1/{parent}/defaultLocation:finalize",
        t.struct(
            {
                "parent": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsUndelete"] = firebase.get(
        "v1beta1/{parent}/iosApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIosAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsPatch"] = firebase.get(
        "v1beta1/{parent}/iosApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIosAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsCreate"] = firebase.get(
        "v1beta1/{parent}/iosApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIosAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsGet"] = firebase.get(
        "v1beta1/{parent}/iosApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIosAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsGetConfig"] = firebase.get(
        "v1beta1/{parent}/iosApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIosAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsRemove"] = firebase.get(
        "v1beta1/{parent}/iosApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIosAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsList"] = firebase.get(
        "v1beta1/{parent}/iosApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIosAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["availableProjectsList"] = firebase.get(
        "v1beta1/availableProjects",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAvailableProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebase", renames=renames, types=Box(types), functions=Box(functions)
    )
