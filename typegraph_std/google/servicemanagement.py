from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_servicemanagement() -> Import:
    servicemanagement = HTTPRuntime("https://servicemanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicemanagement_1_ErrorResponse",
        "MetricDescriptorIn": "_servicemanagement_2_MetricDescriptorIn",
        "MetricDescriptorOut": "_servicemanagement_3_MetricDescriptorOut",
        "JavaSettingsIn": "_servicemanagement_4_JavaSettingsIn",
        "JavaSettingsOut": "_servicemanagement_5_JavaSettingsOut",
        "NodeSettingsIn": "_servicemanagement_6_NodeSettingsIn",
        "NodeSettingsOut": "_servicemanagement_7_NodeSettingsOut",
        "UsageIn": "_servicemanagement_8_UsageIn",
        "UsageOut": "_servicemanagement_9_UsageOut",
        "EnumValueIn": "_servicemanagement_10_EnumValueIn",
        "EnumValueOut": "_servicemanagement_11_EnumValueOut",
        "LongRunningIn": "_servicemanagement_12_LongRunningIn",
        "LongRunningOut": "_servicemanagement_13_LongRunningOut",
        "OptionIn": "_servicemanagement_14_OptionIn",
        "OptionOut": "_servicemanagement_15_OptionOut",
        "ListServicesResponseIn": "_servicemanagement_16_ListServicesResponseIn",
        "ListServicesResponseOut": "_servicemanagement_17_ListServicesResponseOut",
        "StepIn": "_servicemanagement_18_StepIn",
        "StepOut": "_servicemanagement_19_StepOut",
        "OAuthRequirementsIn": "_servicemanagement_20_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_servicemanagement_21_OAuthRequirementsOut",
        "LabelDescriptorIn": "_servicemanagement_22_LabelDescriptorIn",
        "LabelDescriptorOut": "_servicemanagement_23_LabelDescriptorOut",
        "MixinIn": "_servicemanagement_24_MixinIn",
        "MixinOut": "_servicemanagement_25_MixinOut",
        "ContextRuleIn": "_servicemanagement_26_ContextRuleIn",
        "ContextRuleOut": "_servicemanagement_27_ContextRuleOut",
        "FieldIn": "_servicemanagement_28_FieldIn",
        "FieldOut": "_servicemanagement_29_FieldOut",
        "SubmitConfigSourceRequestIn": "_servicemanagement_30_SubmitConfigSourceRequestIn",
        "SubmitConfigSourceRequestOut": "_servicemanagement_31_SubmitConfigSourceRequestOut",
        "ApiIn": "_servicemanagement_32_ApiIn",
        "ApiOut": "_servicemanagement_33_ApiOut",
        "CustomErrorRuleIn": "_servicemanagement_34_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_servicemanagement_35_CustomErrorRuleOut",
        "PhpSettingsIn": "_servicemanagement_36_PhpSettingsIn",
        "PhpSettingsOut": "_servicemanagement_37_PhpSettingsOut",
        "ListServiceRolloutsResponseIn": "_servicemanagement_38_ListServiceRolloutsResponseIn",
        "ListServiceRolloutsResponseOut": "_servicemanagement_39_ListServiceRolloutsResponseOut",
        "GoSettingsIn": "_servicemanagement_40_GoSettingsIn",
        "GoSettingsOut": "_servicemanagement_41_GoSettingsOut",
        "DocumentationIn": "_servicemanagement_42_DocumentationIn",
        "DocumentationOut": "_servicemanagement_43_DocumentationOut",
        "SetIamPolicyRequestIn": "_servicemanagement_44_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_servicemanagement_45_SetIamPolicyRequestOut",
        "AuthRequirementIn": "_servicemanagement_46_AuthRequirementIn",
        "AuthRequirementOut": "_servicemanagement_47_AuthRequirementOut",
        "PolicyIn": "_servicemanagement_48_PolicyIn",
        "PolicyOut": "_servicemanagement_49_PolicyOut",
        "StatusIn": "_servicemanagement_50_StatusIn",
        "StatusOut": "_servicemanagement_51_StatusOut",
        "BillingIn": "_servicemanagement_52_BillingIn",
        "BillingOut": "_servicemanagement_53_BillingOut",
        "CommonLanguageSettingsIn": "_servicemanagement_54_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_servicemanagement_55_CommonLanguageSettingsOut",
        "ChangeReportIn": "_servicemanagement_56_ChangeReportIn",
        "ChangeReportOut": "_servicemanagement_57_ChangeReportOut",
        "CustomErrorIn": "_servicemanagement_58_CustomErrorIn",
        "CustomErrorOut": "_servicemanagement_59_CustomErrorOut",
        "ConfigChangeIn": "_servicemanagement_60_ConfigChangeIn",
        "ConfigChangeOut": "_servicemanagement_61_ConfigChangeOut",
        "MonitoringIn": "_servicemanagement_62_MonitoringIn",
        "MonitoringOut": "_servicemanagement_63_MonitoringOut",
        "PublishingIn": "_servicemanagement_64_PublishingIn",
        "PublishingOut": "_servicemanagement_65_PublishingOut",
        "SourceContextIn": "_servicemanagement_66_SourceContextIn",
        "SourceContextOut": "_servicemanagement_67_SourceContextOut",
        "AuditLogConfigIn": "_servicemanagement_68_AuditLogConfigIn",
        "AuditLogConfigOut": "_servicemanagement_69_AuditLogConfigOut",
        "LoggingDestinationIn": "_servicemanagement_70_LoggingDestinationIn",
        "LoggingDestinationOut": "_servicemanagement_71_LoggingDestinationOut",
        "PythonSettingsIn": "_servicemanagement_72_PythonSettingsIn",
        "PythonSettingsOut": "_servicemanagement_73_PythonSettingsOut",
        "ListOperationsResponseIn": "_servicemanagement_74_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_servicemanagement_75_ListOperationsResponseOut",
        "RubySettingsIn": "_servicemanagement_76_RubySettingsIn",
        "RubySettingsOut": "_servicemanagement_77_RubySettingsOut",
        "UndeleteServiceResponseIn": "_servicemanagement_78_UndeleteServiceResponseIn",
        "UndeleteServiceResponseOut": "_servicemanagement_79_UndeleteServiceResponseOut",
        "GenerateConfigReportResponseIn": "_servicemanagement_80_GenerateConfigReportResponseIn",
        "GenerateConfigReportResponseOut": "_servicemanagement_81_GenerateConfigReportResponseOut",
        "MonitoringDestinationIn": "_servicemanagement_82_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_servicemanagement_83_MonitoringDestinationOut",
        "AuthenticationIn": "_servicemanagement_84_AuthenticationIn",
        "AuthenticationOut": "_servicemanagement_85_AuthenticationOut",
        "FlowErrorDetailsIn": "_servicemanagement_86_FlowErrorDetailsIn",
        "FlowErrorDetailsOut": "_servicemanagement_87_FlowErrorDetailsOut",
        "ConfigSourceIn": "_servicemanagement_88_ConfigSourceIn",
        "ConfigSourceOut": "_servicemanagement_89_ConfigSourceOut",
        "TestIamPermissionsResponseIn": "_servicemanagement_90_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_servicemanagement_91_TestIamPermissionsResponseOut",
        "BillingDestinationIn": "_servicemanagement_92_BillingDestinationIn",
        "BillingDestinationOut": "_servicemanagement_93_BillingDestinationOut",
        "SubmitConfigSourceResponseIn": "_servicemanagement_94_SubmitConfigSourceResponseIn",
        "SubmitConfigSourceResponseOut": "_servicemanagement_95_SubmitConfigSourceResponseOut",
        "BindingIn": "_servicemanagement_96_BindingIn",
        "BindingOut": "_servicemanagement_97_BindingOut",
        "MonitoredResourceDescriptorIn": "_servicemanagement_98_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_servicemanagement_99_MonitoredResourceDescriptorOut",
        "CustomHttpPatternIn": "_servicemanagement_100_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_servicemanagement_101_CustomHttpPatternOut",
        "OperationIn": "_servicemanagement_102_OperationIn",
        "OperationOut": "_servicemanagement_103_OperationOut",
        "HttpIn": "_servicemanagement_104_HttpIn",
        "HttpOut": "_servicemanagement_105_HttpOut",
        "TestIamPermissionsRequestIn": "_servicemanagement_106_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_servicemanagement_107_TestIamPermissionsRequestOut",
        "DiagnosticIn": "_servicemanagement_108_DiagnosticIn",
        "DiagnosticOut": "_servicemanagement_109_DiagnosticOut",
        "SourceInfoIn": "_servicemanagement_110_SourceInfoIn",
        "SourceInfoOut": "_servicemanagement_111_SourceInfoOut",
        "ControlIn": "_servicemanagement_112_ControlIn",
        "ControlOut": "_servicemanagement_113_ControlOut",
        "ConfigFileIn": "_servicemanagement_114_ConfigFileIn",
        "ConfigFileOut": "_servicemanagement_115_ConfigFileOut",
        "EnableServiceResponseIn": "_servicemanagement_116_EnableServiceResponseIn",
        "EnableServiceResponseOut": "_servicemanagement_117_EnableServiceResponseOut",
        "SystemParameterRuleIn": "_servicemanagement_118_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_servicemanagement_119_SystemParameterRuleOut",
        "ServiceIn": "_servicemanagement_120_ServiceIn",
        "ServiceOut": "_servicemanagement_121_ServiceOut",
        "AdviceIn": "_servicemanagement_122_AdviceIn",
        "AdviceOut": "_servicemanagement_123_AdviceOut",
        "MetricDescriptorMetadataIn": "_servicemanagement_124_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_servicemanagement_125_MetricDescriptorMetadataOut",
        "QuotaIn": "_servicemanagement_126_QuotaIn",
        "QuotaOut": "_servicemanagement_127_QuotaOut",
        "AuthProviderIn": "_servicemanagement_128_AuthProviderIn",
        "AuthProviderOut": "_servicemanagement_129_AuthProviderOut",
        "HttpRuleIn": "_servicemanagement_130_HttpRuleIn",
        "HttpRuleOut": "_servicemanagement_131_HttpRuleOut",
        "ManagedServiceIn": "_servicemanagement_132_ManagedServiceIn",
        "ManagedServiceOut": "_servicemanagement_133_ManagedServiceOut",
        "ExprIn": "_servicemanagement_134_ExprIn",
        "ExprOut": "_servicemanagement_135_ExprOut",
        "TypeIn": "_servicemanagement_136_TypeIn",
        "TypeOut": "_servicemanagement_137_TypeOut",
        "ResourceReferenceIn": "_servicemanagement_138_ResourceReferenceIn",
        "ResourceReferenceOut": "_servicemanagement_139_ResourceReferenceOut",
        "GetPolicyOptionsIn": "_servicemanagement_140_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_servicemanagement_141_GetPolicyOptionsOut",
        "AuditConfigIn": "_servicemanagement_142_AuditConfigIn",
        "AuditConfigOut": "_servicemanagement_143_AuditConfigOut",
        "OperationInfoIn": "_servicemanagement_144_OperationInfoIn",
        "OperationInfoOut": "_servicemanagement_145_OperationInfoOut",
        "QuotaLimitIn": "_servicemanagement_146_QuotaLimitIn",
        "QuotaLimitOut": "_servicemanagement_147_QuotaLimitOut",
        "LoggingIn": "_servicemanagement_148_LoggingIn",
        "LoggingOut": "_servicemanagement_149_LoggingOut",
        "OperationMetadataIn": "_servicemanagement_150_OperationMetadataIn",
        "OperationMetadataOut": "_servicemanagement_151_OperationMetadataOut",
        "CppSettingsIn": "_servicemanagement_152_CppSettingsIn",
        "CppSettingsOut": "_servicemanagement_153_CppSettingsOut",
        "LogDescriptorIn": "_servicemanagement_154_LogDescriptorIn",
        "LogDescriptorOut": "_servicemanagement_155_LogDescriptorOut",
        "DocumentationRuleIn": "_servicemanagement_156_DocumentationRuleIn",
        "DocumentationRuleOut": "_servicemanagement_157_DocumentationRuleOut",
        "GenerateConfigReportRequestIn": "_servicemanagement_158_GenerateConfigReportRequestIn",
        "GenerateConfigReportRequestOut": "_servicemanagement_159_GenerateConfigReportRequestOut",
        "MethodIn": "_servicemanagement_160_MethodIn",
        "MethodOut": "_servicemanagement_161_MethodOut",
        "ClientLibrarySettingsIn": "_servicemanagement_162_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_servicemanagement_163_ClientLibrarySettingsOut",
        "BackendIn": "_servicemanagement_164_BackendIn",
        "BackendOut": "_servicemanagement_165_BackendOut",
        "DeleteServiceStrategyIn": "_servicemanagement_166_DeleteServiceStrategyIn",
        "DeleteServiceStrategyOut": "_servicemanagement_167_DeleteServiceStrategyOut",
        "GetIamPolicyRequestIn": "_servicemanagement_168_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_servicemanagement_169_GetIamPolicyRequestOut",
        "SystemParameterIn": "_servicemanagement_170_SystemParameterIn",
        "SystemParameterOut": "_servicemanagement_171_SystemParameterOut",
        "MethodSettingsIn": "_servicemanagement_172_MethodSettingsIn",
        "MethodSettingsOut": "_servicemanagement_173_MethodSettingsOut",
        "AuthenticationRuleIn": "_servicemanagement_174_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_servicemanagement_175_AuthenticationRuleOut",
        "PageIn": "_servicemanagement_176_PageIn",
        "PageOut": "_servicemanagement_177_PageOut",
        "DotnetSettingsIn": "_servicemanagement_178_DotnetSettingsIn",
        "DotnetSettingsOut": "_servicemanagement_179_DotnetSettingsOut",
        "EndpointIn": "_servicemanagement_180_EndpointIn",
        "EndpointOut": "_servicemanagement_181_EndpointOut",
        "ListServiceConfigsResponseIn": "_servicemanagement_182_ListServiceConfigsResponseIn",
        "ListServiceConfigsResponseOut": "_servicemanagement_183_ListServiceConfigsResponseOut",
        "MetricRuleIn": "_servicemanagement_184_MetricRuleIn",
        "MetricRuleOut": "_servicemanagement_185_MetricRuleOut",
        "ContextIn": "_servicemanagement_186_ContextIn",
        "ContextOut": "_servicemanagement_187_ContextOut",
        "UsageRuleIn": "_servicemanagement_188_UsageRuleIn",
        "UsageRuleOut": "_servicemanagement_189_UsageRuleOut",
        "RolloutIn": "_servicemanagement_190_RolloutIn",
        "RolloutOut": "_servicemanagement_191_RolloutOut",
        "ConfigRefIn": "_servicemanagement_192_ConfigRefIn",
        "ConfigRefOut": "_servicemanagement_193_ConfigRefOut",
        "TrafficPercentStrategyIn": "_servicemanagement_194_TrafficPercentStrategyIn",
        "TrafficPercentStrategyOut": "_servicemanagement_195_TrafficPercentStrategyOut",
        "JwtLocationIn": "_servicemanagement_196_JwtLocationIn",
        "JwtLocationOut": "_servicemanagement_197_JwtLocationOut",
        "SystemParametersIn": "_servicemanagement_198_SystemParametersIn",
        "SystemParametersOut": "_servicemanagement_199_SystemParametersOut",
        "BackendRuleIn": "_servicemanagement_200_BackendRuleIn",
        "BackendRuleOut": "_servicemanagement_201_BackendRuleOut",
        "EnumIn": "_servicemanagement_202_EnumIn",
        "EnumOut": "_servicemanagement_203_EnumOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "valueType": t.string().optional(),
            "displayName": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "name": t.string().optional(),
            "valueType": t.string().optional(),
            "displayName": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
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
    types["EnumValueIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "number": t.integer().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EnumValueIn"])
    types["EnumValueOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "number": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValueOut"])
    types["LongRunningIn"] = t.struct(
        {
            "totalPollTimeout": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "maxPollDelay": t.string().optional(),
            "initialPollDelay": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "totalPollTimeout": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "maxPollDelay": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["OptionIn"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OptionIn"])
    types["OptionOut"] = t.struct(
        {
            "value": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OptionOut"])
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
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
    types["LabelDescriptorIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "description": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["LabelDescriptorIn"])
    types["LabelDescriptorOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "description": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelDescriptorOut"])
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
    types["ContextRuleIn"] = t.struct(
        {
            "requested": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "requested": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["FieldIn"] = t.struct(
        {
            "typeUrl": t.string().optional(),
            "cardinality": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "packed": t.boolean().optional(),
            "kind": t.string().optional(),
            "jsonName": t.string().optional(),
            "number": t.integer().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "typeUrl": t.string().optional(),
            "cardinality": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "packed": t.boolean().optional(),
            "kind": t.string().optional(),
            "jsonName": t.string().optional(),
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["SubmitConfigSourceRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "configSource": t.proxy(renames["ConfigSourceIn"]),
        }
    ).named(renames["SubmitConfigSourceRequestIn"])
    types["SubmitConfigSourceRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "configSource": t.proxy(renames["ConfigSourceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitConfigSourceRequestOut"])
    types["ApiIn"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
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
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
    types["ListServiceRolloutsResponseIn"] = t.struct(
        {
            "rollouts": t.array(t.proxy(renames["RolloutIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServiceRolloutsResponseIn"])
    types["ListServiceRolloutsResponseOut"] = t.struct(
        {
            "rollouts": t.array(t.proxy(renames["RolloutOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceRolloutsResponseOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["DocumentationIn"] = t.struct(
        {
            "documentationRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "summary": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "overview": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "documentationRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "summary": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "overview": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["CommonLanguageSettingsIn"] = t.struct(
        {
            "referenceDocsUri": t.string().optional(),
            "destinations": t.array(t.string()).optional(),
        }
    ).named(renames["CommonLanguageSettingsIn"])
    types["CommonLanguageSettingsOut"] = t.struct(
        {
            "referenceDocsUri": t.string().optional(),
            "destinations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommonLanguageSettingsOut"])
    types["ChangeReportIn"] = t.struct(
        {"configChanges": t.array(t.proxy(renames["ConfigChangeIn"])).optional()}
    ).named(renames["ChangeReportIn"])
    types["ChangeReportOut"] = t.struct(
        {
            "configChanges": t.array(t.proxy(renames["ConfigChangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeReportOut"])
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
    types["ConfigChangeIn"] = t.struct(
        {
            "advices": t.array(t.proxy(renames["AdviceIn"])).optional(),
            "element": t.string().optional(),
            "oldValue": t.string().optional(),
            "newValue": t.string().optional(),
            "changeType": t.string().optional(),
        }
    ).named(renames["ConfigChangeIn"])
    types["ConfigChangeOut"] = t.struct(
        {
            "advices": t.array(t.proxy(renames["AdviceOut"])).optional(),
            "element": t.string().optional(),
            "oldValue": t.string().optional(),
            "newValue": t.string().optional(),
            "changeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigChangeOut"])
    types["MonitoringIn"] = t.struct(
        {
            "producerDestinations": t.array(
                t.proxy(renames["MonitoringDestinationIn"])
            ).optional(),
            "consumerDestinations": t.array(
                t.proxy(renames["MonitoringDestinationIn"])
            ).optional(),
        }
    ).named(renames["MonitoringIn"])
    types["MonitoringOut"] = t.struct(
        {
            "producerDestinations": t.array(
                t.proxy(renames["MonitoringDestinationOut"])
            ).optional(),
            "consumerDestinations": t.array(
                t.proxy(renames["MonitoringDestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringOut"])
    types["PublishingIn"] = t.struct(
        {
            "organization": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "apiShortName": t.string().optional(),
            "githubLabel": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "documentationUri": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "organization": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "apiShortName": t.string().optional(),
            "githubLabel": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "documentationUri": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
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
    types["LoggingDestinationIn"] = t.struct(
        {
            "logs": t.array(t.string()).optional(),
            "monitoredResource": t.string().optional(),
        }
    ).named(renames["LoggingDestinationIn"])
    types["LoggingDestinationOut"] = t.struct(
        {
            "logs": t.array(t.string()).optional(),
            "monitoredResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingDestinationOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
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
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["UndeleteServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["ManagedServiceIn"]).optional()}
    ).named(renames["UndeleteServiceResponseIn"])
    types["UndeleteServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["ManagedServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteServiceResponseOut"])
    types["GenerateConfigReportResponseIn"] = t.struct(
        {
            "diagnostics": t.array(t.proxy(renames["DiagnosticIn"])).optional(),
            "id": t.string().optional(),
            "changeReports": t.array(t.proxy(renames["ChangeReportIn"])).optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["GenerateConfigReportResponseIn"])
    types["GenerateConfigReportResponseOut"] = t.struct(
        {
            "diagnostics": t.array(t.proxy(renames["DiagnosticOut"])).optional(),
            "id": t.string().optional(),
            "changeReports": t.array(t.proxy(renames["ChangeReportOut"])).optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConfigReportResponseOut"])
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
    types["ConfigSourceIn"] = t.struct(
        {
            "files": t.array(t.proxy(renames["ConfigFileIn"])).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ConfigSourceIn"])
    types["ConfigSourceOut"] = t.struct(
        {
            "files": t.array(t.proxy(renames["ConfigFileOut"])).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigSourceOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["SubmitConfigSourceResponseIn"] = t.struct(
        {"serviceConfig": t.proxy(renames["ServiceIn"]).optional()}
    ).named(renames["SubmitConfigSourceResponseIn"])
    types["SubmitConfigSourceResponseOut"] = t.struct(
        {
            "serviceConfig": t.proxy(renames["ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitConfigSourceResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "launchStage": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "launchStage": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["CustomHttpPatternIn"] = t.struct(
        {"path": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["CustomHttpPatternIn"])
    types["CustomHttpPatternOut"] = t.struct(
        {
            "path": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomHttpPatternOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["HttpIn"] = t.struct(
        {
            "fullyDecodeReservedExpansion": t.boolean().optional(),
            "rules": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
        }
    ).named(renames["HttpIn"])
    types["HttpOut"] = t.struct(
        {
            "fullyDecodeReservedExpansion": t.boolean().optional(),
            "rules": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["DiagnosticIn"] = t.struct(
        {
            "location": t.string().optional(),
            "message": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DiagnosticIn"])
    types["DiagnosticOut"] = t.struct(
        {
            "location": t.string().optional(),
            "message": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnosticOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["ConfigFileIn"] = t.struct(
        {
            "fileType": t.string().optional(),
            "fileContents": t.string().optional(),
            "filePath": t.string().optional(),
        }
    ).named(renames["ConfigFileIn"])
    types["ConfigFileOut"] = t.struct(
        {
            "fileType": t.string().optional(),
            "fileContents": t.string().optional(),
            "filePath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigFileOut"])
    types["EnableServiceResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableServiceResponseIn"]
    )
    types["EnableServiceResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableServiceResponseOut"])
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
    types["ServiceIn"] = t.struct(
        {
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "name": t.string().optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "producerProjectId": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "configVersion": t.integer().optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "name": t.string().optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "title": t.string().optional(),
            "id": t.string().optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "producerProjectId": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "configVersion": t.integer().optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["AdviceIn"] = t.struct({"description": t.string().optional()}).named(
        renames["AdviceIn"]
    )
    types["AdviceOut"] = t.struct(
        {
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdviceOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
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
    types["AuthProviderIn"] = t.struct(
        {
            "issuer": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "audiences": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "issuer": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "audiences": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "responseBody": t.string().optional(),
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "body": t.string().optional(),
            "post": t.string().optional(),
            "delete": t.string().optional(),
            "put": t.string().optional(),
            "get": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "responseBody": t.string().optional(),
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "body": t.string().optional(),
            "post": t.string().optional(),
            "delete": t.string().optional(),
            "put": t.string().optional(),
            "get": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["ManagedServiceIn"] = t.struct(
        {
            "producerProjectId": t.string().optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["ManagedServiceIn"])
    types["ManagedServiceOut"] = t.struct(
        {
            "producerProjectId": t.string().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedServiceOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["TypeIn"] = t.struct(
        {
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["ResourceReferenceIn"] = t.struct(
        {"type": t.string().optional(), "childType": t.string().optional()}
    ).named(renames["ResourceReferenceIn"])
    types["ResourceReferenceOut"] = t.struct(
        {
            "type": t.string().optional(),
            "childType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceReferenceOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["OperationInfoIn"] = t.struct(
        {"responseType": t.string(), "metadataType": t.string()}
    ).named(renames["OperationInfoIn"])
    types["OperationInfoOut"] = t.struct(
        {
            "responseType": t.string(),
            "metadataType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationInfoOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
            "duration": t.string().optional(),
            "freeTier": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "maxLimit": t.string().optional(),
            "metric": t.string().optional(),
            "defaultLimit": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
            "duration": t.string().optional(),
            "freeTier": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "maxLimit": t.string().optional(),
            "metric": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "progressPercentage": t.integer().optional(),
            "startTime": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
            "resourceNames": t.array(t.string()).optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "progressPercentage": t.integer().optional(),
            "startTime": t.string().optional(),
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["LogDescriptorIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
    types["DocumentationRuleIn"] = t.struct(
        {
            "deprecationDescription": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "selector": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "deprecationDescription": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "selector": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
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
    types["MethodIn"] = t.struct(
        {
            "responseTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "requestStreaming": t.boolean().optional(),
            "requestTypeUrl": t.string().optional(),
            "syntax": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "responseTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "requestStreaming": t.boolean().optional(),
            "requestTypeUrl": t.string().optional(),
            "syntax": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "version": t.string().optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "version": t.string().optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
    types["DeleteServiceStrategyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteServiceStrategyIn"]
    )
    types["DeleteServiceStrategyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteServiceStrategyOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["SystemParameterIn"] = t.struct(
        {
            "name": t.string().optional(),
            "urlQueryParameter": t.string().optional(),
            "httpHeader": t.string().optional(),
        }
    ).named(renames["SystemParameterIn"])
    types["SystemParameterOut"] = t.struct(
        {
            "name": t.string().optional(),
            "urlQueryParameter": t.string().optional(),
            "httpHeader": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParameterOut"])
    types["MethodSettingsIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "longRunning": t.proxy(renames["LongRunningIn"]).optional(),
        }
    ).named(renames["MethodSettingsIn"])
    types["MethodSettingsOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "longRunning": t.proxy(renames["LongRunningOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodSettingsOut"])
    types["AuthenticationRuleIn"] = t.struct(
        {
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
            "selector": t.string().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
            "allowWithoutCredential": t.boolean().optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "selector": t.string().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
    types["PageIn"] = t.struct(
        {
            "subpages": t.array(t.proxy(renames["PageIn"])).optional(),
            "name": t.string().optional(),
            "content": t.string().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "subpages": t.array(t.proxy(renames["PageOut"])).optional(),
            "name": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["EndpointIn"] = t.struct(
        {
            "target": t.string().optional(),
            "name": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "aliases": t.array(t.string()).optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "target": t.string().optional(),
            "name": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "aliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["UsageRuleIn"] = t.struct(
        {
            "allowUnregisteredCalls": t.boolean().optional(),
            "selector": t.string().optional(),
            "skipServiceControl": t.boolean().optional(),
        }
    ).named(renames["UsageRuleIn"])
    types["UsageRuleOut"] = t.struct(
        {
            "allowUnregisteredCalls": t.boolean().optional(),
            "selector": t.string().optional(),
            "skipServiceControl": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageRuleOut"])
    types["RolloutIn"] = t.struct(
        {
            "createdBy": t.string().optional(),
            "serviceName": t.string().optional(),
            "rolloutId": t.string().optional(),
            "status": t.string().optional(),
            "createTime": t.string().optional(),
            "deleteServiceStrategy": t.proxy(
                renames["DeleteServiceStrategyIn"]
            ).optional(),
            "trafficPercentStrategy": t.proxy(
                renames["TrafficPercentStrategyIn"]
            ).optional(),
        }
    ).named(renames["RolloutIn"])
    types["RolloutOut"] = t.struct(
        {
            "createdBy": t.string().optional(),
            "serviceName": t.string().optional(),
            "rolloutId": t.string().optional(),
            "status": t.string().optional(),
            "createTime": t.string().optional(),
            "deleteServiceStrategy": t.proxy(
                renames["DeleteServiceStrategyOut"]
            ).optional(),
            "trafficPercentStrategy": t.proxy(
                renames["TrafficPercentStrategyOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutOut"])
    types["ConfigRefIn"] = t.struct({"name": t.string().optional()}).named(
        renames["ConfigRefIn"]
    )
    types["ConfigRefOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigRefOut"])
    types["TrafficPercentStrategyIn"] = t.struct(
        {"percentages": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["TrafficPercentStrategyIn"])
    types["TrafficPercentStrategyOut"] = t.struct(
        {
            "percentages": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficPercentStrategyOut"])
    types["JwtLocationIn"] = t.struct(
        {
            "query": t.string().optional(),
            "cookie": t.string().optional(),
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "query": t.string().optional(),
            "cookie": t.string().optional(),
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["BackendRuleIn"] = t.struct(
        {
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "disableAuth": t.boolean().optional(),
            "pathTranslation": t.string(),
            "deadline": t.number().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "jwtAudience": t.string().optional(),
            "protocol": t.string().optional(),
            "selector": t.string().optional(),
            "operationDeadline": t.number().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "disableAuth": t.boolean().optional(),
            "pathTranslation": t.string(),
            "deadline": t.number().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "jwtAudience": t.string().optional(),
            "protocol": t.string().optional(),
            "selector": t.string().optional(),
            "operationDeadline": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["EnumIn"] = t.struct(
        {
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "edition": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "edition": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])

    functions = {}
    functions["operationsGet"] = servicemanagement.get(
        "v1/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = servicemanagement.get(
        "v1/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGetIamPolicy"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesCreate"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesUndelete"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGenerateConfigReport"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGetConfig"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTestIamPermissions"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDelete"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesSetIamPolicy"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = servicemanagement.get(
        "v1/services",
        t.struct(
            {
                "consumerId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "producerProjectId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConfigsCreate"] = servicemanagement.post(
        "v1/services/{serviceName}/configs:submit",
        t.struct(
            {
                "serviceName": t.string(),
                "validateOnly": t.boolean().optional(),
                "configSource": t.proxy(renames["ConfigSourceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConfigsGet"] = servicemanagement.post(
        "v1/services/{serviceName}/configs:submit",
        t.struct(
            {
                "serviceName": t.string(),
                "validateOnly": t.boolean().optional(),
                "configSource": t.proxy(renames["ConfigSourceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConfigsList"] = servicemanagement.post(
        "v1/services/{serviceName}/configs:submit",
        t.struct(
            {
                "serviceName": t.string(),
                "validateOnly": t.boolean().optional(),
                "configSource": t.proxy(renames["ConfigSourceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConfigsSubmit"] = servicemanagement.post(
        "v1/services/{serviceName}/configs:submit",
        t.struct(
            {
                "serviceName": t.string(),
                "validateOnly": t.boolean().optional(),
                "configSource": t.proxy(renames["ConfigSourceIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConsumersTestIamPermissions"] = servicemanagement.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConsumersGetIamPolicy"] = servicemanagement.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConsumersSetIamPolicy"] = servicemanagement.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesRolloutsGet"] = servicemanagement.get(
        "v1/services/{serviceName}/rollouts",
        t.struct(
            {
                "filter": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "serviceName": t.string(),
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
                "filter": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "serviceName": t.string(),
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
                "filter": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServiceRolloutsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="servicemanagement", renames=renames, types=types, functions=functions
    )
