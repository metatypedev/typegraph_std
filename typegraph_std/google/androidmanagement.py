from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_androidmanagement() -> Import:
    androidmanagement = HTTPRuntime("https://androidmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_androidmanagement_1_ErrorResponse",
        "PersistentPreferredActivityIn": "_androidmanagement_2_PersistentPreferredActivityIn",
        "PersistentPreferredActivityOut": "_androidmanagement_3_PersistentPreferredActivityOut",
        "LogBufferSizeCriticalEventIn": "_androidmanagement_4_LogBufferSizeCriticalEventIn",
        "LogBufferSizeCriticalEventOut": "_androidmanagement_5_LogBufferSizeCriticalEventOut",
        "ManagedPropertyIn": "_androidmanagement_6_ManagedPropertyIn",
        "ManagedPropertyOut": "_androidmanagement_7_ManagedPropertyOut",
        "ContactInfoIn": "_androidmanagement_8_ContactInfoIn",
        "ContactInfoOut": "_androidmanagement_9_ContactInfoOut",
        "FilePushedEventIn": "_androidmanagement_10_FilePushedEventIn",
        "FilePushedEventOut": "_androidmanagement_11_FilePushedEventOut",
        "PersonalUsagePoliciesIn": "_androidmanagement_12_PersonalUsagePoliciesIn",
        "PersonalUsagePoliciesOut": "_androidmanagement_13_PersonalUsagePoliciesOut",
        "ManagedConfigurationTemplateIn": "_androidmanagement_14_ManagedConfigurationTemplateIn",
        "ManagedConfigurationTemplateOut": "_androidmanagement_15_ManagedConfigurationTemplateOut",
        "OncCertificateProviderIn": "_androidmanagement_16_OncCertificateProviderIn",
        "OncCertificateProviderOut": "_androidmanagement_17_OncCertificateProviderOut",
        "ApplicationIn": "_androidmanagement_18_ApplicationIn",
        "ApplicationOut": "_androidmanagement_19_ApplicationOut",
        "StatusIn": "_androidmanagement_20_StatusIn",
        "StatusOut": "_androidmanagement_21_StatusOut",
        "ApplicationReportingSettingsIn": "_androidmanagement_22_ApplicationReportingSettingsIn",
        "ApplicationReportingSettingsOut": "_androidmanagement_23_ApplicationReportingSettingsOut",
        "AdbShellInteractiveEventIn": "_androidmanagement_24_AdbShellInteractiveEventIn",
        "AdbShellInteractiveEventOut": "_androidmanagement_25_AdbShellInteractiveEventOut",
        "AppTrackInfoIn": "_androidmanagement_26_AppTrackInfoIn",
        "AppTrackInfoOut": "_androidmanagement_27_AppTrackInfoOut",
        "ManagedPropertyEntryIn": "_androidmanagement_28_ManagedPropertyEntryIn",
        "ManagedPropertyEntryOut": "_androidmanagement_29_ManagedPropertyEntryOut",
        "ListOperationsResponseIn": "_androidmanagement_30_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_androidmanagement_31_ListOperationsResponseOut",
        "OsShutdownEventIn": "_androidmanagement_32_OsShutdownEventIn",
        "OsShutdownEventOut": "_androidmanagement_33_OsShutdownEventOut",
        "DateIn": "_androidmanagement_34_DateIn",
        "DateOut": "_androidmanagement_35_DateOut",
        "ListDevicesResponseIn": "_androidmanagement_36_ListDevicesResponseIn",
        "ListDevicesResponseOut": "_androidmanagement_37_ListDevicesResponseOut",
        "SpecificNonComplianceContextIn": "_androidmanagement_38_SpecificNonComplianceContextIn",
        "SpecificNonComplianceContextOut": "_androidmanagement_39_SpecificNonComplianceContextOut",
        "MediaMountEventIn": "_androidmanagement_40_MediaMountEventIn",
        "MediaMountEventOut": "_androidmanagement_41_MediaMountEventOut",
        "MemoryEventIn": "_androidmanagement_42_MemoryEventIn",
        "MemoryEventOut": "_androidmanagement_43_MemoryEventOut",
        "FreezePeriodIn": "_androidmanagement_44_FreezePeriodIn",
        "FreezePeriodOut": "_androidmanagement_45_FreezePeriodOut",
        "CertAuthorityRemovedEventIn": "_androidmanagement_46_CertAuthorityRemovedEventIn",
        "CertAuthorityRemovedEventOut": "_androidmanagement_47_CertAuthorityRemovedEventOut",
        "UsageLogEventIn": "_androidmanagement_48_UsageLogEventIn",
        "UsageLogEventOut": "_androidmanagement_49_UsageLogEventOut",
        "DnsEventIn": "_androidmanagement_50_DnsEventIn",
        "DnsEventOut": "_androidmanagement_51_DnsEventOut",
        "EnterpriseIn": "_androidmanagement_52_EnterpriseIn",
        "EnterpriseOut": "_androidmanagement_53_EnterpriseOut",
        "LoggingStartedEventIn": "_androidmanagement_54_LoggingStartedEventIn",
        "LoggingStartedEventOut": "_androidmanagement_55_LoggingStartedEventOut",
        "DeviceSettingsIn": "_androidmanagement_56_DeviceSettingsIn",
        "DeviceSettingsOut": "_androidmanagement_57_DeviceSettingsOut",
        "RemoteLockEventIn": "_androidmanagement_58_RemoteLockEventIn",
        "RemoteLockEventOut": "_androidmanagement_59_RemoteLockEventOut",
        "PackageNameListIn": "_androidmanagement_60_PackageNameListIn",
        "PackageNameListOut": "_androidmanagement_61_PackageNameListOut",
        "ApplicationPermissionIn": "_androidmanagement_62_ApplicationPermissionIn",
        "ApplicationPermissionOut": "_androidmanagement_63_ApplicationPermissionOut",
        "BlockActionIn": "_androidmanagement_64_BlockActionIn",
        "BlockActionOut": "_androidmanagement_65_BlockActionOut",
        "SetupActionIn": "_androidmanagement_66_SetupActionIn",
        "SetupActionOut": "_androidmanagement_67_SetupActionOut",
        "AppVersionIn": "_androidmanagement_68_AppVersionIn",
        "AppVersionOut": "_androidmanagement_69_AppVersionOut",
        "WebTokenIn": "_androidmanagement_70_WebTokenIn",
        "WebTokenOut": "_androidmanagement_71_WebTokenOut",
        "ApplicationPolicyIn": "_androidmanagement_72_ApplicationPolicyIn",
        "ApplicationPolicyOut": "_androidmanagement_73_ApplicationPolicyOut",
        "ExtensionConfigIn": "_androidmanagement_74_ExtensionConfigIn",
        "ExtensionConfigOut": "_androidmanagement_75_ExtensionConfigOut",
        "BatchUsageLogEventsIn": "_androidmanagement_76_BatchUsageLogEventsIn",
        "BatchUsageLogEventsOut": "_androidmanagement_77_BatchUsageLogEventsOut",
        "SignupUrlIn": "_androidmanagement_78_SignupUrlIn",
        "SignupUrlOut": "_androidmanagement_79_SignupUrlOut",
        "WipeFailureEventIn": "_androidmanagement_80_WipeFailureEventIn",
        "WipeFailureEventOut": "_androidmanagement_81_WipeFailureEventOut",
        "KeyguardDismissAuthAttemptEventIn": "_androidmanagement_82_KeyguardDismissAuthAttemptEventIn",
        "KeyguardDismissAuthAttemptEventOut": "_androidmanagement_83_KeyguardDismissAuthAttemptEventOut",
        "ContentProviderEndpointIn": "_androidmanagement_84_ContentProviderEndpointIn",
        "ContentProviderEndpointOut": "_androidmanagement_85_ContentProviderEndpointOut",
        "WebAppIconIn": "_androidmanagement_86_WebAppIconIn",
        "WebAppIconOut": "_androidmanagement_87_WebAppIconOut",
        "TermsAndConditionsIn": "_androidmanagement_88_TermsAndConditionsIn",
        "TermsAndConditionsOut": "_androidmanagement_89_TermsAndConditionsOut",
        "PowerManagementEventIn": "_androidmanagement_90_PowerManagementEventIn",
        "PowerManagementEventOut": "_androidmanagement_91_PowerManagementEventOut",
        "KeyDestructionEventIn": "_androidmanagement_92_KeyDestructionEventIn",
        "KeyDestructionEventOut": "_androidmanagement_93_KeyDestructionEventOut",
        "CommonCriteriaModeInfoIn": "_androidmanagement_94_CommonCriteriaModeInfoIn",
        "CommonCriteriaModeInfoOut": "_androidmanagement_95_CommonCriteriaModeInfoOut",
        "SigninDetailIn": "_androidmanagement_96_SigninDetailIn",
        "SigninDetailOut": "_androidmanagement_97_SigninDetailOut",
        "CrossProfilePoliciesIn": "_androidmanagement_98_CrossProfilePoliciesIn",
        "CrossProfilePoliciesOut": "_androidmanagement_99_CrossProfilePoliciesOut",
        "MediaUnmountEventIn": "_androidmanagement_100_MediaUnmountEventIn",
        "MediaUnmountEventOut": "_androidmanagement_101_MediaUnmountEventOut",
        "ApplicationReportIn": "_androidmanagement_102_ApplicationReportIn",
        "ApplicationReportOut": "_androidmanagement_103_ApplicationReportOut",
        "AppProcessStartEventIn": "_androidmanagement_104_AppProcessStartEventIn",
        "AppProcessStartEventOut": "_androidmanagement_105_AppProcessStartEventOut",
        "StatusReportingSettingsIn": "_androidmanagement_106_StatusReportingSettingsIn",
        "StatusReportingSettingsOut": "_androidmanagement_107_StatusReportingSettingsOut",
        "LaunchAppActionIn": "_androidmanagement_108_LaunchAppActionIn",
        "LaunchAppActionOut": "_androidmanagement_109_LaunchAppActionOut",
        "HardwareInfoIn": "_androidmanagement_110_HardwareInfoIn",
        "HardwareInfoOut": "_androidmanagement_111_HardwareInfoOut",
        "FilePulledEventIn": "_androidmanagement_112_FilePulledEventIn",
        "FilePulledEventOut": "_androidmanagement_113_FilePulledEventOut",
        "UsageLogIn": "_androidmanagement_114_UsageLogIn",
        "UsageLogOut": "_androidmanagement_115_UsageLogOut",
        "HardwareStatusIn": "_androidmanagement_116_HardwareStatusIn",
        "HardwareStatusOut": "_androidmanagement_117_HardwareStatusOut",
        "ListPoliciesResponseIn": "_androidmanagement_118_ListPoliciesResponseIn",
        "ListPoliciesResponseOut": "_androidmanagement_119_ListPoliciesResponseOut",
        "PermissionGrantIn": "_androidmanagement_120_PermissionGrantIn",
        "PermissionGrantOut": "_androidmanagement_121_PermissionGrantOut",
        "ConnectEventIn": "_androidmanagement_122_ConnectEventIn",
        "ConnectEventOut": "_androidmanagement_123_ConnectEventOut",
        "SoftwareInfoIn": "_androidmanagement_124_SoftwareInfoIn",
        "SoftwareInfoOut": "_androidmanagement_125_SoftwareInfoOut",
        "SystemUpdateInfoIn": "_androidmanagement_126_SystemUpdateInfoIn",
        "SystemUpdateInfoOut": "_androidmanagement_127_SystemUpdateInfoOut",
        "MemoryInfoIn": "_androidmanagement_128_MemoryInfoIn",
        "MemoryInfoOut": "_androidmanagement_129_MemoryInfoOut",
        "SecurityPostureIn": "_androidmanagement_130_SecurityPostureIn",
        "SecurityPostureOut": "_androidmanagement_131_SecurityPostureOut",
        "ChoosePrivateKeyRuleIn": "_androidmanagement_132_ChoosePrivateKeyRuleIn",
        "ChoosePrivateKeyRuleOut": "_androidmanagement_133_ChoosePrivateKeyRuleOut",
        "ExternalDataIn": "_androidmanagement_134_ExternalDataIn",
        "ExternalDataOut": "_androidmanagement_135_ExternalDataOut",
        "NetworkInfoIn": "_androidmanagement_136_NetworkInfoIn",
        "NetworkInfoOut": "_androidmanagement_137_NetworkInfoOut",
        "OperationIn": "_androidmanagement_138_OperationIn",
        "OperationOut": "_androidmanagement_139_OperationOut",
        "PersonalApplicationPolicyIn": "_androidmanagement_140_PersonalApplicationPolicyIn",
        "PersonalApplicationPolicyOut": "_androidmanagement_141_PersonalApplicationPolicyOut",
        "KeyImportEventIn": "_androidmanagement_142_KeyImportEventIn",
        "KeyImportEventOut": "_androidmanagement_143_KeyImportEventOut",
        "WebAppIn": "_androidmanagement_144_WebAppIn",
        "WebAppOut": "_androidmanagement_145_WebAppOut",
        "AdbShellCommandEventIn": "_androidmanagement_146_AdbShellCommandEventIn",
        "AdbShellCommandEventOut": "_androidmanagement_147_AdbShellCommandEventOut",
        "OsStartupEventIn": "_androidmanagement_148_OsStartupEventIn",
        "OsStartupEventOut": "_androidmanagement_149_OsStartupEventOut",
        "PolicyIn": "_androidmanagement_150_PolicyIn",
        "PolicyOut": "_androidmanagement_151_PolicyOut",
        "IssueCommandResponseIn": "_androidmanagement_152_IssueCommandResponseIn",
        "IssueCommandResponseOut": "_androidmanagement_153_IssueCommandResponseOut",
        "ApplicationEventIn": "_androidmanagement_154_ApplicationEventIn",
        "ApplicationEventOut": "_androidmanagement_155_ApplicationEventOut",
        "AdvancedSecurityOverridesIn": "_androidmanagement_156_AdvancedSecurityOverridesIn",
        "AdvancedSecurityOverridesOut": "_androidmanagement_157_AdvancedSecurityOverridesOut",
        "LoggingStoppedEventIn": "_androidmanagement_158_LoggingStoppedEventIn",
        "LoggingStoppedEventOut": "_androidmanagement_159_LoggingStoppedEventOut",
        "UserIn": "_androidmanagement_160_UserIn",
        "UserOut": "_androidmanagement_161_UserOut",
        "KioskCustomizationIn": "_androidmanagement_162_KioskCustomizationIn",
        "KioskCustomizationOut": "_androidmanagement_163_KioskCustomizationOut",
        "WipeActionIn": "_androidmanagement_164_WipeActionIn",
        "WipeActionOut": "_androidmanagement_165_WipeActionOut",
        "PasswordRequirementsIn": "_androidmanagement_166_PasswordRequirementsIn",
        "PasswordRequirementsOut": "_androidmanagement_167_PasswordRequirementsOut",
        "ClearAppsDataParamsIn": "_androidmanagement_168_ClearAppsDataParamsIn",
        "ClearAppsDataParamsOut": "_androidmanagement_169_ClearAppsDataParamsOut",
        "ListEnrollmentTokensResponseIn": "_androidmanagement_170_ListEnrollmentTokensResponseIn",
        "ListEnrollmentTokensResponseOut": "_androidmanagement_171_ListEnrollmentTokensResponseOut",
        "TelephonyInfoIn": "_androidmanagement_172_TelephonyInfoIn",
        "TelephonyInfoOut": "_androidmanagement_173_TelephonyInfoOut",
        "CryptoSelfTestCompletedEventIn": "_androidmanagement_174_CryptoSelfTestCompletedEventIn",
        "CryptoSelfTestCompletedEventOut": "_androidmanagement_175_CryptoSelfTestCompletedEventOut",
        "DisplayIn": "_androidmanagement_176_DisplayIn",
        "DisplayOut": "_androidmanagement_177_DisplayOut",
        "PasswordPoliciesContextIn": "_androidmanagement_178_PasswordPoliciesContextIn",
        "PasswordPoliciesContextOut": "_androidmanagement_179_PasswordPoliciesContextOut",
        "CertValidationFailureEventIn": "_androidmanagement_180_CertValidationFailureEventIn",
        "CertValidationFailureEventOut": "_androidmanagement_181_CertValidationFailureEventOut",
        "CertAuthorityInstalledEventIn": "_androidmanagement_182_CertAuthorityInstalledEventIn",
        "CertAuthorityInstalledEventOut": "_androidmanagement_183_CertAuthorityInstalledEventOut",
        "ComplianceRuleIn": "_androidmanagement_184_ComplianceRuleIn",
        "ComplianceRuleOut": "_androidmanagement_185_ComplianceRuleOut",
        "OncWifiContextIn": "_androidmanagement_186_OncWifiContextIn",
        "OncWifiContextOut": "_androidmanagement_187_OncWifiContextOut",
        "SystemUpdateIn": "_androidmanagement_188_SystemUpdateIn",
        "SystemUpdateOut": "_androidmanagement_189_SystemUpdateOut",
        "UserFacingMessageIn": "_androidmanagement_190_UserFacingMessageIn",
        "UserFacingMessageOut": "_androidmanagement_191_UserFacingMessageOut",
        "EmptyIn": "_androidmanagement_192_EmptyIn",
        "EmptyOut": "_androidmanagement_193_EmptyOut",
        "DeviceIn": "_androidmanagement_194_DeviceIn",
        "DeviceOut": "_androidmanagement_195_DeviceOut",
        "NonComplianceDetailIn": "_androidmanagement_196_NonComplianceDetailIn",
        "NonComplianceDetailOut": "_androidmanagement_197_NonComplianceDetailOut",
        "ListWebAppsResponseIn": "_androidmanagement_198_ListWebAppsResponseIn",
        "ListWebAppsResponseOut": "_androidmanagement_199_ListWebAppsResponseOut",
        "NonComplianceDetailConditionIn": "_androidmanagement_200_NonComplianceDetailConditionIn",
        "NonComplianceDetailConditionOut": "_androidmanagement_201_NonComplianceDetailConditionOut",
        "ListEnterprisesResponseIn": "_androidmanagement_202_ListEnterprisesResponseIn",
        "ListEnterprisesResponseOut": "_androidmanagement_203_ListEnterprisesResponseOut",
        "KeyedAppStateIn": "_androidmanagement_204_KeyedAppStateIn",
        "KeyedAppStateOut": "_androidmanagement_205_KeyedAppStateOut",
        "ClearAppsDataStatusIn": "_androidmanagement_206_ClearAppsDataStatusIn",
        "ClearAppsDataStatusOut": "_androidmanagement_207_ClearAppsDataStatusOut",
        "EnrollmentTokenIn": "_androidmanagement_208_EnrollmentTokenIn",
        "EnrollmentTokenOut": "_androidmanagement_209_EnrollmentTokenOut",
        "AppProcessInfoIn": "_androidmanagement_210_AppProcessInfoIn",
        "AppProcessInfoOut": "_androidmanagement_211_AppProcessInfoOut",
        "ApiLevelConditionIn": "_androidmanagement_212_ApiLevelConditionIn",
        "ApiLevelConditionOut": "_androidmanagement_213_ApiLevelConditionOut",
        "PerAppResultIn": "_androidmanagement_214_PerAppResultIn",
        "PerAppResultOut": "_androidmanagement_215_PerAppResultOut",
        "KeyGeneratedEventIn": "_androidmanagement_216_KeyGeneratedEventIn",
        "KeyGeneratedEventOut": "_androidmanagement_217_KeyGeneratedEventOut",
        "PolicyEnforcementRuleIn": "_androidmanagement_218_PolicyEnforcementRuleIn",
        "PolicyEnforcementRuleOut": "_androidmanagement_219_PolicyEnforcementRuleOut",
        "KeyguardDismissedEventIn": "_androidmanagement_220_KeyguardDismissedEventIn",
        "KeyguardDismissedEventOut": "_androidmanagement_221_KeyguardDismissedEventOut",
        "CommandIn": "_androidmanagement_222_CommandIn",
        "CommandOut": "_androidmanagement_223_CommandOut",
        "PostureDetailIn": "_androidmanagement_224_PostureDetailIn",
        "PostureDetailOut": "_androidmanagement_225_PostureDetailOut",
        "KeyIntegrityViolationEventIn": "_androidmanagement_226_KeyIntegrityViolationEventIn",
        "KeyIntegrityViolationEventOut": "_androidmanagement_227_KeyIntegrityViolationEventOut",
        "AlwaysOnVpnPackageIn": "_androidmanagement_228_AlwaysOnVpnPackageIn",
        "AlwaysOnVpnPackageOut": "_androidmanagement_229_AlwaysOnVpnPackageOut",
        "ProxyInfoIn": "_androidmanagement_230_ProxyInfoIn",
        "ProxyInfoOut": "_androidmanagement_231_ProxyInfoOut",
        "KeyguardSecuredEventIn": "_androidmanagement_232_KeyguardSecuredEventIn",
        "KeyguardSecuredEventOut": "_androidmanagement_233_KeyguardSecuredEventOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PersistentPreferredActivityIn"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "actions": t.array(t.string()).optional(),
            "receiverActivity": t.string().optional(),
        }
    ).named(renames["PersistentPreferredActivityIn"])
    types["PersistentPreferredActivityOut"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "actions": t.array(t.string()).optional(),
            "receiverActivity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistentPreferredActivityOut"])
    types["LogBufferSizeCriticalEventIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["LogBufferSizeCriticalEventIn"])
    types["LogBufferSizeCriticalEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LogBufferSizeCriticalEventOut"])
    types["ManagedPropertyIn"] = t.struct(
        {
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nestedProperties": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
            "description": t.string().optional(),
            "key": t.string().optional(),
            "title": t.string().optional(),
            "entries": t.array(t.proxy(renames["ManagedPropertyEntryIn"])).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ManagedPropertyIn"])
    types["ManagedPropertyOut"] = t.struct(
        {
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nestedProperties": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "description": t.string().optional(),
            "key": t.string().optional(),
            "title": t.string().optional(),
            "entries": t.array(t.proxy(renames["ManagedPropertyEntryOut"])).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPropertyOut"])
    types["ContactInfoIn"] = t.struct(
        {
            "dataProtectionOfficerName": t.string().optional(),
            "euRepresentativeEmail": t.string().optional(),
            "dataProtectionOfficerEmail": t.string().optional(),
            "euRepresentativePhone": t.string().optional(),
            "contactEmail": t.string().optional(),
            "euRepresentativeName": t.string().optional(),
            "dataProtectionOfficerPhone": t.string().optional(),
        }
    ).named(renames["ContactInfoIn"])
    types["ContactInfoOut"] = t.struct(
        {
            "dataProtectionOfficerName": t.string().optional(),
            "euRepresentativeEmail": t.string().optional(),
            "dataProtectionOfficerEmail": t.string().optional(),
            "euRepresentativePhone": t.string().optional(),
            "contactEmail": t.string().optional(),
            "euRepresentativeName": t.string().optional(),
            "dataProtectionOfficerPhone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoOut"])
    types["FilePushedEventIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FilePushedEventIn"]
    )
    types["FilePushedEventOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilePushedEventOut"])
    types["PersonalUsagePoliciesIn"] = t.struct(
        {
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "cameraDisabled": t.boolean().optional(),
            "personalApplications": t.array(
                t.proxy(renames["PersonalApplicationPolicyIn"])
            ).optional(),
            "personalPlayStoreMode": t.string().optional(),
            "maxDaysWithWorkOff": t.integer().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
        }
    ).named(renames["PersonalUsagePoliciesIn"])
    types["PersonalUsagePoliciesOut"] = t.struct(
        {
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "cameraDisabled": t.boolean().optional(),
            "personalApplications": t.array(
                t.proxy(renames["PersonalApplicationPolicyOut"])
            ).optional(),
            "personalPlayStoreMode": t.string().optional(),
            "maxDaysWithWorkOff": t.integer().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalUsagePoliciesOut"])
    types["ManagedConfigurationTemplateIn"] = t.struct(
        {
            "configurationVariables": t.struct({"_": t.string().optional()}).optional(),
            "templateId": t.string().optional(),
        }
    ).named(renames["ManagedConfigurationTemplateIn"])
    types["ManagedConfigurationTemplateOut"] = t.struct(
        {
            "configurationVariables": t.struct({"_": t.string().optional()}).optional(),
            "templateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedConfigurationTemplateOut"])
    types["OncCertificateProviderIn"] = t.struct(
        {
            "certificateReferences": t.array(t.string()).optional(),
            "contentProviderEndpoint": t.proxy(
                renames["ContentProviderEndpointIn"]
            ).optional(),
        }
    ).named(renames["OncCertificateProviderIn"])
    types["OncCertificateProviderOut"] = t.struct(
        {
            "certificateReferences": t.array(t.string()).optional(),
            "contentProviderEndpoint": t.proxy(
                renames["ContentProviderEndpointOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OncCertificateProviderOut"])
    types["ApplicationIn"] = t.struct(
        {
            "appVersions": t.array(t.proxy(renames["AppVersionIn"])).optional(),
            "availableCountries": t.array(t.string()).optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "appTracks": t.array(t.proxy(renames["AppTrackInfoIn"])).optional(),
            "title": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "appPricing": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "smallIconUrl": t.string().optional(),
            "contentRating": t.string().optional(),
            "distributionChannel": t.string().optional(),
            "name": t.string().optional(),
            "iconUrl": t.string().optional(),
            "description": t.string().optional(),
            "managedProperties": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
            "recentChanges": t.string().optional(),
            "category": t.string().optional(),
            "fullDescription": t.string().optional(),
            "playStoreUrl": t.string().optional(),
            "permissions": t.array(
                t.proxy(renames["ApplicationPermissionIn"])
            ).optional(),
            "author": t.string().optional(),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "appVersions": t.array(t.proxy(renames["AppVersionOut"])).optional(),
            "availableCountries": t.array(t.string()).optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "appTracks": t.array(t.proxy(renames["AppTrackInfoOut"])).optional(),
            "title": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "appPricing": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "smallIconUrl": t.string().optional(),
            "contentRating": t.string().optional(),
            "distributionChannel": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "iconUrl": t.string().optional(),
            "description": t.string().optional(),
            "managedProperties": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "recentChanges": t.string().optional(),
            "category": t.string().optional(),
            "fullDescription": t.string().optional(),
            "playStoreUrl": t.string().optional(),
            "permissions": t.array(
                t.proxy(renames["ApplicationPermissionOut"])
            ).optional(),
            "author": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
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
    types["ApplicationReportingSettingsIn"] = t.struct(
        {"includeRemovedApps": t.boolean().optional()}
    ).named(renames["ApplicationReportingSettingsIn"])
    types["ApplicationReportingSettingsOut"] = t.struct(
        {
            "includeRemovedApps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReportingSettingsOut"])
    types["AdbShellInteractiveEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdbShellInteractiveEventIn"]
    )
    types["AdbShellInteractiveEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdbShellInteractiveEventOut"])
    types["AppTrackInfoIn"] = t.struct(
        {"trackId": t.string().optional(), "trackAlias": t.string().optional()}
    ).named(renames["AppTrackInfoIn"])
    types["AppTrackInfoOut"] = t.struct(
        {
            "trackId": t.string().optional(),
            "trackAlias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppTrackInfoOut"])
    types["ManagedPropertyEntryIn"] = t.struct(
        {"value": t.string().optional(), "name": t.string().optional()}
    ).named(renames["ManagedPropertyEntryIn"])
    types["ManagedPropertyEntryOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPropertyEntryOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["OsShutdownEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OsShutdownEventIn"]
    )
    types["OsShutdownEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OsShutdownEventOut"])
    types["DateIn"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["ListDevicesResponseIn"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDevicesResponseIn"])
    types["ListDevicesResponseOut"] = t.struct(
        {
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDevicesResponseOut"])
    types["SpecificNonComplianceContextIn"] = t.struct(
        {
            "passwordPoliciesContext": t.proxy(
                renames["PasswordPoliciesContextIn"]
            ).optional(),
            "oncWifiContext": t.proxy(renames["OncWifiContextIn"]).optional(),
        }
    ).named(renames["SpecificNonComplianceContextIn"])
    types["SpecificNonComplianceContextOut"] = t.struct(
        {
            "passwordPoliciesContext": t.proxy(
                renames["PasswordPoliciesContextOut"]
            ).optional(),
            "oncWifiContext": t.proxy(renames["OncWifiContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecificNonComplianceContextOut"])
    types["MediaMountEventIn"] = t.struct(
        {"volumeLabel": t.string().optional(), "mountPoint": t.string().optional()}
    ).named(renames["MediaMountEventIn"])
    types["MediaMountEventOut"] = t.struct(
        {
            "volumeLabel": t.string().optional(),
            "mountPoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaMountEventOut"])
    types["MemoryEventIn"] = t.struct(
        {
            "eventType": t.string().optional(),
            "createTime": t.string().optional(),
            "byteCount": t.string().optional(),
        }
    ).named(renames["MemoryEventIn"])
    types["MemoryEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "createTime": t.string().optional(),
            "byteCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryEventOut"])
    types["FreezePeriodIn"] = t.struct(
        {
            "endDate": t.proxy(renames["DateIn"]).optional(),
            "startDate": t.proxy(renames["DateIn"]).optional(),
        }
    ).named(renames["FreezePeriodIn"])
    types["FreezePeriodOut"] = t.struct(
        {
            "endDate": t.proxy(renames["DateOut"]).optional(),
            "startDate": t.proxy(renames["DateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FreezePeriodOut"])
    types["CertAuthorityRemovedEventIn"] = t.struct(
        {
            "certificate": t.string().optional(),
            "userId": t.integer().optional(),
            "success": t.boolean().optional(),
        }
    ).named(renames["CertAuthorityRemovedEventIn"])
    types["CertAuthorityRemovedEventOut"] = t.struct(
        {
            "certificate": t.string().optional(),
            "userId": t.integer().optional(),
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertAuthorityRemovedEventOut"])
    types["UsageLogEventIn"] = t.struct(
        {
            "keyguardDismissAuthAttemptEvent": t.proxy(
                renames["KeyguardDismissAuthAttemptEventIn"]
            ).optional(),
            "keyImportEvent": t.proxy(renames["KeyImportEventIn"]).optional(),
            "certAuthorityRemovedEvent": t.proxy(
                renames["CertAuthorityRemovedEventIn"]
            ).optional(),
            "connectEvent": t.proxy(renames["ConnectEventIn"]).optional(),
            "eventTime": t.string().optional(),
            "certValidationFailureEvent": t.proxy(
                renames["CertValidationFailureEventIn"]
            ).optional(),
            "mediaUnmountEvent": t.proxy(renames["MediaUnmountEventIn"]).optional(),
            "filePushedEvent": t.proxy(renames["FilePushedEventIn"]).optional(),
            "keyIntegrityViolationEvent": t.proxy(
                renames["KeyIntegrityViolationEventIn"]
            ).optional(),
            "keyguardSecuredEvent": t.proxy(
                renames["KeyguardSecuredEventIn"]
            ).optional(),
            "appProcessStartEvent": t.proxy(
                renames["AppProcessStartEventIn"]
            ).optional(),
            "loggingStoppedEvent": t.proxy(renames["LoggingStoppedEventIn"]).optional(),
            "wipeFailureEvent": t.proxy(renames["WipeFailureEventIn"]).optional(),
            "keyguardDismissedEvent": t.proxy(
                renames["KeyguardDismissedEventIn"]
            ).optional(),
            "cryptoSelfTestCompletedEvent": t.proxy(
                renames["CryptoSelfTestCompletedEventIn"]
            ).optional(),
            "filePulledEvent": t.proxy(renames["FilePulledEventIn"]).optional(),
            "osShutdownEvent": t.proxy(renames["OsShutdownEventIn"]).optional(),
            "logBufferSizeCriticalEvent": t.proxy(
                renames["LogBufferSizeCriticalEventIn"]
            ).optional(),
            "remoteLockEvent": t.proxy(renames["RemoteLockEventIn"]).optional(),
            "mediaMountEvent": t.proxy(renames["MediaMountEventIn"]).optional(),
            "loggingStartedEvent": t.proxy(renames["LoggingStartedEventIn"]).optional(),
            "dnsEvent": t.proxy(renames["DnsEventIn"]).optional(),
            "osStartupEvent": t.proxy(renames["OsStartupEventIn"]).optional(),
            "eventId": t.string().optional(),
            "keyGeneratedEvent": t.proxy(renames["KeyGeneratedEventIn"]).optional(),
            "adbShellCommandEvent": t.proxy(
                renames["AdbShellCommandEventIn"]
            ).optional(),
            "keyDestructionEvent": t.proxy(renames["KeyDestructionEventIn"]).optional(),
            "certAuthorityInstalledEvent": t.proxy(
                renames["CertAuthorityInstalledEventIn"]
            ).optional(),
            "eventType": t.string().optional(),
            "adbShellInteractiveEvent": t.proxy(
                renames["AdbShellInteractiveEventIn"]
            ).optional(),
        }
    ).named(renames["UsageLogEventIn"])
    types["UsageLogEventOut"] = t.struct(
        {
            "keyguardDismissAuthAttemptEvent": t.proxy(
                renames["KeyguardDismissAuthAttemptEventOut"]
            ).optional(),
            "keyImportEvent": t.proxy(renames["KeyImportEventOut"]).optional(),
            "certAuthorityRemovedEvent": t.proxy(
                renames["CertAuthorityRemovedEventOut"]
            ).optional(),
            "connectEvent": t.proxy(renames["ConnectEventOut"]).optional(),
            "eventTime": t.string().optional(),
            "certValidationFailureEvent": t.proxy(
                renames["CertValidationFailureEventOut"]
            ).optional(),
            "mediaUnmountEvent": t.proxy(renames["MediaUnmountEventOut"]).optional(),
            "filePushedEvent": t.proxy(renames["FilePushedEventOut"]).optional(),
            "keyIntegrityViolationEvent": t.proxy(
                renames["KeyIntegrityViolationEventOut"]
            ).optional(),
            "keyguardSecuredEvent": t.proxy(
                renames["KeyguardSecuredEventOut"]
            ).optional(),
            "appProcessStartEvent": t.proxy(
                renames["AppProcessStartEventOut"]
            ).optional(),
            "loggingStoppedEvent": t.proxy(
                renames["LoggingStoppedEventOut"]
            ).optional(),
            "wipeFailureEvent": t.proxy(renames["WipeFailureEventOut"]).optional(),
            "keyguardDismissedEvent": t.proxy(
                renames["KeyguardDismissedEventOut"]
            ).optional(),
            "cryptoSelfTestCompletedEvent": t.proxy(
                renames["CryptoSelfTestCompletedEventOut"]
            ).optional(),
            "filePulledEvent": t.proxy(renames["FilePulledEventOut"]).optional(),
            "osShutdownEvent": t.proxy(renames["OsShutdownEventOut"]).optional(),
            "logBufferSizeCriticalEvent": t.proxy(
                renames["LogBufferSizeCriticalEventOut"]
            ).optional(),
            "remoteLockEvent": t.proxy(renames["RemoteLockEventOut"]).optional(),
            "mediaMountEvent": t.proxy(renames["MediaMountEventOut"]).optional(),
            "loggingStartedEvent": t.proxy(
                renames["LoggingStartedEventOut"]
            ).optional(),
            "dnsEvent": t.proxy(renames["DnsEventOut"]).optional(),
            "osStartupEvent": t.proxy(renames["OsStartupEventOut"]).optional(),
            "eventId": t.string().optional(),
            "keyGeneratedEvent": t.proxy(renames["KeyGeneratedEventOut"]).optional(),
            "adbShellCommandEvent": t.proxy(
                renames["AdbShellCommandEventOut"]
            ).optional(),
            "keyDestructionEvent": t.proxy(
                renames["KeyDestructionEventOut"]
            ).optional(),
            "certAuthorityInstalledEvent": t.proxy(
                renames["CertAuthorityInstalledEventOut"]
            ).optional(),
            "eventType": t.string().optional(),
            "adbShellInteractiveEvent": t.proxy(
                renames["AdbShellInteractiveEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageLogEventOut"])
    types["DnsEventIn"] = t.struct(
        {
            "totalIpAddressesReturned": t.string().optional(),
            "packageName": t.string().optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "hostname": t.string().optional(),
        }
    ).named(renames["DnsEventIn"])
    types["DnsEventOut"] = t.struct(
        {
            "totalIpAddressesReturned": t.string().optional(),
            "packageName": t.string().optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "hostname": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsEventOut"])
    types["EnterpriseIn"] = t.struct(
        {
            "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
            "pubsubTopic": t.string().optional(),
            "appAutoApprovalEnabled": t.boolean().optional(),
            "logo": t.proxy(renames["ExternalDataIn"]).optional(),
            "enterpriseDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "primaryColor": t.integer().optional(),
            "termsAndConditions": t.array(
                t.proxy(renames["TermsAndConditionsIn"])
            ).optional(),
            "enabledNotificationTypes": t.array(t.string()).optional(),
            "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
        }
    ).named(renames["EnterpriseIn"])
    types["EnterpriseOut"] = t.struct(
        {
            "contactInfo": t.proxy(renames["ContactInfoOut"]).optional(),
            "pubsubTopic": t.string().optional(),
            "appAutoApprovalEnabled": t.boolean().optional(),
            "logo": t.proxy(renames["ExternalDataOut"]).optional(),
            "enterpriseDisplayName": t.string().optional(),
            "name": t.string().optional(),
            "primaryColor": t.integer().optional(),
            "termsAndConditions": t.array(
                t.proxy(renames["TermsAndConditionsOut"])
            ).optional(),
            "enabledNotificationTypes": t.array(t.string()).optional(),
            "signinDetails": t.array(t.proxy(renames["SigninDetailOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseOut"])
    types["LoggingStartedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoggingStartedEventIn"]
    )
    types["LoggingStartedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoggingStartedEventOut"])
    types["DeviceSettingsIn"] = t.struct(
        {
            "isEncrypted": t.boolean().optional(),
            "developmentSettingsEnabled": t.boolean().optional(),
            "unknownSourcesEnabled": t.boolean().optional(),
            "isDeviceSecure": t.boolean().optional(),
            "adbEnabled": t.boolean().optional(),
            "encryptionStatus": t.string().optional(),
            "verifyAppsEnabled": t.boolean().optional(),
        }
    ).named(renames["DeviceSettingsIn"])
    types["DeviceSettingsOut"] = t.struct(
        {
            "isEncrypted": t.boolean().optional(),
            "developmentSettingsEnabled": t.boolean().optional(),
            "unknownSourcesEnabled": t.boolean().optional(),
            "isDeviceSecure": t.boolean().optional(),
            "adbEnabled": t.boolean().optional(),
            "encryptionStatus": t.string().optional(),
            "verifyAppsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSettingsOut"])
    types["RemoteLockEventIn"] = t.struct(
        {
            "targetUserId": t.integer().optional(),
            "adminUserId": t.integer().optional(),
            "adminPackageName": t.string().optional(),
        }
    ).named(renames["RemoteLockEventIn"])
    types["RemoteLockEventOut"] = t.struct(
        {
            "targetUserId": t.integer().optional(),
            "adminUserId": t.integer().optional(),
            "adminPackageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteLockEventOut"])
    types["PackageNameListIn"] = t.struct(
        {"packageNames": t.array(t.string()).optional()}
    ).named(renames["PackageNameListIn"])
    types["PackageNameListOut"] = t.struct(
        {
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageNameListOut"])
    types["ApplicationPermissionIn"] = t.struct(
        {
            "permissionId": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApplicationPermissionIn"])
    types["ApplicationPermissionOut"] = t.struct(
        {
            "permissionId": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationPermissionOut"])
    types["BlockActionIn"] = t.struct(
        {"blockScope": t.string().optional(), "blockAfterDays": t.integer().optional()}
    ).named(renames["BlockActionIn"])
    types["BlockActionOut"] = t.struct(
        {
            "blockScope": t.string().optional(),
            "blockAfterDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BlockActionOut"])
    types["SetupActionIn"] = t.struct(
        {
            "title": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "description": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "launchApp": t.proxy(renames["LaunchAppActionIn"]).optional(),
        }
    ).named(renames["SetupActionIn"])
    types["SetupActionOut"] = t.struct(
        {
            "title": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "description": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "launchApp": t.proxy(renames["LaunchAppActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetupActionOut"])
    types["AppVersionIn"] = t.struct(
        {
            "production": t.boolean().optional(),
            "trackIds": t.array(t.string()).optional(),
            "versionCode": t.integer().optional(),
            "versionString": t.string().optional(),
        }
    ).named(renames["AppVersionIn"])
    types["AppVersionOut"] = t.struct(
        {
            "production": t.boolean().optional(),
            "trackIds": t.array(t.string()).optional(),
            "versionCode": t.integer().optional(),
            "versionString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppVersionOut"])
    types["WebTokenIn"] = t.struct(
        {
            "value": t.string().optional(),
            "parentFrameUrl": t.string().optional(),
            "enabledFeatures": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
        }
    ).named(renames["WebTokenIn"])
    types["WebTokenOut"] = t.struct(
        {
            "value": t.string().optional(),
            "parentFrameUrl": t.string().optional(),
            "enabledFeatures": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebTokenOut"])
    types["ApplicationPolicyIn"] = t.struct(
        {
            "delegatedScopes": t.array(t.string()).optional(),
            "alwaysOnVpnLockdownExemption": t.string().optional(),
            "packageName": t.string().optional(),
            "disabled": t.boolean().optional(),
            "connectedWorkAndPersonalApp": t.string().optional(),
            "autoUpdateMode": t.string().optional(),
            "installType": t.string().optional(),
            "extensionConfig": t.proxy(renames["ExtensionConfigIn"]).optional(),
            "workProfileWidgets": t.string().optional(),
            "lockTaskAllowed": t.boolean().optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantIn"])
            ).optional(),
            "managedConfigurationTemplate": t.proxy(
                renames["ManagedConfigurationTemplateIn"]
            ).optional(),
            "minimumVersionCode": t.integer().optional(),
            "managedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "accessibleTrackIds": t.array(t.string()).optional(),
        }
    ).named(renames["ApplicationPolicyIn"])
    types["ApplicationPolicyOut"] = t.struct(
        {
            "delegatedScopes": t.array(t.string()).optional(),
            "alwaysOnVpnLockdownExemption": t.string().optional(),
            "packageName": t.string().optional(),
            "disabled": t.boolean().optional(),
            "connectedWorkAndPersonalApp": t.string().optional(),
            "autoUpdateMode": t.string().optional(),
            "installType": t.string().optional(),
            "extensionConfig": t.proxy(renames["ExtensionConfigOut"]).optional(),
            "workProfileWidgets": t.string().optional(),
            "lockTaskAllowed": t.boolean().optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantOut"])
            ).optional(),
            "managedConfigurationTemplate": t.proxy(
                renames["ManagedConfigurationTemplateOut"]
            ).optional(),
            "minimumVersionCode": t.integer().optional(),
            "managedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "accessibleTrackIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationPolicyOut"])
    types["ExtensionConfigIn"] = t.struct(
        {
            "notificationReceiver": t.string().optional(),
            "signingKeyFingerprintsSha256": t.array(t.string()).optional(),
        }
    ).named(renames["ExtensionConfigIn"])
    types["ExtensionConfigOut"] = t.struct(
        {
            "notificationReceiver": t.string().optional(),
            "signingKeyFingerprintsSha256": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtensionConfigOut"])
    types["BatchUsageLogEventsIn"] = t.struct(
        {
            "usageLogEvents": t.array(t.proxy(renames["UsageLogEventIn"])).optional(),
            "device": t.string().optional(),
            "user": t.string().optional(),
            "retrievalTime": t.string().optional(),
        }
    ).named(renames["BatchUsageLogEventsIn"])
    types["BatchUsageLogEventsOut"] = t.struct(
        {
            "usageLogEvents": t.array(t.proxy(renames["UsageLogEventOut"])).optional(),
            "device": t.string().optional(),
            "user": t.string().optional(),
            "retrievalTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUsageLogEventsOut"])
    types["SignupUrlIn"] = t.struct(
        {"url": t.string().optional(), "name": t.string().optional()}
    ).named(renames["SignupUrlIn"])
    types["SignupUrlOut"] = t.struct(
        {
            "url": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignupUrlOut"])
    types["WipeFailureEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WipeFailureEventIn"]
    )
    types["WipeFailureEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WipeFailureEventOut"])
    types["KeyguardDismissAuthAttemptEventIn"] = t.struct(
        {
            "strongAuthMethodUsed": t.boolean().optional(),
            "success": t.boolean().optional(),
        }
    ).named(renames["KeyguardDismissAuthAttemptEventIn"])
    types["KeyguardDismissAuthAttemptEventOut"] = t.struct(
        {
            "strongAuthMethodUsed": t.boolean().optional(),
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyguardDismissAuthAttemptEventOut"])
    types["ContentProviderEndpointIn"] = t.struct(
        {
            "signingCertsSha256": t.array(t.string()),
            "packageName": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["ContentProviderEndpointIn"])
    types["ContentProviderEndpointOut"] = t.struct(
        {
            "signingCertsSha256": t.array(t.string()),
            "packageName": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentProviderEndpointOut"])
    types["WebAppIconIn"] = t.struct({"imageData": t.string().optional()}).named(
        renames["WebAppIconIn"]
    )
    types["WebAppIconOut"] = t.struct(
        {
            "imageData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppIconOut"])
    types["TermsAndConditionsIn"] = t.struct(
        {
            "header": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "content": t.proxy(renames["UserFacingMessageIn"]).optional(),
        }
    ).named(renames["TermsAndConditionsIn"])
    types["TermsAndConditionsOut"] = t.struct(
        {
            "header": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "content": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TermsAndConditionsOut"])
    types["PowerManagementEventIn"] = t.struct(
        {
            "eventType": t.string().optional(),
            "createTime": t.string().optional(),
            "batteryLevel": t.number().optional(),
        }
    ).named(renames["PowerManagementEventIn"])
    types["PowerManagementEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "createTime": t.string().optional(),
            "batteryLevel": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PowerManagementEventOut"])
    types["KeyDestructionEventIn"] = t.struct(
        {
            "keyAlias": t.string().optional(),
            "success": t.boolean().optional(),
            "applicationUid": t.integer().optional(),
        }
    ).named(renames["KeyDestructionEventIn"])
    types["KeyDestructionEventOut"] = t.struct(
        {
            "keyAlias": t.string().optional(),
            "success": t.boolean().optional(),
            "applicationUid": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyDestructionEventOut"])
    types["CommonCriteriaModeInfoIn"] = t.struct(
        {"commonCriteriaModeStatus": t.string().optional()}
    ).named(renames["CommonCriteriaModeInfoIn"])
    types["CommonCriteriaModeInfoOut"] = t.struct(
        {
            "commonCriteriaModeStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonCriteriaModeInfoOut"])
    types["SigninDetailIn"] = t.struct(
        {
            "qrCode": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "signinEnrollmentToken": t.string().optional(),
            "signinUrl": t.string().optional(),
        }
    ).named(renames["SigninDetailIn"])
    types["SigninDetailOut"] = t.struct(
        {
            "qrCode": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "signinEnrollmentToken": t.string().optional(),
            "signinUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SigninDetailOut"])
    types["CrossProfilePoliciesIn"] = t.struct(
        {
            "crossProfileCopyPaste": t.string().optional(),
            "workProfileWidgetsDefault": t.string().optional(),
            "showWorkContactsInPersonalProfile": t.string().optional(),
            "crossProfileDataSharing": t.string().optional(),
        }
    ).named(renames["CrossProfilePoliciesIn"])
    types["CrossProfilePoliciesOut"] = t.struct(
        {
            "crossProfileCopyPaste": t.string().optional(),
            "workProfileWidgetsDefault": t.string().optional(),
            "showWorkContactsInPersonalProfile": t.string().optional(),
            "crossProfileDataSharing": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrossProfilePoliciesOut"])
    types["MediaUnmountEventIn"] = t.struct(
        {"mountPoint": t.string().optional(), "volumeLabel": t.string().optional()}
    ).named(renames["MediaUnmountEventIn"])
    types["MediaUnmountEventOut"] = t.struct(
        {
            "mountPoint": t.string().optional(),
            "volumeLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaUnmountEventOut"])
    types["ApplicationReportIn"] = t.struct(
        {
            "installerPackageName": t.string().optional(),
            "packageSha256Hash": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "applicationSource": t.string().optional(),
            "signingKeyCertFingerprints": t.array(t.string()).optional(),
            "versionCode": t.integer().optional(),
            "packageName": t.string().optional(),
            "versionName": t.string().optional(),
            "events": t.array(t.proxy(renames["ApplicationEventIn"])).optional(),
            "keyedAppStates": t.array(t.proxy(renames["KeyedAppStateIn"])).optional(),
        }
    ).named(renames["ApplicationReportIn"])
    types["ApplicationReportOut"] = t.struct(
        {
            "installerPackageName": t.string().optional(),
            "packageSha256Hash": t.string().optional(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "applicationSource": t.string().optional(),
            "signingKeyCertFingerprints": t.array(t.string()).optional(),
            "versionCode": t.integer().optional(),
            "packageName": t.string().optional(),
            "versionName": t.string().optional(),
            "events": t.array(t.proxy(renames["ApplicationEventOut"])).optional(),
            "keyedAppStates": t.array(t.proxy(renames["KeyedAppStateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReportOut"])
    types["AppProcessStartEventIn"] = t.struct(
        {"processInfo": t.proxy(renames["AppProcessInfoIn"]).optional()}
    ).named(renames["AppProcessStartEventIn"])
    types["AppProcessStartEventOut"] = t.struct(
        {
            "processInfo": t.proxy(renames["AppProcessInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProcessStartEventOut"])
    types["StatusReportingSettingsIn"] = t.struct(
        {
            "softwareInfoEnabled": t.boolean().optional(),
            "applicationReportsEnabled": t.boolean().optional(),
            "hardwareStatusEnabled": t.boolean().optional(),
            "displayInfoEnabled": t.boolean().optional(),
            "commonCriteriaModeEnabled": t.boolean().optional(),
            "systemPropertiesEnabled": t.boolean().optional(),
            "powerManagementEventsEnabled": t.boolean().optional(),
            "deviceSettingsEnabled": t.boolean().optional(),
            "applicationReportingSettings": t.proxy(
                renames["ApplicationReportingSettingsIn"]
            ).optional(),
            "memoryInfoEnabled": t.boolean().optional(),
            "networkInfoEnabled": t.boolean().optional(),
        }
    ).named(renames["StatusReportingSettingsIn"])
    types["StatusReportingSettingsOut"] = t.struct(
        {
            "softwareInfoEnabled": t.boolean().optional(),
            "applicationReportsEnabled": t.boolean().optional(),
            "hardwareStatusEnabled": t.boolean().optional(),
            "displayInfoEnabled": t.boolean().optional(),
            "commonCriteriaModeEnabled": t.boolean().optional(),
            "systemPropertiesEnabled": t.boolean().optional(),
            "powerManagementEventsEnabled": t.boolean().optional(),
            "deviceSettingsEnabled": t.boolean().optional(),
            "applicationReportingSettings": t.proxy(
                renames["ApplicationReportingSettingsOut"]
            ).optional(),
            "memoryInfoEnabled": t.boolean().optional(),
            "networkInfoEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusReportingSettingsOut"])
    types["LaunchAppActionIn"] = t.struct({"packageName": t.string().optional()}).named(
        renames["LaunchAppActionIn"]
    )
    types["LaunchAppActionOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchAppActionOut"])
    types["HardwareInfoIn"] = t.struct(
        {
            "deviceBasebandVersion": t.string().optional(),
            "batteryThrottlingTemperatures": t.array(t.number()).optional(),
            "cpuThrottlingTemperatures": t.array(t.number()).optional(),
            "cpuShutdownTemperatures": t.array(t.number()).optional(),
            "gpuThrottlingTemperatures": t.array(t.number()).optional(),
            "serialNumber": t.string().optional(),
            "model": t.string().optional(),
            "gpuShutdownTemperatures": t.array(t.number()).optional(),
            "batteryShutdownTemperatures": t.array(t.number()).optional(),
            "skinThrottlingTemperatures": t.array(t.number()).optional(),
            "manufacturer": t.string().optional(),
            "brand": t.string().optional(),
            "skinShutdownTemperatures": t.array(t.number()).optional(),
            "hardware": t.string().optional(),
        }
    ).named(renames["HardwareInfoIn"])
    types["HardwareInfoOut"] = t.struct(
        {
            "deviceBasebandVersion": t.string().optional(),
            "batteryThrottlingTemperatures": t.array(t.number()).optional(),
            "cpuThrottlingTemperatures": t.array(t.number()).optional(),
            "cpuShutdownTemperatures": t.array(t.number()).optional(),
            "gpuThrottlingTemperatures": t.array(t.number()).optional(),
            "serialNumber": t.string().optional(),
            "model": t.string().optional(),
            "gpuShutdownTemperatures": t.array(t.number()).optional(),
            "batteryShutdownTemperatures": t.array(t.number()).optional(),
            "skinThrottlingTemperatures": t.array(t.number()).optional(),
            "manufacturer": t.string().optional(),
            "brand": t.string().optional(),
            "skinShutdownTemperatures": t.array(t.number()).optional(),
            "enterpriseSpecificId": t.string().optional(),
            "hardware": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HardwareInfoOut"])
    types["FilePulledEventIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FilePulledEventIn"]
    )
    types["FilePulledEventOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilePulledEventOut"])
    types["UsageLogIn"] = t.struct(
        {
            "enabledLogTypes": t.array(t.string()).optional(),
            "uploadOnCellularAllowed": t.array(t.string()).optional(),
        }
    ).named(renames["UsageLogIn"])
    types["UsageLogOut"] = t.struct(
        {
            "enabledLogTypes": t.array(t.string()).optional(),
            "uploadOnCellularAllowed": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageLogOut"])
    types["HardwareStatusIn"] = t.struct(
        {
            "skinTemperatures": t.array(t.number()).optional(),
            "gpuTemperatures": t.array(t.number()).optional(),
            "cpuUsages": t.array(t.number()).optional(),
            "createTime": t.string().optional(),
            "fanSpeeds": t.array(t.number()).optional(),
            "batteryTemperatures": t.array(t.number()).optional(),
            "cpuTemperatures": t.array(t.number()).optional(),
        }
    ).named(renames["HardwareStatusIn"])
    types["HardwareStatusOut"] = t.struct(
        {
            "skinTemperatures": t.array(t.number()).optional(),
            "gpuTemperatures": t.array(t.number()).optional(),
            "cpuUsages": t.array(t.number()).optional(),
            "createTime": t.string().optional(),
            "fanSpeeds": t.array(t.number()).optional(),
            "batteryTemperatures": t.array(t.number()).optional(),
            "cpuTemperatures": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HardwareStatusOut"])
    types["ListPoliciesResponseIn"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["PolicyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListPoliciesResponseIn"])
    types["ListPoliciesResponseOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["PolicyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPoliciesResponseOut"])
    types["PermissionGrantIn"] = t.struct(
        {"permission": t.string().optional(), "policy": t.string().optional()}
    ).named(renames["PermissionGrantIn"])
    types["PermissionGrantOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "policy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionGrantOut"])
    types["ConnectEventIn"] = t.struct(
        {
            "destinationIpAddress": t.string().optional(),
            "packageName": t.string().optional(),
            "destinationPort": t.integer().optional(),
        }
    ).named(renames["ConnectEventIn"])
    types["ConnectEventOut"] = t.struct(
        {
            "destinationIpAddress": t.string().optional(),
            "packageName": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectEventOut"])
    types["SoftwareInfoIn"] = t.struct(
        {
            "androidDevicePolicyVersionName": t.string().optional(),
            "deviceBuildSignature": t.string().optional(),
            "primaryLanguageCode": t.string().optional(),
            "androidBuildNumber": t.string().optional(),
            "androidBuildTime": t.string().optional(),
            "securityPatchLevel": t.string().optional(),
            "androidDevicePolicyVersionCode": t.integer().optional(),
            "deviceKernelVersion": t.string().optional(),
            "bootloaderVersion": t.string().optional(),
            "androidVersion": t.string().optional(),
            "systemUpdateInfo": t.proxy(renames["SystemUpdateInfoIn"]).optional(),
        }
    ).named(renames["SoftwareInfoIn"])
    types["SoftwareInfoOut"] = t.struct(
        {
            "androidDevicePolicyVersionName": t.string().optional(),
            "deviceBuildSignature": t.string().optional(),
            "primaryLanguageCode": t.string().optional(),
            "androidBuildNumber": t.string().optional(),
            "androidBuildTime": t.string().optional(),
            "securityPatchLevel": t.string().optional(),
            "androidDevicePolicyVersionCode": t.integer().optional(),
            "deviceKernelVersion": t.string().optional(),
            "bootloaderVersion": t.string().optional(),
            "androidVersion": t.string().optional(),
            "systemUpdateInfo": t.proxy(renames["SystemUpdateInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareInfoOut"])
    types["SystemUpdateInfoIn"] = t.struct(
        {
            "updateStatus": t.string().optional(),
            "updateReceivedTime": t.string().optional(),
        }
    ).named(renames["SystemUpdateInfoIn"])
    types["SystemUpdateInfoOut"] = t.struct(
        {
            "updateStatus": t.string().optional(),
            "updateReceivedTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemUpdateInfoOut"])
    types["MemoryInfoIn"] = t.struct(
        {
            "totalInternalStorage": t.string().optional(),
            "totalRam": t.string().optional(),
        }
    ).named(renames["MemoryInfoIn"])
    types["MemoryInfoOut"] = t.struct(
        {
            "totalInternalStorage": t.string().optional(),
            "totalRam": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryInfoOut"])
    types["SecurityPostureIn"] = t.struct(
        {
            "devicePosture": t.string().optional(),
            "postureDetails": t.array(t.proxy(renames["PostureDetailIn"])).optional(),
        }
    ).named(renames["SecurityPostureIn"])
    types["SecurityPostureOut"] = t.struct(
        {
            "devicePosture": t.string().optional(),
            "postureDetails": t.array(t.proxy(renames["PostureDetailOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityPostureOut"])
    types["ChoosePrivateKeyRuleIn"] = t.struct(
        {
            "urlPattern": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
            "privateKeyAlias": t.string().optional(),
        }
    ).named(renames["ChoosePrivateKeyRuleIn"])
    types["ChoosePrivateKeyRuleOut"] = t.struct(
        {
            "urlPattern": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
            "privateKeyAlias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChoosePrivateKeyRuleOut"])
    types["ExternalDataIn"] = t.struct(
        {"sha256Hash": t.string().optional(), "url": t.string().optional()}
    ).named(renames["ExternalDataIn"])
    types["ExternalDataOut"] = t.struct(
        {
            "sha256Hash": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalDataOut"])
    types["NetworkInfoIn"] = t.struct(
        {
            "networkOperatorName": t.string().optional(),
            "meid": t.string().optional(),
            "wifiMacAddress": t.string().optional(),
            "telephonyInfos": t.array(t.proxy(renames["TelephonyInfoIn"])).optional(),
            "imei": t.string().optional(),
        }
    ).named(renames["NetworkInfoIn"])
    types["NetworkInfoOut"] = t.struct(
        {
            "networkOperatorName": t.string().optional(),
            "meid": t.string().optional(),
            "wifiMacAddress": t.string().optional(),
            "telephonyInfos": t.array(t.proxy(renames["TelephonyInfoOut"])).optional(),
            "imei": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInfoOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["PersonalApplicationPolicyIn"] = t.struct(
        {"installType": t.string().optional(), "packageName": t.string().optional()}
    ).named(renames["PersonalApplicationPolicyIn"])
    types["PersonalApplicationPolicyOut"] = t.struct(
        {
            "installType": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalApplicationPolicyOut"])
    types["KeyImportEventIn"] = t.struct(
        {
            "applicationUid": t.integer().optional(),
            "keyAlias": t.string().optional(),
            "success": t.boolean().optional(),
        }
    ).named(renames["KeyImportEventIn"])
    types["KeyImportEventOut"] = t.struct(
        {
            "applicationUid": t.integer().optional(),
            "keyAlias": t.string().optional(),
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyImportEventOut"])
    types["WebAppIn"] = t.struct(
        {
            "versionCode": t.string().optional(),
            "startUrl": t.string().optional(),
            "title": t.string().optional(),
            "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
            "name": t.string().optional(),
            "displayMode": t.string().optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "versionCode": t.string().optional(),
            "startUrl": t.string().optional(),
            "title": t.string().optional(),
            "icons": t.array(t.proxy(renames["WebAppIconOut"])).optional(),
            "name": t.string().optional(),
            "displayMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
    types["AdbShellCommandEventIn"] = t.struct(
        {"shellCmd": t.string().optional()}
    ).named(renames["AdbShellCommandEventIn"])
    types["AdbShellCommandEventOut"] = t.struct(
        {
            "shellCmd": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdbShellCommandEventOut"])
    types["OsStartupEventIn"] = t.struct(
        {
            "verityMode": t.string().optional(),
            "verifiedBootState": t.string().optional(),
        }
    ).named(renames["OsStartupEventIn"])
    types["OsStartupEventOut"] = t.struct(
        {
            "verityMode": t.string().optional(),
            "verifiedBootState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsStartupEventOut"])
    types["PolicyIn"] = t.struct(
        {
            "vpnConfigDisabled": t.boolean().optional(),
            "crossProfilePolicies": t.proxy(
                renames["CrossProfilePoliciesIn"]
            ).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "factoryResetDisabled": t.boolean().optional(),
            "keyguardDisabledFeatures": t.array(t.string()).optional(),
            "mobileNetworksConfigDisabled": t.boolean().optional(),
            "setWallpaperDisabled": t.boolean().optional(),
            "funDisabled": t.boolean().optional(),
            "permittedInputMethods": t.proxy(renames["PackageNameListIn"]).optional(),
            "outgoingBeamDisabled": t.boolean().optional(),
            "appAutoUpdatePolicy": t.string().optional(),
            "adjustVolumeDisabled": t.boolean().optional(),
            "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
            "microphoneAccess": t.string().optional(),
            "usbFileTransferDisabled": t.boolean().optional(),
            "autoDateAndTimeZone": t.string().optional(),
            "installAppsDisabled": t.boolean().optional(),
            "encryptionPolicy": t.string().optional(),
            "locationMode": t.string().optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "passwordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsIn"])
            ).optional(),
            "keyguardDisabled": t.boolean().optional(),
            "maximumTimeToLock": t.string().optional(),
            "bluetoothConfigDisabled": t.boolean().optional(),
            "longSupportMessage": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "cellBroadcastsConfigDisabled": t.boolean().optional(),
            "applications": t.array(t.proxy(renames["ApplicationPolicyIn"])).optional(),
            "permittedAccessibilityServices": t.proxy(
                renames["PackageNameListIn"]
            ).optional(),
            "minimumApiLevel": t.integer().optional(),
            "autoTimeRequired": t.boolean().optional(),
            "playStoreMode": t.string().optional(),
            "safeBootDisabled": t.boolean().optional(),
            "credentialsConfigDisabled": t.boolean().optional(),
            "ensureVerifyAppsEnabled": t.boolean().optional(),
            "statusReportingSettings": t.proxy(
                renames["StatusReportingSettingsIn"]
            ).optional(),
            "wifiConfigsLockdownEnabled": t.boolean().optional(),
            "networkResetDisabled": t.boolean().optional(),
            "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
            "shareLocationDisabled": t.boolean().optional(),
            "setUserIconDisabled": t.boolean().optional(),
            "createWindowsDisabled": t.boolean().optional(),
            "dataRoamingDisabled": t.boolean().optional(),
            "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
            "addUserDisabled": t.boolean().optional(),
            "modifyAccountsDisabled": t.boolean().optional(),
            "tetheringConfigDisabled": t.boolean().optional(),
            "oncCertificateProviders": t.array(
                t.proxy(renames["OncCertificateProviderIn"])
            ).optional(),
            "privateKeySelectionEnabled": t.boolean().optional(),
            "outgoingCallsDisabled": t.boolean().optional(),
            "statusBarDisabled": t.boolean().optional(),
            "persistentPreferredActivities": t.array(
                t.proxy(renames["PersistentPreferredActivityIn"])
            ).optional(),
            "bluetoothDisabled": t.boolean().optional(),
            "kioskCustomization": t.proxy(renames["KioskCustomizationIn"]).optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantIn"])
            ).optional(),
            "skipFirstUseHintsEnabled": t.boolean().optional(),
            "kioskCustomLauncherEnabled": t.boolean().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "wifiConfigDisabled": t.boolean().optional(),
            "networkEscapeHatchEnabled": t.boolean().optional(),
            "deviceOwnerLockScreenInfo": t.proxy(
                renames["UserFacingMessageIn"]
            ).optional(),
            "name": t.string().optional(),
            "complianceRules": t.array(t.proxy(renames["ComplianceRuleIn"])).optional(),
            "installUnknownSourcesAllowed": t.boolean().optional(),
            "shortSupportMessage": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "mountPhysicalMediaDisabled": t.boolean().optional(),
            "alwaysOnVpnPackage": t.proxy(renames["AlwaysOnVpnPackageIn"]).optional(),
            "usbMassStorageEnabled": t.boolean().optional(),
            "advancedSecurityOverrides": t.proxy(
                renames["AdvancedSecurityOverridesIn"]
            ).optional(),
            "openNetworkConfiguration": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "version": t.string().optional(),
            "personalUsagePolicies": t.proxy(
                renames["PersonalUsagePoliciesIn"]
            ).optional(),
            "debuggingFeaturesAllowed": t.boolean().optional(),
            "blockApplicationsEnabled": t.boolean().optional(),
            "frpAdminEmails": t.array(t.string()).optional(),
            "smsDisabled": t.boolean().optional(),
            "passwordRequirements": t.proxy(
                renames["PasswordRequirementsIn"]
            ).optional(),
            "policyEnforcementRules": t.array(
                t.proxy(renames["PolicyEnforcementRuleIn"])
            ).optional(),
            "preferentialNetworkService": t.string().optional(),
            "stayOnPluggedModes": t.array(t.string()).optional(),
            "androidDevicePolicyTracks": t.array(t.string()).optional(),
            "unmuteMicrophoneDisabled": t.boolean().optional(),
            "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
            "choosePrivateKeyRules": t.array(
                t.proxy(renames["ChoosePrivateKeyRuleIn"])
            ).optional(),
            "bluetoothContactSharingDisabled": t.boolean().optional(),
            "uninstallAppsDisabled": t.boolean().optional(),
            "removeUserDisabled": t.boolean().optional(),
            "cameraDisabled": t.boolean().optional(),
            "cameraAccess": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "vpnConfigDisabled": t.boolean().optional(),
            "crossProfilePolicies": t.proxy(
                renames["CrossProfilePoliciesOut"]
            ).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "factoryResetDisabled": t.boolean().optional(),
            "keyguardDisabledFeatures": t.array(t.string()).optional(),
            "mobileNetworksConfigDisabled": t.boolean().optional(),
            "setWallpaperDisabled": t.boolean().optional(),
            "funDisabled": t.boolean().optional(),
            "permittedInputMethods": t.proxy(renames["PackageNameListOut"]).optional(),
            "outgoingBeamDisabled": t.boolean().optional(),
            "appAutoUpdatePolicy": t.string().optional(),
            "adjustVolumeDisabled": t.boolean().optional(),
            "usageLog": t.proxy(renames["UsageLogOut"]).optional(),
            "microphoneAccess": t.string().optional(),
            "usbFileTransferDisabled": t.boolean().optional(),
            "autoDateAndTimeZone": t.string().optional(),
            "installAppsDisabled": t.boolean().optional(),
            "encryptionPolicy": t.string().optional(),
            "locationMode": t.string().optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "passwordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsOut"])
            ).optional(),
            "keyguardDisabled": t.boolean().optional(),
            "maximumTimeToLock": t.string().optional(),
            "bluetoothConfigDisabled": t.boolean().optional(),
            "longSupportMessage": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "cellBroadcastsConfigDisabled": t.boolean().optional(),
            "applications": t.array(
                t.proxy(renames["ApplicationPolicyOut"])
            ).optional(),
            "permittedAccessibilityServices": t.proxy(
                renames["PackageNameListOut"]
            ).optional(),
            "minimumApiLevel": t.integer().optional(),
            "autoTimeRequired": t.boolean().optional(),
            "playStoreMode": t.string().optional(),
            "safeBootDisabled": t.boolean().optional(),
            "credentialsConfigDisabled": t.boolean().optional(),
            "ensureVerifyAppsEnabled": t.boolean().optional(),
            "statusReportingSettings": t.proxy(
                renames["StatusReportingSettingsOut"]
            ).optional(),
            "wifiConfigsLockdownEnabled": t.boolean().optional(),
            "networkResetDisabled": t.boolean().optional(),
            "recommendedGlobalProxy": t.proxy(renames["ProxyInfoOut"]).optional(),
            "shareLocationDisabled": t.boolean().optional(),
            "setUserIconDisabled": t.boolean().optional(),
            "createWindowsDisabled": t.boolean().optional(),
            "dataRoamingDisabled": t.boolean().optional(),
            "setupActions": t.array(t.proxy(renames["SetupActionOut"])).optional(),
            "addUserDisabled": t.boolean().optional(),
            "modifyAccountsDisabled": t.boolean().optional(),
            "tetheringConfigDisabled": t.boolean().optional(),
            "oncCertificateProviders": t.array(
                t.proxy(renames["OncCertificateProviderOut"])
            ).optional(),
            "privateKeySelectionEnabled": t.boolean().optional(),
            "outgoingCallsDisabled": t.boolean().optional(),
            "statusBarDisabled": t.boolean().optional(),
            "persistentPreferredActivities": t.array(
                t.proxy(renames["PersistentPreferredActivityOut"])
            ).optional(),
            "bluetoothDisabled": t.boolean().optional(),
            "kioskCustomization": t.proxy(renames["KioskCustomizationOut"]).optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantOut"])
            ).optional(),
            "skipFirstUseHintsEnabled": t.boolean().optional(),
            "kioskCustomLauncherEnabled": t.boolean().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "wifiConfigDisabled": t.boolean().optional(),
            "networkEscapeHatchEnabled": t.boolean().optional(),
            "deviceOwnerLockScreenInfo": t.proxy(
                renames["UserFacingMessageOut"]
            ).optional(),
            "name": t.string().optional(),
            "complianceRules": t.array(
                t.proxy(renames["ComplianceRuleOut"])
            ).optional(),
            "installUnknownSourcesAllowed": t.boolean().optional(),
            "shortSupportMessage": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "mountPhysicalMediaDisabled": t.boolean().optional(),
            "alwaysOnVpnPackage": t.proxy(renames["AlwaysOnVpnPackageOut"]).optional(),
            "usbMassStorageEnabled": t.boolean().optional(),
            "advancedSecurityOverrides": t.proxy(
                renames["AdvancedSecurityOverridesOut"]
            ).optional(),
            "openNetworkConfiguration": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "version": t.string().optional(),
            "personalUsagePolicies": t.proxy(
                renames["PersonalUsagePoliciesOut"]
            ).optional(),
            "debuggingFeaturesAllowed": t.boolean().optional(),
            "blockApplicationsEnabled": t.boolean().optional(),
            "frpAdminEmails": t.array(t.string()).optional(),
            "smsDisabled": t.boolean().optional(),
            "passwordRequirements": t.proxy(
                renames["PasswordRequirementsOut"]
            ).optional(),
            "policyEnforcementRules": t.array(
                t.proxy(renames["PolicyEnforcementRuleOut"])
            ).optional(),
            "preferentialNetworkService": t.string().optional(),
            "stayOnPluggedModes": t.array(t.string()).optional(),
            "androidDevicePolicyTracks": t.array(t.string()).optional(),
            "unmuteMicrophoneDisabled": t.boolean().optional(),
            "systemUpdate": t.proxy(renames["SystemUpdateOut"]).optional(),
            "choosePrivateKeyRules": t.array(
                t.proxy(renames["ChoosePrivateKeyRuleOut"])
            ).optional(),
            "bluetoothContactSharingDisabled": t.boolean().optional(),
            "uninstallAppsDisabled": t.boolean().optional(),
            "removeUserDisabled": t.boolean().optional(),
            "cameraDisabled": t.boolean().optional(),
            "cameraAccess": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["IssueCommandResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IssueCommandResponseIn"]
    )
    types["IssueCommandResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IssueCommandResponseOut"])
    types["ApplicationEventIn"] = t.struct(
        {"eventType": t.string().optional(), "createTime": t.string().optional()}
    ).named(renames["ApplicationEventIn"])
    types["ApplicationEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationEventOut"])
    types["AdvancedSecurityOverridesIn"] = t.struct(
        {
            "developerSettings": t.string().optional(),
            "googlePlayProtectVerifyApps": t.string().optional(),
            "untrustedAppsPolicy": t.string().optional(),
            "personalAppsThatCanReadWorkNotifications": t.array(t.string()).optional(),
            "commonCriteriaMode": t.string().optional(),
        }
    ).named(renames["AdvancedSecurityOverridesIn"])
    types["AdvancedSecurityOverridesOut"] = t.struct(
        {
            "developerSettings": t.string().optional(),
            "googlePlayProtectVerifyApps": t.string().optional(),
            "untrustedAppsPolicy": t.string().optional(),
            "personalAppsThatCanReadWorkNotifications": t.array(t.string()).optional(),
            "commonCriteriaMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedSecurityOverridesOut"])
    types["LoggingStoppedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoggingStoppedEventIn"]
    )
    types["LoggingStoppedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoggingStoppedEventOut"])
    types["UserIn"] = t.struct({"accountIdentifier": t.string().optional()}).named(
        renames["UserIn"]
    )
    types["UserOut"] = t.struct(
        {
            "accountIdentifier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["KioskCustomizationIn"] = t.struct(
        {
            "deviceSettings": t.string().optional(),
            "statusBar": t.string().optional(),
            "powerButtonActions": t.string().optional(),
            "systemErrorWarnings": t.string().optional(),
            "systemNavigation": t.string().optional(),
        }
    ).named(renames["KioskCustomizationIn"])
    types["KioskCustomizationOut"] = t.struct(
        {
            "deviceSettings": t.string().optional(),
            "statusBar": t.string().optional(),
            "powerButtonActions": t.string().optional(),
            "systemErrorWarnings": t.string().optional(),
            "systemNavigation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KioskCustomizationOut"])
    types["WipeActionIn"] = t.struct(
        {"preserveFrp": t.boolean().optional(), "wipeAfterDays": t.integer().optional()}
    ).named(renames["WipeActionIn"])
    types["WipeActionOut"] = t.struct(
        {
            "preserveFrp": t.boolean().optional(),
            "wipeAfterDays": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WipeActionOut"])
    types["PasswordRequirementsIn"] = t.struct(
        {
            "maximumFailedPasswordsForWipe": t.integer().optional(),
            "passwordExpirationTimeout": t.string().optional(),
            "passwordMinimumLetters": t.integer().optional(),
            "passwordQuality": t.string().optional(),
            "passwordScope": t.string().optional(),
            "passwordMinimumSymbols": t.integer().optional(),
            "passwordMinimumNumeric": t.integer().optional(),
            "passwordMinimumLowerCase": t.integer().optional(),
            "passwordMinimumLength": t.integer().optional(),
            "passwordHistoryLength": t.integer().optional(),
            "requirePasswordUnlock": t.string().optional(),
            "passwordMinimumUpperCase": t.integer().optional(),
            "unifiedLockSettings": t.string().optional(),
            "passwordMinimumNonLetter": t.integer().optional(),
        }
    ).named(renames["PasswordRequirementsIn"])
    types["PasswordRequirementsOut"] = t.struct(
        {
            "maximumFailedPasswordsForWipe": t.integer().optional(),
            "passwordExpirationTimeout": t.string().optional(),
            "passwordMinimumLetters": t.integer().optional(),
            "passwordQuality": t.string().optional(),
            "passwordScope": t.string().optional(),
            "passwordMinimumSymbols": t.integer().optional(),
            "passwordMinimumNumeric": t.integer().optional(),
            "passwordMinimumLowerCase": t.integer().optional(),
            "passwordMinimumLength": t.integer().optional(),
            "passwordHistoryLength": t.integer().optional(),
            "requirePasswordUnlock": t.string().optional(),
            "passwordMinimumUpperCase": t.integer().optional(),
            "unifiedLockSettings": t.string().optional(),
            "passwordMinimumNonLetter": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordRequirementsOut"])
    types["ClearAppsDataParamsIn"] = t.struct(
        {"packageNames": t.array(t.string()).optional()}
    ).named(renames["ClearAppsDataParamsIn"])
    types["ClearAppsDataParamsOut"] = t.struct(
        {
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearAppsDataParamsOut"])
    types["ListEnrollmentTokensResponseIn"] = t.struct(
        {
            "enrollmentTokens": t.array(
                t.proxy(renames["EnrollmentTokenIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEnrollmentTokensResponseIn"])
    types["ListEnrollmentTokensResponseOut"] = t.struct(
        {
            "enrollmentTokens": t.array(
                t.proxy(renames["EnrollmentTokenOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnrollmentTokensResponseOut"])
    types["TelephonyInfoIn"] = t.struct(
        {"phoneNumber": t.string().optional(), "carrierName": t.string().optional()}
    ).named(renames["TelephonyInfoIn"])
    types["TelephonyInfoOut"] = t.struct(
        {
            "phoneNumber": t.string().optional(),
            "carrierName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TelephonyInfoOut"])
    types["CryptoSelfTestCompletedEventIn"] = t.struct(
        {"success": t.boolean().optional()}
    ).named(renames["CryptoSelfTestCompletedEventIn"])
    types["CryptoSelfTestCompletedEventOut"] = t.struct(
        {
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoSelfTestCompletedEventOut"])
    types["DisplayIn"] = t.struct(
        {
            "displayId": t.integer().optional(),
            "name": t.string().optional(),
            "refreshRate": t.integer().optional(),
            "density": t.integer().optional(),
            "state": t.string().optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["DisplayIn"])
    types["DisplayOut"] = t.struct(
        {
            "displayId": t.integer().optional(),
            "name": t.string().optional(),
            "refreshRate": t.integer().optional(),
            "density": t.integer().optional(),
            "state": t.string().optional(),
            "width": t.integer().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayOut"])
    types["PasswordPoliciesContextIn"] = t.struct(
        {"passwordPolicyScope": t.string().optional()}
    ).named(renames["PasswordPoliciesContextIn"])
    types["PasswordPoliciesContextOut"] = t.struct(
        {
            "passwordPolicyScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordPoliciesContextOut"])
    types["CertValidationFailureEventIn"] = t.struct(
        {"failureReason": t.string().optional()}
    ).named(renames["CertValidationFailureEventIn"])
    types["CertValidationFailureEventOut"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertValidationFailureEventOut"])
    types["CertAuthorityInstalledEventIn"] = t.struct(
        {
            "certificate": t.string().optional(),
            "userId": t.integer().optional(),
            "success": t.boolean().optional(),
        }
    ).named(renames["CertAuthorityInstalledEventIn"])
    types["CertAuthorityInstalledEventOut"] = t.struct(
        {
            "certificate": t.string().optional(),
            "userId": t.integer().optional(),
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertAuthorityInstalledEventOut"])
    types["ComplianceRuleIn"] = t.struct(
        {
            "apiLevelCondition": t.proxy(renames["ApiLevelConditionIn"]).optional(),
            "disableApps": t.boolean().optional(),
            "packageNamesToDisable": t.array(t.string()).optional(),
            "nonComplianceDetailCondition": t.proxy(
                renames["NonComplianceDetailConditionIn"]
            ).optional(),
        }
    ).named(renames["ComplianceRuleIn"])
    types["ComplianceRuleOut"] = t.struct(
        {
            "apiLevelCondition": t.proxy(renames["ApiLevelConditionOut"]).optional(),
            "disableApps": t.boolean().optional(),
            "packageNamesToDisable": t.array(t.string()).optional(),
            "nonComplianceDetailCondition": t.proxy(
                renames["NonComplianceDetailConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceRuleOut"])
    types["OncWifiContextIn"] = t.struct({"wifiGuid": t.string().optional()}).named(
        renames["OncWifiContextIn"]
    )
    types["OncWifiContextOut"] = t.struct(
        {
            "wifiGuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OncWifiContextOut"])
    types["SystemUpdateIn"] = t.struct(
        {
            "freezePeriods": t.array(t.proxy(renames["FreezePeriodIn"])).optional(),
            "type": t.string().optional(),
            "endMinutes": t.integer().optional(),
            "startMinutes": t.integer().optional(),
        }
    ).named(renames["SystemUpdateIn"])
    types["SystemUpdateOut"] = t.struct(
        {
            "freezePeriods": t.array(t.proxy(renames["FreezePeriodOut"])).optional(),
            "type": t.string().optional(),
            "endMinutes": t.integer().optional(),
            "startMinutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemUpdateOut"])
    types["UserFacingMessageIn"] = t.struct(
        {
            "defaultMessage": t.string().optional(),
            "localizedMessages": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["UserFacingMessageIn"])
    types["UserFacingMessageOut"] = t.struct(
        {
            "defaultMessage": t.string().optional(),
            "localizedMessages": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserFacingMessageOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DeviceIn"] = t.struct(
        {
            "lastPolicySyncTime": t.string().optional(),
            "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
            "enrollmentTokenData": t.string().optional(),
            "appliedState": t.string().optional(),
            "appliedPasswordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsIn"])
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "hardwareStatusSamples": t.array(
                t.proxy(renames["HardwareStatusIn"])
            ).optional(),
            "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "enrollmentTime": t.string().optional(),
            "policyCompliant": t.boolean().optional(),
            "managementMode": t.string().optional(),
            "apiLevel": t.integer().optional(),
            "systemProperties": t.struct({"_": t.string().optional()}).optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
            "lastStatusReportTime": t.string().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "ownership": t.string().optional(),
            "lastPolicyComplianceReportTime": t.string().optional(),
            "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
            "applicationReports": t.array(
                t.proxy(renames["ApplicationReportIn"])
            ).optional(),
            "appliedPolicyName": t.string().optional(),
            "enrollmentTokenName": t.string().optional(),
            "policyName": t.string().optional(),
            "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
            "commonCriteriaModeInfo": t.proxy(
                renames["CommonCriteriaModeInfoIn"]
            ).optional(),
            "nonComplianceDetails": t.array(
                t.proxy(renames["NonComplianceDetailIn"])
            ).optional(),
            "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
            "powerManagementEvents": t.array(
                t.proxy(renames["PowerManagementEventIn"])
            ).optional(),
            "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
            "userName": t.string().optional(),
            "previousDeviceNames": t.array(t.string()).optional(),
            "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
            "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
            "appliedPolicyVersion": t.string().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "lastPolicySyncTime": t.string().optional(),
            "displays": t.array(t.proxy(renames["DisplayOut"])).optional(),
            "enrollmentTokenData": t.string().optional(),
            "appliedState": t.string().optional(),
            "appliedPasswordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsOut"])
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "hardwareStatusSamples": t.array(
                t.proxy(renames["HardwareStatusOut"])
            ).optional(),
            "disabledReason": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "enrollmentTime": t.string().optional(),
            "policyCompliant": t.boolean().optional(),
            "managementMode": t.string().optional(),
            "apiLevel": t.integer().optional(),
            "systemProperties": t.struct({"_": t.string().optional()}).optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoOut"]).optional(),
            "lastStatusReportTime": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "ownership": t.string().optional(),
            "lastPolicyComplianceReportTime": t.string().optional(),
            "securityPosture": t.proxy(renames["SecurityPostureOut"]).optional(),
            "applicationReports": t.array(
                t.proxy(renames["ApplicationReportOut"])
            ).optional(),
            "appliedPolicyName": t.string().optional(),
            "enrollmentTokenName": t.string().optional(),
            "policyName": t.string().optional(),
            "deviceSettings": t.proxy(renames["DeviceSettingsOut"]).optional(),
            "commonCriteriaModeInfo": t.proxy(
                renames["CommonCriteriaModeInfoOut"]
            ).optional(),
            "nonComplianceDetails": t.array(
                t.proxy(renames["NonComplianceDetailOut"])
            ).optional(),
            "memoryEvents": t.array(t.proxy(renames["MemoryEventOut"])).optional(),
            "powerManagementEvents": t.array(
                t.proxy(renames["PowerManagementEventOut"])
            ).optional(),
            "networkInfo": t.proxy(renames["NetworkInfoOut"]).optional(),
            "userName": t.string().optional(),
            "previousDeviceNames": t.array(t.string()).optional(),
            "softwareInfo": t.proxy(renames["SoftwareInfoOut"]).optional(),
            "hardwareInfo": t.proxy(renames["HardwareInfoOut"]).optional(),
            "appliedPolicyVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["NonComplianceDetailIn"] = t.struct(
        {
            "specificNonComplianceContext": t.proxy(
                renames["SpecificNonComplianceContextIn"]
            ).optional(),
            "packageName": t.string().optional(),
            "specificNonComplianceReason": t.string().optional(),
            "fieldPath": t.string().optional(),
            "currentValue": t.struct({"_": t.string().optional()}).optional(),
            "settingName": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
            "installationFailureReason": t.string().optional(),
        }
    ).named(renames["NonComplianceDetailIn"])
    types["NonComplianceDetailOut"] = t.struct(
        {
            "specificNonComplianceContext": t.proxy(
                renames["SpecificNonComplianceContextOut"]
            ).optional(),
            "packageName": t.string().optional(),
            "specificNonComplianceReason": t.string().optional(),
            "fieldPath": t.string().optional(),
            "currentValue": t.struct({"_": t.string().optional()}).optional(),
            "settingName": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
            "installationFailureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonComplianceDetailOut"])
    types["ListWebAppsResponseIn"] = t.struct(
        {
            "webApps": t.array(t.proxy(renames["WebAppIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListWebAppsResponseIn"])
    types["ListWebAppsResponseOut"] = t.struct(
        {
            "webApps": t.array(t.proxy(renames["WebAppOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWebAppsResponseOut"])
    types["NonComplianceDetailConditionIn"] = t.struct(
        {
            "nonComplianceReason": t.string().optional(),
            "packageName": t.string().optional(),
            "settingName": t.string().optional(),
        }
    ).named(renames["NonComplianceDetailConditionIn"])
    types["NonComplianceDetailConditionOut"] = t.struct(
        {
            "nonComplianceReason": t.string().optional(),
            "packageName": t.string().optional(),
            "settingName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonComplianceDetailConditionOut"])
    types["ListEnterprisesResponseIn"] = t.struct(
        {
            "enterprises": t.array(t.proxy(renames["EnterpriseIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEnterprisesResponseIn"])
    types["ListEnterprisesResponseOut"] = t.struct(
        {
            "enterprises": t.array(t.proxy(renames["EnterpriseOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnterprisesResponseOut"])
    types["KeyedAppStateIn"] = t.struct(
        {
            "key": t.string().optional(),
            "data": t.string().optional(),
            "message": t.string().optional(),
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["KeyedAppStateIn"])
    types["KeyedAppStateOut"] = t.struct(
        {
            "key": t.string().optional(),
            "data": t.string().optional(),
            "message": t.string().optional(),
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyedAppStateOut"])
    types["ClearAppsDataStatusIn"] = t.struct(
        {"results": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ClearAppsDataStatusIn"])
    types["ClearAppsDataStatusOut"] = t.struct(
        {
            "results": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearAppsDataStatusOut"])
    types["EnrollmentTokenIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "qrCode": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "expirationTimestamp": t.string().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "name": t.string().optional(),
            "oneTimeOnly": t.boolean().optional(),
            "additionalData": t.string().optional(),
            "value": t.string().optional(),
            "policyName": t.string().optional(),
        }
    ).named(renames["EnrollmentTokenIn"])
    types["EnrollmentTokenOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "qrCode": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "expirationTimestamp": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "name": t.string().optional(),
            "oneTimeOnly": t.boolean().optional(),
            "additionalData": t.string().optional(),
            "value": t.string().optional(),
            "policyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollmentTokenOut"])
    types["AppProcessInfoIn"] = t.struct(
        {
            "seinfo": t.string().optional(),
            "apkSha256Hash": t.string().optional(),
            "processName": t.string().optional(),
            "startTime": t.string().optional(),
            "pid": t.integer().optional(),
            "uid": t.integer().optional(),
            "packageNames": t.array(t.string()).optional(),
        }
    ).named(renames["AppProcessInfoIn"])
    types["AppProcessInfoOut"] = t.struct(
        {
            "seinfo": t.string().optional(),
            "apkSha256Hash": t.string().optional(),
            "processName": t.string().optional(),
            "startTime": t.string().optional(),
            "pid": t.integer().optional(),
            "uid": t.integer().optional(),
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProcessInfoOut"])
    types["ApiLevelConditionIn"] = t.struct(
        {"minApiLevel": t.integer().optional()}
    ).named(renames["ApiLevelConditionIn"])
    types["ApiLevelConditionOut"] = t.struct(
        {
            "minApiLevel": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiLevelConditionOut"])
    types["PerAppResultIn"] = t.struct({"clearingResult": t.string().optional()}).named(
        renames["PerAppResultIn"]
    )
    types["PerAppResultOut"] = t.struct(
        {
            "clearingResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerAppResultOut"])
    types["KeyGeneratedEventIn"] = t.struct(
        {
            "success": t.boolean().optional(),
            "keyAlias": t.string().optional(),
            "applicationUid": t.integer().optional(),
        }
    ).named(renames["KeyGeneratedEventIn"])
    types["KeyGeneratedEventOut"] = t.struct(
        {
            "success": t.boolean().optional(),
            "keyAlias": t.string().optional(),
            "applicationUid": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyGeneratedEventOut"])
    types["PolicyEnforcementRuleIn"] = t.struct(
        {
            "blockAction": t.proxy(renames["BlockActionIn"]).optional(),
            "settingName": t.string().optional(),
            "wipeAction": t.proxy(renames["WipeActionIn"]).optional(),
        }
    ).named(renames["PolicyEnforcementRuleIn"])
    types["PolicyEnforcementRuleOut"] = t.struct(
        {
            "blockAction": t.proxy(renames["BlockActionOut"]).optional(),
            "settingName": t.string().optional(),
            "wipeAction": t.proxy(renames["WipeActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyEnforcementRuleOut"])
    types["KeyguardDismissedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyguardDismissedEventIn"]
    )
    types["KeyguardDismissedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["KeyguardDismissedEventOut"])
    types["CommandIn"] = t.struct(
        {
            "resetPasswordFlags": t.array(t.string()).optional(),
            "newPassword": t.string().optional(),
            "type": t.string().optional(),
            "userName": t.string().optional(),
            "createTime": t.string().optional(),
            "clearAppsDataParams": t.proxy(renames["ClearAppsDataParamsIn"]).optional(),
            "errorCode": t.string().optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "resetPasswordFlags": t.array(t.string()).optional(),
            "clearAppsDataStatus": t.proxy(
                renames["ClearAppsDataStatusOut"]
            ).optional(),
            "newPassword": t.string().optional(),
            "type": t.string().optional(),
            "userName": t.string().optional(),
            "createTime": t.string().optional(),
            "clearAppsDataParams": t.proxy(
                renames["ClearAppsDataParamsOut"]
            ).optional(),
            "errorCode": t.string().optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
    types["PostureDetailIn"] = t.struct(
        {
            "advice": t.array(t.proxy(renames["UserFacingMessageIn"])).optional(),
            "securityRisk": t.string().optional(),
        }
    ).named(renames["PostureDetailIn"])
    types["PostureDetailOut"] = t.struct(
        {
            "advice": t.array(t.proxy(renames["UserFacingMessageOut"])).optional(),
            "securityRisk": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostureDetailOut"])
    types["KeyIntegrityViolationEventIn"] = t.struct(
        {"applicationUid": t.integer().optional(), "keyAlias": t.string().optional()}
    ).named(renames["KeyIntegrityViolationEventIn"])
    types["KeyIntegrityViolationEventOut"] = t.struct(
        {
            "applicationUid": t.integer().optional(),
            "keyAlias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyIntegrityViolationEventOut"])
    types["AlwaysOnVpnPackageIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "lockdownEnabled": t.boolean().optional(),
        }
    ).named(renames["AlwaysOnVpnPackageIn"])
    types["AlwaysOnVpnPackageOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "lockdownEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlwaysOnVpnPackageOut"])
    types["ProxyInfoIn"] = t.struct(
        {
            "excludedHosts": t.array(t.string()).optional(),
            "host": t.string().optional(),
            "port": t.integer().optional(),
            "pacUri": t.string().optional(),
        }
    ).named(renames["ProxyInfoIn"])
    types["ProxyInfoOut"] = t.struct(
        {
            "excludedHosts": t.array(t.string()).optional(),
            "host": t.string().optional(),
            "port": t.integer().optional(),
            "pacUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProxyInfoOut"])
    types["KeyguardSecuredEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyguardSecuredEventIn"]
    )
    types["KeyguardSecuredEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["KeyguardSecuredEventOut"])

    functions = {}
    functions["enterprisesList"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "pubsubTopic": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesCreate"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "pubsubTopic": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGet"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "pubsubTopic": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDelete"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "pubsubTopic": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPatch"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "pubsubTopic": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebTokensCreate"] = androidmanagement.post(
        "v1/{parent}/webTokens",
        t.struct(
            {
                "parent": t.string().optional(),
                "value": t.string().optional(),
                "parentFrameUrl": t.string().optional(),
                "enabledFeatures": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesDelete"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "lastPolicySyncTime": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "enrollmentTokenData": t.string().optional(),
                "appliedState": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "state": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "enrollmentTime": t.string().optional(),
                "policyCompliant": t.boolean().optional(),
                "managementMode": t.string().optional(),
                "apiLevel": t.integer().optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "lastStatusReportTime": t.string().optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "ownership": t.string().optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "appliedPolicyName": t.string().optional(),
                "enrollmentTokenName": t.string().optional(),
                "policyName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "userName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesGet"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "lastPolicySyncTime": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "enrollmentTokenData": t.string().optional(),
                "appliedState": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "state": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "enrollmentTime": t.string().optional(),
                "policyCompliant": t.boolean().optional(),
                "managementMode": t.string().optional(),
                "apiLevel": t.integer().optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "lastStatusReportTime": t.string().optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "ownership": t.string().optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "appliedPolicyName": t.string().optional(),
                "enrollmentTokenName": t.string().optional(),
                "policyName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "userName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesList"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "lastPolicySyncTime": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "enrollmentTokenData": t.string().optional(),
                "appliedState": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "state": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "enrollmentTime": t.string().optional(),
                "policyCompliant": t.boolean().optional(),
                "managementMode": t.string().optional(),
                "apiLevel": t.integer().optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "lastStatusReportTime": t.string().optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "ownership": t.string().optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "appliedPolicyName": t.string().optional(),
                "enrollmentTokenName": t.string().optional(),
                "policyName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "userName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesIssueCommand"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "lastPolicySyncTime": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "enrollmentTokenData": t.string().optional(),
                "appliedState": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "state": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "enrollmentTime": t.string().optional(),
                "policyCompliant": t.boolean().optional(),
                "managementMode": t.string().optional(),
                "apiLevel": t.integer().optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "lastStatusReportTime": t.string().optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "ownership": t.string().optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "appliedPolicyName": t.string().optional(),
                "enrollmentTokenName": t.string().optional(),
                "policyName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "userName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesPatch"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "lastPolicySyncTime": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "enrollmentTokenData": t.string().optional(),
                "appliedState": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "state": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "enrollmentTime": t.string().optional(),
                "policyCompliant": t.boolean().optional(),
                "managementMode": t.string().optional(),
                "apiLevel": t.integer().optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "lastStatusReportTime": t.string().optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "ownership": t.string().optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "appliedPolicyName": t.string().optional(),
                "enrollmentTokenName": t.string().optional(),
                "policyName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "userName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsCancel"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsGet"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsList"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsDelete"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesApplicationsGet"] = androidmanagement.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "languageCode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsCreate"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsPatch"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsList"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsGet"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsDelete"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPoliciesDelete"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPoliciesList"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPoliciesPatch"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPoliciesGet"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnrollmentTokensDelete"] = androidmanagement.get(
        "v1/{parent}/enrollmentTokens",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnrollmentTokensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnrollmentTokensCreate"] = androidmanagement.get(
        "v1/{parent}/enrollmentTokens",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnrollmentTokensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnrollmentTokensGet"] = androidmanagement.get(
        "v1/{parent}/enrollmentTokens",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnrollmentTokensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnrollmentTokensList"] = androidmanagement.get(
        "v1/{parent}/enrollmentTokens",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnrollmentTokensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["signupUrlsCreate"] = androidmanagement.post(
        "v1/signupUrls",
        t.struct(
            {
                "callbackUrl": t.string().optional(),
                "projectId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SignupUrlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="androidmanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
