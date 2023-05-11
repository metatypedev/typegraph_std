from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_serviceusage() -> Import:
    serviceusage = HTTPRuntime("https://serviceusage.googleapis.com/")

    renames = {
        "ErrorResponse": "_serviceusage_1_ErrorResponse",
        "AuthRequirementIn": "_serviceusage_2_AuthRequirementIn",
        "AuthRequirementOut": "_serviceusage_3_AuthRequirementOut",
        "SourceContextIn": "_serviceusage_4_SourceContextIn",
        "SourceContextOut": "_serviceusage_5_SourceContextOut",
        "QuotaIn": "_serviceusage_6_QuotaIn",
        "QuotaOut": "_serviceusage_7_QuotaOut",
        "CppSettingsIn": "_serviceusage_8_CppSettingsIn",
        "CppSettingsOut": "_serviceusage_9_CppSettingsOut",
        "QuotaLimitIn": "_serviceusage_10_QuotaLimitIn",
        "QuotaLimitOut": "_serviceusage_11_QuotaLimitOut",
        "SystemParameterRuleIn": "_serviceusage_12_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_serviceusage_13_SystemParameterRuleOut",
        "MixinIn": "_serviceusage_14_MixinIn",
        "MixinOut": "_serviceusage_15_MixinOut",
        "ImportAdminQuotaPoliciesMetadataIn": "_serviceusage_16_ImportAdminQuotaPoliciesMetadataIn",
        "ImportAdminQuotaPoliciesMetadataOut": "_serviceusage_17_ImportAdminQuotaPoliciesMetadataOut",
        "ImportConsumerOverridesResponseIn": "_serviceusage_18_ImportConsumerOverridesResponseIn",
        "ImportConsumerOverridesResponseOut": "_serviceusage_19_ImportConsumerOverridesResponseOut",
        "ImportAdminOverridesMetadataIn": "_serviceusage_20_ImportAdminOverridesMetadataIn",
        "ImportAdminOverridesMetadataOut": "_serviceusage_21_ImportAdminOverridesMetadataOut",
        "GoSettingsIn": "_serviceusage_22_GoSettingsIn",
        "GoSettingsOut": "_serviceusage_23_GoSettingsOut",
        "OperationMetadataIn": "_serviceusage_24_OperationMetadataIn",
        "OperationMetadataOut": "_serviceusage_25_OperationMetadataOut",
        "SourceInfoIn": "_serviceusage_26_SourceInfoIn",
        "SourceInfoOut": "_serviceusage_27_SourceInfoOut",
        "ApiIn": "_serviceusage_28_ApiIn",
        "ApiOut": "_serviceusage_29_ApiOut",
        "ContextIn": "_serviceusage_30_ContextIn",
        "ContextOut": "_serviceusage_31_ContextOut",
        "CustomErrorIn": "_serviceusage_32_CustomErrorIn",
        "CustomErrorOut": "_serviceusage_33_CustomErrorOut",
        "LoggingDestinationIn": "_serviceusage_34_LoggingDestinationIn",
        "LoggingDestinationOut": "_serviceusage_35_LoggingDestinationOut",
        "DisableServiceRequestIn": "_serviceusage_36_DisableServiceRequestIn",
        "DisableServiceRequestOut": "_serviceusage_37_DisableServiceRequestOut",
        "ValueInfoIn": "_serviceusage_38_ValueInfoIn",
        "ValueInfoOut": "_serviceusage_39_ValueInfoOut",
        "EnumValueIn": "_serviceusage_40_EnumValueIn",
        "EnumValueOut": "_serviceusage_41_EnumValueOut",
        "CreateAdminQuotaPolicyMetadataIn": "_serviceusage_42_CreateAdminQuotaPolicyMetadataIn",
        "CreateAdminQuotaPolicyMetadataOut": "_serviceusage_43_CreateAdminQuotaPolicyMetadataOut",
        "GetServiceIdentityResponseIn": "_serviceusage_44_GetServiceIdentityResponseIn",
        "GetServiceIdentityResponseOut": "_serviceusage_45_GetServiceIdentityResponseOut",
        "RemoveEnableRulesResponseIn": "_serviceusage_46_RemoveEnableRulesResponseIn",
        "RemoveEnableRulesResponseOut": "_serviceusage_47_RemoveEnableRulesResponseOut",
        "MetricRuleIn": "_serviceusage_48_MetricRuleIn",
        "MetricRuleOut": "_serviceusage_49_MetricRuleOut",
        "AuthenticationIn": "_serviceusage_50_AuthenticationIn",
        "AuthenticationOut": "_serviceusage_51_AuthenticationOut",
        "GoogleApiServiceusageV1OperationMetadataIn": "_serviceusage_52_GoogleApiServiceusageV1OperationMetadataIn",
        "GoogleApiServiceusageV1OperationMetadataOut": "_serviceusage_53_GoogleApiServiceusageV1OperationMetadataOut",
        "MetricDescriptorIn": "_serviceusage_54_MetricDescriptorIn",
        "MetricDescriptorOut": "_serviceusage_55_MetricDescriptorOut",
        "RemoveEnableRulesMetadataIn": "_serviceusage_56_RemoveEnableRulesMetadataIn",
        "RemoveEnableRulesMetadataOut": "_serviceusage_57_RemoveEnableRulesMetadataOut",
        "BatchEnableServicesRequestIn": "_serviceusage_58_BatchEnableServicesRequestIn",
        "BatchEnableServicesRequestOut": "_serviceusage_59_BatchEnableServicesRequestOut",
        "EnableRuleIn": "_serviceusage_60_EnableRuleIn",
        "EnableRuleOut": "_serviceusage_61_EnableRuleOut",
        "DocumentationRuleIn": "_serviceusage_62_DocumentationRuleIn",
        "DocumentationRuleOut": "_serviceusage_63_DocumentationRuleOut",
        "ListOperationsResponseIn": "_serviceusage_64_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_serviceusage_65_ListOperationsResponseOut",
        "MethodIn": "_serviceusage_66_MethodIn",
        "MethodOut": "_serviceusage_67_MethodOut",
        "EmptyIn": "_serviceusage_68_EmptyIn",
        "EmptyOut": "_serviceusage_69_EmptyOut",
        "GroupValueIn": "_serviceusage_70_GroupValueIn",
        "GroupValueOut": "_serviceusage_71_GroupValueOut",
        "AddEnableRulesMetadataIn": "_serviceusage_72_AddEnableRulesMetadataIn",
        "AddEnableRulesMetadataOut": "_serviceusage_73_AddEnableRulesMetadataOut",
        "EnableFailureIn": "_serviceusage_74_EnableFailureIn",
        "EnableFailureOut": "_serviceusage_75_EnableFailureOut",
        "ClientLibrarySettingsIn": "_serviceusage_76_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_serviceusage_77_ClientLibrarySettingsOut",
        "UpdateAdminQuotaPolicyMetadataIn": "_serviceusage_78_UpdateAdminQuotaPolicyMetadataIn",
        "UpdateAdminQuotaPolicyMetadataOut": "_serviceusage_79_UpdateAdminQuotaPolicyMetadataOut",
        "CustomErrorRuleIn": "_serviceusage_80_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_serviceusage_81_CustomErrorRuleOut",
        "MonitoringDestinationIn": "_serviceusage_82_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_serviceusage_83_MonitoringDestinationOut",
        "UsageRuleIn": "_serviceusage_84_UsageRuleIn",
        "UsageRuleOut": "_serviceusage_85_UsageRuleOut",
        "EnableServiceResponseIn": "_serviceusage_86_EnableServiceResponseIn",
        "EnableServiceResponseOut": "_serviceusage_87_EnableServiceResponseOut",
        "CommonLanguageSettingsIn": "_serviceusage_88_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_serviceusage_89_CommonLanguageSettingsOut",
        "PageIn": "_serviceusage_90_PageIn",
        "PageOut": "_serviceusage_91_PageOut",
        "BatchCreateConsumerOverridesResponseIn": "_serviceusage_92_BatchCreateConsumerOverridesResponseIn",
        "BatchCreateConsumerOverridesResponseOut": "_serviceusage_93_BatchCreateConsumerOverridesResponseOut",
        "MonitoredResourceDescriptorIn": "_serviceusage_94_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_serviceusage_95_MonitoredResourceDescriptorOut",
        "BatchEnableServicesResponseIn": "_serviceusage_96_BatchEnableServicesResponseIn",
        "BatchEnableServicesResponseOut": "_serviceusage_97_BatchEnableServicesResponseOut",
        "TypeIn": "_serviceusage_98_TypeIn",
        "TypeOut": "_serviceusage_99_TypeOut",
        "BatchCreateAdminOverridesResponseIn": "_serviceusage_100_BatchCreateAdminOverridesResponseIn",
        "BatchCreateAdminOverridesResponseOut": "_serviceusage_101_BatchCreateAdminOverridesResponseOut",
        "MonitoringIn": "_serviceusage_102_MonitoringIn",
        "MonitoringOut": "_serviceusage_103_MonitoringOut",
        "ImportAdminOverridesResponseIn": "_serviceusage_104_ImportAdminOverridesResponseIn",
        "ImportAdminOverridesResponseOut": "_serviceusage_105_ImportAdminOverridesResponseOut",
        "HttpRuleIn": "_serviceusage_106_HttpRuleIn",
        "HttpRuleOut": "_serviceusage_107_HttpRuleOut",
        "GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn": "_serviceusage_108_GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn",
        "GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut": "_serviceusage_109_GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut",
        "BillingDestinationIn": "_serviceusage_110_BillingDestinationIn",
        "BillingDestinationOut": "_serviceusage_111_BillingDestinationOut",
        "AdminQuotaPolicyIn": "_serviceusage_112_AdminQuotaPolicyIn",
        "AdminQuotaPolicyOut": "_serviceusage_113_AdminQuotaPolicyOut",
        "AuthProviderIn": "_serviceusage_114_AuthProviderIn",
        "AuthProviderOut": "_serviceusage_115_AuthProviderOut",
        "AuthenticationRuleIn": "_serviceusage_116_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_serviceusage_117_AuthenticationRuleOut",
        "LogDescriptorIn": "_serviceusage_118_LogDescriptorIn",
        "LogDescriptorOut": "_serviceusage_119_LogDescriptorOut",
        "MetricDescriptorMetadataIn": "_serviceusage_120_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_serviceusage_121_MetricDescriptorMetadataOut",
        "TermsOfServiceIn": "_serviceusage_122_TermsOfServiceIn",
        "TermsOfServiceOut": "_serviceusage_123_TermsOfServiceOut",
        "DeleteAdminQuotaPolicyMetadataIn": "_serviceusage_124_DeleteAdminQuotaPolicyMetadataIn",
        "DeleteAdminQuotaPolicyMetadataOut": "_serviceusage_125_DeleteAdminQuotaPolicyMetadataOut",
        "OAuthRequirementsIn": "_serviceusage_126_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_serviceusage_127_OAuthRequirementsOut",
        "OperationIn": "_serviceusage_128_OperationIn",
        "OperationOut": "_serviceusage_129_OperationOut",
        "GoogleApiServiceusageV1beta1ServiceIdentityIn": "_serviceusage_130_GoogleApiServiceusageV1beta1ServiceIdentityIn",
        "GoogleApiServiceusageV1beta1ServiceIdentityOut": "_serviceusage_131_GoogleApiServiceusageV1beta1ServiceIdentityOut",
        "ImportAdminQuotaPoliciesResponseIn": "_serviceusage_132_ImportAdminQuotaPoliciesResponseIn",
        "ImportAdminQuotaPoliciesResponseOut": "_serviceusage_133_ImportAdminQuotaPoliciesResponseOut",
        "HttpIn": "_serviceusage_134_HttpIn",
        "HttpOut": "_serviceusage_135_HttpOut",
        "UsageIn": "_serviceusage_136_UsageIn",
        "UsageOut": "_serviceusage_137_UsageOut",
        "CustomHttpPatternIn": "_serviceusage_138_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_serviceusage_139_CustomHttpPatternOut",
        "NodeSettingsIn": "_serviceusage_140_NodeSettingsIn",
        "NodeSettingsOut": "_serviceusage_141_NodeSettingsOut",
        "GoogleApiServiceusageV1ServiceIn": "_serviceusage_142_GoogleApiServiceusageV1ServiceIn",
        "GoogleApiServiceusageV1ServiceOut": "_serviceusage_143_GoogleApiServiceusageV1ServiceOut",
        "LabelDescriptorIn": "_serviceusage_144_LabelDescriptorIn",
        "LabelDescriptorOut": "_serviceusage_145_LabelDescriptorOut",
        "DotnetSettingsIn": "_serviceusage_146_DotnetSettingsIn",
        "DotnetSettingsOut": "_serviceusage_147_DotnetSettingsOut",
        "ServiceValueIn": "_serviceusage_148_ServiceValueIn",
        "ServiceValueOut": "_serviceusage_149_ServiceValueOut",
        "JavaSettingsIn": "_serviceusage_150_JavaSettingsIn",
        "JavaSettingsOut": "_serviceusage_151_JavaSettingsOut",
        "LoggingIn": "_serviceusage_152_LoggingIn",
        "LoggingOut": "_serviceusage_153_LoggingOut",
        "BackendIn": "_serviceusage_154_BackendIn",
        "BackendOut": "_serviceusage_155_BackendOut",
        "StatusIn": "_serviceusage_156_StatusIn",
        "StatusOut": "_serviceusage_157_StatusOut",
        "SystemParameterIn": "_serviceusage_158_SystemParameterIn",
        "SystemParameterOut": "_serviceusage_159_SystemParameterOut",
        "DocumentationIn": "_serviceusage_160_DocumentationIn",
        "DocumentationOut": "_serviceusage_161_DocumentationOut",
        "ImportConsumerOverridesMetadataIn": "_serviceusage_162_ImportConsumerOverridesMetadataIn",
        "ImportConsumerOverridesMetadataOut": "_serviceusage_163_ImportConsumerOverridesMetadataOut",
        "PhpSettingsIn": "_serviceusage_164_PhpSettingsIn",
        "PhpSettingsOut": "_serviceusage_165_PhpSettingsOut",
        "PythonSettingsIn": "_serviceusage_166_PythonSettingsIn",
        "PythonSettingsOut": "_serviceusage_167_PythonSettingsOut",
        "PublishingIn": "_serviceusage_168_PublishingIn",
        "PublishingOut": "_serviceusage_169_PublishingOut",
        "ConsumerPolicyIn": "_serviceusage_170_ConsumerPolicyIn",
        "ConsumerPolicyOut": "_serviceusage_171_ConsumerPolicyOut",
        "FieldIn": "_serviceusage_172_FieldIn",
        "FieldOut": "_serviceusage_173_FieldOut",
        "CancelOperationRequestIn": "_serviceusage_174_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_serviceusage_175_CancelOperationRequestOut",
        "LongRunningIn": "_serviceusage_176_LongRunningIn",
        "LongRunningOut": "_serviceusage_177_LongRunningOut",
        "GetServiceIdentityMetadataIn": "_serviceusage_178_GetServiceIdentityMetadataIn",
        "GetServiceIdentityMetadataOut": "_serviceusage_179_GetServiceIdentityMetadataOut",
        "GoogleApiServiceusageV1ServiceConfigIn": "_serviceusage_180_GoogleApiServiceusageV1ServiceConfigIn",
        "GoogleApiServiceusageV1ServiceConfigOut": "_serviceusage_181_GoogleApiServiceusageV1ServiceConfigOut",
        "JwtLocationIn": "_serviceusage_182_JwtLocationIn",
        "JwtLocationOut": "_serviceusage_183_JwtLocationOut",
        "RubySettingsIn": "_serviceusage_184_RubySettingsIn",
        "RubySettingsOut": "_serviceusage_185_RubySettingsOut",
        "DisableServiceResponseIn": "_serviceusage_186_DisableServiceResponseIn",
        "DisableServiceResponseOut": "_serviceusage_187_DisableServiceResponseOut",
        "ServiceIdentityIn": "_serviceusage_188_ServiceIdentityIn",
        "ServiceIdentityOut": "_serviceusage_189_ServiceIdentityOut",
        "ListServicesResponseIn": "_serviceusage_190_ListServicesResponseIn",
        "ListServicesResponseOut": "_serviceusage_191_ListServicesResponseOut",
        "QuotaOverrideIn": "_serviceusage_192_QuotaOverrideIn",
        "QuotaOverrideOut": "_serviceusage_193_QuotaOverrideOut",
        "BatchGetServicesResponseIn": "_serviceusage_194_BatchGetServicesResponseIn",
        "BatchGetServicesResponseOut": "_serviceusage_195_BatchGetServicesResponseOut",
        "EnumIn": "_serviceusage_196_EnumIn",
        "EnumOut": "_serviceusage_197_EnumOut",
        "SystemParametersIn": "_serviceusage_198_SystemParametersIn",
        "SystemParametersOut": "_serviceusage_199_SystemParametersOut",
        "EndpointIn": "_serviceusage_200_EndpointIn",
        "EndpointOut": "_serviceusage_201_EndpointOut",
        "ContextRuleIn": "_serviceusage_202_ContextRuleIn",
        "ContextRuleOut": "_serviceusage_203_ContextRuleOut",
        "ControlIn": "_serviceusage_204_ControlIn",
        "ControlOut": "_serviceusage_205_ControlOut",
        "BackendRuleIn": "_serviceusage_206_BackendRuleIn",
        "BackendRuleOut": "_serviceusage_207_BackendRuleOut",
        "OptionIn": "_serviceusage_208_OptionIn",
        "OptionOut": "_serviceusage_209_OptionOut",
        "UpdateConsumerPolicyLROMetadataIn": "_serviceusage_210_UpdateConsumerPolicyLROMetadataIn",
        "UpdateConsumerPolicyLROMetadataOut": "_serviceusage_211_UpdateConsumerPolicyLROMetadataOut",
        "MethodSettingsIn": "_serviceusage_212_MethodSettingsIn",
        "MethodSettingsOut": "_serviceusage_213_MethodSettingsOut",
        "BillingIn": "_serviceusage_214_BillingIn",
        "BillingOut": "_serviceusage_215_BillingOut",
        "EnableServiceRequestIn": "_serviceusage_216_EnableServiceRequestIn",
        "EnableServiceRequestOut": "_serviceusage_217_EnableServiceRequestOut",
        "GoogleApiServiceIn": "_serviceusage_218_GoogleApiServiceIn",
        "GoogleApiServiceOut": "_serviceusage_219_GoogleApiServiceOut",
        "AddEnableRulesResponseIn": "_serviceusage_220_AddEnableRulesResponseIn",
        "AddEnableRulesResponseOut": "_serviceusage_221_AddEnableRulesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}).optional(),
            "maxLimit": t.string().optional(),
            "name": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "freeTier": t.string().optional(),
            "description": t.string().optional(),
            "metric": t.string().optional(),
            "duration": t.string().optional(),
            "displayName": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}).optional(),
            "maxLimit": t.string().optional(),
            "name": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "freeTier": t.string().optional(),
            "description": t.string().optional(),
            "metric": t.string().optional(),
            "duration": t.string().optional(),
            "displayName": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
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
    types["MixinIn"] = t.struct(
        {"root": t.string().optional(), "name": t.string().optional()}
    ).named(renames["MixinIn"])
    types["MixinOut"] = t.struct(
        {
            "root": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MixinOut"])
    types["ImportAdminQuotaPoliciesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAdminQuotaPoliciesMetadataIn"])
    types["ImportAdminQuotaPoliciesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAdminQuotaPoliciesMetadataOut"])
    types["ImportConsumerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["ImportConsumerOverridesResponseIn"])
    types["ImportConsumerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportConsumerOverridesResponseOut"])
    types["ImportAdminOverridesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAdminOverridesMetadataIn"])
    types["ImportAdminOverridesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAdminOverridesMetadataOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["OperationMetadataIn"] = t.struct(
        {"resourceNames": t.array(t.string()).optional()}
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
    types["ApiIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "syntax": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "syntax": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["CustomErrorIn"] = t.struct(
        {
            "types": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["CustomErrorRuleIn"])).optional(),
        }
    ).named(renames["CustomErrorIn"])
    types["CustomErrorOut"] = t.struct(
        {
            "types": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["CustomErrorRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomErrorOut"])
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
    types["DisableServiceRequestIn"] = t.struct(
        {
            "checkIfServiceHasUsage": t.string().optional(),
            "disableDependentServices": t.boolean().optional(),
        }
    ).named(renames["DisableServiceRequestIn"])
    types["DisableServiceRequestOut"] = t.struct(
        {
            "checkIfServiceHasUsage": t.string().optional(),
            "disableDependentServices": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableServiceRequestOut"])
    types["ValueInfoIn"] = t.struct(
        {
            "serviceValue": t.proxy(renames["ServiceValueIn"]).optional(),
            "groupValue": t.proxy(renames["GroupValueIn"]).optional(),
            "summary": t.string().optional(),
            "title": t.string().optional(),
            "learnmoreLink": t.string().optional(),
        }
    ).named(renames["ValueInfoIn"])
    types["ValueInfoOut"] = t.struct(
        {
            "serviceValue": t.proxy(renames["ServiceValueOut"]).optional(),
            "groupValue": t.proxy(renames["GroupValueOut"]).optional(),
            "summary": t.string().optional(),
            "title": t.string().optional(),
            "learnmoreLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueInfoOut"])
    types["EnumValueIn"] = t.struct(
        {
            "number": t.integer().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["EnumValueIn"])
    types["EnumValueOut"] = t.struct(
        {
            "number": t.integer().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValueOut"])
    types["CreateAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateAdminQuotaPolicyMetadataIn"])
    types["CreateAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateAdminQuotaPolicyMetadataOut"])
    types["GetServiceIdentityResponseIn"] = t.struct(
        {
            "identity": t.proxy(renames["ServiceIdentityIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GetServiceIdentityResponseIn"])
    types["GetServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["ServiceIdentityOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetServiceIdentityResponseOut"])
    types["RemoveEnableRulesResponseIn"] = t.struct(
        {"parent": t.string().optional()}
    ).named(renames["RemoveEnableRulesResponseIn"])
    types["RemoveEnableRulesResponseOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveEnableRulesResponseOut"])
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
    types["GoogleApiServiceusageV1OperationMetadataIn"] = t.struct(
        {"resourceNames": t.array(t.string()).optional()}
    ).named(renames["GoogleApiServiceusageV1OperationMetadataIn"])
    types["GoogleApiServiceusageV1OperationMetadataOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1OperationMetadataOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "metricKind": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "metricKind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["RemoveEnableRulesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveEnableRulesMetadataIn"]
    )
    types["RemoveEnableRulesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveEnableRulesMetadataOut"])
    types["BatchEnableServicesRequestIn"] = t.struct(
        {"serviceIds": t.array(t.string()).optional()}
    ).named(renames["BatchEnableServicesRequestIn"])
    types["BatchEnableServicesRequestOut"] = t.struct(
        {
            "serviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchEnableServicesRequestOut"])
    types["EnableRuleIn"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
            "values": t.array(t.string()).optional(),
            "enableType": t.string().optional(),
        }
    ).named(renames["EnableRuleIn"])
    types["EnableRuleOut"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
            "values": t.array(t.string()).optional(),
            "enableType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableRuleOut"])
    types["DocumentationRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "description": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "deprecationDescription": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "description": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
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
    types["MethodIn"] = t.struct(
        {
            "responseStreaming": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "requestStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "syntax": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "responseStreaming": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "requestStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "syntax": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GroupValueIn"] = t.struct({"name": t.string().optional()}).named(
        renames["GroupValueIn"]
    )
    types["GroupValueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupValueOut"])
    types["AddEnableRulesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddEnableRulesMetadataIn"]
    )
    types["AddEnableRulesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddEnableRulesMetadataOut"])
    types["EnableFailureIn"] = t.struct(
        {"serviceId": t.string().optional(), "errorMessage": t.string().optional()}
    ).named(renames["EnableFailureIn"])
    types["EnableFailureOut"] = t.struct(
        {
            "serviceId": t.string().optional(),
            "errorMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableFailureOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "restNumericEnums": t.boolean().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "launchStage": t.string().optional(),
            "version": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "restNumericEnums": t.boolean().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "version": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["UpdateAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateAdminQuotaPolicyMetadataIn"])
    types["UpdateAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateAdminQuotaPolicyMetadataOut"])
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
    types["MonitoringDestinationIn"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "monitoredResource": t.string().optional(),
        }
    ).named(renames["MonitoringDestinationIn"])
    types["MonitoringDestinationOut"] = t.struct(
        {
            "metrics": t.array(t.string()).optional(),
            "monitoredResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoringDestinationOut"])
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
    types["EnableServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["GoogleApiServiceusageV1ServiceIn"]).optional()}
    ).named(renames["EnableServiceResponseIn"])
    types["EnableServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableServiceResponseOut"])
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
    types["PageIn"] = t.struct(
        {
            "name": t.string().optional(),
            "content": t.string().optional(),
            "subpages": t.array(t.proxy(renames["PageIn"])).optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "name": t.string().optional(),
            "content": t.string().optional(),
            "subpages": t.array(t.proxy(renames["PageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["BatchCreateConsumerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["BatchCreateConsumerOverridesResponseIn"])
    types["BatchCreateConsumerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateConsumerOverridesResponseOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["BatchEnableServicesResponseIn"] = t.struct(
        {
            "failures": t.array(t.proxy(renames["EnableFailureIn"])).optional(),
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceIn"])
            ).optional(),
        }
    ).named(renames["BatchEnableServicesResponseIn"])
    types["BatchEnableServicesResponseOut"] = t.struct(
        {
            "failures": t.array(t.proxy(renames["EnableFailureOut"])).optional(),
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchEnableServicesResponseOut"])
    types["TypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["BatchCreateAdminOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["BatchCreateAdminOverridesResponseIn"])
    types["BatchCreateAdminOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateAdminOverridesResponseOut"])
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
    types["ImportAdminOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["ImportAdminOverridesResponseIn"])
    types["ImportAdminOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAdminOverridesResponseOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "post": t.string().optional(),
            "delete": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "patch": t.string().optional(),
            "responseBody": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "body": t.string().optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "post": t.string().optional(),
            "delete": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "patch": t.string().optional(),
            "responseBody": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "body": t.string().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn"] = t.struct(
        {
            "state": t.string().optional(),
            "identity": t.proxy(
                renames["GoogleApiServiceusageV1beta1ServiceIdentityIn"]
            ).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn"])
    types["GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut"] = t.struct(
        {
            "state": t.string().optional(),
            "identity": t.proxy(
                renames["GoogleApiServiceusageV1beta1ServiceIdentityOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut"])
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
    types["AdminQuotaPolicyIn"] = t.struct(
        {
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "container": t.string().optional(),
            "unit": t.string().optional(),
            "name": t.string().optional(),
            "policyValue": t.string().optional(),
        }
    ).named(renames["AdminQuotaPolicyIn"])
    types["AdminQuotaPolicyOut"] = t.struct(
        {
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "container": t.string().optional(),
            "unit": t.string().optional(),
            "name": t.string().optional(),
            "policyValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminQuotaPolicyOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "jwksUri": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "issuer": t.string().optional(),
            "id": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "audiences": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "jwksUri": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "issuer": t.string().optional(),
            "id": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "audiences": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["AuthenticationRuleIn"] = t.struct(
        {
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
    types["LogDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "ingestDelay": t.string().optional(),
            "launchStage": t.string().optional(),
            "samplePeriod": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "ingestDelay": t.string().optional(),
            "launchStage": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
    types["TermsOfServiceIn"] = t.struct(
        {"uri": t.string().optional(), "title": t.string().optional()}
    ).named(renames["TermsOfServiceIn"])
    types["TermsOfServiceOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TermsOfServiceOut"])
    types["DeleteAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteAdminQuotaPolicyMetadataIn"])
    types["DeleteAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteAdminQuotaPolicyMetadataOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["GoogleApiServiceusageV1beta1ServiceIdentityIn"] = t.struct(
        {"email": t.string().optional(), "uniqueId": t.string().optional()}
    ).named(renames["GoogleApiServiceusageV1beta1ServiceIdentityIn"])
    types["GoogleApiServiceusageV1beta1ServiceIdentityOut"] = t.struct(
        {
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1beta1ServiceIdentityOut"])
    types["ImportAdminQuotaPoliciesResponseIn"] = t.struct(
        {"policies": t.array(t.proxy(renames["AdminQuotaPolicyIn"])).optional()}
    ).named(renames["ImportAdminQuotaPoliciesResponseIn"])
    types["ImportAdminQuotaPoliciesResponseOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["AdminQuotaPolicyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAdminQuotaPoliciesResponseOut"])
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
    types["UsageIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["UsageRuleIn"])).optional(),
            "producerNotificationChannel": t.string().optional(),
            "requirements": t.array(t.string()).optional(),
        }
    ).named(renames["UsageIn"])
    types["UsageOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["UsageRuleOut"])).optional(),
            "producerNotificationChannel": t.string().optional(),
            "requirements": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageOut"])
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
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["GoogleApiServiceusageV1ServiceIn"] = t.struct(
        {
            "config": t.proxy(
                renames["GoogleApiServiceusageV1ServiceConfigIn"]
            ).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceIn"])
    types["GoogleApiServiceusageV1ServiceOut"] = t.struct(
        {
            "config": t.proxy(
                renames["GoogleApiServiceusageV1ServiceConfigOut"]
            ).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceOut"])
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
    types["DotnetSettingsIn"] = t.struct(
        {
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["ServiceValueIn"] = t.struct(
        {
            "name": t.string().optional(),
            "tos": t.array(t.proxy(renames["TermsOfServiceIn"])).optional(),
            "pricingLink": t.string().optional(),
            "dnsAddress": t.string().optional(),
        }
    ).named(renames["ServiceValueIn"])
    types["ServiceValueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "tos": t.array(t.proxy(renames["TermsOfServiceOut"])).optional(),
            "pricingLink": t.string().optional(),
            "dnsAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceValueOut"])
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
    types["LoggingIn"] = t.struct(
        {
            "producerDestinations": t.array(
                t.proxy(renames["LoggingDestinationIn"])
            ).optional(),
            "consumerDestinations": t.array(
                t.proxy(renames["LoggingDestinationIn"])
            ).optional(),
        }
    ).named(renames["LoggingIn"])
    types["LoggingOut"] = t.struct(
        {
            "producerDestinations": t.array(
                t.proxy(renames["LoggingDestinationOut"])
            ).optional(),
            "consumerDestinations": t.array(
                t.proxy(renames["LoggingDestinationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LoggingOut"])
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
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
    types["DocumentationIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "summary": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["ImportConsumerOverridesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportConsumerOverridesMetadataIn"])
    types["ImportConsumerOverridesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportConsumerOverridesMetadataOut"])
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
    types["PublishingIn"] = t.struct(
        {
            "documentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "organization": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "githubLabel": t.string().optional(),
            "newIssueUri": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "documentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "organization": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "githubLabel": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["ConsumerPolicyIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "enableRules": t.array(t.proxy(renames["EnableRuleIn"])).optional(),
        }
    ).named(renames["ConsumerPolicyIn"])
    types["ConsumerPolicyOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "enableRules": t.array(t.proxy(renames["EnableRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerPolicyOut"])
    types["FieldIn"] = t.struct(
        {
            "typeUrl": t.string().optional(),
            "defaultValue": t.string().optional(),
            "kind": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "packed": t.boolean().optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
            "jsonName": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "number": t.integer().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "typeUrl": t.string().optional(),
            "defaultValue": t.string().optional(),
            "kind": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "packed": t.boolean().optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
            "jsonName": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["LongRunningIn"] = t.struct(
        {
            "totalPollTimeout": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "maxPollDelay": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "totalPollTimeout": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "maxPollDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["GetServiceIdentityMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetServiceIdentityMetadataIn"])
    types["GetServiceIdentityMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GetServiceIdentityMetadataOut"])
    types["GoogleApiServiceusageV1ServiceConfigIn"] = t.struct(
        {
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "title": t.string().optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceConfigIn"])
    types["GoogleApiServiceusageV1ServiceConfigOut"] = t.struct(
        {
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "title": t.string().optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceConfigOut"])
    types["JwtLocationIn"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "header": t.string().optional(),
            "cookie": t.string().optional(),
            "query": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "header": t.string().optional(),
            "cookie": t.string().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["DisableServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["GoogleApiServiceusageV1ServiceIn"]).optional()}
    ).named(renames["DisableServiceResponseIn"])
    types["DisableServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableServiceResponseOut"])
    types["ServiceIdentityIn"] = t.struct(
        {"email": t.string().optional(), "uniqueId": t.string().optional()}
    ).named(renames["ServiceIdentityIn"])
    types["ServiceIdentityOut"] = t.struct(
        {
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceIdentityOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceIn"])
            ).optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["QuotaOverrideIn"] = t.struct(
        {
            "overrideValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "adminOverrideAncestor": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["QuotaOverrideIn"])
    types["QuotaOverrideOut"] = t.struct(
        {
            "overrideValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "adminOverrideAncestor": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOverrideOut"])
    types["BatchGetServicesResponseIn"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceIn"])
            ).optional()
        }
    ).named(renames["BatchGetServicesResponseIn"])
    types["BatchGetServicesResponseOut"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchGetServicesResponseOut"])
    types["EnumIn"] = t.struct(
        {
            "syntax": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "syntax": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["EndpointIn"] = t.struct(
        {
            "name": t.string().optional(),
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "aliases": t.array(t.string()).optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "name": t.string().optional(),
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "aliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "requested": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "requested": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["BackendRuleIn"] = t.struct(
        {
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "operationDeadline": t.number().optional(),
            "jwtAudience": t.string().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "pathTranslation": t.string(),
            "protocol": t.string().optional(),
            "selector": t.string().optional(),
            "disableAuth": t.boolean().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "operationDeadline": t.number().optional(),
            "jwtAudience": t.string().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "pathTranslation": t.string(),
            "protocol": t.string().optional(),
            "selector": t.string().optional(),
            "disableAuth": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
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
    types["UpdateConsumerPolicyLROMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateConsumerPolicyLROMetadataIn"])
    types["UpdateConsumerPolicyLROMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateConsumerPolicyLROMetadataOut"])
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
    types["EnableServiceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableServiceRequestIn"]
    )
    types["EnableServiceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableServiceRequestOut"])
    types["GoogleApiServiceIn"] = t.struct(
        {
            "configVersion": t.integer().optional(),
            "producerProjectId": t.string().optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "id": t.string().optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "name": t.string().optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "title": t.string().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
        }
    ).named(renames["GoogleApiServiceIn"])
    types["GoogleApiServiceOut"] = t.struct(
        {
            "configVersion": t.integer().optional(),
            "producerProjectId": t.string().optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "id": t.string().optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "name": t.string().optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "title": t.string().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceOut"])
    types["AddEnableRulesResponseIn"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueInfoIn"])).optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["AddEnableRulesResponseIn"])
    types["AddEnableRulesResponseOut"] = t.struct(
        {
            "values": t.array(t.proxy(renames["ValueInfoOut"])).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddEnableRulesResponseOut"])

    functions = {}
    functions["operationsList"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesEnable"] = serviceusage.post(
        "v1/{parent}/services:batchEnable",
        t.struct(
            {
                "parent": t.string().optional(),
                "serviceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = serviceusage.post(
        "v1/{parent}/services:batchEnable",
        t.struct(
            {
                "parent": t.string().optional(),
                "serviceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesBatchGet"] = serviceusage.post(
        "v1/{parent}/services:batchEnable",
        t.struct(
            {
                "parent": t.string().optional(),
                "serviceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDisable"] = serviceusage.post(
        "v1/{parent}/services:batchEnable",
        t.struct(
            {
                "parent": t.string().optional(),
                "serviceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = serviceusage.post(
        "v1/{parent}/services:batchEnable",
        t.struct(
            {
                "parent": t.string().optional(),
                "serviceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesBatchEnable"] = serviceusage.post(
        "v1/{parent}/services:batchEnable",
        t.struct(
            {
                "parent": t.string().optional(),
                "serviceIds": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="serviceusage", renames=renames, types=types, functions=functions
    )
