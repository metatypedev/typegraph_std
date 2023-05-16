from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_servicemanagement() -> Import:
    servicemanagement = HTTPRuntime("https://servicemanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicemanagement_1_ErrorResponse",
        "CustomHttpPatternIn": "_servicemanagement_2_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_servicemanagement_3_CustomHttpPatternOut",
        "GoSettingsIn": "_servicemanagement_4_GoSettingsIn",
        "GoSettingsOut": "_servicemanagement_5_GoSettingsOut",
        "TypeIn": "_servicemanagement_6_TypeIn",
        "TypeOut": "_servicemanagement_7_TypeOut",
        "ConfigRefIn": "_servicemanagement_8_ConfigRefIn",
        "ConfigRefOut": "_servicemanagement_9_ConfigRefOut",
        "EnumValueIn": "_servicemanagement_10_EnumValueIn",
        "EnumValueOut": "_servicemanagement_11_EnumValueOut",
        "DocumentationRuleIn": "_servicemanagement_12_DocumentationRuleIn",
        "DocumentationRuleOut": "_servicemanagement_13_DocumentationRuleOut",
        "OperationInfoIn": "_servicemanagement_14_OperationInfoIn",
        "OperationInfoOut": "_servicemanagement_15_OperationInfoOut",
        "AuditConfigIn": "_servicemanagement_16_AuditConfigIn",
        "AuditConfigOut": "_servicemanagement_17_AuditConfigOut",
        "TestIamPermissionsRequestIn": "_servicemanagement_18_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_servicemanagement_19_TestIamPermissionsRequestOut",
        "NodeSettingsIn": "_servicemanagement_20_NodeSettingsIn",
        "NodeSettingsOut": "_servicemanagement_21_NodeSettingsOut",
        "ApiIn": "_servicemanagement_22_ApiIn",
        "ApiOut": "_servicemanagement_23_ApiOut",
        "HttpIn": "_servicemanagement_24_HttpIn",
        "HttpOut": "_servicemanagement_25_HttpOut",
        "CommonLanguageSettingsIn": "_servicemanagement_26_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_servicemanagement_27_CommonLanguageSettingsOut",
        "ConfigFileIn": "_servicemanagement_28_ConfigFileIn",
        "ConfigFileOut": "_servicemanagement_29_ConfigFileOut",
        "GenerateConfigReportResponseIn": "_servicemanagement_30_GenerateConfigReportResponseIn",
        "GenerateConfigReportResponseOut": "_servicemanagement_31_GenerateConfigReportResponseOut",
        "StatusIn": "_servicemanagement_32_StatusIn",
        "StatusOut": "_servicemanagement_33_StatusOut",
        "PythonSettingsIn": "_servicemanagement_34_PythonSettingsIn",
        "PythonSettingsOut": "_servicemanagement_35_PythonSettingsOut",
        "ContextIn": "_servicemanagement_36_ContextIn",
        "ContextOut": "_servicemanagement_37_ContextOut",
        "EnableServiceResponseIn": "_servicemanagement_38_EnableServiceResponseIn",
        "EnableServiceResponseOut": "_servicemanagement_39_EnableServiceResponseOut",
        "AuthRequirementIn": "_servicemanagement_40_AuthRequirementIn",
        "AuthRequirementOut": "_servicemanagement_41_AuthRequirementOut",
        "SourceContextIn": "_servicemanagement_42_SourceContextIn",
        "SourceContextOut": "_servicemanagement_43_SourceContextOut",
        "SystemParameterRuleIn": "_servicemanagement_44_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_servicemanagement_45_SystemParameterRuleOut",
        "EndpointIn": "_servicemanagement_46_EndpointIn",
        "EndpointOut": "_servicemanagement_47_EndpointOut",
        "RolloutIn": "_servicemanagement_48_RolloutIn",
        "RolloutOut": "_servicemanagement_49_RolloutOut",
        "BackendRuleIn": "_servicemanagement_50_BackendRuleIn",
        "BackendRuleOut": "_servicemanagement_51_BackendRuleOut",
        "ResourceReferenceIn": "_servicemanagement_52_ResourceReferenceIn",
        "ResourceReferenceOut": "_servicemanagement_53_ResourceReferenceOut",
        "ListOperationsResponseIn": "_servicemanagement_54_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_servicemanagement_55_ListOperationsResponseOut",
        "MixinIn": "_servicemanagement_56_MixinIn",
        "MixinOut": "_servicemanagement_57_MixinOut",
        "LogDescriptorIn": "_servicemanagement_58_LogDescriptorIn",
        "LogDescriptorOut": "_servicemanagement_59_LogDescriptorOut",
        "ConfigChangeIn": "_servicemanagement_60_ConfigChangeIn",
        "ConfigChangeOut": "_servicemanagement_61_ConfigChangeOut",
        "SystemParametersIn": "_servicemanagement_62_SystemParametersIn",
        "SystemParametersOut": "_servicemanagement_63_SystemParametersOut",
        "UsageIn": "_servicemanagement_64_UsageIn",
        "UsageOut": "_servicemanagement_65_UsageOut",
        "DocumentationIn": "_servicemanagement_66_DocumentationIn",
        "DocumentationOut": "_servicemanagement_67_DocumentationOut",
        "MetricDescriptorMetadataIn": "_servicemanagement_68_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_servicemanagement_69_MetricDescriptorMetadataOut",
        "ListServiceConfigsResponseIn": "_servicemanagement_70_ListServiceConfigsResponseIn",
        "ListServiceConfigsResponseOut": "_servicemanagement_71_ListServiceConfigsResponseOut",
        "AuthProviderIn": "_servicemanagement_72_AuthProviderIn",
        "AuthProviderOut": "_servicemanagement_73_AuthProviderOut",
        "ClientLibrarySettingsIn": "_servicemanagement_74_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_servicemanagement_75_ClientLibrarySettingsOut",
        "BindingIn": "_servicemanagement_76_BindingIn",
        "BindingOut": "_servicemanagement_77_BindingOut",
        "PhpSettingsIn": "_servicemanagement_78_PhpSettingsIn",
        "PhpSettingsOut": "_servicemanagement_79_PhpSettingsOut",
        "ServiceIn": "_servicemanagement_80_ServiceIn",
        "ServiceOut": "_servicemanagement_81_ServiceOut",
        "QuotaLimitIn": "_servicemanagement_82_QuotaLimitIn",
        "QuotaLimitOut": "_servicemanagement_83_QuotaLimitOut",
        "OAuthRequirementsIn": "_servicemanagement_84_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_servicemanagement_85_OAuthRequirementsOut",
        "BillingIn": "_servicemanagement_86_BillingIn",
        "BillingOut": "_servicemanagement_87_BillingOut",
        "PageIn": "_servicemanagement_88_PageIn",
        "PageOut": "_servicemanagement_89_PageOut",
        "SubmitConfigSourceResponseIn": "_servicemanagement_90_SubmitConfigSourceResponseIn",
        "SubmitConfigSourceResponseOut": "_servicemanagement_91_SubmitConfigSourceResponseOut",
        "JwtLocationIn": "_servicemanagement_92_JwtLocationIn",
        "JwtLocationOut": "_servicemanagement_93_JwtLocationOut",
        "BillingDestinationIn": "_servicemanagement_94_BillingDestinationIn",
        "BillingDestinationOut": "_servicemanagement_95_BillingDestinationOut",
        "StepIn": "_servicemanagement_96_StepIn",
        "StepOut": "_servicemanagement_97_StepOut",
        "MethodSettingsIn": "_servicemanagement_98_MethodSettingsIn",
        "MethodSettingsOut": "_servicemanagement_99_MethodSettingsOut",
        "HttpRuleIn": "_servicemanagement_100_HttpRuleIn",
        "HttpRuleOut": "_servicemanagement_101_HttpRuleOut",
        "AuditLogConfigIn": "_servicemanagement_102_AuditLogConfigIn",
        "AuditLogConfigOut": "_servicemanagement_103_AuditLogConfigOut",
        "AdviceIn": "_servicemanagement_104_AdviceIn",
        "AdviceOut": "_servicemanagement_105_AdviceOut",
        "MethodIn": "_servicemanagement_106_MethodIn",
        "MethodOut": "_servicemanagement_107_MethodOut",
        "SubmitConfigSourceRequestIn": "_servicemanagement_108_SubmitConfigSourceRequestIn",
        "SubmitConfigSourceRequestOut": "_servicemanagement_109_SubmitConfigSourceRequestOut",
        "CustomErrorIn": "_servicemanagement_110_CustomErrorIn",
        "CustomErrorOut": "_servicemanagement_111_CustomErrorOut",
        "GetIamPolicyRequestIn": "_servicemanagement_112_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_servicemanagement_113_GetIamPolicyRequestOut",
        "ChangeReportIn": "_servicemanagement_114_ChangeReportIn",
        "ChangeReportOut": "_servicemanagement_115_ChangeReportOut",
        "ManagedServiceIn": "_servicemanagement_116_ManagedServiceIn",
        "ManagedServiceOut": "_servicemanagement_117_ManagedServiceOut",
        "LabelDescriptorIn": "_servicemanagement_118_LabelDescriptorIn",
        "LabelDescriptorOut": "_servicemanagement_119_LabelDescriptorOut",
        "OperationIn": "_servicemanagement_120_OperationIn",
        "OperationOut": "_servicemanagement_121_OperationOut",
        "GetPolicyOptionsIn": "_servicemanagement_122_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_servicemanagement_123_GetPolicyOptionsOut",
        "LoggingDestinationIn": "_servicemanagement_124_LoggingDestinationIn",
        "LoggingDestinationOut": "_servicemanagement_125_LoggingDestinationOut",
        "MonitoringIn": "_servicemanagement_126_MonitoringIn",
        "MonitoringOut": "_servicemanagement_127_MonitoringOut",
        "DiagnosticIn": "_servicemanagement_128_DiagnosticIn",
        "DiagnosticOut": "_servicemanagement_129_DiagnosticOut",
        "ListServiceRolloutsResponseIn": "_servicemanagement_130_ListServiceRolloutsResponseIn",
        "ListServiceRolloutsResponseOut": "_servicemanagement_131_ListServiceRolloutsResponseOut",
        "ListServicesResponseIn": "_servicemanagement_132_ListServicesResponseIn",
        "ListServicesResponseOut": "_servicemanagement_133_ListServicesResponseOut",
        "PolicyIn": "_servicemanagement_134_PolicyIn",
        "PolicyOut": "_servicemanagement_135_PolicyOut",
        "CppSettingsIn": "_servicemanagement_136_CppSettingsIn",
        "CppSettingsOut": "_servicemanagement_137_CppSettingsOut",
        "ControlIn": "_servicemanagement_138_ControlIn",
        "ControlOut": "_servicemanagement_139_ControlOut",
        "DeleteServiceStrategyIn": "_servicemanagement_140_DeleteServiceStrategyIn",
        "DeleteServiceStrategyOut": "_servicemanagement_141_DeleteServiceStrategyOut",
        "UndeleteServiceResponseIn": "_servicemanagement_142_UndeleteServiceResponseIn",
        "UndeleteServiceResponseOut": "_servicemanagement_143_UndeleteServiceResponseOut",
        "QuotaIn": "_servicemanagement_144_QuotaIn",
        "QuotaOut": "_servicemanagement_145_QuotaOut",
        "SourceInfoIn": "_servicemanagement_146_SourceInfoIn",
        "SourceInfoOut": "_servicemanagement_147_SourceInfoOut",
        "OperationMetadataIn": "_servicemanagement_148_OperationMetadataIn",
        "OperationMetadataOut": "_servicemanagement_149_OperationMetadataOut",
        "OptionIn": "_servicemanagement_150_OptionIn",
        "OptionOut": "_servicemanagement_151_OptionOut",
        "MetricRuleIn": "_servicemanagement_152_MetricRuleIn",
        "MetricRuleOut": "_servicemanagement_153_MetricRuleOut",
        "SystemParameterIn": "_servicemanagement_154_SystemParameterIn",
        "SystemParameterOut": "_servicemanagement_155_SystemParameterOut",
        "EnumIn": "_servicemanagement_156_EnumIn",
        "EnumOut": "_servicemanagement_157_EnumOut",
        "SetIamPolicyRequestIn": "_servicemanagement_158_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_servicemanagement_159_SetIamPolicyRequestOut",
        "MonitoredResourceDescriptorIn": "_servicemanagement_160_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_servicemanagement_161_MonitoredResourceDescriptorOut",
        "TestIamPermissionsResponseIn": "_servicemanagement_162_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_servicemanagement_163_TestIamPermissionsResponseOut",
        "DotnetSettingsIn": "_servicemanagement_164_DotnetSettingsIn",
        "DotnetSettingsOut": "_servicemanagement_165_DotnetSettingsOut",
        "ExprIn": "_servicemanagement_166_ExprIn",
        "ExprOut": "_servicemanagement_167_ExprOut",
        "ConfigSourceIn": "_servicemanagement_168_ConfigSourceIn",
        "ConfigSourceOut": "_servicemanagement_169_ConfigSourceOut",
        "MonitoringDestinationIn": "_servicemanagement_170_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_servicemanagement_171_MonitoringDestinationOut",
        "LongRunningIn": "_servicemanagement_172_LongRunningIn",
        "LongRunningOut": "_servicemanagement_173_LongRunningOut",
        "GenerateConfigReportRequestIn": "_servicemanagement_174_GenerateConfigReportRequestIn",
        "GenerateConfigReportRequestOut": "_servicemanagement_175_GenerateConfigReportRequestOut",
        "UsageRuleIn": "_servicemanagement_176_UsageRuleIn",
        "UsageRuleOut": "_servicemanagement_177_UsageRuleOut",
        "RubySettingsIn": "_servicemanagement_178_RubySettingsIn",
        "RubySettingsOut": "_servicemanagement_179_RubySettingsOut",
        "ContextRuleIn": "_servicemanagement_180_ContextRuleIn",
        "ContextRuleOut": "_servicemanagement_181_ContextRuleOut",
        "AuthenticationRuleIn": "_servicemanagement_182_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_servicemanagement_183_AuthenticationRuleOut",
        "MetricDescriptorIn": "_servicemanagement_184_MetricDescriptorIn",
        "MetricDescriptorOut": "_servicemanagement_185_MetricDescriptorOut",
        "TrafficPercentStrategyIn": "_servicemanagement_186_TrafficPercentStrategyIn",
        "TrafficPercentStrategyOut": "_servicemanagement_187_TrafficPercentStrategyOut",
        "LoggingIn": "_servicemanagement_188_LoggingIn",
        "LoggingOut": "_servicemanagement_189_LoggingOut",
        "FlowErrorDetailsIn": "_servicemanagement_190_FlowErrorDetailsIn",
        "FlowErrorDetailsOut": "_servicemanagement_191_FlowErrorDetailsOut",
        "JavaSettingsIn": "_servicemanagement_192_JavaSettingsIn",
        "JavaSettingsOut": "_servicemanagement_193_JavaSettingsOut",
        "PublishingIn": "_servicemanagement_194_PublishingIn",
        "PublishingOut": "_servicemanagement_195_PublishingOut",
        "CustomErrorRuleIn": "_servicemanagement_196_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_servicemanagement_197_CustomErrorRuleOut",
        "BackendIn": "_servicemanagement_198_BackendIn",
        "BackendOut": "_servicemanagement_199_BackendOut",
        "AuthenticationIn": "_servicemanagement_200_AuthenticationIn",
        "AuthenticationOut": "_servicemanagement_201_AuthenticationOut",
        "FieldIn": "_servicemanagement_202_FieldIn",
        "FieldOut": "_servicemanagement_203_FieldOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CustomHttpPatternIn"] = t.struct(
        {"kind": t.string().optional(), "path": t.string().optional()}
    ).named(renames["CustomHttpPatternIn"])
    types["CustomHttpPatternOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomHttpPatternOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["TypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "syntax": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "syntax": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["ConfigRefIn"] = t.struct({"name": t.string().optional()}).named(
        renames["ConfigRefIn"]
    )
    types["ConfigRefOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigRefOut"])
    types["EnumValueIn"] = t.struct(
        {
            "number": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EnumValueIn"])
    types["EnumValueOut"] = t.struct(
        {
            "number": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValueOut"])
    types["DocumentationRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "description": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "description": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
    types["OperationInfoIn"] = t.struct(
        {"metadataType": t.string(), "responseType": t.string()}
    ).named(renames["OperationInfoIn"])
    types["OperationInfoOut"] = t.struct(
        {
            "metadataType": t.string(),
            "responseType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationInfoOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["ApiIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "syntax": t.string().optional(),
            "version": t.string().optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "syntax": t.string().optional(),
            "version": t.string().optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["HttpIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "fullyDecodeReservedExpansion": t.boolean().optional(),
        }
    ).named(renames["HttpIn"])
    types["HttpOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "fullyDecodeReservedExpansion": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpOut"])
    types["CommonLanguageSettingsIn"] = t.struct(
        {
            "destinations": t.array(t.string()).optional(),
            "referenceDocsUri": t.string().optional(),
        }
    ).named(renames["CommonLanguageSettingsIn"])
    types["CommonLanguageSettingsOut"] = t.struct(
        {
            "destinations": t.array(t.string()).optional(),
            "referenceDocsUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonLanguageSettingsOut"])
    types["ConfigFileIn"] = t.struct(
        {
            "fileContents": t.string().optional(),
            "fileType": t.string().optional(),
            "filePath": t.string().optional(),
        }
    ).named(renames["ConfigFileIn"])
    types["ConfigFileOut"] = t.struct(
        {
            "fileContents": t.string().optional(),
            "fileType": t.string().optional(),
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigFileOut"])
    types["GenerateConfigReportResponseIn"] = t.struct(
        {
            "id": t.string().optional(),
            "changeReports": t.array(t.proxy(renames["ChangeReportIn"])).optional(),
            "serviceName": t.string().optional(),
            "diagnostics": t.array(t.proxy(renames["DiagnosticIn"])).optional(),
        }
    ).named(renames["GenerateConfigReportResponseIn"])
    types["GenerateConfigReportResponseOut"] = t.struct(
        {
            "id": t.string().optional(),
            "changeReports": t.array(t.proxy(renames["ChangeReportOut"])).optional(),
            "serviceName": t.string().optional(),
            "diagnostics": t.array(t.proxy(renames["DiagnosticOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConfigReportResponseOut"])
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
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["EnableServiceResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableServiceResponseIn"]
    )
    types["EnableServiceResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableServiceResponseOut"])
    types["AuthRequirementIn"] = t.struct(
        {"audiences": t.string().optional(), "providerId": t.string().optional()}
    ).named(renames["AuthRequirementIn"])
    types["AuthRequirementOut"] = t.struct(
        {
            "audiences": t.string().optional(),
            "providerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthRequirementOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["SystemParameterRuleIn"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["SystemParameterIn"])).optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["SystemParameterRuleIn"])
    types["SystemParameterRuleOut"] = t.struct(
        {
            "parameters": t.array(t.proxy(renames["SystemParameterOut"])).optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParameterRuleOut"])
    types["EndpointIn"] = t.struct(
        {
            "name": t.string().optional(),
            "target": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "allowCors": t.boolean().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "name": t.string().optional(),
            "target": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "allowCors": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["RolloutIn"] = t.struct(
        {
            "createdBy": t.string().optional(),
            "status": t.string().optional(),
            "trafficPercentStrategy": t.proxy(
                renames["TrafficPercentStrategyIn"]
            ).optional(),
            "rolloutId": t.string().optional(),
            "deleteServiceStrategy": t.proxy(
                renames["DeleteServiceStrategyIn"]
            ).optional(),
            "serviceName": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["RolloutIn"])
    types["RolloutOut"] = t.struct(
        {
            "createdBy": t.string().optional(),
            "status": t.string().optional(),
            "trafficPercentStrategy": t.proxy(
                renames["TrafficPercentStrategyOut"]
            ).optional(),
            "rolloutId": t.string().optional(),
            "deleteServiceStrategy": t.proxy(
                renames["DeleteServiceStrategyOut"]
            ).optional(),
            "serviceName": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutOut"])
    types["BackendRuleIn"] = t.struct(
        {
            "disableAuth": t.boolean().optional(),
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "operationDeadline": t.number().optional(),
            "deadline": t.number().optional(),
            "selector": t.string().optional(),
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "protocol": t.string().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "disableAuth": t.boolean().optional(),
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "operationDeadline": t.number().optional(),
            "deadline": t.number().optional(),
            "selector": t.string().optional(),
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "protocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["ResourceReferenceIn"] = t.struct(
        {"childType": t.string().optional(), "type": t.string().optional()}
    ).named(renames["ResourceReferenceIn"])
    types["ResourceReferenceOut"] = t.struct(
        {
            "childType": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceReferenceOut"])
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
    types["MixinIn"] = t.struct(
        {"name": t.string().optional(), "root": t.string().optional()}
    ).named(renames["MixinIn"])
    types["MixinOut"] = t.struct(
        {
            "name": t.string().optional(),
            "root": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MixinOut"])
    types["LogDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
    types["ConfigChangeIn"] = t.struct(
        {
            "element": t.string().optional(),
            "advices": t.array(t.proxy(renames["AdviceIn"])).optional(),
            "changeType": t.string().optional(),
            "oldValue": t.string().optional(),
            "newValue": t.string().optional(),
        }
    ).named(renames["ConfigChangeIn"])
    types["ConfigChangeOut"] = t.struct(
        {
            "element": t.string().optional(),
            "advices": t.array(t.proxy(renames["AdviceOut"])).optional(),
            "changeType": t.string().optional(),
            "oldValue": t.string().optional(),
            "newValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigChangeOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["UsageIn"] = t.struct(
        {
            "requirements": t.array(t.string()).optional(),
            "producerNotificationChannel": t.string().optional(),
            "rules": t.array(t.proxy(renames["UsageRuleIn"])).optional(),
        }
    ).named(renames["UsageIn"])
    types["UsageOut"] = t.struct(
        {
            "requirements": t.array(t.string()).optional(),
            "producerNotificationChannel": t.string().optional(),
            "rules": t.array(t.proxy(renames["UsageRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageOut"])
    types["DocumentationIn"] = t.struct(
        {
            "serviceRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "serviceRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "samplePeriod": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
    types["ListServiceConfigsResponseIn"] = t.struct(
        {
            "serviceConfigs": t.array(t.proxy(renames["ServiceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServiceConfigsResponseIn"])
    types["ListServiceConfigsResponseOut"] = t.struct(
        {
            "serviceConfigs": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceConfigsResponseOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "id": t.string().optional(),
            "jwksUri": t.string().optional(),
            "audiences": t.string().optional(),
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "authorizationUrl": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "id": t.string().optional(),
            "jwksUri": t.string().optional(),
            "audiences": t.string().optional(),
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "authorizationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "version": t.string().optional(),
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "version": t.string().optional(),
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
    types["ServiceIn"] = t.struct(
        {
            "title": t.string().optional(),
            "configVersion": t.integer().optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "id": t.string().optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "producerProjectId": t.string().optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "name": t.string().optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "title": t.string().optional(),
            "configVersion": t.integer().optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "id": t.string().optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "producerProjectId": t.string().optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "name": t.string().optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "freeTier": t.string().optional(),
            "description": t.string().optional(),
            "metric": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "name": t.string().optional(),
            "maxLimit": t.string().optional(),
            "displayName": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "freeTier": t.string().optional(),
            "description": t.string().optional(),
            "metric": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "name": t.string().optional(),
            "maxLimit": t.string().optional(),
            "displayName": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
    types["BillingIn"] = t.struct(
        {
            "consumerDestinations": t.array(
                t.proxy(renames["BillingDestinationIn"])
            ).optional()
        }
    ).named(renames["BillingIn"])
    types["BillingOut"] = t.struct(
        {
            "consumerDestinations": t.array(
                t.proxy(renames["BillingDestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingOut"])
    types["PageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "subpages": t.array(t.proxy(renames["PageIn"])).optional(),
            "content": t.string().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "subpages": t.array(t.proxy(renames["PageOut"])).optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["SubmitConfigSourceResponseIn"] = t.struct(
        {"serviceConfig": t.proxy(renames["ServiceIn"]).optional()}
    ).named(renames["SubmitConfigSourceResponseIn"])
    types["SubmitConfigSourceResponseOut"] = t.struct(
        {
            "serviceConfig": t.proxy(renames["ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitConfigSourceResponseOut"])
    types["JwtLocationIn"] = t.struct(
        {
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
            "query": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["BillingDestinationIn"] = t.struct(
        {
            "monitoredResource": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
        }
    ).named(renames["BillingDestinationIn"])
    types["BillingDestinationOut"] = t.struct(
        {
            "monitoredResource": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingDestinationOut"])
    types["StepIn"] = t.struct(
        {"status": t.string().optional(), "description": t.string().optional()}
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "status": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["MethodSettingsIn"] = t.struct(
        {
            "longRunning": t.proxy(renames["LongRunningIn"]).optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["MethodSettingsIn"])
    types["MethodSettingsOut"] = t.struct(
        {
            "longRunning": t.proxy(renames["LongRunningOut"]).optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodSettingsOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "patch": t.string().optional(),
            "body": t.string().optional(),
            "get": t.string().optional(),
            "delete": t.string().optional(),
            "post": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "put": t.string().optional(),
            "responseBody": t.string().optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "patch": t.string().optional(),
            "body": t.string().optional(),
            "get": t.string().optional(),
            "delete": t.string().optional(),
            "post": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "put": t.string().optional(),
            "responseBody": t.string().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["AdviceIn"] = t.struct({"description": t.string().optional()}).named(
        renames["AdviceIn"]
    )
    types["AdviceOut"] = t.struct(
        {
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdviceOut"])
    types["MethodIn"] = t.struct(
        {
            "responseTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "responseStreaming": t.boolean().optional(),
            "requestStreaming": t.boolean().optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "responseTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "responseStreaming": t.boolean().optional(),
            "requestStreaming": t.boolean().optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["SubmitConfigSourceRequestIn"] = t.struct(
        {
            "configSource": t.proxy(renames["ConfigSourceIn"]),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["SubmitConfigSourceRequestIn"])
    types["SubmitConfigSourceRequestOut"] = t.struct(
        {
            "configSource": t.proxy(renames["ConfigSourceOut"]),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitConfigSourceRequestOut"])
    types["CustomErrorIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["CustomErrorRuleIn"])).optional(),
            "types": t.array(t.string()).optional(),
        }
    ).named(renames["CustomErrorIn"])
    types["CustomErrorOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["CustomErrorRuleOut"])).optional(),
            "types": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomErrorOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["ChangeReportIn"] = t.struct(
        {"configChanges": t.array(t.proxy(renames["ConfigChangeIn"])).optional()}
    ).named(renames["ChangeReportIn"])
    types["ChangeReportOut"] = t.struct(
        {
            "configChanges": t.array(t.proxy(renames["ConfigChangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeReportOut"])
    types["ManagedServiceIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "producerProjectId": t.string().optional(),
        }
    ).named(renames["ManagedServiceIn"])
    types["ManagedServiceOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "producerProjectId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedServiceOut"])
    types["LabelDescriptorIn"] = t.struct(
        {
            "key": t.string().optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
        }
    ).named(renames["LabelDescriptorIn"])
    types["LabelDescriptorOut"] = t.struct(
        {
            "key": t.string().optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelDescriptorOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["LoggingDestinationIn"] = t.struct(
        {
            "monitoredResource": t.string().optional(),
            "logs": t.array(t.string()).optional(),
        }
    ).named(renames["LoggingDestinationIn"])
    types["LoggingDestinationOut"] = t.struct(
        {
            "monitoredResource": t.string().optional(),
            "logs": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingDestinationOut"])
    types["MonitoringIn"] = t.struct(
        {
            "consumerDestinations": t.array(
                t.proxy(renames["MonitoringDestinationIn"])
            ).optional(),
            "producerDestinations": t.array(
                t.proxy(renames["MonitoringDestinationIn"])
            ).optional(),
        }
    ).named(renames["MonitoringIn"])
    types["MonitoringOut"] = t.struct(
        {
            "consumerDestinations": t.array(
                t.proxy(renames["MonitoringDestinationOut"])
            ).optional(),
            "producerDestinations": t.array(
                t.proxy(renames["MonitoringDestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringOut"])
    types["DiagnosticIn"] = t.struct(
        {
            "message": t.string().optional(),
            "kind": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["DiagnosticIn"])
    types["DiagnosticOut"] = t.struct(
        {
            "message": t.string().optional(),
            "kind": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnosticOut"])
    types["ListServiceRolloutsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rollouts": t.array(t.proxy(renames["RolloutIn"])).optional(),
        }
    ).named(renames["ListServiceRolloutsResponseIn"])
    types["ListServiceRolloutsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "rollouts": t.array(t.proxy(renames["RolloutOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceRolloutsResponseOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(t.proxy(renames["ManagedServiceIn"])).optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(t.proxy(renames["ManagedServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["DeleteServiceStrategyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteServiceStrategyIn"]
    )
    types["DeleteServiceStrategyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteServiceStrategyOut"])
    types["UndeleteServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["ManagedServiceIn"]).optional()}
    ).named(renames["UndeleteServiceResponseIn"])
    types["UndeleteServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["ManagedServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteServiceResponseOut"])
    types["QuotaIn"] = t.struct(
        {
            "limits": t.array(t.proxy(renames["QuotaLimitIn"])).optional(),
            "metricRules": t.array(t.proxy(renames["MetricRuleIn"])).optional(),
        }
    ).named(renames["QuotaIn"])
    types["QuotaOut"] = t.struct(
        {
            "limits": t.array(t.proxy(renames["QuotaLimitOut"])).optional(),
            "metricRules": t.array(t.proxy(renames["MetricRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
            "resourceNames": t.array(t.string()).optional(),
            "progressPercentage": t.integer().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "resourceNames": t.array(t.string()).optional(),
            "progressPercentage": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["OptionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OptionIn"])
    types["OptionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "value": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionOut"])
    types["MetricRuleIn"] = t.struct(
        {
            "metricCosts": t.struct({"_": t.string().optional()}).optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["MetricRuleIn"])
    types["MetricRuleOut"] = t.struct(
        {
            "metricCosts": t.struct({"_": t.string().optional()}).optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricRuleOut"])
    types["SystemParameterIn"] = t.struct(
        {
            "name": t.string().optional(),
            "httpHeader": t.string().optional(),
            "urlQueryParameter": t.string().optional(),
        }
    ).named(renames["SystemParameterIn"])
    types["SystemParameterOut"] = t.struct(
        {
            "name": t.string().optional(),
            "httpHeader": t.string().optional(),
            "urlQueryParameter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParameterOut"])
    types["EnumIn"] = t.struct(
        {
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ConfigSourceIn"] = t.struct(
        {
            "id": t.string().optional(),
            "files": t.array(t.proxy(renames["ConfigFileIn"])).optional(),
        }
    ).named(renames["ConfigSourceIn"])
    types["ConfigSourceOut"] = t.struct(
        {
            "id": t.string().optional(),
            "files": t.array(t.proxy(renames["ConfigFileOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigSourceOut"])
    types["MonitoringDestinationIn"] = t.struct(
        {
            "monitoredResource": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
        }
    ).named(renames["MonitoringDestinationIn"])
    types["MonitoringDestinationOut"] = t.struct(
        {
            "monitoredResource": t.string().optional(),
            "metrics": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringDestinationOut"])
    types["LongRunningIn"] = t.struct(
        {
            "maxPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "initialPollDelay": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "maxPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "initialPollDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["GenerateConfigReportRequestIn"] = t.struct(
        {
            "newConfig": t.struct({"_": t.string().optional()}),
            "oldConfig": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GenerateConfigReportRequestIn"])
    types["GenerateConfigReportRequestOut"] = t.struct(
        {
            "newConfig": t.struct({"_": t.string().optional()}),
            "oldConfig": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConfigReportRequestOut"])
    types["UsageRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "skipServiceControl": t.boolean().optional(),
            "allowUnregisteredCalls": t.boolean().optional(),
        }
    ).named(renames["UsageRuleIn"])
    types["UsageRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "skipServiceControl": t.boolean().optional(),
            "allowUnregisteredCalls": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageRuleOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["AuthenticationRuleIn"] = t.struct(
        {
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
            "selector": t.string().optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "selector": t.string().optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "metricKind": t.string().optional(),
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "metricKind": t.string().optional(),
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["TrafficPercentStrategyIn"] = t.struct(
        {"percentages": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["TrafficPercentStrategyIn"])
    types["TrafficPercentStrategyOut"] = t.struct(
        {
            "percentages": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficPercentStrategyOut"])
    types["LoggingIn"] = t.struct(
        {
            "consumerDestinations": t.array(
                t.proxy(renames["LoggingDestinationIn"])
            ).optional(),
            "producerDestinations": t.array(
                t.proxy(renames["LoggingDestinationIn"])
            ).optional(),
        }
    ).named(renames["LoggingIn"])
    types["LoggingOut"] = t.struct(
        {
            "consumerDestinations": t.array(
                t.proxy(renames["LoggingDestinationOut"])
            ).optional(),
            "producerDestinations": t.array(
                t.proxy(renames["LoggingDestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingOut"])
    types["FlowErrorDetailsIn"] = t.struct(
        {"exceptionType": t.string().optional(), "flowStepId": t.string().optional()}
    ).named(renames["FlowErrorDetailsIn"])
    types["FlowErrorDetailsOut"] = t.struct(
        {
            "exceptionType": t.string().optional(),
            "flowStepId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlowErrorDetailsOut"])
    types["JavaSettingsIn"] = t.struct(
        {
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "libraryPackage": t.string().optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
        }
    ).named(renames["JavaSettingsIn"])
    types["JavaSettingsOut"] = t.struct(
        {
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "libraryPackage": t.string().optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JavaSettingsOut"])
    types["PublishingIn"] = t.struct(
        {
            "docTagPrefix": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "documentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "githubLabel": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "docTagPrefix": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "documentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "githubLabel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["CustomErrorRuleIn"] = t.struct(
        {"selector": t.string().optional(), "isErrorType": t.boolean().optional()}
    ).named(renames["CustomErrorRuleIn"])
    types["CustomErrorRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "isErrorType": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomErrorRuleOut"])
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
    types["AuthenticationIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["AuthenticationRuleIn"])).optional(),
            "providers": t.array(t.proxy(renames["AuthProviderIn"])).optional(),
        }
    ).named(renames["AuthenticationIn"])
    types["AuthenticationOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["AuthenticationRuleOut"])).optional(),
            "providers": t.array(t.proxy(renames["AuthProviderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationOut"])
    types["FieldIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "typeUrl": t.string().optional(),
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "jsonName": t.string().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "oneofIndex": t.integer().optional(),
            "packed": t.boolean().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "typeUrl": t.string().optional(),
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "jsonName": t.string().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "oneofIndex": t.integer().optional(),
            "packed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])

    functions = {}
    functions["operationsList"] = servicemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = servicemanagement.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesSetIamPolicy"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGetConfig"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesUndelete"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGenerateConfigReport"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDelete"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesCreate"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGetIamPolicy"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTestIamPermissions"] = servicemanagement.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesRolloutsGet"] = servicemanagement.get(
        "v1/services/{serviceName}/rollouts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "serviceName": t.string(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesRolloutsCreate"] = servicemanagement.get(
        "v1/services/{serviceName}/rollouts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "serviceName": t.string(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesRolloutsList"] = servicemanagement.get(
        "v1/services/{serviceName}/rollouts",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "serviceName": t.string(),
                "filter": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConsumersTestIamPermissions"] = servicemanagement.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConsumersSetIamPolicy"] = servicemanagement.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConsumersGetIamPolicy"] = servicemanagement.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConfigsCreate"] = servicemanagement.get(
        "v1/services/{serviceName}/configs/{configId}",
        t.struct(
            {
                "serviceName": t.string(),
                "view": t.string().optional(),
                "configId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConfigsList"] = servicemanagement.get(
        "v1/services/{serviceName}/configs/{configId}",
        t.struct(
            {
                "serviceName": t.string(),
                "view": t.string().optional(),
                "configId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConfigsSubmit"] = servicemanagement.get(
        "v1/services/{serviceName}/configs/{configId}",
        t.struct(
            {
                "serviceName": t.string(),
                "view": t.string().optional(),
                "configId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConfigsGet"] = servicemanagement.get(
        "v1/services/{serviceName}/configs/{configId}",
        t.struct(
            {
                "serviceName": t.string(),
                "view": t.string().optional(),
                "configId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="servicemanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
