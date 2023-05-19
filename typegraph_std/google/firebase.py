from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_firebase() -> Import:
    firebase = HTTPRuntime("https://firebase.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebase_1_ErrorResponse",
        "AddGoogleAnalyticsRequestIn": "_firebase_2_AddGoogleAnalyticsRequestIn",
        "AddGoogleAnalyticsRequestOut": "_firebase_3_AddGoogleAnalyticsRequestOut",
        "ListAvailableLocationsResponseIn": "_firebase_4_ListAvailableLocationsResponseIn",
        "ListAvailableLocationsResponseOut": "_firebase_5_ListAvailableLocationsResponseOut",
        "RemoveWebAppRequestIn": "_firebase_6_RemoveWebAppRequestIn",
        "RemoveWebAppRequestOut": "_firebase_7_RemoveWebAppRequestOut",
        "StreamMappingIn": "_firebase_8_StreamMappingIn",
        "StreamMappingOut": "_firebase_9_StreamMappingOut",
        "UndeleteWebAppRequestIn": "_firebase_10_UndeleteWebAppRequestIn",
        "UndeleteWebAppRequestOut": "_firebase_11_UndeleteWebAppRequestOut",
        "OperationIn": "_firebase_12_OperationIn",
        "OperationOut": "_firebase_13_OperationOut",
        "RemoveIosAppRequestIn": "_firebase_14_RemoveIosAppRequestIn",
        "RemoveIosAppRequestOut": "_firebase_15_RemoveIosAppRequestOut",
        "ListAndroidAppsResponseIn": "_firebase_16_ListAndroidAppsResponseIn",
        "ListAndroidAppsResponseOut": "_firebase_17_ListAndroidAppsResponseOut",
        "ShaCertificateIn": "_firebase_18_ShaCertificateIn",
        "ShaCertificateOut": "_firebase_19_ShaCertificateOut",
        "IosAppIn": "_firebase_20_IosAppIn",
        "IosAppOut": "_firebase_21_IosAppOut",
        "UndeleteAndroidAppRequestIn": "_firebase_22_UndeleteAndroidAppRequestIn",
        "UndeleteAndroidAppRequestOut": "_firebase_23_UndeleteAndroidAppRequestOut",
        "AnalyticsDetailsIn": "_firebase_24_AnalyticsDetailsIn",
        "AnalyticsDetailsOut": "_firebase_25_AnalyticsDetailsOut",
        "ListFirebaseProjectsResponseIn": "_firebase_26_ListFirebaseProjectsResponseIn",
        "ListFirebaseProjectsResponseOut": "_firebase_27_ListFirebaseProjectsResponseOut",
        "ListWebAppsResponseIn": "_firebase_28_ListWebAppsResponseIn",
        "ListWebAppsResponseOut": "_firebase_29_ListWebAppsResponseOut",
        "RemoveAnalyticsRequestIn": "_firebase_30_RemoveAnalyticsRequestIn",
        "RemoveAnalyticsRequestOut": "_firebase_31_RemoveAnalyticsRequestOut",
        "ListIosAppsResponseIn": "_firebase_32_ListIosAppsResponseIn",
        "ListIosAppsResponseOut": "_firebase_33_ListIosAppsResponseOut",
        "StatusIn": "_firebase_34_StatusIn",
        "StatusOut": "_firebase_35_StatusOut",
        "AdminSdkConfigIn": "_firebase_36_AdminSdkConfigIn",
        "AdminSdkConfigOut": "_firebase_37_AdminSdkConfigOut",
        "WebAppConfigIn": "_firebase_38_WebAppConfigIn",
        "WebAppConfigOut": "_firebase_39_WebAppConfigOut",
        "AndroidAppIn": "_firebase_40_AndroidAppIn",
        "AndroidAppOut": "_firebase_41_AndroidAppOut",
        "StatusProtoIn": "_firebase_42_StatusProtoIn",
        "StatusProtoOut": "_firebase_43_StatusProtoOut",
        "EmptyIn": "_firebase_44_EmptyIn",
        "EmptyOut": "_firebase_45_EmptyOut",
        "FirebaseAppInfoIn": "_firebase_46_FirebaseAppInfoIn",
        "FirebaseAppInfoOut": "_firebase_47_FirebaseAppInfoOut",
        "MessageSetIn": "_firebase_48_MessageSetIn",
        "MessageSetOut": "_firebase_49_MessageSetOut",
        "AnalyticsPropertyIn": "_firebase_50_AnalyticsPropertyIn",
        "AnalyticsPropertyOut": "_firebase_51_AnalyticsPropertyOut",
        "FinalizeDefaultLocationRequestIn": "_firebase_52_FinalizeDefaultLocationRequestIn",
        "FinalizeDefaultLocationRequestOut": "_firebase_53_FinalizeDefaultLocationRequestOut",
        "AddFirebaseRequestIn": "_firebase_54_AddFirebaseRequestIn",
        "AddFirebaseRequestOut": "_firebase_55_AddFirebaseRequestOut",
        "ListAvailableProjectsResponseIn": "_firebase_56_ListAvailableProjectsResponseIn",
        "ListAvailableProjectsResponseOut": "_firebase_57_ListAvailableProjectsResponseOut",
        "FirebaseProjectIn": "_firebase_58_FirebaseProjectIn",
        "FirebaseProjectOut": "_firebase_59_FirebaseProjectOut",
        "AndroidAppConfigIn": "_firebase_60_AndroidAppConfigIn",
        "AndroidAppConfigOut": "_firebase_61_AndroidAppConfigOut",
        "UndeleteIosAppRequestIn": "_firebase_62_UndeleteIosAppRequestIn",
        "UndeleteIosAppRequestOut": "_firebase_63_UndeleteIosAppRequestOut",
        "SearchFirebaseAppsResponseIn": "_firebase_64_SearchFirebaseAppsResponseIn",
        "SearchFirebaseAppsResponseOut": "_firebase_65_SearchFirebaseAppsResponseOut",
        "LocationIn": "_firebase_66_LocationIn",
        "LocationOut": "_firebase_67_LocationOut",
        "ListShaCertificatesResponseIn": "_firebase_68_ListShaCertificatesResponseIn",
        "ListShaCertificatesResponseOut": "_firebase_69_ListShaCertificatesResponseOut",
        "ProductMetadataIn": "_firebase_70_ProductMetadataIn",
        "ProductMetadataOut": "_firebase_71_ProductMetadataOut",
        "RemoveAndroidAppRequestIn": "_firebase_72_RemoveAndroidAppRequestIn",
        "RemoveAndroidAppRequestOut": "_firebase_73_RemoveAndroidAppRequestOut",
        "DefaultResourcesIn": "_firebase_74_DefaultResourcesIn",
        "DefaultResourcesOut": "_firebase_75_DefaultResourcesOut",
        "WebAppIn": "_firebase_76_WebAppIn",
        "WebAppOut": "_firebase_77_WebAppOut",
        "ProjectInfoIn": "_firebase_78_ProjectInfoIn",
        "ProjectInfoOut": "_firebase_79_ProjectInfoOut",
        "IosAppConfigIn": "_firebase_80_IosAppConfigIn",
        "IosAppConfigOut": "_firebase_81_IosAppConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["RemoveWebAppRequestIn"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["RemoveWebAppRequestIn"])
    types["RemoveWebAppRequestOut"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveWebAppRequestOut"])
    types["StreamMappingIn"] = t.struct(
        {
            "streamId": t.string().optional(),
            "app": t.string().optional(),
            "measurementId": t.string().optional(),
        }
    ).named(renames["StreamMappingIn"])
    types["StreamMappingOut"] = t.struct(
        {
            "streamId": t.string().optional(),
            "app": t.string().optional(),
            "measurementId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StreamMappingOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["RemoveIosAppRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "immediate": t.boolean().optional(),
        }
    ).named(renames["RemoveIosAppRequestIn"])
    types["RemoveIosAppRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "allowMissing": t.boolean().optional(),
            "immediate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveIosAppRequestOut"])
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
    types["ShaCertificateIn"] = t.struct(
        {
            "shaHash": t.string().optional(),
            "name": t.string().optional(),
            "certType": t.string().optional(),
        }
    ).named(renames["ShaCertificateIn"])
    types["ShaCertificateOut"] = t.struct(
        {
            "shaHash": t.string().optional(),
            "name": t.string().optional(),
            "certType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ShaCertificateOut"])
    types["IosAppIn"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "appStoreId": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "teamId": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["IosAppIn"])
    types["IosAppOut"] = t.struct(
        {
            "bundleId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "appStoreId": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "projectId": t.string().optional(),
            "teamId": t.string().optional(),
            "appId": t.string().optional(),
            "etag": t.string().optional(),
            "expireTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppOut"])
    types["UndeleteAndroidAppRequestIn"] = t.struct(
        {"validateOnly": t.boolean().optional(), "etag": t.string().optional()}
    ).named(renames["UndeleteAndroidAppRequestIn"])
    types["UndeleteAndroidAppRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteAndroidAppRequestOut"])
    types["AnalyticsDetailsIn"] = t.struct(
        {
            "analyticsProperty": t.proxy(renames["AnalyticsPropertyIn"]).optional(),
            "streamMappings": t.array(t.proxy(renames["StreamMappingIn"])).optional(),
        }
    ).named(renames["AnalyticsDetailsIn"])
    types["AnalyticsDetailsOut"] = t.struct(
        {
            "analyticsProperty": t.proxy(renames["AnalyticsPropertyOut"]).optional(),
            "streamMappings": t.array(t.proxy(renames["StreamMappingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyticsDetailsOut"])
    types["ListFirebaseProjectsResponseIn"] = t.struct(
        {
            "results": t.array(t.proxy(renames["FirebaseProjectIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFirebaseProjectsResponseIn"])
    types["ListFirebaseProjectsResponseOut"] = t.struct(
        {
            "results": t.array(t.proxy(renames["FirebaseProjectOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFirebaseProjectsResponseOut"])
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
    types["RemoveAnalyticsRequestIn"] = t.struct(
        {"analyticsPropertyId": t.string().optional()}
    ).named(renames["RemoveAnalyticsRequestIn"])
    types["RemoveAnalyticsRequestOut"] = t.struct(
        {
            "analyticsPropertyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveAnalyticsRequestOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AdminSdkConfigIn"] = t.struct(
        {
            "storageBucket": t.string().optional(),
            "locationId": t.string().optional(),
            "projectId": t.string().optional(),
            "databaseURL": t.string().optional(),
        }
    ).named(renames["AdminSdkConfigIn"])
    types["AdminSdkConfigOut"] = t.struct(
        {
            "storageBucket": t.string().optional(),
            "locationId": t.string().optional(),
            "projectId": t.string().optional(),
            "databaseURL": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminSdkConfigOut"])
    types["WebAppConfigIn"] = t.struct(
        {
            "measurementId": t.string().optional(),
            "appId": t.string().optional(),
            "messagingSenderId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "projectId": t.string().optional(),
            "apiKey": t.string().optional(),
            "locationId": t.string().optional(),
            "authDomain": t.string().optional(),
            "databaseURL": t.string().optional(),
        }
    ).named(renames["WebAppConfigIn"])
    types["WebAppConfigOut"] = t.struct(
        {
            "measurementId": t.string().optional(),
            "appId": t.string().optional(),
            "messagingSenderId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "projectId": t.string().optional(),
            "apiKey": t.string().optional(),
            "locationId": t.string().optional(),
            "authDomain": t.string().optional(),
            "databaseURL": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppConfigOut"])
    types["AndroidAppIn"] = t.struct(
        {
            "sha1Hashes": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "sha256Hashes": t.array(t.string()).optional(),
            "apiKeyId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AndroidAppIn"])
    types["AndroidAppOut"] = t.struct(
        {
            "sha1Hashes": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "appId": t.string().optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "expireTime": t.string().optional(),
            "sha256Hashes": t.array(t.string()).optional(),
            "projectId": t.string().optional(),
            "state": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppOut"])
    types["StatusProtoIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "messageSet": t.proxy(renames["MessageSetIn"]).optional(),
            "canonicalCode": t.integer().optional(),
            "message": t.string().optional(),
            "space": t.string().optional(),
        }
    ).named(renames["StatusProtoIn"])
    types["StatusProtoOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "messageSet": t.proxy(renames["MessageSetOut"]).optional(),
            "canonicalCode": t.integer().optional(),
            "message": t.string().optional(),
            "space": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusProtoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["FirebaseAppInfoIn"] = t.struct(
        {
            "platform": t.string().optional(),
            "displayName": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FirebaseAppInfoIn"])
    types["FirebaseAppInfoOut"] = t.struct(
        {
            "platform": t.string().optional(),
            "displayName": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "namespace": t.string().optional(),
            "state": t.string().optional(),
            "appId": t.string().optional(),
            "expireTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirebaseAppInfoOut"])
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
    types["AnalyticsPropertyIn"] = t.struct(
        {"id": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["AnalyticsPropertyIn"])
    types["AnalyticsPropertyOut"] = t.struct(
        {
            "analyticsAccountId": t.string().optional(),
            "id": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyticsPropertyOut"])
    types["FinalizeDefaultLocationRequestIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["FinalizeDefaultLocationRequestIn"])
    types["FinalizeDefaultLocationRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FinalizeDefaultLocationRequestOut"])
    types["AddFirebaseRequestIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["AddFirebaseRequestIn"])
    types["AddFirebaseRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFirebaseRequestOut"])
    types["ListAvailableProjectsResponseIn"] = t.struct(
        {
            "projectInfo": t.array(t.proxy(renames["ProjectInfoIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAvailableProjectsResponseIn"])
    types["ListAvailableProjectsResponseOut"] = t.struct(
        {
            "projectInfo": t.array(t.proxy(renames["ProjectInfoOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAvailableProjectsResponseOut"])
    types["FirebaseProjectIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FirebaseProjectIn"])
    types["FirebaseProjectOut"] = t.struct(
        {
            "resources": t.proxy(renames["DefaultResourcesOut"]).optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "projectId": t.string().optional(),
            "projectNumber": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirebaseProjectOut"])
    types["AndroidAppConfigIn"] = t.struct(
        {
            "configFileContents": t.string().optional(),
            "configFilename": t.string().optional(),
        }
    ).named(renames["AndroidAppConfigIn"])
    types["AndroidAppConfigOut"] = t.struct(
        {
            "configFileContents": t.string().optional(),
            "configFilename": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppConfigOut"])
    types["UndeleteIosAppRequestIn"] = t.struct(
        {"etag": t.string().optional(), "validateOnly": t.boolean().optional()}
    ).named(renames["UndeleteIosAppRequestIn"])
    types["UndeleteIosAppRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteIosAppRequestOut"])
    types["SearchFirebaseAppsResponseIn"] = t.struct(
        {
            "apps": t.array(t.proxy(renames["FirebaseAppInfoIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchFirebaseAppsResponseIn"])
    types["SearchFirebaseAppsResponseOut"] = t.struct(
        {
            "apps": t.array(t.proxy(renames["FirebaseAppInfoOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchFirebaseAppsResponseOut"])
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
    types["ListShaCertificatesResponseIn"] = t.struct(
        {"certificates": t.array(t.proxy(renames["ShaCertificateIn"])).optional()}
    ).named(renames["ListShaCertificatesResponseIn"])
    types["ListShaCertificatesResponseOut"] = t.struct(
        {
            "certificates": t.array(t.proxy(renames["ShaCertificateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListShaCertificatesResponseOut"])
    types["ProductMetadataIn"] = t.struct(
        {"warningMessages": t.array(t.string()).optional()}
    ).named(renames["ProductMetadataIn"])
    types["ProductMetadataOut"] = t.struct(
        {
            "warningMessages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductMetadataOut"])
    types["RemoveAndroidAppRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["RemoveAndroidAppRequestIn"])
    types["RemoveAndroidAppRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveAndroidAppRequestOut"])
    types["DefaultResourcesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DefaultResourcesIn"]
    )
    types["DefaultResourcesOut"] = t.struct(
        {
            "hostingSite": t.string().optional(),
            "storageBucket": t.string().optional(),
            "locationId": t.string().optional(),
            "realtimeDatabaseInstance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultResourcesOut"])
    types["WebAppIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "appUrls": t.array(t.string()).optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "webId": t.string().optional(),
            "expireTime": t.string().optional(),
            "displayName": t.string().optional(),
            "projectId": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "state": t.string().optional(),
            "appUrls": t.array(t.string()).optional(),
            "appId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
    types["ProjectInfoIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "project": t.string().optional(),
        }
    ).named(renames["ProjectInfoIn"])
    types["ProjectInfoOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectInfoOut"])
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

    functions = {}
    functions["projectsGetAnalyticsDetails"] = firebase.get(
        "v1beta1/{parent}:searchApps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchFirebaseAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = firebase.get(
        "v1beta1/{parent}:searchApps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchFirebaseAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRemoveAnalytics"] = firebase.get(
        "v1beta1/{parent}:searchApps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchFirebaseAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAddFirebase"] = firebase.get(
        "v1beta1/{parent}:searchApps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchFirebaseAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetAdminSdkConfig"] = firebase.get(
        "v1beta1/{parent}:searchApps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchFirebaseAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatch"] = firebase.get(
        "v1beta1/{parent}:searchApps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchFirebaseAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAddGoogleAnalytics"] = firebase.get(
        "v1beta1/{parent}:searchApps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchFirebaseAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsList"] = firebase.get(
        "v1beta1/{parent}:searchApps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchFirebaseAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSearchApps"] = firebase.get(
        "v1beta1/{parent}:searchApps",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "showDeleted": t.boolean().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchFirebaseAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsUndelete"] = firebase.get(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsGetConfig"] = firebase.get(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsGet"] = firebase.get(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsCreate"] = firebase.get(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsPatch"] = firebase.get(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsRemove"] = firebase.get(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsList"] = firebase.get(
        "v1beta1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "showDeleted": t.boolean().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsPatch"] = firebase.post(
        "v1beta1/{name}:undelete",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
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
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
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
                "parent": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAvailableLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsUndelete"] = firebase.post(
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsList"] = firebase.post(
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsGet"] = firebase.post(
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsPatch"] = firebase.post(
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsCreate"] = firebase.post(
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsGetConfig"] = firebase.post(
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsRemove"] = firebase.post(
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsShaDelete"] = firebase.get(
        "v1beta1/{parent}/sha",
        t.struct({"parent": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListShaCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsShaCreate"] = firebase.get(
        "v1beta1/{parent}/sha",
        t.struct({"parent": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListShaCertificatesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsShaList"] = firebase.get(
        "v1beta1/{parent}/sha",
        t.struct({"parent": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ListShaCertificatesResponseOut"]),
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
    functions["operationsGet"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
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

    return Import(
        importer="firebase", renames=renames, types=Box(types), functions=Box(functions)
    )
