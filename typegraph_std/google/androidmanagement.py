from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_androidmanagement():
    androidmanagement = HTTPRuntime("https://androidmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_androidmanagement_1_ErrorResponse",
        "ExternalDataIn": "_androidmanagement_2_ExternalDataIn",
        "ExternalDataOut": "_androidmanagement_3_ExternalDataOut",
        "PasswordRequirementsIn": "_androidmanagement_4_PasswordRequirementsIn",
        "PasswordRequirementsOut": "_androidmanagement_5_PasswordRequirementsOut",
        "CryptoSelfTestCompletedEventIn": "_androidmanagement_6_CryptoSelfTestCompletedEventIn",
        "CryptoSelfTestCompletedEventOut": "_androidmanagement_7_CryptoSelfTestCompletedEventOut",
        "CertValidationFailureEventIn": "_androidmanagement_8_CertValidationFailureEventIn",
        "CertValidationFailureEventOut": "_androidmanagement_9_CertValidationFailureEventOut",
        "PowerManagementEventIn": "_androidmanagement_10_PowerManagementEventIn",
        "PowerManagementEventOut": "_androidmanagement_11_PowerManagementEventOut",
        "StatusIn": "_androidmanagement_12_StatusIn",
        "StatusOut": "_androidmanagement_13_StatusOut",
        "NonComplianceDetailConditionIn": "_androidmanagement_14_NonComplianceDetailConditionIn",
        "NonComplianceDetailConditionOut": "_androidmanagement_15_NonComplianceDetailConditionOut",
        "ClearAppsDataStatusIn": "_androidmanagement_16_ClearAppsDataStatusIn",
        "ClearAppsDataStatusOut": "_androidmanagement_17_ClearAppsDataStatusOut",
        "ListPoliciesResponseIn": "_androidmanagement_18_ListPoliciesResponseIn",
        "ListPoliciesResponseOut": "_androidmanagement_19_ListPoliciesResponseOut",
        "RemoteLockEventIn": "_androidmanagement_20_RemoteLockEventIn",
        "RemoteLockEventOut": "_androidmanagement_21_RemoteLockEventOut",
        "ListDevicesResponseIn": "_androidmanagement_22_ListDevicesResponseIn",
        "ListDevicesResponseOut": "_androidmanagement_23_ListDevicesResponseOut",
        "OsStartupEventIn": "_androidmanagement_24_OsStartupEventIn",
        "OsStartupEventOut": "_androidmanagement_25_OsStartupEventOut",
        "SignupUrlIn": "_androidmanagement_26_SignupUrlIn",
        "SignupUrlOut": "_androidmanagement_27_SignupUrlOut",
        "AppProcessStartEventIn": "_androidmanagement_28_AppProcessStartEventIn",
        "AppProcessStartEventOut": "_androidmanagement_29_AppProcessStartEventOut",
        "PersonalUsagePoliciesIn": "_androidmanagement_30_PersonalUsagePoliciesIn",
        "PersonalUsagePoliciesOut": "_androidmanagement_31_PersonalUsagePoliciesOut",
        "ApplicationPermissionIn": "_androidmanagement_32_ApplicationPermissionIn",
        "ApplicationPermissionOut": "_androidmanagement_33_ApplicationPermissionOut",
        "WebAppIconIn": "_androidmanagement_34_WebAppIconIn",
        "WebAppIconOut": "_androidmanagement_35_WebAppIconOut",
        "MemoryEventIn": "_androidmanagement_36_MemoryEventIn",
        "MemoryEventOut": "_androidmanagement_37_MemoryEventOut",
        "ApplicationIn": "_androidmanagement_38_ApplicationIn",
        "ApplicationOut": "_androidmanagement_39_ApplicationOut",
        "LoggingStoppedEventIn": "_androidmanagement_40_LoggingStoppedEventIn",
        "LoggingStoppedEventOut": "_androidmanagement_41_LoggingStoppedEventOut",
        "EnrollmentTokenIn": "_androidmanagement_42_EnrollmentTokenIn",
        "EnrollmentTokenOut": "_androidmanagement_43_EnrollmentTokenOut",
        "CommandIn": "_androidmanagement_44_CommandIn",
        "CommandOut": "_androidmanagement_45_CommandOut",
        "NonComplianceDetailIn": "_androidmanagement_46_NonComplianceDetailIn",
        "NonComplianceDetailOut": "_androidmanagement_47_NonComplianceDetailOut",
        "AdvancedSecurityOverridesIn": "_androidmanagement_48_AdvancedSecurityOverridesIn",
        "AdvancedSecurityOverridesOut": "_androidmanagement_49_AdvancedSecurityOverridesOut",
        "DisplayIn": "_androidmanagement_50_DisplayIn",
        "DisplayOut": "_androidmanagement_51_DisplayOut",
        "SystemUpdateIn": "_androidmanagement_52_SystemUpdateIn",
        "SystemUpdateOut": "_androidmanagement_53_SystemUpdateOut",
        "BlockActionIn": "_androidmanagement_54_BlockActionIn",
        "BlockActionOut": "_androidmanagement_55_BlockActionOut",
        "PolicyEnforcementRuleIn": "_androidmanagement_56_PolicyEnforcementRuleIn",
        "PolicyEnforcementRuleOut": "_androidmanagement_57_PolicyEnforcementRuleOut",
        "SetupActionIn": "_androidmanagement_58_SetupActionIn",
        "SetupActionOut": "_androidmanagement_59_SetupActionOut",
        "PersistentPreferredActivityIn": "_androidmanagement_60_PersistentPreferredActivityIn",
        "PersistentPreferredActivityOut": "_androidmanagement_61_PersistentPreferredActivityOut",
        "SpecificNonComplianceContextIn": "_androidmanagement_62_SpecificNonComplianceContextIn",
        "SpecificNonComplianceContextOut": "_androidmanagement_63_SpecificNonComplianceContextOut",
        "ApplicationReportingSettingsIn": "_androidmanagement_64_ApplicationReportingSettingsIn",
        "ApplicationReportingSettingsOut": "_androidmanagement_65_ApplicationReportingSettingsOut",
        "WipeActionIn": "_androidmanagement_66_WipeActionIn",
        "WipeActionOut": "_androidmanagement_67_WipeActionOut",
        "ApiLevelConditionIn": "_androidmanagement_68_ApiLevelConditionIn",
        "ApiLevelConditionOut": "_androidmanagement_69_ApiLevelConditionOut",
        "ApplicationPolicyIn": "_androidmanagement_70_ApplicationPolicyIn",
        "ApplicationPolicyOut": "_androidmanagement_71_ApplicationPolicyOut",
        "ListOperationsResponseIn": "_androidmanagement_72_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_androidmanagement_73_ListOperationsResponseOut",
        "ListEnterprisesResponseIn": "_androidmanagement_74_ListEnterprisesResponseIn",
        "ListEnterprisesResponseOut": "_androidmanagement_75_ListEnterprisesResponseOut",
        "MemoryInfoIn": "_androidmanagement_76_MemoryInfoIn",
        "MemoryInfoOut": "_androidmanagement_77_MemoryInfoOut",
        "MediaUnmountEventIn": "_androidmanagement_78_MediaUnmountEventIn",
        "MediaUnmountEventOut": "_androidmanagement_79_MediaUnmountEventOut",
        "KeyedAppStateIn": "_androidmanagement_80_KeyedAppStateIn",
        "KeyedAppStateOut": "_androidmanagement_81_KeyedAppStateOut",
        "ListWebAppsResponseIn": "_androidmanagement_82_ListWebAppsResponseIn",
        "ListWebAppsResponseOut": "_androidmanagement_83_ListWebAppsResponseOut",
        "UsageLogIn": "_androidmanagement_84_UsageLogIn",
        "UsageLogOut": "_androidmanagement_85_UsageLogOut",
        "AppProcessInfoIn": "_androidmanagement_86_AppProcessInfoIn",
        "AppProcessInfoOut": "_androidmanagement_87_AppProcessInfoOut",
        "OncCertificateProviderIn": "_androidmanagement_88_OncCertificateProviderIn",
        "OncCertificateProviderOut": "_androidmanagement_89_OncCertificateProviderOut",
        "DeviceSettingsIn": "_androidmanagement_90_DeviceSettingsIn",
        "DeviceSettingsOut": "_androidmanagement_91_DeviceSettingsOut",
        "KeyIntegrityViolationEventIn": "_androidmanagement_92_KeyIntegrityViolationEventIn",
        "KeyIntegrityViolationEventOut": "_androidmanagement_93_KeyIntegrityViolationEventOut",
        "ChoosePrivateKeyRuleIn": "_androidmanagement_94_ChoosePrivateKeyRuleIn",
        "ChoosePrivateKeyRuleOut": "_androidmanagement_95_ChoosePrivateKeyRuleOut",
        "AppVersionIn": "_androidmanagement_96_AppVersionIn",
        "AppVersionOut": "_androidmanagement_97_AppVersionOut",
        "ContentProviderEndpointIn": "_androidmanagement_98_ContentProviderEndpointIn",
        "ContentProviderEndpointOut": "_androidmanagement_99_ContentProviderEndpointOut",
        "PolicyIn": "_androidmanagement_100_PolicyIn",
        "PolicyOut": "_androidmanagement_101_PolicyOut",
        "HardwareInfoIn": "_androidmanagement_102_HardwareInfoIn",
        "HardwareInfoOut": "_androidmanagement_103_HardwareInfoOut",
        "ManagedPropertyIn": "_androidmanagement_104_ManagedPropertyIn",
        "ManagedPropertyOut": "_androidmanagement_105_ManagedPropertyOut",
        "ManagedPropertyEntryIn": "_androidmanagement_106_ManagedPropertyEntryIn",
        "ManagedPropertyEntryOut": "_androidmanagement_107_ManagedPropertyEntryOut",
        "EnterpriseIn": "_androidmanagement_108_EnterpriseIn",
        "EnterpriseOut": "_androidmanagement_109_EnterpriseOut",
        "ClearAppsDataParamsIn": "_androidmanagement_110_ClearAppsDataParamsIn",
        "ClearAppsDataParamsOut": "_androidmanagement_111_ClearAppsDataParamsOut",
        "ConnectEventIn": "_androidmanagement_112_ConnectEventIn",
        "ConnectEventOut": "_androidmanagement_113_ConnectEventOut",
        "CommonCriteriaModeInfoIn": "_androidmanagement_114_CommonCriteriaModeInfoIn",
        "CommonCriteriaModeInfoOut": "_androidmanagement_115_CommonCriteriaModeInfoOut",
        "PasswordPoliciesContextIn": "_androidmanagement_116_PasswordPoliciesContextIn",
        "PasswordPoliciesContextOut": "_androidmanagement_117_PasswordPoliciesContextOut",
        "ApplicationEventIn": "_androidmanagement_118_ApplicationEventIn",
        "ApplicationEventOut": "_androidmanagement_119_ApplicationEventOut",
        "SecurityPostureIn": "_androidmanagement_120_SecurityPostureIn",
        "SecurityPostureOut": "_androidmanagement_121_SecurityPostureOut",
        "WipeFailureEventIn": "_androidmanagement_122_WipeFailureEventIn",
        "WipeFailureEventOut": "_androidmanagement_123_WipeFailureEventOut",
        "StatusReportingSettingsIn": "_androidmanagement_124_StatusReportingSettingsIn",
        "StatusReportingSettingsOut": "_androidmanagement_125_StatusReportingSettingsOut",
        "UserIn": "_androidmanagement_126_UserIn",
        "UserOut": "_androidmanagement_127_UserOut",
        "FilePushedEventIn": "_androidmanagement_128_FilePushedEventIn",
        "FilePushedEventOut": "_androidmanagement_129_FilePushedEventOut",
        "DeviceConnectivityManagementIn": "_androidmanagement_130_DeviceConnectivityManagementIn",
        "DeviceConnectivityManagementOut": "_androidmanagement_131_DeviceConnectivityManagementOut",
        "AppTrackInfoIn": "_androidmanagement_132_AppTrackInfoIn",
        "AppTrackInfoOut": "_androidmanagement_133_AppTrackInfoOut",
        "ComplianceRuleIn": "_androidmanagement_134_ComplianceRuleIn",
        "ComplianceRuleOut": "_androidmanagement_135_ComplianceRuleOut",
        "KeyguardDismissedEventIn": "_androidmanagement_136_KeyguardDismissedEventIn",
        "KeyguardDismissedEventOut": "_androidmanagement_137_KeyguardDismissedEventOut",
        "IssueCommandResponseIn": "_androidmanagement_138_IssueCommandResponseIn",
        "IssueCommandResponseOut": "_androidmanagement_139_IssueCommandResponseOut",
        "AdbShellInteractiveEventIn": "_androidmanagement_140_AdbShellInteractiveEventIn",
        "AdbShellInteractiveEventOut": "_androidmanagement_141_AdbShellInteractiveEventOut",
        "KeyImportEventIn": "_androidmanagement_142_KeyImportEventIn",
        "KeyImportEventOut": "_androidmanagement_143_KeyImportEventOut",
        "LoggingStartedEventIn": "_androidmanagement_144_LoggingStartedEventIn",
        "LoggingStartedEventOut": "_androidmanagement_145_LoggingStartedEventOut",
        "KeyguardSecuredEventIn": "_androidmanagement_146_KeyguardSecuredEventIn",
        "KeyguardSecuredEventOut": "_androidmanagement_147_KeyguardSecuredEventOut",
        "SigninDetailIn": "_androidmanagement_148_SigninDetailIn",
        "SigninDetailOut": "_androidmanagement_149_SigninDetailOut",
        "PostureDetailIn": "_androidmanagement_150_PostureDetailIn",
        "PostureDetailOut": "_androidmanagement_151_PostureDetailOut",
        "PermissionGrantIn": "_androidmanagement_152_PermissionGrantIn",
        "PermissionGrantOut": "_androidmanagement_153_PermissionGrantOut",
        "DeviceIn": "_androidmanagement_154_DeviceIn",
        "DeviceOut": "_androidmanagement_155_DeviceOut",
        "ListEnrollmentTokensResponseIn": "_androidmanagement_156_ListEnrollmentTokensResponseIn",
        "ListEnrollmentTokensResponseOut": "_androidmanagement_157_ListEnrollmentTokensResponseOut",
        "NetworkInfoIn": "_androidmanagement_158_NetworkInfoIn",
        "NetworkInfoOut": "_androidmanagement_159_NetworkInfoOut",
        "EmptyIn": "_androidmanagement_160_EmptyIn",
        "EmptyOut": "_androidmanagement_161_EmptyOut",
        "TermsAndConditionsIn": "_androidmanagement_162_TermsAndConditionsIn",
        "TermsAndConditionsOut": "_androidmanagement_163_TermsAndConditionsOut",
        "MediaMountEventIn": "_androidmanagement_164_MediaMountEventIn",
        "MediaMountEventOut": "_androidmanagement_165_MediaMountEventOut",
        "BatchUsageLogEventsIn": "_androidmanagement_166_BatchUsageLogEventsIn",
        "BatchUsageLogEventsOut": "_androidmanagement_167_BatchUsageLogEventsOut",
        "KioskCustomizationIn": "_androidmanagement_168_KioskCustomizationIn",
        "KioskCustomizationOut": "_androidmanagement_169_KioskCustomizationOut",
        "OsShutdownEventIn": "_androidmanagement_170_OsShutdownEventIn",
        "OsShutdownEventOut": "_androidmanagement_171_OsShutdownEventOut",
        "DnsEventIn": "_androidmanagement_172_DnsEventIn",
        "DnsEventOut": "_androidmanagement_173_DnsEventOut",
        "ProxyInfoIn": "_androidmanagement_174_ProxyInfoIn",
        "ProxyInfoOut": "_androidmanagement_175_ProxyInfoOut",
        "ContactInfoIn": "_androidmanagement_176_ContactInfoIn",
        "ContactInfoOut": "_androidmanagement_177_ContactInfoOut",
        "CertAuthorityRemovedEventIn": "_androidmanagement_178_CertAuthorityRemovedEventIn",
        "CertAuthorityRemovedEventOut": "_androidmanagement_179_CertAuthorityRemovedEventOut",
        "AdbShellCommandEventIn": "_androidmanagement_180_AdbShellCommandEventIn",
        "AdbShellCommandEventOut": "_androidmanagement_181_AdbShellCommandEventOut",
        "OncWifiContextIn": "_androidmanagement_182_OncWifiContextIn",
        "OncWifiContextOut": "_androidmanagement_183_OncWifiContextOut",
        "KeyGeneratedEventIn": "_androidmanagement_184_KeyGeneratedEventIn",
        "KeyGeneratedEventOut": "_androidmanagement_185_KeyGeneratedEventOut",
        "SoftwareInfoIn": "_androidmanagement_186_SoftwareInfoIn",
        "SoftwareInfoOut": "_androidmanagement_187_SoftwareInfoOut",
        "LogBufferSizeCriticalEventIn": "_androidmanagement_188_LogBufferSizeCriticalEventIn",
        "LogBufferSizeCriticalEventOut": "_androidmanagement_189_LogBufferSizeCriticalEventOut",
        "FilePulledEventIn": "_androidmanagement_190_FilePulledEventIn",
        "FilePulledEventOut": "_androidmanagement_191_FilePulledEventOut",
        "UserFacingMessageIn": "_androidmanagement_192_UserFacingMessageIn",
        "UserFacingMessageOut": "_androidmanagement_193_UserFacingMessageOut",
        "PersonalApplicationPolicyIn": "_androidmanagement_194_PersonalApplicationPolicyIn",
        "PersonalApplicationPolicyOut": "_androidmanagement_195_PersonalApplicationPolicyOut",
        "UsageLogEventIn": "_androidmanagement_196_UsageLogEventIn",
        "UsageLogEventOut": "_androidmanagement_197_UsageLogEventOut",
        "ManagedConfigurationTemplateIn": "_androidmanagement_198_ManagedConfigurationTemplateIn",
        "ManagedConfigurationTemplateOut": "_androidmanagement_199_ManagedConfigurationTemplateOut",
        "ApplicationReportIn": "_androidmanagement_200_ApplicationReportIn",
        "ApplicationReportOut": "_androidmanagement_201_ApplicationReportOut",
        "ExtensionConfigIn": "_androidmanagement_202_ExtensionConfigIn",
        "ExtensionConfigOut": "_androidmanagement_203_ExtensionConfigOut",
        "PackageNameListIn": "_androidmanagement_204_PackageNameListIn",
        "PackageNameListOut": "_androidmanagement_205_PackageNameListOut",
        "CrossProfilePoliciesIn": "_androidmanagement_206_CrossProfilePoliciesIn",
        "CrossProfilePoliciesOut": "_androidmanagement_207_CrossProfilePoliciesOut",
        "WebAppIn": "_androidmanagement_208_WebAppIn",
        "WebAppOut": "_androidmanagement_209_WebAppOut",
        "CertAuthorityInstalledEventIn": "_androidmanagement_210_CertAuthorityInstalledEventIn",
        "CertAuthorityInstalledEventOut": "_androidmanagement_211_CertAuthorityInstalledEventOut",
        "SystemUpdateInfoIn": "_androidmanagement_212_SystemUpdateInfoIn",
        "SystemUpdateInfoOut": "_androidmanagement_213_SystemUpdateInfoOut",
        "TelephonyInfoIn": "_androidmanagement_214_TelephonyInfoIn",
        "TelephonyInfoOut": "_androidmanagement_215_TelephonyInfoOut",
        "OperationIn": "_androidmanagement_216_OperationIn",
        "OperationOut": "_androidmanagement_217_OperationOut",
        "KeyDestructionEventIn": "_androidmanagement_218_KeyDestructionEventIn",
        "KeyDestructionEventOut": "_androidmanagement_219_KeyDestructionEventOut",
        "WebTokenIn": "_androidmanagement_220_WebTokenIn",
        "WebTokenOut": "_androidmanagement_221_WebTokenOut",
        "HardwareStatusIn": "_androidmanagement_222_HardwareStatusIn",
        "HardwareStatusOut": "_androidmanagement_223_HardwareStatusOut",
        "DateIn": "_androidmanagement_224_DateIn",
        "DateOut": "_androidmanagement_225_DateOut",
        "KeyguardDismissAuthAttemptEventIn": "_androidmanagement_226_KeyguardDismissAuthAttemptEventIn",
        "KeyguardDismissAuthAttemptEventOut": "_androidmanagement_227_KeyguardDismissAuthAttemptEventOut",
        "LaunchAppActionIn": "_androidmanagement_228_LaunchAppActionIn",
        "LaunchAppActionOut": "_androidmanagement_229_LaunchAppActionOut",
        "AlwaysOnVpnPackageIn": "_androidmanagement_230_AlwaysOnVpnPackageIn",
        "AlwaysOnVpnPackageOut": "_androidmanagement_231_AlwaysOnVpnPackageOut",
        "PerAppResultIn": "_androidmanagement_232_PerAppResultIn",
        "PerAppResultOut": "_androidmanagement_233_PerAppResultOut",
        "FreezePeriodIn": "_androidmanagement_234_FreezePeriodIn",
        "FreezePeriodOut": "_androidmanagement_235_FreezePeriodOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExternalDataIn"] = t.struct(
        {"url": t.string().optional(), "sha256Hash": t.string().optional()}
    ).named(renames["ExternalDataIn"])
    types["ExternalDataOut"] = t.struct(
        {
            "url": t.string().optional(),
            "sha256Hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExternalDataOut"])
    types["PasswordRequirementsIn"] = t.struct(
        {
            "passwordMinimumNonLetter": t.integer().optional(),
            "requirePasswordUnlock": t.string().optional(),
            "passwordHistoryLength": t.integer().optional(),
            "passwordQuality": t.string().optional(),
            "passwordExpirationTimeout": t.string().optional(),
            "passwordMinimumNumeric": t.integer().optional(),
            "maximumFailedPasswordsForWipe": t.integer().optional(),
            "passwordMinimumUpperCase": t.integer().optional(),
            "passwordMinimumLowerCase": t.integer().optional(),
            "passwordMinimumLength": t.integer().optional(),
            "passwordScope": t.string().optional(),
            "passwordMinimumSymbols": t.integer().optional(),
            "unifiedLockSettings": t.string().optional(),
            "passwordMinimumLetters": t.integer().optional(),
        }
    ).named(renames["PasswordRequirementsIn"])
    types["PasswordRequirementsOut"] = t.struct(
        {
            "passwordMinimumNonLetter": t.integer().optional(),
            "requirePasswordUnlock": t.string().optional(),
            "passwordHistoryLength": t.integer().optional(),
            "passwordQuality": t.string().optional(),
            "passwordExpirationTimeout": t.string().optional(),
            "passwordMinimumNumeric": t.integer().optional(),
            "maximumFailedPasswordsForWipe": t.integer().optional(),
            "passwordMinimumUpperCase": t.integer().optional(),
            "passwordMinimumLowerCase": t.integer().optional(),
            "passwordMinimumLength": t.integer().optional(),
            "passwordScope": t.string().optional(),
            "passwordMinimumSymbols": t.integer().optional(),
            "unifiedLockSettings": t.string().optional(),
            "passwordMinimumLetters": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordRequirementsOut"])
    types["CryptoSelfTestCompletedEventIn"] = t.struct(
        {"success": t.boolean().optional()}
    ).named(renames["CryptoSelfTestCompletedEventIn"])
    types["CryptoSelfTestCompletedEventOut"] = t.struct(
        {
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoSelfTestCompletedEventOut"])
    types["CertValidationFailureEventIn"] = t.struct(
        {"failureReason": t.string().optional()}
    ).named(renames["CertValidationFailureEventIn"])
    types["CertValidationFailureEventOut"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertValidationFailureEventOut"])
    types["PowerManagementEventIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "eventType": t.string().optional(),
            "batteryLevel": t.number().optional(),
        }
    ).named(renames["PowerManagementEventIn"])
    types["PowerManagementEventOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "eventType": t.string().optional(),
            "batteryLevel": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PowerManagementEventOut"])
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
    types["NonComplianceDetailConditionIn"] = t.struct(
        {
            "settingName": t.string().optional(),
            "packageName": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
        }
    ).named(renames["NonComplianceDetailConditionIn"])
    types["NonComplianceDetailConditionOut"] = t.struct(
        {
            "settingName": t.string().optional(),
            "packageName": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonComplianceDetailConditionOut"])
    types["ClearAppsDataStatusIn"] = t.struct(
        {"results": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ClearAppsDataStatusIn"])
    types["ClearAppsDataStatusOut"] = t.struct(
        {
            "results": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearAppsDataStatusOut"])
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
    types["RemoteLockEventIn"] = t.struct(
        {
            "adminUserId": t.integer().optional(),
            "targetUserId": t.integer().optional(),
            "adminPackageName": t.string().optional(),
        }
    ).named(renames["RemoteLockEventIn"])
    types["RemoteLockEventOut"] = t.struct(
        {
            "adminUserId": t.integer().optional(),
            "targetUserId": t.integer().optional(),
            "adminPackageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteLockEventOut"])
    types["ListDevicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceIn"])).optional(),
        }
    ).named(renames["ListDevicesResponseIn"])
    types["ListDevicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "devices": t.array(t.proxy(renames["DeviceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDevicesResponseOut"])
    types["OsStartupEventIn"] = t.struct(
        {
            "verifiedBootState": t.string().optional(),
            "verityMode": t.string().optional(),
        }
    ).named(renames["OsStartupEventIn"])
    types["OsStartupEventOut"] = t.struct(
        {
            "verifiedBootState": t.string().optional(),
            "verityMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsStartupEventOut"])
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
    types["AppProcessStartEventIn"] = t.struct(
        {"processInfo": t.proxy(renames["AppProcessInfoIn"]).optional()}
    ).named(renames["AppProcessStartEventIn"])
    types["AppProcessStartEventOut"] = t.struct(
        {
            "processInfo": t.proxy(renames["AppProcessInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProcessStartEventOut"])
    types["PersonalUsagePoliciesIn"] = t.struct(
        {
            "screenCaptureDisabled": t.boolean().optional(),
            "personalApplications": t.array(
                t.proxy(renames["PersonalApplicationPolicyIn"])
            ).optional(),
            "maxDaysWithWorkOff": t.integer().optional(),
            "cameraDisabled": t.boolean().optional(),
            "personalPlayStoreMode": t.string().optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
        }
    ).named(renames["PersonalUsagePoliciesIn"])
    types["PersonalUsagePoliciesOut"] = t.struct(
        {
            "screenCaptureDisabled": t.boolean().optional(),
            "personalApplications": t.array(
                t.proxy(renames["PersonalApplicationPolicyOut"])
            ).optional(),
            "maxDaysWithWorkOff": t.integer().optional(),
            "cameraDisabled": t.boolean().optional(),
            "personalPlayStoreMode": t.string().optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalUsagePoliciesOut"])
    types["ApplicationPermissionIn"] = t.struct(
        {
            "permissionId": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ApplicationPermissionIn"])
    types["ApplicationPermissionOut"] = t.struct(
        {
            "permissionId": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationPermissionOut"])
    types["WebAppIconIn"] = t.struct({"imageData": t.string().optional()}).named(
        renames["WebAppIconIn"]
    )
    types["WebAppIconOut"] = t.struct(
        {
            "imageData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppIconOut"])
    types["MemoryEventIn"] = t.struct(
        {
            "byteCount": t.string().optional(),
            "eventType": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["MemoryEventIn"])
    types["MemoryEventOut"] = t.struct(
        {
            "byteCount": t.string().optional(),
            "eventType": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryEventOut"])
    types["ApplicationIn"] = t.struct(
        {
            "title": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "permissions": t.array(
                t.proxy(renames["ApplicationPermissionIn"])
            ).optional(),
            "availableCountries": t.array(t.string()).optional(),
            "appVersions": t.array(t.proxy(renames["AppVersionIn"])).optional(),
            "recentChanges": t.string().optional(),
            "author": t.string().optional(),
            "fullDescription": t.string().optional(),
            "playStoreUrl": t.string().optional(),
            "description": t.string().optional(),
            "contentRating": t.string().optional(),
            "smallIconUrl": t.string().optional(),
            "iconUrl": t.string().optional(),
            "appTracks": t.array(t.proxy(renames["AppTrackInfoIn"])).optional(),
            "distributionChannel": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "category": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "managedProperties": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
            "appPricing": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "title": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "permissions": t.array(
                t.proxy(renames["ApplicationPermissionOut"])
            ).optional(),
            "availableCountries": t.array(t.string()).optional(),
            "appVersions": t.array(t.proxy(renames["AppVersionOut"])).optional(),
            "recentChanges": t.string().optional(),
            "author": t.string().optional(),
            "fullDescription": t.string().optional(),
            "playStoreUrl": t.string().optional(),
            "description": t.string().optional(),
            "contentRating": t.string().optional(),
            "smallIconUrl": t.string().optional(),
            "iconUrl": t.string().optional(),
            "appTracks": t.array(t.proxy(renames["AppTrackInfoOut"])).optional(),
            "distributionChannel": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "category": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "managedProperties": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "appPricing": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
    types["LoggingStoppedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoggingStoppedEventIn"]
    )
    types["LoggingStoppedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoggingStoppedEventOut"])
    types["EnrollmentTokenIn"] = t.struct(
        {
            "qrCode": t.string().optional(),
            "oneTimeOnly": t.boolean().optional(),
            "value": t.string().optional(),
            "policyName": t.string().optional(),
            "name": t.string().optional(),
            "expirationTimestamp": t.string().optional(),
            "additionalData": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["EnrollmentTokenIn"])
    types["EnrollmentTokenOut"] = t.struct(
        {
            "qrCode": t.string().optional(),
            "oneTimeOnly": t.boolean().optional(),
            "value": t.string().optional(),
            "policyName": t.string().optional(),
            "name": t.string().optional(),
            "expirationTimestamp": t.string().optional(),
            "additionalData": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "duration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollmentTokenOut"])
    types["CommandIn"] = t.struct(
        {
            "type": t.string().optional(),
            "errorCode": t.string().optional(),
            "userName": t.string().optional(),
            "resetPasswordFlags": t.array(t.string()).optional(),
            "newPassword": t.string().optional(),
            "clearAppsDataParams": t.proxy(renames["ClearAppsDataParamsIn"]).optional(),
            "duration": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "type": t.string().optional(),
            "errorCode": t.string().optional(),
            "userName": t.string().optional(),
            "resetPasswordFlags": t.array(t.string()).optional(),
            "newPassword": t.string().optional(),
            "clearAppsDataParams": t.proxy(
                renames["ClearAppsDataParamsOut"]
            ).optional(),
            "duration": t.string().optional(),
            "clearAppsDataStatus": t.proxy(
                renames["ClearAppsDataStatusOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
    types["NonComplianceDetailIn"] = t.struct(
        {
            "installationFailureReason": t.string().optional(),
            "fieldPath": t.string().optional(),
            "specificNonComplianceContext": t.proxy(
                renames["SpecificNonComplianceContextIn"]
            ).optional(),
            "packageName": t.string().optional(),
            "specificNonComplianceReason": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
            "settingName": t.string().optional(),
            "currentValue": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["NonComplianceDetailIn"])
    types["NonComplianceDetailOut"] = t.struct(
        {
            "installationFailureReason": t.string().optional(),
            "fieldPath": t.string().optional(),
            "specificNonComplianceContext": t.proxy(
                renames["SpecificNonComplianceContextOut"]
            ).optional(),
            "packageName": t.string().optional(),
            "specificNonComplianceReason": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
            "settingName": t.string().optional(),
            "currentValue": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonComplianceDetailOut"])
    types["AdvancedSecurityOverridesIn"] = t.struct(
        {
            "googlePlayProtectVerifyApps": t.string().optional(),
            "commonCriteriaMode": t.string().optional(),
            "untrustedAppsPolicy": t.string().optional(),
            "developerSettings": t.string().optional(),
            "personalAppsThatCanReadWorkNotifications": t.array(t.string()).optional(),
        }
    ).named(renames["AdvancedSecurityOverridesIn"])
    types["AdvancedSecurityOverridesOut"] = t.struct(
        {
            "googlePlayProtectVerifyApps": t.string().optional(),
            "commonCriteriaMode": t.string().optional(),
            "untrustedAppsPolicy": t.string().optional(),
            "developerSettings": t.string().optional(),
            "personalAppsThatCanReadWorkNotifications": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedSecurityOverridesOut"])
    types["DisplayIn"] = t.struct(
        {
            "displayId": t.integer().optional(),
            "state": t.string().optional(),
            "density": t.integer().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "refreshRate": t.integer().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DisplayIn"])
    types["DisplayOut"] = t.struct(
        {
            "displayId": t.integer().optional(),
            "state": t.string().optional(),
            "density": t.integer().optional(),
            "height": t.integer().optional(),
            "width": t.integer().optional(),
            "refreshRate": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayOut"])
    types["SystemUpdateIn"] = t.struct(
        {
            "startMinutes": t.integer().optional(),
            "type": t.string().optional(),
            "freezePeriods": t.array(t.proxy(renames["FreezePeriodIn"])).optional(),
            "endMinutes": t.integer().optional(),
        }
    ).named(renames["SystemUpdateIn"])
    types["SystemUpdateOut"] = t.struct(
        {
            "startMinutes": t.integer().optional(),
            "type": t.string().optional(),
            "freezePeriods": t.array(t.proxy(renames["FreezePeriodOut"])).optional(),
            "endMinutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemUpdateOut"])
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
    types["PolicyEnforcementRuleIn"] = t.struct(
        {
            "settingName": t.string().optional(),
            "blockAction": t.proxy(renames["BlockActionIn"]).optional(),
            "wipeAction": t.proxy(renames["WipeActionIn"]).optional(),
        }
    ).named(renames["PolicyEnforcementRuleIn"])
    types["PolicyEnforcementRuleOut"] = t.struct(
        {
            "settingName": t.string().optional(),
            "blockAction": t.proxy(renames["BlockActionOut"]).optional(),
            "wipeAction": t.proxy(renames["WipeActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyEnforcementRuleOut"])
    types["SetupActionIn"] = t.struct(
        {
            "launchApp": t.proxy(renames["LaunchAppActionIn"]).optional(),
            "description": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "title": t.proxy(renames["UserFacingMessageIn"]).optional(),
        }
    ).named(renames["SetupActionIn"])
    types["SetupActionOut"] = t.struct(
        {
            "launchApp": t.proxy(renames["LaunchAppActionOut"]).optional(),
            "description": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "title": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetupActionOut"])
    types["PersistentPreferredActivityIn"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "receiverActivity": t.string().optional(),
            "actions": t.array(t.string()).optional(),
        }
    ).named(renames["PersistentPreferredActivityIn"])
    types["PersistentPreferredActivityOut"] = t.struct(
        {
            "categories": t.array(t.string()).optional(),
            "receiverActivity": t.string().optional(),
            "actions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersistentPreferredActivityOut"])
    types["SpecificNonComplianceContextIn"] = t.struct(
        {
            "oncWifiContext": t.proxy(renames["OncWifiContextIn"]).optional(),
            "passwordPoliciesContext": t.proxy(
                renames["PasswordPoliciesContextIn"]
            ).optional(),
        }
    ).named(renames["SpecificNonComplianceContextIn"])
    types["SpecificNonComplianceContextOut"] = t.struct(
        {
            "oncWifiContext": t.proxy(renames["OncWifiContextOut"]).optional(),
            "passwordPoliciesContext": t.proxy(
                renames["PasswordPoliciesContextOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpecificNonComplianceContextOut"])
    types["ApplicationReportingSettingsIn"] = t.struct(
        {"includeRemovedApps": t.boolean().optional()}
    ).named(renames["ApplicationReportingSettingsIn"])
    types["ApplicationReportingSettingsOut"] = t.struct(
        {
            "includeRemovedApps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReportingSettingsOut"])
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
    types["ApiLevelConditionIn"] = t.struct(
        {"minApiLevel": t.integer().optional()}
    ).named(renames["ApiLevelConditionIn"])
    types["ApiLevelConditionOut"] = t.struct(
        {
            "minApiLevel": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiLevelConditionOut"])
    types["ApplicationPolicyIn"] = t.struct(
        {
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantIn"])
            ).optional(),
            "lockTaskAllowed": t.boolean().optional(),
            "connectedWorkAndPersonalApp": t.string().optional(),
            "managedConfigurationTemplate": t.proxy(
                renames["ManagedConfigurationTemplateIn"]
            ).optional(),
            "minimumVersionCode": t.integer().optional(),
            "alwaysOnVpnLockdownExemption": t.string().optional(),
            "installType": t.string().optional(),
            "autoUpdateMode": t.string().optional(),
            "workProfileWidgets": t.string().optional(),
            "delegatedScopes": t.array(t.string()).optional(),
            "accessibleTrackIds": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "extensionConfig": t.proxy(renames["ExtensionConfigIn"]).optional(),
            "managedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "disabled": t.boolean().optional(),
        }
    ).named(renames["ApplicationPolicyIn"])
    types["ApplicationPolicyOut"] = t.struct(
        {
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantOut"])
            ).optional(),
            "lockTaskAllowed": t.boolean().optional(),
            "connectedWorkAndPersonalApp": t.string().optional(),
            "managedConfigurationTemplate": t.proxy(
                renames["ManagedConfigurationTemplateOut"]
            ).optional(),
            "minimumVersionCode": t.integer().optional(),
            "alwaysOnVpnLockdownExemption": t.string().optional(),
            "installType": t.string().optional(),
            "autoUpdateMode": t.string().optional(),
            "workProfileWidgets": t.string().optional(),
            "delegatedScopes": t.array(t.string()).optional(),
            "accessibleTrackIds": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "extensionConfig": t.proxy(renames["ExtensionConfigOut"]).optional(),
            "managedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "disabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationPolicyOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
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
    types["MemoryInfoIn"] = t.struct(
        {
            "totalRam": t.string().optional(),
            "totalInternalStorage": t.string().optional(),
        }
    ).named(renames["MemoryInfoIn"])
    types["MemoryInfoOut"] = t.struct(
        {
            "totalRam": t.string().optional(),
            "totalInternalStorage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryInfoOut"])
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
    types["KeyedAppStateIn"] = t.struct(
        {
            "data": t.string().optional(),
            "key": t.string().optional(),
            "message": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "severity": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["KeyedAppStateIn"])
    types["KeyedAppStateOut"] = t.struct(
        {
            "data": t.string().optional(),
            "key": t.string().optional(),
            "message": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "severity": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyedAppStateOut"])
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
    types["AppProcessInfoIn"] = t.struct(
        {
            "processName": t.string().optional(),
            "startTime": t.string().optional(),
            "seinfo": t.string().optional(),
            "pid": t.integer().optional(),
            "apkSha256Hash": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
            "uid": t.integer().optional(),
        }
    ).named(renames["AppProcessInfoIn"])
    types["AppProcessInfoOut"] = t.struct(
        {
            "processName": t.string().optional(),
            "startTime": t.string().optional(),
            "seinfo": t.string().optional(),
            "pid": t.integer().optional(),
            "apkSha256Hash": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
            "uid": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProcessInfoOut"])
    types["OncCertificateProviderIn"] = t.struct(
        {
            "contentProviderEndpoint": t.proxy(
                renames["ContentProviderEndpointIn"]
            ).optional(),
            "certificateReferences": t.array(t.string()).optional(),
        }
    ).named(renames["OncCertificateProviderIn"])
    types["OncCertificateProviderOut"] = t.struct(
        {
            "contentProviderEndpoint": t.proxy(
                renames["ContentProviderEndpointOut"]
            ).optional(),
            "certificateReferences": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OncCertificateProviderOut"])
    types["DeviceSettingsIn"] = t.struct(
        {
            "adbEnabled": t.boolean().optional(),
            "developmentSettingsEnabled": t.boolean().optional(),
            "unknownSourcesEnabled": t.boolean().optional(),
            "encryptionStatus": t.string().optional(),
            "isDeviceSecure": t.boolean().optional(),
            "verifyAppsEnabled": t.boolean().optional(),
            "isEncrypted": t.boolean().optional(),
        }
    ).named(renames["DeviceSettingsIn"])
    types["DeviceSettingsOut"] = t.struct(
        {
            "adbEnabled": t.boolean().optional(),
            "developmentSettingsEnabled": t.boolean().optional(),
            "unknownSourcesEnabled": t.boolean().optional(),
            "encryptionStatus": t.string().optional(),
            "isDeviceSecure": t.boolean().optional(),
            "verifyAppsEnabled": t.boolean().optional(),
            "isEncrypted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSettingsOut"])
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
    types["ChoosePrivateKeyRuleIn"] = t.struct(
        {
            "urlPattern": t.string().optional(),
            "privateKeyAlias": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
        }
    ).named(renames["ChoosePrivateKeyRuleIn"])
    types["ChoosePrivateKeyRuleOut"] = t.struct(
        {
            "urlPattern": t.string().optional(),
            "privateKeyAlias": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChoosePrivateKeyRuleOut"])
    types["AppVersionIn"] = t.struct(
        {
            "production": t.boolean().optional(),
            "versionString": t.string().optional(),
            "versionCode": t.integer().optional(),
            "trackIds": t.array(t.string()).optional(),
        }
    ).named(renames["AppVersionIn"])
    types["AppVersionOut"] = t.struct(
        {
            "production": t.boolean().optional(),
            "versionString": t.string().optional(),
            "versionCode": t.integer().optional(),
            "trackIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppVersionOut"])
    types["ContentProviderEndpointIn"] = t.struct(
        {
            "signingCertsSha256": t.array(t.string()),
            "uri": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["ContentProviderEndpointIn"])
    types["ContentProviderEndpointOut"] = t.struct(
        {
            "signingCertsSha256": t.array(t.string()),
            "uri": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentProviderEndpointOut"])
    types["PolicyIn"] = t.struct(
        {
            "keyguardDisabled": t.boolean().optional(),
            "skipFirstUseHintsEnabled": t.boolean().optional(),
            "appAutoUpdatePolicy": t.string().optional(),
            "shortSupportMessage": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "adjustVolumeDisabled": t.boolean().optional(),
            "cameraDisabled": t.boolean().optional(),
            "usbFileTransferDisabled": t.boolean().optional(),
            "kioskCustomLauncherEnabled": t.boolean().optional(),
            "microphoneAccess": t.string().optional(),
            "bluetoothDisabled": t.boolean().optional(),
            "locationMode": t.string().optional(),
            "debuggingFeaturesAllowed": t.boolean().optional(),
            "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "passwordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsIn"])
            ).optional(),
            "crossProfilePolicies": t.proxy(
                renames["CrossProfilePoliciesIn"]
            ).optional(),
            "modifyAccountsDisabled": t.boolean().optional(),
            "autoDateAndTimeZone": t.string().optional(),
            "permittedAccessibilityServices": t.proxy(
                renames["PackageNameListIn"]
            ).optional(),
            "bluetoothContactSharingDisabled": t.boolean().optional(),
            "shareLocationDisabled": t.boolean().optional(),
            "version": t.string().optional(),
            "applications": t.array(t.proxy(renames["ApplicationPolicyIn"])).optional(),
            "unmuteMicrophoneDisabled": t.boolean().optional(),
            "removeUserDisabled": t.boolean().optional(),
            "setUserIconDisabled": t.boolean().optional(),
            "minimumApiLevel": t.integer().optional(),
            "deviceConnectivityManagement": t.proxy(
                renames["DeviceConnectivityManagementIn"]
            ).optional(),
            "networkEscapeHatchEnabled": t.boolean().optional(),
            "permittedInputMethods": t.proxy(renames["PackageNameListIn"]).optional(),
            "usbMassStorageEnabled": t.boolean().optional(),
            "playStoreMode": t.string().optional(),
            "credentialsConfigDisabled": t.boolean().optional(),
            "name": t.string().optional(),
            "androidDevicePolicyTracks": t.array(t.string()).optional(),
            "choosePrivateKeyRules": t.array(
                t.proxy(renames["ChoosePrivateKeyRuleIn"])
            ).optional(),
            "complianceRules": t.array(t.proxy(renames["ComplianceRuleIn"])).optional(),
            "outgoingBeamDisabled": t.boolean().optional(),
            "cellBroadcastsConfigDisabled": t.boolean().optional(),
            "persistentPreferredActivities": t.array(
                t.proxy(renames["PersistentPreferredActivityIn"])
            ).optional(),
            "statusBarDisabled": t.boolean().optional(),
            "statusReportingSettings": t.proxy(
                renames["StatusReportingSettingsIn"]
            ).optional(),
            "deviceOwnerLockScreenInfo": t.proxy(
                renames["UserFacingMessageIn"]
            ).optional(),
            "tetheringConfigDisabled": t.boolean().optional(),
            "wifiConfigsLockdownEnabled": t.boolean().optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "openNetworkConfiguration": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "advancedSecurityOverrides": t.proxy(
                renames["AdvancedSecurityOverridesIn"]
            ).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "passwordRequirements": t.proxy(
                renames["PasswordRequirementsIn"]
            ).optional(),
            "frpAdminEmails": t.array(t.string()).optional(),
            "oncCertificateProviders": t.array(
                t.proxy(renames["OncCertificateProviderIn"])
            ).optional(),
            "blockApplicationsEnabled": t.boolean().optional(),
            "outgoingCallsDisabled": t.boolean().optional(),
            "smsDisabled": t.boolean().optional(),
            "mobileNetworksConfigDisabled": t.boolean().optional(),
            "safeBootDisabled": t.boolean().optional(),
            "networkResetDisabled": t.boolean().optional(),
            "dataRoamingDisabled": t.boolean().optional(),
            "installUnknownSourcesAllowed": t.boolean().optional(),
            "longSupportMessage": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "createWindowsDisabled": t.boolean().optional(),
            "installAppsDisabled": t.boolean().optional(),
            "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
            "setWallpaperDisabled": t.boolean().optional(),
            "factoryResetDisabled": t.boolean().optional(),
            "personalUsagePolicies": t.proxy(
                renames["PersonalUsagePoliciesIn"]
            ).optional(),
            "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
            "mountPhysicalMediaDisabled": t.boolean().optional(),
            "alwaysOnVpnPackage": t.proxy(renames["AlwaysOnVpnPackageIn"]).optional(),
            "wifiConfigDisabled": t.boolean().optional(),
            "ensureVerifyAppsEnabled": t.boolean().optional(),
            "uninstallAppsDisabled": t.boolean().optional(),
            "keyguardDisabledFeatures": t.array(t.string()).optional(),
            "kioskCustomization": t.proxy(renames["KioskCustomizationIn"]).optional(),
            "stayOnPluggedModes": t.array(t.string()).optional(),
            "privateKeySelectionEnabled": t.boolean().optional(),
            "encryptionPolicy": t.string().optional(),
            "policyEnforcementRules": t.array(
                t.proxy(renames["PolicyEnforcementRuleIn"])
            ).optional(),
            "maximumTimeToLock": t.string().optional(),
            "preferentialNetworkService": t.string().optional(),
            "addUserDisabled": t.boolean().optional(),
            "bluetoothConfigDisabled": t.boolean().optional(),
            "cameraAccess": t.string().optional(),
            "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
            "autoTimeRequired": t.boolean().optional(),
            "funDisabled": t.boolean().optional(),
            "vpnConfigDisabled": t.boolean().optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantIn"])
            ).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "keyguardDisabled": t.boolean().optional(),
            "skipFirstUseHintsEnabled": t.boolean().optional(),
            "appAutoUpdatePolicy": t.string().optional(),
            "shortSupportMessage": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "adjustVolumeDisabled": t.boolean().optional(),
            "cameraDisabled": t.boolean().optional(),
            "usbFileTransferDisabled": t.boolean().optional(),
            "kioskCustomLauncherEnabled": t.boolean().optional(),
            "microphoneAccess": t.string().optional(),
            "bluetoothDisabled": t.boolean().optional(),
            "locationMode": t.string().optional(),
            "debuggingFeaturesAllowed": t.boolean().optional(),
            "usageLog": t.proxy(renames["UsageLogOut"]).optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "passwordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsOut"])
            ).optional(),
            "crossProfilePolicies": t.proxy(
                renames["CrossProfilePoliciesOut"]
            ).optional(),
            "modifyAccountsDisabled": t.boolean().optional(),
            "autoDateAndTimeZone": t.string().optional(),
            "permittedAccessibilityServices": t.proxy(
                renames["PackageNameListOut"]
            ).optional(),
            "bluetoothContactSharingDisabled": t.boolean().optional(),
            "shareLocationDisabled": t.boolean().optional(),
            "version": t.string().optional(),
            "applications": t.array(
                t.proxy(renames["ApplicationPolicyOut"])
            ).optional(),
            "unmuteMicrophoneDisabled": t.boolean().optional(),
            "removeUserDisabled": t.boolean().optional(),
            "setUserIconDisabled": t.boolean().optional(),
            "minimumApiLevel": t.integer().optional(),
            "deviceConnectivityManagement": t.proxy(
                renames["DeviceConnectivityManagementOut"]
            ).optional(),
            "networkEscapeHatchEnabled": t.boolean().optional(),
            "permittedInputMethods": t.proxy(renames["PackageNameListOut"]).optional(),
            "usbMassStorageEnabled": t.boolean().optional(),
            "playStoreMode": t.string().optional(),
            "credentialsConfigDisabled": t.boolean().optional(),
            "name": t.string().optional(),
            "androidDevicePolicyTracks": t.array(t.string()).optional(),
            "choosePrivateKeyRules": t.array(
                t.proxy(renames["ChoosePrivateKeyRuleOut"])
            ).optional(),
            "complianceRules": t.array(
                t.proxy(renames["ComplianceRuleOut"])
            ).optional(),
            "outgoingBeamDisabled": t.boolean().optional(),
            "cellBroadcastsConfigDisabled": t.boolean().optional(),
            "persistentPreferredActivities": t.array(
                t.proxy(renames["PersistentPreferredActivityOut"])
            ).optional(),
            "statusBarDisabled": t.boolean().optional(),
            "statusReportingSettings": t.proxy(
                renames["StatusReportingSettingsOut"]
            ).optional(),
            "deviceOwnerLockScreenInfo": t.proxy(
                renames["UserFacingMessageOut"]
            ).optional(),
            "tetheringConfigDisabled": t.boolean().optional(),
            "wifiConfigsLockdownEnabled": t.boolean().optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "openNetworkConfiguration": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "advancedSecurityOverrides": t.proxy(
                renames["AdvancedSecurityOverridesOut"]
            ).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "passwordRequirements": t.proxy(
                renames["PasswordRequirementsOut"]
            ).optional(),
            "frpAdminEmails": t.array(t.string()).optional(),
            "oncCertificateProviders": t.array(
                t.proxy(renames["OncCertificateProviderOut"])
            ).optional(),
            "blockApplicationsEnabled": t.boolean().optional(),
            "outgoingCallsDisabled": t.boolean().optional(),
            "smsDisabled": t.boolean().optional(),
            "mobileNetworksConfigDisabled": t.boolean().optional(),
            "safeBootDisabled": t.boolean().optional(),
            "networkResetDisabled": t.boolean().optional(),
            "dataRoamingDisabled": t.boolean().optional(),
            "installUnknownSourcesAllowed": t.boolean().optional(),
            "longSupportMessage": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "createWindowsDisabled": t.boolean().optional(),
            "installAppsDisabled": t.boolean().optional(),
            "recommendedGlobalProxy": t.proxy(renames["ProxyInfoOut"]).optional(),
            "setWallpaperDisabled": t.boolean().optional(),
            "factoryResetDisabled": t.boolean().optional(),
            "personalUsagePolicies": t.proxy(
                renames["PersonalUsagePoliciesOut"]
            ).optional(),
            "systemUpdate": t.proxy(renames["SystemUpdateOut"]).optional(),
            "mountPhysicalMediaDisabled": t.boolean().optional(),
            "alwaysOnVpnPackage": t.proxy(renames["AlwaysOnVpnPackageOut"]).optional(),
            "wifiConfigDisabled": t.boolean().optional(),
            "ensureVerifyAppsEnabled": t.boolean().optional(),
            "uninstallAppsDisabled": t.boolean().optional(),
            "keyguardDisabledFeatures": t.array(t.string()).optional(),
            "kioskCustomization": t.proxy(renames["KioskCustomizationOut"]).optional(),
            "stayOnPluggedModes": t.array(t.string()).optional(),
            "privateKeySelectionEnabled": t.boolean().optional(),
            "encryptionPolicy": t.string().optional(),
            "policyEnforcementRules": t.array(
                t.proxy(renames["PolicyEnforcementRuleOut"])
            ).optional(),
            "maximumTimeToLock": t.string().optional(),
            "preferentialNetworkService": t.string().optional(),
            "addUserDisabled": t.boolean().optional(),
            "bluetoothConfigDisabled": t.boolean().optional(),
            "cameraAccess": t.string().optional(),
            "setupActions": t.array(t.proxy(renames["SetupActionOut"])).optional(),
            "autoTimeRequired": t.boolean().optional(),
            "funDisabled": t.boolean().optional(),
            "vpnConfigDisabled": t.boolean().optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["HardwareInfoIn"] = t.struct(
        {
            "manufacturer": t.string().optional(),
            "brand": t.string().optional(),
            "batteryThrottlingTemperatures": t.array(t.number()).optional(),
            "gpuShutdownTemperatures": t.array(t.number()).optional(),
            "model": t.string().optional(),
            "hardware": t.string().optional(),
            "cpuThrottlingTemperatures": t.array(t.number()).optional(),
            "skinShutdownTemperatures": t.array(t.number()).optional(),
            "gpuThrottlingTemperatures": t.array(t.number()).optional(),
            "serialNumber": t.string().optional(),
            "batteryShutdownTemperatures": t.array(t.number()).optional(),
            "skinThrottlingTemperatures": t.array(t.number()).optional(),
            "deviceBasebandVersion": t.string().optional(),
            "cpuShutdownTemperatures": t.array(t.number()).optional(),
        }
    ).named(renames["HardwareInfoIn"])
    types["HardwareInfoOut"] = t.struct(
        {
            "manufacturer": t.string().optional(),
            "brand": t.string().optional(),
            "batteryThrottlingTemperatures": t.array(t.number()).optional(),
            "gpuShutdownTemperatures": t.array(t.number()).optional(),
            "model": t.string().optional(),
            "hardware": t.string().optional(),
            "cpuThrottlingTemperatures": t.array(t.number()).optional(),
            "skinShutdownTemperatures": t.array(t.number()).optional(),
            "gpuThrottlingTemperatures": t.array(t.number()).optional(),
            "serialNumber": t.string().optional(),
            "batteryShutdownTemperatures": t.array(t.number()).optional(),
            "skinThrottlingTemperatures": t.array(t.number()).optional(),
            "deviceBasebandVersion": t.string().optional(),
            "enterpriseSpecificId": t.string().optional(),
            "cpuShutdownTemperatures": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HardwareInfoOut"])
    types["ManagedPropertyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "entries": t.array(t.proxy(renames["ManagedPropertyEntryIn"])).optional(),
            "nestedProperties": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
            "key": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ManagedPropertyIn"])
    types["ManagedPropertyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string().optional(),
            "entries": t.array(t.proxy(renames["ManagedPropertyEntryOut"])).optional(),
            "nestedProperties": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "key": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPropertyOut"])
    types["ManagedPropertyEntryIn"] = t.struct(
        {"name": t.string().optional(), "value": t.string().optional()}
    ).named(renames["ManagedPropertyEntryIn"])
    types["ManagedPropertyEntryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPropertyEntryOut"])
    types["EnterpriseIn"] = t.struct(
        {
            "primaryColor": t.integer().optional(),
            "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
            "enterpriseDisplayName": t.string().optional(),
            "logo": t.proxy(renames["ExternalDataIn"]).optional(),
            "termsAndConditions": t.array(
                t.proxy(renames["TermsAndConditionsIn"])
            ).optional(),
            "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
            "name": t.string().optional(),
            "appAutoApprovalEnabled": t.boolean().optional(),
            "enabledNotificationTypes": t.array(t.string()).optional(),
            "pubsubTopic": t.string().optional(),
        }
    ).named(renames["EnterpriseIn"])
    types["EnterpriseOut"] = t.struct(
        {
            "primaryColor": t.integer().optional(),
            "contactInfo": t.proxy(renames["ContactInfoOut"]).optional(),
            "enterpriseDisplayName": t.string().optional(),
            "logo": t.proxy(renames["ExternalDataOut"]).optional(),
            "termsAndConditions": t.array(
                t.proxy(renames["TermsAndConditionsOut"])
            ).optional(),
            "signinDetails": t.array(t.proxy(renames["SigninDetailOut"])).optional(),
            "name": t.string().optional(),
            "appAutoApprovalEnabled": t.boolean().optional(),
            "enabledNotificationTypes": t.array(t.string()).optional(),
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseOut"])
    types["ClearAppsDataParamsIn"] = t.struct(
        {"packageNames": t.array(t.string()).optional()}
    ).named(renames["ClearAppsDataParamsIn"])
    types["ClearAppsDataParamsOut"] = t.struct(
        {
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearAppsDataParamsOut"])
    types["ConnectEventIn"] = t.struct(
        {
            "destinationPort": t.integer().optional(),
            "destinationIpAddress": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["ConnectEventIn"])
    types["ConnectEventOut"] = t.struct(
        {
            "destinationPort": t.integer().optional(),
            "destinationIpAddress": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectEventOut"])
    types["CommonCriteriaModeInfoIn"] = t.struct(
        {"commonCriteriaModeStatus": t.string().optional()}
    ).named(renames["CommonCriteriaModeInfoIn"])
    types["CommonCriteriaModeInfoOut"] = t.struct(
        {
            "commonCriteriaModeStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonCriteriaModeInfoOut"])
    types["PasswordPoliciesContextIn"] = t.struct(
        {"passwordPolicyScope": t.string().optional()}
    ).named(renames["PasswordPoliciesContextIn"])
    types["PasswordPoliciesContextOut"] = t.struct(
        {
            "passwordPolicyScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordPoliciesContextOut"])
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
    types["WipeFailureEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WipeFailureEventIn"]
    )
    types["WipeFailureEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WipeFailureEventOut"])
    types["StatusReportingSettingsIn"] = t.struct(
        {
            "displayInfoEnabled": t.boolean().optional(),
            "applicationReportingSettings": t.proxy(
                renames["ApplicationReportingSettingsIn"]
            ).optional(),
            "hardwareStatusEnabled": t.boolean().optional(),
            "applicationReportsEnabled": t.boolean().optional(),
            "powerManagementEventsEnabled": t.boolean().optional(),
            "systemPropertiesEnabled": t.boolean().optional(),
            "memoryInfoEnabled": t.boolean().optional(),
            "commonCriteriaModeEnabled": t.boolean().optional(),
            "deviceSettingsEnabled": t.boolean().optional(),
            "networkInfoEnabled": t.boolean().optional(),
            "softwareInfoEnabled": t.boolean().optional(),
        }
    ).named(renames["StatusReportingSettingsIn"])
    types["StatusReportingSettingsOut"] = t.struct(
        {
            "displayInfoEnabled": t.boolean().optional(),
            "applicationReportingSettings": t.proxy(
                renames["ApplicationReportingSettingsOut"]
            ).optional(),
            "hardwareStatusEnabled": t.boolean().optional(),
            "applicationReportsEnabled": t.boolean().optional(),
            "powerManagementEventsEnabled": t.boolean().optional(),
            "systemPropertiesEnabled": t.boolean().optional(),
            "memoryInfoEnabled": t.boolean().optional(),
            "commonCriteriaModeEnabled": t.boolean().optional(),
            "deviceSettingsEnabled": t.boolean().optional(),
            "networkInfoEnabled": t.boolean().optional(),
            "softwareInfoEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusReportingSettingsOut"])
    types["UserIn"] = t.struct({"accountIdentifier": t.string().optional()}).named(
        renames["UserIn"]
    )
    types["UserOut"] = t.struct(
        {
            "accountIdentifier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["FilePushedEventIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FilePushedEventIn"]
    )
    types["FilePushedEventOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilePushedEventOut"])
    types["DeviceConnectivityManagementIn"] = t.struct(
        {"usbDataAccess": t.string().optional()}
    ).named(renames["DeviceConnectivityManagementIn"])
    types["DeviceConnectivityManagementOut"] = t.struct(
        {
            "usbDataAccess": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceConnectivityManagementOut"])
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
    types["ComplianceRuleIn"] = t.struct(
        {
            "apiLevelCondition": t.proxy(renames["ApiLevelConditionIn"]).optional(),
            "packageNamesToDisable": t.array(t.string()).optional(),
            "disableApps": t.boolean().optional(),
            "nonComplianceDetailCondition": t.proxy(
                renames["NonComplianceDetailConditionIn"]
            ).optional(),
        }
    ).named(renames["ComplianceRuleIn"])
    types["ComplianceRuleOut"] = t.struct(
        {
            "apiLevelCondition": t.proxy(renames["ApiLevelConditionOut"]).optional(),
            "packageNamesToDisable": t.array(t.string()).optional(),
            "disableApps": t.boolean().optional(),
            "nonComplianceDetailCondition": t.proxy(
                renames["NonComplianceDetailConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceRuleOut"])
    types["KeyguardDismissedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyguardDismissedEventIn"]
    )
    types["KeyguardDismissedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["KeyguardDismissedEventOut"])
    types["IssueCommandResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IssueCommandResponseIn"]
    )
    types["IssueCommandResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IssueCommandResponseOut"])
    types["AdbShellInteractiveEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdbShellInteractiveEventIn"]
    )
    types["AdbShellInteractiveEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdbShellInteractiveEventOut"])
    types["KeyImportEventIn"] = t.struct(
        {
            "success": t.boolean().optional(),
            "keyAlias": t.string().optional(),
            "applicationUid": t.integer().optional(),
        }
    ).named(renames["KeyImportEventIn"])
    types["KeyImportEventOut"] = t.struct(
        {
            "success": t.boolean().optional(),
            "keyAlias": t.string().optional(),
            "applicationUid": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyImportEventOut"])
    types["LoggingStartedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoggingStartedEventIn"]
    )
    types["LoggingStartedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoggingStartedEventOut"])
    types["KeyguardSecuredEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyguardSecuredEventIn"]
    )
    types["KeyguardSecuredEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["KeyguardSecuredEventOut"])
    types["SigninDetailIn"] = t.struct(
        {
            "qrCode": t.string().optional(),
            "signinEnrollmentToken": t.string().optional(),
            "signinUrl": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
        }
    ).named(renames["SigninDetailIn"])
    types["SigninDetailOut"] = t.struct(
        {
            "qrCode": t.string().optional(),
            "signinEnrollmentToken": t.string().optional(),
            "signinUrl": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SigninDetailOut"])
    types["PostureDetailIn"] = t.struct(
        {
            "securityRisk": t.string().optional(),
            "advice": t.array(t.proxy(renames["UserFacingMessageIn"])).optional(),
        }
    ).named(renames["PostureDetailIn"])
    types["PostureDetailOut"] = t.struct(
        {
            "securityRisk": t.string().optional(),
            "advice": t.array(t.proxy(renames["UserFacingMessageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostureDetailOut"])
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
    types["DeviceIn"] = t.struct(
        {
            "lastPolicySyncTime": t.string().optional(),
            "state": t.string().optional(),
            "nonComplianceDetails": t.array(
                t.proxy(renames["NonComplianceDetailIn"])
            ).optional(),
            "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
            "lastPolicyComplianceReportTime": t.string().optional(),
            "powerManagementEvents": t.array(
                t.proxy(renames["PowerManagementEventIn"])
            ).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "applicationReports": t.array(
                t.proxy(renames["ApplicationReportIn"])
            ).optional(),
            "systemProperties": t.struct({"_": t.string().optional()}).optional(),
            "lastStatusReportTime": t.string().optional(),
            "appliedPasswordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsIn"])
            ).optional(),
            "policyName": t.string().optional(),
            "previousDeviceNames": t.array(t.string()).optional(),
            "ownership": t.string().optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
            "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
            "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
            "appliedPolicyVersion": t.string().optional(),
            "hardwareStatusSamples": t.array(
                t.proxy(renames["HardwareStatusIn"])
            ).optional(),
            "apiLevel": t.integer().optional(),
            "enrollmentTokenName": t.string().optional(),
            "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
            "name": t.string().optional(),
            "appliedState": t.string().optional(),
            "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
            "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "policyCompliant": t.boolean().optional(),
            "appliedPolicyName": t.string().optional(),
            "commonCriteriaModeInfo": t.proxy(
                renames["CommonCriteriaModeInfoIn"]
            ).optional(),
            "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
            "enrollmentTokenData": t.string().optional(),
            "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
            "userName": t.string().optional(),
            "enrollmentTime": t.string().optional(),
            "managementMode": t.string().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "lastPolicySyncTime": t.string().optional(),
            "state": t.string().optional(),
            "nonComplianceDetails": t.array(
                t.proxy(renames["NonComplianceDetailOut"])
            ).optional(),
            "networkInfo": t.proxy(renames["NetworkInfoOut"]).optional(),
            "lastPolicyComplianceReportTime": t.string().optional(),
            "powerManagementEvents": t.array(
                t.proxy(renames["PowerManagementEventOut"])
            ).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "applicationReports": t.array(
                t.proxy(renames["ApplicationReportOut"])
            ).optional(),
            "systemProperties": t.struct({"_": t.string().optional()}).optional(),
            "lastStatusReportTime": t.string().optional(),
            "appliedPasswordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsOut"])
            ).optional(),
            "policyName": t.string().optional(),
            "previousDeviceNames": t.array(t.string()).optional(),
            "ownership": t.string().optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoOut"]).optional(),
            "securityPosture": t.proxy(renames["SecurityPostureOut"]).optional(),
            "softwareInfo": t.proxy(renames["SoftwareInfoOut"]).optional(),
            "appliedPolicyVersion": t.string().optional(),
            "hardwareStatusSamples": t.array(
                t.proxy(renames["HardwareStatusOut"])
            ).optional(),
            "apiLevel": t.integer().optional(),
            "enrollmentTokenName": t.string().optional(),
            "deviceSettings": t.proxy(renames["DeviceSettingsOut"]).optional(),
            "name": t.string().optional(),
            "appliedState": t.string().optional(),
            "memoryEvents": t.array(t.proxy(renames["MemoryEventOut"])).optional(),
            "disabledReason": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "policyCompliant": t.boolean().optional(),
            "appliedPolicyName": t.string().optional(),
            "commonCriteriaModeInfo": t.proxy(
                renames["CommonCriteriaModeInfoOut"]
            ).optional(),
            "hardwareInfo": t.proxy(renames["HardwareInfoOut"]).optional(),
            "enrollmentTokenData": t.string().optional(),
            "displays": t.array(t.proxy(renames["DisplayOut"])).optional(),
            "userName": t.string().optional(),
            "enrollmentTime": t.string().optional(),
            "managementMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
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
    types["NetworkInfoIn"] = t.struct(
        {
            "telephonyInfos": t.array(t.proxy(renames["TelephonyInfoIn"])).optional(),
            "imei": t.string().optional(),
            "meid": t.string().optional(),
            "networkOperatorName": t.string().optional(),
            "wifiMacAddress": t.string().optional(),
        }
    ).named(renames["NetworkInfoIn"])
    types["NetworkInfoOut"] = t.struct(
        {
            "telephonyInfos": t.array(t.proxy(renames["TelephonyInfoOut"])).optional(),
            "imei": t.string().optional(),
            "meid": t.string().optional(),
            "networkOperatorName": t.string().optional(),
            "wifiMacAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInfoOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TermsAndConditionsIn"] = t.struct(
        {
            "content": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "header": t.proxy(renames["UserFacingMessageIn"]).optional(),
        }
    ).named(renames["TermsAndConditionsIn"])
    types["TermsAndConditionsOut"] = t.struct(
        {
            "content": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "header": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TermsAndConditionsOut"])
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
    types["BatchUsageLogEventsIn"] = t.struct(
        {
            "retrievalTime": t.string().optional(),
            "device": t.string().optional(),
            "user": t.string().optional(),
            "usageLogEvents": t.array(t.proxy(renames["UsageLogEventIn"])).optional(),
        }
    ).named(renames["BatchUsageLogEventsIn"])
    types["BatchUsageLogEventsOut"] = t.struct(
        {
            "retrievalTime": t.string().optional(),
            "device": t.string().optional(),
            "user": t.string().optional(),
            "usageLogEvents": t.array(t.proxy(renames["UsageLogEventOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUsageLogEventsOut"])
    types["KioskCustomizationIn"] = t.struct(
        {
            "statusBar": t.string().optional(),
            "deviceSettings": t.string().optional(),
            "systemErrorWarnings": t.string().optional(),
            "systemNavigation": t.string().optional(),
            "powerButtonActions": t.string().optional(),
        }
    ).named(renames["KioskCustomizationIn"])
    types["KioskCustomizationOut"] = t.struct(
        {
            "statusBar": t.string().optional(),
            "deviceSettings": t.string().optional(),
            "systemErrorWarnings": t.string().optional(),
            "systemNavigation": t.string().optional(),
            "powerButtonActions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KioskCustomizationOut"])
    types["OsShutdownEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OsShutdownEventIn"]
    )
    types["OsShutdownEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OsShutdownEventOut"])
    types["DnsEventIn"] = t.struct(
        {
            "hostname": t.string().optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "totalIpAddressesReturned": t.string().optional(),
        }
    ).named(renames["DnsEventIn"])
    types["DnsEventOut"] = t.struct(
        {
            "hostname": t.string().optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "packageName": t.string().optional(),
            "totalIpAddressesReturned": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsEventOut"])
    types["ProxyInfoIn"] = t.struct(
        {
            "excludedHosts": t.array(t.string()).optional(),
            "host": t.string().optional(),
            "pacUri": t.string().optional(),
            "port": t.integer().optional(),
        }
    ).named(renames["ProxyInfoIn"])
    types["ProxyInfoOut"] = t.struct(
        {
            "excludedHosts": t.array(t.string()).optional(),
            "host": t.string().optional(),
            "pacUri": t.string().optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProxyInfoOut"])
    types["ContactInfoIn"] = t.struct(
        {
            "dataProtectionOfficerName": t.string().optional(),
            "dataProtectionOfficerEmail": t.string().optional(),
            "euRepresentativePhone": t.string().optional(),
            "euRepresentativeName": t.string().optional(),
            "dataProtectionOfficerPhone": t.string().optional(),
            "contactEmail": t.string().optional(),
            "euRepresentativeEmail": t.string().optional(),
        }
    ).named(renames["ContactInfoIn"])
    types["ContactInfoOut"] = t.struct(
        {
            "dataProtectionOfficerName": t.string().optional(),
            "dataProtectionOfficerEmail": t.string().optional(),
            "euRepresentativePhone": t.string().optional(),
            "euRepresentativeName": t.string().optional(),
            "dataProtectionOfficerPhone": t.string().optional(),
            "contactEmail": t.string().optional(),
            "euRepresentativeEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoOut"])
    types["CertAuthorityRemovedEventIn"] = t.struct(
        {
            "success": t.boolean().optional(),
            "certificate": t.string().optional(),
            "userId": t.integer().optional(),
        }
    ).named(renames["CertAuthorityRemovedEventIn"])
    types["CertAuthorityRemovedEventOut"] = t.struct(
        {
            "success": t.boolean().optional(),
            "certificate": t.string().optional(),
            "userId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertAuthorityRemovedEventOut"])
    types["AdbShellCommandEventIn"] = t.struct(
        {"shellCmd": t.string().optional()}
    ).named(renames["AdbShellCommandEventIn"])
    types["AdbShellCommandEventOut"] = t.struct(
        {
            "shellCmd": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdbShellCommandEventOut"])
    types["OncWifiContextIn"] = t.struct({"wifiGuid": t.string().optional()}).named(
        renames["OncWifiContextIn"]
    )
    types["OncWifiContextOut"] = t.struct(
        {
            "wifiGuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OncWifiContextOut"])
    types["KeyGeneratedEventIn"] = t.struct(
        {
            "keyAlias": t.string().optional(),
            "success": t.boolean().optional(),
            "applicationUid": t.integer().optional(),
        }
    ).named(renames["KeyGeneratedEventIn"])
    types["KeyGeneratedEventOut"] = t.struct(
        {
            "keyAlias": t.string().optional(),
            "success": t.boolean().optional(),
            "applicationUid": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyGeneratedEventOut"])
    types["SoftwareInfoIn"] = t.struct(
        {
            "systemUpdateInfo": t.proxy(renames["SystemUpdateInfoIn"]).optional(),
            "androidVersion": t.string().optional(),
            "deviceBuildSignature": t.string().optional(),
            "securityPatchLevel": t.string().optional(),
            "androidBuildTime": t.string().optional(),
            "androidBuildNumber": t.string().optional(),
            "primaryLanguageCode": t.string().optional(),
            "bootloaderVersion": t.string().optional(),
            "deviceKernelVersion": t.string().optional(),
            "androidDevicePolicyVersionName": t.string().optional(),
            "androidDevicePolicyVersionCode": t.integer().optional(),
        }
    ).named(renames["SoftwareInfoIn"])
    types["SoftwareInfoOut"] = t.struct(
        {
            "systemUpdateInfo": t.proxy(renames["SystemUpdateInfoOut"]).optional(),
            "androidVersion": t.string().optional(),
            "deviceBuildSignature": t.string().optional(),
            "securityPatchLevel": t.string().optional(),
            "androidBuildTime": t.string().optional(),
            "androidBuildNumber": t.string().optional(),
            "primaryLanguageCode": t.string().optional(),
            "bootloaderVersion": t.string().optional(),
            "deviceKernelVersion": t.string().optional(),
            "androidDevicePolicyVersionName": t.string().optional(),
            "androidDevicePolicyVersionCode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareInfoOut"])
    types["LogBufferSizeCriticalEventIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["LogBufferSizeCriticalEventIn"])
    types["LogBufferSizeCriticalEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LogBufferSizeCriticalEventOut"])
    types["FilePulledEventIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FilePulledEventIn"]
    )
    types["FilePulledEventOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilePulledEventOut"])
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
    types["PersonalApplicationPolicyIn"] = t.struct(
        {"packageName": t.string().optional(), "installType": t.string().optional()}
    ).named(renames["PersonalApplicationPolicyIn"])
    types["PersonalApplicationPolicyOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "installType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalApplicationPolicyOut"])
    types["UsageLogEventIn"] = t.struct(
        {
            "keyIntegrityViolationEvent": t.proxy(
                renames["KeyIntegrityViolationEventIn"]
            ).optional(),
            "adbShellCommandEvent": t.proxy(
                renames["AdbShellCommandEventIn"]
            ).optional(),
            "osShutdownEvent": t.proxy(renames["OsShutdownEventIn"]).optional(),
            "certAuthorityRemovedEvent": t.proxy(
                renames["CertAuthorityRemovedEventIn"]
            ).optional(),
            "appProcessStartEvent": t.proxy(
                renames["AppProcessStartEventIn"]
            ).optional(),
            "osStartupEvent": t.proxy(renames["OsStartupEventIn"]).optional(),
            "certValidationFailureEvent": t.proxy(
                renames["CertValidationFailureEventIn"]
            ).optional(),
            "keyGeneratedEvent": t.proxy(renames["KeyGeneratedEventIn"]).optional(),
            "cryptoSelfTestCompletedEvent": t.proxy(
                renames["CryptoSelfTestCompletedEventIn"]
            ).optional(),
            "filePushedEvent": t.proxy(renames["FilePushedEventIn"]).optional(),
            "eventType": t.string().optional(),
            "keyDestructionEvent": t.proxy(renames["KeyDestructionEventIn"]).optional(),
            "keyImportEvent": t.proxy(renames["KeyImportEventIn"]).optional(),
            "eventId": t.string().optional(),
            "loggingStartedEvent": t.proxy(renames["LoggingStartedEventIn"]).optional(),
            "loggingStoppedEvent": t.proxy(renames["LoggingStoppedEventIn"]).optional(),
            "filePulledEvent": t.proxy(renames["FilePulledEventIn"]).optional(),
            "dnsEvent": t.proxy(renames["DnsEventIn"]).optional(),
            "keyguardSecuredEvent": t.proxy(
                renames["KeyguardSecuredEventIn"]
            ).optional(),
            "logBufferSizeCriticalEvent": t.proxy(
                renames["LogBufferSizeCriticalEventIn"]
            ).optional(),
            "mediaMountEvent": t.proxy(renames["MediaMountEventIn"]).optional(),
            "eventTime": t.string().optional(),
            "connectEvent": t.proxy(renames["ConnectEventIn"]).optional(),
            "keyguardDismissAuthAttemptEvent": t.proxy(
                renames["KeyguardDismissAuthAttemptEventIn"]
            ).optional(),
            "certAuthorityInstalledEvent": t.proxy(
                renames["CertAuthorityInstalledEventIn"]
            ).optional(),
            "mediaUnmountEvent": t.proxy(renames["MediaUnmountEventIn"]).optional(),
            "adbShellInteractiveEvent": t.proxy(
                renames["AdbShellInteractiveEventIn"]
            ).optional(),
            "wipeFailureEvent": t.proxy(renames["WipeFailureEventIn"]).optional(),
            "remoteLockEvent": t.proxy(renames["RemoteLockEventIn"]).optional(),
            "keyguardDismissedEvent": t.proxy(
                renames["KeyguardDismissedEventIn"]
            ).optional(),
        }
    ).named(renames["UsageLogEventIn"])
    types["UsageLogEventOut"] = t.struct(
        {
            "keyIntegrityViolationEvent": t.proxy(
                renames["KeyIntegrityViolationEventOut"]
            ).optional(),
            "adbShellCommandEvent": t.proxy(
                renames["AdbShellCommandEventOut"]
            ).optional(),
            "osShutdownEvent": t.proxy(renames["OsShutdownEventOut"]).optional(),
            "certAuthorityRemovedEvent": t.proxy(
                renames["CertAuthorityRemovedEventOut"]
            ).optional(),
            "appProcessStartEvent": t.proxy(
                renames["AppProcessStartEventOut"]
            ).optional(),
            "osStartupEvent": t.proxy(renames["OsStartupEventOut"]).optional(),
            "certValidationFailureEvent": t.proxy(
                renames["CertValidationFailureEventOut"]
            ).optional(),
            "keyGeneratedEvent": t.proxy(renames["KeyGeneratedEventOut"]).optional(),
            "cryptoSelfTestCompletedEvent": t.proxy(
                renames["CryptoSelfTestCompletedEventOut"]
            ).optional(),
            "filePushedEvent": t.proxy(renames["FilePushedEventOut"]).optional(),
            "eventType": t.string().optional(),
            "keyDestructionEvent": t.proxy(
                renames["KeyDestructionEventOut"]
            ).optional(),
            "keyImportEvent": t.proxy(renames["KeyImportEventOut"]).optional(),
            "eventId": t.string().optional(),
            "loggingStartedEvent": t.proxy(
                renames["LoggingStartedEventOut"]
            ).optional(),
            "loggingStoppedEvent": t.proxy(
                renames["LoggingStoppedEventOut"]
            ).optional(),
            "filePulledEvent": t.proxy(renames["FilePulledEventOut"]).optional(),
            "dnsEvent": t.proxy(renames["DnsEventOut"]).optional(),
            "keyguardSecuredEvent": t.proxy(
                renames["KeyguardSecuredEventOut"]
            ).optional(),
            "logBufferSizeCriticalEvent": t.proxy(
                renames["LogBufferSizeCriticalEventOut"]
            ).optional(),
            "mediaMountEvent": t.proxy(renames["MediaMountEventOut"]).optional(),
            "eventTime": t.string().optional(),
            "connectEvent": t.proxy(renames["ConnectEventOut"]).optional(),
            "keyguardDismissAuthAttemptEvent": t.proxy(
                renames["KeyguardDismissAuthAttemptEventOut"]
            ).optional(),
            "certAuthorityInstalledEvent": t.proxy(
                renames["CertAuthorityInstalledEventOut"]
            ).optional(),
            "mediaUnmountEvent": t.proxy(renames["MediaUnmountEventOut"]).optional(),
            "adbShellInteractiveEvent": t.proxy(
                renames["AdbShellInteractiveEventOut"]
            ).optional(),
            "wipeFailureEvent": t.proxy(renames["WipeFailureEventOut"]).optional(),
            "remoteLockEvent": t.proxy(renames["RemoteLockEventOut"]).optional(),
            "keyguardDismissedEvent": t.proxy(
                renames["KeyguardDismissedEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageLogEventOut"])
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
    types["ApplicationReportIn"] = t.struct(
        {
            "packageSha256Hash": t.string().optional(),
            "events": t.array(t.proxy(renames["ApplicationEventIn"])).optional(),
            "packageName": t.string().optional(),
            "keyedAppStates": t.array(t.proxy(renames["KeyedAppStateIn"])).optional(),
            "state": t.string().optional(),
            "installerPackageName": t.string().optional(),
            "signingKeyCertFingerprints": t.array(t.string()).optional(),
            "versionCode": t.integer().optional(),
            "displayName": t.string().optional(),
            "applicationSource": t.string().optional(),
            "versionName": t.string().optional(),
        }
    ).named(renames["ApplicationReportIn"])
    types["ApplicationReportOut"] = t.struct(
        {
            "packageSha256Hash": t.string().optional(),
            "events": t.array(t.proxy(renames["ApplicationEventOut"])).optional(),
            "packageName": t.string().optional(),
            "keyedAppStates": t.array(t.proxy(renames["KeyedAppStateOut"])).optional(),
            "state": t.string().optional(),
            "installerPackageName": t.string().optional(),
            "signingKeyCertFingerprints": t.array(t.string()).optional(),
            "versionCode": t.integer().optional(),
            "displayName": t.string().optional(),
            "applicationSource": t.string().optional(),
            "versionName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReportOut"])
    types["ExtensionConfigIn"] = t.struct(
        {
            "signingKeyFingerprintsSha256": t.array(t.string()).optional(),
            "notificationReceiver": t.string().optional(),
        }
    ).named(renames["ExtensionConfigIn"])
    types["ExtensionConfigOut"] = t.struct(
        {
            "signingKeyFingerprintsSha256": t.array(t.string()).optional(),
            "notificationReceiver": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtensionConfigOut"])
    types["PackageNameListIn"] = t.struct(
        {"packageNames": t.array(t.string()).optional()}
    ).named(renames["PackageNameListIn"])
    types["PackageNameListOut"] = t.struct(
        {
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageNameListOut"])
    types["CrossProfilePoliciesIn"] = t.struct(
        {
            "crossProfileCopyPaste": t.string().optional(),
            "crossProfileDataSharing": t.string().optional(),
            "showWorkContactsInPersonalProfile": t.string().optional(),
            "workProfileWidgetsDefault": t.string().optional(),
        }
    ).named(renames["CrossProfilePoliciesIn"])
    types["CrossProfilePoliciesOut"] = t.struct(
        {
            "crossProfileCopyPaste": t.string().optional(),
            "crossProfileDataSharing": t.string().optional(),
            "showWorkContactsInPersonalProfile": t.string().optional(),
            "workProfileWidgetsDefault": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrossProfilePoliciesOut"])
    types["WebAppIn"] = t.struct(
        {
            "displayMode": t.string().optional(),
            "versionCode": t.string().optional(),
            "startUrl": t.string().optional(),
            "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "displayMode": t.string().optional(),
            "versionCode": t.string().optional(),
            "startUrl": t.string().optional(),
            "icons": t.array(t.proxy(renames["WebAppIconOut"])).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
    types["CertAuthorityInstalledEventIn"] = t.struct(
        {
            "userId": t.integer().optional(),
            "certificate": t.string().optional(),
            "success": t.boolean().optional(),
        }
    ).named(renames["CertAuthorityInstalledEventIn"])
    types["CertAuthorityInstalledEventOut"] = t.struct(
        {
            "userId": t.integer().optional(),
            "certificate": t.string().optional(),
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertAuthorityInstalledEventOut"])
    types["SystemUpdateInfoIn"] = t.struct(
        {
            "updateReceivedTime": t.string().optional(),
            "updateStatus": t.string().optional(),
        }
    ).named(renames["SystemUpdateInfoIn"])
    types["SystemUpdateInfoOut"] = t.struct(
        {
            "updateReceivedTime": t.string().optional(),
            "updateStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemUpdateInfoOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["KeyDestructionEventIn"] = t.struct(
        {
            "keyAlias": t.string().optional(),
            "applicationUid": t.integer().optional(),
            "success": t.boolean().optional(),
        }
    ).named(renames["KeyDestructionEventIn"])
    types["KeyDestructionEventOut"] = t.struct(
        {
            "keyAlias": t.string().optional(),
            "applicationUid": t.integer().optional(),
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyDestructionEventOut"])
    types["WebTokenIn"] = t.struct(
        {
            "enabledFeatures": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "parentFrameUrl": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "value": t.string().optional(),
        }
    ).named(renames["WebTokenIn"])
    types["WebTokenOut"] = t.struct(
        {
            "enabledFeatures": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "parentFrameUrl": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebTokenOut"])
    types["HardwareStatusIn"] = t.struct(
        {
            "fanSpeeds": t.array(t.number()).optional(),
            "skinTemperatures": t.array(t.number()).optional(),
            "batteryTemperatures": t.array(t.number()).optional(),
            "cpuUsages": t.array(t.number()).optional(),
            "createTime": t.string().optional(),
            "cpuTemperatures": t.array(t.number()).optional(),
            "gpuTemperatures": t.array(t.number()).optional(),
        }
    ).named(renames["HardwareStatusIn"])
    types["HardwareStatusOut"] = t.struct(
        {
            "fanSpeeds": t.array(t.number()).optional(),
            "skinTemperatures": t.array(t.number()).optional(),
            "batteryTemperatures": t.array(t.number()).optional(),
            "cpuUsages": t.array(t.number()).optional(),
            "createTime": t.string().optional(),
            "cpuTemperatures": t.array(t.number()).optional(),
            "gpuTemperatures": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HardwareStatusOut"])
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
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
    types["LaunchAppActionIn"] = t.struct({"packageName": t.string().optional()}).named(
        renames["LaunchAppActionIn"]
    )
    types["LaunchAppActionOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchAppActionOut"])
    types["AlwaysOnVpnPackageIn"] = t.struct(
        {
            "lockdownEnabled": t.boolean().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["AlwaysOnVpnPackageIn"])
    types["AlwaysOnVpnPackageOut"] = t.struct(
        {
            "lockdownEnabled": t.boolean().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AlwaysOnVpnPackageOut"])
    types["PerAppResultIn"] = t.struct({"clearingResult": t.string().optional()}).named(
        renames["PerAppResultIn"]
    )
    types["PerAppResultOut"] = t.struct(
        {
            "clearingResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerAppResultOut"])
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

    functions = {}
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
    functions["enterprisesPatch"] = androidmanagement.post(
        "v1/enterprises",
        t.struct(
            {
                "projectId": t.string().optional(),
                "enterpriseToken": t.string().optional(),
                "signupUrlName": t.string().optional(),
                "agreementAccepted": t.boolean().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "name": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "pubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesList"] = androidmanagement.post(
        "v1/enterprises",
        t.struct(
            {
                "projectId": t.string().optional(),
                "enterpriseToken": t.string().optional(),
                "signupUrlName": t.string().optional(),
                "agreementAccepted": t.boolean().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "name": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "pubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDelete"] = androidmanagement.post(
        "v1/enterprises",
        t.struct(
            {
                "projectId": t.string().optional(),
                "enterpriseToken": t.string().optional(),
                "signupUrlName": t.string().optional(),
                "agreementAccepted": t.boolean().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "name": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "pubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGet"] = androidmanagement.post(
        "v1/enterprises",
        t.struct(
            {
                "projectId": t.string().optional(),
                "enterpriseToken": t.string().optional(),
                "signupUrlName": t.string().optional(),
                "agreementAccepted": t.boolean().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "name": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "pubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesCreate"] = androidmanagement.post(
        "v1/enterprises",
        t.struct(
            {
                "projectId": t.string().optional(),
                "enterpriseToken": t.string().optional(),
                "signupUrlName": t.string().optional(),
                "agreementAccepted": t.boolean().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "name": t.string().optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "pubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPoliciesList"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "keyguardDisabled": t.boolean().optional(),
                "skipFirstUseHintsEnabled": t.boolean().optional(),
                "appAutoUpdatePolicy": t.string().optional(),
                "shortSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "adjustVolumeDisabled": t.boolean().optional(),
                "cameraDisabled": t.boolean().optional(),
                "usbFileTransferDisabled": t.boolean().optional(),
                "kioskCustomLauncherEnabled": t.boolean().optional(),
                "microphoneAccess": t.string().optional(),
                "bluetoothDisabled": t.boolean().optional(),
                "locationMode": t.string().optional(),
                "debuggingFeaturesAllowed": t.boolean().optional(),
                "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
                "screenCaptureDisabled": t.boolean().optional(),
                "passwordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "crossProfilePolicies": t.proxy(
                    renames["CrossProfilePoliciesIn"]
                ).optional(),
                "modifyAccountsDisabled": t.boolean().optional(),
                "autoDateAndTimeZone": t.string().optional(),
                "permittedAccessibilityServices": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "bluetoothContactSharingDisabled": t.boolean().optional(),
                "shareLocationDisabled": t.boolean().optional(),
                "version": t.string().optional(),
                "applications": t.array(
                    t.proxy(renames["ApplicationPolicyIn"])
                ).optional(),
                "unmuteMicrophoneDisabled": t.boolean().optional(),
                "removeUserDisabled": t.boolean().optional(),
                "setUserIconDisabled": t.boolean().optional(),
                "minimumApiLevel": t.integer().optional(),
                "deviceConnectivityManagement": t.proxy(
                    renames["DeviceConnectivityManagementIn"]
                ).optional(),
                "networkEscapeHatchEnabled": t.boolean().optional(),
                "permittedInputMethods": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "usbMassStorageEnabled": t.boolean().optional(),
                "playStoreMode": t.string().optional(),
                "credentialsConfigDisabled": t.boolean().optional(),
                "androidDevicePolicyTracks": t.array(t.string()).optional(),
                "choosePrivateKeyRules": t.array(
                    t.proxy(renames["ChoosePrivateKeyRuleIn"])
                ).optional(),
                "complianceRules": t.array(
                    t.proxy(renames["ComplianceRuleIn"])
                ).optional(),
                "outgoingBeamDisabled": t.boolean().optional(),
                "cellBroadcastsConfigDisabled": t.boolean().optional(),
                "persistentPreferredActivities": t.array(
                    t.proxy(renames["PersistentPreferredActivityIn"])
                ).optional(),
                "statusBarDisabled": t.boolean().optional(),
                "statusReportingSettings": t.proxy(
                    renames["StatusReportingSettingsIn"]
                ).optional(),
                "deviceOwnerLockScreenInfo": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "tetheringConfigDisabled": t.boolean().optional(),
                "wifiConfigsLockdownEnabled": t.boolean().optional(),
                "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
                "openNetworkConfiguration": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "advancedSecurityOverrides": t.proxy(
                    renames["AdvancedSecurityOverridesIn"]
                ).optional(),
                "defaultPermissionPolicy": t.string().optional(),
                "passwordRequirements": t.proxy(
                    renames["PasswordRequirementsIn"]
                ).optional(),
                "frpAdminEmails": t.array(t.string()).optional(),
                "oncCertificateProviders": t.array(
                    t.proxy(renames["OncCertificateProviderIn"])
                ).optional(),
                "blockApplicationsEnabled": t.boolean().optional(),
                "outgoingCallsDisabled": t.boolean().optional(),
                "smsDisabled": t.boolean().optional(),
                "mobileNetworksConfigDisabled": t.boolean().optional(),
                "safeBootDisabled": t.boolean().optional(),
                "networkResetDisabled": t.boolean().optional(),
                "dataRoamingDisabled": t.boolean().optional(),
                "installUnknownSourcesAllowed": t.boolean().optional(),
                "longSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "createWindowsDisabled": t.boolean().optional(),
                "installAppsDisabled": t.boolean().optional(),
                "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
                "setWallpaperDisabled": t.boolean().optional(),
                "factoryResetDisabled": t.boolean().optional(),
                "personalUsagePolicies": t.proxy(
                    renames["PersonalUsagePoliciesIn"]
                ).optional(),
                "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
                "mountPhysicalMediaDisabled": t.boolean().optional(),
                "alwaysOnVpnPackage": t.proxy(
                    renames["AlwaysOnVpnPackageIn"]
                ).optional(),
                "wifiConfigDisabled": t.boolean().optional(),
                "ensureVerifyAppsEnabled": t.boolean().optional(),
                "uninstallAppsDisabled": t.boolean().optional(),
                "keyguardDisabledFeatures": t.array(t.string()).optional(),
                "kioskCustomization": t.proxy(
                    renames["KioskCustomizationIn"]
                ).optional(),
                "stayOnPluggedModes": t.array(t.string()).optional(),
                "privateKeySelectionEnabled": t.boolean().optional(),
                "encryptionPolicy": t.string().optional(),
                "policyEnforcementRules": t.array(
                    t.proxy(renames["PolicyEnforcementRuleIn"])
                ).optional(),
                "maximumTimeToLock": t.string().optional(),
                "preferentialNetworkService": t.string().optional(),
                "addUserDisabled": t.boolean().optional(),
                "bluetoothConfigDisabled": t.boolean().optional(),
                "cameraAccess": t.string().optional(),
                "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
                "autoTimeRequired": t.boolean().optional(),
                "funDisabled": t.boolean().optional(),
                "vpnConfigDisabled": t.boolean().optional(),
                "permissionGrants": t.array(
                    t.proxy(renames["PermissionGrantIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPoliciesGet"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "keyguardDisabled": t.boolean().optional(),
                "skipFirstUseHintsEnabled": t.boolean().optional(),
                "appAutoUpdatePolicy": t.string().optional(),
                "shortSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "adjustVolumeDisabled": t.boolean().optional(),
                "cameraDisabled": t.boolean().optional(),
                "usbFileTransferDisabled": t.boolean().optional(),
                "kioskCustomLauncherEnabled": t.boolean().optional(),
                "microphoneAccess": t.string().optional(),
                "bluetoothDisabled": t.boolean().optional(),
                "locationMode": t.string().optional(),
                "debuggingFeaturesAllowed": t.boolean().optional(),
                "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
                "screenCaptureDisabled": t.boolean().optional(),
                "passwordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "crossProfilePolicies": t.proxy(
                    renames["CrossProfilePoliciesIn"]
                ).optional(),
                "modifyAccountsDisabled": t.boolean().optional(),
                "autoDateAndTimeZone": t.string().optional(),
                "permittedAccessibilityServices": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "bluetoothContactSharingDisabled": t.boolean().optional(),
                "shareLocationDisabled": t.boolean().optional(),
                "version": t.string().optional(),
                "applications": t.array(
                    t.proxy(renames["ApplicationPolicyIn"])
                ).optional(),
                "unmuteMicrophoneDisabled": t.boolean().optional(),
                "removeUserDisabled": t.boolean().optional(),
                "setUserIconDisabled": t.boolean().optional(),
                "minimumApiLevel": t.integer().optional(),
                "deviceConnectivityManagement": t.proxy(
                    renames["DeviceConnectivityManagementIn"]
                ).optional(),
                "networkEscapeHatchEnabled": t.boolean().optional(),
                "permittedInputMethods": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "usbMassStorageEnabled": t.boolean().optional(),
                "playStoreMode": t.string().optional(),
                "credentialsConfigDisabled": t.boolean().optional(),
                "androidDevicePolicyTracks": t.array(t.string()).optional(),
                "choosePrivateKeyRules": t.array(
                    t.proxy(renames["ChoosePrivateKeyRuleIn"])
                ).optional(),
                "complianceRules": t.array(
                    t.proxy(renames["ComplianceRuleIn"])
                ).optional(),
                "outgoingBeamDisabled": t.boolean().optional(),
                "cellBroadcastsConfigDisabled": t.boolean().optional(),
                "persistentPreferredActivities": t.array(
                    t.proxy(renames["PersistentPreferredActivityIn"])
                ).optional(),
                "statusBarDisabled": t.boolean().optional(),
                "statusReportingSettings": t.proxy(
                    renames["StatusReportingSettingsIn"]
                ).optional(),
                "deviceOwnerLockScreenInfo": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "tetheringConfigDisabled": t.boolean().optional(),
                "wifiConfigsLockdownEnabled": t.boolean().optional(),
                "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
                "openNetworkConfiguration": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "advancedSecurityOverrides": t.proxy(
                    renames["AdvancedSecurityOverridesIn"]
                ).optional(),
                "defaultPermissionPolicy": t.string().optional(),
                "passwordRequirements": t.proxy(
                    renames["PasswordRequirementsIn"]
                ).optional(),
                "frpAdminEmails": t.array(t.string()).optional(),
                "oncCertificateProviders": t.array(
                    t.proxy(renames["OncCertificateProviderIn"])
                ).optional(),
                "blockApplicationsEnabled": t.boolean().optional(),
                "outgoingCallsDisabled": t.boolean().optional(),
                "smsDisabled": t.boolean().optional(),
                "mobileNetworksConfigDisabled": t.boolean().optional(),
                "safeBootDisabled": t.boolean().optional(),
                "networkResetDisabled": t.boolean().optional(),
                "dataRoamingDisabled": t.boolean().optional(),
                "installUnknownSourcesAllowed": t.boolean().optional(),
                "longSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "createWindowsDisabled": t.boolean().optional(),
                "installAppsDisabled": t.boolean().optional(),
                "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
                "setWallpaperDisabled": t.boolean().optional(),
                "factoryResetDisabled": t.boolean().optional(),
                "personalUsagePolicies": t.proxy(
                    renames["PersonalUsagePoliciesIn"]
                ).optional(),
                "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
                "mountPhysicalMediaDisabled": t.boolean().optional(),
                "alwaysOnVpnPackage": t.proxy(
                    renames["AlwaysOnVpnPackageIn"]
                ).optional(),
                "wifiConfigDisabled": t.boolean().optional(),
                "ensureVerifyAppsEnabled": t.boolean().optional(),
                "uninstallAppsDisabled": t.boolean().optional(),
                "keyguardDisabledFeatures": t.array(t.string()).optional(),
                "kioskCustomization": t.proxy(
                    renames["KioskCustomizationIn"]
                ).optional(),
                "stayOnPluggedModes": t.array(t.string()).optional(),
                "privateKeySelectionEnabled": t.boolean().optional(),
                "encryptionPolicy": t.string().optional(),
                "policyEnforcementRules": t.array(
                    t.proxy(renames["PolicyEnforcementRuleIn"])
                ).optional(),
                "maximumTimeToLock": t.string().optional(),
                "preferentialNetworkService": t.string().optional(),
                "addUserDisabled": t.boolean().optional(),
                "bluetoothConfigDisabled": t.boolean().optional(),
                "cameraAccess": t.string().optional(),
                "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
                "autoTimeRequired": t.boolean().optional(),
                "funDisabled": t.boolean().optional(),
                "vpnConfigDisabled": t.boolean().optional(),
                "permissionGrants": t.array(
                    t.proxy(renames["PermissionGrantIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPoliciesDelete"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "keyguardDisabled": t.boolean().optional(),
                "skipFirstUseHintsEnabled": t.boolean().optional(),
                "appAutoUpdatePolicy": t.string().optional(),
                "shortSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "adjustVolumeDisabled": t.boolean().optional(),
                "cameraDisabled": t.boolean().optional(),
                "usbFileTransferDisabled": t.boolean().optional(),
                "kioskCustomLauncherEnabled": t.boolean().optional(),
                "microphoneAccess": t.string().optional(),
                "bluetoothDisabled": t.boolean().optional(),
                "locationMode": t.string().optional(),
                "debuggingFeaturesAllowed": t.boolean().optional(),
                "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
                "screenCaptureDisabled": t.boolean().optional(),
                "passwordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "crossProfilePolicies": t.proxy(
                    renames["CrossProfilePoliciesIn"]
                ).optional(),
                "modifyAccountsDisabled": t.boolean().optional(),
                "autoDateAndTimeZone": t.string().optional(),
                "permittedAccessibilityServices": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "bluetoothContactSharingDisabled": t.boolean().optional(),
                "shareLocationDisabled": t.boolean().optional(),
                "version": t.string().optional(),
                "applications": t.array(
                    t.proxy(renames["ApplicationPolicyIn"])
                ).optional(),
                "unmuteMicrophoneDisabled": t.boolean().optional(),
                "removeUserDisabled": t.boolean().optional(),
                "setUserIconDisabled": t.boolean().optional(),
                "minimumApiLevel": t.integer().optional(),
                "deviceConnectivityManagement": t.proxy(
                    renames["DeviceConnectivityManagementIn"]
                ).optional(),
                "networkEscapeHatchEnabled": t.boolean().optional(),
                "permittedInputMethods": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "usbMassStorageEnabled": t.boolean().optional(),
                "playStoreMode": t.string().optional(),
                "credentialsConfigDisabled": t.boolean().optional(),
                "androidDevicePolicyTracks": t.array(t.string()).optional(),
                "choosePrivateKeyRules": t.array(
                    t.proxy(renames["ChoosePrivateKeyRuleIn"])
                ).optional(),
                "complianceRules": t.array(
                    t.proxy(renames["ComplianceRuleIn"])
                ).optional(),
                "outgoingBeamDisabled": t.boolean().optional(),
                "cellBroadcastsConfigDisabled": t.boolean().optional(),
                "persistentPreferredActivities": t.array(
                    t.proxy(renames["PersistentPreferredActivityIn"])
                ).optional(),
                "statusBarDisabled": t.boolean().optional(),
                "statusReportingSettings": t.proxy(
                    renames["StatusReportingSettingsIn"]
                ).optional(),
                "deviceOwnerLockScreenInfo": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "tetheringConfigDisabled": t.boolean().optional(),
                "wifiConfigsLockdownEnabled": t.boolean().optional(),
                "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
                "openNetworkConfiguration": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "advancedSecurityOverrides": t.proxy(
                    renames["AdvancedSecurityOverridesIn"]
                ).optional(),
                "defaultPermissionPolicy": t.string().optional(),
                "passwordRequirements": t.proxy(
                    renames["PasswordRequirementsIn"]
                ).optional(),
                "frpAdminEmails": t.array(t.string()).optional(),
                "oncCertificateProviders": t.array(
                    t.proxy(renames["OncCertificateProviderIn"])
                ).optional(),
                "blockApplicationsEnabled": t.boolean().optional(),
                "outgoingCallsDisabled": t.boolean().optional(),
                "smsDisabled": t.boolean().optional(),
                "mobileNetworksConfigDisabled": t.boolean().optional(),
                "safeBootDisabled": t.boolean().optional(),
                "networkResetDisabled": t.boolean().optional(),
                "dataRoamingDisabled": t.boolean().optional(),
                "installUnknownSourcesAllowed": t.boolean().optional(),
                "longSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "createWindowsDisabled": t.boolean().optional(),
                "installAppsDisabled": t.boolean().optional(),
                "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
                "setWallpaperDisabled": t.boolean().optional(),
                "factoryResetDisabled": t.boolean().optional(),
                "personalUsagePolicies": t.proxy(
                    renames["PersonalUsagePoliciesIn"]
                ).optional(),
                "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
                "mountPhysicalMediaDisabled": t.boolean().optional(),
                "alwaysOnVpnPackage": t.proxy(
                    renames["AlwaysOnVpnPackageIn"]
                ).optional(),
                "wifiConfigDisabled": t.boolean().optional(),
                "ensureVerifyAppsEnabled": t.boolean().optional(),
                "uninstallAppsDisabled": t.boolean().optional(),
                "keyguardDisabledFeatures": t.array(t.string()).optional(),
                "kioskCustomization": t.proxy(
                    renames["KioskCustomizationIn"]
                ).optional(),
                "stayOnPluggedModes": t.array(t.string()).optional(),
                "privateKeySelectionEnabled": t.boolean().optional(),
                "encryptionPolicy": t.string().optional(),
                "policyEnforcementRules": t.array(
                    t.proxy(renames["PolicyEnforcementRuleIn"])
                ).optional(),
                "maximumTimeToLock": t.string().optional(),
                "preferentialNetworkService": t.string().optional(),
                "addUserDisabled": t.boolean().optional(),
                "bluetoothConfigDisabled": t.boolean().optional(),
                "cameraAccess": t.string().optional(),
                "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
                "autoTimeRequired": t.boolean().optional(),
                "funDisabled": t.boolean().optional(),
                "vpnConfigDisabled": t.boolean().optional(),
                "permissionGrants": t.array(
                    t.proxy(renames["PermissionGrantIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPoliciesPatch"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "keyguardDisabled": t.boolean().optional(),
                "skipFirstUseHintsEnabled": t.boolean().optional(),
                "appAutoUpdatePolicy": t.string().optional(),
                "shortSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "adjustVolumeDisabled": t.boolean().optional(),
                "cameraDisabled": t.boolean().optional(),
                "usbFileTransferDisabled": t.boolean().optional(),
                "kioskCustomLauncherEnabled": t.boolean().optional(),
                "microphoneAccess": t.string().optional(),
                "bluetoothDisabled": t.boolean().optional(),
                "locationMode": t.string().optional(),
                "debuggingFeaturesAllowed": t.boolean().optional(),
                "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
                "screenCaptureDisabled": t.boolean().optional(),
                "passwordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "crossProfilePolicies": t.proxy(
                    renames["CrossProfilePoliciesIn"]
                ).optional(),
                "modifyAccountsDisabled": t.boolean().optional(),
                "autoDateAndTimeZone": t.string().optional(),
                "permittedAccessibilityServices": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "bluetoothContactSharingDisabled": t.boolean().optional(),
                "shareLocationDisabled": t.boolean().optional(),
                "version": t.string().optional(),
                "applications": t.array(
                    t.proxy(renames["ApplicationPolicyIn"])
                ).optional(),
                "unmuteMicrophoneDisabled": t.boolean().optional(),
                "removeUserDisabled": t.boolean().optional(),
                "setUserIconDisabled": t.boolean().optional(),
                "minimumApiLevel": t.integer().optional(),
                "deviceConnectivityManagement": t.proxy(
                    renames["DeviceConnectivityManagementIn"]
                ).optional(),
                "networkEscapeHatchEnabled": t.boolean().optional(),
                "permittedInputMethods": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "usbMassStorageEnabled": t.boolean().optional(),
                "playStoreMode": t.string().optional(),
                "credentialsConfigDisabled": t.boolean().optional(),
                "androidDevicePolicyTracks": t.array(t.string()).optional(),
                "choosePrivateKeyRules": t.array(
                    t.proxy(renames["ChoosePrivateKeyRuleIn"])
                ).optional(),
                "complianceRules": t.array(
                    t.proxy(renames["ComplianceRuleIn"])
                ).optional(),
                "outgoingBeamDisabled": t.boolean().optional(),
                "cellBroadcastsConfigDisabled": t.boolean().optional(),
                "persistentPreferredActivities": t.array(
                    t.proxy(renames["PersistentPreferredActivityIn"])
                ).optional(),
                "statusBarDisabled": t.boolean().optional(),
                "statusReportingSettings": t.proxy(
                    renames["StatusReportingSettingsIn"]
                ).optional(),
                "deviceOwnerLockScreenInfo": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "tetheringConfigDisabled": t.boolean().optional(),
                "wifiConfigsLockdownEnabled": t.boolean().optional(),
                "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
                "openNetworkConfiguration": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "advancedSecurityOverrides": t.proxy(
                    renames["AdvancedSecurityOverridesIn"]
                ).optional(),
                "defaultPermissionPolicy": t.string().optional(),
                "passwordRequirements": t.proxy(
                    renames["PasswordRequirementsIn"]
                ).optional(),
                "frpAdminEmails": t.array(t.string()).optional(),
                "oncCertificateProviders": t.array(
                    t.proxy(renames["OncCertificateProviderIn"])
                ).optional(),
                "blockApplicationsEnabled": t.boolean().optional(),
                "outgoingCallsDisabled": t.boolean().optional(),
                "smsDisabled": t.boolean().optional(),
                "mobileNetworksConfigDisabled": t.boolean().optional(),
                "safeBootDisabled": t.boolean().optional(),
                "networkResetDisabled": t.boolean().optional(),
                "dataRoamingDisabled": t.boolean().optional(),
                "installUnknownSourcesAllowed": t.boolean().optional(),
                "longSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "createWindowsDisabled": t.boolean().optional(),
                "installAppsDisabled": t.boolean().optional(),
                "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
                "setWallpaperDisabled": t.boolean().optional(),
                "factoryResetDisabled": t.boolean().optional(),
                "personalUsagePolicies": t.proxy(
                    renames["PersonalUsagePoliciesIn"]
                ).optional(),
                "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
                "mountPhysicalMediaDisabled": t.boolean().optional(),
                "alwaysOnVpnPackage": t.proxy(
                    renames["AlwaysOnVpnPackageIn"]
                ).optional(),
                "wifiConfigDisabled": t.boolean().optional(),
                "ensureVerifyAppsEnabled": t.boolean().optional(),
                "uninstallAppsDisabled": t.boolean().optional(),
                "keyguardDisabledFeatures": t.array(t.string()).optional(),
                "kioskCustomization": t.proxy(
                    renames["KioskCustomizationIn"]
                ).optional(),
                "stayOnPluggedModes": t.array(t.string()).optional(),
                "privateKeySelectionEnabled": t.boolean().optional(),
                "encryptionPolicy": t.string().optional(),
                "policyEnforcementRules": t.array(
                    t.proxy(renames["PolicyEnforcementRuleIn"])
                ).optional(),
                "maximumTimeToLock": t.string().optional(),
                "preferentialNetworkService": t.string().optional(),
                "addUserDisabled": t.boolean().optional(),
                "bluetoothConfigDisabled": t.boolean().optional(),
                "cameraAccess": t.string().optional(),
                "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
                "autoTimeRequired": t.boolean().optional(),
                "funDisabled": t.boolean().optional(),
                "vpnConfigDisabled": t.boolean().optional(),
                "permissionGrants": t.array(
                    t.proxy(renames["PermissionGrantIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebTokensCreate"] = androidmanagement.post(
        "v1/{parent}/webTokens",
        t.struct(
            {
                "parent": t.string().optional(),
                "enabledFeatures": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "parentFrameUrl": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "value": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebTokenOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnrollmentTokensList"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnrollmentTokensGet"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnrollmentTokensCreate"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnrollmentTokensDelete"] = androidmanagement.delete(
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
    functions["enterprisesWebAppsCreate"] = androidmanagement.delete(
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
    functions["enterprisesDevicesGet"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "lastPolicySyncTime": t.string().optional(),
                "state": t.string().optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "lastStatusReportTime": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "policyName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "ownership": t.string().optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "apiLevel": t.integer().optional(),
                "enrollmentTokenName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "appliedState": t.string().optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "policyCompliant": t.boolean().optional(),
                "appliedPolicyName": t.string().optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "enrollmentTokenData": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "userName": t.string().optional(),
                "enrollmentTime": t.string().optional(),
                "managementMode": t.string().optional(),
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
                "state": t.string().optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "lastStatusReportTime": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "policyName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "ownership": t.string().optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "apiLevel": t.integer().optional(),
                "enrollmentTokenName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "appliedState": t.string().optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "policyCompliant": t.boolean().optional(),
                "appliedPolicyName": t.string().optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "enrollmentTokenData": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "userName": t.string().optional(),
                "enrollmentTime": t.string().optional(),
                "managementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
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
                "state": t.string().optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "lastStatusReportTime": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "policyName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "ownership": t.string().optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "apiLevel": t.integer().optional(),
                "enrollmentTokenName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "appliedState": t.string().optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "policyCompliant": t.boolean().optional(),
                "appliedPolicyName": t.string().optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "enrollmentTokenData": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "userName": t.string().optional(),
                "enrollmentTime": t.string().optional(),
                "managementMode": t.string().optional(),
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
                "state": t.string().optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "lastStatusReportTime": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "policyName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "ownership": t.string().optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "apiLevel": t.integer().optional(),
                "enrollmentTokenName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "appliedState": t.string().optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "policyCompliant": t.boolean().optional(),
                "appliedPolicyName": t.string().optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "enrollmentTokenData": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "userName": t.string().optional(),
                "enrollmentTime": t.string().optional(),
                "managementMode": t.string().optional(),
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
                "state": t.string().optional(),
                "nonComplianceDetails": t.array(
                    t.proxy(renames["NonComplianceDetailIn"])
                ).optional(),
                "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
                "lastPolicyComplianceReportTime": t.string().optional(),
                "powerManagementEvents": t.array(
                    t.proxy(renames["PowerManagementEventIn"])
                ).optional(),
                "user": t.proxy(renames["UserIn"]).optional(),
                "applicationReports": t.array(
                    t.proxy(renames["ApplicationReportIn"])
                ).optional(),
                "systemProperties": t.struct({"_": t.string().optional()}).optional(),
                "lastStatusReportTime": t.string().optional(),
                "appliedPasswordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "policyName": t.string().optional(),
                "previousDeviceNames": t.array(t.string()).optional(),
                "ownership": t.string().optional(),
                "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
                "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
                "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
                "appliedPolicyVersion": t.string().optional(),
                "hardwareStatusSamples": t.array(
                    t.proxy(renames["HardwareStatusIn"])
                ).optional(),
                "apiLevel": t.integer().optional(),
                "enrollmentTokenName": t.string().optional(),
                "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
                "appliedState": t.string().optional(),
                "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
                "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
                "policyCompliant": t.boolean().optional(),
                "appliedPolicyName": t.string().optional(),
                "commonCriteriaModeInfo": t.proxy(
                    renames["CommonCriteriaModeInfoIn"]
                ).optional(),
                "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
                "enrollmentTokenData": t.string().optional(),
                "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
                "userName": t.string().optional(),
                "enrollmentTime": t.string().optional(),
                "managementMode": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsList"] = androidmanagement.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsGet"] = androidmanagement.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsDelete"] = androidmanagement.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsCancel"] = androidmanagement.post(
        "v1/{name}:cancel",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="androidmanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
