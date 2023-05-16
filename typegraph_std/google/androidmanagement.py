from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_androidmanagement() -> Import:
    androidmanagement = HTTPRuntime("https://androidmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_androidmanagement_1_ErrorResponse",
        "FilePushedEventIn": "_androidmanagement_2_FilePushedEventIn",
        "FilePushedEventOut": "_androidmanagement_3_FilePushedEventOut",
        "DeviceSettingsIn": "_androidmanagement_4_DeviceSettingsIn",
        "DeviceSettingsOut": "_androidmanagement_5_DeviceSettingsOut",
        "WipeActionIn": "_androidmanagement_6_WipeActionIn",
        "WipeActionOut": "_androidmanagement_7_WipeActionOut",
        "FilePulledEventIn": "_androidmanagement_8_FilePulledEventIn",
        "FilePulledEventOut": "_androidmanagement_9_FilePulledEventOut",
        "KeyguardSecuredEventIn": "_androidmanagement_10_KeyguardSecuredEventIn",
        "KeyguardSecuredEventOut": "_androidmanagement_11_KeyguardSecuredEventOut",
        "ManagedConfigurationTemplateIn": "_androidmanagement_12_ManagedConfigurationTemplateIn",
        "ManagedConfigurationTemplateOut": "_androidmanagement_13_ManagedConfigurationTemplateOut",
        "SystemUpdateInfoIn": "_androidmanagement_14_SystemUpdateInfoIn",
        "SystemUpdateInfoOut": "_androidmanagement_15_SystemUpdateInfoOut",
        "SecurityPostureIn": "_androidmanagement_16_SecurityPostureIn",
        "SecurityPostureOut": "_androidmanagement_17_SecurityPostureOut",
        "UserFacingMessageIn": "_androidmanagement_18_UserFacingMessageIn",
        "UserFacingMessageOut": "_androidmanagement_19_UserFacingMessageOut",
        "UsageLogIn": "_androidmanagement_20_UsageLogIn",
        "UsageLogOut": "_androidmanagement_21_UsageLogOut",
        "WebTokenIn": "_androidmanagement_22_WebTokenIn",
        "WebTokenOut": "_androidmanagement_23_WebTokenOut",
        "OsShutdownEventIn": "_androidmanagement_24_OsShutdownEventIn",
        "OsShutdownEventOut": "_androidmanagement_25_OsShutdownEventOut",
        "ApplicationPermissionIn": "_androidmanagement_26_ApplicationPermissionIn",
        "ApplicationPermissionOut": "_androidmanagement_27_ApplicationPermissionOut",
        "PowerManagementEventIn": "_androidmanagement_28_PowerManagementEventIn",
        "PowerManagementEventOut": "_androidmanagement_29_PowerManagementEventOut",
        "EmptyIn": "_androidmanagement_30_EmptyIn",
        "EmptyOut": "_androidmanagement_31_EmptyOut",
        "ApplicationEventIn": "_androidmanagement_32_ApplicationEventIn",
        "ApplicationEventOut": "_androidmanagement_33_ApplicationEventOut",
        "ApplicationIn": "_androidmanagement_34_ApplicationIn",
        "ApplicationOut": "_androidmanagement_35_ApplicationOut",
        "MemoryEventIn": "_androidmanagement_36_MemoryEventIn",
        "MemoryEventOut": "_androidmanagement_37_MemoryEventOut",
        "PersonalUsagePoliciesIn": "_androidmanagement_38_PersonalUsagePoliciesIn",
        "PersonalUsagePoliciesOut": "_androidmanagement_39_PersonalUsagePoliciesOut",
        "KioskCustomizationIn": "_androidmanagement_40_KioskCustomizationIn",
        "KioskCustomizationOut": "_androidmanagement_41_KioskCustomizationOut",
        "AppVersionIn": "_androidmanagement_42_AppVersionIn",
        "AppVersionOut": "_androidmanagement_43_AppVersionOut",
        "PermissionGrantIn": "_androidmanagement_44_PermissionGrantIn",
        "PermissionGrantOut": "_androidmanagement_45_PermissionGrantOut",
        "ExtensionConfigIn": "_androidmanagement_46_ExtensionConfigIn",
        "ExtensionConfigOut": "_androidmanagement_47_ExtensionConfigOut",
        "LogBufferSizeCriticalEventIn": "_androidmanagement_48_LogBufferSizeCriticalEventIn",
        "LogBufferSizeCriticalEventOut": "_androidmanagement_49_LogBufferSizeCriticalEventOut",
        "BlockActionIn": "_androidmanagement_50_BlockActionIn",
        "BlockActionOut": "_androidmanagement_51_BlockActionOut",
        "NetworkInfoIn": "_androidmanagement_52_NetworkInfoIn",
        "NetworkInfoOut": "_androidmanagement_53_NetworkInfoOut",
        "MemoryInfoIn": "_androidmanagement_54_MemoryInfoIn",
        "MemoryInfoOut": "_androidmanagement_55_MemoryInfoOut",
        "SoftwareInfoIn": "_androidmanagement_56_SoftwareInfoIn",
        "SoftwareInfoOut": "_androidmanagement_57_SoftwareInfoOut",
        "OncCertificateProviderIn": "_androidmanagement_58_OncCertificateProviderIn",
        "OncCertificateProviderOut": "_androidmanagement_59_OncCertificateProviderOut",
        "KeyguardDismissAuthAttemptEventIn": "_androidmanagement_60_KeyguardDismissAuthAttemptEventIn",
        "KeyguardDismissAuthAttemptEventOut": "_androidmanagement_61_KeyguardDismissAuthAttemptEventOut",
        "UserIn": "_androidmanagement_62_UserIn",
        "UserOut": "_androidmanagement_63_UserOut",
        "UsageLogEventIn": "_androidmanagement_64_UsageLogEventIn",
        "UsageLogEventOut": "_androidmanagement_65_UsageLogEventOut",
        "ApiLevelConditionIn": "_androidmanagement_66_ApiLevelConditionIn",
        "ApiLevelConditionOut": "_androidmanagement_67_ApiLevelConditionOut",
        "AlwaysOnVpnPackageIn": "_androidmanagement_68_AlwaysOnVpnPackageIn",
        "AlwaysOnVpnPackageOut": "_androidmanagement_69_AlwaysOnVpnPackageOut",
        "LoggingStartedEventIn": "_androidmanagement_70_LoggingStartedEventIn",
        "LoggingStartedEventOut": "_androidmanagement_71_LoggingStartedEventOut",
        "ListOperationsResponseIn": "_androidmanagement_72_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_androidmanagement_73_ListOperationsResponseOut",
        "AdvancedSecurityOverridesIn": "_androidmanagement_74_AdvancedSecurityOverridesIn",
        "AdvancedSecurityOverridesOut": "_androidmanagement_75_AdvancedSecurityOverridesOut",
        "ExternalDataIn": "_androidmanagement_76_ExternalDataIn",
        "ExternalDataOut": "_androidmanagement_77_ExternalDataOut",
        "ManagedPropertyIn": "_androidmanagement_78_ManagedPropertyIn",
        "ManagedPropertyOut": "_androidmanagement_79_ManagedPropertyOut",
        "ManagedPropertyEntryIn": "_androidmanagement_80_ManagedPropertyEntryIn",
        "ManagedPropertyEntryOut": "_androidmanagement_81_ManagedPropertyEntryOut",
        "ApplicationReportIn": "_androidmanagement_82_ApplicationReportIn",
        "ApplicationReportOut": "_androidmanagement_83_ApplicationReportOut",
        "CertValidationFailureEventIn": "_androidmanagement_84_CertValidationFailureEventIn",
        "CertValidationFailureEventOut": "_androidmanagement_85_CertValidationFailureEventOut",
        "SpecificNonComplianceContextIn": "_androidmanagement_86_SpecificNonComplianceContextIn",
        "SpecificNonComplianceContextOut": "_androidmanagement_87_SpecificNonComplianceContextOut",
        "ContentProviderEndpointIn": "_androidmanagement_88_ContentProviderEndpointIn",
        "ContentProviderEndpointOut": "_androidmanagement_89_ContentProviderEndpointOut",
        "ListWebAppsResponseIn": "_androidmanagement_90_ListWebAppsResponseIn",
        "ListWebAppsResponseOut": "_androidmanagement_91_ListWebAppsResponseOut",
        "DeviceConnectivityManagementIn": "_androidmanagement_92_DeviceConnectivityManagementIn",
        "DeviceConnectivityManagementOut": "_androidmanagement_93_DeviceConnectivityManagementOut",
        "SignupUrlIn": "_androidmanagement_94_SignupUrlIn",
        "SignupUrlOut": "_androidmanagement_95_SignupUrlOut",
        "AdbShellCommandEventIn": "_androidmanagement_96_AdbShellCommandEventIn",
        "AdbShellCommandEventOut": "_androidmanagement_97_AdbShellCommandEventOut",
        "HardwareInfoIn": "_androidmanagement_98_HardwareInfoIn",
        "HardwareInfoOut": "_androidmanagement_99_HardwareInfoOut",
        "ClearAppsDataParamsIn": "_androidmanagement_100_ClearAppsDataParamsIn",
        "ClearAppsDataParamsOut": "_androidmanagement_101_ClearAppsDataParamsOut",
        "KeyedAppStateIn": "_androidmanagement_102_KeyedAppStateIn",
        "KeyedAppStateOut": "_androidmanagement_103_KeyedAppStateOut",
        "PolicyIn": "_androidmanagement_104_PolicyIn",
        "PolicyOut": "_androidmanagement_105_PolicyOut",
        "PolicyEnforcementRuleIn": "_androidmanagement_106_PolicyEnforcementRuleIn",
        "PolicyEnforcementRuleOut": "_androidmanagement_107_PolicyEnforcementRuleOut",
        "SystemUpdateIn": "_androidmanagement_108_SystemUpdateIn",
        "SystemUpdateOut": "_androidmanagement_109_SystemUpdateOut",
        "NonComplianceDetailIn": "_androidmanagement_110_NonComplianceDetailIn",
        "NonComplianceDetailOut": "_androidmanagement_111_NonComplianceDetailOut",
        "PackageNameListIn": "_androidmanagement_112_PackageNameListIn",
        "PackageNameListOut": "_androidmanagement_113_PackageNameListOut",
        "WebAppIn": "_androidmanagement_114_WebAppIn",
        "WebAppOut": "_androidmanagement_115_WebAppOut",
        "WebAppIconIn": "_androidmanagement_116_WebAppIconIn",
        "WebAppIconOut": "_androidmanagement_117_WebAppIconOut",
        "ProxyInfoIn": "_androidmanagement_118_ProxyInfoIn",
        "ProxyInfoOut": "_androidmanagement_119_ProxyInfoOut",
        "FreezePeriodIn": "_androidmanagement_120_FreezePeriodIn",
        "FreezePeriodOut": "_androidmanagement_121_FreezePeriodOut",
        "StatusIn": "_androidmanagement_122_StatusIn",
        "StatusOut": "_androidmanagement_123_StatusOut",
        "EnrollmentTokenIn": "_androidmanagement_124_EnrollmentTokenIn",
        "EnrollmentTokenOut": "_androidmanagement_125_EnrollmentTokenOut",
        "ChoosePrivateKeyRuleIn": "_androidmanagement_126_ChoosePrivateKeyRuleIn",
        "ChoosePrivateKeyRuleOut": "_androidmanagement_127_ChoosePrivateKeyRuleOut",
        "BatchUsageLogEventsIn": "_androidmanagement_128_BatchUsageLogEventsIn",
        "BatchUsageLogEventsOut": "_androidmanagement_129_BatchUsageLogEventsOut",
        "ComplianceRuleIn": "_androidmanagement_130_ComplianceRuleIn",
        "ComplianceRuleOut": "_androidmanagement_131_ComplianceRuleOut",
        "OperationIn": "_androidmanagement_132_OperationIn",
        "OperationOut": "_androidmanagement_133_OperationOut",
        "PasswordRequirementsIn": "_androidmanagement_134_PasswordRequirementsIn",
        "PasswordRequirementsOut": "_androidmanagement_135_PasswordRequirementsOut",
        "LoggingStoppedEventIn": "_androidmanagement_136_LoggingStoppedEventIn",
        "LoggingStoppedEventOut": "_androidmanagement_137_LoggingStoppedEventOut",
        "StatusReportingSettingsIn": "_androidmanagement_138_StatusReportingSettingsIn",
        "StatusReportingSettingsOut": "_androidmanagement_139_StatusReportingSettingsOut",
        "SetupActionIn": "_androidmanagement_140_SetupActionIn",
        "SetupActionOut": "_androidmanagement_141_SetupActionOut",
        "PostureDetailIn": "_androidmanagement_142_PostureDetailIn",
        "PostureDetailOut": "_androidmanagement_143_PostureDetailOut",
        "ListEnterprisesResponseIn": "_androidmanagement_144_ListEnterprisesResponseIn",
        "ListEnterprisesResponseOut": "_androidmanagement_145_ListEnterprisesResponseOut",
        "ConnectEventIn": "_androidmanagement_146_ConnectEventIn",
        "ConnectEventOut": "_androidmanagement_147_ConnectEventOut",
        "DnsEventIn": "_androidmanagement_148_DnsEventIn",
        "DnsEventOut": "_androidmanagement_149_DnsEventOut",
        "AdbShellInteractiveEventIn": "_androidmanagement_150_AdbShellInteractiveEventIn",
        "AdbShellInteractiveEventOut": "_androidmanagement_151_AdbShellInteractiveEventOut",
        "AppProcessInfoIn": "_androidmanagement_152_AppProcessInfoIn",
        "AppProcessInfoOut": "_androidmanagement_153_AppProcessInfoOut",
        "OsStartupEventIn": "_androidmanagement_154_OsStartupEventIn",
        "OsStartupEventOut": "_androidmanagement_155_OsStartupEventOut",
        "TermsAndConditionsIn": "_androidmanagement_156_TermsAndConditionsIn",
        "TermsAndConditionsOut": "_androidmanagement_157_TermsAndConditionsOut",
        "CryptoSelfTestCompletedEventIn": "_androidmanagement_158_CryptoSelfTestCompletedEventIn",
        "CryptoSelfTestCompletedEventOut": "_androidmanagement_159_CryptoSelfTestCompletedEventOut",
        "CrossProfilePoliciesIn": "_androidmanagement_160_CrossProfilePoliciesIn",
        "CrossProfilePoliciesOut": "_androidmanagement_161_CrossProfilePoliciesOut",
        "ListEnrollmentTokensResponseIn": "_androidmanagement_162_ListEnrollmentTokensResponseIn",
        "ListEnrollmentTokensResponseOut": "_androidmanagement_163_ListEnrollmentTokensResponseOut",
        "DateIn": "_androidmanagement_164_DateIn",
        "DateOut": "_androidmanagement_165_DateOut",
        "PasswordPoliciesContextIn": "_androidmanagement_166_PasswordPoliciesContextIn",
        "PasswordPoliciesContextOut": "_androidmanagement_167_PasswordPoliciesContextOut",
        "ApplicationReportingSettingsIn": "_androidmanagement_168_ApplicationReportingSettingsIn",
        "ApplicationReportingSettingsOut": "_androidmanagement_169_ApplicationReportingSettingsOut",
        "AppProcessStartEventIn": "_androidmanagement_170_AppProcessStartEventIn",
        "AppProcessStartEventOut": "_androidmanagement_171_AppProcessStartEventOut",
        "ListDevicesResponseIn": "_androidmanagement_172_ListDevicesResponseIn",
        "ListDevicesResponseOut": "_androidmanagement_173_ListDevicesResponseOut",
        "CommandIn": "_androidmanagement_174_CommandIn",
        "CommandOut": "_androidmanagement_175_CommandOut",
        "CertAuthorityInstalledEventIn": "_androidmanagement_176_CertAuthorityInstalledEventIn",
        "CertAuthorityInstalledEventOut": "_androidmanagement_177_CertAuthorityInstalledEventOut",
        "TelephonyInfoIn": "_androidmanagement_178_TelephonyInfoIn",
        "TelephonyInfoOut": "_androidmanagement_179_TelephonyInfoOut",
        "KeyIntegrityViolationEventIn": "_androidmanagement_180_KeyIntegrityViolationEventIn",
        "KeyIntegrityViolationEventOut": "_androidmanagement_181_KeyIntegrityViolationEventOut",
        "NonComplianceDetailConditionIn": "_androidmanagement_182_NonComplianceDetailConditionIn",
        "NonComplianceDetailConditionOut": "_androidmanagement_183_NonComplianceDetailConditionOut",
        "SigninDetailIn": "_androidmanagement_184_SigninDetailIn",
        "SigninDetailOut": "_androidmanagement_185_SigninDetailOut",
        "HardwareStatusIn": "_androidmanagement_186_HardwareStatusIn",
        "HardwareStatusOut": "_androidmanagement_187_HardwareStatusOut",
        "ListPoliciesResponseIn": "_androidmanagement_188_ListPoliciesResponseIn",
        "ListPoliciesResponseOut": "_androidmanagement_189_ListPoliciesResponseOut",
        "PersonalApplicationPolicyIn": "_androidmanagement_190_PersonalApplicationPolicyIn",
        "PersonalApplicationPolicyOut": "_androidmanagement_191_PersonalApplicationPolicyOut",
        "OncWifiContextIn": "_androidmanagement_192_OncWifiContextIn",
        "OncWifiContextOut": "_androidmanagement_193_OncWifiContextOut",
        "ContactInfoIn": "_androidmanagement_194_ContactInfoIn",
        "ContactInfoOut": "_androidmanagement_195_ContactInfoOut",
        "MediaMountEventIn": "_androidmanagement_196_MediaMountEventIn",
        "MediaMountEventOut": "_androidmanagement_197_MediaMountEventOut",
        "KeyImportEventIn": "_androidmanagement_198_KeyImportEventIn",
        "KeyImportEventOut": "_androidmanagement_199_KeyImportEventOut",
        "KeyGeneratedEventIn": "_androidmanagement_200_KeyGeneratedEventIn",
        "KeyGeneratedEventOut": "_androidmanagement_201_KeyGeneratedEventOut",
        "LaunchAppActionIn": "_androidmanagement_202_LaunchAppActionIn",
        "LaunchAppActionOut": "_androidmanagement_203_LaunchAppActionOut",
        "KeyDestructionEventIn": "_androidmanagement_204_KeyDestructionEventIn",
        "KeyDestructionEventOut": "_androidmanagement_205_KeyDestructionEventOut",
        "DisplayIn": "_androidmanagement_206_DisplayIn",
        "DisplayOut": "_androidmanagement_207_DisplayOut",
        "ApplicationPolicyIn": "_androidmanagement_208_ApplicationPolicyIn",
        "ApplicationPolicyOut": "_androidmanagement_209_ApplicationPolicyOut",
        "KeyguardDismissedEventIn": "_androidmanagement_210_KeyguardDismissedEventIn",
        "KeyguardDismissedEventOut": "_androidmanagement_211_KeyguardDismissedEventOut",
        "DeviceIn": "_androidmanagement_212_DeviceIn",
        "DeviceOut": "_androidmanagement_213_DeviceOut",
        "CommonCriteriaModeInfoIn": "_androidmanagement_214_CommonCriteriaModeInfoIn",
        "CommonCriteriaModeInfoOut": "_androidmanagement_215_CommonCriteriaModeInfoOut",
        "PerAppResultIn": "_androidmanagement_216_PerAppResultIn",
        "PerAppResultOut": "_androidmanagement_217_PerAppResultOut",
        "CertAuthorityRemovedEventIn": "_androidmanagement_218_CertAuthorityRemovedEventIn",
        "CertAuthorityRemovedEventOut": "_androidmanagement_219_CertAuthorityRemovedEventOut",
        "PersistentPreferredActivityIn": "_androidmanagement_220_PersistentPreferredActivityIn",
        "PersistentPreferredActivityOut": "_androidmanagement_221_PersistentPreferredActivityOut",
        "WipeFailureEventIn": "_androidmanagement_222_WipeFailureEventIn",
        "WipeFailureEventOut": "_androidmanagement_223_WipeFailureEventOut",
        "EnterpriseIn": "_androidmanagement_224_EnterpriseIn",
        "EnterpriseOut": "_androidmanagement_225_EnterpriseOut",
        "RemoteLockEventIn": "_androidmanagement_226_RemoteLockEventIn",
        "RemoteLockEventOut": "_androidmanagement_227_RemoteLockEventOut",
        "MediaUnmountEventIn": "_androidmanagement_228_MediaUnmountEventIn",
        "MediaUnmountEventOut": "_androidmanagement_229_MediaUnmountEventOut",
        "AppTrackInfoIn": "_androidmanagement_230_AppTrackInfoIn",
        "AppTrackInfoOut": "_androidmanagement_231_AppTrackInfoOut",
        "IssueCommandResponseIn": "_androidmanagement_232_IssueCommandResponseIn",
        "IssueCommandResponseOut": "_androidmanagement_233_IssueCommandResponseOut",
        "ClearAppsDataStatusIn": "_androidmanagement_234_ClearAppsDataStatusIn",
        "ClearAppsDataStatusOut": "_androidmanagement_235_ClearAppsDataStatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["FilePushedEventIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FilePushedEventIn"]
    )
    types["FilePushedEventOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilePushedEventOut"])
    types["DeviceSettingsIn"] = t.struct(
        {
            "verifyAppsEnabled": t.boolean().optional(),
            "isEncrypted": t.boolean().optional(),
            "isDeviceSecure": t.boolean().optional(),
            "encryptionStatus": t.string().optional(),
            "unknownSourcesEnabled": t.boolean().optional(),
            "adbEnabled": t.boolean().optional(),
            "developmentSettingsEnabled": t.boolean().optional(),
        }
    ).named(renames["DeviceSettingsIn"])
    types["DeviceSettingsOut"] = t.struct(
        {
            "verifyAppsEnabled": t.boolean().optional(),
            "isEncrypted": t.boolean().optional(),
            "isDeviceSecure": t.boolean().optional(),
            "encryptionStatus": t.string().optional(),
            "unknownSourcesEnabled": t.boolean().optional(),
            "adbEnabled": t.boolean().optional(),
            "developmentSettingsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSettingsOut"])
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
    types["FilePulledEventIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FilePulledEventIn"]
    )
    types["FilePulledEventOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilePulledEventOut"])
    types["KeyguardSecuredEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyguardSecuredEventIn"]
    )
    types["KeyguardSecuredEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["KeyguardSecuredEventOut"])
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
    types["SecurityPostureIn"] = t.struct(
        {
            "postureDetails": t.array(t.proxy(renames["PostureDetailIn"])).optional(),
            "devicePosture": t.string().optional(),
        }
    ).named(renames["SecurityPostureIn"])
    types["SecurityPostureOut"] = t.struct(
        {
            "postureDetails": t.array(t.proxy(renames["PostureDetailOut"])).optional(),
            "devicePosture": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecurityPostureOut"])
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
    types["UsageLogIn"] = t.struct(
        {
            "uploadOnCellularAllowed": t.array(t.string()).optional(),
            "enabledLogTypes": t.array(t.string()).optional(),
        }
    ).named(renames["UsageLogIn"])
    types["UsageLogOut"] = t.struct(
        {
            "uploadOnCellularAllowed": t.array(t.string()).optional(),
            "enabledLogTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageLogOut"])
    types["WebTokenIn"] = t.struct(
        {
            "enabledFeatures": t.array(t.string()).optional(),
            "permissions": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "parentFrameUrl": t.string().optional(),
        }
    ).named(renames["WebTokenIn"])
    types["WebTokenOut"] = t.struct(
        {
            "enabledFeatures": t.array(t.string()).optional(),
            "permissions": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "parentFrameUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebTokenOut"])
    types["OsShutdownEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OsShutdownEventIn"]
    )
    types["OsShutdownEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OsShutdownEventOut"])
    types["ApplicationPermissionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "permissionId": t.string().optional(),
        }
    ).named(renames["ApplicationPermissionIn"])
    types["ApplicationPermissionOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "permissionId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationPermissionOut"])
    types["PowerManagementEventIn"] = t.struct(
        {
            "eventType": t.string().optional(),
            "batteryLevel": t.number().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["PowerManagementEventIn"])
    types["PowerManagementEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "batteryLevel": t.number().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PowerManagementEventOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ApplicationEventIn"] = t.struct(
        {"createTime": t.string().optional(), "eventType": t.string().optional()}
    ).named(renames["ApplicationEventIn"])
    types["ApplicationEventOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "eventType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationEventOut"])
    types["ApplicationIn"] = t.struct(
        {
            "iconUrl": t.string().optional(),
            "author": t.string().optional(),
            "name": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "permissions": t.array(
                t.proxy(renames["ApplicationPermissionIn"])
            ).optional(),
            "fullDescription": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "playStoreUrl": t.string().optional(),
            "smallIconUrl": t.string().optional(),
            "appVersions": t.array(t.proxy(renames["AppVersionIn"])).optional(),
            "category": t.string().optional(),
            "appTracks": t.array(t.proxy(renames["AppTrackInfoIn"])).optional(),
            "contentRating": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "distributionChannel": t.string().optional(),
            "recentChanges": t.string().optional(),
            "managedProperties": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
            "appPricing": t.string().optional(),
            "availableCountries": t.array(t.string()).optional(),
            "minAndroidSdkVersion": t.integer().optional(),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "iconUrl": t.string().optional(),
            "author": t.string().optional(),
            "name": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "permissions": t.array(
                t.proxy(renames["ApplicationPermissionOut"])
            ).optional(),
            "fullDescription": t.string().optional(),
            "features": t.array(t.string()).optional(),
            "playStoreUrl": t.string().optional(),
            "smallIconUrl": t.string().optional(),
            "appVersions": t.array(t.proxy(renames["AppVersionOut"])).optional(),
            "category": t.string().optional(),
            "appTracks": t.array(t.proxy(renames["AppTrackInfoOut"])).optional(),
            "updateTime": t.string().optional(),
            "contentRating": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "distributionChannel": t.string().optional(),
            "recentChanges": t.string().optional(),
            "managedProperties": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "appPricing": t.string().optional(),
            "availableCountries": t.array(t.string()).optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
    types["MemoryEventIn"] = t.struct(
        {
            "eventType": t.string().optional(),
            "byteCount": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["MemoryEventIn"])
    types["MemoryEventOut"] = t.struct(
        {
            "eventType": t.string().optional(),
            "byteCount": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MemoryEventOut"])
    types["PersonalUsagePoliciesIn"] = t.struct(
        {
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "personalPlayStoreMode": t.string().optional(),
            "cameraDisabled": t.boolean().optional(),
            "maxDaysWithWorkOff": t.integer().optional(),
            "personalApplications": t.array(
                t.proxy(renames["PersonalApplicationPolicyIn"])
            ).optional(),
            "screenCaptureDisabled": t.boolean().optional(),
        }
    ).named(renames["PersonalUsagePoliciesIn"])
    types["PersonalUsagePoliciesOut"] = t.struct(
        {
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "personalPlayStoreMode": t.string().optional(),
            "cameraDisabled": t.boolean().optional(),
            "maxDaysWithWorkOff": t.integer().optional(),
            "personalApplications": t.array(
                t.proxy(renames["PersonalApplicationPolicyOut"])
            ).optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalUsagePoliciesOut"])
    types["KioskCustomizationIn"] = t.struct(
        {
            "deviceSettings": t.string().optional(),
            "statusBar": t.string().optional(),
            "systemNavigation": t.string().optional(),
            "powerButtonActions": t.string().optional(),
            "systemErrorWarnings": t.string().optional(),
        }
    ).named(renames["KioskCustomizationIn"])
    types["KioskCustomizationOut"] = t.struct(
        {
            "deviceSettings": t.string().optional(),
            "statusBar": t.string().optional(),
            "systemNavigation": t.string().optional(),
            "powerButtonActions": t.string().optional(),
            "systemErrorWarnings": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KioskCustomizationOut"])
    types["AppVersionIn"] = t.struct(
        {
            "versionString": t.string().optional(),
            "versionCode": t.integer().optional(),
            "trackIds": t.array(t.string()).optional(),
            "production": t.boolean().optional(),
        }
    ).named(renames["AppVersionIn"])
    types["AppVersionOut"] = t.struct(
        {
            "versionString": t.string().optional(),
            "versionCode": t.integer().optional(),
            "trackIds": t.array(t.string()).optional(),
            "production": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppVersionOut"])
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
    types["LogBufferSizeCriticalEventIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["LogBufferSizeCriticalEventIn"])
    types["LogBufferSizeCriticalEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LogBufferSizeCriticalEventOut"])
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
    types["NetworkInfoIn"] = t.struct(
        {
            "imei": t.string().optional(),
            "meid": t.string().optional(),
            "networkOperatorName": t.string().optional(),
            "wifiMacAddress": t.string().optional(),
            "telephonyInfos": t.array(t.proxy(renames["TelephonyInfoIn"])).optional(),
        }
    ).named(renames["NetworkInfoIn"])
    types["NetworkInfoOut"] = t.struct(
        {
            "imei": t.string().optional(),
            "meid": t.string().optional(),
            "networkOperatorName": t.string().optional(),
            "wifiMacAddress": t.string().optional(),
            "telephonyInfos": t.array(t.proxy(renames["TelephonyInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInfoOut"])
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
    types["SoftwareInfoIn"] = t.struct(
        {
            "securityPatchLevel": t.string().optional(),
            "primaryLanguageCode": t.string().optional(),
            "androidVersion": t.string().optional(),
            "deviceKernelVersion": t.string().optional(),
            "deviceBuildSignature": t.string().optional(),
            "androidDevicePolicyVersionCode": t.integer().optional(),
            "androidDevicePolicyVersionName": t.string().optional(),
            "systemUpdateInfo": t.proxy(renames["SystemUpdateInfoIn"]).optional(),
            "androidBuildTime": t.string().optional(),
            "androidBuildNumber": t.string().optional(),
            "bootloaderVersion": t.string().optional(),
        }
    ).named(renames["SoftwareInfoIn"])
    types["SoftwareInfoOut"] = t.struct(
        {
            "securityPatchLevel": t.string().optional(),
            "primaryLanguageCode": t.string().optional(),
            "androidVersion": t.string().optional(),
            "deviceKernelVersion": t.string().optional(),
            "deviceBuildSignature": t.string().optional(),
            "androidDevicePolicyVersionCode": t.integer().optional(),
            "androidDevicePolicyVersionName": t.string().optional(),
            "systemUpdateInfo": t.proxy(renames["SystemUpdateInfoOut"]).optional(),
            "androidBuildTime": t.string().optional(),
            "androidBuildNumber": t.string().optional(),
            "bootloaderVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareInfoOut"])
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
    types["UserIn"] = t.struct({"accountIdentifier": t.string().optional()}).named(
        renames["UserIn"]
    )
    types["UserOut"] = t.struct(
        {
            "accountIdentifier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["UsageLogEventIn"] = t.struct(
        {
            "certValidationFailureEvent": t.proxy(
                renames["CertValidationFailureEventIn"]
            ).optional(),
            "connectEvent": t.proxy(renames["ConnectEventIn"]).optional(),
            "keyguardDismissedEvent": t.proxy(
                renames["KeyguardDismissedEventIn"]
            ).optional(),
            "keyGeneratedEvent": t.proxy(renames["KeyGeneratedEventIn"]).optional(),
            "eventId": t.string().optional(),
            "remoteLockEvent": t.proxy(renames["RemoteLockEventIn"]).optional(),
            "adbShellInteractiveEvent": t.proxy(
                renames["AdbShellInteractiveEventIn"]
            ).optional(),
            "osStartupEvent": t.proxy(renames["OsStartupEventIn"]).optional(),
            "certAuthorityInstalledEvent": t.proxy(
                renames["CertAuthorityInstalledEventIn"]
            ).optional(),
            "loggingStoppedEvent": t.proxy(renames["LoggingStoppedEventIn"]).optional(),
            "loggingStartedEvent": t.proxy(renames["LoggingStartedEventIn"]).optional(),
            "eventType": t.string().optional(),
            "keyDestructionEvent": t.proxy(renames["KeyDestructionEventIn"]).optional(),
            "dnsEvent": t.proxy(renames["DnsEventIn"]).optional(),
            "filePushedEvent": t.proxy(renames["FilePushedEventIn"]).optional(),
            "adbShellCommandEvent": t.proxy(
                renames["AdbShellCommandEventIn"]
            ).optional(),
            "eventTime": t.string().optional(),
            "mediaMountEvent": t.proxy(renames["MediaMountEventIn"]).optional(),
            "certAuthorityRemovedEvent": t.proxy(
                renames["CertAuthorityRemovedEventIn"]
            ).optional(),
            "keyguardDismissAuthAttemptEvent": t.proxy(
                renames["KeyguardDismissAuthAttemptEventIn"]
            ).optional(),
            "filePulledEvent": t.proxy(renames["FilePulledEventIn"]).optional(),
            "osShutdownEvent": t.proxy(renames["OsShutdownEventIn"]).optional(),
            "appProcessStartEvent": t.proxy(
                renames["AppProcessStartEventIn"]
            ).optional(),
            "cryptoSelfTestCompletedEvent": t.proxy(
                renames["CryptoSelfTestCompletedEventIn"]
            ).optional(),
            "keyguardSecuredEvent": t.proxy(
                renames["KeyguardSecuredEventIn"]
            ).optional(),
            "mediaUnmountEvent": t.proxy(renames["MediaUnmountEventIn"]).optional(),
            "wipeFailureEvent": t.proxy(renames["WipeFailureEventIn"]).optional(),
            "keyImportEvent": t.proxy(renames["KeyImportEventIn"]).optional(),
            "logBufferSizeCriticalEvent": t.proxy(
                renames["LogBufferSizeCriticalEventIn"]
            ).optional(),
            "keyIntegrityViolationEvent": t.proxy(
                renames["KeyIntegrityViolationEventIn"]
            ).optional(),
        }
    ).named(renames["UsageLogEventIn"])
    types["UsageLogEventOut"] = t.struct(
        {
            "certValidationFailureEvent": t.proxy(
                renames["CertValidationFailureEventOut"]
            ).optional(),
            "connectEvent": t.proxy(renames["ConnectEventOut"]).optional(),
            "keyguardDismissedEvent": t.proxy(
                renames["KeyguardDismissedEventOut"]
            ).optional(),
            "keyGeneratedEvent": t.proxy(renames["KeyGeneratedEventOut"]).optional(),
            "eventId": t.string().optional(),
            "remoteLockEvent": t.proxy(renames["RemoteLockEventOut"]).optional(),
            "adbShellInteractiveEvent": t.proxy(
                renames["AdbShellInteractiveEventOut"]
            ).optional(),
            "osStartupEvent": t.proxy(renames["OsStartupEventOut"]).optional(),
            "certAuthorityInstalledEvent": t.proxy(
                renames["CertAuthorityInstalledEventOut"]
            ).optional(),
            "loggingStoppedEvent": t.proxy(
                renames["LoggingStoppedEventOut"]
            ).optional(),
            "loggingStartedEvent": t.proxy(
                renames["LoggingStartedEventOut"]
            ).optional(),
            "eventType": t.string().optional(),
            "keyDestructionEvent": t.proxy(
                renames["KeyDestructionEventOut"]
            ).optional(),
            "dnsEvent": t.proxy(renames["DnsEventOut"]).optional(),
            "filePushedEvent": t.proxy(renames["FilePushedEventOut"]).optional(),
            "adbShellCommandEvent": t.proxy(
                renames["AdbShellCommandEventOut"]
            ).optional(),
            "eventTime": t.string().optional(),
            "mediaMountEvent": t.proxy(renames["MediaMountEventOut"]).optional(),
            "certAuthorityRemovedEvent": t.proxy(
                renames["CertAuthorityRemovedEventOut"]
            ).optional(),
            "keyguardDismissAuthAttemptEvent": t.proxy(
                renames["KeyguardDismissAuthAttemptEventOut"]
            ).optional(),
            "filePulledEvent": t.proxy(renames["FilePulledEventOut"]).optional(),
            "osShutdownEvent": t.proxy(renames["OsShutdownEventOut"]).optional(),
            "appProcessStartEvent": t.proxy(
                renames["AppProcessStartEventOut"]
            ).optional(),
            "cryptoSelfTestCompletedEvent": t.proxy(
                renames["CryptoSelfTestCompletedEventOut"]
            ).optional(),
            "keyguardSecuredEvent": t.proxy(
                renames["KeyguardSecuredEventOut"]
            ).optional(),
            "mediaUnmountEvent": t.proxy(renames["MediaUnmountEventOut"]).optional(),
            "wipeFailureEvent": t.proxy(renames["WipeFailureEventOut"]).optional(),
            "keyImportEvent": t.proxy(renames["KeyImportEventOut"]).optional(),
            "logBufferSizeCriticalEvent": t.proxy(
                renames["LogBufferSizeCriticalEventOut"]
            ).optional(),
            "keyIntegrityViolationEvent": t.proxy(
                renames["KeyIntegrityViolationEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageLogEventOut"])
    types["ApiLevelConditionIn"] = t.struct(
        {"minApiLevel": t.integer().optional()}
    ).named(renames["ApiLevelConditionIn"])
    types["ApiLevelConditionOut"] = t.struct(
        {
            "minApiLevel": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiLevelConditionOut"])
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
    types["LoggingStartedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoggingStartedEventIn"]
    )
    types["LoggingStartedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoggingStartedEventOut"])
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
    types["AdvancedSecurityOverridesIn"] = t.struct(
        {
            "untrustedAppsPolicy": t.string().optional(),
            "personalAppsThatCanReadWorkNotifications": t.array(t.string()).optional(),
            "googlePlayProtectVerifyApps": t.string().optional(),
            "developerSettings": t.string().optional(),
            "commonCriteriaMode": t.string().optional(),
        }
    ).named(renames["AdvancedSecurityOverridesIn"])
    types["AdvancedSecurityOverridesOut"] = t.struct(
        {
            "untrustedAppsPolicy": t.string().optional(),
            "personalAppsThatCanReadWorkNotifications": t.array(t.string()).optional(),
            "googlePlayProtectVerifyApps": t.string().optional(),
            "developerSettings": t.string().optional(),
            "commonCriteriaMode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedSecurityOverridesOut"])
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
    types["ManagedPropertyIn"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["ManagedPropertyEntryIn"])).optional(),
            "title": t.string().optional(),
            "key": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "nestedProperties": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
        }
    ).named(renames["ManagedPropertyIn"])
    types["ManagedPropertyOut"] = t.struct(
        {
            "entries": t.array(t.proxy(renames["ManagedPropertyEntryOut"])).optional(),
            "title": t.string().optional(),
            "key": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "nestedProperties": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPropertyOut"])
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
    types["ApplicationReportIn"] = t.struct(
        {
            "events": t.array(t.proxy(renames["ApplicationEventIn"])).optional(),
            "signingKeyCertFingerprints": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "versionCode": t.integer().optional(),
            "versionName": t.string().optional(),
            "installerPackageName": t.string().optional(),
            "displayName": t.string().optional(),
            "applicationSource": t.string().optional(),
            "packageSha256Hash": t.string().optional(),
            "packageName": t.string().optional(),
            "keyedAppStates": t.array(t.proxy(renames["KeyedAppStateIn"])).optional(),
        }
    ).named(renames["ApplicationReportIn"])
    types["ApplicationReportOut"] = t.struct(
        {
            "events": t.array(t.proxy(renames["ApplicationEventOut"])).optional(),
            "signingKeyCertFingerprints": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "versionCode": t.integer().optional(),
            "versionName": t.string().optional(),
            "installerPackageName": t.string().optional(),
            "displayName": t.string().optional(),
            "applicationSource": t.string().optional(),
            "packageSha256Hash": t.string().optional(),
            "packageName": t.string().optional(),
            "keyedAppStates": t.array(t.proxy(renames["KeyedAppStateOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReportOut"])
    types["CertValidationFailureEventIn"] = t.struct(
        {"failureReason": t.string().optional()}
    ).named(renames["CertValidationFailureEventIn"])
    types["CertValidationFailureEventOut"] = t.struct(
        {
            "failureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertValidationFailureEventOut"])
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
    types["DeviceConnectivityManagementIn"] = t.struct(
        {"usbDataAccess": t.string().optional()}
    ).named(renames["DeviceConnectivityManagementIn"])
    types["DeviceConnectivityManagementOut"] = t.struct(
        {
            "usbDataAccess": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceConnectivityManagementOut"])
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
    types["AdbShellCommandEventIn"] = t.struct(
        {"shellCmd": t.string().optional()}
    ).named(renames["AdbShellCommandEventIn"])
    types["AdbShellCommandEventOut"] = t.struct(
        {
            "shellCmd": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdbShellCommandEventOut"])
    types["HardwareInfoIn"] = t.struct(
        {
            "cpuShutdownTemperatures": t.array(t.number()).optional(),
            "brand": t.string().optional(),
            "gpuThrottlingTemperatures": t.array(t.number()).optional(),
            "skinThrottlingTemperatures": t.array(t.number()).optional(),
            "batteryShutdownTemperatures": t.array(t.number()).optional(),
            "serialNumber": t.string().optional(),
            "manufacturer": t.string().optional(),
            "model": t.string().optional(),
            "cpuThrottlingTemperatures": t.array(t.number()).optional(),
            "deviceBasebandVersion": t.string().optional(),
            "batteryThrottlingTemperatures": t.array(t.number()).optional(),
            "skinShutdownTemperatures": t.array(t.number()).optional(),
            "hardware": t.string().optional(),
            "gpuShutdownTemperatures": t.array(t.number()).optional(),
        }
    ).named(renames["HardwareInfoIn"])
    types["HardwareInfoOut"] = t.struct(
        {
            "cpuShutdownTemperatures": t.array(t.number()).optional(),
            "brand": t.string().optional(),
            "gpuThrottlingTemperatures": t.array(t.number()).optional(),
            "skinThrottlingTemperatures": t.array(t.number()).optional(),
            "batteryShutdownTemperatures": t.array(t.number()).optional(),
            "serialNumber": t.string().optional(),
            "manufacturer": t.string().optional(),
            "model": t.string().optional(),
            "cpuThrottlingTemperatures": t.array(t.number()).optional(),
            "deviceBasebandVersion": t.string().optional(),
            "batteryThrottlingTemperatures": t.array(t.number()).optional(),
            "skinShutdownTemperatures": t.array(t.number()).optional(),
            "hardware": t.string().optional(),
            "enterpriseSpecificId": t.string().optional(),
            "gpuShutdownTemperatures": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HardwareInfoOut"])
    types["ClearAppsDataParamsIn"] = t.struct(
        {"packageNames": t.array(t.string()).optional()}
    ).named(renames["ClearAppsDataParamsIn"])
    types["ClearAppsDataParamsOut"] = t.struct(
        {
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearAppsDataParamsOut"])
    types["KeyedAppStateIn"] = t.struct(
        {
            "data": t.string().optional(),
            "message": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "key": t.string().optional(),
            "createTime": t.string().optional(),
            "severity": t.string().optional(),
        }
    ).named(renames["KeyedAppStateIn"])
    types["KeyedAppStateOut"] = t.struct(
        {
            "data": t.string().optional(),
            "message": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "key": t.string().optional(),
            "createTime": t.string().optional(),
            "severity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyedAppStateOut"])
    types["PolicyIn"] = t.struct(
        {
            "encryptionPolicy": t.string().optional(),
            "openNetworkConfiguration": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "shareLocationDisabled": t.boolean().optional(),
            "wifiConfigsLockdownEnabled": t.boolean().optional(),
            "factoryResetDisabled": t.boolean().optional(),
            "cameraDisabled": t.boolean().optional(),
            "frpAdminEmails": t.array(t.string()).optional(),
            "mountPhysicalMediaDisabled": t.boolean().optional(),
            "stayOnPluggedModes": t.array(t.string()).optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "autoTimeRequired": t.boolean().optional(),
            "outgoingCallsDisabled": t.boolean().optional(),
            "crossProfilePolicies": t.proxy(
                renames["CrossProfilePoliciesIn"]
            ).optional(),
            "networkResetDisabled": t.boolean().optional(),
            "setWallpaperDisabled": t.boolean().optional(),
            "passwordRequirements": t.proxy(
                renames["PasswordRequirementsIn"]
            ).optional(),
            "name": t.string().optional(),
            "autoDateAndTimeZone": t.string().optional(),
            "deviceConnectivityManagement": t.proxy(
                renames["DeviceConnectivityManagementIn"]
            ).optional(),
            "kioskCustomLauncherEnabled": t.boolean().optional(),
            "outgoingBeamDisabled": t.boolean().optional(),
            "removeUserDisabled": t.boolean().optional(),
            "playStoreMode": t.string().optional(),
            "bluetoothContactSharingDisabled": t.boolean().optional(),
            "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
            "debuggingFeaturesAllowed": t.boolean().optional(),
            "persistentPreferredActivities": t.array(
                t.proxy(renames["PersistentPreferredActivityIn"])
            ).optional(),
            "ensureVerifyAppsEnabled": t.boolean().optional(),
            "preferentialNetworkService": t.string().optional(),
            "addUserDisabled": t.boolean().optional(),
            "funDisabled": t.boolean().optional(),
            "usbMassStorageEnabled": t.boolean().optional(),
            "passwordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsIn"])
            ).optional(),
            "setUserIconDisabled": t.boolean().optional(),
            "oncCertificateProviders": t.array(
                t.proxy(renames["OncCertificateProviderIn"])
            ).optional(),
            "privateKeySelectionEnabled": t.boolean().optional(),
            "cellBroadcastsConfigDisabled": t.boolean().optional(),
            "maximumTimeToLock": t.string().optional(),
            "choosePrivateKeyRules": t.array(
                t.proxy(renames["ChoosePrivateKeyRuleIn"])
            ).optional(),
            "alwaysOnVpnPackage": t.proxy(renames["AlwaysOnVpnPackageIn"]).optional(),
            "mobileNetworksConfigDisabled": t.boolean().optional(),
            "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
            "keyguardDisabled": t.boolean().optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantIn"])
            ).optional(),
            "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
            "shortSupportMessage": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "complianceRules": t.array(t.proxy(renames["ComplianceRuleIn"])).optional(),
            "deviceOwnerLockScreenInfo": t.proxy(
                renames["UserFacingMessageIn"]
            ).optional(),
            "createWindowsDisabled": t.boolean().optional(),
            "permittedAccessibilityServices": t.proxy(
                renames["PackageNameListIn"]
            ).optional(),
            "statusBarDisabled": t.boolean().optional(),
            "uninstallAppsDisabled": t.boolean().optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "advancedSecurityOverrides": t.proxy(
                renames["AdvancedSecurityOverridesIn"]
            ).optional(),
            "minimumApiLevel": t.integer().optional(),
            "cameraAccess": t.string().optional(),
            "installUnknownSourcesAllowed": t.boolean().optional(),
            "statusReportingSettings": t.proxy(
                renames["StatusReportingSettingsIn"]
            ).optional(),
            "microphoneAccess": t.string().optional(),
            "permittedInputMethods": t.proxy(renames["PackageNameListIn"]).optional(),
            "adjustVolumeDisabled": t.boolean().optional(),
            "dataRoamingDisabled": t.boolean().optional(),
            "usbFileTransferDisabled": t.boolean().optional(),
            "bluetoothDisabled": t.boolean().optional(),
            "safeBootDisabled": t.boolean().optional(),
            "credentialsConfigDisabled": t.boolean().optional(),
            "appAutoUpdatePolicy": t.string().optional(),
            "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
            "bluetoothConfigDisabled": t.boolean().optional(),
            "androidDevicePolicyTracks": t.array(t.string()).optional(),
            "installAppsDisabled": t.boolean().optional(),
            "keyguardDisabledFeatures": t.array(t.string()).optional(),
            "wifiConfigDisabled": t.boolean().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "policyEnforcementRules": t.array(
                t.proxy(renames["PolicyEnforcementRuleIn"])
            ).optional(),
            "networkEscapeHatchEnabled": t.boolean().optional(),
            "locationMode": t.string().optional(),
            "kioskCustomization": t.proxy(renames["KioskCustomizationIn"]).optional(),
            "skipFirstUseHintsEnabled": t.boolean().optional(),
            "smsDisabled": t.boolean().optional(),
            "modifyAccountsDisabled": t.boolean().optional(),
            "tetheringConfigDisabled": t.boolean().optional(),
            "version": t.string().optional(),
            "vpnConfigDisabled": t.boolean().optional(),
            "applications": t.array(t.proxy(renames["ApplicationPolicyIn"])).optional(),
            "blockApplicationsEnabled": t.boolean().optional(),
            "personalUsagePolicies": t.proxy(
                renames["PersonalUsagePoliciesIn"]
            ).optional(),
            "longSupportMessage": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "unmuteMicrophoneDisabled": t.boolean().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "encryptionPolicy": t.string().optional(),
            "openNetworkConfiguration": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "shareLocationDisabled": t.boolean().optional(),
            "wifiConfigsLockdownEnabled": t.boolean().optional(),
            "factoryResetDisabled": t.boolean().optional(),
            "cameraDisabled": t.boolean().optional(),
            "frpAdminEmails": t.array(t.string()).optional(),
            "mountPhysicalMediaDisabled": t.boolean().optional(),
            "stayOnPluggedModes": t.array(t.string()).optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "autoTimeRequired": t.boolean().optional(),
            "outgoingCallsDisabled": t.boolean().optional(),
            "crossProfilePolicies": t.proxy(
                renames["CrossProfilePoliciesOut"]
            ).optional(),
            "networkResetDisabled": t.boolean().optional(),
            "setWallpaperDisabled": t.boolean().optional(),
            "passwordRequirements": t.proxy(
                renames["PasswordRequirementsOut"]
            ).optional(),
            "name": t.string().optional(),
            "autoDateAndTimeZone": t.string().optional(),
            "deviceConnectivityManagement": t.proxy(
                renames["DeviceConnectivityManagementOut"]
            ).optional(),
            "kioskCustomLauncherEnabled": t.boolean().optional(),
            "outgoingBeamDisabled": t.boolean().optional(),
            "removeUserDisabled": t.boolean().optional(),
            "playStoreMode": t.string().optional(),
            "bluetoothContactSharingDisabled": t.boolean().optional(),
            "systemUpdate": t.proxy(renames["SystemUpdateOut"]).optional(),
            "debuggingFeaturesAllowed": t.boolean().optional(),
            "persistentPreferredActivities": t.array(
                t.proxy(renames["PersistentPreferredActivityOut"])
            ).optional(),
            "ensureVerifyAppsEnabled": t.boolean().optional(),
            "preferentialNetworkService": t.string().optional(),
            "addUserDisabled": t.boolean().optional(),
            "funDisabled": t.boolean().optional(),
            "usbMassStorageEnabled": t.boolean().optional(),
            "passwordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsOut"])
            ).optional(),
            "setUserIconDisabled": t.boolean().optional(),
            "oncCertificateProviders": t.array(
                t.proxy(renames["OncCertificateProviderOut"])
            ).optional(),
            "privateKeySelectionEnabled": t.boolean().optional(),
            "cellBroadcastsConfigDisabled": t.boolean().optional(),
            "maximumTimeToLock": t.string().optional(),
            "choosePrivateKeyRules": t.array(
                t.proxy(renames["ChoosePrivateKeyRuleOut"])
            ).optional(),
            "alwaysOnVpnPackage": t.proxy(renames["AlwaysOnVpnPackageOut"]).optional(),
            "mobileNetworksConfigDisabled": t.boolean().optional(),
            "recommendedGlobalProxy": t.proxy(renames["ProxyInfoOut"]).optional(),
            "keyguardDisabled": t.boolean().optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantOut"])
            ).optional(),
            "usageLog": t.proxy(renames["UsageLogOut"]).optional(),
            "shortSupportMessage": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "complianceRules": t.array(
                t.proxy(renames["ComplianceRuleOut"])
            ).optional(),
            "deviceOwnerLockScreenInfo": t.proxy(
                renames["UserFacingMessageOut"]
            ).optional(),
            "createWindowsDisabled": t.boolean().optional(),
            "permittedAccessibilityServices": t.proxy(
                renames["PackageNameListOut"]
            ).optional(),
            "statusBarDisabled": t.boolean().optional(),
            "uninstallAppsDisabled": t.boolean().optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "advancedSecurityOverrides": t.proxy(
                renames["AdvancedSecurityOverridesOut"]
            ).optional(),
            "minimumApiLevel": t.integer().optional(),
            "cameraAccess": t.string().optional(),
            "installUnknownSourcesAllowed": t.boolean().optional(),
            "statusReportingSettings": t.proxy(
                renames["StatusReportingSettingsOut"]
            ).optional(),
            "microphoneAccess": t.string().optional(),
            "permittedInputMethods": t.proxy(renames["PackageNameListOut"]).optional(),
            "adjustVolumeDisabled": t.boolean().optional(),
            "dataRoamingDisabled": t.boolean().optional(),
            "usbFileTransferDisabled": t.boolean().optional(),
            "bluetoothDisabled": t.boolean().optional(),
            "safeBootDisabled": t.boolean().optional(),
            "credentialsConfigDisabled": t.boolean().optional(),
            "appAutoUpdatePolicy": t.string().optional(),
            "setupActions": t.array(t.proxy(renames["SetupActionOut"])).optional(),
            "bluetoothConfigDisabled": t.boolean().optional(),
            "androidDevicePolicyTracks": t.array(t.string()).optional(),
            "installAppsDisabled": t.boolean().optional(),
            "keyguardDisabledFeatures": t.array(t.string()).optional(),
            "wifiConfigDisabled": t.boolean().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "policyEnforcementRules": t.array(
                t.proxy(renames["PolicyEnforcementRuleOut"])
            ).optional(),
            "networkEscapeHatchEnabled": t.boolean().optional(),
            "locationMode": t.string().optional(),
            "kioskCustomization": t.proxy(renames["KioskCustomizationOut"]).optional(),
            "skipFirstUseHintsEnabled": t.boolean().optional(),
            "smsDisabled": t.boolean().optional(),
            "modifyAccountsDisabled": t.boolean().optional(),
            "tetheringConfigDisabled": t.boolean().optional(),
            "version": t.string().optional(),
            "vpnConfigDisabled": t.boolean().optional(),
            "applications": t.array(
                t.proxy(renames["ApplicationPolicyOut"])
            ).optional(),
            "blockApplicationsEnabled": t.boolean().optional(),
            "personalUsagePolicies": t.proxy(
                renames["PersonalUsagePoliciesOut"]
            ).optional(),
            "longSupportMessage": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "unmuteMicrophoneDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["PolicyEnforcementRuleIn"] = t.struct(
        {
            "wipeAction": t.proxy(renames["WipeActionIn"]).optional(),
            "blockAction": t.proxy(renames["BlockActionIn"]).optional(),
            "settingName": t.string().optional(),
        }
    ).named(renames["PolicyEnforcementRuleIn"])
    types["PolicyEnforcementRuleOut"] = t.struct(
        {
            "wipeAction": t.proxy(renames["WipeActionOut"]).optional(),
            "blockAction": t.proxy(renames["BlockActionOut"]).optional(),
            "settingName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyEnforcementRuleOut"])
    types["SystemUpdateIn"] = t.struct(
        {
            "startMinutes": t.integer().optional(),
            "freezePeriods": t.array(t.proxy(renames["FreezePeriodIn"])).optional(),
            "type": t.string().optional(),
            "endMinutes": t.integer().optional(),
        }
    ).named(renames["SystemUpdateIn"])
    types["SystemUpdateOut"] = t.struct(
        {
            "startMinutes": t.integer().optional(),
            "freezePeriods": t.array(t.proxy(renames["FreezePeriodOut"])).optional(),
            "type": t.string().optional(),
            "endMinutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemUpdateOut"])
    types["NonComplianceDetailIn"] = t.struct(
        {
            "specificNonComplianceReason": t.string().optional(),
            "specificNonComplianceContext": t.proxy(
                renames["SpecificNonComplianceContextIn"]
            ).optional(),
            "installationFailureReason": t.string().optional(),
            "currentValue": t.struct({"_": t.string().optional()}).optional(),
            "packageName": t.string().optional(),
            "fieldPath": t.string().optional(),
            "settingName": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
        }
    ).named(renames["NonComplianceDetailIn"])
    types["NonComplianceDetailOut"] = t.struct(
        {
            "specificNonComplianceReason": t.string().optional(),
            "specificNonComplianceContext": t.proxy(
                renames["SpecificNonComplianceContextOut"]
            ).optional(),
            "installationFailureReason": t.string().optional(),
            "currentValue": t.struct({"_": t.string().optional()}).optional(),
            "packageName": t.string().optional(),
            "fieldPath": t.string().optional(),
            "settingName": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonComplianceDetailOut"])
    types["PackageNameListIn"] = t.struct(
        {"packageNames": t.array(t.string()).optional()}
    ).named(renames["PackageNameListIn"])
    types["PackageNameListOut"] = t.struct(
        {
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageNameListOut"])
    types["WebAppIn"] = t.struct(
        {
            "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
            "title": t.string().optional(),
            "startUrl": t.string().optional(),
            "displayMode": t.string().optional(),
            "versionCode": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "icons": t.array(t.proxy(renames["WebAppIconOut"])).optional(),
            "title": t.string().optional(),
            "startUrl": t.string().optional(),
            "displayMode": t.string().optional(),
            "versionCode": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
    types["WebAppIconIn"] = t.struct({"imageData": t.string().optional()}).named(
        renames["WebAppIconIn"]
    )
    types["WebAppIconOut"] = t.struct(
        {
            "imageData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppIconOut"])
    types["ProxyInfoIn"] = t.struct(
        {
            "host": t.string().optional(),
            "excludedHosts": t.array(t.string()).optional(),
            "pacUri": t.string().optional(),
            "port": t.integer().optional(),
        }
    ).named(renames["ProxyInfoIn"])
    types["ProxyInfoOut"] = t.struct(
        {
            "host": t.string().optional(),
            "excludedHosts": t.array(t.string()).optional(),
            "pacUri": t.string().optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProxyInfoOut"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["EnrollmentTokenIn"] = t.struct(
        {
            "expirationTimestamp": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "qrCode": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "duration": t.string().optional(),
            "additionalData": t.string().optional(),
            "oneTimeOnly": t.boolean().optional(),
            "policyName": t.string().optional(),
        }
    ).named(renames["EnrollmentTokenIn"])
    types["EnrollmentTokenOut"] = t.struct(
        {
            "expirationTimestamp": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "qrCode": t.string().optional(),
            "name": t.string().optional(),
            "value": t.string().optional(),
            "duration": t.string().optional(),
            "additionalData": t.string().optional(),
            "oneTimeOnly": t.boolean().optional(),
            "policyName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollmentTokenOut"])
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
    types["BatchUsageLogEventsIn"] = t.struct(
        {
            "device": t.string().optional(),
            "retrievalTime": t.string().optional(),
            "usageLogEvents": t.array(t.proxy(renames["UsageLogEventIn"])).optional(),
            "user": t.string().optional(),
        }
    ).named(renames["BatchUsageLogEventsIn"])
    types["BatchUsageLogEventsOut"] = t.struct(
        {
            "device": t.string().optional(),
            "retrievalTime": t.string().optional(),
            "usageLogEvents": t.array(t.proxy(renames["UsageLogEventOut"])).optional(),
            "user": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUsageLogEventsOut"])
    types["ComplianceRuleIn"] = t.struct(
        {
            "nonComplianceDetailCondition": t.proxy(
                renames["NonComplianceDetailConditionIn"]
            ).optional(),
            "apiLevelCondition": t.proxy(renames["ApiLevelConditionIn"]).optional(),
            "disableApps": t.boolean().optional(),
            "packageNamesToDisable": t.array(t.string()).optional(),
        }
    ).named(renames["ComplianceRuleIn"])
    types["ComplianceRuleOut"] = t.struct(
        {
            "nonComplianceDetailCondition": t.proxy(
                renames["NonComplianceDetailConditionOut"]
            ).optional(),
            "apiLevelCondition": t.proxy(renames["ApiLevelConditionOut"]).optional(),
            "disableApps": t.boolean().optional(),
            "packageNamesToDisable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceRuleOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["PasswordRequirementsIn"] = t.struct(
        {
            "passwordHistoryLength": t.integer().optional(),
            "passwordMinimumLetters": t.integer().optional(),
            "passwordMinimumLowerCase": t.integer().optional(),
            "passwordMinimumSymbols": t.integer().optional(),
            "passwordMinimumLength": t.integer().optional(),
            "passwordExpirationTimeout": t.string().optional(),
            "passwordScope": t.string().optional(),
            "passwordMinimumNonLetter": t.integer().optional(),
            "requirePasswordUnlock": t.string().optional(),
            "passwordMinimumUpperCase": t.integer().optional(),
            "unifiedLockSettings": t.string().optional(),
            "maximumFailedPasswordsForWipe": t.integer().optional(),
            "passwordQuality": t.string().optional(),
            "passwordMinimumNumeric": t.integer().optional(),
        }
    ).named(renames["PasswordRequirementsIn"])
    types["PasswordRequirementsOut"] = t.struct(
        {
            "passwordHistoryLength": t.integer().optional(),
            "passwordMinimumLetters": t.integer().optional(),
            "passwordMinimumLowerCase": t.integer().optional(),
            "passwordMinimumSymbols": t.integer().optional(),
            "passwordMinimumLength": t.integer().optional(),
            "passwordExpirationTimeout": t.string().optional(),
            "passwordScope": t.string().optional(),
            "passwordMinimumNonLetter": t.integer().optional(),
            "requirePasswordUnlock": t.string().optional(),
            "passwordMinimumUpperCase": t.integer().optional(),
            "unifiedLockSettings": t.string().optional(),
            "maximumFailedPasswordsForWipe": t.integer().optional(),
            "passwordQuality": t.string().optional(),
            "passwordMinimumNumeric": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordRequirementsOut"])
    types["LoggingStoppedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoggingStoppedEventIn"]
    )
    types["LoggingStoppedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoggingStoppedEventOut"])
    types["StatusReportingSettingsIn"] = t.struct(
        {
            "systemPropertiesEnabled": t.boolean().optional(),
            "memoryInfoEnabled": t.boolean().optional(),
            "powerManagementEventsEnabled": t.boolean().optional(),
            "networkInfoEnabled": t.boolean().optional(),
            "applicationReportsEnabled": t.boolean().optional(),
            "softwareInfoEnabled": t.boolean().optional(),
            "deviceSettingsEnabled": t.boolean().optional(),
            "hardwareStatusEnabled": t.boolean().optional(),
            "displayInfoEnabled": t.boolean().optional(),
            "commonCriteriaModeEnabled": t.boolean().optional(),
            "applicationReportingSettings": t.proxy(
                renames["ApplicationReportingSettingsIn"]
            ).optional(),
        }
    ).named(renames["StatusReportingSettingsIn"])
    types["StatusReportingSettingsOut"] = t.struct(
        {
            "systemPropertiesEnabled": t.boolean().optional(),
            "memoryInfoEnabled": t.boolean().optional(),
            "powerManagementEventsEnabled": t.boolean().optional(),
            "networkInfoEnabled": t.boolean().optional(),
            "applicationReportsEnabled": t.boolean().optional(),
            "softwareInfoEnabled": t.boolean().optional(),
            "deviceSettingsEnabled": t.boolean().optional(),
            "hardwareStatusEnabled": t.boolean().optional(),
            "displayInfoEnabled": t.boolean().optional(),
            "commonCriteriaModeEnabled": t.boolean().optional(),
            "applicationReportingSettings": t.proxy(
                renames["ApplicationReportingSettingsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusReportingSettingsOut"])
    types["SetupActionIn"] = t.struct(
        {
            "title": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "launchApp": t.proxy(renames["LaunchAppActionIn"]).optional(),
            "description": t.proxy(renames["UserFacingMessageIn"]).optional(),
        }
    ).named(renames["SetupActionIn"])
    types["SetupActionOut"] = t.struct(
        {
            "title": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "launchApp": t.proxy(renames["LaunchAppActionOut"]).optional(),
            "description": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetupActionOut"])
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
    types["ListEnterprisesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "enterprises": t.array(t.proxy(renames["EnterpriseIn"])).optional(),
        }
    ).named(renames["ListEnterprisesResponseIn"])
    types["ListEnterprisesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "enterprises": t.array(t.proxy(renames["EnterpriseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnterprisesResponseOut"])
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
    types["DnsEventIn"] = t.struct(
        {
            "totalIpAddressesReturned": t.string().optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "hostname": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["DnsEventIn"])
    types["DnsEventOut"] = t.struct(
        {
            "totalIpAddressesReturned": t.string().optional(),
            "ipAddresses": t.array(t.string()).optional(),
            "hostname": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsEventOut"])
    types["AdbShellInteractiveEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdbShellInteractiveEventIn"]
    )
    types["AdbShellInteractiveEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdbShellInteractiveEventOut"])
    types["AppProcessInfoIn"] = t.struct(
        {
            "processName": t.string().optional(),
            "uid": t.integer().optional(),
            "seinfo": t.string().optional(),
            "pid": t.integer().optional(),
            "startTime": t.string().optional(),
            "apkSha256Hash": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
        }
    ).named(renames["AppProcessInfoIn"])
    types["AppProcessInfoOut"] = t.struct(
        {
            "processName": t.string().optional(),
            "uid": t.integer().optional(),
            "seinfo": t.string().optional(),
            "pid": t.integer().optional(),
            "startTime": t.string().optional(),
            "apkSha256Hash": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProcessInfoOut"])
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
    types["CryptoSelfTestCompletedEventIn"] = t.struct(
        {"success": t.boolean().optional()}
    ).named(renames["CryptoSelfTestCompletedEventIn"])
    types["CryptoSelfTestCompletedEventOut"] = t.struct(
        {
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoSelfTestCompletedEventOut"])
    types["CrossProfilePoliciesIn"] = t.struct(
        {
            "showWorkContactsInPersonalProfile": t.string().optional(),
            "workProfileWidgetsDefault": t.string().optional(),
            "crossProfileCopyPaste": t.string().optional(),
            "crossProfileDataSharing": t.string().optional(),
        }
    ).named(renames["CrossProfilePoliciesIn"])
    types["CrossProfilePoliciesOut"] = t.struct(
        {
            "showWorkContactsInPersonalProfile": t.string().optional(),
            "workProfileWidgetsDefault": t.string().optional(),
            "crossProfileCopyPaste": t.string().optional(),
            "crossProfileDataSharing": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrossProfilePoliciesOut"])
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
    types["DateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["PasswordPoliciesContextIn"] = t.struct(
        {"passwordPolicyScope": t.string().optional()}
    ).named(renames["PasswordPoliciesContextIn"])
    types["PasswordPoliciesContextOut"] = t.struct(
        {
            "passwordPolicyScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordPoliciesContextOut"])
    types["ApplicationReportingSettingsIn"] = t.struct(
        {"includeRemovedApps": t.boolean().optional()}
    ).named(renames["ApplicationReportingSettingsIn"])
    types["ApplicationReportingSettingsOut"] = t.struct(
        {
            "includeRemovedApps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReportingSettingsOut"])
    types["AppProcessStartEventIn"] = t.struct(
        {"processInfo": t.proxy(renames["AppProcessInfoIn"]).optional()}
    ).named(renames["AppProcessStartEventIn"])
    types["AppProcessStartEventOut"] = t.struct(
        {
            "processInfo": t.proxy(renames["AppProcessInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProcessStartEventOut"])
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
    types["CommandIn"] = t.struct(
        {
            "newPassword": t.string().optional(),
            "resetPasswordFlags": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "duration": t.string().optional(),
            "clearAppsDataParams": t.proxy(renames["ClearAppsDataParamsIn"]).optional(),
            "createTime": t.string().optional(),
            "errorCode": t.string().optional(),
            "userName": t.string().optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "newPassword": t.string().optional(),
            "resetPasswordFlags": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "clearAppsDataStatus": t.proxy(
                renames["ClearAppsDataStatusOut"]
            ).optional(),
            "duration": t.string().optional(),
            "clearAppsDataParams": t.proxy(
                renames["ClearAppsDataParamsOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "errorCode": t.string().optional(),
            "userName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
    types["CertAuthorityInstalledEventIn"] = t.struct(
        {
            "userId": t.integer().optional(),
            "success": t.boolean().optional(),
            "certificate": t.string().optional(),
        }
    ).named(renames["CertAuthorityInstalledEventIn"])
    types["CertAuthorityInstalledEventOut"] = t.struct(
        {
            "userId": t.integer().optional(),
            "success": t.boolean().optional(),
            "certificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertAuthorityInstalledEventOut"])
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
    types["KeyIntegrityViolationEventIn"] = t.struct(
        {"keyAlias": t.string().optional(), "applicationUid": t.integer().optional()}
    ).named(renames["KeyIntegrityViolationEventIn"])
    types["KeyIntegrityViolationEventOut"] = t.struct(
        {
            "keyAlias": t.string().optional(),
            "applicationUid": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyIntegrityViolationEventOut"])
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
    types["SigninDetailIn"] = t.struct(
        {
            "allowPersonalUsage": t.string().optional(),
            "signinEnrollmentToken": t.string().optional(),
            "qrCode": t.string().optional(),
            "signinUrl": t.string().optional(),
        }
    ).named(renames["SigninDetailIn"])
    types["SigninDetailOut"] = t.struct(
        {
            "allowPersonalUsage": t.string().optional(),
            "signinEnrollmentToken": t.string().optional(),
            "qrCode": t.string().optional(),
            "signinUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SigninDetailOut"])
    types["HardwareStatusIn"] = t.struct(
        {
            "fanSpeeds": t.array(t.number()).optional(),
            "batteryTemperatures": t.array(t.number()).optional(),
            "createTime": t.string().optional(),
            "gpuTemperatures": t.array(t.number()).optional(),
            "skinTemperatures": t.array(t.number()).optional(),
            "cpuUsages": t.array(t.number()).optional(),
            "cpuTemperatures": t.array(t.number()).optional(),
        }
    ).named(renames["HardwareStatusIn"])
    types["HardwareStatusOut"] = t.struct(
        {
            "fanSpeeds": t.array(t.number()).optional(),
            "batteryTemperatures": t.array(t.number()).optional(),
            "createTime": t.string().optional(),
            "gpuTemperatures": t.array(t.number()).optional(),
            "skinTemperatures": t.array(t.number()).optional(),
            "cpuUsages": t.array(t.number()).optional(),
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
    types["OncWifiContextIn"] = t.struct({"wifiGuid": t.string().optional()}).named(
        renames["OncWifiContextIn"]
    )
    types["OncWifiContextOut"] = t.struct(
        {
            "wifiGuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OncWifiContextOut"])
    types["ContactInfoIn"] = t.struct(
        {
            "dataProtectionOfficerPhone": t.string().optional(),
            "euRepresentativeName": t.string().optional(),
            "contactEmail": t.string().optional(),
            "dataProtectionOfficerName": t.string().optional(),
            "dataProtectionOfficerEmail": t.string().optional(),
            "euRepresentativePhone": t.string().optional(),
            "euRepresentativeEmail": t.string().optional(),
        }
    ).named(renames["ContactInfoIn"])
    types["ContactInfoOut"] = t.struct(
        {
            "dataProtectionOfficerPhone": t.string().optional(),
            "euRepresentativeName": t.string().optional(),
            "contactEmail": t.string().optional(),
            "dataProtectionOfficerName": t.string().optional(),
            "dataProtectionOfficerEmail": t.string().optional(),
            "euRepresentativePhone": t.string().optional(),
            "euRepresentativeEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoOut"])
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
    types["KeyGeneratedEventIn"] = t.struct(
        {
            "keyAlias": t.string().optional(),
            "applicationUid": t.integer().optional(),
            "success": t.boolean().optional(),
        }
    ).named(renames["KeyGeneratedEventIn"])
    types["KeyGeneratedEventOut"] = t.struct(
        {
            "keyAlias": t.string().optional(),
            "applicationUid": t.integer().optional(),
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyGeneratedEventOut"])
    types["LaunchAppActionIn"] = t.struct({"packageName": t.string().optional()}).named(
        renames["LaunchAppActionIn"]
    )
    types["LaunchAppActionOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchAppActionOut"])
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
    types["DisplayIn"] = t.struct(
        {
            "name": t.string().optional(),
            "width": t.integer().optional(),
            "state": t.string().optional(),
            "height": t.integer().optional(),
            "refreshRate": t.integer().optional(),
            "displayId": t.integer().optional(),
            "density": t.integer().optional(),
        }
    ).named(renames["DisplayIn"])
    types["DisplayOut"] = t.struct(
        {
            "name": t.string().optional(),
            "width": t.integer().optional(),
            "state": t.string().optional(),
            "height": t.integer().optional(),
            "refreshRate": t.integer().optional(),
            "displayId": t.integer().optional(),
            "density": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayOut"])
    types["ApplicationPolicyIn"] = t.struct(
        {
            "managedConfigurationTemplate": t.proxy(
                renames["ManagedConfigurationTemplateIn"]
            ).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "connectedWorkAndPersonalApp": t.string().optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantIn"])
            ).optional(),
            "disabled": t.boolean().optional(),
            "accessibleTrackIds": t.array(t.string()).optional(),
            "installType": t.string().optional(),
            "delegatedScopes": t.array(t.string()).optional(),
            "alwaysOnVpnLockdownExemption": t.string().optional(),
            "minimumVersionCode": t.integer().optional(),
            "autoUpdateMode": t.string().optional(),
            "packageName": t.string().optional(),
            "managedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "lockTaskAllowed": t.boolean().optional(),
            "workProfileWidgets": t.string().optional(),
            "extensionConfig": t.proxy(renames["ExtensionConfigIn"]).optional(),
        }
    ).named(renames["ApplicationPolicyIn"])
    types["ApplicationPolicyOut"] = t.struct(
        {
            "managedConfigurationTemplate": t.proxy(
                renames["ManagedConfigurationTemplateOut"]
            ).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "connectedWorkAndPersonalApp": t.string().optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantOut"])
            ).optional(),
            "disabled": t.boolean().optional(),
            "accessibleTrackIds": t.array(t.string()).optional(),
            "installType": t.string().optional(),
            "delegatedScopes": t.array(t.string()).optional(),
            "alwaysOnVpnLockdownExemption": t.string().optional(),
            "minimumVersionCode": t.integer().optional(),
            "autoUpdateMode": t.string().optional(),
            "packageName": t.string().optional(),
            "managedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "lockTaskAllowed": t.boolean().optional(),
            "workProfileWidgets": t.string().optional(),
            "extensionConfig": t.proxy(renames["ExtensionConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationPolicyOut"])
    types["KeyguardDismissedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyguardDismissedEventIn"]
    )
    types["KeyguardDismissedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["KeyguardDismissedEventOut"])
    types["DeviceIn"] = t.struct(
        {
            "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
            "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
            "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
            "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
            "nonComplianceDetails": t.array(
                t.proxy(renames["NonComplianceDetailIn"])
            ).optional(),
            "systemProperties": t.struct({"_": t.string().optional()}).optional(),
            "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "appliedPolicyName": t.string().optional(),
            "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "commonCriteriaModeInfo": t.proxy(
                renames["CommonCriteriaModeInfoIn"]
            ).optional(),
            "appliedPolicyVersion": t.string().optional(),
            "lastStatusReportTime": t.string().optional(),
            "apiLevel": t.integer().optional(),
            "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
            "policyCompliant": t.boolean().optional(),
            "state": t.string().optional(),
            "powerManagementEvents": t.array(
                t.proxy(renames["PowerManagementEventIn"])
            ).optional(),
            "lastPolicyComplianceReportTime": t.string().optional(),
            "name": t.string().optional(),
            "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
            "userName": t.string().optional(),
            "lastPolicySyncTime": t.string().optional(),
            "appliedState": t.string().optional(),
            "policyName": t.string().optional(),
            "enrollmentTokenName": t.string().optional(),
            "appliedPasswordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsIn"])
            ).optional(),
            "hardwareStatusSamples": t.array(
                t.proxy(renames["HardwareStatusIn"])
            ).optional(),
            "enrollmentTime": t.string().optional(),
            "applicationReports": t.array(
                t.proxy(renames["ApplicationReportIn"])
            ).optional(),
            "previousDeviceNames": t.array(t.string()).optional(),
            "managementMode": t.string().optional(),
            "enrollmentTokenData": t.string().optional(),
            "ownership": t.string().optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "memoryEvents": t.array(t.proxy(renames["MemoryEventOut"])).optional(),
            "softwareInfo": t.proxy(renames["SoftwareInfoOut"]).optional(),
            "displays": t.array(t.proxy(renames["DisplayOut"])).optional(),
            "securityPosture": t.proxy(renames["SecurityPostureOut"]).optional(),
            "nonComplianceDetails": t.array(
                t.proxy(renames["NonComplianceDetailOut"])
            ).optional(),
            "systemProperties": t.struct({"_": t.string().optional()}).optional(),
            "disabledReason": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "appliedPolicyName": t.string().optional(),
            "networkInfo": t.proxy(renames["NetworkInfoOut"]).optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "commonCriteriaModeInfo": t.proxy(
                renames["CommonCriteriaModeInfoOut"]
            ).optional(),
            "appliedPolicyVersion": t.string().optional(),
            "lastStatusReportTime": t.string().optional(),
            "apiLevel": t.integer().optional(),
            "deviceSettings": t.proxy(renames["DeviceSettingsOut"]).optional(),
            "policyCompliant": t.boolean().optional(),
            "state": t.string().optional(),
            "powerManagementEvents": t.array(
                t.proxy(renames["PowerManagementEventOut"])
            ).optional(),
            "lastPolicyComplianceReportTime": t.string().optional(),
            "name": t.string().optional(),
            "hardwareInfo": t.proxy(renames["HardwareInfoOut"]).optional(),
            "userName": t.string().optional(),
            "lastPolicySyncTime": t.string().optional(),
            "appliedState": t.string().optional(),
            "policyName": t.string().optional(),
            "enrollmentTokenName": t.string().optional(),
            "appliedPasswordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsOut"])
            ).optional(),
            "hardwareStatusSamples": t.array(
                t.proxy(renames["HardwareStatusOut"])
            ).optional(),
            "enrollmentTime": t.string().optional(),
            "applicationReports": t.array(
                t.proxy(renames["ApplicationReportOut"])
            ).optional(),
            "previousDeviceNames": t.array(t.string()).optional(),
            "managementMode": t.string().optional(),
            "enrollmentTokenData": t.string().optional(),
            "ownership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
    types["CommonCriteriaModeInfoIn"] = t.struct(
        {"commonCriteriaModeStatus": t.string().optional()}
    ).named(renames["CommonCriteriaModeInfoIn"])
    types["CommonCriteriaModeInfoOut"] = t.struct(
        {
            "commonCriteriaModeStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonCriteriaModeInfoOut"])
    types["PerAppResultIn"] = t.struct({"clearingResult": t.string().optional()}).named(
        renames["PerAppResultIn"]
    )
    types["PerAppResultOut"] = t.struct(
        {
            "clearingResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerAppResultOut"])
    types["CertAuthorityRemovedEventIn"] = t.struct(
        {
            "userId": t.integer().optional(),
            "certificate": t.string().optional(),
            "success": t.boolean().optional(),
        }
    ).named(renames["CertAuthorityRemovedEventIn"])
    types["CertAuthorityRemovedEventOut"] = t.struct(
        {
            "userId": t.integer().optional(),
            "certificate": t.string().optional(),
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertAuthorityRemovedEventOut"])
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
    types["WipeFailureEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WipeFailureEventIn"]
    )
    types["WipeFailureEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WipeFailureEventOut"])
    types["EnterpriseIn"] = t.struct(
        {
            "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
            "enterpriseDisplayName": t.string().optional(),
            "primaryColor": t.integer().optional(),
            "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
            "termsAndConditions": t.array(
                t.proxy(renames["TermsAndConditionsIn"])
            ).optional(),
            "enabledNotificationTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "logo": t.proxy(renames["ExternalDataIn"]).optional(),
            "appAutoApprovalEnabled": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
        }
    ).named(renames["EnterpriseIn"])
    types["EnterpriseOut"] = t.struct(
        {
            "signinDetails": t.array(t.proxy(renames["SigninDetailOut"])).optional(),
            "enterpriseDisplayName": t.string().optional(),
            "primaryColor": t.integer().optional(),
            "contactInfo": t.proxy(renames["ContactInfoOut"]).optional(),
            "termsAndConditions": t.array(
                t.proxy(renames["TermsAndConditionsOut"])
            ).optional(),
            "enabledNotificationTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "logo": t.proxy(renames["ExternalDataOut"]).optional(),
            "appAutoApprovalEnabled": t.boolean().optional(),
            "pubsubTopic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseOut"])
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
    types["MediaUnmountEventIn"] = t.struct(
        {"volumeLabel": t.string().optional(), "mountPoint": t.string().optional()}
    ).named(renames["MediaUnmountEventIn"])
    types["MediaUnmountEventOut"] = t.struct(
        {
            "volumeLabel": t.string().optional(),
            "mountPoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaUnmountEventOut"])
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
    types["IssueCommandResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IssueCommandResponseIn"]
    )
    types["IssueCommandResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IssueCommandResponseOut"])
    types["ClearAppsDataStatusIn"] = t.struct(
        {"results": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ClearAppsDataStatusIn"])
    types["ClearAppsDataStatusOut"] = t.struct(
        {
            "results": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearAppsDataStatusOut"])

    functions = {}
    functions["enterprisesPatch"] = androidmanagement.post(
        "v1/enterprises",
        t.struct(
            {
                "projectId": t.string().optional(),
                "enterpriseToken": t.string().optional(),
                "signupUrlName": t.string().optional(),
                "agreementAccepted": t.boolean().optional(),
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
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
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
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
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
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
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
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
                "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
                "enterpriseDisplayName": t.string().optional(),
                "primaryColor": t.integer().optional(),
                "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
                "termsAndConditions": t.array(
                    t.proxy(renames["TermsAndConditionsIn"])
                ).optional(),
                "enabledNotificationTypes": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "logo": t.proxy(renames["ExternalDataIn"]).optional(),
                "appAutoApprovalEnabled": t.boolean().optional(),
                "pubsubTopic": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EnterpriseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsPatch"] = androidmanagement.post(
        "v1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "versionCode": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsDelete"] = androidmanagement.post(
        "v1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "versionCode": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsGet"] = androidmanagement.post(
        "v1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "versionCode": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsList"] = androidmanagement.post(
        "v1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "versionCode": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsCreate"] = androidmanagement.post(
        "v1/{parent}/webApps",
        t.struct(
            {
                "parent": t.string().optional(),
                "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
                "title": t.string().optional(),
                "startUrl": t.string().optional(),
                "displayMode": t.string().optional(),
                "versionCode": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebAppOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesEnrollmentTokensDelete"] = androidmanagement.get(
        "v1/{parent}/enrollmentTokens",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEnrollmentTokensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesGet"] = androidmanagement.post(
        "v1/{name}:issueCommand",
        t.struct(
            {
                "name": t.string().optional(),
                "newPassword": t.string().optional(),
                "resetPasswordFlags": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "duration": t.string().optional(),
                "clearAppsDataParams": t.proxy(
                    renames["ClearAppsDataParamsIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "errorCode": t.string().optional(),
                "userName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesDelete"] = androidmanagement.post(
        "v1/{name}:issueCommand",
        t.struct(
            {
                "name": t.string().optional(),
                "newPassword": t.string().optional(),
                "resetPasswordFlags": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "duration": t.string().optional(),
                "clearAppsDataParams": t.proxy(
                    renames["ClearAppsDataParamsIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "errorCode": t.string().optional(),
                "userName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesPatch"] = androidmanagement.post(
        "v1/{name}:issueCommand",
        t.struct(
            {
                "name": t.string().optional(),
                "newPassword": t.string().optional(),
                "resetPasswordFlags": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "duration": t.string().optional(),
                "clearAppsDataParams": t.proxy(
                    renames["ClearAppsDataParamsIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "errorCode": t.string().optional(),
                "userName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesList"] = androidmanagement.post(
        "v1/{name}:issueCommand",
        t.struct(
            {
                "name": t.string().optional(),
                "newPassword": t.string().optional(),
                "resetPasswordFlags": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "duration": t.string().optional(),
                "clearAppsDataParams": t.proxy(
                    renames["ClearAppsDataParamsIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "errorCode": t.string().optional(),
                "userName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesIssueCommand"] = androidmanagement.post(
        "v1/{name}:issueCommand",
        t.struct(
            {
                "name": t.string().optional(),
                "newPassword": t.string().optional(),
                "resetPasswordFlags": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "duration": t.string().optional(),
                "clearAppsDataParams": t.proxy(
                    renames["ClearAppsDataParamsIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "errorCode": t.string().optional(),
                "userName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["enterprisesDevicesOperationsList"] = androidmanagement.post(
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
    functions["enterprisesApplicationsGet"] = androidmanagement.get(
        "v1/{name}",
        t.struct(
            {
                "languageCode": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebTokensCreate"] = androidmanagement.post(
        "v1/{parent}/webTokens",
        t.struct(
            {
                "parent": t.string().optional(),
                "enabledFeatures": t.array(t.string()).optional(),
                "permissions": t.array(t.string()).optional(),
                "name": t.string().optional(),
                "value": t.string().optional(),
                "parentFrameUrl": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebTokenOut"]),
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
    functions["enterprisesPoliciesGet"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["PolicyOut"]),
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
