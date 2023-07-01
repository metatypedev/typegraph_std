from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_servicemanagement():
    servicemanagement = HTTPRuntime("https://servicemanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicemanagement_1_ErrorResponse",
        "JwtLocationIn": "_servicemanagement_2_JwtLocationIn",
        "JwtLocationOut": "_servicemanagement_3_JwtLocationOut",
        "ContextRuleIn": "_servicemanagement_4_ContextRuleIn",
        "ContextRuleOut": "_servicemanagement_5_ContextRuleOut",
        "PolicyIn": "_servicemanagement_6_PolicyIn",
        "PolicyOut": "_servicemanagement_7_PolicyOut",
        "LogDescriptorIn": "_servicemanagement_8_LogDescriptorIn",
        "LogDescriptorOut": "_servicemanagement_9_LogDescriptorOut",
        "QuotaLimitIn": "_servicemanagement_10_QuotaLimitIn",
        "QuotaLimitOut": "_servicemanagement_11_QuotaLimitOut",
        "JavaSettingsIn": "_servicemanagement_12_JavaSettingsIn",
        "JavaSettingsOut": "_servicemanagement_13_JavaSettingsOut",
        "MonitoringDestinationIn": "_servicemanagement_14_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_servicemanagement_15_MonitoringDestinationOut",
        "SourceContextIn": "_servicemanagement_16_SourceContextIn",
        "SourceContextOut": "_servicemanagement_17_SourceContextOut",
        "BindingIn": "_servicemanagement_18_BindingIn",
        "BindingOut": "_servicemanagement_19_BindingOut",
        "TestIamPermissionsResponseIn": "_servicemanagement_20_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_servicemanagement_21_TestIamPermissionsResponseOut",
        "SystemParameterIn": "_servicemanagement_22_SystemParameterIn",
        "SystemParameterOut": "_servicemanagement_23_SystemParameterOut",
        "TypeIn": "_servicemanagement_24_TypeIn",
        "TypeOut": "_servicemanagement_25_TypeOut",
        "DocumentationRuleIn": "_servicemanagement_26_DocumentationRuleIn",
        "DocumentationRuleOut": "_servicemanagement_27_DocumentationRuleOut",
        "ExprIn": "_servicemanagement_28_ExprIn",
        "ExprOut": "_servicemanagement_29_ExprOut",
        "LoggingDestinationIn": "_servicemanagement_30_LoggingDestinationIn",
        "LoggingDestinationOut": "_servicemanagement_31_LoggingDestinationOut",
        "ManagedServiceIn": "_servicemanagement_32_ManagedServiceIn",
        "ManagedServiceOut": "_servicemanagement_33_ManagedServiceOut",
        "AdviceIn": "_servicemanagement_34_AdviceIn",
        "AdviceOut": "_servicemanagement_35_AdviceOut",
        "MethodIn": "_servicemanagement_36_MethodIn",
        "MethodOut": "_servicemanagement_37_MethodOut",
        "MonitoredResourceDescriptorIn": "_servicemanagement_38_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_servicemanagement_39_MonitoredResourceDescriptorOut",
        "ApiIn": "_servicemanagement_40_ApiIn",
        "ApiOut": "_servicemanagement_41_ApiOut",
        "AuthenticationIn": "_servicemanagement_42_AuthenticationIn",
        "AuthenticationOut": "_servicemanagement_43_AuthenticationOut",
        "HttpRuleIn": "_servicemanagement_44_HttpRuleIn",
        "HttpRuleOut": "_servicemanagement_45_HttpRuleOut",
        "OperationInfoIn": "_servicemanagement_46_OperationInfoIn",
        "OperationInfoOut": "_servicemanagement_47_OperationInfoOut",
        "GetIamPolicyRequestIn": "_servicemanagement_48_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_servicemanagement_49_GetIamPolicyRequestOut",
        "ConfigFileIn": "_servicemanagement_50_ConfigFileIn",
        "ConfigFileOut": "_servicemanagement_51_ConfigFileOut",
        "ConfigChangeIn": "_servicemanagement_52_ConfigChangeIn",
        "ConfigChangeOut": "_servicemanagement_53_ConfigChangeOut",
        "DeleteServiceStrategyIn": "_servicemanagement_54_DeleteServiceStrategyIn",
        "DeleteServiceStrategyOut": "_servicemanagement_55_DeleteServiceStrategyOut",
        "CustomHttpPatternIn": "_servicemanagement_56_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_servicemanagement_57_CustomHttpPatternOut",
        "UsageIn": "_servicemanagement_58_UsageIn",
        "UsageOut": "_servicemanagement_59_UsageOut",
        "FieldIn": "_servicemanagement_60_FieldIn",
        "FieldOut": "_servicemanagement_61_FieldOut",
        "UsageRuleIn": "_servicemanagement_62_UsageRuleIn",
        "UsageRuleOut": "_servicemanagement_63_UsageRuleOut",
        "PhpSettingsIn": "_servicemanagement_64_PhpSettingsIn",
        "PhpSettingsOut": "_servicemanagement_65_PhpSettingsOut",
        "StatusIn": "_servicemanagement_66_StatusIn",
        "StatusOut": "_servicemanagement_67_StatusOut",
        "ChangeReportIn": "_servicemanagement_68_ChangeReportIn",
        "ChangeReportOut": "_servicemanagement_69_ChangeReportOut",
        "SystemParameterRuleIn": "_servicemanagement_70_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_servicemanagement_71_SystemParameterRuleOut",
        "GetPolicyOptionsIn": "_servicemanagement_72_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_servicemanagement_73_GetPolicyOptionsOut",
        "GenerateConfigReportResponseIn": "_servicemanagement_74_GenerateConfigReportResponseIn",
        "GenerateConfigReportResponseOut": "_servicemanagement_75_GenerateConfigReportResponseOut",
        "SourceInfoIn": "_servicemanagement_76_SourceInfoIn",
        "SourceInfoOut": "_servicemanagement_77_SourceInfoOut",
        "LoggingIn": "_servicemanagement_78_LoggingIn",
        "LoggingOut": "_servicemanagement_79_LoggingOut",
        "OperationMetadataIn": "_servicemanagement_80_OperationMetadataIn",
        "OperationMetadataOut": "_servicemanagement_81_OperationMetadataOut",
        "HttpIn": "_servicemanagement_82_HttpIn",
        "HttpOut": "_servicemanagement_83_HttpOut",
        "EnumIn": "_servicemanagement_84_EnumIn",
        "EnumOut": "_servicemanagement_85_EnumOut",
        "CppSettingsIn": "_servicemanagement_86_CppSettingsIn",
        "CppSettingsOut": "_servicemanagement_87_CppSettingsOut",
        "ListServiceConfigsResponseIn": "_servicemanagement_88_ListServiceConfigsResponseIn",
        "ListServiceConfigsResponseOut": "_servicemanagement_89_ListServiceConfigsResponseOut",
        "BackendRuleIn": "_servicemanagement_90_BackendRuleIn",
        "BackendRuleOut": "_servicemanagement_91_BackendRuleOut",
        "OperationIn": "_servicemanagement_92_OperationIn",
        "OperationOut": "_servicemanagement_93_OperationOut",
        "EnableServiceResponseIn": "_servicemanagement_94_EnableServiceResponseIn",
        "EnableServiceResponseOut": "_servicemanagement_95_EnableServiceResponseOut",
        "PythonSettingsIn": "_servicemanagement_96_PythonSettingsIn",
        "PythonSettingsOut": "_servicemanagement_97_PythonSettingsOut",
        "ServiceIn": "_servicemanagement_98_ServiceIn",
        "ServiceOut": "_servicemanagement_99_ServiceOut",
        "OptionIn": "_servicemanagement_100_OptionIn",
        "OptionOut": "_servicemanagement_101_OptionOut",
        "SubmitConfigSourceResponseIn": "_servicemanagement_102_SubmitConfigSourceResponseIn",
        "SubmitConfigSourceResponseOut": "_servicemanagement_103_SubmitConfigSourceResponseOut",
        "AuthRequirementIn": "_servicemanagement_104_AuthRequirementIn",
        "AuthRequirementOut": "_servicemanagement_105_AuthRequirementOut",
        "DiagnosticIn": "_servicemanagement_106_DiagnosticIn",
        "DiagnosticOut": "_servicemanagement_107_DiagnosticOut",
        "AuthenticationRuleIn": "_servicemanagement_108_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_servicemanagement_109_AuthenticationRuleOut",
        "ClientLibrarySettingsIn": "_servicemanagement_110_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_servicemanagement_111_ClientLibrarySettingsOut",
        "NodeSettingsIn": "_servicemanagement_112_NodeSettingsIn",
        "NodeSettingsOut": "_servicemanagement_113_NodeSettingsOut",
        "OAuthRequirementsIn": "_servicemanagement_114_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_servicemanagement_115_OAuthRequirementsOut",
        "QuotaIn": "_servicemanagement_116_QuotaIn",
        "QuotaOut": "_servicemanagement_117_QuotaOut",
        "MetricDescriptorIn": "_servicemanagement_118_MetricDescriptorIn",
        "MetricDescriptorOut": "_servicemanagement_119_MetricDescriptorOut",
        "BillingIn": "_servicemanagement_120_BillingIn",
        "BillingOut": "_servicemanagement_121_BillingOut",
        "SubmitConfigSourceRequestIn": "_servicemanagement_122_SubmitConfigSourceRequestIn",
        "SubmitConfigSourceRequestOut": "_servicemanagement_123_SubmitConfigSourceRequestOut",
        "EndpointIn": "_servicemanagement_124_EndpointIn",
        "EndpointOut": "_servicemanagement_125_EndpointOut",
        "ListServiceRolloutsResponseIn": "_servicemanagement_126_ListServiceRolloutsResponseIn",
        "ListServiceRolloutsResponseOut": "_servicemanagement_127_ListServiceRolloutsResponseOut",
        "LabelDescriptorIn": "_servicemanagement_128_LabelDescriptorIn",
        "LabelDescriptorOut": "_servicemanagement_129_LabelDescriptorOut",
        "DotnetSettingsIn": "_servicemanagement_130_DotnetSettingsIn",
        "DotnetSettingsOut": "_servicemanagement_131_DotnetSettingsOut",
        "TestIamPermissionsRequestIn": "_servicemanagement_132_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_servicemanagement_133_TestIamPermissionsRequestOut",
        "ConfigRefIn": "_servicemanagement_134_ConfigRefIn",
        "ConfigRefOut": "_servicemanagement_135_ConfigRefOut",
        "TrafficPercentStrategyIn": "_servicemanagement_136_TrafficPercentStrategyIn",
        "TrafficPercentStrategyOut": "_servicemanagement_137_TrafficPercentStrategyOut",
        "ControlIn": "_servicemanagement_138_ControlIn",
        "ControlOut": "_servicemanagement_139_ControlOut",
        "RolloutIn": "_servicemanagement_140_RolloutIn",
        "RolloutOut": "_servicemanagement_141_RolloutOut",
        "SystemParametersIn": "_servicemanagement_142_SystemParametersIn",
        "SystemParametersOut": "_servicemanagement_143_SystemParametersOut",
        "ListOperationsResponseIn": "_servicemanagement_144_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_servicemanagement_145_ListOperationsResponseOut",
        "ConfigSourceIn": "_servicemanagement_146_ConfigSourceIn",
        "ConfigSourceOut": "_servicemanagement_147_ConfigSourceOut",
        "EnumValueIn": "_servicemanagement_148_EnumValueIn",
        "EnumValueOut": "_servicemanagement_149_EnumValueOut",
        "StepIn": "_servicemanagement_150_StepIn",
        "StepOut": "_servicemanagement_151_StepOut",
        "AuditConfigIn": "_servicemanagement_152_AuditConfigIn",
        "AuditConfigOut": "_servicemanagement_153_AuditConfigOut",
        "BackendIn": "_servicemanagement_154_BackendIn",
        "BackendOut": "_servicemanagement_155_BackendOut",
        "SetIamPolicyRequestIn": "_servicemanagement_156_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_servicemanagement_157_SetIamPolicyRequestOut",
        "GoSettingsIn": "_servicemanagement_158_GoSettingsIn",
        "GoSettingsOut": "_servicemanagement_159_GoSettingsOut",
        "CustomErrorIn": "_servicemanagement_160_CustomErrorIn",
        "CustomErrorOut": "_servicemanagement_161_CustomErrorOut",
        "MethodSettingsIn": "_servicemanagement_162_MethodSettingsIn",
        "MethodSettingsOut": "_servicemanagement_163_MethodSettingsOut",
        "PageIn": "_servicemanagement_164_PageIn",
        "PageOut": "_servicemanagement_165_PageOut",
        "MetricDescriptorMetadataIn": "_servicemanagement_166_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_servicemanagement_167_MetricDescriptorMetadataOut",
        "ResourceReferenceIn": "_servicemanagement_168_ResourceReferenceIn",
        "ResourceReferenceOut": "_servicemanagement_169_ResourceReferenceOut",
        "FlowErrorDetailsIn": "_servicemanagement_170_FlowErrorDetailsIn",
        "FlowErrorDetailsOut": "_servicemanagement_171_FlowErrorDetailsOut",
        "LongRunningIn": "_servicemanagement_172_LongRunningIn",
        "LongRunningOut": "_servicemanagement_173_LongRunningOut",
        "UndeleteServiceResponseIn": "_servicemanagement_174_UndeleteServiceResponseIn",
        "UndeleteServiceResponseOut": "_servicemanagement_175_UndeleteServiceResponseOut",
        "RubySettingsIn": "_servicemanagement_176_RubySettingsIn",
        "RubySettingsOut": "_servicemanagement_177_RubySettingsOut",
        "CustomErrorRuleIn": "_servicemanagement_178_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_servicemanagement_179_CustomErrorRuleOut",
        "MetricRuleIn": "_servicemanagement_180_MetricRuleIn",
        "MetricRuleOut": "_servicemanagement_181_MetricRuleOut",
        "MixinIn": "_servicemanagement_182_MixinIn",
        "MixinOut": "_servicemanagement_183_MixinOut",
        "BillingDestinationIn": "_servicemanagement_184_BillingDestinationIn",
        "BillingDestinationOut": "_servicemanagement_185_BillingDestinationOut",
        "ListServicesResponseIn": "_servicemanagement_186_ListServicesResponseIn",
        "ListServicesResponseOut": "_servicemanagement_187_ListServicesResponseOut",
        "AuthProviderIn": "_servicemanagement_188_AuthProviderIn",
        "AuthProviderOut": "_servicemanagement_189_AuthProviderOut",
        "MonitoringIn": "_servicemanagement_190_MonitoringIn",
        "MonitoringOut": "_servicemanagement_191_MonitoringOut",
        "PublishingIn": "_servicemanagement_192_PublishingIn",
        "PublishingOut": "_servicemanagement_193_PublishingOut",
        "AuditLogConfigIn": "_servicemanagement_194_AuditLogConfigIn",
        "AuditLogConfigOut": "_servicemanagement_195_AuditLogConfigOut",
        "ContextIn": "_servicemanagement_196_ContextIn",
        "ContextOut": "_servicemanagement_197_ContextOut",
        "CommonLanguageSettingsIn": "_servicemanagement_198_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_servicemanagement_199_CommonLanguageSettingsOut",
        "DocumentationIn": "_servicemanagement_200_DocumentationIn",
        "DocumentationOut": "_servicemanagement_201_DocumentationOut",
        "GenerateConfigReportRequestIn": "_servicemanagement_202_GenerateConfigReportRequestIn",
        "GenerateConfigReportRequestOut": "_servicemanagement_203_GenerateConfigReportRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["JwtLocationIn"] = t.struct(
        {
            "query": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
            "header": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "query": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
            "header": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "provided": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "provided": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["LogDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "freeTier": t.string().optional(),
            "maxLimit": t.string().optional(),
            "description": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "defaultLimit": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "freeTier": t.string().optional(),
            "maxLimit": t.string().optional(),
            "description": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "defaultLimit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["JavaSettingsIn"] = t.struct(
        {
            "libraryPackage": t.string().optional(),
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
        }
    ).named(renames["JavaSettingsIn"])
    types["JavaSettingsOut"] = t.struct(
        {
            "libraryPackage": t.string().optional(),
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JavaSettingsOut"])
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
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["TypeIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
            "requestTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "syntax": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "requestTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "syntax": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "type": t.string(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "type": t.string(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["ApiIn"] = t.struct(
        {
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "version": t.string().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "version": t.string().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["AuthenticationIn"] = t.struct(
        {
            "providers": t.array(t.proxy(renames["AuthProviderIn"])).optional(),
            "rules": t.array(t.proxy(renames["AuthenticationRuleIn"])).optional(),
        }
    ).named(renames["AuthenticationIn"])
    types["AuthenticationOut"] = t.struct(
        {
            "providers": t.array(t.proxy(renames["AuthProviderOut"])).optional(),
            "rules": t.array(t.proxy(renames["AuthenticationRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "post": t.string().optional(),
            "selector": t.string().optional(),
            "delete": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "patch": t.string().optional(),
            "body": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "put": t.string().optional(),
            "get": t.string().optional(),
            "responseBody": t.string().optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "post": t.string().optional(),
            "selector": t.string().optional(),
            "delete": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "patch": t.string().optional(),
            "body": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "put": t.string().optional(),
            "get": t.string().optional(),
            "responseBody": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["ConfigFileIn"] = t.struct(
        {
            "fileType": t.string().optional(),
            "filePath": t.string().optional(),
            "fileContents": t.string().optional(),
        }
    ).named(renames["ConfigFileIn"])
    types["ConfigFileOut"] = t.struct(
        {
            "fileType": t.string().optional(),
            "filePath": t.string().optional(),
            "fileContents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigFileOut"])
    types["ConfigChangeIn"] = t.struct(
        {
            "newValue": t.string().optional(),
            "oldValue": t.string().optional(),
            "element": t.string().optional(),
            "changeType": t.string().optional(),
            "advices": t.array(t.proxy(renames["AdviceIn"])).optional(),
        }
    ).named(renames["ConfigChangeIn"])
    types["ConfigChangeOut"] = t.struct(
        {
            "newValue": t.string().optional(),
            "oldValue": t.string().optional(),
            "element": t.string().optional(),
            "changeType": t.string().optional(),
            "advices": t.array(t.proxy(renames["AdviceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigChangeOut"])
    types["DeleteServiceStrategyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteServiceStrategyIn"]
    )
    types["DeleteServiceStrategyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteServiceStrategyOut"])
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
    types["UsageIn"] = t.struct(
        {
            "producerNotificationChannel": t.string().optional(),
            "rules": t.array(t.proxy(renames["UsageRuleIn"])).optional(),
            "requirements": t.array(t.string()).optional(),
        }
    ).named(renames["UsageIn"])
    types["UsageOut"] = t.struct(
        {
            "producerNotificationChannel": t.string().optional(),
            "rules": t.array(t.proxy(renames["UsageRuleOut"])).optional(),
            "requirements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageOut"])
    types["FieldIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "number": t.integer().optional(),
            "cardinality": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "typeUrl": t.string().optional(),
            "defaultValue": t.string().optional(),
            "jsonName": t.string().optional(),
            "name": t.string().optional(),
            "packed": t.boolean().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "number": t.integer().optional(),
            "cardinality": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "typeUrl": t.string().optional(),
            "defaultValue": t.string().optional(),
            "jsonName": t.string().optional(),
            "name": t.string().optional(),
            "packed": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["UsageRuleIn"] = t.struct(
        {
            "skipServiceControl": t.boolean().optional(),
            "allowUnregisteredCalls": t.boolean().optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["UsageRuleIn"])
    types["UsageRuleOut"] = t.struct(
        {
            "skipServiceControl": t.boolean().optional(),
            "allowUnregisteredCalls": t.boolean().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageRuleOut"])
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
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
    types["ChangeReportIn"] = t.struct(
        {"configChanges": t.array(t.proxy(renames["ConfigChangeIn"])).optional()}
    ).named(renames["ChangeReportIn"])
    types["ChangeReportOut"] = t.struct(
        {
            "configChanges": t.array(t.proxy(renames["ConfigChangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeReportOut"])
    types["SystemParameterRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "parameters": t.array(t.proxy(renames["SystemParameterIn"])).optional(),
        }
    ).named(renames["SystemParameterRuleIn"])
    types["SystemParameterRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "parameters": t.array(t.proxy(renames["SystemParameterOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParameterRuleOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["GenerateConfigReportResponseIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "id": t.string().optional(),
            "changeReports": t.array(t.proxy(renames["ChangeReportIn"])).optional(),
            "diagnostics": t.array(t.proxy(renames["DiagnosticIn"])).optional(),
        }
    ).named(renames["GenerateConfigReportResponseIn"])
    types["GenerateConfigReportResponseOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "id": t.string().optional(),
            "changeReports": t.array(t.proxy(renames["ChangeReportOut"])).optional(),
            "diagnostics": t.array(t.proxy(renames["DiagnosticOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GenerateConfigReportResponseOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
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
    types["EnumIn"] = t.struct(
        {
            "syntax": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "syntax": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["ListServiceConfigsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serviceConfigs": t.array(t.proxy(renames["ServiceIn"])).optional(),
        }
    ).named(renames["ListServiceConfigsResponseIn"])
    types["ListServiceConfigsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "serviceConfigs": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServiceConfigsResponseOut"])
    types["BackendRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "deadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "jwtAudience": t.string().optional(),
            "pathTranslation": t.string(),
            "disableAuth": t.boolean().optional(),
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "protocol": t.string().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "deadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "jwtAudience": t.string().optional(),
            "pathTranslation": t.string(),
            "disableAuth": t.boolean().optional(),
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "protocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["EnableServiceResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableServiceResponseIn"]
    )
    types["EnableServiceResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableServiceResponseOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
    types["ServiceIn"] = t.struct(
        {
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "name": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "producerProjectId": t.string().optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "id": t.string().optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "title": t.string().optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "configVersion": t.integer().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "name": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "producerProjectId": t.string().optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "id": t.string().optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "title": t.string().optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "configVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
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
    types["SubmitConfigSourceResponseIn"] = t.struct(
        {"serviceConfig": t.proxy(renames["ServiceIn"]).optional()}
    ).named(renames["SubmitConfigSourceResponseIn"])
    types["SubmitConfigSourceResponseOut"] = t.struct(
        {
            "serviceConfig": t.proxy(renames["ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitConfigSourceResponseOut"])
    types["AuthRequirementIn"] = t.struct(
        {"providerId": t.string().optional(), "audiences": t.string().optional()}
    ).named(renames["AuthRequirementIn"])
    types["AuthRequirementOut"] = t.struct(
        {
            "providerId": t.string().optional(),
            "audiences": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthRequirementOut"])
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
    types["AuthenticationRuleIn"] = t.struct(
        {
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
            "selector": t.string().optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "selector": t.string().optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "version": t.string().optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "version": t.string().optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
    types["QuotaIn"] = t.struct(
        {
            "metricRules": t.array(t.proxy(renames["MetricRuleIn"])).optional(),
            "limits": t.array(t.proxy(renames["QuotaLimitIn"])).optional(),
        }
    ).named(renames["QuotaIn"])
    types["QuotaOut"] = t.struct(
        {
            "metricRules": t.array(t.proxy(renames["MetricRuleOut"])).optional(),
            "limits": t.array(t.proxy(renames["QuotaLimitOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "description": t.string().optional(),
            "metricKind": t.string().optional(),
            "name": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "metricKind": t.string().optional(),
            "name": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["EndpointIn"] = t.struct(
        {
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["LabelDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "key": t.string().optional(),
        }
    ).named(renames["LabelDescriptorIn"])
    types["LabelDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelDescriptorOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["RolloutIn"] = t.struct(
        {
            "rolloutId": t.string().optional(),
            "status": t.string().optional(),
            "deleteServiceStrategy": t.proxy(
                renames["DeleteServiceStrategyIn"]
            ).optional(),
            "createdBy": t.string().optional(),
            "trafficPercentStrategy": t.proxy(
                renames["TrafficPercentStrategyIn"]
            ).optional(),
            "serviceName": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["RolloutIn"])
    types["RolloutOut"] = t.struct(
        {
            "rolloutId": t.string().optional(),
            "status": t.string().optional(),
            "deleteServiceStrategy": t.proxy(
                renames["DeleteServiceStrategyOut"]
            ).optional(),
            "createdBy": t.string().optional(),
            "trafficPercentStrategy": t.proxy(
                renames["TrafficPercentStrategyOut"]
            ).optional(),
            "serviceName": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
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
    types["EnumValueIn"] = t.struct(
        {
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "number": t.integer().optional(),
        }
    ).named(renames["EnumValueIn"])
    types["EnumValueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValueOut"])
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
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
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
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
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
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
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
    types["LongRunningIn"] = t.struct(
        {
            "pollDelayMultiplier": t.number().optional(),
            "totalPollTimeout": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "initialPollDelay": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "pollDelayMultiplier": t.number().optional(),
            "totalPollTimeout": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["UndeleteServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["ManagedServiceIn"]).optional()}
    ).named(renames["UndeleteServiceResponseIn"])
    types["UndeleteServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["ManagedServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteServiceResponseOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
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
    types["MetricRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "metricCosts": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["MetricRuleIn"])
    types["MetricRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "metricCosts": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricRuleOut"])
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
    types["BillingDestinationIn"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "monitoredResource": t.string().optional(),
        }
    ).named(renames["BillingDestinationIn"])
    types["BillingDestinationOut"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "monitoredResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingDestinationOut"])
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
    types["AuthProviderIn"] = t.struct(
        {
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "audiences": t.string().optional(),
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "authorizationUrl": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "audiences": t.string().optional(),
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
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
            "newIssueUri": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "apiShortName": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "githubLabel": t.string().optional(),
            "documentationUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "docTagPrefix": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "newIssueUri": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "apiShortName": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "githubLabel": t.string().optional(),
            "documentationUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "docTagPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
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
    types["DocumentationIn"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
            "sectionOverrides": t.array(t.proxy(renames["PageIn"])).optional(),
            "overview": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
            "sectionOverrides": t.array(t.proxy(renames["PageOut"])).optional(),
            "overview": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
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

    functions = {}
    functions["operationsGet"] = servicemanagement.get(
        "v1/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
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
    functions["servicesRolloutsList"] = servicemanagement.get(
        "v1/services/{serviceName}/rollouts/{rolloutId}",
        t.struct(
            {
                "rolloutId": t.string(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RolloutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesRolloutsCreate"] = servicemanagement.get(
        "v1/services/{serviceName}/rollouts/{rolloutId}",
        t.struct(
            {
                "rolloutId": t.string(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RolloutOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesRolloutsGet"] = servicemanagement.get(
        "v1/services/{serviceName}/rollouts/{rolloutId}",
        t.struct(
            {
                "rolloutId": t.string(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["RolloutOut"]),
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

    return Import(
        importer="servicemanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
