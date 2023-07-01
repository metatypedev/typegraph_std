from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_firebase():
    firebase = HTTPRuntime("https://firebase.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebase_1_ErrorResponse",
        "ListShaCertificatesResponseIn": "_firebase_2_ListShaCertificatesResponseIn",
        "ListShaCertificatesResponseOut": "_firebase_3_ListShaCertificatesResponseOut",
        "FinalizeDefaultLocationRequestIn": "_firebase_4_FinalizeDefaultLocationRequestIn",
        "FinalizeDefaultLocationRequestOut": "_firebase_5_FinalizeDefaultLocationRequestOut",
        "ProjectInfoIn": "_firebase_6_ProjectInfoIn",
        "ProjectInfoOut": "_firebase_7_ProjectInfoOut",
        "DefaultResourcesIn": "_firebase_8_DefaultResourcesIn",
        "DefaultResourcesOut": "_firebase_9_DefaultResourcesOut",
        "FirebaseAppInfoIn": "_firebase_10_FirebaseAppInfoIn",
        "FirebaseAppInfoOut": "_firebase_11_FirebaseAppInfoOut",
        "ListIosAppsResponseIn": "_firebase_12_ListIosAppsResponseIn",
        "ListIosAppsResponseOut": "_firebase_13_ListIosAppsResponseOut",
        "RemoveAnalyticsRequestIn": "_firebase_14_RemoveAnalyticsRequestIn",
        "RemoveAnalyticsRequestOut": "_firebase_15_RemoveAnalyticsRequestOut",
        "ListWebAppsResponseIn": "_firebase_16_ListWebAppsResponseIn",
        "ListWebAppsResponseOut": "_firebase_17_ListWebAppsResponseOut",
        "AndroidAppConfigIn": "_firebase_18_AndroidAppConfigIn",
        "AndroidAppConfigOut": "_firebase_19_AndroidAppConfigOut",
        "LocationIn": "_firebase_20_LocationIn",
        "LocationOut": "_firebase_21_LocationOut",
        "AddFirebaseRequestIn": "_firebase_22_AddFirebaseRequestIn",
        "AddFirebaseRequestOut": "_firebase_23_AddFirebaseRequestOut",
        "WebAppIn": "_firebase_24_WebAppIn",
        "WebAppOut": "_firebase_25_WebAppOut",
        "UndeleteAndroidAppRequestIn": "_firebase_26_UndeleteAndroidAppRequestIn",
        "UndeleteAndroidAppRequestOut": "_firebase_27_UndeleteAndroidAppRequestOut",
        "IosAppIn": "_firebase_28_IosAppIn",
        "IosAppOut": "_firebase_29_IosAppOut",
        "EmptyIn": "_firebase_30_EmptyIn",
        "EmptyOut": "_firebase_31_EmptyOut",
        "AnalyticsPropertyIn": "_firebase_32_AnalyticsPropertyIn",
        "AnalyticsPropertyOut": "_firebase_33_AnalyticsPropertyOut",
        "RemoveIosAppRequestIn": "_firebase_34_RemoveIosAppRequestIn",
        "RemoveIosAppRequestOut": "_firebase_35_RemoveIosAppRequestOut",
        "RemoveAndroidAppRequestIn": "_firebase_36_RemoveAndroidAppRequestIn",
        "RemoveAndroidAppRequestOut": "_firebase_37_RemoveAndroidAppRequestOut",
        "AddGoogleAnalyticsRequestIn": "_firebase_38_AddGoogleAnalyticsRequestIn",
        "AddGoogleAnalyticsRequestOut": "_firebase_39_AddGoogleAnalyticsRequestOut",
        "RemoveWebAppRequestIn": "_firebase_40_RemoveWebAppRequestIn",
        "RemoveWebAppRequestOut": "_firebase_41_RemoveWebAppRequestOut",
        "WebAppConfigIn": "_firebase_42_WebAppConfigIn",
        "WebAppConfigOut": "_firebase_43_WebAppConfigOut",
        "ListAvailableLocationsResponseIn": "_firebase_44_ListAvailableLocationsResponseIn",
        "ListAvailableLocationsResponseOut": "_firebase_45_ListAvailableLocationsResponseOut",
        "AdminSdkConfigIn": "_firebase_46_AdminSdkConfigIn",
        "AdminSdkConfigOut": "_firebase_47_AdminSdkConfigOut",
        "ShaCertificateIn": "_firebase_48_ShaCertificateIn",
        "ShaCertificateOut": "_firebase_49_ShaCertificateOut",
        "StatusProtoIn": "_firebase_50_StatusProtoIn",
        "StatusProtoOut": "_firebase_51_StatusProtoOut",
        "AndroidAppIn": "_firebase_52_AndroidAppIn",
        "AndroidAppOut": "_firebase_53_AndroidAppOut",
        "ListAndroidAppsResponseIn": "_firebase_54_ListAndroidAppsResponseIn",
        "ListAndroidAppsResponseOut": "_firebase_55_ListAndroidAppsResponseOut",
        "UndeleteIosAppRequestIn": "_firebase_56_UndeleteIosAppRequestIn",
        "UndeleteIosAppRequestOut": "_firebase_57_UndeleteIosAppRequestOut",
        "SearchFirebaseAppsResponseIn": "_firebase_58_SearchFirebaseAppsResponseIn",
        "SearchFirebaseAppsResponseOut": "_firebase_59_SearchFirebaseAppsResponseOut",
        "ProductMetadataIn": "_firebase_60_ProductMetadataIn",
        "ProductMetadataOut": "_firebase_61_ProductMetadataOut",
        "OperationIn": "_firebase_62_OperationIn",
        "OperationOut": "_firebase_63_OperationOut",
        "UndeleteWebAppRequestIn": "_firebase_64_UndeleteWebAppRequestIn",
        "UndeleteWebAppRequestOut": "_firebase_65_UndeleteWebAppRequestOut",
        "MessageSetIn": "_firebase_66_MessageSetIn",
        "MessageSetOut": "_firebase_67_MessageSetOut",
        "ListAvailableProjectsResponseIn": "_firebase_68_ListAvailableProjectsResponseIn",
        "ListAvailableProjectsResponseOut": "_firebase_69_ListAvailableProjectsResponseOut",
        "IosAppConfigIn": "_firebase_70_IosAppConfigIn",
        "IosAppConfigOut": "_firebase_71_IosAppConfigOut",
        "StatusIn": "_firebase_72_StatusIn",
        "StatusOut": "_firebase_73_StatusOut",
        "StreamMappingIn": "_firebase_74_StreamMappingIn",
        "StreamMappingOut": "_firebase_75_StreamMappingOut",
        "AnalyticsDetailsIn": "_firebase_76_AnalyticsDetailsIn",
        "AnalyticsDetailsOut": "_firebase_77_AnalyticsDetailsOut",
        "ListFirebaseProjectsResponseIn": "_firebase_78_ListFirebaseProjectsResponseIn",
        "ListFirebaseProjectsResponseOut": "_firebase_79_ListFirebaseProjectsResponseOut",
        "FirebaseProjectIn": "_firebase_80_FirebaseProjectIn",
        "FirebaseProjectOut": "_firebase_81_FirebaseProjectOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListShaCertificatesResponseIn"] = t.struct(
        {"certificates": t.array(t.proxy(renames["ShaCertificateIn"])).optional()}
    ).named(renames["ListShaCertificatesResponseIn"])
    types["ListShaCertificatesResponseOut"] = t.struct(
        {
            "certificates": t.array(t.proxy(renames["ShaCertificateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListShaCertificatesResponseOut"])
    types["FinalizeDefaultLocationRequestIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["FinalizeDefaultLocationRequestIn"])
    types["FinalizeDefaultLocationRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FinalizeDefaultLocationRequestOut"])
    types["ProjectInfoIn"] = t.struct(
        {
            "project": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["ProjectInfoIn"])
    types["ProjectInfoOut"] = t.struct(
        {
            "project": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectInfoOut"])
    types["DefaultResourcesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DefaultResourcesIn"]
    )
    types["DefaultResourcesOut"] = t.struct(
        {
            "hostingSite": t.string().optional(),
            "locationId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "realtimeDatabaseInstance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultResourcesOut"])
    types["FirebaseAppInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "platform": t.string().optional(),
        }
    ).named(renames["FirebaseAppInfoIn"])
    types["FirebaseAppInfoOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "namespace": t.string().optional(),
            "name": t.string().optional(),
            "appId": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "platform": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirebaseAppInfoOut"])
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
    types["RemoveAnalyticsRequestIn"] = t.struct(
        {"analyticsPropertyId": t.string().optional()}
    ).named(renames["RemoveAnalyticsRequestIn"])
    types["RemoveAnalyticsRequestOut"] = t.struct(
        {
            "analyticsPropertyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveAnalyticsRequestOut"])
    types["ListWebAppsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["WebAppIn"])).optional(),
        }
    ).named(renames["ListWebAppsResponseIn"])
    types["ListWebAppsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "apps": t.array(t.proxy(renames["WebAppOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWebAppsResponseOut"])
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
            "locationId": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AddFirebaseRequestIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["AddFirebaseRequestIn"])
    types["AddFirebaseRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFirebaseRequestOut"])
    types["WebAppIn"] = t.struct(
        {
            "appUrls": t.array(t.string()).optional(),
            "apiKeyId": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "state": t.string().optional(),
            "expireTime": t.string().optional(),
            "webId": t.string().optional(),
            "appUrls": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "appId": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
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
    types["IosAppIn"] = t.struct(
        {
            "name": t.string().optional(),
            "teamId": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "appStoreId": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "bundleId": t.string().optional(),
        }
    ).named(renames["IosAppIn"])
    types["IosAppOut"] = t.struct(
        {
            "name": t.string().optional(),
            "teamId": t.string().optional(),
            "displayName": t.string().optional(),
            "projectId": t.string().optional(),
            "state": t.string().optional(),
            "etag": t.string().optional(),
            "expireTime": t.string().optional(),
            "appStoreId": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "appId": t.string().optional(),
            "bundleId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["RemoveIosAppRequestIn"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "etag": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["RemoveIosAppRequestIn"])
    types["RemoveIosAppRequestOut"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "etag": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveIosAppRequestOut"])
    types["RemoveAndroidAppRequestIn"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["RemoveAndroidAppRequestIn"])
    types["RemoveAndroidAppRequestOut"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
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
    types["RemoveWebAppRequestIn"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["RemoveWebAppRequestIn"])
    types["RemoveWebAppRequestOut"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveWebAppRequestOut"])
    types["WebAppConfigIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "appId": t.string().optional(),
            "messagingSenderId": t.string().optional(),
            "databaseURL": t.string().optional(),
            "authDomain": t.string().optional(),
            "apiKey": t.string().optional(),
            "storageBucket": t.string().optional(),
            "measurementId": t.string().optional(),
            "projectId": t.string().optional(),
        }
    ).named(renames["WebAppConfigIn"])
    types["WebAppConfigOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "appId": t.string().optional(),
            "messagingSenderId": t.string().optional(),
            "databaseURL": t.string().optional(),
            "authDomain": t.string().optional(),
            "apiKey": t.string().optional(),
            "storageBucket": t.string().optional(),
            "measurementId": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppConfigOut"])
    types["ListAvailableLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListAvailableLocationsResponseIn"])
    types["ListAvailableLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAvailableLocationsResponseOut"])
    types["AdminSdkConfigIn"] = t.struct(
        {
            "databaseURL": t.string().optional(),
            "projectId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["AdminSdkConfigIn"])
    types["AdminSdkConfigOut"] = t.struct(
        {
            "databaseURL": t.string().optional(),
            "projectId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminSdkConfigOut"])
    types["ShaCertificateIn"] = t.struct(
        {
            "name": t.string().optional(),
            "shaHash": t.string().optional(),
            "certType": t.string().optional(),
        }
    ).named(renames["ShaCertificateIn"])
    types["ShaCertificateOut"] = t.struct(
        {
            "name": t.string().optional(),
            "shaHash": t.string().optional(),
            "certType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShaCertificateOut"])
    types["StatusProtoIn"] = t.struct(
        {
            "message": t.string().optional(),
            "canonicalCode": t.integer().optional(),
            "space": t.string().optional(),
            "messageSet": t.proxy(renames["MessageSetIn"]).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusProtoIn"])
    types["StatusProtoOut"] = t.struct(
        {
            "message": t.string().optional(),
            "canonicalCode": t.integer().optional(),
            "space": t.string().optional(),
            "messageSet": t.proxy(renames["MessageSetOut"]).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusProtoOut"])
    types["AndroidAppIn"] = t.struct(
        {
            "apiKeyId": t.string().optional(),
            "etag": t.string().optional(),
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "sha256Hashes": t.array(t.string()).optional(),
            "sha1Hashes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AndroidAppIn"])
    types["AndroidAppOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "etag": t.string().optional(),
            "packageName": t.string().optional(),
            "appId": t.string().optional(),
            "name": t.string().optional(),
            "sha256Hashes": t.array(t.string()).optional(),
            "sha1Hashes": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppOut"])
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
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["UndeleteWebAppRequestIn"] = t.struct(
        {"validateOnly": t.boolean().optional(), "etag": t.string().optional()}
    ).named(renames["UndeleteWebAppRequestIn"])
    types["UndeleteWebAppRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteWebAppRequestOut"])
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
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
    types["IosAppConfigIn"] = t.struct(
        {
            "configFileContents": t.string().optional(),
            "configFilename": t.string().optional(),
        }
    ).named(renames["IosAppConfigIn"])
    types["IosAppConfigOut"] = t.struct(
        {
            "configFileContents": t.string().optional(),
            "configFilename": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppConfigOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["StreamMappingIn"] = t.struct(
        {
            "measurementId": t.string().optional(),
            "streamId": t.string().optional(),
            "app": t.string().optional(),
        }
    ).named(renames["StreamMappingIn"])
    types["StreamMappingOut"] = t.struct(
        {
            "measurementId": t.string().optional(),
            "streamId": t.string().optional(),
            "app": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamMappingOut"])
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
            "resources": t.proxy(renames["DefaultResourcesOut"]).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "projectNumber": t.string().optional(),
            "etag": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirebaseProjectOut"])

    functions = {}
    functions["projectsPatch"] = firebase.get(
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
    functions["projectsAddFirebase"] = firebase.get(
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
    functions["projectsRemoveAnalytics"] = firebase.get(
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
    functions["projectsGetAnalyticsDetails"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["AnalyticsDetailsOut"]),
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
    functions["projectsIosAppsPatch"] = firebase.post(
        "v1beta1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsList"] = firebase.post(
        "v1beta1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsGetConfig"] = firebase.post(
        "v1beta1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsRemove"] = firebase.post(
        "v1beta1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsGet"] = firebase.post(
        "v1beta1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsCreate"] = firebase.post(
        "v1beta1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsUndelete"] = firebase.post(
        "v1beta1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsPatch"] = firebase.get(
        "v1beta1/{parent}/androidApps",
        t.struct(
            {
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAndroidAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsCreate"] = firebase.get(
        "v1beta1/{parent}/androidApps",
        t.struct(
            {
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAndroidAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsGetConfig"] = firebase.get(
        "v1beta1/{parent}/androidApps",
        t.struct(
            {
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAndroidAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsGet"] = firebase.get(
        "v1beta1/{parent}/androidApps",
        t.struct(
            {
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAndroidAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsUndelete"] = firebase.get(
        "v1beta1/{parent}/androidApps",
        t.struct(
            {
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAndroidAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsRemove"] = firebase.get(
        "v1beta1/{parent}/androidApps",
        t.struct(
            {
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAndroidAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsList"] = firebase.get(
        "v1beta1/{parent}/androidApps",
        t.struct(
            {
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAndroidAppsResponseOut"]),
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
    functions["projectsAndroidAppsShaCreate"] = firebase.delete(
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
    functions["projectsWebAppsRemove"] = firebase.post(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "appUrls": t.array(t.string()).optional(),
                "apiKeyId": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsPatch"] = firebase.post(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "appUrls": t.array(t.string()).optional(),
                "apiKeyId": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsGet"] = firebase.post(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "appUrls": t.array(t.string()).optional(),
                "apiKeyId": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsList"] = firebase.post(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "appUrls": t.array(t.string()).optional(),
                "apiKeyId": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsUndelete"] = firebase.post(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "appUrls": t.array(t.string()).optional(),
                "apiKeyId": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsGetConfig"] = firebase.post(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "appUrls": t.array(t.string()).optional(),
                "apiKeyId": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsCreate"] = firebase.post(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "appUrls": t.array(t.string()).optional(),
                "apiKeyId": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAvailableLocationsList"] = firebase.get(
        "v1beta1/{parent}/availableLocations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAvailableLocationsResponseOut"]),
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
