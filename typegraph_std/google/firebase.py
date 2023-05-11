from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_firebase() -> Import:
    firebase = HTTPRuntime("https://firebase.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebase_1_ErrorResponse",
        "RemoveAndroidAppRequestIn": "_firebase_2_RemoveAndroidAppRequestIn",
        "RemoveAndroidAppRequestOut": "_firebase_3_RemoveAndroidAppRequestOut",
        "ProductMetadataIn": "_firebase_4_ProductMetadataIn",
        "ProductMetadataOut": "_firebase_5_ProductMetadataOut",
        "DefaultResourcesIn": "_firebase_6_DefaultResourcesIn",
        "DefaultResourcesOut": "_firebase_7_DefaultResourcesOut",
        "AddFirebaseRequestIn": "_firebase_8_AddFirebaseRequestIn",
        "AddFirebaseRequestOut": "_firebase_9_AddFirebaseRequestOut",
        "ListAndroidAppsResponseIn": "_firebase_10_ListAndroidAppsResponseIn",
        "ListAndroidAppsResponseOut": "_firebase_11_ListAndroidAppsResponseOut",
        "StatusProtoIn": "_firebase_12_StatusProtoIn",
        "StatusProtoOut": "_firebase_13_StatusProtoOut",
        "FirebaseProjectIn": "_firebase_14_FirebaseProjectIn",
        "FirebaseProjectOut": "_firebase_15_FirebaseProjectOut",
        "RemoveIosAppRequestIn": "_firebase_16_RemoveIosAppRequestIn",
        "RemoveIosAppRequestOut": "_firebase_17_RemoveIosAppRequestOut",
        "FirebaseAppInfoIn": "_firebase_18_FirebaseAppInfoIn",
        "FirebaseAppInfoOut": "_firebase_19_FirebaseAppInfoOut",
        "IosAppIn": "_firebase_20_IosAppIn",
        "IosAppOut": "_firebase_21_IosAppOut",
        "ListIosAppsResponseIn": "_firebase_22_ListIosAppsResponseIn",
        "ListIosAppsResponseOut": "_firebase_23_ListIosAppsResponseOut",
        "UndeleteIosAppRequestIn": "_firebase_24_UndeleteIosAppRequestIn",
        "UndeleteIosAppRequestOut": "_firebase_25_UndeleteIosAppRequestOut",
        "ListShaCertificatesResponseIn": "_firebase_26_ListShaCertificatesResponseIn",
        "ListShaCertificatesResponseOut": "_firebase_27_ListShaCertificatesResponseOut",
        "WebAppConfigIn": "_firebase_28_WebAppConfigIn",
        "WebAppConfigOut": "_firebase_29_WebAppConfigOut",
        "ListAvailableProjectsResponseIn": "_firebase_30_ListAvailableProjectsResponseIn",
        "ListAvailableProjectsResponseOut": "_firebase_31_ListAvailableProjectsResponseOut",
        "SearchFirebaseAppsResponseIn": "_firebase_32_SearchFirebaseAppsResponseIn",
        "SearchFirebaseAppsResponseOut": "_firebase_33_SearchFirebaseAppsResponseOut",
        "AdminSdkConfigIn": "_firebase_34_AdminSdkConfigIn",
        "AdminSdkConfigOut": "_firebase_35_AdminSdkConfigOut",
        "UndeleteAndroidAppRequestIn": "_firebase_36_UndeleteAndroidAppRequestIn",
        "UndeleteAndroidAppRequestOut": "_firebase_37_UndeleteAndroidAppRequestOut",
        "ShaCertificateIn": "_firebase_38_ShaCertificateIn",
        "ShaCertificateOut": "_firebase_39_ShaCertificateOut",
        "ListAvailableLocationsResponseIn": "_firebase_40_ListAvailableLocationsResponseIn",
        "ListAvailableLocationsResponseOut": "_firebase_41_ListAvailableLocationsResponseOut",
        "IosAppConfigIn": "_firebase_42_IosAppConfigIn",
        "IosAppConfigOut": "_firebase_43_IosAppConfigOut",
        "ListFirebaseProjectsResponseIn": "_firebase_44_ListFirebaseProjectsResponseIn",
        "ListFirebaseProjectsResponseOut": "_firebase_45_ListFirebaseProjectsResponseOut",
        "AddGoogleAnalyticsRequestIn": "_firebase_46_AddGoogleAnalyticsRequestIn",
        "AddGoogleAnalyticsRequestOut": "_firebase_47_AddGoogleAnalyticsRequestOut",
        "ProjectInfoIn": "_firebase_48_ProjectInfoIn",
        "ProjectInfoOut": "_firebase_49_ProjectInfoOut",
        "WebAppIn": "_firebase_50_WebAppIn",
        "WebAppOut": "_firebase_51_WebAppOut",
        "UndeleteWebAppRequestIn": "_firebase_52_UndeleteWebAppRequestIn",
        "UndeleteWebAppRequestOut": "_firebase_53_UndeleteWebAppRequestOut",
        "OperationIn": "_firebase_54_OperationIn",
        "OperationOut": "_firebase_55_OperationOut",
        "RemoveWebAppRequestIn": "_firebase_56_RemoveWebAppRequestIn",
        "RemoveWebAppRequestOut": "_firebase_57_RemoveWebAppRequestOut",
        "StreamMappingIn": "_firebase_58_StreamMappingIn",
        "StreamMappingOut": "_firebase_59_StreamMappingOut",
        "LocationIn": "_firebase_60_LocationIn",
        "LocationOut": "_firebase_61_LocationOut",
        "EmptyIn": "_firebase_62_EmptyIn",
        "EmptyOut": "_firebase_63_EmptyOut",
        "MessageSetIn": "_firebase_64_MessageSetIn",
        "MessageSetOut": "_firebase_65_MessageSetOut",
        "StatusIn": "_firebase_66_StatusIn",
        "StatusOut": "_firebase_67_StatusOut",
        "FinalizeDefaultLocationRequestIn": "_firebase_68_FinalizeDefaultLocationRequestIn",
        "FinalizeDefaultLocationRequestOut": "_firebase_69_FinalizeDefaultLocationRequestOut",
        "AnalyticsDetailsIn": "_firebase_70_AnalyticsDetailsIn",
        "AnalyticsDetailsOut": "_firebase_71_AnalyticsDetailsOut",
        "AnalyticsPropertyIn": "_firebase_72_AnalyticsPropertyIn",
        "AnalyticsPropertyOut": "_firebase_73_AnalyticsPropertyOut",
        "AndroidAppConfigIn": "_firebase_74_AndroidAppConfigIn",
        "AndroidAppConfigOut": "_firebase_75_AndroidAppConfigOut",
        "ListWebAppsResponseIn": "_firebase_76_ListWebAppsResponseIn",
        "ListWebAppsResponseOut": "_firebase_77_ListWebAppsResponseOut",
        "RemoveAnalyticsRequestIn": "_firebase_78_RemoveAnalyticsRequestIn",
        "RemoveAnalyticsRequestOut": "_firebase_79_RemoveAnalyticsRequestOut",
        "AndroidAppIn": "_firebase_80_AndroidAppIn",
        "AndroidAppOut": "_firebase_81_AndroidAppOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ProductMetadataIn"] = t.struct(
        {"warningMessages": t.array(t.string()).optional()}
    ).named(renames["ProductMetadataIn"])
    types["ProductMetadataOut"] = t.struct(
        {
            "warningMessages": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductMetadataOut"])
    types["DefaultResourcesIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DefaultResourcesIn"]
    )
    types["DefaultResourcesOut"] = t.struct(
        {
            "storageBucket": t.string().optional(),
            "locationId": t.string().optional(),
            "hostingSite": t.string().optional(),
            "realtimeDatabaseInstance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DefaultResourcesOut"])
    types["AddFirebaseRequestIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["AddFirebaseRequestIn"])
    types["AddFirebaseRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddFirebaseRequestOut"])
    types["ListAndroidAppsResponseIn"] = t.struct(
        {
            "apps": t.array(t.proxy(renames["AndroidAppIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAndroidAppsResponseIn"])
    types["ListAndroidAppsResponseOut"] = t.struct(
        {
            "apps": t.array(t.proxy(renames["AndroidAppOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAndroidAppsResponseOut"])
    types["StatusProtoIn"] = t.struct(
        {
            "message": t.string().optional(),
            "canonicalCode": t.integer().optional(),
            "code": t.integer().optional(),
            "messageSet": t.proxy(renames["MessageSetIn"]).optional(),
            "space": t.string().optional(),
        }
    ).named(renames["StatusProtoIn"])
    types["StatusProtoOut"] = t.struct(
        {
            "message": t.string().optional(),
            "canonicalCode": t.integer().optional(),
            "code": t.integer().optional(),
            "messageSet": t.proxy(renames["MessageSetOut"]).optional(),
            "space": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusProtoOut"])
    types["FirebaseProjectIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FirebaseProjectIn"])
    types["FirebaseProjectOut"] = t.struct(
        {
            "state": t.string().optional(),
            "projectId": t.string().optional(),
            "resources": t.proxy(renames["DefaultResourcesOut"]).optional(),
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "projectNumber": t.string().optional(),
            "name": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirebaseProjectOut"])
    types["RemoveIosAppRequestIn"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["RemoveIosAppRequestIn"])
    types["RemoveIosAppRequestOut"] = t.struct(
        {
            "immediate": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveIosAppRequestOut"])
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
            "expireTime": t.string().optional(),
            "state": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "appId": t.string().optional(),
            "namespace": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirebaseAppInfoOut"])
    types["IosAppIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "teamId": t.string().optional(),
            "name": t.string().optional(),
            "bundleId": t.string().optional(),
            "etag": t.string().optional(),
            "appStoreId": t.string().optional(),
            "apiKeyId": t.string().optional(),
        }
    ).named(renames["IosAppIn"])
    types["IosAppOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "teamId": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "bundleId": t.string().optional(),
            "expireTime": t.string().optional(),
            "etag": t.string().optional(),
            "appStoreId": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "projectId": t.string().optional(),
            "appId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IosAppOut"])
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
    types["ListShaCertificatesResponseIn"] = t.struct(
        {"certificates": t.array(t.proxy(renames["ShaCertificateIn"])).optional()}
    ).named(renames["ListShaCertificatesResponseIn"])
    types["ListShaCertificatesResponseOut"] = t.struct(
        {
            "certificates": t.array(t.proxy(renames["ShaCertificateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListShaCertificatesResponseOut"])
    types["WebAppConfigIn"] = t.struct(
        {
            "apiKey": t.string().optional(),
            "projectId": t.string().optional(),
            "databaseURL": t.string().optional(),
            "appId": t.string().optional(),
            "locationId": t.string().optional(),
            "measurementId": t.string().optional(),
            "authDomain": t.string().optional(),
            "storageBucket": t.string().optional(),
            "messagingSenderId": t.string().optional(),
        }
    ).named(renames["WebAppConfigIn"])
    types["WebAppConfigOut"] = t.struct(
        {
            "apiKey": t.string().optional(),
            "projectId": t.string().optional(),
            "databaseURL": t.string().optional(),
            "appId": t.string().optional(),
            "locationId": t.string().optional(),
            "measurementId": t.string().optional(),
            "authDomain": t.string().optional(),
            "storageBucket": t.string().optional(),
            "messagingSenderId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppConfigOut"])
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
    types["AdminSdkConfigIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "projectId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "databaseURL": t.string().optional(),
        }
    ).named(renames["AdminSdkConfigIn"])
    types["AdminSdkConfigOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "projectId": t.string().optional(),
            "storageBucket": t.string().optional(),
            "databaseURL": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminSdkConfigOut"])
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
    types["AddGoogleAnalyticsRequestIn"] = t.struct(
        {
            "analyticsAccountId": t.string().optional(),
            "analyticsPropertyId": t.string().optional(),
        }
    ).named(renames["AddGoogleAnalyticsRequestIn"])
    types["AddGoogleAnalyticsRequestOut"] = t.struct(
        {
            "analyticsAccountId": t.string().optional(),
            "analyticsPropertyId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddGoogleAnalyticsRequestOut"])
    types["ProjectInfoIn"] = t.struct(
        {
            "project": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ProjectInfoIn"])
    types["ProjectInfoOut"] = t.struct(
        {
            "project": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectInfoOut"])
    types["WebAppIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "appUrls": t.array(t.string()).optional(),
            "apiKeyId": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "appUrls": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "etag": t.string().optional(),
            "appId": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "webId": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
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
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["RemoveWebAppRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "immediate": t.boolean().optional(),
        }
    ).named(renames["RemoveWebAppRequestIn"])
    types["RemoveWebAppRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "allowMissing": t.boolean().optional(),
            "etag": t.string().optional(),
            "immediate": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveWebAppRequestOut"])
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
    types["LocationIn"] = t.struct(
        {
            "type": t.string().optional(),
            "locationId": t.string().optional(),
            "features": t.array(t.string()).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "type": t.string().optional(),
            "locationId": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MessageSetIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MessageSetIn"]
    )
    types["MessageSetOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MessageSetOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["FinalizeDefaultLocationRequestIn"] = t.struct(
        {"locationId": t.string().optional()}
    ).named(renames["FinalizeDefaultLocationRequestIn"])
    types["FinalizeDefaultLocationRequestOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FinalizeDefaultLocationRequestOut"])
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
    types["AndroidAppIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "sha256Hashes": t.array(t.string()).optional(),
            "sha1Hashes": t.array(t.string()).optional(),
            "etag": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AndroidAppIn"])
    types["AndroidAppOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "name": t.string().optional(),
            "sha256Hashes": t.array(t.string()).optional(),
            "sha1Hashes": t.array(t.string()).optional(),
            "etag": t.string().optional(),
            "apiKeyId": t.string().optional(),
            "expireTime": t.string().optional(),
            "state": t.string().optional(),
            "appId": t.string().optional(),
            "displayName": t.string().optional(),
            "projectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppOut"])

    functions = {}
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
    functions["projectsGetAdminSdkConfig"] = firebase.post(
        "v1beta1/{project}:addFirebase",
        t.struct(
            {
                "project": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsList"] = firebase.post(
        "v1beta1/{project}:addFirebase",
        t.struct(
            {
                "project": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSearchApps"] = firebase.post(
        "v1beta1/{project}:addFirebase",
        t.struct(
            {
                "project": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsRemoveAnalytics"] = firebase.post(
        "v1beta1/{project}:addFirebase",
        t.struct(
            {
                "project": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetAnalyticsDetails"] = firebase.post(
        "v1beta1/{project}:addFirebase",
        t.struct(
            {
                "project": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAddGoogleAnalytics"] = firebase.post(
        "v1beta1/{project}:addFirebase",
        t.struct(
            {
                "project": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = firebase.post(
        "v1beta1/{project}:addFirebase",
        t.struct(
            {
                "project": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatch"] = firebase.post(
        "v1beta1/{project}:addFirebase",
        t.struct(
            {
                "project": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAddFirebase"] = firebase.post(
        "v1beta1/{project}:addFirebase",
        t.struct(
            {
                "project": t.string().optional(),
                "locationId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsCreate"] = firebase.post(
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
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
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
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
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
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
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsIosAppsPatch"] = firebase.post(
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
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
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
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
        "v1beta1/{name}:remove",
        t.struct(
            {
                "name": t.string(),
                "immediate": t.boolean().optional(),
                "allowMissing": t.boolean().optional(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsWebAppsRemove"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsPatch"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsCreate"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsList"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsUndelete"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsGetConfig"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsWebAppsGet"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAndroidAppsList"] = firebase.post(
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
    functions["projectsAndroidAppsGetConfig"] = firebase.post(
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
    functions["projectsAndroidAppsRemove"] = firebase.post(
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
    functions["projectsAndroidAppsPatch"] = firebase.post(
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
    functions["projectsAndroidAppsCreate"] = firebase.post(
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
    functions["projectsAndroidAppsGet"] = firebase.post(
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
    functions["projectsAndroidAppsUndelete"] = firebase.post(
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
    functions["operationsGet"] = firebase.get(
        "v1beta1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebase", renames=renames, types=types, functions=functions
    )
