from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_androidenterprise() -> Import:
    androidenterprise = HTTPRuntime("https://androidenterprise.googleapis.com/")

    renames = {
        "ErrorResponse": "_androidenterprise_1_ErrorResponse",
        "EntitlementIn": "_androidenterprise_2_EntitlementIn",
        "EntitlementOut": "_androidenterprise_3_EntitlementOut",
        "ConfigurationVariablesIn": "_androidenterprise_4_ConfigurationVariablesIn",
        "ConfigurationVariablesOut": "_androidenterprise_5_ConfigurationVariablesOut",
        "ManagedPropertyBundleIn": "_androidenterprise_6_ManagedPropertyBundleIn",
        "ManagedPropertyBundleOut": "_androidenterprise_7_ManagedPropertyBundleOut",
        "AppRestrictionsSchemaRestrictionIn": "_androidenterprise_8_AppRestrictionsSchemaRestrictionIn",
        "AppRestrictionsSchemaRestrictionOut": "_androidenterprise_9_AppRestrictionsSchemaRestrictionOut",
        "WebAppIn": "_androidenterprise_10_WebAppIn",
        "WebAppOut": "_androidenterprise_11_WebAppOut",
        "AdministratorWebTokenSpecPrivateAppsIn": "_androidenterprise_12_AdministratorWebTokenSpecPrivateAppsIn",
        "AdministratorWebTokenSpecPrivateAppsOut": "_androidenterprise_13_AdministratorWebTokenSpecPrivateAppsOut",
        "NotificationSetIn": "_androidenterprise_14_NotificationSetIn",
        "NotificationSetOut": "_androidenterprise_15_NotificationSetOut",
        "AppRestrictionsSchemaIn": "_androidenterprise_16_AppRestrictionsSchemaIn",
        "AppRestrictionsSchemaOut": "_androidenterprise_17_AppRestrictionsSchemaOut",
        "EnterpriseAccountIn": "_androidenterprise_18_EnterpriseAccountIn",
        "EnterpriseAccountOut": "_androidenterprise_19_EnterpriseAccountOut",
        "GoogleAuthenticationSettingsIn": "_androidenterprise_20_GoogleAuthenticationSettingsIn",
        "GoogleAuthenticationSettingsOut": "_androidenterprise_21_GoogleAuthenticationSettingsOut",
        "KeyedAppStateIn": "_androidenterprise_22_KeyedAppStateIn",
        "KeyedAppStateOut": "_androidenterprise_23_KeyedAppStateOut",
        "PolicyIn": "_androidenterprise_24_PolicyIn",
        "PolicyOut": "_androidenterprise_25_PolicyOut",
        "ManagedConfigurationsSettingsIn": "_androidenterprise_26_ManagedConfigurationsSettingsIn",
        "ManagedConfigurationsSettingsOut": "_androidenterprise_27_ManagedConfigurationsSettingsOut",
        "ServiceAccountKeysListResponseIn": "_androidenterprise_28_ServiceAccountKeysListResponseIn",
        "ServiceAccountKeysListResponseOut": "_androidenterprise_29_ServiceAccountKeysListResponseOut",
        "ServiceAccountKeyIn": "_androidenterprise_30_ServiceAccountKeyIn",
        "ServiceAccountKeyOut": "_androidenterprise_31_ServiceAccountKeyOut",
        "WebAppsListResponseIn": "_androidenterprise_32_WebAppsListResponseIn",
        "WebAppsListResponseOut": "_androidenterprise_33_WebAppsListResponseOut",
        "ProductsApproveRequestIn": "_androidenterprise_34_ProductsApproveRequestIn",
        "ProductsApproveRequestOut": "_androidenterprise_35_ProductsApproveRequestOut",
        "DevicesListResponseIn": "_androidenterprise_36_DevicesListResponseIn",
        "DevicesListResponseOut": "_androidenterprise_37_DevicesListResponseOut",
        "DeviceReportUpdateEventIn": "_androidenterprise_38_DeviceReportUpdateEventIn",
        "DeviceReportUpdateEventOut": "_androidenterprise_39_DeviceReportUpdateEventOut",
        "ProductIn": "_androidenterprise_40_ProductIn",
        "ProductOut": "_androidenterprise_41_ProductOut",
        "TrackInfoIn": "_androidenterprise_42_TrackInfoIn",
        "TrackInfoOut": "_androidenterprise_43_TrackInfoOut",
        "AdministratorWebTokenSpecWebAppsIn": "_androidenterprise_44_AdministratorWebTokenSpecWebAppsIn",
        "AdministratorWebTokenSpecWebAppsOut": "_androidenterprise_45_AdministratorWebTokenSpecWebAppsOut",
        "PermissionIn": "_androidenterprise_46_PermissionIn",
        "PermissionOut": "_androidenterprise_47_PermissionOut",
        "ProductPolicyIn": "_androidenterprise_48_ProductPolicyIn",
        "ProductPolicyOut": "_androidenterprise_49_ProductPolicyOut",
        "EnterpriseAuthenticationAppLinkConfigIn": "_androidenterprise_50_EnterpriseAuthenticationAppLinkConfigIn",
        "EnterpriseAuthenticationAppLinkConfigOut": "_androidenterprise_51_EnterpriseAuthenticationAppLinkConfigOut",
        "AuthenticationTokenIn": "_androidenterprise_52_AuthenticationTokenIn",
        "AuthenticationTokenOut": "_androidenterprise_53_AuthenticationTokenOut",
        "ServiceAccountIn": "_androidenterprise_54_ServiceAccountIn",
        "ServiceAccountOut": "_androidenterprise_55_ServiceAccountOut",
        "StoreClusterIn": "_androidenterprise_56_StoreClusterIn",
        "StoreClusterOut": "_androidenterprise_57_StoreClusterOut",
        "PageInfoIn": "_androidenterprise_58_PageInfoIn",
        "PageInfoOut": "_androidenterprise_59_PageInfoOut",
        "GroupLicenseIn": "_androidenterprise_60_GroupLicenseIn",
        "GroupLicenseOut": "_androidenterprise_61_GroupLicenseOut",
        "InstallIn": "_androidenterprise_62_InstallIn",
        "InstallOut": "_androidenterprise_63_InstallOut",
        "ManagedPropertyIn": "_androidenterprise_64_ManagedPropertyIn",
        "ManagedPropertyOut": "_androidenterprise_65_ManagedPropertyOut",
        "EnterprisesSendTestPushNotificationResponseIn": "_androidenterprise_66_EnterprisesSendTestPushNotificationResponseIn",
        "EnterprisesSendTestPushNotificationResponseOut": "_androidenterprise_67_EnterprisesSendTestPushNotificationResponseOut",
        "SignupInfoIn": "_androidenterprise_68_SignupInfoIn",
        "SignupInfoOut": "_androidenterprise_69_SignupInfoOut",
        "InstallFailureEventIn": "_androidenterprise_70_InstallFailureEventIn",
        "InstallFailureEventOut": "_androidenterprise_71_InstallFailureEventOut",
        "AppRestrictionsSchemaRestrictionRestrictionValueIn": "_androidenterprise_72_AppRestrictionsSchemaRestrictionRestrictionValueIn",
        "AppRestrictionsSchemaRestrictionRestrictionValueOut": "_androidenterprise_73_AppRestrictionsSchemaRestrictionRestrictionValueOut",
        "NotificationIn": "_androidenterprise_74_NotificationIn",
        "NotificationOut": "_androidenterprise_75_NotificationOut",
        "EntitlementsListResponseIn": "_androidenterprise_76_EntitlementsListResponseIn",
        "EntitlementsListResponseOut": "_androidenterprise_77_EntitlementsListResponseOut",
        "NewDeviceEventIn": "_androidenterprise_78_NewDeviceEventIn",
        "NewDeviceEventOut": "_androidenterprise_79_NewDeviceEventOut",
        "ProductApprovalEventIn": "_androidenterprise_80_ProductApprovalEventIn",
        "ProductApprovalEventOut": "_androidenterprise_81_ProductApprovalEventOut",
        "ManagedConfigurationIn": "_androidenterprise_82_ManagedConfigurationIn",
        "ManagedConfigurationOut": "_androidenterprise_83_ManagedConfigurationOut",
        "DeviceStateIn": "_androidenterprise_84_DeviceStateIn",
        "DeviceStateOut": "_androidenterprise_85_DeviceStateOut",
        "AdministratorWebTokenSpecPlaySearchIn": "_androidenterprise_86_AdministratorWebTokenSpecPlaySearchIn",
        "AdministratorWebTokenSpecPlaySearchOut": "_androidenterprise_87_AdministratorWebTokenSpecPlaySearchOut",
        "StorePageIn": "_androidenterprise_88_StorePageIn",
        "StorePageOut": "_androidenterprise_89_StorePageOut",
        "ProductsListResponseIn": "_androidenterprise_90_ProductsListResponseIn",
        "ProductsListResponseOut": "_androidenterprise_91_ProductsListResponseOut",
        "EnterprisesListResponseIn": "_androidenterprise_92_EnterprisesListResponseIn",
        "EnterprisesListResponseOut": "_androidenterprise_93_EnterprisesListResponseOut",
        "UsersListResponseIn": "_androidenterprise_94_UsersListResponseIn",
        "UsersListResponseOut": "_androidenterprise_95_UsersListResponseOut",
        "ProductSigningCertificateIn": "_androidenterprise_96_ProductSigningCertificateIn",
        "ProductSigningCertificateOut": "_androidenterprise_97_ProductSigningCertificateOut",
        "StoreLayoutIn": "_androidenterprise_98_StoreLayoutIn",
        "StoreLayoutOut": "_androidenterprise_99_StoreLayoutOut",
        "GroupLicenseUsersListResponseIn": "_androidenterprise_100_GroupLicenseUsersListResponseIn",
        "GroupLicenseUsersListResponseOut": "_androidenterprise_101_GroupLicenseUsersListResponseOut",
        "ManagedConfigurationsSettingsListResponseIn": "_androidenterprise_102_ManagedConfigurationsSettingsListResponseIn",
        "ManagedConfigurationsSettingsListResponseOut": "_androidenterprise_103_ManagedConfigurationsSettingsListResponseOut",
        "AdministratorWebTokenIn": "_androidenterprise_104_AdministratorWebTokenIn",
        "AdministratorWebTokenOut": "_androidenterprise_105_AdministratorWebTokenOut",
        "ApprovalUrlInfoIn": "_androidenterprise_106_ApprovalUrlInfoIn",
        "ApprovalUrlInfoOut": "_androidenterprise_107_ApprovalUrlInfoOut",
        "AppUpdateEventIn": "_androidenterprise_108_AppUpdateEventIn",
        "AppUpdateEventOut": "_androidenterprise_109_AppUpdateEventOut",
        "StoreLayoutPagesListResponseIn": "_androidenterprise_110_StoreLayoutPagesListResponseIn",
        "StoreLayoutPagesListResponseOut": "_androidenterprise_111_StoreLayoutPagesListResponseOut",
        "TokenPaginationIn": "_androidenterprise_112_TokenPaginationIn",
        "TokenPaginationOut": "_androidenterprise_113_TokenPaginationOut",
        "ManagedConfigurationsForUserListResponseIn": "_androidenterprise_114_ManagedConfigurationsForUserListResponseIn",
        "ManagedConfigurationsForUserListResponseOut": "_androidenterprise_115_ManagedConfigurationsForUserListResponseOut",
        "EnterpriseIn": "_androidenterprise_116_EnterpriseIn",
        "EnterpriseOut": "_androidenterprise_117_EnterpriseOut",
        "ProductSetIn": "_androidenterprise_118_ProductSetIn",
        "ProductSetOut": "_androidenterprise_119_ProductSetOut",
        "NewPermissionsEventIn": "_androidenterprise_120_NewPermissionsEventIn",
        "NewPermissionsEventOut": "_androidenterprise_121_NewPermissionsEventOut",
        "AppStateIn": "_androidenterprise_122_AppStateIn",
        "AppStateOut": "_androidenterprise_123_AppStateOut",
        "ProductsGenerateApprovalUrlResponseIn": "_androidenterprise_124_ProductsGenerateApprovalUrlResponseIn",
        "ProductsGenerateApprovalUrlResponseOut": "_androidenterprise_125_ProductsGenerateApprovalUrlResponseOut",
        "ProductPermissionIn": "_androidenterprise_126_ProductPermissionIn",
        "ProductPermissionOut": "_androidenterprise_127_ProductPermissionOut",
        "ProductAvailabilityChangeEventIn": "_androidenterprise_128_ProductAvailabilityChangeEventIn",
        "ProductAvailabilityChangeEventOut": "_androidenterprise_129_ProductAvailabilityChangeEventOut",
        "AdministratorWebTokenSpecStoreBuilderIn": "_androidenterprise_130_AdministratorWebTokenSpecStoreBuilderIn",
        "AdministratorWebTokenSpecStoreBuilderOut": "_androidenterprise_131_AdministratorWebTokenSpecStoreBuilderOut",
        "DeviceReportIn": "_androidenterprise_132_DeviceReportIn",
        "DeviceReportOut": "_androidenterprise_133_DeviceReportOut",
        "AdministratorWebTokenSpecIn": "_androidenterprise_134_AdministratorWebTokenSpecIn",
        "AdministratorWebTokenSpecOut": "_androidenterprise_135_AdministratorWebTokenSpecOut",
        "VariableSetIn": "_androidenterprise_136_VariableSetIn",
        "VariableSetOut": "_androidenterprise_137_VariableSetOut",
        "WebAppIconIn": "_androidenterprise_138_WebAppIconIn",
        "WebAppIconOut": "_androidenterprise_139_WebAppIconOut",
        "GroupLicensesListResponseIn": "_androidenterprise_140_GroupLicensesListResponseIn",
        "GroupLicensesListResponseOut": "_androidenterprise_141_GroupLicensesListResponseOut",
        "AdministratorWebTokenSpecManagedConfigurationsIn": "_androidenterprise_142_AdministratorWebTokenSpecManagedConfigurationsIn",
        "AdministratorWebTokenSpecManagedConfigurationsOut": "_androidenterprise_143_AdministratorWebTokenSpecManagedConfigurationsOut",
        "AdministratorIn": "_androidenterprise_144_AdministratorIn",
        "AdministratorOut": "_androidenterprise_145_AdministratorOut",
        "UserIn": "_androidenterprise_146_UserIn",
        "UserOut": "_androidenterprise_147_UserOut",
        "ManagedConfigurationsForDeviceListResponseIn": "_androidenterprise_148_ManagedConfigurationsForDeviceListResponseIn",
        "ManagedConfigurationsForDeviceListResponseOut": "_androidenterprise_149_ManagedConfigurationsForDeviceListResponseOut",
        "AppRestrictionsSchemaChangeEventIn": "_androidenterprise_150_AppRestrictionsSchemaChangeEventIn",
        "AppRestrictionsSchemaChangeEventOut": "_androidenterprise_151_AppRestrictionsSchemaChangeEventOut",
        "LocalizedTextIn": "_androidenterprise_152_LocalizedTextIn",
        "LocalizedTextOut": "_androidenterprise_153_LocalizedTextOut",
        "ProductVisibilityIn": "_androidenterprise_154_ProductVisibilityIn",
        "ProductVisibilityOut": "_androidenterprise_155_ProductVisibilityOut",
        "ProductPermissionsIn": "_androidenterprise_156_ProductPermissionsIn",
        "ProductPermissionsOut": "_androidenterprise_157_ProductPermissionsOut",
        "CreateEnrollmentTokenResponseIn": "_androidenterprise_158_CreateEnrollmentTokenResponseIn",
        "CreateEnrollmentTokenResponseOut": "_androidenterprise_159_CreateEnrollmentTokenResponseOut",
        "AppVersionIn": "_androidenterprise_160_AppVersionIn",
        "AppVersionOut": "_androidenterprise_161_AppVersionOut",
        "MaintenanceWindowIn": "_androidenterprise_162_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_androidenterprise_163_MaintenanceWindowOut",
        "AutoInstallPolicyIn": "_androidenterprise_164_AutoInstallPolicyIn",
        "AutoInstallPolicyOut": "_androidenterprise_165_AutoInstallPolicyOut",
        "AdministratorWebTokenSpecZeroTouchIn": "_androidenterprise_166_AdministratorWebTokenSpecZeroTouchIn",
        "AdministratorWebTokenSpecZeroTouchOut": "_androidenterprise_167_AdministratorWebTokenSpecZeroTouchOut",
        "AutoInstallConstraintIn": "_androidenterprise_168_AutoInstallConstraintIn",
        "AutoInstallConstraintOut": "_androidenterprise_169_AutoInstallConstraintOut",
        "InstallsListResponseIn": "_androidenterprise_170_InstallsListResponseIn",
        "InstallsListResponseOut": "_androidenterprise_171_InstallsListResponseOut",
        "DeviceIn": "_androidenterprise_172_DeviceIn",
        "DeviceOut": "_androidenterprise_173_DeviceOut",
        "StoreLayoutClustersListResponseIn": "_androidenterprise_174_StoreLayoutClustersListResponseIn",
        "StoreLayoutClustersListResponseOut": "_androidenterprise_175_StoreLayoutClustersListResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EntitlementIn"] = t.struct(
        {"reason": t.string().optional(), "productId": t.string().optional()}
    ).named(renames["EntitlementIn"])
    types["EntitlementOut"] = t.struct(
        {
            "reason": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntitlementOut"])
    types["ConfigurationVariablesIn"] = t.struct(
        {
            "mcmId": t.string().optional(),
            "variableSet": t.array(t.proxy(renames["VariableSetIn"])).optional(),
        }
    ).named(renames["ConfigurationVariablesIn"])
    types["ConfigurationVariablesOut"] = t.struct(
        {
            "mcmId": t.string().optional(),
            "variableSet": t.array(t.proxy(renames["VariableSetOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigurationVariablesOut"])
    types["ManagedPropertyBundleIn"] = t.struct(
        {"managedProperty": t.array(t.proxy(renames["ManagedPropertyIn"])).optional()}
    ).named(renames["ManagedPropertyBundleIn"])
    types["ManagedPropertyBundleOut"] = t.struct(
        {
            "managedProperty": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPropertyBundleOut"])
    types["AppRestrictionsSchemaRestrictionIn"] = t.struct(
        {
            "entryValue": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "defaultValue": t.proxy(
                renames["AppRestrictionsSchemaRestrictionRestrictionValueIn"]
            ).optional(),
            "restrictionType": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "entry": t.array(t.string()).optional(),
            "nestedRestriction": t.array(
                t.proxy(renames["AppRestrictionsSchemaRestrictionIn"])
            ).optional(),
        }
    ).named(renames["AppRestrictionsSchemaRestrictionIn"])
    types["AppRestrictionsSchemaRestrictionOut"] = t.struct(
        {
            "entryValue": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "defaultValue": t.proxy(
                renames["AppRestrictionsSchemaRestrictionRestrictionValueOut"]
            ).optional(),
            "restrictionType": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "entry": t.array(t.string()).optional(),
            "nestedRestriction": t.array(
                t.proxy(renames["AppRestrictionsSchemaRestrictionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppRestrictionsSchemaRestrictionOut"])
    types["WebAppIn"] = t.struct(
        {
            "versionCode": t.string().optional(),
            "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
            "title": t.string().optional(),
            "webAppId": t.string().optional(),
            "startUrl": t.string().optional(),
            "displayMode": t.string().optional(),
            "isPublished": t.boolean().optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "versionCode": t.string().optional(),
            "icons": t.array(t.proxy(renames["WebAppIconOut"])).optional(),
            "title": t.string().optional(),
            "webAppId": t.string().optional(),
            "startUrl": t.string().optional(),
            "displayMode": t.string().optional(),
            "isPublished": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
    types["AdministratorWebTokenSpecPrivateAppsIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecPrivateAppsIn"])
    types["AdministratorWebTokenSpecPrivateAppsOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecPrivateAppsOut"])
    types["NotificationSetIn"] = t.struct(
        {
            "notificationSetId": t.string().optional(),
            "notification": t.array(t.proxy(renames["NotificationIn"])).optional(),
        }
    ).named(renames["NotificationSetIn"])
    types["NotificationSetOut"] = t.struct(
        {
            "notificationSetId": t.string().optional(),
            "notification": t.array(t.proxy(renames["NotificationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationSetOut"])
    types["AppRestrictionsSchemaIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "restrictions": t.array(
                t.proxy(renames["AppRestrictionsSchemaRestrictionIn"])
            ).optional(),
        }
    ).named(renames["AppRestrictionsSchemaIn"])
    types["AppRestrictionsSchemaOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "restrictions": t.array(
                t.proxy(renames["AppRestrictionsSchemaRestrictionOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppRestrictionsSchemaOut"])
    types["EnterpriseAccountIn"] = t.struct(
        {"accountEmail": t.string().optional()}
    ).named(renames["EnterpriseAccountIn"])
    types["EnterpriseAccountOut"] = t.struct(
        {
            "accountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseAccountOut"])
    types["GoogleAuthenticationSettingsIn"] = t.struct(
        {
            "dedicatedDevicesAllowed": t.string().optional(),
            "googleAuthenticationRequired": t.string().optional(),
        }
    ).named(renames["GoogleAuthenticationSettingsIn"])
    types["GoogleAuthenticationSettingsOut"] = t.struct(
        {
            "dedicatedDevicesAllowed": t.string().optional(),
            "googleAuthenticationRequired": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAuthenticationSettingsOut"])
    types["KeyedAppStateIn"] = t.struct(
        {
            "severity": t.string().optional(),
            "key": t.string().optional(),
            "data": t.string().optional(),
            "stateTimestampMillis": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["KeyedAppStateIn"])
    types["KeyedAppStateOut"] = t.struct(
        {
            "severity": t.string().optional(),
            "key": t.string().optional(),
            "data": t.string().optional(),
            "stateTimestampMillis": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyedAppStateOut"])
    types["PolicyIn"] = t.struct(
        {
            "productPolicy": t.array(t.proxy(renames["ProductPolicyIn"])).optional(),
            "productAvailabilityPolicy": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "deviceReportPolicy": t.string().optional(),
            "autoUpdatePolicy": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "productPolicy": t.array(t.proxy(renames["ProductPolicyOut"])).optional(),
            "productAvailabilityPolicy": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "deviceReportPolicy": t.string().optional(),
            "autoUpdatePolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ManagedConfigurationsSettingsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "lastUpdatedTimestampMillis": t.string().optional(),
            "mcmId": t.string().optional(),
        }
    ).named(renames["ManagedConfigurationsSettingsIn"])
    types["ManagedConfigurationsSettingsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "lastUpdatedTimestampMillis": t.string().optional(),
            "mcmId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedConfigurationsSettingsOut"])
    types["ServiceAccountKeysListResponseIn"] = t.struct(
        {
            "serviceAccountKey": t.array(
                t.proxy(renames["ServiceAccountKeyIn"])
            ).optional()
        }
    ).named(renames["ServiceAccountKeysListResponseIn"])
    types["ServiceAccountKeysListResponseOut"] = t.struct(
        {
            "serviceAccountKey": t.array(
                t.proxy(renames["ServiceAccountKeyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountKeysListResponseOut"])
    types["ServiceAccountKeyIn"] = t.struct(
        {
            "id": t.string().optional(),
            "data": t.string().optional(),
            "type": t.string().optional(),
            "publicData": t.string().optional(),
        }
    ).named(renames["ServiceAccountKeyIn"])
    types["ServiceAccountKeyOut"] = t.struct(
        {
            "id": t.string().optional(),
            "data": t.string().optional(),
            "type": t.string().optional(),
            "publicData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountKeyOut"])
    types["WebAppsListResponseIn"] = t.struct(
        {"webApp": t.array(t.proxy(renames["WebAppIn"])).optional()}
    ).named(renames["WebAppsListResponseIn"])
    types["WebAppsListResponseOut"] = t.struct(
        {
            "webApp": t.array(t.proxy(renames["WebAppOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppsListResponseOut"])
    types["ProductsApproveRequestIn"] = t.struct(
        {
            "approvalUrlInfo": t.proxy(renames["ApprovalUrlInfoIn"]).optional(),
            "approvedPermissions": t.string().optional(),
        }
    ).named(renames["ProductsApproveRequestIn"])
    types["ProductsApproveRequestOut"] = t.struct(
        {
            "approvalUrlInfo": t.proxy(renames["ApprovalUrlInfoOut"]).optional(),
            "approvedPermissions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsApproveRequestOut"])
    types["DevicesListResponseIn"] = t.struct(
        {"device": t.array(t.proxy(renames["DeviceIn"])).optional()}
    ).named(renames["DevicesListResponseIn"])
    types["DevicesListResponseOut"] = t.struct(
        {
            "device": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicesListResponseOut"])
    types["DeviceReportUpdateEventIn"] = t.struct(
        {
            "userId": t.string().optional(),
            "report": t.proxy(renames["DeviceReportIn"]).optional(),
            "deviceId": t.string().optional(),
        }
    ).named(renames["DeviceReportUpdateEventIn"])
    types["DeviceReportUpdateEventOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "report": t.proxy(renames["DeviceReportOut"]).optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceReportUpdateEventOut"])
    types["ProductIn"] = t.struct(
        {
            "appTracks": t.array(t.proxy(renames["TrackInfoIn"])).optional(),
            "workDetailsUrl": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "smallIconUrl": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "requiresContainerApp": t.boolean().optional(),
            "contentRating": t.string().optional(),
            "availableTracks": t.array(t.string()).optional(),
            "iconUrl": t.string().optional(),
            "availableCountries": t.array(t.string()).optional(),
            "permissions": t.array(t.proxy(renames["ProductPermissionIn"])).optional(),
            "detailsUrl": t.string().optional(),
            "distributionChannel": t.string().optional(),
            "title": t.string().optional(),
            "lastUpdatedTimestampMillis": t.string().optional(),
            "fullDescription": t.string().optional(),
            "productId": t.string().optional(),
            "appRestrictionsSchema": t.proxy(
                renames["AppRestrictionsSchemaIn"]
            ).optional(),
            "authorName": t.string().optional(),
            "productPricing": t.string().optional(),
            "category": t.string().optional(),
            "signingCertificate": t.proxy(
                renames["ProductSigningCertificateIn"]
            ).optional(),
            "description": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "appVersion": t.array(t.proxy(renames["AppVersionIn"])).optional(),
            "recentChanges": t.string().optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "appTracks": t.array(t.proxy(renames["TrackInfoOut"])).optional(),
            "workDetailsUrl": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "smallIconUrl": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "requiresContainerApp": t.boolean().optional(),
            "contentRating": t.string().optional(),
            "availableTracks": t.array(t.string()).optional(),
            "iconUrl": t.string().optional(),
            "availableCountries": t.array(t.string()).optional(),
            "permissions": t.array(t.proxy(renames["ProductPermissionOut"])).optional(),
            "detailsUrl": t.string().optional(),
            "distributionChannel": t.string().optional(),
            "title": t.string().optional(),
            "lastUpdatedTimestampMillis": t.string().optional(),
            "fullDescription": t.string().optional(),
            "productId": t.string().optional(),
            "appRestrictionsSchema": t.proxy(
                renames["AppRestrictionsSchemaOut"]
            ).optional(),
            "authorName": t.string().optional(),
            "productPricing": t.string().optional(),
            "category": t.string().optional(),
            "signingCertificate": t.proxy(
                renames["ProductSigningCertificateOut"]
            ).optional(),
            "description": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "appVersion": t.array(t.proxy(renames["AppVersionOut"])).optional(),
            "recentChanges": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
    types["TrackInfoIn"] = t.struct(
        {"trackId": t.string().optional(), "trackAlias": t.string().optional()}
    ).named(renames["TrackInfoIn"])
    types["TrackInfoOut"] = t.struct(
        {
            "trackId": t.string().optional(),
            "trackAlias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackInfoOut"])
    types["AdministratorWebTokenSpecWebAppsIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecWebAppsIn"])
    types["AdministratorWebTokenSpecWebAppsOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecWebAppsOut"])
    types["PermissionIn"] = t.struct(
        {
            "permissionId": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["PermissionIn"])
    types["PermissionOut"] = t.struct(
        {
            "permissionId": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionOut"])
    types["ProductPolicyIn"] = t.struct(
        {
            "autoInstallPolicy": t.proxy(renames["AutoInstallPolicyIn"]).optional(),
            "managedConfiguration": t.proxy(
                renames["ManagedConfigurationIn"]
            ).optional(),
            "trackIds": t.array(t.string()).optional(),
            "autoUpdateMode": t.string().optional(),
            "enterpriseAuthenticationAppLinkConfigs": t.array(
                t.proxy(renames["EnterpriseAuthenticationAppLinkConfigIn"])
            ).optional(),
            "productId": t.string().optional(),
            "tracks": t.array(t.string()).optional(),
        }
    ).named(renames["ProductPolicyIn"])
    types["ProductPolicyOut"] = t.struct(
        {
            "autoInstallPolicy": t.proxy(renames["AutoInstallPolicyOut"]).optional(),
            "managedConfiguration": t.proxy(
                renames["ManagedConfigurationOut"]
            ).optional(),
            "trackIds": t.array(t.string()).optional(),
            "autoUpdateMode": t.string().optional(),
            "enterpriseAuthenticationAppLinkConfigs": t.array(
                t.proxy(renames["EnterpriseAuthenticationAppLinkConfigOut"])
            ).optional(),
            "productId": t.string().optional(),
            "tracks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductPolicyOut"])
    types["EnterpriseAuthenticationAppLinkConfigIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["EnterpriseAuthenticationAppLinkConfigIn"])
    types["EnterpriseAuthenticationAppLinkConfigOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseAuthenticationAppLinkConfigOut"])
    types["AuthenticationTokenIn"] = t.struct({"token": t.string().optional()}).named(
        renames["AuthenticationTokenIn"]
    )
    types["AuthenticationTokenOut"] = t.struct(
        {
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationTokenOut"])
    types["ServiceAccountIn"] = t.struct(
        {
            "name": t.string().optional(),
            "key": t.proxy(renames["ServiceAccountKeyIn"]).optional(),
        }
    ).named(renames["ServiceAccountIn"])
    types["ServiceAccountOut"] = t.struct(
        {
            "name": t.string().optional(),
            "key": t.proxy(renames["ServiceAccountKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountOut"])
    types["StoreClusterIn"] = t.struct(
        {
            "orderInPage": t.string().optional(),
            "productId": t.array(t.string()).optional(),
            "name": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["StoreClusterIn"])
    types["StoreClusterOut"] = t.struct(
        {
            "orderInPage": t.string().optional(),
            "productId": t.array(t.string()).optional(),
            "name": t.array(t.proxy(renames["LocalizedTextOut"])).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoreClusterOut"])
    types["PageInfoIn"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "resultPerPage": t.integer().optional(),
            "startIndex": t.integer().optional(),
        }
    ).named(renames["PageInfoIn"])
    types["PageInfoOut"] = t.struct(
        {
            "totalResults": t.integer().optional(),
            "resultPerPage": t.integer().optional(),
            "startIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageInfoOut"])
    types["GroupLicenseIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "numPurchased": t.integer().optional(),
            "permissions": t.string().optional(),
            "approval": t.string().optional(),
            "acquisitionKind": t.string().optional(),
            "numProvisioned": t.integer().optional(),
        }
    ).named(renames["GroupLicenseIn"])
    types["GroupLicenseOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "numPurchased": t.integer().optional(),
            "permissions": t.string().optional(),
            "approval": t.string().optional(),
            "acquisitionKind": t.string().optional(),
            "numProvisioned": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupLicenseOut"])
    types["InstallIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "versionCode": t.integer().optional(),
            "installState": t.string().optional(),
        }
    ).named(renames["InstallIn"])
    types["InstallOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "versionCode": t.integer().optional(),
            "installState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstallOut"])
    types["ManagedPropertyIn"] = t.struct(
        {
            "valueBundle": t.proxy(renames["ManagedPropertyBundleIn"]).optional(),
            "valueBundleArray": t.array(
                t.proxy(renames["ManagedPropertyBundleIn"])
            ).optional(),
            "valueInteger": t.integer().optional(),
            "valueBool": t.boolean().optional(),
            "valueString": t.string().optional(),
            "key": t.string().optional(),
            "valueStringArray": t.array(t.string()).optional(),
        }
    ).named(renames["ManagedPropertyIn"])
    types["ManagedPropertyOut"] = t.struct(
        {
            "valueBundle": t.proxy(renames["ManagedPropertyBundleOut"]).optional(),
            "valueBundleArray": t.array(
                t.proxy(renames["ManagedPropertyBundleOut"])
            ).optional(),
            "valueInteger": t.integer().optional(),
            "valueBool": t.boolean().optional(),
            "valueString": t.string().optional(),
            "key": t.string().optional(),
            "valueStringArray": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPropertyOut"])
    types["EnterprisesSendTestPushNotificationResponseIn"] = t.struct(
        {"messageId": t.string().optional(), "topicName": t.string().optional()}
    ).named(renames["EnterprisesSendTestPushNotificationResponseIn"])
    types["EnterprisesSendTestPushNotificationResponseOut"] = t.struct(
        {
            "messageId": t.string().optional(),
            "topicName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterprisesSendTestPushNotificationResponseOut"])
    types["SignupInfoIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "completionToken": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["SignupInfoIn"])
    types["SignupInfoOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "completionToken": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignupInfoOut"])
    types["InstallFailureEventIn"] = t.struct(
        {
            "failureDetails": t.string().optional(),
            "failureReason": t.string().optional(),
            "productId": t.string().optional(),
            "userId": t.string().optional(),
            "deviceId": t.string().optional(),
        }
    ).named(renames["InstallFailureEventIn"])
    types["InstallFailureEventOut"] = t.struct(
        {
            "failureDetails": t.string().optional(),
            "failureReason": t.string().optional(),
            "productId": t.string().optional(),
            "userId": t.string().optional(),
            "deviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstallFailureEventOut"])
    types["AppRestrictionsSchemaRestrictionRestrictionValueIn"] = t.struct(
        {
            "type": t.string().optional(),
            "valueMultiselect": t.array(t.string()).optional(),
            "valueInteger": t.integer().optional(),
            "valueString": t.string().optional(),
            "valueBool": t.boolean().optional(),
        }
    ).named(renames["AppRestrictionsSchemaRestrictionRestrictionValueIn"])
    types["AppRestrictionsSchemaRestrictionRestrictionValueOut"] = t.struct(
        {
            "type": t.string().optional(),
            "valueMultiselect": t.array(t.string()).optional(),
            "valueInteger": t.integer().optional(),
            "valueString": t.string().optional(),
            "valueBool": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppRestrictionsSchemaRestrictionRestrictionValueOut"])
    types["NotificationIn"] = t.struct(
        {
            "notificationType": t.string().optional(),
            "productAvailabilityChangeEvent": t.proxy(
                renames["ProductAvailabilityChangeEventIn"]
            ).optional(),
            "appRestrictionsSchemaChangeEvent": t.proxy(
                renames["AppRestrictionsSchemaChangeEventIn"]
            ).optional(),
            "deviceReportUpdateEvent": t.proxy(
                renames["DeviceReportUpdateEventIn"]
            ).optional(),
            "newDeviceEvent": t.proxy(renames["NewDeviceEventIn"]).optional(),
            "enterpriseId": t.string().optional(),
            "productApprovalEvent": t.proxy(
                renames["ProductApprovalEventIn"]
            ).optional(),
            "installFailureEvent": t.proxy(renames["InstallFailureEventIn"]).optional(),
            "appUpdateEvent": t.proxy(renames["AppUpdateEventIn"]).optional(),
            "newPermissionsEvent": t.proxy(renames["NewPermissionsEventIn"]).optional(),
            "timestampMillis": t.string().optional(),
        }
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "notificationType": t.string().optional(),
            "productAvailabilityChangeEvent": t.proxy(
                renames["ProductAvailabilityChangeEventOut"]
            ).optional(),
            "appRestrictionsSchemaChangeEvent": t.proxy(
                renames["AppRestrictionsSchemaChangeEventOut"]
            ).optional(),
            "deviceReportUpdateEvent": t.proxy(
                renames["DeviceReportUpdateEventOut"]
            ).optional(),
            "newDeviceEvent": t.proxy(renames["NewDeviceEventOut"]).optional(),
            "enterpriseId": t.string().optional(),
            "productApprovalEvent": t.proxy(
                renames["ProductApprovalEventOut"]
            ).optional(),
            "installFailureEvent": t.proxy(
                renames["InstallFailureEventOut"]
            ).optional(),
            "appUpdateEvent": t.proxy(renames["AppUpdateEventOut"]).optional(),
            "newPermissionsEvent": t.proxy(
                renames["NewPermissionsEventOut"]
            ).optional(),
            "timestampMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["EntitlementsListResponseIn"] = t.struct(
        {"entitlement": t.array(t.proxy(renames["EntitlementIn"])).optional()}
    ).named(renames["EntitlementsListResponseIn"])
    types["EntitlementsListResponseOut"] = t.struct(
        {
            "entitlement": t.array(t.proxy(renames["EntitlementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntitlementsListResponseOut"])
    types["NewDeviceEventIn"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "userId": t.string().optional(),
            "managementType": t.string().optional(),
            "dpcPackageName": t.string().optional(),
        }
    ).named(renames["NewDeviceEventIn"])
    types["NewDeviceEventOut"] = t.struct(
        {
            "deviceId": t.string().optional(),
            "userId": t.string().optional(),
            "managementType": t.string().optional(),
            "dpcPackageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NewDeviceEventOut"])
    types["ProductApprovalEventIn"] = t.struct(
        {"productId": t.string().optional(), "approved": t.string().optional()}
    ).named(renames["ProductApprovalEventIn"])
    types["ProductApprovalEventOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "approved": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductApprovalEventOut"])
    types["ManagedConfigurationIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "managedProperty": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
            "productId": t.string().optional(),
            "configurationVariables": t.proxy(
                renames["ConfigurationVariablesIn"]
            ).optional(),
        }
    ).named(renames["ManagedConfigurationIn"])
    types["ManagedConfigurationOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "managedProperty": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "productId": t.string().optional(),
            "configurationVariables": t.proxy(
                renames["ConfigurationVariablesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedConfigurationOut"])
    types["DeviceStateIn"] = t.struct({"accountState": t.string().optional()}).named(
        renames["DeviceStateIn"]
    )
    types["DeviceStateOut"] = t.struct(
        {
            "accountState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceStateOut"])
    types["AdministratorWebTokenSpecPlaySearchIn"] = t.struct(
        {"approveApps": t.boolean().optional(), "enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecPlaySearchIn"])
    types["AdministratorWebTokenSpecPlaySearchOut"] = t.struct(
        {
            "approveApps": t.boolean().optional(),
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecPlaySearchOut"])
    types["StorePageIn"] = t.struct(
        {
            "id": t.string().optional(),
            "link": t.array(t.string()).optional(),
            "name": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
        }
    ).named(renames["StorePageIn"])
    types["StorePageOut"] = t.struct(
        {
            "id": t.string().optional(),
            "link": t.array(t.string()).optional(),
            "name": t.array(t.proxy(renames["LocalizedTextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorePageOut"])
    types["ProductsListResponseIn"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]).optional(),
            "product": t.array(t.proxy(renames["ProductIn"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
        }
    ).named(renames["ProductsListResponseIn"])
    types["ProductsListResponseOut"] = t.struct(
        {
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]).optional(),
            "product": t.array(t.proxy(renames["ProductOut"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsListResponseOut"])
    types["EnterprisesListResponseIn"] = t.struct(
        {"enterprise": t.array(t.proxy(renames["EnterpriseIn"])).optional()}
    ).named(renames["EnterprisesListResponseIn"])
    types["EnterprisesListResponseOut"] = t.struct(
        {
            "enterprise": t.array(t.proxy(renames["EnterpriseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterprisesListResponseOut"])
    types["UsersListResponseIn"] = t.struct(
        {"user": t.array(t.proxy(renames["UserIn"])).optional()}
    ).named(renames["UsersListResponseIn"])
    types["UsersListResponseOut"] = t.struct(
        {
            "user": t.array(t.proxy(renames["UserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsersListResponseOut"])
    types["ProductSigningCertificateIn"] = t.struct(
        {
            "certificateHashSha256": t.string().optional(),
            "certificateHashSha1": t.string().optional(),
        }
    ).named(renames["ProductSigningCertificateIn"])
    types["ProductSigningCertificateOut"] = t.struct(
        {
            "certificateHashSha256": t.string().optional(),
            "certificateHashSha1": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSigningCertificateOut"])
    types["StoreLayoutIn"] = t.struct(
        {"homepageId": t.string().optional(), "storeLayoutType": t.string().optional()}
    ).named(renames["StoreLayoutIn"])
    types["StoreLayoutOut"] = t.struct(
        {
            "homepageId": t.string().optional(),
            "storeLayoutType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoreLayoutOut"])
    types["GroupLicenseUsersListResponseIn"] = t.struct(
        {"user": t.array(t.proxy(renames["UserIn"])).optional()}
    ).named(renames["GroupLicenseUsersListResponseIn"])
    types["GroupLicenseUsersListResponseOut"] = t.struct(
        {
            "user": t.array(t.proxy(renames["UserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupLicenseUsersListResponseOut"])
    types["ManagedConfigurationsSettingsListResponseIn"] = t.struct(
        {
            "managedConfigurationsSettings": t.array(
                t.proxy(renames["ManagedConfigurationsSettingsIn"])
            ).optional()
        }
    ).named(renames["ManagedConfigurationsSettingsListResponseIn"])
    types["ManagedConfigurationsSettingsListResponseOut"] = t.struct(
        {
            "managedConfigurationsSettings": t.array(
                t.proxy(renames["ManagedConfigurationsSettingsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedConfigurationsSettingsListResponseOut"])
    types["AdministratorWebTokenIn"] = t.struct({"token": t.string().optional()}).named(
        renames["AdministratorWebTokenIn"]
    )
    types["AdministratorWebTokenOut"] = t.struct(
        {
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenOut"])
    types["ApprovalUrlInfoIn"] = t.struct({"approvalUrl": t.string().optional()}).named(
        renames["ApprovalUrlInfoIn"]
    )
    types["ApprovalUrlInfoOut"] = t.struct(
        {
            "approvalUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalUrlInfoOut"])
    types["AppUpdateEventIn"] = t.struct({"productId": t.string().optional()}).named(
        renames["AppUpdateEventIn"]
    )
    types["AppUpdateEventOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppUpdateEventOut"])
    types["StoreLayoutPagesListResponseIn"] = t.struct(
        {"page": t.array(t.proxy(renames["StorePageIn"])).optional()}
    ).named(renames["StoreLayoutPagesListResponseIn"])
    types["StoreLayoutPagesListResponseOut"] = t.struct(
        {
            "page": t.array(t.proxy(renames["StorePageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoreLayoutPagesListResponseOut"])
    types["TokenPaginationIn"] = t.struct(
        {"previousPageToken": t.string(), "nextPageToken": t.string().optional()}
    ).named(renames["TokenPaginationIn"])
    types["TokenPaginationOut"] = t.struct(
        {
            "previousPageToken": t.string(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenPaginationOut"])
    types["ManagedConfigurationsForUserListResponseIn"] = t.struct(
        {
            "managedConfigurationForUser": t.array(
                t.proxy(renames["ManagedConfigurationIn"])
            ).optional()
        }
    ).named(renames["ManagedConfigurationsForUserListResponseIn"])
    types["ManagedConfigurationsForUserListResponseOut"] = t.struct(
        {
            "managedConfigurationForUser": t.array(
                t.proxy(renames["ManagedConfigurationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedConfigurationsForUserListResponseOut"])
    types["EnterpriseIn"] = t.struct(
        {
            "administrator": t.array(t.proxy(renames["AdministratorIn"])).optional(),
            "name": t.string().optional(),
            "primaryDomain": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["EnterpriseIn"])
    types["EnterpriseOut"] = t.struct(
        {
            "administrator": t.array(t.proxy(renames["AdministratorOut"])).optional(),
            "googleAuthenticationSettings": t.proxy(
                renames["GoogleAuthenticationSettingsOut"]
            ).optional(),
            "name": t.string().optional(),
            "primaryDomain": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseOut"])
    types["ProductSetIn"] = t.struct(
        {
            "productVisibility": t.array(
                t.proxy(renames["ProductVisibilityIn"])
            ).optional(),
            "productId": t.array(t.string()).optional(),
            "productSetBehavior": t.string().optional(),
        }
    ).named(renames["ProductSetIn"])
    types["ProductSetOut"] = t.struct(
        {
            "productVisibility": t.array(
                t.proxy(renames["ProductVisibilityOut"])
            ).optional(),
            "productId": t.array(t.string()).optional(),
            "productSetBehavior": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSetOut"])
    types["NewPermissionsEventIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "requestedPermissions": t.array(t.string()).optional(),
            "approvedPermissions": t.array(t.string()).optional(),
        }
    ).named(renames["NewPermissionsEventIn"])
    types["NewPermissionsEventOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "requestedPermissions": t.array(t.string()).optional(),
            "approvedPermissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NewPermissionsEventOut"])
    types["AppStateIn"] = t.struct(
        {
            "keyedAppState": t.array(t.proxy(renames["KeyedAppStateIn"])).optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["AppStateIn"])
    types["AppStateOut"] = t.struct(
        {
            "keyedAppState": t.array(t.proxy(renames["KeyedAppStateOut"])).optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppStateOut"])
    types["ProductsGenerateApprovalUrlResponseIn"] = t.struct(
        {"url": t.string().optional()}
    ).named(renames["ProductsGenerateApprovalUrlResponseIn"])
    types["ProductsGenerateApprovalUrlResponseOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsGenerateApprovalUrlResponseOut"])
    types["ProductPermissionIn"] = t.struct(
        {"permissionId": t.string().optional(), "state": t.string().optional()}
    ).named(renames["ProductPermissionIn"])
    types["ProductPermissionOut"] = t.struct(
        {
            "permissionId": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductPermissionOut"])
    types["ProductAvailabilityChangeEventIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "availabilityStatus": t.string().optional(),
        }
    ).named(renames["ProductAvailabilityChangeEventIn"])
    types["ProductAvailabilityChangeEventOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "availabilityStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductAvailabilityChangeEventOut"])
    types["AdministratorWebTokenSpecStoreBuilderIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecStoreBuilderIn"])
    types["AdministratorWebTokenSpecStoreBuilderOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecStoreBuilderOut"])
    types["DeviceReportIn"] = t.struct(
        {
            "appState": t.array(t.proxy(renames["AppStateIn"])).optional(),
            "lastUpdatedTimestampMillis": t.string().optional(),
        }
    ).named(renames["DeviceReportIn"])
    types["DeviceReportOut"] = t.struct(
        {
            "appState": t.array(t.proxy(renames["AppStateOut"])).optional(),
            "lastUpdatedTimestampMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceReportOut"])
    types["AdministratorWebTokenSpecIn"] = t.struct(
        {
            "playSearch": t.proxy(
                renames["AdministratorWebTokenSpecPlaySearchIn"]
            ).optional(),
            "privateApps": t.proxy(
                renames["AdministratorWebTokenSpecPrivateAppsIn"]
            ).optional(),
            "zeroTouch": t.proxy(
                renames["AdministratorWebTokenSpecZeroTouchIn"]
            ).optional(),
            "webApps": t.proxy(
                renames["AdministratorWebTokenSpecWebAppsIn"]
            ).optional(),
            "managedConfigurations": t.proxy(
                renames["AdministratorWebTokenSpecManagedConfigurationsIn"]
            ).optional(),
            "permission": t.array(t.string()).optional(),
            "parent": t.string().optional(),
            "storeBuilder": t.proxy(
                renames["AdministratorWebTokenSpecStoreBuilderIn"]
            ).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecIn"])
    types["AdministratorWebTokenSpecOut"] = t.struct(
        {
            "playSearch": t.proxy(
                renames["AdministratorWebTokenSpecPlaySearchOut"]
            ).optional(),
            "privateApps": t.proxy(
                renames["AdministratorWebTokenSpecPrivateAppsOut"]
            ).optional(),
            "zeroTouch": t.proxy(
                renames["AdministratorWebTokenSpecZeroTouchOut"]
            ).optional(),
            "webApps": t.proxy(
                renames["AdministratorWebTokenSpecWebAppsOut"]
            ).optional(),
            "managedConfigurations": t.proxy(
                renames["AdministratorWebTokenSpecManagedConfigurationsOut"]
            ).optional(),
            "permission": t.array(t.string()).optional(),
            "parent": t.string().optional(),
            "storeBuilder": t.proxy(
                renames["AdministratorWebTokenSpecStoreBuilderOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecOut"])
    types["VariableSetIn"] = t.struct(
        {"userValue": t.string().optional(), "placeholder": t.string().optional()}
    ).named(renames["VariableSetIn"])
    types["VariableSetOut"] = t.struct(
        {
            "userValue": t.string().optional(),
            "placeholder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableSetOut"])
    types["WebAppIconIn"] = t.struct({"imageData": t.string().optional()}).named(
        renames["WebAppIconIn"]
    )
    types["WebAppIconOut"] = t.struct(
        {
            "imageData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppIconOut"])
    types["GroupLicensesListResponseIn"] = t.struct(
        {"groupLicense": t.array(t.proxy(renames["GroupLicenseIn"])).optional()}
    ).named(renames["GroupLicensesListResponseIn"])
    types["GroupLicensesListResponseOut"] = t.struct(
        {
            "groupLicense": t.array(t.proxy(renames["GroupLicenseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupLicensesListResponseOut"])
    types["AdministratorWebTokenSpecManagedConfigurationsIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecManagedConfigurationsIn"])
    types["AdministratorWebTokenSpecManagedConfigurationsOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecManagedConfigurationsOut"])
    types["AdministratorIn"] = t.struct({"email": t.string().optional()}).named(
        renames["AdministratorIn"]
    )
    types["AdministratorOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorOut"])
    types["UserIn"] = t.struct(
        {
            "accountType": t.string().optional(),
            "primaryEmail": t.string().optional(),
            "id": t.string().optional(),
            "accountIdentifier": t.string().optional(),
            "managementType": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "accountType": t.string().optional(),
            "primaryEmail": t.string().optional(),
            "id": t.string().optional(),
            "accountIdentifier": t.string().optional(),
            "managementType": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["ManagedConfigurationsForDeviceListResponseIn"] = t.struct(
        {
            "managedConfigurationForDevice": t.array(
                t.proxy(renames["ManagedConfigurationIn"])
            ).optional()
        }
    ).named(renames["ManagedConfigurationsForDeviceListResponseIn"])
    types["ManagedConfigurationsForDeviceListResponseOut"] = t.struct(
        {
            "managedConfigurationForDevice": t.array(
                t.proxy(renames["ManagedConfigurationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedConfigurationsForDeviceListResponseOut"])
    types["AppRestrictionsSchemaChangeEventIn"] = t.struct(
        {"productId": t.string().optional()}
    ).named(renames["AppRestrictionsSchemaChangeEventIn"])
    types["AppRestrictionsSchemaChangeEventOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppRestrictionsSchemaChangeEventOut"])
    types["LocalizedTextIn"] = t.struct(
        {"locale": t.string().optional(), "text": t.string().optional()}
    ).named(renames["LocalizedTextIn"])
    types["LocalizedTextOut"] = t.struct(
        {
            "locale": t.string().optional(),
            "text": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedTextOut"])
    types["ProductVisibilityIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "tracks": t.array(t.string()).optional(),
            "trackIds": t.array(t.string()).optional(),
        }
    ).named(renames["ProductVisibilityIn"])
    types["ProductVisibilityOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "tracks": t.array(t.string()).optional(),
            "trackIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductVisibilityOut"])
    types["ProductPermissionsIn"] = t.struct(
        {
            "permission": t.array(t.proxy(renames["ProductPermissionIn"])).optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["ProductPermissionsIn"])
    types["ProductPermissionsOut"] = t.struct(
        {
            "permission": t.array(t.proxy(renames["ProductPermissionOut"])).optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductPermissionsOut"])
    types["CreateEnrollmentTokenResponseIn"] = t.struct(
        {"enrollmentToken": t.string().optional()}
    ).named(renames["CreateEnrollmentTokenResponseIn"])
    types["CreateEnrollmentTokenResponseOut"] = t.struct(
        {
            "enrollmentToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateEnrollmentTokenResponseOut"])
    types["AppVersionIn"] = t.struct(
        {
            "versionString": t.string().optional(),
            "versionCode": t.integer().optional(),
            "track": t.string().optional(),
            "trackId": t.array(t.string()).optional(),
            "isProduction": t.boolean().optional(),
        }
    ).named(renames["AppVersionIn"])
    types["AppVersionOut"] = t.struct(
        {
            "versionString": t.string().optional(),
            "versionCode": t.integer().optional(),
            "track": t.string().optional(),
            "trackId": t.array(t.string()).optional(),
            "isProduction": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppVersionOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "durationMs": t.string().optional(),
            "startTimeAfterMidnightMs": t.string().optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "durationMs": t.string().optional(),
            "startTimeAfterMidnightMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
    types["AutoInstallPolicyIn"] = t.struct(
        {
            "autoInstallMode": t.string().optional(),
            "autoInstallConstraint": t.array(
                t.proxy(renames["AutoInstallConstraintIn"])
            ).optional(),
            "minimumVersionCode": t.integer().optional(),
            "autoInstallPriority": t.integer().optional(),
        }
    ).named(renames["AutoInstallPolicyIn"])
    types["AutoInstallPolicyOut"] = t.struct(
        {
            "autoInstallMode": t.string().optional(),
            "autoInstallConstraint": t.array(
                t.proxy(renames["AutoInstallConstraintOut"])
            ).optional(),
            "minimumVersionCode": t.integer().optional(),
            "autoInstallPriority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoInstallPolicyOut"])
    types["AdministratorWebTokenSpecZeroTouchIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecZeroTouchIn"])
    types["AdministratorWebTokenSpecZeroTouchOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecZeroTouchOut"])
    types["AutoInstallConstraintIn"] = t.struct(
        {
            "networkTypeConstraint": t.string().optional(),
            "deviceIdleStateConstraint": t.string().optional(),
            "chargingStateConstraint": t.string().optional(),
        }
    ).named(renames["AutoInstallConstraintIn"])
    types["AutoInstallConstraintOut"] = t.struct(
        {
            "networkTypeConstraint": t.string().optional(),
            "deviceIdleStateConstraint": t.string().optional(),
            "chargingStateConstraint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoInstallConstraintOut"])
    types["InstallsListResponseIn"] = t.struct(
        {"install": t.array(t.proxy(renames["InstallIn"])).optional()}
    ).named(renames["InstallsListResponseIn"])
    types["InstallsListResponseOut"] = t.struct(
        {
            "install": t.array(t.proxy(renames["InstallOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstallsListResponseOut"])
    types["DeviceIn"] = t.struct(
        {
            "device": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "retailBrand": t.string().optional(),
            "maker": t.string().optional(),
            "sdkVersion": t.integer().optional(),
            "androidId": t.string().optional(),
            "report": t.proxy(renames["DeviceReportIn"]).optional(),
            "latestBuildFingerprint": t.string().optional(),
            "model": t.string().optional(),
            "product": t.string().optional(),
            "managementType": t.string().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "device": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "retailBrand": t.string().optional(),
            "maker": t.string().optional(),
            "sdkVersion": t.integer().optional(),
            "androidId": t.string().optional(),
            "report": t.proxy(renames["DeviceReportOut"]).optional(),
            "latestBuildFingerprint": t.string().optional(),
            "model": t.string().optional(),
            "product": t.string().optional(),
            "managementType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["StoreLayoutClustersListResponseIn"] = t.struct(
        {"cluster": t.array(t.proxy(renames["StoreClusterIn"])).optional()}
    ).named(renames["StoreLayoutClustersListResponseIn"])
    types["StoreLayoutClustersListResponseOut"] = t.struct(
        {
            "cluster": t.array(t.proxy(renames["StoreClusterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoreLayoutClustersListResponseOut"])

    functions = {}
    functions["managedconfigurationsfordeviceGet"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "deviceId": t.string().optional(),
                "managedConfigurationForDeviceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsfordeviceList"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "deviceId": t.string().optional(),
                "managedConfigurationForDeviceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsfordeviceUpdate"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "deviceId": t.string().optional(),
                "managedConfigurationForDeviceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsfordeviceDelete"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "deviceId": t.string().optional(),
                "managedConfigurationForDeviceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsforuserGet"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser/{managedConfigurationForUserId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "managedConfigurationForUserId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsforuserUpdate"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser/{managedConfigurationForUserId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "managedConfigurationForUserId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsforuserList"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser/{managedConfigurationForUserId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "managedConfigurationForUserId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsforuserDelete"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser/{managedConfigurationForUserId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "managedConfigurationForUserId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["permissionsGet"] = androidenterprise.get(
        "androidenterprise/v1/permissions/{permissionId}",
        t.struct(
            {
                "language": t.string().optional(),
                "permissionId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PermissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersDelete"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutClustersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersInsert"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutClustersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersUpdate"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutClustersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutClustersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutClustersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPullNotificationSet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesAcknowledgeNotificationSet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesCreateEnrollmentToken"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGetServiceAccount"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGenerateSignupUrl"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesCreateWebToken"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesCompleteSignup"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesSetAccount"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesUnenroll"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesSendTestPushNotification"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnroll"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesSetStoreLayout"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGetStoreLayout"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises",
        t.struct({"domain": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EnterprisesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGetAppRestrictionsSchema"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/unapprove",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGetPermissions"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/unapprove",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsApprove"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/unapprove",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGet"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/unapprove",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGenerateApprovalUrl"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/unapprove",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsList"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/unapprove",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsUnapprove"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/unapprove",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesInsert"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesList"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesUpdate"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesGet"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesDelete"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsDelete"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "versionCode": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "webAppId": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "isPublished": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsUpdate"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "versionCode": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "webAppId": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "isPublished": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsGet"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "versionCode": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "webAppId": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "isPublished": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsList"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "versionCode": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "webAppId": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "isPublished": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsInsert"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "versionCode": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "webAppId": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "isPublished": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grouplicensesList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/groupLicenses/{groupLicenseId}",
        t.struct(
            {
                "groupLicenseId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupLicenseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grouplicensesGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/groupLicenses/{groupLicenseId}",
        t.struct(
            {
                "groupLicenseId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupLicenseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grouplicenseusersList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/groupLicenses/{groupLicenseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "groupLicenseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupLicenseUsersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["serviceaccountkeysList"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/serviceAccountKeys",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "id": t.string().optional(),
                "data": t.string().optional(),
                "type": t.string().optional(),
                "publicData": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceAccountKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["serviceaccountkeysDelete"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/serviceAccountKeys",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "id": t.string().optional(),
                "data": t.string().optional(),
                "type": t.string().optional(),
                "publicData": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceAccountKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["serviceaccountkeysInsert"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/serviceAccountKeys",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "id": t.string().optional(),
                "data": t.string().optional(),
                "type": t.string().optional(),
                "publicData": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceAccountKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installsList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs/{installId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "userId": t.string().optional(),
                "installId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstallOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installsDelete"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs/{installId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "userId": t.string().optional(),
                "installId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstallOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installsUpdate"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs/{installId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "userId": t.string().optional(),
                "installId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstallOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installsGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs/{installId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "userId": t.string().optional(),
                "installId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstallOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersRevokeDeviceAccess"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/availableProductSet",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "productVisibility": t.array(
                    t.proxy(renames["ProductVisibilityIn"])
                ).optional(),
                "productId": t.array(t.string()).optional(),
                "productSetBehavior": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGetAvailableProductSet"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/availableProductSet",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "productVisibility": t.array(
                    t.proxy(renames["ProductVisibilityIn"])
                ).optional(),
                "productId": t.array(t.string()).optional(),
                "productSetBehavior": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/availableProductSet",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "productVisibility": t.array(
                    t.proxy(renames["ProductVisibilityIn"])
                ).optional(),
                "productId": t.array(t.string()).optional(),
                "productSetBehavior": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersUpdate"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/availableProductSet",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "productVisibility": t.array(
                    t.proxy(renames["ProductVisibilityIn"])
                ).optional(),
                "productId": t.array(t.string()).optional(),
                "productSetBehavior": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/availableProductSet",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "productVisibility": t.array(
                    t.proxy(renames["ProductVisibilityIn"])
                ).optional(),
                "productId": t.array(t.string()).optional(),
                "productSetBehavior": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGet"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/availableProductSet",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "productVisibility": t.array(
                    t.proxy(renames["ProductVisibilityIn"])
                ).optional(),
                "productId": t.array(t.string()).optional(),
                "productSetBehavior": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersInsert"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/availableProductSet",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "productVisibility": t.array(
                    t.proxy(renames["ProductVisibilityIn"])
                ).optional(),
                "productId": t.array(t.string()).optional(),
                "productSetBehavior": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGenerateAuthenticationToken"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/availableProductSet",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "productVisibility": t.array(
                    t.proxy(renames["ProductVisibilityIn"])
                ).optional(),
                "productId": t.array(t.string()).optional(),
                "productSetBehavior": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSetAvailableProductSet"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/availableProductSet",
        t.struct(
            {
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "productVisibility": t.array(
                    t.proxy(renames["ProductVisibilityIn"])
                ).optional(),
                "productId": t.array(t.string()).optional(),
                "productSetBehavior": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductSetOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationssettingsList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/managedConfigurationsSettings",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "productId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManagedConfigurationsSettingsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entitlementsGet"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "entitlementId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entitlementsUpdate"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "entitlementId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entitlementsList"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "entitlementId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entitlementsDelete"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "entitlementId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesList"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "updateMask": t.string().optional(),
                "userId": t.string().optional(),
                "device": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "retailBrand": t.string().optional(),
                "maker": t.string().optional(),
                "sdkVersion": t.integer().optional(),
                "androidId": t.string().optional(),
                "report": t.proxy(renames["DeviceReportIn"]).optional(),
                "latestBuildFingerprint": t.string().optional(),
                "model": t.string().optional(),
                "product": t.string().optional(),
                "managementType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesGetState"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "updateMask": t.string().optional(),
                "userId": t.string().optional(),
                "device": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "retailBrand": t.string().optional(),
                "maker": t.string().optional(),
                "sdkVersion": t.integer().optional(),
                "androidId": t.string().optional(),
                "report": t.proxy(renames["DeviceReportIn"]).optional(),
                "latestBuildFingerprint": t.string().optional(),
                "model": t.string().optional(),
                "product": t.string().optional(),
                "managementType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesSetState"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "updateMask": t.string().optional(),
                "userId": t.string().optional(),
                "device": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "retailBrand": t.string().optional(),
                "maker": t.string().optional(),
                "sdkVersion": t.integer().optional(),
                "androidId": t.string().optional(),
                "report": t.proxy(renames["DeviceReportIn"]).optional(),
                "latestBuildFingerprint": t.string().optional(),
                "model": t.string().optional(),
                "product": t.string().optional(),
                "managementType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesGet"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "updateMask": t.string().optional(),
                "userId": t.string().optional(),
                "device": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "retailBrand": t.string().optional(),
                "maker": t.string().optional(),
                "sdkVersion": t.integer().optional(),
                "androidId": t.string().optional(),
                "report": t.proxy(renames["DeviceReportIn"]).optional(),
                "latestBuildFingerprint": t.string().optional(),
                "model": t.string().optional(),
                "product": t.string().optional(),
                "managementType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesForceReportUpload"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "updateMask": t.string().optional(),
                "userId": t.string().optional(),
                "device": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "retailBrand": t.string().optional(),
                "maker": t.string().optional(),
                "sdkVersion": t.integer().optional(),
                "androidId": t.string().optional(),
                "report": t.proxy(renames["DeviceReportIn"]).optional(),
                "latestBuildFingerprint": t.string().optional(),
                "model": t.string().optional(),
                "product": t.string().optional(),
                "managementType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesUpdate"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}",
        t.struct(
            {
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "updateMask": t.string().optional(),
                "userId": t.string().optional(),
                "device": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "retailBrand": t.string().optional(),
                "maker": t.string().optional(),
                "sdkVersion": t.integer().optional(),
                "androidId": t.string().optional(),
                "report": t.proxy(renames["DeviceReportIn"]).optional(),
                "latestBuildFingerprint": t.string().optional(),
                "model": t.string().optional(),
                "product": t.string().optional(),
                "managementType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="androidenterprise",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
