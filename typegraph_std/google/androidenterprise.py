from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_androidenterprise():
    androidenterprise = HTTPRuntime("https://androidenterprise.googleapis.com/")

    renames = {
        "ErrorResponse": "_androidenterprise_1_ErrorResponse",
        "EnterprisesListResponseIn": "_androidenterprise_2_EnterprisesListResponseIn",
        "EnterprisesListResponseOut": "_androidenterprise_3_EnterprisesListResponseOut",
        "AdministratorWebTokenSpecManagedConfigurationsIn": "_androidenterprise_4_AdministratorWebTokenSpecManagedConfigurationsIn",
        "AdministratorWebTokenSpecManagedConfigurationsOut": "_androidenterprise_5_AdministratorWebTokenSpecManagedConfigurationsOut",
        "AdministratorWebTokenSpecPlaySearchIn": "_androidenterprise_6_AdministratorWebTokenSpecPlaySearchIn",
        "AdministratorWebTokenSpecPlaySearchOut": "_androidenterprise_7_AdministratorWebTokenSpecPlaySearchOut",
        "AuthenticationTokenIn": "_androidenterprise_8_AuthenticationTokenIn",
        "AuthenticationTokenOut": "_androidenterprise_9_AuthenticationTokenOut",
        "EntitlementsListResponseIn": "_androidenterprise_10_EntitlementsListResponseIn",
        "EntitlementsListResponseOut": "_androidenterprise_11_EntitlementsListResponseOut",
        "ApprovalUrlInfoIn": "_androidenterprise_12_ApprovalUrlInfoIn",
        "ApprovalUrlInfoOut": "_androidenterprise_13_ApprovalUrlInfoOut",
        "AdministratorIn": "_androidenterprise_14_AdministratorIn",
        "AdministratorOut": "_androidenterprise_15_AdministratorOut",
        "EntitlementIn": "_androidenterprise_16_EntitlementIn",
        "EntitlementOut": "_androidenterprise_17_EntitlementOut",
        "NotificationSetIn": "_androidenterprise_18_NotificationSetIn",
        "NotificationSetOut": "_androidenterprise_19_NotificationSetOut",
        "ProductIn": "_androidenterprise_20_ProductIn",
        "ProductOut": "_androidenterprise_21_ProductOut",
        "ManagedPropertyBundleIn": "_androidenterprise_22_ManagedPropertyBundleIn",
        "ManagedPropertyBundleOut": "_androidenterprise_23_ManagedPropertyBundleOut",
        "DeviceReportUpdateEventIn": "_androidenterprise_24_DeviceReportUpdateEventIn",
        "DeviceReportUpdateEventOut": "_androidenterprise_25_DeviceReportUpdateEventOut",
        "ProductPermissionsIn": "_androidenterprise_26_ProductPermissionsIn",
        "ProductPermissionsOut": "_androidenterprise_27_ProductPermissionsOut",
        "WebAppIconIn": "_androidenterprise_28_WebAppIconIn",
        "WebAppIconOut": "_androidenterprise_29_WebAppIconOut",
        "AppRestrictionsSchemaIn": "_androidenterprise_30_AppRestrictionsSchemaIn",
        "AppRestrictionsSchemaOut": "_androidenterprise_31_AppRestrictionsSchemaOut",
        "ProductsListResponseIn": "_androidenterprise_32_ProductsListResponseIn",
        "ProductsListResponseOut": "_androidenterprise_33_ProductsListResponseOut",
        "UserIn": "_androidenterprise_34_UserIn",
        "UserOut": "_androidenterprise_35_UserOut",
        "StoreLayoutPagesListResponseIn": "_androidenterprise_36_StoreLayoutPagesListResponseIn",
        "StoreLayoutPagesListResponseOut": "_androidenterprise_37_StoreLayoutPagesListResponseOut",
        "ProductApprovalEventIn": "_androidenterprise_38_ProductApprovalEventIn",
        "ProductApprovalEventOut": "_androidenterprise_39_ProductApprovalEventOut",
        "CreateEnrollmentTokenResponseIn": "_androidenterprise_40_CreateEnrollmentTokenResponseIn",
        "CreateEnrollmentTokenResponseOut": "_androidenterprise_41_CreateEnrollmentTokenResponseOut",
        "ProductVisibilityIn": "_androidenterprise_42_ProductVisibilityIn",
        "ProductVisibilityOut": "_androidenterprise_43_ProductVisibilityOut",
        "AdministratorWebTokenSpecZeroTouchIn": "_androidenterprise_44_AdministratorWebTokenSpecZeroTouchIn",
        "AdministratorWebTokenSpecZeroTouchOut": "_androidenterprise_45_AdministratorWebTokenSpecZeroTouchOut",
        "StoreClusterIn": "_androidenterprise_46_StoreClusterIn",
        "StoreClusterOut": "_androidenterprise_47_StoreClusterOut",
        "StoreLayoutIn": "_androidenterprise_48_StoreLayoutIn",
        "StoreLayoutOut": "_androidenterprise_49_StoreLayoutOut",
        "AutoInstallConstraintIn": "_androidenterprise_50_AutoInstallConstraintIn",
        "AutoInstallConstraintOut": "_androidenterprise_51_AutoInstallConstraintOut",
        "StoreLayoutClustersListResponseIn": "_androidenterprise_52_StoreLayoutClustersListResponseIn",
        "StoreLayoutClustersListResponseOut": "_androidenterprise_53_StoreLayoutClustersListResponseOut",
        "NotificationIn": "_androidenterprise_54_NotificationIn",
        "NotificationOut": "_androidenterprise_55_NotificationOut",
        "ServiceAccountKeyIn": "_androidenterprise_56_ServiceAccountKeyIn",
        "ServiceAccountKeyOut": "_androidenterprise_57_ServiceAccountKeyOut",
        "TrackInfoIn": "_androidenterprise_58_TrackInfoIn",
        "TrackInfoOut": "_androidenterprise_59_TrackInfoOut",
        "PolicyIn": "_androidenterprise_60_PolicyIn",
        "PolicyOut": "_androidenterprise_61_PolicyOut",
        "EnterpriseAuthenticationAppLinkConfigIn": "_androidenterprise_62_EnterpriseAuthenticationAppLinkConfigIn",
        "EnterpriseAuthenticationAppLinkConfigOut": "_androidenterprise_63_EnterpriseAuthenticationAppLinkConfigOut",
        "DeviceStateIn": "_androidenterprise_64_DeviceStateIn",
        "DeviceStateOut": "_androidenterprise_65_DeviceStateOut",
        "StorePageIn": "_androidenterprise_66_StorePageIn",
        "StorePageOut": "_androidenterprise_67_StorePageOut",
        "AdministratorWebTokenIn": "_androidenterprise_68_AdministratorWebTokenIn",
        "AdministratorWebTokenOut": "_androidenterprise_69_AdministratorWebTokenOut",
        "WebAppIn": "_androidenterprise_70_WebAppIn",
        "WebAppOut": "_androidenterprise_71_WebAppOut",
        "UsersListResponseIn": "_androidenterprise_72_UsersListResponseIn",
        "UsersListResponseOut": "_androidenterprise_73_UsersListResponseOut",
        "ServiceAccountKeysListResponseIn": "_androidenterprise_74_ServiceAccountKeysListResponseIn",
        "ServiceAccountKeysListResponseOut": "_androidenterprise_75_ServiceAccountKeysListResponseOut",
        "ManagedConfigurationsSettingsListResponseIn": "_androidenterprise_76_ManagedConfigurationsSettingsListResponseIn",
        "ManagedConfigurationsSettingsListResponseOut": "_androidenterprise_77_ManagedConfigurationsSettingsListResponseOut",
        "ManagedConfigurationsForDeviceListResponseIn": "_androidenterprise_78_ManagedConfigurationsForDeviceListResponseIn",
        "ManagedConfigurationsForDeviceListResponseOut": "_androidenterprise_79_ManagedConfigurationsForDeviceListResponseOut",
        "ProductSigningCertificateIn": "_androidenterprise_80_ProductSigningCertificateIn",
        "ProductSigningCertificateOut": "_androidenterprise_81_ProductSigningCertificateOut",
        "NewPermissionsEventIn": "_androidenterprise_82_NewPermissionsEventIn",
        "NewPermissionsEventOut": "_androidenterprise_83_NewPermissionsEventOut",
        "GroupLicensesListResponseIn": "_androidenterprise_84_GroupLicensesListResponseIn",
        "GroupLicensesListResponseOut": "_androidenterprise_85_GroupLicensesListResponseOut",
        "KeyedAppStateIn": "_androidenterprise_86_KeyedAppStateIn",
        "KeyedAppStateOut": "_androidenterprise_87_KeyedAppStateOut",
        "AdministratorWebTokenSpecIn": "_androidenterprise_88_AdministratorWebTokenSpecIn",
        "AdministratorWebTokenSpecOut": "_androidenterprise_89_AdministratorWebTokenSpecOut",
        "ProductAvailabilityChangeEventIn": "_androidenterprise_90_ProductAvailabilityChangeEventIn",
        "ProductAvailabilityChangeEventOut": "_androidenterprise_91_ProductAvailabilityChangeEventOut",
        "AppRestrictionsSchemaRestrictionIn": "_androidenterprise_92_AppRestrictionsSchemaRestrictionIn",
        "AppRestrictionsSchemaRestrictionOut": "_androidenterprise_93_AppRestrictionsSchemaRestrictionOut",
        "AppRestrictionsSchemaChangeEventIn": "_androidenterprise_94_AppRestrictionsSchemaChangeEventIn",
        "AppRestrictionsSchemaChangeEventOut": "_androidenterprise_95_AppRestrictionsSchemaChangeEventOut",
        "AppRestrictionsSchemaRestrictionRestrictionValueIn": "_androidenterprise_96_AppRestrictionsSchemaRestrictionRestrictionValueIn",
        "AppRestrictionsSchemaRestrictionRestrictionValueOut": "_androidenterprise_97_AppRestrictionsSchemaRestrictionRestrictionValueOut",
        "SignupInfoIn": "_androidenterprise_98_SignupInfoIn",
        "SignupInfoOut": "_androidenterprise_99_SignupInfoOut",
        "WebAppsListResponseIn": "_androidenterprise_100_WebAppsListResponseIn",
        "WebAppsListResponseOut": "_androidenterprise_101_WebAppsListResponseOut",
        "EnterprisesSendTestPushNotificationResponseIn": "_androidenterprise_102_EnterprisesSendTestPushNotificationResponseIn",
        "EnterprisesSendTestPushNotificationResponseOut": "_androidenterprise_103_EnterprisesSendTestPushNotificationResponseOut",
        "ConfigurationVariablesIn": "_androidenterprise_104_ConfigurationVariablesIn",
        "ConfigurationVariablesOut": "_androidenterprise_105_ConfigurationVariablesOut",
        "GoogleAuthenticationSettingsIn": "_androidenterprise_106_GoogleAuthenticationSettingsIn",
        "GoogleAuthenticationSettingsOut": "_androidenterprise_107_GoogleAuthenticationSettingsOut",
        "AdministratorWebTokenSpecPrivateAppsIn": "_androidenterprise_108_AdministratorWebTokenSpecPrivateAppsIn",
        "AdministratorWebTokenSpecPrivateAppsOut": "_androidenterprise_109_AdministratorWebTokenSpecPrivateAppsOut",
        "LocalizedTextIn": "_androidenterprise_110_LocalizedTextIn",
        "LocalizedTextOut": "_androidenterprise_111_LocalizedTextOut",
        "InstallsListResponseIn": "_androidenterprise_112_InstallsListResponseIn",
        "InstallsListResponseOut": "_androidenterprise_113_InstallsListResponseOut",
        "DeviceReportIn": "_androidenterprise_114_DeviceReportIn",
        "DeviceReportOut": "_androidenterprise_115_DeviceReportOut",
        "ManagedConfigurationsSettingsIn": "_androidenterprise_116_ManagedConfigurationsSettingsIn",
        "ManagedConfigurationsSettingsOut": "_androidenterprise_117_ManagedConfigurationsSettingsOut",
        "VariableSetIn": "_androidenterprise_118_VariableSetIn",
        "VariableSetOut": "_androidenterprise_119_VariableSetOut",
        "GroupLicenseUsersListResponseIn": "_androidenterprise_120_GroupLicenseUsersListResponseIn",
        "GroupLicenseUsersListResponseOut": "_androidenterprise_121_GroupLicenseUsersListResponseOut",
        "ManagedPropertyIn": "_androidenterprise_122_ManagedPropertyIn",
        "ManagedPropertyOut": "_androidenterprise_123_ManagedPropertyOut",
        "EnterpriseIn": "_androidenterprise_124_EnterpriseIn",
        "EnterpriseOut": "_androidenterprise_125_EnterpriseOut",
        "ManagedConfigurationsForUserListResponseIn": "_androidenterprise_126_ManagedConfigurationsForUserListResponseIn",
        "ManagedConfigurationsForUserListResponseOut": "_androidenterprise_127_ManagedConfigurationsForUserListResponseOut",
        "ProductsApproveRequestIn": "_androidenterprise_128_ProductsApproveRequestIn",
        "ProductsApproveRequestOut": "_androidenterprise_129_ProductsApproveRequestOut",
        "AdministratorWebTokenSpecStoreBuilderIn": "_androidenterprise_130_AdministratorWebTokenSpecStoreBuilderIn",
        "AdministratorWebTokenSpecStoreBuilderOut": "_androidenterprise_131_AdministratorWebTokenSpecStoreBuilderOut",
        "PageInfoIn": "_androidenterprise_132_PageInfoIn",
        "PageInfoOut": "_androidenterprise_133_PageInfoOut",
        "DeviceIn": "_androidenterprise_134_DeviceIn",
        "DeviceOut": "_androidenterprise_135_DeviceOut",
        "ManagedConfigurationIn": "_androidenterprise_136_ManagedConfigurationIn",
        "ManagedConfigurationOut": "_androidenterprise_137_ManagedConfigurationOut",
        "AutoInstallPolicyIn": "_androidenterprise_138_AutoInstallPolicyIn",
        "AutoInstallPolicyOut": "_androidenterprise_139_AutoInstallPolicyOut",
        "TokenPaginationIn": "_androidenterprise_140_TokenPaginationIn",
        "TokenPaginationOut": "_androidenterprise_141_TokenPaginationOut",
        "NewDeviceEventIn": "_androidenterprise_142_NewDeviceEventIn",
        "NewDeviceEventOut": "_androidenterprise_143_NewDeviceEventOut",
        "AppStateIn": "_androidenterprise_144_AppStateIn",
        "AppStateOut": "_androidenterprise_145_AppStateOut",
        "ProductPolicyIn": "_androidenterprise_146_ProductPolicyIn",
        "ProductPolicyOut": "_androidenterprise_147_ProductPolicyOut",
        "DevicesListResponseIn": "_androidenterprise_148_DevicesListResponseIn",
        "DevicesListResponseOut": "_androidenterprise_149_DevicesListResponseOut",
        "GroupLicenseIn": "_androidenterprise_150_GroupLicenseIn",
        "GroupLicenseOut": "_androidenterprise_151_GroupLicenseOut",
        "MaintenanceWindowIn": "_androidenterprise_152_MaintenanceWindowIn",
        "MaintenanceWindowOut": "_androidenterprise_153_MaintenanceWindowOut",
        "PermissionIn": "_androidenterprise_154_PermissionIn",
        "PermissionOut": "_androidenterprise_155_PermissionOut",
        "ServiceAccountIn": "_androidenterprise_156_ServiceAccountIn",
        "ServiceAccountOut": "_androidenterprise_157_ServiceAccountOut",
        "InstallIn": "_androidenterprise_158_InstallIn",
        "InstallOut": "_androidenterprise_159_InstallOut",
        "ProductsGenerateApprovalUrlResponseIn": "_androidenterprise_160_ProductsGenerateApprovalUrlResponseIn",
        "ProductsGenerateApprovalUrlResponseOut": "_androidenterprise_161_ProductsGenerateApprovalUrlResponseOut",
        "ProductSetIn": "_androidenterprise_162_ProductSetIn",
        "ProductSetOut": "_androidenterprise_163_ProductSetOut",
        "EnterpriseAccountIn": "_androidenterprise_164_EnterpriseAccountIn",
        "EnterpriseAccountOut": "_androidenterprise_165_EnterpriseAccountOut",
        "ProductPermissionIn": "_androidenterprise_166_ProductPermissionIn",
        "ProductPermissionOut": "_androidenterprise_167_ProductPermissionOut",
        "AppVersionIn": "_androidenterprise_168_AppVersionIn",
        "AppVersionOut": "_androidenterprise_169_AppVersionOut",
        "AppUpdateEventIn": "_androidenterprise_170_AppUpdateEventIn",
        "AppUpdateEventOut": "_androidenterprise_171_AppUpdateEventOut",
        "InstallFailureEventIn": "_androidenterprise_172_InstallFailureEventIn",
        "InstallFailureEventOut": "_androidenterprise_173_InstallFailureEventOut",
        "AdministratorWebTokenSpecWebAppsIn": "_androidenterprise_174_AdministratorWebTokenSpecWebAppsIn",
        "AdministratorWebTokenSpecWebAppsOut": "_androidenterprise_175_AdministratorWebTokenSpecWebAppsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EnterprisesListResponseIn"] = t.struct(
        {"enterprise": t.array(t.proxy(renames["EnterpriseIn"])).optional()}
    ).named(renames["EnterprisesListResponseIn"])
    types["EnterprisesListResponseOut"] = t.struct(
        {
            "enterprise": t.array(t.proxy(renames["EnterpriseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterprisesListResponseOut"])
    types["AdministratorWebTokenSpecManagedConfigurationsIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecManagedConfigurationsIn"])
    types["AdministratorWebTokenSpecManagedConfigurationsOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecManagedConfigurationsOut"])
    types["AdministratorWebTokenSpecPlaySearchIn"] = t.struct(
        {"enabled": t.boolean().optional(), "approveApps": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecPlaySearchIn"])
    types["AdministratorWebTokenSpecPlaySearchOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "approveApps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecPlaySearchOut"])
    types["AuthenticationTokenIn"] = t.struct({"token": t.string().optional()}).named(
        renames["AuthenticationTokenIn"]
    )
    types["AuthenticationTokenOut"] = t.struct(
        {
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationTokenOut"])
    types["EntitlementsListResponseIn"] = t.struct(
        {"entitlement": t.array(t.proxy(renames["EntitlementIn"])).optional()}
    ).named(renames["EntitlementsListResponseIn"])
    types["EntitlementsListResponseOut"] = t.struct(
        {
            "entitlement": t.array(t.proxy(renames["EntitlementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntitlementsListResponseOut"])
    types["ApprovalUrlInfoIn"] = t.struct({"approvalUrl": t.string().optional()}).named(
        renames["ApprovalUrlInfoIn"]
    )
    types["ApprovalUrlInfoOut"] = t.struct(
        {
            "approvalUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApprovalUrlInfoOut"])
    types["AdministratorIn"] = t.struct({"email": t.string().optional()}).named(
        renames["AdministratorIn"]
    )
    types["AdministratorOut"] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorOut"])
    types["EntitlementIn"] = t.struct(
        {"productId": t.string().optional(), "reason": t.string().optional()}
    ).named(renames["EntitlementIn"])
    types["EntitlementOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntitlementOut"])
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
    types["ProductIn"] = t.struct(
        {
            "smallIconUrl": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "availableTracks": t.array(t.string()).optional(),
            "contentRating": t.string().optional(),
            "requiresContainerApp": t.boolean().optional(),
            "detailsUrl": t.string().optional(),
            "workDetailsUrl": t.string().optional(),
            "category": t.string().optional(),
            "availableCountries": t.array(t.string()).optional(),
            "productId": t.string().optional(),
            "iconUrl": t.string().optional(),
            "authorName": t.string().optional(),
            "signingCertificate": t.proxy(
                renames["ProductSigningCertificateIn"]
            ).optional(),
            "distributionChannel": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "appVersion": t.array(t.proxy(renames["AppVersionIn"])).optional(),
            "appRestrictionsSchema": t.proxy(
                renames["AppRestrictionsSchemaIn"]
            ).optional(),
            "appTracks": t.array(t.proxy(renames["TrackInfoIn"])).optional(),
            "lastUpdatedTimestampMillis": t.string().optional(),
            "fullDescription": t.string().optional(),
            "recentChanges": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "permissions": t.array(t.proxy(renames["ProductPermissionIn"])).optional(),
            "productPricing": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
        }
    ).named(renames["ProductIn"])
    types["ProductOut"] = t.struct(
        {
            "smallIconUrl": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "availableTracks": t.array(t.string()).optional(),
            "contentRating": t.string().optional(),
            "requiresContainerApp": t.boolean().optional(),
            "detailsUrl": t.string().optional(),
            "workDetailsUrl": t.string().optional(),
            "category": t.string().optional(),
            "availableCountries": t.array(t.string()).optional(),
            "productId": t.string().optional(),
            "iconUrl": t.string().optional(),
            "authorName": t.string().optional(),
            "signingCertificate": t.proxy(
                renames["ProductSigningCertificateOut"]
            ).optional(),
            "distributionChannel": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "appVersion": t.array(t.proxy(renames["AppVersionOut"])).optional(),
            "appRestrictionsSchema": t.proxy(
                renames["AppRestrictionsSchemaOut"]
            ).optional(),
            "appTracks": t.array(t.proxy(renames["TrackInfoOut"])).optional(),
            "lastUpdatedTimestampMillis": t.string().optional(),
            "fullDescription": t.string().optional(),
            "recentChanges": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "permissions": t.array(t.proxy(renames["ProductPermissionOut"])).optional(),
            "productPricing": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductOut"])
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
    types["DeviceReportUpdateEventIn"] = t.struct(
        {
            "userId": t.string().optional(),
            "deviceId": t.string().optional(),
            "report": t.proxy(renames["DeviceReportIn"]).optional(),
        }
    ).named(renames["DeviceReportUpdateEventIn"])
    types["DeviceReportUpdateEventOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "deviceId": t.string().optional(),
            "report": t.proxy(renames["DeviceReportOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceReportUpdateEventOut"])
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
    types["WebAppIconIn"] = t.struct({"imageData": t.string().optional()}).named(
        renames["WebAppIconIn"]
    )
    types["WebAppIconOut"] = t.struct(
        {
            "imageData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppIconOut"])
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
    types["ProductsListResponseIn"] = t.struct(
        {
            "product": t.array(t.proxy(renames["ProductIn"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoIn"]).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationIn"]).optional(),
        }
    ).named(renames["ProductsListResponseIn"])
    types["ProductsListResponseOut"] = t.struct(
        {
            "product": t.array(t.proxy(renames["ProductOut"])).optional(),
            "pageInfo": t.proxy(renames["PageInfoOut"]).optional(),
            "tokenPagination": t.proxy(renames["TokenPaginationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsListResponseOut"])
    types["UserIn"] = t.struct(
        {
            "managementType": t.string().optional(),
            "primaryEmail": t.string().optional(),
            "accountIdentifier": t.string().optional(),
            "accountType": t.string().optional(),
            "displayName": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["UserIn"])
    types["UserOut"] = t.struct(
        {
            "managementType": t.string().optional(),
            "primaryEmail": t.string().optional(),
            "accountIdentifier": t.string().optional(),
            "accountType": t.string().optional(),
            "displayName": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["StoreLayoutPagesListResponseIn"] = t.struct(
        {"page": t.array(t.proxy(renames["StorePageIn"])).optional()}
    ).named(renames["StoreLayoutPagesListResponseIn"])
    types["StoreLayoutPagesListResponseOut"] = t.struct(
        {
            "page": t.array(t.proxy(renames["StorePageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoreLayoutPagesListResponseOut"])
    types["ProductApprovalEventIn"] = t.struct(
        {"approved": t.string().optional(), "productId": t.string().optional()}
    ).named(renames["ProductApprovalEventIn"])
    types["ProductApprovalEventOut"] = t.struct(
        {
            "approved": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductApprovalEventOut"])
    types["CreateEnrollmentTokenResponseIn"] = t.struct(
        {"enrollmentToken": t.string().optional()}
    ).named(renames["CreateEnrollmentTokenResponseIn"])
    types["CreateEnrollmentTokenResponseOut"] = t.struct(
        {
            "enrollmentToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateEnrollmentTokenResponseOut"])
    types["ProductVisibilityIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "trackIds": t.array(t.string()).optional(),
            "tracks": t.array(t.string()).optional(),
        }
    ).named(renames["ProductVisibilityIn"])
    types["ProductVisibilityOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "trackIds": t.array(t.string()).optional(),
            "tracks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductVisibilityOut"])
    types["AdministratorWebTokenSpecZeroTouchIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecZeroTouchIn"])
    types["AdministratorWebTokenSpecZeroTouchOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecZeroTouchOut"])
    types["StoreClusterIn"] = t.struct(
        {
            "productId": t.array(t.string()).optional(),
            "name": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
            "orderInPage": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["StoreClusterIn"])
    types["StoreClusterOut"] = t.struct(
        {
            "productId": t.array(t.string()).optional(),
            "name": t.array(t.proxy(renames["LocalizedTextOut"])).optional(),
            "orderInPage": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoreClusterOut"])
    types["StoreLayoutIn"] = t.struct(
        {"storeLayoutType": t.string().optional(), "homepageId": t.string().optional()}
    ).named(renames["StoreLayoutIn"])
    types["StoreLayoutOut"] = t.struct(
        {
            "storeLayoutType": t.string().optional(),
            "homepageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoreLayoutOut"])
    types["AutoInstallConstraintIn"] = t.struct(
        {
            "deviceIdleStateConstraint": t.string().optional(),
            "networkTypeConstraint": t.string().optional(),
            "chargingStateConstraint": t.string().optional(),
        }
    ).named(renames["AutoInstallConstraintIn"])
    types["AutoInstallConstraintOut"] = t.struct(
        {
            "deviceIdleStateConstraint": t.string().optional(),
            "networkTypeConstraint": t.string().optional(),
            "chargingStateConstraint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoInstallConstraintOut"])
    types["StoreLayoutClustersListResponseIn"] = t.struct(
        {"cluster": t.array(t.proxy(renames["StoreClusterIn"])).optional()}
    ).named(renames["StoreLayoutClustersListResponseIn"])
    types["StoreLayoutClustersListResponseOut"] = t.struct(
        {
            "cluster": t.array(t.proxy(renames["StoreClusterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StoreLayoutClustersListResponseOut"])
    types["NotificationIn"] = t.struct(
        {
            "installFailureEvent": t.proxy(renames["InstallFailureEventIn"]).optional(),
            "productApprovalEvent": t.proxy(
                renames["ProductApprovalEventIn"]
            ).optional(),
            "deviceReportUpdateEvent": t.proxy(
                renames["DeviceReportUpdateEventIn"]
            ).optional(),
            "appRestrictionsSchemaChangeEvent": t.proxy(
                renames["AppRestrictionsSchemaChangeEventIn"]
            ).optional(),
            "notificationType": t.string().optional(),
            "timestampMillis": t.string().optional(),
            "appUpdateEvent": t.proxy(renames["AppUpdateEventIn"]).optional(),
            "newDeviceEvent": t.proxy(renames["NewDeviceEventIn"]).optional(),
            "newPermissionsEvent": t.proxy(renames["NewPermissionsEventIn"]).optional(),
            "productAvailabilityChangeEvent": t.proxy(
                renames["ProductAvailabilityChangeEventIn"]
            ).optional(),
            "enterpriseId": t.string().optional(),
        }
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "installFailureEvent": t.proxy(
                renames["InstallFailureEventOut"]
            ).optional(),
            "productApprovalEvent": t.proxy(
                renames["ProductApprovalEventOut"]
            ).optional(),
            "deviceReportUpdateEvent": t.proxy(
                renames["DeviceReportUpdateEventOut"]
            ).optional(),
            "appRestrictionsSchemaChangeEvent": t.proxy(
                renames["AppRestrictionsSchemaChangeEventOut"]
            ).optional(),
            "notificationType": t.string().optional(),
            "timestampMillis": t.string().optional(),
            "appUpdateEvent": t.proxy(renames["AppUpdateEventOut"]).optional(),
            "newDeviceEvent": t.proxy(renames["NewDeviceEventOut"]).optional(),
            "newPermissionsEvent": t.proxy(
                renames["NewPermissionsEventOut"]
            ).optional(),
            "productAvailabilityChangeEvent": t.proxy(
                renames["ProductAvailabilityChangeEventOut"]
            ).optional(),
            "enterpriseId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["ServiceAccountKeyIn"] = t.struct(
        {
            "type": t.string().optional(),
            "data": t.string().optional(),
            "id": t.string().optional(),
            "publicData": t.string().optional(),
        }
    ).named(renames["ServiceAccountKeyIn"])
    types["ServiceAccountKeyOut"] = t.struct(
        {
            "type": t.string().optional(),
            "data": t.string().optional(),
            "id": t.string().optional(),
            "publicData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountKeyOut"])
    types["TrackInfoIn"] = t.struct(
        {"trackAlias": t.string().optional(), "trackId": t.string().optional()}
    ).named(renames["TrackInfoIn"])
    types["TrackInfoOut"] = t.struct(
        {
            "trackAlias": t.string().optional(),
            "trackId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrackInfoOut"])
    types["PolicyIn"] = t.struct(
        {
            "deviceReportPolicy": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowIn"]).optional(),
            "productPolicy": t.array(t.proxy(renames["ProductPolicyIn"])).optional(),
            "autoUpdatePolicy": t.string().optional(),
            "productAvailabilityPolicy": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "deviceReportPolicy": t.string().optional(),
            "maintenanceWindow": t.proxy(renames["MaintenanceWindowOut"]).optional(),
            "productPolicy": t.array(t.proxy(renames["ProductPolicyOut"])).optional(),
            "autoUpdatePolicy": t.string().optional(),
            "productAvailabilityPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["EnterpriseAuthenticationAppLinkConfigIn"] = t.struct(
        {"uri": t.string().optional()}
    ).named(renames["EnterpriseAuthenticationAppLinkConfigIn"])
    types["EnterpriseAuthenticationAppLinkConfigOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseAuthenticationAppLinkConfigOut"])
    types["DeviceStateIn"] = t.struct({"accountState": t.string().optional()}).named(
        renames["DeviceStateIn"]
    )
    types["DeviceStateOut"] = t.struct(
        {
            "accountState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceStateOut"])
    types["StorePageIn"] = t.struct(
        {
            "name": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
            "id": t.string().optional(),
            "link": t.array(t.string()).optional(),
        }
    ).named(renames["StorePageIn"])
    types["StorePageOut"] = t.struct(
        {
            "name": t.array(t.proxy(renames["LocalizedTextOut"])).optional(),
            "id": t.string().optional(),
            "link": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StorePageOut"])
    types["AdministratorWebTokenIn"] = t.struct({"token": t.string().optional()}).named(
        renames["AdministratorWebTokenIn"]
    )
    types["AdministratorWebTokenOut"] = t.struct(
        {
            "token": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenOut"])
    types["WebAppIn"] = t.struct(
        {
            "title": t.string().optional(),
            "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
            "versionCode": t.string().optional(),
            "webAppId": t.string().optional(),
            "displayMode": t.string().optional(),
            "startUrl": t.string().optional(),
            "isPublished": t.boolean().optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "title": t.string().optional(),
            "icons": t.array(t.proxy(renames["WebAppIconOut"])).optional(),
            "versionCode": t.string().optional(),
            "webAppId": t.string().optional(),
            "displayMode": t.string().optional(),
            "startUrl": t.string().optional(),
            "isPublished": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
    types["UsersListResponseIn"] = t.struct(
        {"user": t.array(t.proxy(renames["UserIn"])).optional()}
    ).named(renames["UsersListResponseIn"])
    types["UsersListResponseOut"] = t.struct(
        {
            "user": t.array(t.proxy(renames["UserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsersListResponseOut"])
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
    types["ProductSigningCertificateIn"] = t.struct(
        {
            "certificateHashSha1": t.string().optional(),
            "certificateHashSha256": t.string().optional(),
        }
    ).named(renames["ProductSigningCertificateIn"])
    types["ProductSigningCertificateOut"] = t.struct(
        {
            "certificateHashSha1": t.string().optional(),
            "certificateHashSha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductSigningCertificateOut"])
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
    types["GroupLicensesListResponseIn"] = t.struct(
        {"groupLicense": t.array(t.proxy(renames["GroupLicenseIn"])).optional()}
    ).named(renames["GroupLicensesListResponseIn"])
    types["GroupLicensesListResponseOut"] = t.struct(
        {
            "groupLicense": t.array(t.proxy(renames["GroupLicenseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupLicensesListResponseOut"])
    types["KeyedAppStateIn"] = t.struct(
        {
            "message": t.string().optional(),
            "key": t.string().optional(),
            "data": t.string().optional(),
            "severity": t.string().optional(),
            "stateTimestampMillis": t.string().optional(),
        }
    ).named(renames["KeyedAppStateIn"])
    types["KeyedAppStateOut"] = t.struct(
        {
            "message": t.string().optional(),
            "key": t.string().optional(),
            "data": t.string().optional(),
            "severity": t.string().optional(),
            "stateTimestampMillis": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyedAppStateOut"])
    types["AdministratorWebTokenSpecIn"] = t.struct(
        {
            "webApps": t.proxy(
                renames["AdministratorWebTokenSpecWebAppsIn"]
            ).optional(),
            "permission": t.array(t.string()).optional(),
            "storeBuilder": t.proxy(
                renames["AdministratorWebTokenSpecStoreBuilderIn"]
            ).optional(),
            "playSearch": t.proxy(
                renames["AdministratorWebTokenSpecPlaySearchIn"]
            ).optional(),
            "zeroTouch": t.proxy(
                renames["AdministratorWebTokenSpecZeroTouchIn"]
            ).optional(),
            "managedConfigurations": t.proxy(
                renames["AdministratorWebTokenSpecManagedConfigurationsIn"]
            ).optional(),
            "parent": t.string().optional(),
            "privateApps": t.proxy(
                renames["AdministratorWebTokenSpecPrivateAppsIn"]
            ).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecIn"])
    types["AdministratorWebTokenSpecOut"] = t.struct(
        {
            "webApps": t.proxy(
                renames["AdministratorWebTokenSpecWebAppsOut"]
            ).optional(),
            "permission": t.array(t.string()).optional(),
            "storeBuilder": t.proxy(
                renames["AdministratorWebTokenSpecStoreBuilderOut"]
            ).optional(),
            "playSearch": t.proxy(
                renames["AdministratorWebTokenSpecPlaySearchOut"]
            ).optional(),
            "zeroTouch": t.proxy(
                renames["AdministratorWebTokenSpecZeroTouchOut"]
            ).optional(),
            "managedConfigurations": t.proxy(
                renames["AdministratorWebTokenSpecManagedConfigurationsOut"]
            ).optional(),
            "parent": t.string().optional(),
            "privateApps": t.proxy(
                renames["AdministratorWebTokenSpecPrivateAppsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecOut"])
    types["ProductAvailabilityChangeEventIn"] = t.struct(
        {
            "availabilityStatus": t.string().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["ProductAvailabilityChangeEventIn"])
    types["ProductAvailabilityChangeEventOut"] = t.struct(
        {
            "availabilityStatus": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductAvailabilityChangeEventOut"])
    types["AppRestrictionsSchemaRestrictionIn"] = t.struct(
        {
            "key": t.string().optional(),
            "entryValue": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "defaultValue": t.proxy(
                renames["AppRestrictionsSchemaRestrictionRestrictionValueIn"]
            ).optional(),
            "restrictionType": t.string().optional(),
            "nestedRestriction": t.array(
                t.proxy(renames["AppRestrictionsSchemaRestrictionIn"])
            ).optional(),
            "title": t.string().optional(),
            "entry": t.array(t.string()).optional(),
        }
    ).named(renames["AppRestrictionsSchemaRestrictionIn"])
    types["AppRestrictionsSchemaRestrictionOut"] = t.struct(
        {
            "key": t.string().optional(),
            "entryValue": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "defaultValue": t.proxy(
                renames["AppRestrictionsSchemaRestrictionRestrictionValueOut"]
            ).optional(),
            "restrictionType": t.string().optional(),
            "nestedRestriction": t.array(
                t.proxy(renames["AppRestrictionsSchemaRestrictionOut"])
            ).optional(),
            "title": t.string().optional(),
            "entry": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppRestrictionsSchemaRestrictionOut"])
    types["AppRestrictionsSchemaChangeEventIn"] = t.struct(
        {"productId": t.string().optional()}
    ).named(renames["AppRestrictionsSchemaChangeEventIn"])
    types["AppRestrictionsSchemaChangeEventOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppRestrictionsSchemaChangeEventOut"])
    types["AppRestrictionsSchemaRestrictionRestrictionValueIn"] = t.struct(
        {
            "valueBool": t.boolean().optional(),
            "valueString": t.string().optional(),
            "valueMultiselect": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "valueInteger": t.integer().optional(),
        }
    ).named(renames["AppRestrictionsSchemaRestrictionRestrictionValueIn"])
    types["AppRestrictionsSchemaRestrictionRestrictionValueOut"] = t.struct(
        {
            "valueBool": t.boolean().optional(),
            "valueString": t.string().optional(),
            "valueMultiselect": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "valueInteger": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppRestrictionsSchemaRestrictionRestrictionValueOut"])
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
    types["WebAppsListResponseIn"] = t.struct(
        {"webApp": t.array(t.proxy(renames["WebAppIn"])).optional()}
    ).named(renames["WebAppsListResponseIn"])
    types["WebAppsListResponseOut"] = t.struct(
        {
            "webApp": t.array(t.proxy(renames["WebAppOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppsListResponseOut"])
    types["EnterprisesSendTestPushNotificationResponseIn"] = t.struct(
        {"topicName": t.string().optional(), "messageId": t.string().optional()}
    ).named(renames["EnterprisesSendTestPushNotificationResponseIn"])
    types["EnterprisesSendTestPushNotificationResponseOut"] = t.struct(
        {
            "topicName": t.string().optional(),
            "messageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterprisesSendTestPushNotificationResponseOut"])
    types["ConfigurationVariablesIn"] = t.struct(
        {
            "variableSet": t.array(t.proxy(renames["VariableSetIn"])).optional(),
            "mcmId": t.string().optional(),
        }
    ).named(renames["ConfigurationVariablesIn"])
    types["ConfigurationVariablesOut"] = t.struct(
        {
            "variableSet": t.array(t.proxy(renames["VariableSetOut"])).optional(),
            "mcmId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigurationVariablesOut"])
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
    types["AdministratorWebTokenSpecPrivateAppsIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecPrivateAppsIn"])
    types["AdministratorWebTokenSpecPrivateAppsOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecPrivateAppsOut"])
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
    types["InstallsListResponseIn"] = t.struct(
        {"install": t.array(t.proxy(renames["InstallIn"])).optional()}
    ).named(renames["InstallsListResponseIn"])
    types["InstallsListResponseOut"] = t.struct(
        {
            "install": t.array(t.proxy(renames["InstallOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstallsListResponseOut"])
    types["DeviceReportIn"] = t.struct(
        {
            "lastUpdatedTimestampMillis": t.string().optional(),
            "appState": t.array(t.proxy(renames["AppStateIn"])).optional(),
        }
    ).named(renames["DeviceReportIn"])
    types["DeviceReportOut"] = t.struct(
        {
            "lastUpdatedTimestampMillis": t.string().optional(),
            "appState": t.array(t.proxy(renames["AppStateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceReportOut"])
    types["ManagedConfigurationsSettingsIn"] = t.struct(
        {
            "lastUpdatedTimestampMillis": t.string().optional(),
            "mcmId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ManagedConfigurationsSettingsIn"])
    types["ManagedConfigurationsSettingsOut"] = t.struct(
        {
            "lastUpdatedTimestampMillis": t.string().optional(),
            "mcmId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedConfigurationsSettingsOut"])
    types["VariableSetIn"] = t.struct(
        {"placeholder": t.string().optional(), "userValue": t.string().optional()}
    ).named(renames["VariableSetIn"])
    types["VariableSetOut"] = t.struct(
        {
            "placeholder": t.string().optional(),
            "userValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VariableSetOut"])
    types["GroupLicenseUsersListResponseIn"] = t.struct(
        {"user": t.array(t.proxy(renames["UserIn"])).optional()}
    ).named(renames["GroupLicenseUsersListResponseIn"])
    types["GroupLicenseUsersListResponseOut"] = t.struct(
        {
            "user": t.array(t.proxy(renames["UserOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupLicenseUsersListResponseOut"])
    types["ManagedPropertyIn"] = t.struct(
        {
            "valueStringArray": t.array(t.string()).optional(),
            "valueInteger": t.integer().optional(),
            "key": t.string().optional(),
            "valueBool": t.boolean().optional(),
            "valueBundleArray": t.array(
                t.proxy(renames["ManagedPropertyBundleIn"])
            ).optional(),
            "valueBundle": t.proxy(renames["ManagedPropertyBundleIn"]).optional(),
            "valueString": t.string().optional(),
        }
    ).named(renames["ManagedPropertyIn"])
    types["ManagedPropertyOut"] = t.struct(
        {
            "valueStringArray": t.array(t.string()).optional(),
            "valueInteger": t.integer().optional(),
            "key": t.string().optional(),
            "valueBool": t.boolean().optional(),
            "valueBundleArray": t.array(
                t.proxy(renames["ManagedPropertyBundleOut"])
            ).optional(),
            "valueBundle": t.proxy(renames["ManagedPropertyBundleOut"]).optional(),
            "valueString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPropertyOut"])
    types["EnterpriseIn"] = t.struct(
        {
            "id": t.string().optional(),
            "administrator": t.array(t.proxy(renames["AdministratorIn"])).optional(),
            "name": t.string().optional(),
            "primaryDomain": t.string().optional(),
        }
    ).named(renames["EnterpriseIn"])
    types["EnterpriseOut"] = t.struct(
        {
            "googleAuthenticationSettings": t.proxy(
                renames["GoogleAuthenticationSettingsOut"]
            ).optional(),
            "id": t.string().optional(),
            "administrator": t.array(t.proxy(renames["AdministratorOut"])).optional(),
            "name": t.string().optional(),
            "primaryDomain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseOut"])
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
    types["AdministratorWebTokenSpecStoreBuilderIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecStoreBuilderIn"])
    types["AdministratorWebTokenSpecStoreBuilderOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecStoreBuilderOut"])
    types["PageInfoIn"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "resultPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
        }
    ).named(renames["PageInfoIn"])
    types["PageInfoOut"] = t.struct(
        {
            "startIndex": t.integer().optional(),
            "resultPerPage": t.integer().optional(),
            "totalResults": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageInfoOut"])
    types["DeviceIn"] = t.struct(
        {
            "retailBrand": t.string().optional(),
            "managementType": t.string().optional(),
            "report": t.proxy(renames["DeviceReportIn"]).optional(),
            "maker": t.string().optional(),
            "product": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "latestBuildFingerprint": t.string().optional(),
            "device": t.string().optional(),
            "sdkVersion": t.integer().optional(),
            "androidId": t.string().optional(),
            "model": t.string().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "retailBrand": t.string().optional(),
            "managementType": t.string().optional(),
            "report": t.proxy(renames["DeviceReportOut"]).optional(),
            "maker": t.string().optional(),
            "product": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "latestBuildFingerprint": t.string().optional(),
            "device": t.string().optional(),
            "sdkVersion": t.integer().optional(),
            "androidId": t.string().optional(),
            "model": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["ManagedConfigurationIn"] = t.struct(
        {
            "managedProperty": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
            "kind": t.string().optional(),
            "productId": t.string().optional(),
            "configurationVariables": t.proxy(
                renames["ConfigurationVariablesIn"]
            ).optional(),
        }
    ).named(renames["ManagedConfigurationIn"])
    types["ManagedConfigurationOut"] = t.struct(
        {
            "managedProperty": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "kind": t.string().optional(),
            "productId": t.string().optional(),
            "configurationVariables": t.proxy(
                renames["ConfigurationVariablesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedConfigurationOut"])
    types["AutoInstallPolicyIn"] = t.struct(
        {
            "autoInstallPriority": t.integer().optional(),
            "autoInstallConstraint": t.array(
                t.proxy(renames["AutoInstallConstraintIn"])
            ).optional(),
            "autoInstallMode": t.string().optional(),
            "minimumVersionCode": t.integer().optional(),
        }
    ).named(renames["AutoInstallPolicyIn"])
    types["AutoInstallPolicyOut"] = t.struct(
        {
            "autoInstallPriority": t.integer().optional(),
            "autoInstallConstraint": t.array(
                t.proxy(renames["AutoInstallConstraintOut"])
            ).optional(),
            "autoInstallMode": t.string().optional(),
            "minimumVersionCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutoInstallPolicyOut"])
    types["TokenPaginationIn"] = t.struct(
        {"nextPageToken": t.string().optional(), "previousPageToken": t.string()}
    ).named(renames["TokenPaginationIn"])
    types["TokenPaginationOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "previousPageToken": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenPaginationOut"])
    types["NewDeviceEventIn"] = t.struct(
        {
            "dpcPackageName": t.string().optional(),
            "deviceId": t.string().optional(),
            "userId": t.string().optional(),
            "managementType": t.string().optional(),
        }
    ).named(renames["NewDeviceEventIn"])
    types["NewDeviceEventOut"] = t.struct(
        {
            "dpcPackageName": t.string().optional(),
            "deviceId": t.string().optional(),
            "userId": t.string().optional(),
            "managementType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NewDeviceEventOut"])
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
    types["ProductPolicyIn"] = t.struct(
        {
            "enterpriseAuthenticationAppLinkConfigs": t.array(
                t.proxy(renames["EnterpriseAuthenticationAppLinkConfigIn"])
            ).optional(),
            "autoUpdateMode": t.string().optional(),
            "autoInstallPolicy": t.proxy(renames["AutoInstallPolicyIn"]).optional(),
            "tracks": t.array(t.string()).optional(),
            "managedConfiguration": t.proxy(
                renames["ManagedConfigurationIn"]
            ).optional(),
            "productId": t.string().optional(),
            "trackIds": t.array(t.string()).optional(),
        }
    ).named(renames["ProductPolicyIn"])
    types["ProductPolicyOut"] = t.struct(
        {
            "enterpriseAuthenticationAppLinkConfigs": t.array(
                t.proxy(renames["EnterpriseAuthenticationAppLinkConfigOut"])
            ).optional(),
            "autoUpdateMode": t.string().optional(),
            "autoInstallPolicy": t.proxy(renames["AutoInstallPolicyOut"]).optional(),
            "tracks": t.array(t.string()).optional(),
            "managedConfiguration": t.proxy(
                renames["ManagedConfigurationOut"]
            ).optional(),
            "productId": t.string().optional(),
            "trackIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductPolicyOut"])
    types["DevicesListResponseIn"] = t.struct(
        {"device": t.array(t.proxy(renames["DeviceIn"])).optional()}
    ).named(renames["DevicesListResponseIn"])
    types["DevicesListResponseOut"] = t.struct(
        {
            "device": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicesListResponseOut"])
    types["GroupLicenseIn"] = t.struct(
        {
            "numPurchased": t.integer().optional(),
            "acquisitionKind": t.string().optional(),
            "numProvisioned": t.integer().optional(),
            "productId": t.string().optional(),
            "permissions": t.string().optional(),
            "approval": t.string().optional(),
        }
    ).named(renames["GroupLicenseIn"])
    types["GroupLicenseOut"] = t.struct(
        {
            "numPurchased": t.integer().optional(),
            "acquisitionKind": t.string().optional(),
            "numProvisioned": t.integer().optional(),
            "productId": t.string().optional(),
            "permissions": t.string().optional(),
            "approval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupLicenseOut"])
    types["MaintenanceWindowIn"] = t.struct(
        {
            "startTimeAfterMidnightMs": t.string().optional(),
            "durationMs": t.string().optional(),
        }
    ).named(renames["MaintenanceWindowIn"])
    types["MaintenanceWindowOut"] = t.struct(
        {
            "startTimeAfterMidnightMs": t.string().optional(),
            "durationMs": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MaintenanceWindowOut"])
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
    types["InstallIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "installState": t.string().optional(),
            "versionCode": t.integer().optional(),
        }
    ).named(renames["InstallIn"])
    types["InstallOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "installState": t.string().optional(),
            "versionCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstallOut"])
    types["ProductsGenerateApprovalUrlResponseIn"] = t.struct(
        {"url": t.string().optional()}
    ).named(renames["ProductsGenerateApprovalUrlResponseIn"])
    types["ProductsGenerateApprovalUrlResponseOut"] = t.struct(
        {
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProductsGenerateApprovalUrlResponseOut"])
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
    types["EnterpriseAccountIn"] = t.struct(
        {"accountEmail": t.string().optional()}
    ).named(renames["EnterpriseAccountIn"])
    types["EnterpriseAccountOut"] = t.struct(
        {
            "accountEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseAccountOut"])
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
    types["AppVersionIn"] = t.struct(
        {
            "trackId": t.array(t.string()).optional(),
            "versionCode": t.integer().optional(),
            "track": t.string().optional(),
            "versionString": t.string().optional(),
            "isProduction": t.boolean().optional(),
        }
    ).named(renames["AppVersionIn"])
    types["AppVersionOut"] = t.struct(
        {
            "trackId": t.array(t.string()).optional(),
            "versionCode": t.integer().optional(),
            "track": t.string().optional(),
            "versionString": t.string().optional(),
            "isProduction": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppVersionOut"])
    types["AppUpdateEventIn"] = t.struct({"productId": t.string().optional()}).named(
        renames["AppUpdateEventIn"]
    )
    types["AppUpdateEventOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppUpdateEventOut"])
    types["InstallFailureEventIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "deviceId": t.string().optional(),
            "failureReason": t.string().optional(),
            "failureDetails": t.string().optional(),
            "userId": t.string().optional(),
        }
    ).named(renames["InstallFailureEventIn"])
    types["InstallFailureEventOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "deviceId": t.string().optional(),
            "failureReason": t.string().optional(),
            "failureDetails": t.string().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstallFailureEventOut"])
    types["AdministratorWebTokenSpecWebAppsIn"] = t.struct(
        {"enabled": t.boolean().optional()}
    ).named(renames["AdministratorWebTokenSpecWebAppsIn"])
    types["AdministratorWebTokenSpecWebAppsOut"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdministratorWebTokenSpecWebAppsOut"])

    functions = {}
    functions["usersGet"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "managementType": t.string().optional(),
                "primaryEmail": t.string().optional(),
                "accountIdentifier": t.string().optional(),
                "accountType": t.string().optional(),
                "displayName": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersDelete"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "managementType": t.string().optional(),
                "primaryEmail": t.string().optional(),
                "accountIdentifier": t.string().optional(),
                "accountType": t.string().optional(),
                "displayName": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersRevokeDeviceAccess"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "managementType": t.string().optional(),
                "primaryEmail": t.string().optional(),
                "accountIdentifier": t.string().optional(),
                "accountType": t.string().optional(),
                "displayName": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersSetAvailableProductSet"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "managementType": t.string().optional(),
                "primaryEmail": t.string().optional(),
                "accountIdentifier": t.string().optional(),
                "accountType": t.string().optional(),
                "displayName": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGenerateAuthenticationToken"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "managementType": t.string().optional(),
                "primaryEmail": t.string().optional(),
                "accountIdentifier": t.string().optional(),
                "accountType": t.string().optional(),
                "displayName": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersGetAvailableProductSet"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "managementType": t.string().optional(),
                "primaryEmail": t.string().optional(),
                "accountIdentifier": t.string().optional(),
                "accountType": t.string().optional(),
                "displayName": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersList"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "managementType": t.string().optional(),
                "primaryEmail": t.string().optional(),
                "accountIdentifier": t.string().optional(),
                "accountType": t.string().optional(),
                "displayName": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersUpdate"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "managementType": t.string().optional(),
                "primaryEmail": t.string().optional(),
                "accountIdentifier": t.string().optional(),
                "accountType": t.string().optional(),
                "displayName": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["usersInsert"] = androidenterprise.post(
        "androidenterprise/v1/enterprises/{enterpriseId}/users",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "managementType": t.string().optional(),
                "primaryEmail": t.string().optional(),
                "accountIdentifier": t.string().optional(),
                "accountType": t.string().optional(),
                "displayName": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UserOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGetAppRestrictionsSchema"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/permissions",
        t.struct(
            {
                "productId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPermissionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsApprove"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/permissions",
        t.struct(
            {
                "productId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPermissionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/permissions",
        t.struct(
            {
                "productId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPermissionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/permissions",
        t.struct(
            {
                "productId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPermissionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsUnapprove"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/permissions",
        t.struct(
            {
                "productId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPermissionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGenerateApprovalUrl"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/permissions",
        t.struct(
            {
                "productId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPermissionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["productsGetPermissions"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/permissions",
        t.struct(
            {
                "productId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProductPermissionsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entitlementsList"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "entitlementId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "install": t.boolean().optional(),
                "productId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entitlementsGet"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "entitlementId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "install": t.boolean().optional(),
                "productId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entitlementsDelete"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "entitlementId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "install": t.boolean().optional(),
                "productId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["entitlementsUpdate"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}",
        t.struct(
            {
                "userId": t.string().optional(),
                "entitlementId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "install": t.boolean().optional(),
                "productId": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EntitlementOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsList"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps/{webAppId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "webAppId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsGet"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps/{webAppId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "webAppId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsUpdate"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps/{webAppId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "webAppId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsInsert"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps/{webAppId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "webAppId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["webappsDelete"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/webApps/{webAppId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "webAppId": t.string().optional(),
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
    functions["managedconfigurationsforuserGet"] = androidenterprise.delete(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser/{managedConfigurationForUserId}",
        t.struct(
            {
                "managedConfigurationForUserId": t.string().optional(),
                "userId": t.string().optional(),
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
                "managedConfigurationForUserId": t.string().optional(),
                "userId": t.string().optional(),
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
                "managedConfigurationForUserId": t.string().optional(),
                "userId": t.string().optional(),
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
                "managedConfigurationForUserId": t.string().optional(),
                "userId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["serviceaccountkeysInsert"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/serviceAccountKeys",
        t.struct(
            {"enterpriseId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ServiceAccountKeysListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["serviceaccountkeysDelete"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/serviceAccountKeys",
        t.struct(
            {"enterpriseId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ServiceAccountKeysListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["serviceaccountkeysList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/serviceAccountKeys",
        t.struct(
            {"enterpriseId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["ServiceAccountKeysListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installsGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "deviceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstallsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installsDelete"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "deviceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstallsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installsUpdate"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "deviceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstallsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["installsList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "deviceId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstallsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersDelete"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters/{clusterId}",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "clusterId": t.string().optional(),
                "productId": t.array(t.string()).optional(),
                "name": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
                "orderInPage": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersGet"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters/{clusterId}",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "clusterId": t.string().optional(),
                "productId": t.array(t.string()).optional(),
                "name": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
                "orderInPage": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersList"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters/{clusterId}",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "clusterId": t.string().optional(),
                "productId": t.array(t.string()).optional(),
                "name": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
                "orderInPage": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersInsert"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters/{clusterId}",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "clusterId": t.string().optional(),
                "productId": t.array(t.string()).optional(),
                "name": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
                "orderInPage": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutclustersUpdate"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters/{clusterId}",
        t.struct(
            {
                "pageId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "clusterId": t.string().optional(),
                "productId": t.array(t.string()).optional(),
                "name": t.array(t.proxy(renames["LocalizedTextIn"])).optional(),
                "orderInPage": t.string().optional(),
                "id": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreClusterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsfordeviceDelete"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice",
        t.struct(
            {
                "userId": t.string().optional(),
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManagedConfigurationsForDeviceListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsfordeviceGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice",
        t.struct(
            {
                "userId": t.string().optional(),
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManagedConfigurationsForDeviceListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsfordeviceUpdate"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice",
        t.struct(
            {
                "userId": t.string().optional(),
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManagedConfigurationsForDeviceListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationsfordeviceList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice",
        t.struct(
            {
                "userId": t.string().optional(),
                "deviceId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManagedConfigurationsForDeviceListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grouplicenseusersList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/groupLicenses/{groupLicenseId}/users",
        t.struct(
            {
                "groupLicenseId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GroupLicenseUsersListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grouplicensesGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/groupLicenses",
        t.struct(
            {"enterpriseId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GroupLicensesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["grouplicensesList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/groupLicenses",
        t.struct(
            {"enterpriseId": t.string().optional(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GroupLicensesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesForceReportUpload"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DevicesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesGetState"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DevicesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DevicesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesUpdate"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DevicesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesSetState"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DevicesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["devicesList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/users/{userId}/devices",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "userId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DevicesListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["managedconfigurationssettingsList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/products/{productId}/managedConfigurationsSettings",
        t.struct(
            {
                "productId": t.string().optional(),
                "enterpriseId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ManagedConfigurationsSettingsListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesCreateEnrollmentToken"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesCreateWebToken"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGenerateSignupUrl"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGetServiceAccount"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesCompleteSignup"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnroll"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesSetAccount"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesList"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGet"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesAcknowledgeNotificationSet"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesSendTestPushNotification"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGetStoreLayout"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesUnenroll"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPullNotificationSet"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesSetStoreLayout"] = androidenterprise.put(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "storeLayoutType": t.string().optional(),
                "homepageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StoreLayoutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesUpdate"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StorePageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesList"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StorePageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesDelete"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StorePageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesInsert"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StorePageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["storelayoutpagesGet"] = androidenterprise.get(
        "androidenterprise/v1/enterprises/{enterpriseId}/storeLayout/pages/{pageId}",
        t.struct(
            {
                "enterpriseId": t.string().optional(),
                "pageId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["StorePageOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="androidenterprise",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
