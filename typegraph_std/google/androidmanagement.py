from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_androidmanagement() -> Import:
    androidmanagement = HTTPRuntime("https://androidmanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_androidmanagement_1_ErrorResponse",
        "KeyImportEventIn": "_androidmanagement_2_KeyImportEventIn",
        "KeyImportEventOut": "_androidmanagement_3_KeyImportEventOut",
        "UsageLogEventIn": "_androidmanagement_4_UsageLogEventIn",
        "UsageLogEventOut": "_androidmanagement_5_UsageLogEventOut",
        "CommandIn": "_androidmanagement_6_CommandIn",
        "CommandOut": "_androidmanagement_7_CommandOut",
        "HardwareStatusIn": "_androidmanagement_8_HardwareStatusIn",
        "HardwareStatusOut": "_androidmanagement_9_HardwareStatusOut",
        "DateIn": "_androidmanagement_10_DateIn",
        "DateOut": "_androidmanagement_11_DateOut",
        "TermsAndConditionsIn": "_androidmanagement_12_TermsAndConditionsIn",
        "TermsAndConditionsOut": "_androidmanagement_13_TermsAndConditionsOut",
        "LoggingStartedEventIn": "_androidmanagement_14_LoggingStartedEventIn",
        "LoggingStartedEventOut": "_androidmanagement_15_LoggingStartedEventOut",
        "LoggingStoppedEventIn": "_androidmanagement_16_LoggingStoppedEventIn",
        "LoggingStoppedEventOut": "_androidmanagement_17_LoggingStoppedEventOut",
        "PackageNameListIn": "_androidmanagement_18_PackageNameListIn",
        "PackageNameListOut": "_androidmanagement_19_PackageNameListOut",
        "SecurityPostureIn": "_androidmanagement_20_SecurityPostureIn",
        "SecurityPostureOut": "_androidmanagement_21_SecurityPostureOut",
        "MemoryEventIn": "_androidmanagement_22_MemoryEventIn",
        "MemoryEventOut": "_androidmanagement_23_MemoryEventOut",
        "OsShutdownEventIn": "_androidmanagement_24_OsShutdownEventIn",
        "OsShutdownEventOut": "_androidmanagement_25_OsShutdownEventOut",
        "KeyguardSecuredEventIn": "_androidmanagement_26_KeyguardSecuredEventIn",
        "KeyguardSecuredEventOut": "_androidmanagement_27_KeyguardSecuredEventOut",
        "MediaMountEventIn": "_androidmanagement_28_MediaMountEventIn",
        "MediaMountEventOut": "_androidmanagement_29_MediaMountEventOut",
        "DnsEventIn": "_androidmanagement_30_DnsEventIn",
        "DnsEventOut": "_androidmanagement_31_DnsEventOut",
        "PolicyIn": "_androidmanagement_32_PolicyIn",
        "PolicyOut": "_androidmanagement_33_PolicyOut",
        "ListWebAppsResponseIn": "_androidmanagement_34_ListWebAppsResponseIn",
        "ListWebAppsResponseOut": "_androidmanagement_35_ListWebAppsResponseOut",
        "ListOperationsResponseIn": "_androidmanagement_36_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_androidmanagement_37_ListOperationsResponseOut",
        "ClearAppsDataStatusIn": "_androidmanagement_38_ClearAppsDataStatusIn",
        "ClearAppsDataStatusOut": "_androidmanagement_39_ClearAppsDataStatusOut",
        "IssueCommandResponseIn": "_androidmanagement_40_IssueCommandResponseIn",
        "IssueCommandResponseOut": "_androidmanagement_41_IssueCommandResponseOut",
        "WebAppIn": "_androidmanagement_42_WebAppIn",
        "WebAppOut": "_androidmanagement_43_WebAppOut",
        "PostureDetailIn": "_androidmanagement_44_PostureDetailIn",
        "PostureDetailOut": "_androidmanagement_45_PostureDetailOut",
        "OncWifiContextIn": "_androidmanagement_46_OncWifiContextIn",
        "OncWifiContextOut": "_androidmanagement_47_OncWifiContextOut",
        "AppProcessInfoIn": "_androidmanagement_48_AppProcessInfoIn",
        "AppProcessInfoOut": "_androidmanagement_49_AppProcessInfoOut",
        "SystemUpdateInfoIn": "_androidmanagement_50_SystemUpdateInfoIn",
        "SystemUpdateInfoOut": "_androidmanagement_51_SystemUpdateInfoOut",
        "AdvancedSecurityOverridesIn": "_androidmanagement_52_AdvancedSecurityOverridesIn",
        "AdvancedSecurityOverridesOut": "_androidmanagement_53_AdvancedSecurityOverridesOut",
        "AppProcessStartEventIn": "_androidmanagement_54_AppProcessStartEventIn",
        "AppProcessStartEventOut": "_androidmanagement_55_AppProcessStartEventOut",
        "PermissionGrantIn": "_androidmanagement_56_PermissionGrantIn",
        "PermissionGrantOut": "_androidmanagement_57_PermissionGrantOut",
        "ComplianceRuleIn": "_androidmanagement_58_ComplianceRuleIn",
        "ComplianceRuleOut": "_androidmanagement_59_ComplianceRuleOut",
        "TelephonyInfoIn": "_androidmanagement_60_TelephonyInfoIn",
        "TelephonyInfoOut": "_androidmanagement_61_TelephonyInfoOut",
        "CertAuthorityRemovedEventIn": "_androidmanagement_62_CertAuthorityRemovedEventIn",
        "CertAuthorityRemovedEventOut": "_androidmanagement_63_CertAuthorityRemovedEventOut",
        "MediaUnmountEventIn": "_androidmanagement_64_MediaUnmountEventIn",
        "MediaUnmountEventOut": "_androidmanagement_65_MediaUnmountEventOut",
        "FilePushedEventIn": "_androidmanagement_66_FilePushedEventIn",
        "FilePushedEventOut": "_androidmanagement_67_FilePushedEventOut",
        "SystemUpdateIn": "_androidmanagement_68_SystemUpdateIn",
        "SystemUpdateOut": "_androidmanagement_69_SystemUpdateOut",
        "ApplicationEventIn": "_androidmanagement_70_ApplicationEventIn",
        "ApplicationEventOut": "_androidmanagement_71_ApplicationEventOut",
        "HardwareInfoIn": "_androidmanagement_72_HardwareInfoIn",
        "HardwareInfoOut": "_androidmanagement_73_HardwareInfoOut",
        "WipeActionIn": "_androidmanagement_74_WipeActionIn",
        "WipeActionOut": "_androidmanagement_75_WipeActionOut",
        "SetupActionIn": "_androidmanagement_76_SetupActionIn",
        "SetupActionOut": "_androidmanagement_77_SetupActionOut",
        "LogBufferSizeCriticalEventIn": "_androidmanagement_78_LogBufferSizeCriticalEventIn",
        "LogBufferSizeCriticalEventOut": "_androidmanagement_79_LogBufferSizeCriticalEventOut",
        "PersonalApplicationPolicyIn": "_androidmanagement_80_PersonalApplicationPolicyIn",
        "PersonalApplicationPolicyOut": "_androidmanagement_81_PersonalApplicationPolicyOut",
        "AppTrackInfoIn": "_androidmanagement_82_AppTrackInfoIn",
        "AppTrackInfoOut": "_androidmanagement_83_AppTrackInfoOut",
        "CrossProfilePoliciesIn": "_androidmanagement_84_CrossProfilePoliciesIn",
        "CrossProfilePoliciesOut": "_androidmanagement_85_CrossProfilePoliciesOut",
        "PerAppResultIn": "_androidmanagement_86_PerAppResultIn",
        "PerAppResultOut": "_androidmanagement_87_PerAppResultOut",
        "CryptoSelfTestCompletedEventIn": "_androidmanagement_88_CryptoSelfTestCompletedEventIn",
        "CryptoSelfTestCompletedEventOut": "_androidmanagement_89_CryptoSelfTestCompletedEventOut",
        "ListPoliciesResponseIn": "_androidmanagement_90_ListPoliciesResponseIn",
        "ListPoliciesResponseOut": "_androidmanagement_91_ListPoliciesResponseOut",
        "CertAuthorityInstalledEventIn": "_androidmanagement_92_CertAuthorityInstalledEventIn",
        "CertAuthorityInstalledEventOut": "_androidmanagement_93_CertAuthorityInstalledEventOut",
        "DeviceSettingsIn": "_androidmanagement_94_DeviceSettingsIn",
        "DeviceSettingsOut": "_androidmanagement_95_DeviceSettingsOut",
        "WipeFailureEventIn": "_androidmanagement_96_WipeFailureEventIn",
        "WipeFailureEventOut": "_androidmanagement_97_WipeFailureEventOut",
        "ApplicationPermissionIn": "_androidmanagement_98_ApplicationPermissionIn",
        "ApplicationPermissionOut": "_androidmanagement_99_ApplicationPermissionOut",
        "ManagedConfigurationTemplateIn": "_androidmanagement_100_ManagedConfigurationTemplateIn",
        "ManagedConfigurationTemplateOut": "_androidmanagement_101_ManagedConfigurationTemplateOut",
        "FilePulledEventIn": "_androidmanagement_102_FilePulledEventIn",
        "FilePulledEventOut": "_androidmanagement_103_FilePulledEventOut",
        "ListEnrollmentTokensResponseIn": "_androidmanagement_104_ListEnrollmentTokensResponseIn",
        "ListEnrollmentTokensResponseOut": "_androidmanagement_105_ListEnrollmentTokensResponseOut",
        "BatchUsageLogEventsIn": "_androidmanagement_106_BatchUsageLogEventsIn",
        "BatchUsageLogEventsOut": "_androidmanagement_107_BatchUsageLogEventsOut",
        "ContentProviderEndpointIn": "_androidmanagement_108_ContentProviderEndpointIn",
        "ContentProviderEndpointOut": "_androidmanagement_109_ContentProviderEndpointOut",
        "AdbShellInteractiveEventIn": "_androidmanagement_110_AdbShellInteractiveEventIn",
        "AdbShellInteractiveEventOut": "_androidmanagement_111_AdbShellInteractiveEventOut",
        "StatusIn": "_androidmanagement_112_StatusIn",
        "StatusOut": "_androidmanagement_113_StatusOut",
        "OsStartupEventIn": "_androidmanagement_114_OsStartupEventIn",
        "OsStartupEventOut": "_androidmanagement_115_OsStartupEventOut",
        "KeyIntegrityViolationEventIn": "_androidmanagement_116_KeyIntegrityViolationEventIn",
        "KeyIntegrityViolationEventOut": "_androidmanagement_117_KeyIntegrityViolationEventOut",
        "StatusReportingSettingsIn": "_androidmanagement_118_StatusReportingSettingsIn",
        "StatusReportingSettingsOut": "_androidmanagement_119_StatusReportingSettingsOut",
        "EnrollmentTokenIn": "_androidmanagement_120_EnrollmentTokenIn",
        "EnrollmentTokenOut": "_androidmanagement_121_EnrollmentTokenOut",
        "ListEnterprisesResponseIn": "_androidmanagement_122_ListEnterprisesResponseIn",
        "ListEnterprisesResponseOut": "_androidmanagement_123_ListEnterprisesResponseOut",
        "OncCertificateProviderIn": "_androidmanagement_124_OncCertificateProviderIn",
        "OncCertificateProviderOut": "_androidmanagement_125_OncCertificateProviderOut",
        "NonComplianceDetailConditionIn": "_androidmanagement_126_NonComplianceDetailConditionIn",
        "NonComplianceDetailConditionOut": "_androidmanagement_127_NonComplianceDetailConditionOut",
        "EmptyIn": "_androidmanagement_128_EmptyIn",
        "EmptyOut": "_androidmanagement_129_EmptyOut",
        "SigninDetailIn": "_androidmanagement_130_SigninDetailIn",
        "SigninDetailOut": "_androidmanagement_131_SigninDetailOut",
        "OperationIn": "_androidmanagement_132_OperationIn",
        "OperationOut": "_androidmanagement_133_OperationOut",
        "SoftwareInfoIn": "_androidmanagement_134_SoftwareInfoIn",
        "SoftwareInfoOut": "_androidmanagement_135_SoftwareInfoOut",
        "AdbShellCommandEventIn": "_androidmanagement_136_AdbShellCommandEventIn",
        "AdbShellCommandEventOut": "_androidmanagement_137_AdbShellCommandEventOut",
        "RemoteLockEventIn": "_androidmanagement_138_RemoteLockEventIn",
        "RemoteLockEventOut": "_androidmanagement_139_RemoteLockEventOut",
        "NetworkInfoIn": "_androidmanagement_140_NetworkInfoIn",
        "NetworkInfoOut": "_androidmanagement_141_NetworkInfoOut",
        "ManagedPropertyEntryIn": "_androidmanagement_142_ManagedPropertyEntryIn",
        "ManagedPropertyEntryOut": "_androidmanagement_143_ManagedPropertyEntryOut",
        "BlockActionIn": "_androidmanagement_144_BlockActionIn",
        "BlockActionOut": "_androidmanagement_145_BlockActionOut",
        "DeviceIn": "_androidmanagement_146_DeviceIn",
        "DeviceOut": "_androidmanagement_147_DeviceOut",
        "MemoryInfoIn": "_androidmanagement_148_MemoryInfoIn",
        "MemoryInfoOut": "_androidmanagement_149_MemoryInfoOut",
        "LaunchAppActionIn": "_androidmanagement_150_LaunchAppActionIn",
        "LaunchAppActionOut": "_androidmanagement_151_LaunchAppActionOut",
        "KioskCustomizationIn": "_androidmanagement_152_KioskCustomizationIn",
        "KioskCustomizationOut": "_androidmanagement_153_KioskCustomizationOut",
        "KeyguardDismissedEventIn": "_androidmanagement_154_KeyguardDismissedEventIn",
        "KeyguardDismissedEventOut": "_androidmanagement_155_KeyguardDismissedEventOut",
        "ExternalDataIn": "_androidmanagement_156_ExternalDataIn",
        "ExternalDataOut": "_androidmanagement_157_ExternalDataOut",
        "PasswordRequirementsIn": "_androidmanagement_158_PasswordRequirementsIn",
        "PasswordRequirementsOut": "_androidmanagement_159_PasswordRequirementsOut",
        "ConnectEventIn": "_androidmanagement_160_ConnectEventIn",
        "ConnectEventOut": "_androidmanagement_161_ConnectEventOut",
        "UserIn": "_androidmanagement_162_UserIn",
        "UserOut": "_androidmanagement_163_UserOut",
        "WebAppIconIn": "_androidmanagement_164_WebAppIconIn",
        "WebAppIconOut": "_androidmanagement_165_WebAppIconOut",
        "ApplicationReportIn": "_androidmanagement_166_ApplicationReportIn",
        "ApplicationReportOut": "_androidmanagement_167_ApplicationReportOut",
        "ApplicationPolicyIn": "_androidmanagement_168_ApplicationPolicyIn",
        "ApplicationPolicyOut": "_androidmanagement_169_ApplicationPolicyOut",
        "UserFacingMessageIn": "_androidmanagement_170_UserFacingMessageIn",
        "UserFacingMessageOut": "_androidmanagement_171_UserFacingMessageOut",
        "ClearAppsDataParamsIn": "_androidmanagement_172_ClearAppsDataParamsIn",
        "ClearAppsDataParamsOut": "_androidmanagement_173_ClearAppsDataParamsOut",
        "ApiLevelConditionIn": "_androidmanagement_174_ApiLevelConditionIn",
        "ApiLevelConditionOut": "_androidmanagement_175_ApiLevelConditionOut",
        "PersonalUsagePoliciesIn": "_androidmanagement_176_PersonalUsagePoliciesIn",
        "PersonalUsagePoliciesOut": "_androidmanagement_177_PersonalUsagePoliciesOut",
        "ChoosePrivateKeyRuleIn": "_androidmanagement_178_ChoosePrivateKeyRuleIn",
        "ChoosePrivateKeyRuleOut": "_androidmanagement_179_ChoosePrivateKeyRuleOut",
        "KeyguardDismissAuthAttemptEventIn": "_androidmanagement_180_KeyguardDismissAuthAttemptEventIn",
        "KeyguardDismissAuthAttemptEventOut": "_androidmanagement_181_KeyguardDismissAuthAttemptEventOut",
        "AlwaysOnVpnPackageIn": "_androidmanagement_182_AlwaysOnVpnPackageIn",
        "AlwaysOnVpnPackageOut": "_androidmanagement_183_AlwaysOnVpnPackageOut",
        "DisplayIn": "_androidmanagement_184_DisplayIn",
        "DisplayOut": "_androidmanagement_185_DisplayOut",
        "KeyedAppStateIn": "_androidmanagement_186_KeyedAppStateIn",
        "KeyedAppStateOut": "_androidmanagement_187_KeyedAppStateOut",
        "PolicyEnforcementRuleIn": "_androidmanagement_188_PolicyEnforcementRuleIn",
        "PolicyEnforcementRuleOut": "_androidmanagement_189_PolicyEnforcementRuleOut",
        "ApplicationIn": "_androidmanagement_190_ApplicationIn",
        "ApplicationOut": "_androidmanagement_191_ApplicationOut",
        "WebTokenIn": "_androidmanagement_192_WebTokenIn",
        "WebTokenOut": "_androidmanagement_193_WebTokenOut",
        "FreezePeriodIn": "_androidmanagement_194_FreezePeriodIn",
        "FreezePeriodOut": "_androidmanagement_195_FreezePeriodOut",
        "SignupUrlIn": "_androidmanagement_196_SignupUrlIn",
        "SignupUrlOut": "_androidmanagement_197_SignupUrlOut",
        "ProxyInfoIn": "_androidmanagement_198_ProxyInfoIn",
        "ProxyInfoOut": "_androidmanagement_199_ProxyInfoOut",
        "ContactInfoIn": "_androidmanagement_200_ContactInfoIn",
        "ContactInfoOut": "_androidmanagement_201_ContactInfoOut",
        "ApplicationReportingSettingsIn": "_androidmanagement_202_ApplicationReportingSettingsIn",
        "ApplicationReportingSettingsOut": "_androidmanagement_203_ApplicationReportingSettingsOut",
        "EnterpriseIn": "_androidmanagement_204_EnterpriseIn",
        "EnterpriseOut": "_androidmanagement_205_EnterpriseOut",
        "CertValidationFailureEventIn": "_androidmanagement_206_CertValidationFailureEventIn",
        "CertValidationFailureEventOut": "_androidmanagement_207_CertValidationFailureEventOut",
        "SpecificNonComplianceContextIn": "_androidmanagement_208_SpecificNonComplianceContextIn",
        "SpecificNonComplianceContextOut": "_androidmanagement_209_SpecificNonComplianceContextOut",
        "PowerManagementEventIn": "_androidmanagement_210_PowerManagementEventIn",
        "PowerManagementEventOut": "_androidmanagement_211_PowerManagementEventOut",
        "PasswordPoliciesContextIn": "_androidmanagement_212_PasswordPoliciesContextIn",
        "PasswordPoliciesContextOut": "_androidmanagement_213_PasswordPoliciesContextOut",
        "ListDevicesResponseIn": "_androidmanagement_214_ListDevicesResponseIn",
        "ListDevicesResponseOut": "_androidmanagement_215_ListDevicesResponseOut",
        "PersistentPreferredActivityIn": "_androidmanagement_216_PersistentPreferredActivityIn",
        "PersistentPreferredActivityOut": "_androidmanagement_217_PersistentPreferredActivityOut",
        "ExtensionConfigIn": "_androidmanagement_218_ExtensionConfigIn",
        "ExtensionConfigOut": "_androidmanagement_219_ExtensionConfigOut",
        "CommonCriteriaModeInfoIn": "_androidmanagement_220_CommonCriteriaModeInfoIn",
        "CommonCriteriaModeInfoOut": "_androidmanagement_221_CommonCriteriaModeInfoOut",
        "ManagedPropertyIn": "_androidmanagement_222_ManagedPropertyIn",
        "ManagedPropertyOut": "_androidmanagement_223_ManagedPropertyOut",
        "KeyGeneratedEventIn": "_androidmanagement_224_KeyGeneratedEventIn",
        "KeyGeneratedEventOut": "_androidmanagement_225_KeyGeneratedEventOut",
        "AppVersionIn": "_androidmanagement_226_AppVersionIn",
        "AppVersionOut": "_androidmanagement_227_AppVersionOut",
        "NonComplianceDetailIn": "_androidmanagement_228_NonComplianceDetailIn",
        "NonComplianceDetailOut": "_androidmanagement_229_NonComplianceDetailOut",
        "KeyDestructionEventIn": "_androidmanagement_230_KeyDestructionEventIn",
        "KeyDestructionEventOut": "_androidmanagement_231_KeyDestructionEventOut",
        "UsageLogIn": "_androidmanagement_232_UsageLogIn",
        "UsageLogOut": "_androidmanagement_233_UsageLogOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["UsageLogEventIn"] = t.struct(
        {
            "appProcessStartEvent": t.proxy(
                renames["AppProcessStartEventIn"]
            ).optional(),
            "keyImportEvent": t.proxy(renames["KeyImportEventIn"]).optional(),
            "loggingStartedEvent": t.proxy(renames["LoggingStartedEventIn"]).optional(),
            "eventId": t.string().optional(),
            "keyguardDismissedEvent": t.proxy(
                renames["KeyguardDismissedEventIn"]
            ).optional(),
            "adbShellInteractiveEvent": t.proxy(
                renames["AdbShellInteractiveEventIn"]
            ).optional(),
            "dnsEvent": t.proxy(renames["DnsEventIn"]).optional(),
            "mediaMountEvent": t.proxy(renames["MediaMountEventIn"]).optional(),
            "connectEvent": t.proxy(renames["ConnectEventIn"]).optional(),
            "filePulledEvent": t.proxy(renames["FilePulledEventIn"]).optional(),
            "loggingStoppedEvent": t.proxy(renames["LoggingStoppedEventIn"]).optional(),
            "keyDestructionEvent": t.proxy(renames["KeyDestructionEventIn"]).optional(),
            "certValidationFailureEvent": t.proxy(
                renames["CertValidationFailureEventIn"]
            ).optional(),
            "keyguardSecuredEvent": t.proxy(
                renames["KeyguardSecuredEventIn"]
            ).optional(),
            "certAuthorityInstalledEvent": t.proxy(
                renames["CertAuthorityInstalledEventIn"]
            ).optional(),
            "remoteLockEvent": t.proxy(renames["RemoteLockEventIn"]).optional(),
            "filePushedEvent": t.proxy(renames["FilePushedEventIn"]).optional(),
            "certAuthorityRemovedEvent": t.proxy(
                renames["CertAuthorityRemovedEventIn"]
            ).optional(),
            "eventType": t.string().optional(),
            "osStartupEvent": t.proxy(renames["OsStartupEventIn"]).optional(),
            "adbShellCommandEvent": t.proxy(
                renames["AdbShellCommandEventIn"]
            ).optional(),
            "wipeFailureEvent": t.proxy(renames["WipeFailureEventIn"]).optional(),
            "osShutdownEvent": t.proxy(renames["OsShutdownEventIn"]).optional(),
            "keyguardDismissAuthAttemptEvent": t.proxy(
                renames["KeyguardDismissAuthAttemptEventIn"]
            ).optional(),
            "eventTime": t.string().optional(),
            "mediaUnmountEvent": t.proxy(renames["MediaUnmountEventIn"]).optional(),
            "logBufferSizeCriticalEvent": t.proxy(
                renames["LogBufferSizeCriticalEventIn"]
            ).optional(),
            "keyGeneratedEvent": t.proxy(renames["KeyGeneratedEventIn"]).optional(),
            "cryptoSelfTestCompletedEvent": t.proxy(
                renames["CryptoSelfTestCompletedEventIn"]
            ).optional(),
            "keyIntegrityViolationEvent": t.proxy(
                renames["KeyIntegrityViolationEventIn"]
            ).optional(),
        }
    ).named(renames["UsageLogEventIn"])
    types["UsageLogEventOut"] = t.struct(
        {
            "appProcessStartEvent": t.proxy(
                renames["AppProcessStartEventOut"]
            ).optional(),
            "keyImportEvent": t.proxy(renames["KeyImportEventOut"]).optional(),
            "loggingStartedEvent": t.proxy(
                renames["LoggingStartedEventOut"]
            ).optional(),
            "eventId": t.string().optional(),
            "keyguardDismissedEvent": t.proxy(
                renames["KeyguardDismissedEventOut"]
            ).optional(),
            "adbShellInteractiveEvent": t.proxy(
                renames["AdbShellInteractiveEventOut"]
            ).optional(),
            "dnsEvent": t.proxy(renames["DnsEventOut"]).optional(),
            "mediaMountEvent": t.proxy(renames["MediaMountEventOut"]).optional(),
            "connectEvent": t.proxy(renames["ConnectEventOut"]).optional(),
            "filePulledEvent": t.proxy(renames["FilePulledEventOut"]).optional(),
            "loggingStoppedEvent": t.proxy(
                renames["LoggingStoppedEventOut"]
            ).optional(),
            "keyDestructionEvent": t.proxy(
                renames["KeyDestructionEventOut"]
            ).optional(),
            "certValidationFailureEvent": t.proxy(
                renames["CertValidationFailureEventOut"]
            ).optional(),
            "keyguardSecuredEvent": t.proxy(
                renames["KeyguardSecuredEventOut"]
            ).optional(),
            "certAuthorityInstalledEvent": t.proxy(
                renames["CertAuthorityInstalledEventOut"]
            ).optional(),
            "remoteLockEvent": t.proxy(renames["RemoteLockEventOut"]).optional(),
            "filePushedEvent": t.proxy(renames["FilePushedEventOut"]).optional(),
            "certAuthorityRemovedEvent": t.proxy(
                renames["CertAuthorityRemovedEventOut"]
            ).optional(),
            "eventType": t.string().optional(),
            "osStartupEvent": t.proxy(renames["OsStartupEventOut"]).optional(),
            "adbShellCommandEvent": t.proxy(
                renames["AdbShellCommandEventOut"]
            ).optional(),
            "wipeFailureEvent": t.proxy(renames["WipeFailureEventOut"]).optional(),
            "osShutdownEvent": t.proxy(renames["OsShutdownEventOut"]).optional(),
            "keyguardDismissAuthAttemptEvent": t.proxy(
                renames["KeyguardDismissAuthAttemptEventOut"]
            ).optional(),
            "eventTime": t.string().optional(),
            "mediaUnmountEvent": t.proxy(renames["MediaUnmountEventOut"]).optional(),
            "logBufferSizeCriticalEvent": t.proxy(
                renames["LogBufferSizeCriticalEventOut"]
            ).optional(),
            "keyGeneratedEvent": t.proxy(renames["KeyGeneratedEventOut"]).optional(),
            "cryptoSelfTestCompletedEvent": t.proxy(
                renames["CryptoSelfTestCompletedEventOut"]
            ).optional(),
            "keyIntegrityViolationEvent": t.proxy(
                renames["KeyIntegrityViolationEventOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageLogEventOut"])
    types["CommandIn"] = t.struct(
        {
            "type": t.string().optional(),
            "resetPasswordFlags": t.array(t.string()).optional(),
            "userName": t.string().optional(),
            "clearAppsDataParams": t.proxy(renames["ClearAppsDataParamsIn"]).optional(),
            "errorCode": t.string().optional(),
            "newPassword": t.string().optional(),
            "createTime": t.string().optional(),
            "duration": t.string().optional(),
        }
    ).named(renames["CommandIn"])
    types["CommandOut"] = t.struct(
        {
            "type": t.string().optional(),
            "resetPasswordFlags": t.array(t.string()).optional(),
            "userName": t.string().optional(),
            "clearAppsDataParams": t.proxy(
                renames["ClearAppsDataParamsOut"]
            ).optional(),
            "errorCode": t.string().optional(),
            "newPassword": t.string().optional(),
            "createTime": t.string().optional(),
            "duration": t.string().optional(),
            "clearAppsDataStatus": t.proxy(
                renames["ClearAppsDataStatusOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommandOut"])
    types["HardwareStatusIn"] = t.struct(
        {
            "gpuTemperatures": t.array(t.number()).optional(),
            "batteryTemperatures": t.array(t.number()).optional(),
            "skinTemperatures": t.array(t.number()).optional(),
            "cpuUsages": t.array(t.number()).optional(),
            "cpuTemperatures": t.array(t.number()).optional(),
            "createTime": t.string().optional(),
            "fanSpeeds": t.array(t.number()).optional(),
        }
    ).named(renames["HardwareStatusIn"])
    types["HardwareStatusOut"] = t.struct(
        {
            "gpuTemperatures": t.array(t.number()).optional(),
            "batteryTemperatures": t.array(t.number()).optional(),
            "skinTemperatures": t.array(t.number()).optional(),
            "cpuUsages": t.array(t.number()).optional(),
            "cpuTemperatures": t.array(t.number()).optional(),
            "createTime": t.string().optional(),
            "fanSpeeds": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HardwareStatusOut"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
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
    types["LoggingStartedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoggingStartedEventIn"]
    )
    types["LoggingStartedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoggingStartedEventOut"])
    types["LoggingStoppedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["LoggingStoppedEventIn"]
    )
    types["LoggingStoppedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LoggingStoppedEventOut"])
    types["PackageNameListIn"] = t.struct(
        {"packageNames": t.array(t.string()).optional()}
    ).named(renames["PackageNameListIn"])
    types["PackageNameListOut"] = t.struct(
        {
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PackageNameListOut"])
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
    types["OsShutdownEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OsShutdownEventIn"]
    )
    types["OsShutdownEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["OsShutdownEventOut"])
    types["KeyguardSecuredEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyguardSecuredEventIn"]
    )
    types["KeyguardSecuredEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["KeyguardSecuredEventOut"])
    types["MediaMountEventIn"] = t.struct(
        {"mountPoint": t.string().optional(), "volumeLabel": t.string().optional()}
    ).named(renames["MediaMountEventIn"])
    types["MediaMountEventOut"] = t.struct(
        {
            "mountPoint": t.string().optional(),
            "volumeLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MediaMountEventOut"])
    types["DnsEventIn"] = t.struct(
        {
            "ipAddresses": t.array(t.string()).optional(),
            "hostname": t.string().optional(),
            "totalIpAddressesReturned": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["DnsEventIn"])
    types["DnsEventOut"] = t.struct(
        {
            "ipAddresses": t.array(t.string()).optional(),
            "hostname": t.string().optional(),
            "totalIpAddressesReturned": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsEventOut"])
    types["PolicyIn"] = t.struct(
        {
            "frpAdminEmails": t.array(t.string()).optional(),
            "safeBootDisabled": t.boolean().optional(),
            "mountPhysicalMediaDisabled": t.boolean().optional(),
            "cameraDisabled": t.boolean().optional(),
            "appAutoUpdatePolicy": t.string().optional(),
            "permittedAccessibilityServices": t.proxy(
                renames["PackageNameListIn"]
            ).optional(),
            "bluetoothContactSharingDisabled": t.boolean().optional(),
            "unmuteMicrophoneDisabled": t.boolean().optional(),
            "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
            "alwaysOnVpnPackage": t.proxy(renames["AlwaysOnVpnPackageIn"]).optional(),
            "installUnknownSourcesAllowed": t.boolean().optional(),
            "bluetoothConfigDisabled": t.boolean().optional(),
            "advancedSecurityOverrides": t.proxy(
                renames["AdvancedSecurityOverridesIn"]
            ).optional(),
            "addUserDisabled": t.boolean().optional(),
            "personalUsagePolicies": t.proxy(
                renames["PersonalUsagePoliciesIn"]
            ).optional(),
            "applications": t.array(t.proxy(renames["ApplicationPolicyIn"])).optional(),
            "removeUserDisabled": t.boolean().optional(),
            "microphoneAccess": t.string().optional(),
            "complianceRules": t.array(t.proxy(renames["ComplianceRuleIn"])).optional(),
            "createWindowsDisabled": t.boolean().optional(),
            "shortSupportMessage": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "policyEnforcementRules": t.array(
                t.proxy(renames["PolicyEnforcementRuleIn"])
            ).optional(),
            "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
            "networkEscapeHatchEnabled": t.boolean().optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "kioskCustomLauncherEnabled": t.boolean().optional(),
            "outgoingBeamDisabled": t.boolean().optional(),
            "permittedInputMethods": t.proxy(renames["PackageNameListIn"]).optional(),
            "deviceOwnerLockScreenInfo": t.proxy(
                renames["UserFacingMessageIn"]
            ).optional(),
            "wifiConfigsLockdownEnabled": t.boolean().optional(),
            "wifiConfigDisabled": t.boolean().optional(),
            "bluetoothDisabled": t.boolean().optional(),
            "tetheringConfigDisabled": t.boolean().optional(),
            "adjustVolumeDisabled": t.boolean().optional(),
            "outgoingCallsDisabled": t.boolean().optional(),
            "ensureVerifyAppsEnabled": t.boolean().optional(),
            "choosePrivateKeyRules": t.array(
                t.proxy(renames["ChoosePrivateKeyRuleIn"])
            ).optional(),
            "keyguardDisabled": t.boolean().optional(),
            "passwordRequirements": t.proxy(
                renames["PasswordRequirementsIn"]
            ).optional(),
            "setWallpaperDisabled": t.boolean().optional(),
            "cellBroadcastsConfigDisabled": t.boolean().optional(),
            "uninstallAppsDisabled": t.boolean().optional(),
            "minimumApiLevel": t.integer().optional(),
            "statusReportingSettings": t.proxy(
                renames["StatusReportingSettingsIn"]
            ).optional(),
            "maximumTimeToLock": t.string().optional(),
            "stayOnPluggedModes": t.array(t.string()).optional(),
            "crossProfilePolicies": t.proxy(
                renames["CrossProfilePoliciesIn"]
            ).optional(),
            "version": t.string().optional(),
            "privateKeySelectionEnabled": t.boolean().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantIn"])
            ).optional(),
            "skipFirstUseHintsEnabled": t.boolean().optional(),
            "factoryResetDisabled": t.boolean().optional(),
            "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
            "longSupportMessage": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "preferentialNetworkService": t.string().optional(),
            "openNetworkConfiguration": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "modifyAccountsDisabled": t.boolean().optional(),
            "encryptionPolicy": t.string().optional(),
            "statusBarDisabled": t.boolean().optional(),
            "playStoreMode": t.string().optional(),
            "installAppsDisabled": t.boolean().optional(),
            "cameraAccess": t.string().optional(),
            "shareLocationDisabled": t.boolean().optional(),
            "networkResetDisabled": t.boolean().optional(),
            "usbMassStorageEnabled": t.boolean().optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "blockApplicationsEnabled": t.boolean().optional(),
            "autoDateAndTimeZone": t.string().optional(),
            "kioskCustomization": t.proxy(renames["KioskCustomizationIn"]).optional(),
            "debuggingFeaturesAllowed": t.boolean().optional(),
            "setUserIconDisabled": t.boolean().optional(),
            "dataRoamingDisabled": t.boolean().optional(),
            "smsDisabled": t.boolean().optional(),
            "androidDevicePolicyTracks": t.array(t.string()).optional(),
            "mobileNetworksConfigDisabled": t.boolean().optional(),
            "locationMode": t.string().optional(),
            "oncCertificateProviders": t.array(
                t.proxy(renames["OncCertificateProviderIn"])
            ).optional(),
            "usbFileTransferDisabled": t.boolean().optional(),
            "passwordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsIn"])
            ).optional(),
            "credentialsConfigDisabled": t.boolean().optional(),
            "persistentPreferredActivities": t.array(
                t.proxy(renames["PersistentPreferredActivityIn"])
            ).optional(),
            "vpnConfigDisabled": t.boolean().optional(),
            "autoTimeRequired": t.boolean().optional(),
            "keyguardDisabledFeatures": t.array(t.string()).optional(),
            "funDisabled": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "frpAdminEmails": t.array(t.string()).optional(),
            "safeBootDisabled": t.boolean().optional(),
            "mountPhysicalMediaDisabled": t.boolean().optional(),
            "cameraDisabled": t.boolean().optional(),
            "appAutoUpdatePolicy": t.string().optional(),
            "permittedAccessibilityServices": t.proxy(
                renames["PackageNameListOut"]
            ).optional(),
            "bluetoothContactSharingDisabled": t.boolean().optional(),
            "unmuteMicrophoneDisabled": t.boolean().optional(),
            "systemUpdate": t.proxy(renames["SystemUpdateOut"]).optional(),
            "alwaysOnVpnPackage": t.proxy(renames["AlwaysOnVpnPackageOut"]).optional(),
            "installUnknownSourcesAllowed": t.boolean().optional(),
            "bluetoothConfigDisabled": t.boolean().optional(),
            "advancedSecurityOverrides": t.proxy(
                renames["AdvancedSecurityOverridesOut"]
            ).optional(),
            "addUserDisabled": t.boolean().optional(),
            "personalUsagePolicies": t.proxy(
                renames["PersonalUsagePoliciesOut"]
            ).optional(),
            "applications": t.array(
                t.proxy(renames["ApplicationPolicyOut"])
            ).optional(),
            "removeUserDisabled": t.boolean().optional(),
            "microphoneAccess": t.string().optional(),
            "complianceRules": t.array(
                t.proxy(renames["ComplianceRuleOut"])
            ).optional(),
            "createWindowsDisabled": t.boolean().optional(),
            "shortSupportMessage": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "policyEnforcementRules": t.array(
                t.proxy(renames["PolicyEnforcementRuleOut"])
            ).optional(),
            "recommendedGlobalProxy": t.proxy(renames["ProxyInfoOut"]).optional(),
            "networkEscapeHatchEnabled": t.boolean().optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "kioskCustomLauncherEnabled": t.boolean().optional(),
            "outgoingBeamDisabled": t.boolean().optional(),
            "permittedInputMethods": t.proxy(renames["PackageNameListOut"]).optional(),
            "deviceOwnerLockScreenInfo": t.proxy(
                renames["UserFacingMessageOut"]
            ).optional(),
            "wifiConfigsLockdownEnabled": t.boolean().optional(),
            "wifiConfigDisabled": t.boolean().optional(),
            "bluetoothDisabled": t.boolean().optional(),
            "tetheringConfigDisabled": t.boolean().optional(),
            "adjustVolumeDisabled": t.boolean().optional(),
            "outgoingCallsDisabled": t.boolean().optional(),
            "ensureVerifyAppsEnabled": t.boolean().optional(),
            "choosePrivateKeyRules": t.array(
                t.proxy(renames["ChoosePrivateKeyRuleOut"])
            ).optional(),
            "keyguardDisabled": t.boolean().optional(),
            "passwordRequirements": t.proxy(
                renames["PasswordRequirementsOut"]
            ).optional(),
            "setWallpaperDisabled": t.boolean().optional(),
            "cellBroadcastsConfigDisabled": t.boolean().optional(),
            "uninstallAppsDisabled": t.boolean().optional(),
            "minimumApiLevel": t.integer().optional(),
            "statusReportingSettings": t.proxy(
                renames["StatusReportingSettingsOut"]
            ).optional(),
            "maximumTimeToLock": t.string().optional(),
            "stayOnPluggedModes": t.array(t.string()).optional(),
            "crossProfilePolicies": t.proxy(
                renames["CrossProfilePoliciesOut"]
            ).optional(),
            "version": t.string().optional(),
            "privateKeySelectionEnabled": t.boolean().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "usageLog": t.proxy(renames["UsageLogOut"]).optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantOut"])
            ).optional(),
            "skipFirstUseHintsEnabled": t.boolean().optional(),
            "factoryResetDisabled": t.boolean().optional(),
            "setupActions": t.array(t.proxy(renames["SetupActionOut"])).optional(),
            "longSupportMessage": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "preferentialNetworkService": t.string().optional(),
            "openNetworkConfiguration": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "modifyAccountsDisabled": t.boolean().optional(),
            "encryptionPolicy": t.string().optional(),
            "statusBarDisabled": t.boolean().optional(),
            "playStoreMode": t.string().optional(),
            "installAppsDisabled": t.boolean().optional(),
            "cameraAccess": t.string().optional(),
            "shareLocationDisabled": t.boolean().optional(),
            "networkResetDisabled": t.boolean().optional(),
            "usbMassStorageEnabled": t.boolean().optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "blockApplicationsEnabled": t.boolean().optional(),
            "autoDateAndTimeZone": t.string().optional(),
            "kioskCustomization": t.proxy(renames["KioskCustomizationOut"]).optional(),
            "debuggingFeaturesAllowed": t.boolean().optional(),
            "setUserIconDisabled": t.boolean().optional(),
            "dataRoamingDisabled": t.boolean().optional(),
            "smsDisabled": t.boolean().optional(),
            "androidDevicePolicyTracks": t.array(t.string()).optional(),
            "mobileNetworksConfigDisabled": t.boolean().optional(),
            "locationMode": t.string().optional(),
            "oncCertificateProviders": t.array(
                t.proxy(renames["OncCertificateProviderOut"])
            ).optional(),
            "usbFileTransferDisabled": t.boolean().optional(),
            "passwordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsOut"])
            ).optional(),
            "credentialsConfigDisabled": t.boolean().optional(),
            "persistentPreferredActivities": t.array(
                t.proxy(renames["PersistentPreferredActivityOut"])
            ).optional(),
            "vpnConfigDisabled": t.boolean().optional(),
            "autoTimeRequired": t.boolean().optional(),
            "keyguardDisabledFeatures": t.array(t.string()).optional(),
            "funDisabled": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListWebAppsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "webApps": t.array(t.proxy(renames["WebAppIn"])).optional(),
        }
    ).named(renames["ListWebAppsResponseIn"])
    types["ListWebAppsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "webApps": t.array(t.proxy(renames["WebAppOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListWebAppsResponseOut"])
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
    types["ClearAppsDataStatusIn"] = t.struct(
        {"results": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ClearAppsDataStatusIn"])
    types["ClearAppsDataStatusOut"] = t.struct(
        {
            "results": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearAppsDataStatusOut"])
    types["IssueCommandResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["IssueCommandResponseIn"]
    )
    types["IssueCommandResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["IssueCommandResponseOut"])
    types["WebAppIn"] = t.struct(
        {
            "icons": t.array(t.proxy(renames["WebAppIconIn"])).optional(),
            "displayMode": t.string().optional(),
            "startUrl": t.string().optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "versionCode": t.string().optional(),
        }
    ).named(renames["WebAppIn"])
    types["WebAppOut"] = t.struct(
        {
            "icons": t.array(t.proxy(renames["WebAppIconOut"])).optional(),
            "displayMode": t.string().optional(),
            "startUrl": t.string().optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "versionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppOut"])
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
    types["OncWifiContextIn"] = t.struct({"wifiGuid": t.string().optional()}).named(
        renames["OncWifiContextIn"]
    )
    types["OncWifiContextOut"] = t.struct(
        {
            "wifiGuid": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OncWifiContextOut"])
    types["AppProcessInfoIn"] = t.struct(
        {
            "pid": t.integer().optional(),
            "uid": t.integer().optional(),
            "apkSha256Hash": t.string().optional(),
            "seinfo": t.string().optional(),
            "processName": t.string().optional(),
            "startTime": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
        }
    ).named(renames["AppProcessInfoIn"])
    types["AppProcessInfoOut"] = t.struct(
        {
            "pid": t.integer().optional(),
            "uid": t.integer().optional(),
            "apkSha256Hash": t.string().optional(),
            "seinfo": t.string().optional(),
            "processName": t.string().optional(),
            "startTime": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProcessInfoOut"])
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
    types["AdvancedSecurityOverridesIn"] = t.struct(
        {
            "commonCriteriaMode": t.string().optional(),
            "googlePlayProtectVerifyApps": t.string().optional(),
            "developerSettings": t.string().optional(),
            "untrustedAppsPolicy": t.string().optional(),
            "personalAppsThatCanReadWorkNotifications": t.array(t.string()).optional(),
        }
    ).named(renames["AdvancedSecurityOverridesIn"])
    types["AdvancedSecurityOverridesOut"] = t.struct(
        {
            "commonCriteriaMode": t.string().optional(),
            "googlePlayProtectVerifyApps": t.string().optional(),
            "developerSettings": t.string().optional(),
            "untrustedAppsPolicy": t.string().optional(),
            "personalAppsThatCanReadWorkNotifications": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdvancedSecurityOverridesOut"])
    types["AppProcessStartEventIn"] = t.struct(
        {"processInfo": t.proxy(renames["AppProcessInfoIn"]).optional()}
    ).named(renames["AppProcessStartEventIn"])
    types["AppProcessStartEventOut"] = t.struct(
        {
            "processInfo": t.proxy(renames["AppProcessInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppProcessStartEventOut"])
    types["PermissionGrantIn"] = t.struct(
        {"policy": t.string().optional(), "permission": t.string().optional()}
    ).named(renames["PermissionGrantIn"])
    types["PermissionGrantOut"] = t.struct(
        {
            "policy": t.string().optional(),
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PermissionGrantOut"])
    types["ComplianceRuleIn"] = t.struct(
        {
            "disableApps": t.boolean().optional(),
            "packageNamesToDisable": t.array(t.string()).optional(),
            "apiLevelCondition": t.proxy(renames["ApiLevelConditionIn"]).optional(),
            "nonComplianceDetailCondition": t.proxy(
                renames["NonComplianceDetailConditionIn"]
            ).optional(),
        }
    ).named(renames["ComplianceRuleIn"])
    types["ComplianceRuleOut"] = t.struct(
        {
            "disableApps": t.boolean().optional(),
            "packageNamesToDisable": t.array(t.string()).optional(),
            "apiLevelCondition": t.proxy(renames["ApiLevelConditionOut"]).optional(),
            "nonComplianceDetailCondition": t.proxy(
                renames["NonComplianceDetailConditionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComplianceRuleOut"])
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
    types["FilePushedEventIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FilePushedEventIn"]
    )
    types["FilePushedEventOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilePushedEventOut"])
    types["SystemUpdateIn"] = t.struct(
        {
            "type": t.string().optional(),
            "startMinutes": t.integer().optional(),
            "freezePeriods": t.array(t.proxy(renames["FreezePeriodIn"])).optional(),
            "endMinutes": t.integer().optional(),
        }
    ).named(renames["SystemUpdateIn"])
    types["SystemUpdateOut"] = t.struct(
        {
            "type": t.string().optional(),
            "startMinutes": t.integer().optional(),
            "freezePeriods": t.array(t.proxy(renames["FreezePeriodOut"])).optional(),
            "endMinutes": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemUpdateOut"])
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
    types["HardwareInfoIn"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "skinThrottlingTemperatures": t.array(t.number()).optional(),
            "model": t.string().optional(),
            "brand": t.string().optional(),
            "cpuThrottlingTemperatures": t.array(t.number()).optional(),
            "gpuShutdownTemperatures": t.array(t.number()).optional(),
            "hardware": t.string().optional(),
            "manufacturer": t.string().optional(),
            "cpuShutdownTemperatures": t.array(t.number()).optional(),
            "batteryShutdownTemperatures": t.array(t.number()).optional(),
            "batteryThrottlingTemperatures": t.array(t.number()).optional(),
            "deviceBasebandVersion": t.string().optional(),
            "skinShutdownTemperatures": t.array(t.number()).optional(),
            "gpuThrottlingTemperatures": t.array(t.number()).optional(),
        }
    ).named(renames["HardwareInfoIn"])
    types["HardwareInfoOut"] = t.struct(
        {
            "serialNumber": t.string().optional(),
            "skinThrottlingTemperatures": t.array(t.number()).optional(),
            "model": t.string().optional(),
            "enterpriseSpecificId": t.string().optional(),
            "brand": t.string().optional(),
            "cpuThrottlingTemperatures": t.array(t.number()).optional(),
            "gpuShutdownTemperatures": t.array(t.number()).optional(),
            "hardware": t.string().optional(),
            "manufacturer": t.string().optional(),
            "cpuShutdownTemperatures": t.array(t.number()).optional(),
            "batteryShutdownTemperatures": t.array(t.number()).optional(),
            "batteryThrottlingTemperatures": t.array(t.number()).optional(),
            "deviceBasebandVersion": t.string().optional(),
            "skinShutdownTemperatures": t.array(t.number()).optional(),
            "gpuThrottlingTemperatures": t.array(t.number()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HardwareInfoOut"])
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
    types["SetupActionIn"] = t.struct(
        {
            "launchApp": t.proxy(renames["LaunchAppActionIn"]).optional(),
            "title": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "description": t.proxy(renames["UserFacingMessageIn"]).optional(),
        }
    ).named(renames["SetupActionIn"])
    types["SetupActionOut"] = t.struct(
        {
            "launchApp": t.proxy(renames["LaunchAppActionOut"]).optional(),
            "title": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "description": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetupActionOut"])
    types["LogBufferSizeCriticalEventIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["LogBufferSizeCriticalEventIn"])
    types["LogBufferSizeCriticalEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["LogBufferSizeCriticalEventOut"])
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
    types["CrossProfilePoliciesIn"] = t.struct(
        {
            "crossProfileCopyPaste": t.string().optional(),
            "showWorkContactsInPersonalProfile": t.string().optional(),
            "workProfileWidgetsDefault": t.string().optional(),
            "crossProfileDataSharing": t.string().optional(),
        }
    ).named(renames["CrossProfilePoliciesIn"])
    types["CrossProfilePoliciesOut"] = t.struct(
        {
            "crossProfileCopyPaste": t.string().optional(),
            "showWorkContactsInPersonalProfile": t.string().optional(),
            "workProfileWidgetsDefault": t.string().optional(),
            "crossProfileDataSharing": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrossProfilePoliciesOut"])
    types["PerAppResultIn"] = t.struct({"clearingResult": t.string().optional()}).named(
        renames["PerAppResultIn"]
    )
    types["PerAppResultOut"] = t.struct(
        {
            "clearingResult": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerAppResultOut"])
    types["CryptoSelfTestCompletedEventIn"] = t.struct(
        {"success": t.boolean().optional()}
    ).named(renames["CryptoSelfTestCompletedEventIn"])
    types["CryptoSelfTestCompletedEventOut"] = t.struct(
        {
            "success": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CryptoSelfTestCompletedEventOut"])
    types["ListPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "policies": t.array(t.proxy(renames["PolicyIn"])).optional(),
        }
    ).named(renames["ListPoliciesResponseIn"])
    types["ListPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "policies": t.array(t.proxy(renames["PolicyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPoliciesResponseOut"])
    types["CertAuthorityInstalledEventIn"] = t.struct(
        {
            "success": t.boolean().optional(),
            "certificate": t.string().optional(),
            "userId": t.integer().optional(),
        }
    ).named(renames["CertAuthorityInstalledEventIn"])
    types["CertAuthorityInstalledEventOut"] = t.struct(
        {
            "success": t.boolean().optional(),
            "certificate": t.string().optional(),
            "userId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertAuthorityInstalledEventOut"])
    types["DeviceSettingsIn"] = t.struct(
        {
            "encryptionStatus": t.string().optional(),
            "verifyAppsEnabled": t.boolean().optional(),
            "unknownSourcesEnabled": t.boolean().optional(),
            "adbEnabled": t.boolean().optional(),
            "isDeviceSecure": t.boolean().optional(),
            "isEncrypted": t.boolean().optional(),
            "developmentSettingsEnabled": t.boolean().optional(),
        }
    ).named(renames["DeviceSettingsIn"])
    types["DeviceSettingsOut"] = t.struct(
        {
            "encryptionStatus": t.string().optional(),
            "verifyAppsEnabled": t.boolean().optional(),
            "unknownSourcesEnabled": t.boolean().optional(),
            "adbEnabled": t.boolean().optional(),
            "isDeviceSecure": t.boolean().optional(),
            "isEncrypted": t.boolean().optional(),
            "developmentSettingsEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSettingsOut"])
    types["WipeFailureEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["WipeFailureEventIn"]
    )
    types["WipeFailureEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["WipeFailureEventOut"])
    types["ApplicationPermissionIn"] = t.struct(
        {
            "description": t.string().optional(),
            "permissionId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApplicationPermissionIn"])
    types["ApplicationPermissionOut"] = t.struct(
        {
            "description": t.string().optional(),
            "permissionId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationPermissionOut"])
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
    types["FilePulledEventIn"] = t.struct({"filePath": t.string().optional()}).named(
        renames["FilePulledEventIn"]
    )
    types["FilePulledEventOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FilePulledEventOut"])
    types["ListEnrollmentTokensResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "enrollmentTokens": t.array(
                t.proxy(renames["EnrollmentTokenIn"])
            ).optional(),
        }
    ).named(renames["ListEnrollmentTokensResponseIn"])
    types["ListEnrollmentTokensResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "enrollmentTokens": t.array(
                t.proxy(renames["EnrollmentTokenOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEnrollmentTokensResponseOut"])
    types["BatchUsageLogEventsIn"] = t.struct(
        {
            "retrievalTime": t.string().optional(),
            "usageLogEvents": t.array(t.proxy(renames["UsageLogEventIn"])).optional(),
            "device": t.string().optional(),
            "user": t.string().optional(),
        }
    ).named(renames["BatchUsageLogEventsIn"])
    types["BatchUsageLogEventsOut"] = t.struct(
        {
            "retrievalTime": t.string().optional(),
            "usageLogEvents": t.array(t.proxy(renames["UsageLogEventOut"])).optional(),
            "device": t.string().optional(),
            "user": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUsageLogEventsOut"])
    types["ContentProviderEndpointIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "signingCertsSha256": t.array(t.string()),
            "uri": t.string().optional(),
        }
    ).named(renames["ContentProviderEndpointIn"])
    types["ContentProviderEndpointOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "signingCertsSha256": t.array(t.string()),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContentProviderEndpointOut"])
    types["AdbShellInteractiveEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdbShellInteractiveEventIn"]
    )
    types["AdbShellInteractiveEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdbShellInteractiveEventOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["StatusReportingSettingsIn"] = t.struct(
        {
            "networkInfoEnabled": t.boolean().optional(),
            "applicationReportsEnabled": t.boolean().optional(),
            "commonCriteriaModeEnabled": t.boolean().optional(),
            "powerManagementEventsEnabled": t.boolean().optional(),
            "hardwareStatusEnabled": t.boolean().optional(),
            "softwareInfoEnabled": t.boolean().optional(),
            "displayInfoEnabled": t.boolean().optional(),
            "applicationReportingSettings": t.proxy(
                renames["ApplicationReportingSettingsIn"]
            ).optional(),
            "deviceSettingsEnabled": t.boolean().optional(),
            "systemPropertiesEnabled": t.boolean().optional(),
            "memoryInfoEnabled": t.boolean().optional(),
        }
    ).named(renames["StatusReportingSettingsIn"])
    types["StatusReportingSettingsOut"] = t.struct(
        {
            "networkInfoEnabled": t.boolean().optional(),
            "applicationReportsEnabled": t.boolean().optional(),
            "commonCriteriaModeEnabled": t.boolean().optional(),
            "powerManagementEventsEnabled": t.boolean().optional(),
            "hardwareStatusEnabled": t.boolean().optional(),
            "softwareInfoEnabled": t.boolean().optional(),
            "displayInfoEnabled": t.boolean().optional(),
            "applicationReportingSettings": t.proxy(
                renames["ApplicationReportingSettingsOut"]
            ).optional(),
            "deviceSettingsEnabled": t.boolean().optional(),
            "systemPropertiesEnabled": t.boolean().optional(),
            "memoryInfoEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusReportingSettingsOut"])
    types["EnrollmentTokenIn"] = t.struct(
        {
            "name": t.string().optional(),
            "qrCode": t.string().optional(),
            "policyName": t.string().optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "oneTimeOnly": t.boolean().optional(),
            "duration": t.string().optional(),
            "additionalData": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "expirationTimestamp": t.string().optional(),
            "value": t.string().optional(),
        }
    ).named(renames["EnrollmentTokenIn"])
    types["EnrollmentTokenOut"] = t.struct(
        {
            "name": t.string().optional(),
            "qrCode": t.string().optional(),
            "policyName": t.string().optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "oneTimeOnly": t.boolean().optional(),
            "duration": t.string().optional(),
            "additionalData": t.string().optional(),
            "allowPersonalUsage": t.string().optional(),
            "expirationTimestamp": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnrollmentTokenOut"])
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
    types["NonComplianceDetailConditionIn"] = t.struct(
        {
            "nonComplianceReason": t.string().optional(),
            "settingName": t.string().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["NonComplianceDetailConditionIn"])
    types["NonComplianceDetailConditionOut"] = t.struct(
        {
            "nonComplianceReason": t.string().optional(),
            "settingName": t.string().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonComplianceDetailConditionOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SigninDetailIn"] = t.struct(
        {
            "allowPersonalUsage": t.string().optional(),
            "signinUrl": t.string().optional(),
            "qrCode": t.string().optional(),
            "signinEnrollmentToken": t.string().optional(),
        }
    ).named(renames["SigninDetailIn"])
    types["SigninDetailOut"] = t.struct(
        {
            "allowPersonalUsage": t.string().optional(),
            "signinUrl": t.string().optional(),
            "qrCode": t.string().optional(),
            "signinEnrollmentToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SigninDetailOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["SoftwareInfoIn"] = t.struct(
        {
            "primaryLanguageCode": t.string().optional(),
            "bootloaderVersion": t.string().optional(),
            "androidBuildNumber": t.string().optional(),
            "androidVersion": t.string().optional(),
            "deviceKernelVersion": t.string().optional(),
            "systemUpdateInfo": t.proxy(renames["SystemUpdateInfoIn"]).optional(),
            "androidDevicePolicyVersionName": t.string().optional(),
            "securityPatchLevel": t.string().optional(),
            "androidBuildTime": t.string().optional(),
            "androidDevicePolicyVersionCode": t.integer().optional(),
            "deviceBuildSignature": t.string().optional(),
        }
    ).named(renames["SoftwareInfoIn"])
    types["SoftwareInfoOut"] = t.struct(
        {
            "primaryLanguageCode": t.string().optional(),
            "bootloaderVersion": t.string().optional(),
            "androidBuildNumber": t.string().optional(),
            "androidVersion": t.string().optional(),
            "deviceKernelVersion": t.string().optional(),
            "systemUpdateInfo": t.proxy(renames["SystemUpdateInfoOut"]).optional(),
            "androidDevicePolicyVersionName": t.string().optional(),
            "securityPatchLevel": t.string().optional(),
            "androidBuildTime": t.string().optional(),
            "androidDevicePolicyVersionCode": t.integer().optional(),
            "deviceBuildSignature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SoftwareInfoOut"])
    types["AdbShellCommandEventIn"] = t.struct(
        {"shellCmd": t.string().optional()}
    ).named(renames["AdbShellCommandEventIn"])
    types["AdbShellCommandEventOut"] = t.struct(
        {
            "shellCmd": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdbShellCommandEventOut"])
    types["RemoteLockEventIn"] = t.struct(
        {
            "adminUserId": t.integer().optional(),
            "adminPackageName": t.string().optional(),
            "targetUserId": t.integer().optional(),
        }
    ).named(renames["RemoteLockEventIn"])
    types["RemoteLockEventOut"] = t.struct(
        {
            "adminUserId": t.integer().optional(),
            "adminPackageName": t.string().optional(),
            "targetUserId": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoteLockEventOut"])
    types["NetworkInfoIn"] = t.struct(
        {
            "meid": t.string().optional(),
            "networkOperatorName": t.string().optional(),
            "imei": t.string().optional(),
            "wifiMacAddress": t.string().optional(),
            "telephonyInfos": t.array(t.proxy(renames["TelephonyInfoIn"])).optional(),
        }
    ).named(renames["NetworkInfoIn"])
    types["NetworkInfoOut"] = t.struct(
        {
            "meid": t.string().optional(),
            "networkOperatorName": t.string().optional(),
            "imei": t.string().optional(),
            "wifiMacAddress": t.string().optional(),
            "telephonyInfos": t.array(t.proxy(renames["TelephonyInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInfoOut"])
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
    types["DeviceIn"] = t.struct(
        {
            "userName": t.string().optional(),
            "lastStatusReportTime": t.string().optional(),
            "enrollmentTokenData": t.string().optional(),
            "memoryEvents": t.array(t.proxy(renames["MemoryEventIn"])).optional(),
            "networkInfo": t.proxy(renames["NetworkInfoIn"]).optional(),
            "managementMode": t.string().optional(),
            "state": t.string().optional(),
            "policyName": t.string().optional(),
            "hardwareStatusSamples": t.array(
                t.proxy(renames["HardwareStatusIn"])
            ).optional(),
            "apiLevel": t.integer().optional(),
            "policyCompliant": t.boolean().optional(),
            "lastPolicyComplianceReportTime": t.string().optional(),
            "nonComplianceDetails": t.array(
                t.proxy(renames["NonComplianceDetailIn"])
            ).optional(),
            "appliedPolicyName": t.string().optional(),
            "commonCriteriaModeInfo": t.proxy(
                renames["CommonCriteriaModeInfoIn"]
            ).optional(),
            "hardwareInfo": t.proxy(renames["HardwareInfoIn"]).optional(),
            "deviceSettings": t.proxy(renames["DeviceSettingsIn"]).optional(),
            "lastPolicySyncTime": t.string().optional(),
            "powerManagementEvents": t.array(
                t.proxy(renames["PowerManagementEventIn"])
            ).optional(),
            "appliedState": t.string().optional(),
            "name": t.string().optional(),
            "applicationReports": t.array(
                t.proxy(renames["ApplicationReportIn"])
            ).optional(),
            "previousDeviceNames": t.array(t.string()).optional(),
            "appliedPolicyVersion": t.string().optional(),
            "disabledReason": t.proxy(renames["UserFacingMessageIn"]).optional(),
            "user": t.proxy(renames["UserIn"]).optional(),
            "enrollmentTokenName": t.string().optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoIn"]).optional(),
            "ownership": t.string().optional(),
            "systemProperties": t.struct({"_": t.string().optional()}).optional(),
            "enrollmentTime": t.string().optional(),
            "softwareInfo": t.proxy(renames["SoftwareInfoIn"]).optional(),
            "displays": t.array(t.proxy(renames["DisplayIn"])).optional(),
            "appliedPasswordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsIn"])
            ).optional(),
            "securityPosture": t.proxy(renames["SecurityPostureIn"]).optional(),
        }
    ).named(renames["DeviceIn"])
    types["DeviceOut"] = t.struct(
        {
            "userName": t.string().optional(),
            "lastStatusReportTime": t.string().optional(),
            "enrollmentTokenData": t.string().optional(),
            "memoryEvents": t.array(t.proxy(renames["MemoryEventOut"])).optional(),
            "networkInfo": t.proxy(renames["NetworkInfoOut"]).optional(),
            "managementMode": t.string().optional(),
            "state": t.string().optional(),
            "policyName": t.string().optional(),
            "hardwareStatusSamples": t.array(
                t.proxy(renames["HardwareStatusOut"])
            ).optional(),
            "apiLevel": t.integer().optional(),
            "policyCompliant": t.boolean().optional(),
            "lastPolicyComplianceReportTime": t.string().optional(),
            "nonComplianceDetails": t.array(
                t.proxy(renames["NonComplianceDetailOut"])
            ).optional(),
            "appliedPolicyName": t.string().optional(),
            "commonCriteriaModeInfo": t.proxy(
                renames["CommonCriteriaModeInfoOut"]
            ).optional(),
            "hardwareInfo": t.proxy(renames["HardwareInfoOut"]).optional(),
            "deviceSettings": t.proxy(renames["DeviceSettingsOut"]).optional(),
            "lastPolicySyncTime": t.string().optional(),
            "powerManagementEvents": t.array(
                t.proxy(renames["PowerManagementEventOut"])
            ).optional(),
            "appliedState": t.string().optional(),
            "name": t.string().optional(),
            "applicationReports": t.array(
                t.proxy(renames["ApplicationReportOut"])
            ).optional(),
            "previousDeviceNames": t.array(t.string()).optional(),
            "appliedPolicyVersion": t.string().optional(),
            "disabledReason": t.proxy(renames["UserFacingMessageOut"]).optional(),
            "user": t.proxy(renames["UserOut"]).optional(),
            "enrollmentTokenName": t.string().optional(),
            "memoryInfo": t.proxy(renames["MemoryInfoOut"]).optional(),
            "ownership": t.string().optional(),
            "systemProperties": t.struct({"_": t.string().optional()}).optional(),
            "enrollmentTime": t.string().optional(),
            "softwareInfo": t.proxy(renames["SoftwareInfoOut"]).optional(),
            "displays": t.array(t.proxy(renames["DisplayOut"])).optional(),
            "appliedPasswordPolicies": t.array(
                t.proxy(renames["PasswordRequirementsOut"])
            ).optional(),
            "securityPosture": t.proxy(renames["SecurityPostureOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceOut"])
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
    types["LaunchAppActionIn"] = t.struct({"packageName": t.string().optional()}).named(
        renames["LaunchAppActionIn"]
    )
    types["LaunchAppActionOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LaunchAppActionOut"])
    types["KioskCustomizationIn"] = t.struct(
        {
            "systemErrorWarnings": t.string().optional(),
            "powerButtonActions": t.string().optional(),
            "deviceSettings": t.string().optional(),
            "statusBar": t.string().optional(),
            "systemNavigation": t.string().optional(),
        }
    ).named(renames["KioskCustomizationIn"])
    types["KioskCustomizationOut"] = t.struct(
        {
            "systemErrorWarnings": t.string().optional(),
            "powerButtonActions": t.string().optional(),
            "deviceSettings": t.string().optional(),
            "statusBar": t.string().optional(),
            "systemNavigation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KioskCustomizationOut"])
    types["KeyguardDismissedEventIn"] = t.struct({"_": t.string().optional()}).named(
        renames["KeyguardDismissedEventIn"]
    )
    types["KeyguardDismissedEventOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["KeyguardDismissedEventOut"])
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
    types["PasswordRequirementsIn"] = t.struct(
        {
            "requirePasswordUnlock": t.string().optional(),
            "passwordMinimumSymbols": t.integer().optional(),
            "passwordQuality": t.string().optional(),
            "passwordMinimumUpperCase": t.integer().optional(),
            "passwordMinimumLowerCase": t.integer().optional(),
            "passwordMinimumNonLetter": t.integer().optional(),
            "passwordScope": t.string().optional(),
            "passwordMinimumLength": t.integer().optional(),
            "passwordMinimumLetters": t.integer().optional(),
            "passwordExpirationTimeout": t.string().optional(),
            "maximumFailedPasswordsForWipe": t.integer().optional(),
            "passwordHistoryLength": t.integer().optional(),
            "passwordMinimumNumeric": t.integer().optional(),
            "unifiedLockSettings": t.string().optional(),
        }
    ).named(renames["PasswordRequirementsIn"])
    types["PasswordRequirementsOut"] = t.struct(
        {
            "requirePasswordUnlock": t.string().optional(),
            "passwordMinimumSymbols": t.integer().optional(),
            "passwordQuality": t.string().optional(),
            "passwordMinimumUpperCase": t.integer().optional(),
            "passwordMinimumLowerCase": t.integer().optional(),
            "passwordMinimumNonLetter": t.integer().optional(),
            "passwordScope": t.string().optional(),
            "passwordMinimumLength": t.integer().optional(),
            "passwordMinimumLetters": t.integer().optional(),
            "passwordExpirationTimeout": t.string().optional(),
            "maximumFailedPasswordsForWipe": t.integer().optional(),
            "passwordHistoryLength": t.integer().optional(),
            "passwordMinimumNumeric": t.integer().optional(),
            "unifiedLockSettings": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordRequirementsOut"])
    types["ConnectEventIn"] = t.struct(
        {
            "destinationIpAddress": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "packageName": t.string().optional(),
        }
    ).named(renames["ConnectEventIn"])
    types["ConnectEventOut"] = t.struct(
        {
            "destinationIpAddress": t.string().optional(),
            "destinationPort": t.integer().optional(),
            "packageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectEventOut"])
    types["UserIn"] = t.struct({"accountIdentifier": t.string().optional()}).named(
        renames["UserIn"]
    )
    types["UserOut"] = t.struct(
        {
            "accountIdentifier": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOut"])
    types["WebAppIconIn"] = t.struct({"imageData": t.string().optional()}).named(
        renames["WebAppIconIn"]
    )
    types["WebAppIconOut"] = t.struct(
        {
            "imageData": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAppIconOut"])
    types["ApplicationReportIn"] = t.struct(
        {
            "versionCode": t.integer().optional(),
            "keyedAppStates": t.array(t.proxy(renames["KeyedAppStateIn"])).optional(),
            "applicationSource": t.string().optional(),
            "state": t.string().optional(),
            "events": t.array(t.proxy(renames["ApplicationEventIn"])).optional(),
            "versionName": t.string().optional(),
            "packageSha256Hash": t.string().optional(),
            "packageName": t.string().optional(),
            "displayName": t.string().optional(),
            "signingKeyCertFingerprints": t.array(t.string()).optional(),
            "installerPackageName": t.string().optional(),
        }
    ).named(renames["ApplicationReportIn"])
    types["ApplicationReportOut"] = t.struct(
        {
            "versionCode": t.integer().optional(),
            "keyedAppStates": t.array(t.proxy(renames["KeyedAppStateOut"])).optional(),
            "applicationSource": t.string().optional(),
            "state": t.string().optional(),
            "events": t.array(t.proxy(renames["ApplicationEventOut"])).optional(),
            "versionName": t.string().optional(),
            "packageSha256Hash": t.string().optional(),
            "packageName": t.string().optional(),
            "displayName": t.string().optional(),
            "signingKeyCertFingerprints": t.array(t.string()).optional(),
            "installerPackageName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReportOut"])
    types["ApplicationPolicyIn"] = t.struct(
        {
            "managedConfigurationTemplate": t.proxy(
                renames["ManagedConfigurationTemplateIn"]
            ).optional(),
            "installType": t.string().optional(),
            "packageName": t.string().optional(),
            "lockTaskAllowed": t.boolean().optional(),
            "delegatedScopes": t.array(t.string()).optional(),
            "autoUpdateMode": t.string().optional(),
            "accessibleTrackIds": t.array(t.string()).optional(),
            "connectedWorkAndPersonalApp": t.string().optional(),
            "workProfileWidgets": t.string().optional(),
            "minimumVersionCode": t.integer().optional(),
            "managedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantIn"])
            ).optional(),
            "alwaysOnVpnLockdownExemption": t.string().optional(),
            "disabled": t.boolean().optional(),
            "extensionConfig": t.proxy(renames["ExtensionConfigIn"]).optional(),
            "defaultPermissionPolicy": t.string().optional(),
        }
    ).named(renames["ApplicationPolicyIn"])
    types["ApplicationPolicyOut"] = t.struct(
        {
            "managedConfigurationTemplate": t.proxy(
                renames["ManagedConfigurationTemplateOut"]
            ).optional(),
            "installType": t.string().optional(),
            "packageName": t.string().optional(),
            "lockTaskAllowed": t.boolean().optional(),
            "delegatedScopes": t.array(t.string()).optional(),
            "autoUpdateMode": t.string().optional(),
            "accessibleTrackIds": t.array(t.string()).optional(),
            "connectedWorkAndPersonalApp": t.string().optional(),
            "workProfileWidgets": t.string().optional(),
            "minimumVersionCode": t.integer().optional(),
            "managedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "permissionGrants": t.array(
                t.proxy(renames["PermissionGrantOut"])
            ).optional(),
            "alwaysOnVpnLockdownExemption": t.string().optional(),
            "disabled": t.boolean().optional(),
            "extensionConfig": t.proxy(renames["ExtensionConfigOut"]).optional(),
            "defaultPermissionPolicy": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationPolicyOut"])
    types["UserFacingMessageIn"] = t.struct(
        {
            "localizedMessages": t.struct({"_": t.string().optional()}).optional(),
            "defaultMessage": t.string().optional(),
        }
    ).named(renames["UserFacingMessageIn"])
    types["UserFacingMessageOut"] = t.struct(
        {
            "localizedMessages": t.struct({"_": t.string().optional()}).optional(),
            "defaultMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserFacingMessageOut"])
    types["ClearAppsDataParamsIn"] = t.struct(
        {"packageNames": t.array(t.string()).optional()}
    ).named(renames["ClearAppsDataParamsIn"])
    types["ClearAppsDataParamsOut"] = t.struct(
        {
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClearAppsDataParamsOut"])
    types["ApiLevelConditionIn"] = t.struct(
        {"minApiLevel": t.integer().optional()}
    ).named(renames["ApiLevelConditionIn"])
    types["ApiLevelConditionOut"] = t.struct(
        {
            "minApiLevel": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiLevelConditionOut"])
    types["PersonalUsagePoliciesIn"] = t.struct(
        {
            "maxDaysWithWorkOff": t.integer().optional(),
            "personalApplications": t.array(
                t.proxy(renames["PersonalApplicationPolicyIn"])
            ).optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "cameraDisabled": t.boolean().optional(),
            "personalPlayStoreMode": t.string().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
        }
    ).named(renames["PersonalUsagePoliciesIn"])
    types["PersonalUsagePoliciesOut"] = t.struct(
        {
            "maxDaysWithWorkOff": t.integer().optional(),
            "personalApplications": t.array(
                t.proxy(renames["PersonalApplicationPolicyOut"])
            ).optional(),
            "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
            "cameraDisabled": t.boolean().optional(),
            "personalPlayStoreMode": t.string().optional(),
            "screenCaptureDisabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PersonalUsagePoliciesOut"])
    types["ChoosePrivateKeyRuleIn"] = t.struct(
        {
            "privateKeyAlias": t.string().optional(),
            "urlPattern": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
        }
    ).named(renames["ChoosePrivateKeyRuleIn"])
    types["ChoosePrivateKeyRuleOut"] = t.struct(
        {
            "privateKeyAlias": t.string().optional(),
            "urlPattern": t.string().optional(),
            "packageNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChoosePrivateKeyRuleOut"])
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
    types["DisplayIn"] = t.struct(
        {
            "density": t.integer().optional(),
            "state": t.string().optional(),
            "width": t.integer().optional(),
            "refreshRate": t.integer().optional(),
            "displayId": t.integer().optional(),
            "name": t.string().optional(),
            "height": t.integer().optional(),
        }
    ).named(renames["DisplayIn"])
    types["DisplayOut"] = t.struct(
        {
            "density": t.integer().optional(),
            "state": t.string().optional(),
            "width": t.integer().optional(),
            "refreshRate": t.integer().optional(),
            "displayId": t.integer().optional(),
            "name": t.string().optional(),
            "height": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisplayOut"])
    types["KeyedAppStateIn"] = t.struct(
        {
            "lastUpdateTime": t.string().optional(),
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "key": t.string().optional(),
            "createTime": t.string().optional(),
            "data": t.string().optional(),
        }
    ).named(renames["KeyedAppStateIn"])
    types["KeyedAppStateOut"] = t.struct(
        {
            "lastUpdateTime": t.string().optional(),
            "severity": t.string().optional(),
            "message": t.string().optional(),
            "key": t.string().optional(),
            "createTime": t.string().optional(),
            "data": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyedAppStateOut"])
    types["PolicyEnforcementRuleIn"] = t.struct(
        {
            "wipeAction": t.proxy(renames["WipeActionIn"]).optional(),
            "settingName": t.string().optional(),
            "blockAction": t.proxy(renames["BlockActionIn"]).optional(),
        }
    ).named(renames["PolicyEnforcementRuleIn"])
    types["PolicyEnforcementRuleOut"] = t.struct(
        {
            "wipeAction": t.proxy(renames["WipeActionOut"]).optional(),
            "settingName": t.string().optional(),
            "blockAction": t.proxy(renames["BlockActionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyEnforcementRuleOut"])
    types["ApplicationIn"] = t.struct(
        {
            "managedProperties": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
            "title": t.string().optional(),
            "appPricing": t.string().optional(),
            "permissions": t.array(
                t.proxy(renames["ApplicationPermissionIn"])
            ).optional(),
            "appVersions": t.array(t.proxy(renames["AppVersionIn"])).optional(),
            "recentChanges": t.string().optional(),
            "iconUrl": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "distributionChannel": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "features": t.array(t.string()).optional(),
            "smallIconUrl": t.string().optional(),
            "description": t.string().optional(),
            "playStoreUrl": t.string().optional(),
            "appTracks": t.array(t.proxy(renames["AppTrackInfoIn"])).optional(),
            "fullDescription": t.string().optional(),
            "name": t.string().optional(),
            "category": t.string().optional(),
            "author": t.string().optional(),
            "availableCountries": t.array(t.string()).optional(),
            "contentRating": t.string().optional(),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "managedProperties": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "title": t.string().optional(),
            "appPricing": t.string().optional(),
            "permissions": t.array(
                t.proxy(renames["ApplicationPermissionOut"])
            ).optional(),
            "appVersions": t.array(t.proxy(renames["AppVersionOut"])).optional(),
            "recentChanges": t.string().optional(),
            "iconUrl": t.string().optional(),
            "screenshotUrls": t.array(t.string()).optional(),
            "distributionChannel": t.string().optional(),
            "minAndroidSdkVersion": t.integer().optional(),
            "features": t.array(t.string()).optional(),
            "smallIconUrl": t.string().optional(),
            "description": t.string().optional(),
            "playStoreUrl": t.string().optional(),
            "appTracks": t.array(t.proxy(renames["AppTrackInfoOut"])).optional(),
            "fullDescription": t.string().optional(),
            "name": t.string().optional(),
            "category": t.string().optional(),
            "author": t.string().optional(),
            "availableCountries": t.array(t.string()).optional(),
            "contentRating": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
    types["WebTokenIn"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "parentFrameUrl": t.string().optional(),
            "enabledFeatures": t.array(t.string()).optional(),
        }
    ).named(renames["WebTokenIn"])
    types["WebTokenOut"] = t.struct(
        {
            "value": t.string().optional(),
            "name": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "parentFrameUrl": t.string().optional(),
            "enabledFeatures": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebTokenOut"])
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
    types["SignupUrlIn"] = t.struct(
        {"name": t.string().optional(), "url": t.string().optional()}
    ).named(renames["SignupUrlIn"])
    types["SignupUrlOut"] = t.struct(
        {
            "name": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignupUrlOut"])
    types["ProxyInfoIn"] = t.struct(
        {
            "pacUri": t.string().optional(),
            "excludedHosts": t.array(t.string()).optional(),
            "port": t.integer().optional(),
            "host": t.string().optional(),
        }
    ).named(renames["ProxyInfoIn"])
    types["ProxyInfoOut"] = t.struct(
        {
            "pacUri": t.string().optional(),
            "excludedHosts": t.array(t.string()).optional(),
            "port": t.integer().optional(),
            "host": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProxyInfoOut"])
    types["ContactInfoIn"] = t.struct(
        {
            "euRepresentativeName": t.string().optional(),
            "dataProtectionOfficerEmail": t.string().optional(),
            "dataProtectionOfficerPhone": t.string().optional(),
            "dataProtectionOfficerName": t.string().optional(),
            "euRepresentativePhone": t.string().optional(),
            "euRepresentativeEmail": t.string().optional(),
            "contactEmail": t.string().optional(),
        }
    ).named(renames["ContactInfoIn"])
    types["ContactInfoOut"] = t.struct(
        {
            "euRepresentativeName": t.string().optional(),
            "dataProtectionOfficerEmail": t.string().optional(),
            "dataProtectionOfficerPhone": t.string().optional(),
            "dataProtectionOfficerName": t.string().optional(),
            "euRepresentativePhone": t.string().optional(),
            "euRepresentativeEmail": t.string().optional(),
            "contactEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactInfoOut"])
    types["ApplicationReportingSettingsIn"] = t.struct(
        {"includeRemovedApps": t.boolean().optional()}
    ).named(renames["ApplicationReportingSettingsIn"])
    types["ApplicationReportingSettingsOut"] = t.struct(
        {
            "includeRemovedApps": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationReportingSettingsOut"])
    types["EnterpriseIn"] = t.struct(
        {
            "termsAndConditions": t.array(
                t.proxy(renames["TermsAndConditionsIn"])
            ).optional(),
            "enterpriseDisplayName": t.string().optional(),
            "signinDetails": t.array(t.proxy(renames["SigninDetailIn"])).optional(),
            "logo": t.proxy(renames["ExternalDataIn"]).optional(),
            "primaryColor": t.integer().optional(),
            "pubsubTopic": t.string().optional(),
            "name": t.string().optional(),
            "appAutoApprovalEnabled": t.boolean().optional(),
            "enabledNotificationTypes": t.array(t.string()).optional(),
            "contactInfo": t.proxy(renames["ContactInfoIn"]).optional(),
        }
    ).named(renames["EnterpriseIn"])
    types["EnterpriseOut"] = t.struct(
        {
            "termsAndConditions": t.array(
                t.proxy(renames["TermsAndConditionsOut"])
            ).optional(),
            "enterpriseDisplayName": t.string().optional(),
            "signinDetails": t.array(t.proxy(renames["SigninDetailOut"])).optional(),
            "logo": t.proxy(renames["ExternalDataOut"]).optional(),
            "primaryColor": t.integer().optional(),
            "pubsubTopic": t.string().optional(),
            "name": t.string().optional(),
            "appAutoApprovalEnabled": t.boolean().optional(),
            "enabledNotificationTypes": t.array(t.string()).optional(),
            "contactInfo": t.proxy(renames["ContactInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnterpriseOut"])
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
    types["PowerManagementEventIn"] = t.struct(
        {
            "batteryLevel": t.number().optional(),
            "eventType": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["PowerManagementEventIn"])
    types["PowerManagementEventOut"] = t.struct(
        {
            "batteryLevel": t.number().optional(),
            "eventType": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PowerManagementEventOut"])
    types["PasswordPoliciesContextIn"] = t.struct(
        {"passwordPolicyScope": t.string().optional()}
    ).named(renames["PasswordPoliciesContextIn"])
    types["PasswordPoliciesContextOut"] = t.struct(
        {
            "passwordPolicyScope": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PasswordPoliciesContextOut"])
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
    types["CommonCriteriaModeInfoIn"] = t.struct(
        {"commonCriteriaModeStatus": t.string().optional()}
    ).named(renames["CommonCriteriaModeInfoIn"])
    types["CommonCriteriaModeInfoOut"] = t.struct(
        {
            "commonCriteriaModeStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonCriteriaModeInfoOut"])
    types["ManagedPropertyIn"] = t.struct(
        {
            "description": t.string().optional(),
            "key": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nestedProperties": t.array(
                t.proxy(renames["ManagedPropertyIn"])
            ).optional(),
            "type": t.string().optional(),
            "entries": t.array(t.proxy(renames["ManagedPropertyEntryIn"])).optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ManagedPropertyIn"])
    types["ManagedPropertyOut"] = t.struct(
        {
            "description": t.string().optional(),
            "key": t.string().optional(),
            "defaultValue": t.struct({"_": t.string().optional()}).optional(),
            "nestedProperties": t.array(
                t.proxy(renames["ManagedPropertyOut"])
            ).optional(),
            "type": t.string().optional(),
            "entries": t.array(t.proxy(renames["ManagedPropertyEntryOut"])).optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedPropertyOut"])
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
    types["AppVersionIn"] = t.struct(
        {
            "production": t.boolean().optional(),
            "versionCode": t.integer().optional(),
            "trackIds": t.array(t.string()).optional(),
            "versionString": t.string().optional(),
        }
    ).named(renames["AppVersionIn"])
    types["AppVersionOut"] = t.struct(
        {
            "production": t.boolean().optional(),
            "versionCode": t.integer().optional(),
            "trackIds": t.array(t.string()).optional(),
            "versionString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppVersionOut"])
    types["NonComplianceDetailIn"] = t.struct(
        {
            "specificNonComplianceContext": t.proxy(
                renames["SpecificNonComplianceContextIn"]
            ).optional(),
            "fieldPath": t.string().optional(),
            "currentValue": t.struct({"_": t.string().optional()}).optional(),
            "settingName": t.string().optional(),
            "packageName": t.string().optional(),
            "installationFailureReason": t.string().optional(),
            "specificNonComplianceReason": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
        }
    ).named(renames["NonComplianceDetailIn"])
    types["NonComplianceDetailOut"] = t.struct(
        {
            "specificNonComplianceContext": t.proxy(
                renames["SpecificNonComplianceContextOut"]
            ).optional(),
            "fieldPath": t.string().optional(),
            "currentValue": t.struct({"_": t.string().optional()}).optional(),
            "settingName": t.string().optional(),
            "packageName": t.string().optional(),
            "installationFailureReason": t.string().optional(),
            "specificNonComplianceReason": t.string().optional(),
            "nonComplianceReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NonComplianceDetailOut"])
    types["KeyDestructionEventIn"] = t.struct(
        {
            "success": t.boolean().optional(),
            "applicationUid": t.integer().optional(),
            "keyAlias": t.string().optional(),
        }
    ).named(renames["KeyDestructionEventIn"])
    types["KeyDestructionEventOut"] = t.struct(
        {
            "success": t.boolean().optional(),
            "applicationUid": t.integer().optional(),
            "keyAlias": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["KeyDestructionEventOut"])
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

    functions = {}
    functions["enterprisesList"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesCreate"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesGet"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPatch"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDelete"] = androidmanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsCreate"] = androidmanagement.get(
        "v1/{parent}/webApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsGet"] = androidmanagement.get(
        "v1/{parent}/webApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsDelete"] = androidmanagement.get(
        "v1/{parent}/webApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsPatch"] = androidmanagement.get(
        "v1/{parent}/webApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesWebAppsList"] = androidmanagement.get(
        "v1/{parent}/webApps",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListWebAppsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesPatch"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesList"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesIssueCommand"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesDelete"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesGet"] = androidmanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["DeviceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsGet"] = androidmanagement.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsCancel"] = androidmanagement.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsDelete"] = androidmanagement.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesDevicesOperationsList"] = androidmanagement.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["enterprisesPoliciesList"] = androidmanagement.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "frpAdminEmails": t.array(t.string()).optional(),
                "safeBootDisabled": t.boolean().optional(),
                "mountPhysicalMediaDisabled": t.boolean().optional(),
                "cameraDisabled": t.boolean().optional(),
                "appAutoUpdatePolicy": t.string().optional(),
                "permittedAccessibilityServices": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "bluetoothContactSharingDisabled": t.boolean().optional(),
                "unmuteMicrophoneDisabled": t.boolean().optional(),
                "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
                "alwaysOnVpnPackage": t.proxy(
                    renames["AlwaysOnVpnPackageIn"]
                ).optional(),
                "installUnknownSourcesAllowed": t.boolean().optional(),
                "bluetoothConfigDisabled": t.boolean().optional(),
                "advancedSecurityOverrides": t.proxy(
                    renames["AdvancedSecurityOverridesIn"]
                ).optional(),
                "addUserDisabled": t.boolean().optional(),
                "personalUsagePolicies": t.proxy(
                    renames["PersonalUsagePoliciesIn"]
                ).optional(),
                "applications": t.array(
                    t.proxy(renames["ApplicationPolicyIn"])
                ).optional(),
                "removeUserDisabled": t.boolean().optional(),
                "microphoneAccess": t.string().optional(),
                "complianceRules": t.array(
                    t.proxy(renames["ComplianceRuleIn"])
                ).optional(),
                "createWindowsDisabled": t.boolean().optional(),
                "shortSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "policyEnforcementRules": t.array(
                    t.proxy(renames["PolicyEnforcementRuleIn"])
                ).optional(),
                "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
                "networkEscapeHatchEnabled": t.boolean().optional(),
                "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
                "kioskCustomLauncherEnabled": t.boolean().optional(),
                "outgoingBeamDisabled": t.boolean().optional(),
                "permittedInputMethods": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "deviceOwnerLockScreenInfo": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "wifiConfigsLockdownEnabled": t.boolean().optional(),
                "wifiConfigDisabled": t.boolean().optional(),
                "bluetoothDisabled": t.boolean().optional(),
                "tetheringConfigDisabled": t.boolean().optional(),
                "adjustVolumeDisabled": t.boolean().optional(),
                "outgoingCallsDisabled": t.boolean().optional(),
                "ensureVerifyAppsEnabled": t.boolean().optional(),
                "choosePrivateKeyRules": t.array(
                    t.proxy(renames["ChoosePrivateKeyRuleIn"])
                ).optional(),
                "keyguardDisabled": t.boolean().optional(),
                "passwordRequirements": t.proxy(
                    renames["PasswordRequirementsIn"]
                ).optional(),
                "setWallpaperDisabled": t.boolean().optional(),
                "cellBroadcastsConfigDisabled": t.boolean().optional(),
                "uninstallAppsDisabled": t.boolean().optional(),
                "minimumApiLevel": t.integer().optional(),
                "statusReportingSettings": t.proxy(
                    renames["StatusReportingSettingsIn"]
                ).optional(),
                "maximumTimeToLock": t.string().optional(),
                "stayOnPluggedModes": t.array(t.string()).optional(),
                "crossProfilePolicies": t.proxy(
                    renames["CrossProfilePoliciesIn"]
                ).optional(),
                "version": t.string().optional(),
                "privateKeySelectionEnabled": t.boolean().optional(),
                "screenCaptureDisabled": t.boolean().optional(),
                "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
                "permissionGrants": t.array(
                    t.proxy(renames["PermissionGrantIn"])
                ).optional(),
                "skipFirstUseHintsEnabled": t.boolean().optional(),
                "factoryResetDisabled": t.boolean().optional(),
                "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
                "longSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "preferentialNetworkService": t.string().optional(),
                "openNetworkConfiguration": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "modifyAccountsDisabled": t.boolean().optional(),
                "encryptionPolicy": t.string().optional(),
                "statusBarDisabled": t.boolean().optional(),
                "playStoreMode": t.string().optional(),
                "installAppsDisabled": t.boolean().optional(),
                "cameraAccess": t.string().optional(),
                "shareLocationDisabled": t.boolean().optional(),
                "networkResetDisabled": t.boolean().optional(),
                "usbMassStorageEnabled": t.boolean().optional(),
                "defaultPermissionPolicy": t.string().optional(),
                "blockApplicationsEnabled": t.boolean().optional(),
                "autoDateAndTimeZone": t.string().optional(),
                "kioskCustomization": t.proxy(
                    renames["KioskCustomizationIn"]
                ).optional(),
                "debuggingFeaturesAllowed": t.boolean().optional(),
                "setUserIconDisabled": t.boolean().optional(),
                "dataRoamingDisabled": t.boolean().optional(),
                "smsDisabled": t.boolean().optional(),
                "androidDevicePolicyTracks": t.array(t.string()).optional(),
                "mobileNetworksConfigDisabled": t.boolean().optional(),
                "locationMode": t.string().optional(),
                "oncCertificateProviders": t.array(
                    t.proxy(renames["OncCertificateProviderIn"])
                ).optional(),
                "usbFileTransferDisabled": t.boolean().optional(),
                "passwordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "credentialsConfigDisabled": t.boolean().optional(),
                "persistentPreferredActivities": t.array(
                    t.proxy(renames["PersistentPreferredActivityIn"])
                ).optional(),
                "vpnConfigDisabled": t.boolean().optional(),
                "autoTimeRequired": t.boolean().optional(),
                "keyguardDisabledFeatures": t.array(t.string()).optional(),
                "funDisabled": t.boolean().optional(),
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
                "frpAdminEmails": t.array(t.string()).optional(),
                "safeBootDisabled": t.boolean().optional(),
                "mountPhysicalMediaDisabled": t.boolean().optional(),
                "cameraDisabled": t.boolean().optional(),
                "appAutoUpdatePolicy": t.string().optional(),
                "permittedAccessibilityServices": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "bluetoothContactSharingDisabled": t.boolean().optional(),
                "unmuteMicrophoneDisabled": t.boolean().optional(),
                "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
                "alwaysOnVpnPackage": t.proxy(
                    renames["AlwaysOnVpnPackageIn"]
                ).optional(),
                "installUnknownSourcesAllowed": t.boolean().optional(),
                "bluetoothConfigDisabled": t.boolean().optional(),
                "advancedSecurityOverrides": t.proxy(
                    renames["AdvancedSecurityOverridesIn"]
                ).optional(),
                "addUserDisabled": t.boolean().optional(),
                "personalUsagePolicies": t.proxy(
                    renames["PersonalUsagePoliciesIn"]
                ).optional(),
                "applications": t.array(
                    t.proxy(renames["ApplicationPolicyIn"])
                ).optional(),
                "removeUserDisabled": t.boolean().optional(),
                "microphoneAccess": t.string().optional(),
                "complianceRules": t.array(
                    t.proxy(renames["ComplianceRuleIn"])
                ).optional(),
                "createWindowsDisabled": t.boolean().optional(),
                "shortSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "policyEnforcementRules": t.array(
                    t.proxy(renames["PolicyEnforcementRuleIn"])
                ).optional(),
                "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
                "networkEscapeHatchEnabled": t.boolean().optional(),
                "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
                "kioskCustomLauncherEnabled": t.boolean().optional(),
                "outgoingBeamDisabled": t.boolean().optional(),
                "permittedInputMethods": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "deviceOwnerLockScreenInfo": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "wifiConfigsLockdownEnabled": t.boolean().optional(),
                "wifiConfigDisabled": t.boolean().optional(),
                "bluetoothDisabled": t.boolean().optional(),
                "tetheringConfigDisabled": t.boolean().optional(),
                "adjustVolumeDisabled": t.boolean().optional(),
                "outgoingCallsDisabled": t.boolean().optional(),
                "ensureVerifyAppsEnabled": t.boolean().optional(),
                "choosePrivateKeyRules": t.array(
                    t.proxy(renames["ChoosePrivateKeyRuleIn"])
                ).optional(),
                "keyguardDisabled": t.boolean().optional(),
                "passwordRequirements": t.proxy(
                    renames["PasswordRequirementsIn"]
                ).optional(),
                "setWallpaperDisabled": t.boolean().optional(),
                "cellBroadcastsConfigDisabled": t.boolean().optional(),
                "uninstallAppsDisabled": t.boolean().optional(),
                "minimumApiLevel": t.integer().optional(),
                "statusReportingSettings": t.proxy(
                    renames["StatusReportingSettingsIn"]
                ).optional(),
                "maximumTimeToLock": t.string().optional(),
                "stayOnPluggedModes": t.array(t.string()).optional(),
                "crossProfilePolicies": t.proxy(
                    renames["CrossProfilePoliciesIn"]
                ).optional(),
                "version": t.string().optional(),
                "privateKeySelectionEnabled": t.boolean().optional(),
                "screenCaptureDisabled": t.boolean().optional(),
                "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
                "permissionGrants": t.array(
                    t.proxy(renames["PermissionGrantIn"])
                ).optional(),
                "skipFirstUseHintsEnabled": t.boolean().optional(),
                "factoryResetDisabled": t.boolean().optional(),
                "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
                "longSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "preferentialNetworkService": t.string().optional(),
                "openNetworkConfiguration": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "modifyAccountsDisabled": t.boolean().optional(),
                "encryptionPolicy": t.string().optional(),
                "statusBarDisabled": t.boolean().optional(),
                "playStoreMode": t.string().optional(),
                "installAppsDisabled": t.boolean().optional(),
                "cameraAccess": t.string().optional(),
                "shareLocationDisabled": t.boolean().optional(),
                "networkResetDisabled": t.boolean().optional(),
                "usbMassStorageEnabled": t.boolean().optional(),
                "defaultPermissionPolicy": t.string().optional(),
                "blockApplicationsEnabled": t.boolean().optional(),
                "autoDateAndTimeZone": t.string().optional(),
                "kioskCustomization": t.proxy(
                    renames["KioskCustomizationIn"]
                ).optional(),
                "debuggingFeaturesAllowed": t.boolean().optional(),
                "setUserIconDisabled": t.boolean().optional(),
                "dataRoamingDisabled": t.boolean().optional(),
                "smsDisabled": t.boolean().optional(),
                "androidDevicePolicyTracks": t.array(t.string()).optional(),
                "mobileNetworksConfigDisabled": t.boolean().optional(),
                "locationMode": t.string().optional(),
                "oncCertificateProviders": t.array(
                    t.proxy(renames["OncCertificateProviderIn"])
                ).optional(),
                "usbFileTransferDisabled": t.boolean().optional(),
                "passwordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "credentialsConfigDisabled": t.boolean().optional(),
                "persistentPreferredActivities": t.array(
                    t.proxy(renames["PersistentPreferredActivityIn"])
                ).optional(),
                "vpnConfigDisabled": t.boolean().optional(),
                "autoTimeRequired": t.boolean().optional(),
                "keyguardDisabledFeatures": t.array(t.string()).optional(),
                "funDisabled": t.boolean().optional(),
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
                "frpAdminEmails": t.array(t.string()).optional(),
                "safeBootDisabled": t.boolean().optional(),
                "mountPhysicalMediaDisabled": t.boolean().optional(),
                "cameraDisabled": t.boolean().optional(),
                "appAutoUpdatePolicy": t.string().optional(),
                "permittedAccessibilityServices": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "bluetoothContactSharingDisabled": t.boolean().optional(),
                "unmuteMicrophoneDisabled": t.boolean().optional(),
                "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
                "alwaysOnVpnPackage": t.proxy(
                    renames["AlwaysOnVpnPackageIn"]
                ).optional(),
                "installUnknownSourcesAllowed": t.boolean().optional(),
                "bluetoothConfigDisabled": t.boolean().optional(),
                "advancedSecurityOverrides": t.proxy(
                    renames["AdvancedSecurityOverridesIn"]
                ).optional(),
                "addUserDisabled": t.boolean().optional(),
                "personalUsagePolicies": t.proxy(
                    renames["PersonalUsagePoliciesIn"]
                ).optional(),
                "applications": t.array(
                    t.proxy(renames["ApplicationPolicyIn"])
                ).optional(),
                "removeUserDisabled": t.boolean().optional(),
                "microphoneAccess": t.string().optional(),
                "complianceRules": t.array(
                    t.proxy(renames["ComplianceRuleIn"])
                ).optional(),
                "createWindowsDisabled": t.boolean().optional(),
                "shortSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "policyEnforcementRules": t.array(
                    t.proxy(renames["PolicyEnforcementRuleIn"])
                ).optional(),
                "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
                "networkEscapeHatchEnabled": t.boolean().optional(),
                "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
                "kioskCustomLauncherEnabled": t.boolean().optional(),
                "outgoingBeamDisabled": t.boolean().optional(),
                "permittedInputMethods": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "deviceOwnerLockScreenInfo": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "wifiConfigsLockdownEnabled": t.boolean().optional(),
                "wifiConfigDisabled": t.boolean().optional(),
                "bluetoothDisabled": t.boolean().optional(),
                "tetheringConfigDisabled": t.boolean().optional(),
                "adjustVolumeDisabled": t.boolean().optional(),
                "outgoingCallsDisabled": t.boolean().optional(),
                "ensureVerifyAppsEnabled": t.boolean().optional(),
                "choosePrivateKeyRules": t.array(
                    t.proxy(renames["ChoosePrivateKeyRuleIn"])
                ).optional(),
                "keyguardDisabled": t.boolean().optional(),
                "passwordRequirements": t.proxy(
                    renames["PasswordRequirementsIn"]
                ).optional(),
                "setWallpaperDisabled": t.boolean().optional(),
                "cellBroadcastsConfigDisabled": t.boolean().optional(),
                "uninstallAppsDisabled": t.boolean().optional(),
                "minimumApiLevel": t.integer().optional(),
                "statusReportingSettings": t.proxy(
                    renames["StatusReportingSettingsIn"]
                ).optional(),
                "maximumTimeToLock": t.string().optional(),
                "stayOnPluggedModes": t.array(t.string()).optional(),
                "crossProfilePolicies": t.proxy(
                    renames["CrossProfilePoliciesIn"]
                ).optional(),
                "version": t.string().optional(),
                "privateKeySelectionEnabled": t.boolean().optional(),
                "screenCaptureDisabled": t.boolean().optional(),
                "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
                "permissionGrants": t.array(
                    t.proxy(renames["PermissionGrantIn"])
                ).optional(),
                "skipFirstUseHintsEnabled": t.boolean().optional(),
                "factoryResetDisabled": t.boolean().optional(),
                "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
                "longSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "preferentialNetworkService": t.string().optional(),
                "openNetworkConfiguration": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "modifyAccountsDisabled": t.boolean().optional(),
                "encryptionPolicy": t.string().optional(),
                "statusBarDisabled": t.boolean().optional(),
                "playStoreMode": t.string().optional(),
                "installAppsDisabled": t.boolean().optional(),
                "cameraAccess": t.string().optional(),
                "shareLocationDisabled": t.boolean().optional(),
                "networkResetDisabled": t.boolean().optional(),
                "usbMassStorageEnabled": t.boolean().optional(),
                "defaultPermissionPolicy": t.string().optional(),
                "blockApplicationsEnabled": t.boolean().optional(),
                "autoDateAndTimeZone": t.string().optional(),
                "kioskCustomization": t.proxy(
                    renames["KioskCustomizationIn"]
                ).optional(),
                "debuggingFeaturesAllowed": t.boolean().optional(),
                "setUserIconDisabled": t.boolean().optional(),
                "dataRoamingDisabled": t.boolean().optional(),
                "smsDisabled": t.boolean().optional(),
                "androidDevicePolicyTracks": t.array(t.string()).optional(),
                "mobileNetworksConfigDisabled": t.boolean().optional(),
                "locationMode": t.string().optional(),
                "oncCertificateProviders": t.array(
                    t.proxy(renames["OncCertificateProviderIn"])
                ).optional(),
                "usbFileTransferDisabled": t.boolean().optional(),
                "passwordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "credentialsConfigDisabled": t.boolean().optional(),
                "persistentPreferredActivities": t.array(
                    t.proxy(renames["PersistentPreferredActivityIn"])
                ).optional(),
                "vpnConfigDisabled": t.boolean().optional(),
                "autoTimeRequired": t.boolean().optional(),
                "keyguardDisabledFeatures": t.array(t.string()).optional(),
                "funDisabled": t.boolean().optional(),
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
                "frpAdminEmails": t.array(t.string()).optional(),
                "safeBootDisabled": t.boolean().optional(),
                "mountPhysicalMediaDisabled": t.boolean().optional(),
                "cameraDisabled": t.boolean().optional(),
                "appAutoUpdatePolicy": t.string().optional(),
                "permittedAccessibilityServices": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "bluetoothContactSharingDisabled": t.boolean().optional(),
                "unmuteMicrophoneDisabled": t.boolean().optional(),
                "systemUpdate": t.proxy(renames["SystemUpdateIn"]).optional(),
                "alwaysOnVpnPackage": t.proxy(
                    renames["AlwaysOnVpnPackageIn"]
                ).optional(),
                "installUnknownSourcesAllowed": t.boolean().optional(),
                "bluetoothConfigDisabled": t.boolean().optional(),
                "advancedSecurityOverrides": t.proxy(
                    renames["AdvancedSecurityOverridesIn"]
                ).optional(),
                "addUserDisabled": t.boolean().optional(),
                "personalUsagePolicies": t.proxy(
                    renames["PersonalUsagePoliciesIn"]
                ).optional(),
                "applications": t.array(
                    t.proxy(renames["ApplicationPolicyIn"])
                ).optional(),
                "removeUserDisabled": t.boolean().optional(),
                "microphoneAccess": t.string().optional(),
                "complianceRules": t.array(
                    t.proxy(renames["ComplianceRuleIn"])
                ).optional(),
                "createWindowsDisabled": t.boolean().optional(),
                "shortSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "policyEnforcementRules": t.array(
                    t.proxy(renames["PolicyEnforcementRuleIn"])
                ).optional(),
                "recommendedGlobalProxy": t.proxy(renames["ProxyInfoIn"]).optional(),
                "networkEscapeHatchEnabled": t.boolean().optional(),
                "accountTypesWithManagementDisabled": t.array(t.string()).optional(),
                "kioskCustomLauncherEnabled": t.boolean().optional(),
                "outgoingBeamDisabled": t.boolean().optional(),
                "permittedInputMethods": t.proxy(
                    renames["PackageNameListIn"]
                ).optional(),
                "deviceOwnerLockScreenInfo": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "wifiConfigsLockdownEnabled": t.boolean().optional(),
                "wifiConfigDisabled": t.boolean().optional(),
                "bluetoothDisabled": t.boolean().optional(),
                "tetheringConfigDisabled": t.boolean().optional(),
                "adjustVolumeDisabled": t.boolean().optional(),
                "outgoingCallsDisabled": t.boolean().optional(),
                "ensureVerifyAppsEnabled": t.boolean().optional(),
                "choosePrivateKeyRules": t.array(
                    t.proxy(renames["ChoosePrivateKeyRuleIn"])
                ).optional(),
                "keyguardDisabled": t.boolean().optional(),
                "passwordRequirements": t.proxy(
                    renames["PasswordRequirementsIn"]
                ).optional(),
                "setWallpaperDisabled": t.boolean().optional(),
                "cellBroadcastsConfigDisabled": t.boolean().optional(),
                "uninstallAppsDisabled": t.boolean().optional(),
                "minimumApiLevel": t.integer().optional(),
                "statusReportingSettings": t.proxy(
                    renames["StatusReportingSettingsIn"]
                ).optional(),
                "maximumTimeToLock": t.string().optional(),
                "stayOnPluggedModes": t.array(t.string()).optional(),
                "crossProfilePolicies": t.proxy(
                    renames["CrossProfilePoliciesIn"]
                ).optional(),
                "version": t.string().optional(),
                "privateKeySelectionEnabled": t.boolean().optional(),
                "screenCaptureDisabled": t.boolean().optional(),
                "usageLog": t.proxy(renames["UsageLogIn"]).optional(),
                "permissionGrants": t.array(
                    t.proxy(renames["PermissionGrantIn"])
                ).optional(),
                "skipFirstUseHintsEnabled": t.boolean().optional(),
                "factoryResetDisabled": t.boolean().optional(),
                "setupActions": t.array(t.proxy(renames["SetupActionIn"])).optional(),
                "longSupportMessage": t.proxy(
                    renames["UserFacingMessageIn"]
                ).optional(),
                "preferentialNetworkService": t.string().optional(),
                "openNetworkConfiguration": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "modifyAccountsDisabled": t.boolean().optional(),
                "encryptionPolicy": t.string().optional(),
                "statusBarDisabled": t.boolean().optional(),
                "playStoreMode": t.string().optional(),
                "installAppsDisabled": t.boolean().optional(),
                "cameraAccess": t.string().optional(),
                "shareLocationDisabled": t.boolean().optional(),
                "networkResetDisabled": t.boolean().optional(),
                "usbMassStorageEnabled": t.boolean().optional(),
                "defaultPermissionPolicy": t.string().optional(),
                "blockApplicationsEnabled": t.boolean().optional(),
                "autoDateAndTimeZone": t.string().optional(),
                "kioskCustomization": t.proxy(
                    renames["KioskCustomizationIn"]
                ).optional(),
                "debuggingFeaturesAllowed": t.boolean().optional(),
                "setUserIconDisabled": t.boolean().optional(),
                "dataRoamingDisabled": t.boolean().optional(),
                "smsDisabled": t.boolean().optional(),
                "androidDevicePolicyTracks": t.array(t.string()).optional(),
                "mobileNetworksConfigDisabled": t.boolean().optional(),
                "locationMode": t.string().optional(),
                "oncCertificateProviders": t.array(
                    t.proxy(renames["OncCertificateProviderIn"])
                ).optional(),
                "usbFileTransferDisabled": t.boolean().optional(),
                "passwordPolicies": t.array(
                    t.proxy(renames["PasswordRequirementsIn"])
                ).optional(),
                "credentialsConfigDisabled": t.boolean().optional(),
                "persistentPreferredActivities": t.array(
                    t.proxy(renames["PersistentPreferredActivityIn"])
                ).optional(),
                "vpnConfigDisabled": t.boolean().optional(),
                "autoTimeRequired": t.boolean().optional(),
                "keyguardDisabledFeatures": t.array(t.string()).optional(),
                "funDisabled": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
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
    functions["enterprisesWebTokensCreate"] = androidmanagement.post(
        "v1/{parent}/webTokens",
        t.struct(
            {
                "parent": t.string().optional(),
                "value": t.string().optional(),
                "name": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "parentFrameUrl": t.string().optional(),
                "enabledFeatures": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["WebTokenOut"]),
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
        importer="androidmanagement", renames=renames, types=types, functions=functions
    )
