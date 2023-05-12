from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_servicemanagement() -> Import:
    servicemanagement = HTTPRuntime("https://servicemanagement.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicemanagement_1_ErrorResponse",
        "PublishingIn": "_servicemanagement_2_PublishingIn",
        "PublishingOut": "_servicemanagement_3_PublishingOut",
        "ListServiceConfigsResponseIn": "_servicemanagement_4_ListServiceConfigsResponseIn",
        "ListServiceConfigsResponseOut": "_servicemanagement_5_ListServiceConfigsResponseOut",
        "BackendIn": "_servicemanagement_6_BackendIn",
        "BackendOut": "_servicemanagement_7_BackendOut",
        "GoSettingsIn": "_servicemanagement_8_GoSettingsIn",
        "GoSettingsOut": "_servicemanagement_9_GoSettingsOut",
        "JavaSettingsIn": "_servicemanagement_10_JavaSettingsIn",
        "JavaSettingsOut": "_servicemanagement_11_JavaSettingsOut",
        "DeleteServiceStrategyIn": "_servicemanagement_12_DeleteServiceStrategyIn",
        "DeleteServiceStrategyOut": "_servicemanagement_13_DeleteServiceStrategyOut",
        "OptionIn": "_servicemanagement_14_OptionIn",
        "OptionOut": "_servicemanagement_15_OptionOut",
        "AdviceIn": "_servicemanagement_16_AdviceIn",
        "AdviceOut": "_servicemanagement_17_AdviceOut",
        "ResourceReferenceIn": "_servicemanagement_18_ResourceReferenceIn",
        "ResourceReferenceOut": "_servicemanagement_19_ResourceReferenceOut",
        "AuthProviderIn": "_servicemanagement_20_AuthProviderIn",
        "AuthProviderOut": "_servicemanagement_21_AuthProviderOut",
        "AuditLogConfigIn": "_servicemanagement_22_AuditLogConfigIn",
        "AuditLogConfigOut": "_servicemanagement_23_AuditLogConfigOut",
        "EnumValueIn": "_servicemanagement_24_EnumValueIn",
        "EnumValueOut": "_servicemanagement_25_EnumValueOut",
        "SourceContextIn": "_servicemanagement_26_SourceContextIn",
        "SourceContextOut": "_servicemanagement_27_SourceContextOut",
        "OperationMetadataIn": "_servicemanagement_28_OperationMetadataIn",
        "OperationMetadataOut": "_servicemanagement_29_OperationMetadataOut",
        "PythonSettingsIn": "_servicemanagement_30_PythonSettingsIn",
        "PythonSettingsOut": "_servicemanagement_31_PythonSettingsOut",
        "BindingIn": "_servicemanagement_32_BindingIn",
        "BindingOut": "_servicemanagement_33_BindingOut",
        "TestIamPermissionsRequestIn": "_servicemanagement_34_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_servicemanagement_35_TestIamPermissionsRequestOut",
        "FieldIn": "_servicemanagement_36_FieldIn",
        "FieldOut": "_servicemanagement_37_FieldOut",
        "QuotaLimitIn": "_servicemanagement_38_QuotaLimitIn",
        "QuotaLimitOut": "_servicemanagement_39_QuotaLimitOut",
        "RubySettingsIn": "_servicemanagement_40_RubySettingsIn",
        "RubySettingsOut": "_servicemanagement_41_RubySettingsOut",
        "BillingDestinationIn": "_servicemanagement_42_BillingDestinationIn",
        "BillingDestinationOut": "_servicemanagement_43_BillingDestinationOut",
        "EnableServiceResponseIn": "_servicemanagement_44_EnableServiceResponseIn",
        "EnableServiceResponseOut": "_servicemanagement_45_EnableServiceResponseOut",
        "HttpRuleIn": "_servicemanagement_46_HttpRuleIn",
        "HttpRuleOut": "_servicemanagement_47_HttpRuleOut",
        "CustomErrorRuleIn": "_servicemanagement_48_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_servicemanagement_49_CustomErrorRuleOut",
        "SystemParameterIn": "_servicemanagement_50_SystemParameterIn",
        "SystemParameterOut": "_servicemanagement_51_SystemParameterOut",
        "EnumIn": "_servicemanagement_52_EnumIn",
        "EnumOut": "_servicemanagement_53_EnumOut",
        "RolloutIn": "_servicemanagement_54_RolloutIn",
        "RolloutOut": "_servicemanagement_55_RolloutOut",
        "ServiceIn": "_servicemanagement_56_ServiceIn",
        "ServiceOut": "_servicemanagement_57_ServiceOut",
        "EndpointIn": "_servicemanagement_58_EndpointIn",
        "EndpointOut": "_servicemanagement_59_EndpointOut",
        "CustomHttpPatternIn": "_servicemanagement_60_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_servicemanagement_61_CustomHttpPatternOut",
        "AuthRequirementIn": "_servicemanagement_62_AuthRequirementIn",
        "AuthRequirementOut": "_servicemanagement_63_AuthRequirementOut",
        "CommonLanguageSettingsIn": "_servicemanagement_64_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_servicemanagement_65_CommonLanguageSettingsOut",
        "HttpIn": "_servicemanagement_66_HttpIn",
        "HttpOut": "_servicemanagement_67_HttpOut",
        "LabelDescriptorIn": "_servicemanagement_68_LabelDescriptorIn",
        "LabelDescriptorOut": "_servicemanagement_69_LabelDescriptorOut",
        "CustomErrorIn": "_servicemanagement_70_CustomErrorIn",
        "CustomErrorOut": "_servicemanagement_71_CustomErrorOut",
        "OperationInfoIn": "_servicemanagement_72_OperationInfoIn",
        "OperationInfoOut": "_servicemanagement_73_OperationInfoOut",
        "PageIn": "_servicemanagement_74_PageIn",
        "PageOut": "_servicemanagement_75_PageOut",
        "SystemParametersIn": "_servicemanagement_76_SystemParametersIn",
        "SystemParametersOut": "_servicemanagement_77_SystemParametersOut",
        "ListServiceRolloutsResponseIn": "_servicemanagement_78_ListServiceRolloutsResponseIn",
        "ListServiceRolloutsResponseOut": "_servicemanagement_79_ListServiceRolloutsResponseOut",
        "NodeSettingsIn": "_servicemanagement_80_NodeSettingsIn",
        "NodeSettingsOut": "_servicemanagement_81_NodeSettingsOut",
        "ManagedServiceIn": "_servicemanagement_82_ManagedServiceIn",
        "ManagedServiceOut": "_servicemanagement_83_ManagedServiceOut",
        "ClientLibrarySettingsIn": "_servicemanagement_84_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_servicemanagement_85_ClientLibrarySettingsOut",
        "FlowErrorDetailsIn": "_servicemanagement_86_FlowErrorDetailsIn",
        "FlowErrorDetailsOut": "_servicemanagement_87_FlowErrorDetailsOut",
        "StatusIn": "_servicemanagement_88_StatusIn",
        "StatusOut": "_servicemanagement_89_StatusOut",
        "MethodIn": "_servicemanagement_90_MethodIn",
        "MethodOut": "_servicemanagement_91_MethodOut",
        "DocumentationIn": "_servicemanagement_92_DocumentationIn",
        "DocumentationOut": "_servicemanagement_93_DocumentationOut",
        "ConfigFileIn": "_servicemanagement_94_ConfigFileIn",
        "ConfigFileOut": "_servicemanagement_95_ConfigFileOut",
        "UndeleteServiceResponseIn": "_servicemanagement_96_UndeleteServiceResponseIn",
        "UndeleteServiceResponseOut": "_servicemanagement_97_UndeleteServiceResponseOut",
        "ConfigRefIn": "_servicemanagement_98_ConfigRefIn",
        "ConfigRefOut": "_servicemanagement_99_ConfigRefOut",
        "QuotaIn": "_servicemanagement_100_QuotaIn",
        "QuotaOut": "_servicemanagement_101_QuotaOut",
        "TestIamPermissionsResponseIn": "_servicemanagement_102_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_servicemanagement_103_TestIamPermissionsResponseOut",
        "BackendRuleIn": "_servicemanagement_104_BackendRuleIn",
        "BackendRuleOut": "_servicemanagement_105_BackendRuleOut",
        "UsageIn": "_servicemanagement_106_UsageIn",
        "UsageOut": "_servicemanagement_107_UsageOut",
        "ConfigChangeIn": "_servicemanagement_108_ConfigChangeIn",
        "ConfigChangeOut": "_servicemanagement_109_ConfigChangeOut",
        "AuthenticationRuleIn": "_servicemanagement_110_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_servicemanagement_111_AuthenticationRuleOut",
        "MetricRuleIn": "_servicemanagement_112_MetricRuleIn",
        "MetricRuleOut": "_servicemanagement_113_MetricRuleOut",
        "MonitoringIn": "_servicemanagement_114_MonitoringIn",
        "MonitoringOut": "_servicemanagement_115_MonitoringOut",
        "ListServicesResponseIn": "_servicemanagement_116_ListServicesResponseIn",
        "ListServicesResponseOut": "_servicemanagement_117_ListServicesResponseOut",
        "LongRunningIn": "_servicemanagement_118_LongRunningIn",
        "LongRunningOut": "_servicemanagement_119_LongRunningOut",
        "ContextRuleIn": "_servicemanagement_120_ContextRuleIn",
        "ContextRuleOut": "_servicemanagement_121_ContextRuleOut",
        "SubmitConfigSourceRequestIn": "_servicemanagement_122_SubmitConfigSourceRequestIn",
        "SubmitConfigSourceRequestOut": "_servicemanagement_123_SubmitConfigSourceRequestOut",
        "TypeIn": "_servicemanagement_124_TypeIn",
        "TypeOut": "_servicemanagement_125_TypeOut",
        "MonitoringDestinationIn": "_servicemanagement_126_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_servicemanagement_127_MonitoringDestinationOut",
        "DiagnosticIn": "_servicemanagement_128_DiagnosticIn",
        "DiagnosticOut": "_servicemanagement_129_DiagnosticOut",
        "ListOperationsResponseIn": "_servicemanagement_130_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_servicemanagement_131_ListOperationsResponseOut",
        "BillingIn": "_servicemanagement_132_BillingIn",
        "BillingOut": "_servicemanagement_133_BillingOut",
        "ApiIn": "_servicemanagement_134_ApiIn",
        "ApiOut": "_servicemanagement_135_ApiOut",
        "GenerateConfigReportResponseIn": "_servicemanagement_136_GenerateConfigReportResponseIn",
        "GenerateConfigReportResponseOut": "_servicemanagement_137_GenerateConfigReportResponseOut",
        "LoggingIn": "_servicemanagement_138_LoggingIn",
        "LoggingOut": "_servicemanagement_139_LoggingOut",
        "DotnetSettingsIn": "_servicemanagement_140_DotnetSettingsIn",
        "DotnetSettingsOut": "_servicemanagement_141_DotnetSettingsOut",
        "MethodSettingsIn": "_servicemanagement_142_MethodSettingsIn",
        "MethodSettingsOut": "_servicemanagement_143_MethodSettingsOut",
        "AuditConfigIn": "_servicemanagement_144_AuditConfigIn",
        "AuditConfigOut": "_servicemanagement_145_AuditConfigOut",
        "ControlIn": "_servicemanagement_146_ControlIn",
        "ControlOut": "_servicemanagement_147_ControlOut",
        "SourceInfoIn": "_servicemanagement_148_SourceInfoIn",
        "SourceInfoOut": "_servicemanagement_149_SourceInfoOut",
        "ConfigSourceIn": "_servicemanagement_150_ConfigSourceIn",
        "ConfigSourceOut": "_servicemanagement_151_ConfigSourceOut",
        "GetIamPolicyRequestIn": "_servicemanagement_152_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_servicemanagement_153_GetIamPolicyRequestOut",
        "CppSettingsIn": "_servicemanagement_154_CppSettingsIn",
        "CppSettingsOut": "_servicemanagement_155_CppSettingsOut",
        "MetricDescriptorMetadataIn": "_servicemanagement_156_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_servicemanagement_157_MetricDescriptorMetadataOut",
        "LoggingDestinationIn": "_servicemanagement_158_LoggingDestinationIn",
        "LoggingDestinationOut": "_servicemanagement_159_LoggingDestinationOut",
        "GenerateConfigReportRequestIn": "_servicemanagement_160_GenerateConfigReportRequestIn",
        "GenerateConfigReportRequestOut": "_servicemanagement_161_GenerateConfigReportRequestOut",
        "UsageRuleIn": "_servicemanagement_162_UsageRuleIn",
        "UsageRuleOut": "_servicemanagement_163_UsageRuleOut",
        "PhpSettingsIn": "_servicemanagement_164_PhpSettingsIn",
        "PhpSettingsOut": "_servicemanagement_165_PhpSettingsOut",
        "OAuthRequirementsIn": "_servicemanagement_166_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_servicemanagement_167_OAuthRequirementsOut",
        "GetPolicyOptionsIn": "_servicemanagement_168_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_servicemanagement_169_GetPolicyOptionsOut",
        "JwtLocationIn": "_servicemanagement_170_JwtLocationIn",
        "JwtLocationOut": "_servicemanagement_171_JwtLocationOut",
        "MonitoredResourceDescriptorIn": "_servicemanagement_172_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_servicemanagement_173_MonitoredResourceDescriptorOut",
        "StepIn": "_servicemanagement_174_StepIn",
        "StepOut": "_servicemanagement_175_StepOut",
        "DocumentationRuleIn": "_servicemanagement_176_DocumentationRuleIn",
        "DocumentationRuleOut": "_servicemanagement_177_DocumentationRuleOut",
        "PolicyIn": "_servicemanagement_178_PolicyIn",
        "PolicyOut": "_servicemanagement_179_PolicyOut",
        "AuthenticationIn": "_servicemanagement_180_AuthenticationIn",
        "AuthenticationOut": "_servicemanagement_181_AuthenticationOut",
        "MixinIn": "_servicemanagement_182_MixinIn",
        "MixinOut": "_servicemanagement_183_MixinOut",
        "SystemParameterRuleIn": "_servicemanagement_184_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_servicemanagement_185_SystemParameterRuleOut",
        "ExprIn": "_servicemanagement_186_ExprIn",
        "ExprOut": "_servicemanagement_187_ExprOut",
        "SubmitConfigSourceResponseIn": "_servicemanagement_188_SubmitConfigSourceResponseIn",
        "SubmitConfigSourceResponseOut": "_servicemanagement_189_SubmitConfigSourceResponseOut",
        "ChangeReportIn": "_servicemanagement_190_ChangeReportIn",
        "ChangeReportOut": "_servicemanagement_191_ChangeReportOut",
        "TrafficPercentStrategyIn": "_servicemanagement_192_TrafficPercentStrategyIn",
        "TrafficPercentStrategyOut": "_servicemanagement_193_TrafficPercentStrategyOut",
        "LogDescriptorIn": "_servicemanagement_194_LogDescriptorIn",
        "LogDescriptorOut": "_servicemanagement_195_LogDescriptorOut",
        "OperationIn": "_servicemanagement_196_OperationIn",
        "OperationOut": "_servicemanagement_197_OperationOut",
        "ContextIn": "_servicemanagement_198_ContextIn",
        "ContextOut": "_servicemanagement_199_ContextOut",
        "MetricDescriptorIn": "_servicemanagement_200_MetricDescriptorIn",
        "MetricDescriptorOut": "_servicemanagement_201_MetricDescriptorOut",
        "SetIamPolicyRequestIn": "_servicemanagement_202_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_servicemanagement_203_SetIamPolicyRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PublishingIn"] = t.struct(
        {
            "docTagPrefix": t.string().optional(),
            "organization": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "apiShortName": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "githubLabel": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "documentationUri": t.string().optional(),
            "newIssueUri": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "docTagPrefix": t.string().optional(),
            "organization": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "apiShortName": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "githubLabel": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "documentationUri": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
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
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["JavaSettingsIn"] = t.struct(
        {
            "libraryPackage": t.string().optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["JavaSettingsIn"])
    types["JavaSettingsOut"] = t.struct(
        {
            "libraryPackage": t.string().optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JavaSettingsOut"])
    types["DeleteServiceStrategyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteServiceStrategyIn"]
    )
    types["DeleteServiceStrategyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteServiceStrategyOut"])
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
    types["AdviceIn"] = t.struct({"description": t.string().optional()}).named(
        renames["AdviceIn"]
    )
    types["AdviceOut"] = t.struct(
        {
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdviceOut"])
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
    types["AuthProviderIn"] = t.struct(
        {
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "id": t.string().optional(),
            "jwksUri": t.string().optional(),
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "id": t.string().optional(),
            "jwksUri": t.string().optional(),
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
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
    types["EnumValueIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
            "number": t.integer().optional(),
        }
    ).named(renames["EnumValueIn"])
    types["EnumValueOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValueOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "progressPercentage": t.integer().optional(),
            "steps": t.array(t.proxy(renames["StepIn"])).optional(),
            "startTime": t.string().optional(),
            "resourceNames": t.array(t.string()).optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "progressPercentage": t.integer().optional(),
            "steps": t.array(t.proxy(renames["StepOut"])).optional(),
            "startTime": t.string().optional(),
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["FieldIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
            "jsonName": t.string().optional(),
            "kind": t.string().optional(),
            "number": t.integer().optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "cardinality": t.string().optional(),
            "defaultValue": t.string().optional(),
            "oneofIndex": t.integer().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "jsonName": t.string().optional(),
            "kind": t.string().optional(),
            "number": t.integer().optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "cardinality": t.string().optional(),
            "defaultValue": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "unit": t.string().optional(),
            "maxLimit": t.string().optional(),
            "freeTier": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "unit": t.string().optional(),
            "maxLimit": t.string().optional(),
            "freeTier": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
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
    types["EnableServiceResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableServiceResponseIn"]
    )
    types["EnableServiceResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableServiceResponseOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "body": t.string().optional(),
            "selector": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "post": t.string().optional(),
            "delete": t.string().optional(),
            "put": t.string().optional(),
            "patch": t.string().optional(),
            "get": t.string().optional(),
            "responseBody": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "body": t.string().optional(),
            "selector": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "post": t.string().optional(),
            "delete": t.string().optional(),
            "put": t.string().optional(),
            "patch": t.string().optional(),
            "get": t.string().optional(),
            "responseBody": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["CustomErrorRuleIn"] = t.struct(
        {"isErrorType": t.boolean().optional(), "selector": t.string().optional()}
    ).named(renames["CustomErrorRuleIn"])
    types["CustomErrorRuleOut"] = t.struct(
        {
            "isErrorType": t.boolean().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomErrorRuleOut"])
    types["SystemParameterIn"] = t.struct(
        {
            "urlQueryParameter": t.string().optional(),
            "httpHeader": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SystemParameterIn"])
    types["SystemParameterOut"] = t.struct(
        {
            "urlQueryParameter": t.string().optional(),
            "httpHeader": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParameterOut"])
    types["EnumIn"] = t.struct(
        {
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["RolloutIn"] = t.struct(
        {
            "trafficPercentStrategy": t.proxy(
                renames["TrafficPercentStrategyIn"]
            ).optional(),
            "deleteServiceStrategy": t.proxy(
                renames["DeleteServiceStrategyIn"]
            ).optional(),
            "rolloutId": t.string().optional(),
            "createdBy": t.string().optional(),
            "createTime": t.string().optional(),
            "status": t.string().optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["RolloutIn"])
    types["RolloutOut"] = t.struct(
        {
            "trafficPercentStrategy": t.proxy(
                renames["TrafficPercentStrategyOut"]
            ).optional(),
            "deleteServiceStrategy": t.proxy(
                renames["DeleteServiceStrategyOut"]
            ).optional(),
            "rolloutId": t.string().optional(),
            "createdBy": t.string().optional(),
            "createTime": t.string().optional(),
            "status": t.string().optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RolloutOut"])
    types["ServiceIn"] = t.struct(
        {
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "id": t.string().optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "producerProjectId": t.string().optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "configVersion": t.integer().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "name": t.string().optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "title": t.string().optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "id": t.string().optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "producerProjectId": t.string().optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "configVersion": t.integer().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "name": t.string().optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "title": t.string().optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["EndpointIn"] = t.struct(
        {
            "name": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "target": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "name": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "target": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["LabelDescriptorIn"] = t.struct(
        {
            "valueType": t.string().optional(),
            "key": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LabelDescriptorIn"])
    types["LabelDescriptorOut"] = t.struct(
        {
            "valueType": t.string().optional(),
            "key": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelDescriptorOut"])
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
    types["PageIn"] = t.struct(
        {
            "subpages": t.array(t.proxy(renames["PageIn"])).optional(),
            "content": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "subpages": t.array(t.proxy(renames["PageOut"])).optional(),
            "content": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
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
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
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
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "version": t.string().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "version": t.string().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
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
    types["MethodIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "requestTypeUrl": t.string().optional(),
            "syntax": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "requestTypeUrl": t.string().optional(),
            "syntax": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["DocumentationIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "overview": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["ConfigFileIn"] = t.struct(
        {
            "filePath": t.string().optional(),
            "fileType": t.string().optional(),
            "fileContents": t.string().optional(),
        }
    ).named(renames["ConfigFileIn"])
    types["ConfigFileOut"] = t.struct(
        {
            "filePath": t.string().optional(),
            "fileType": t.string().optional(),
            "fileContents": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigFileOut"])
    types["UndeleteServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["ManagedServiceIn"]).optional()}
    ).named(renames["UndeleteServiceResponseIn"])
    types["UndeleteServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["ManagedServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UndeleteServiceResponseOut"])
    types["ConfigRefIn"] = t.struct({"name": t.string().optional()}).named(
        renames["ConfigRefIn"]
    )
    types["ConfigRefOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigRefOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["BackendRuleIn"] = t.struct(
        {
            "address": t.string().optional(),
            "jwtAudience": t.string().optional(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "operationDeadline": t.number().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "pathTranslation": t.string(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "address": t.string().optional(),
            "jwtAudience": t.string().optional(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "operationDeadline": t.number().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "pathTranslation": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["UsageIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["UsageRuleIn"])).optional(),
            "requirements": t.array(t.string()).optional(),
            "producerNotificationChannel": t.string().optional(),
        }
    ).named(renames["UsageIn"])
    types["UsageOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["UsageRuleOut"])).optional(),
            "requirements": t.array(t.string()).optional(),
            "producerNotificationChannel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageOut"])
    types["ConfigChangeIn"] = t.struct(
        {
            "oldValue": t.string().optional(),
            "newValue": t.string().optional(),
            "element": t.string().optional(),
            "advices": t.array(t.proxy(renames["AdviceIn"])).optional(),
            "changeType": t.string().optional(),
        }
    ).named(renames["ConfigChangeIn"])
    types["ConfigChangeOut"] = t.struct(
        {
            "oldValue": t.string().optional(),
            "newValue": t.string().optional(),
            "element": t.string().optional(),
            "advices": t.array(t.proxy(renames["AdviceOut"])).optional(),
            "changeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigChangeOut"])
    types["AuthenticationRuleIn"] = t.struct(
        {
            "allowWithoutCredential": t.boolean().optional(),
            "selector": t.string().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "allowWithoutCredential": t.boolean().optional(),
            "selector": t.string().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
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
    types["ListServicesResponseIn"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ManagedServiceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ManagedServiceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["LongRunningIn"] = t.struct(
        {
            "pollDelayMultiplier": t.number().optional(),
            "initialPollDelay": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "pollDelayMultiplier": t.number().optional(),
            "initialPollDelay": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "requested": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "requested": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
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
    types["TypeIn"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "oneofs": t.array(t.string()).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "oneofs": t.array(t.string()).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["DiagnosticIn"] = t.struct(
        {
            "message": t.string().optional(),
            "location": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["DiagnosticIn"])
    types["DiagnosticOut"] = t.struct(
        {
            "message": t.string().optional(),
            "location": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiagnosticOut"])
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
    types["ApiIn"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "version": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "version": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
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
    types["DotnetSettingsIn"] = t.struct(
        {
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
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
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "ingestDelay": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
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
    types["GenerateConfigReportRequestIn"] = t.struct(
        {
            "oldConfig": t.struct({"_": t.string().optional()}).optional(),
            "newConfig": t.struct({"_": t.string().optional()}),
        }
    ).named(renames["GenerateConfigReportRequestIn"])
    types["GenerateConfigReportRequestOut"] = t.struct(
        {
            "oldConfig": t.struct({"_": t.string().optional()}).optional(),
            "newConfig": t.struct({"_": t.string().optional()}),
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
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["JwtLocationIn"] = t.struct(
        {
            "header": t.string().optional(),
            "query": t.string().optional(),
            "cookie": t.string().optional(),
            "valuePrefix": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "header": t.string().optional(),
            "query": t.string().optional(),
            "cookie": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "description": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["StepIn"] = t.struct(
        {"description": t.string().optional(), "status": t.string().optional()}
    ).named(renames["StepIn"])
    types["StepOut"] = t.struct(
        {
            "description": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StepOut"])
    types["DocumentationRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "description": t.string().optional(),
            "deprecationDescription": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "description": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
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
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["SubmitConfigSourceResponseIn"] = t.struct(
        {"serviceConfig": t.proxy(renames["ServiceIn"]).optional()}
    ).named(renames["SubmitConfigSourceResponseIn"])
    types["SubmitConfigSourceResponseOut"] = t.struct(
        {
            "serviceConfig": t.proxy(renames["ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitConfigSourceResponseOut"])
    types["ChangeReportIn"] = t.struct(
        {"configChanges": t.array(t.proxy(renames["ConfigChangeIn"])).optional()}
    ).named(renames["ChangeReportIn"])
    types["ChangeReportOut"] = t.struct(
        {
            "configChanges": t.array(t.proxy(renames["ConfigChangeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChangeReportOut"])
    types["TrafficPercentStrategyIn"] = t.struct(
        {"percentages": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["TrafficPercentStrategyIn"])
    types["TrafficPercentStrategyOut"] = t.struct(
        {
            "percentages": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficPercentStrategyOut"])
    types["LogDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "launchStage": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "launchStage": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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

    functions = {}
    functions["servicesGenerateConfigReport"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesSetIamPolicy"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTestIamPermissions"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDelete"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGetIamPolicy"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesUndelete"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesCreate"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGetConfig"] = servicemanagement.get(
        "v1/services/{serviceName}/config",
        t.struct(
            {
                "configId": t.string(),
                "view": t.string().optional(),
                "serviceName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConfigsList"] = servicemanagement.post(
        "v1/services/{serviceName}/configs:submit",
        t.struct(
            {
                "serviceName": t.string(),
                "configSource": t.proxy(renames["ConfigSourceIn"]),
                "validateOnly": t.boolean().optional(),
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
                "configSource": t.proxy(renames["ConfigSourceIn"]),
                "validateOnly": t.boolean().optional(),
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
                "configSource": t.proxy(renames["ConfigSourceIn"]),
                "validateOnly": t.boolean().optional(),
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
                "configSource": t.proxy(renames["ConfigSourceIn"]),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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

    return Import(
        importer="servicemanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
