from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_serviceusage() -> Import:
    serviceusage = HTTPRuntime("https://serviceusage.googleapis.com/")

    renames = {
        "ErrorResponse": "_serviceusage_1_ErrorResponse",
        "RemoveEnableRulesMetadataIn": "_serviceusage_2_RemoveEnableRulesMetadataIn",
        "RemoveEnableRulesMetadataOut": "_serviceusage_3_RemoveEnableRulesMetadataOut",
        "DotnetSettingsIn": "_serviceusage_4_DotnetSettingsIn",
        "DotnetSettingsOut": "_serviceusage_5_DotnetSettingsOut",
        "ImportConsumerOverridesMetadataIn": "_serviceusage_6_ImportConsumerOverridesMetadataIn",
        "ImportConsumerOverridesMetadataOut": "_serviceusage_7_ImportConsumerOverridesMetadataOut",
        "PhpSettingsIn": "_serviceusage_8_PhpSettingsIn",
        "PhpSettingsOut": "_serviceusage_9_PhpSettingsOut",
        "QuotaLimitIn": "_serviceusage_10_QuotaLimitIn",
        "QuotaLimitOut": "_serviceusage_11_QuotaLimitOut",
        "AddEnableRulesResponseIn": "_serviceusage_12_AddEnableRulesResponseIn",
        "AddEnableRulesResponseOut": "_serviceusage_13_AddEnableRulesResponseOut",
        "JavaSettingsIn": "_serviceusage_14_JavaSettingsIn",
        "JavaSettingsOut": "_serviceusage_15_JavaSettingsOut",
        "BackendRuleIn": "_serviceusage_16_BackendRuleIn",
        "BackendRuleOut": "_serviceusage_17_BackendRuleOut",
        "SystemParameterRuleIn": "_serviceusage_18_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_serviceusage_19_SystemParameterRuleOut",
        "RemoveEnableRulesResponseIn": "_serviceusage_20_RemoveEnableRulesResponseIn",
        "RemoveEnableRulesResponseOut": "_serviceusage_21_RemoveEnableRulesResponseOut",
        "AuthRequirementIn": "_serviceusage_22_AuthRequirementIn",
        "AuthRequirementOut": "_serviceusage_23_AuthRequirementOut",
        "BatchCreateConsumerOverridesResponseIn": "_serviceusage_24_BatchCreateConsumerOverridesResponseIn",
        "BatchCreateConsumerOverridesResponseOut": "_serviceusage_25_BatchCreateConsumerOverridesResponseOut",
        "EnableServiceRequestIn": "_serviceusage_26_EnableServiceRequestIn",
        "EnableServiceRequestOut": "_serviceusage_27_EnableServiceRequestOut",
        "MetricDescriptorIn": "_serviceusage_28_MetricDescriptorIn",
        "MetricDescriptorOut": "_serviceusage_29_MetricDescriptorOut",
        "ControlIn": "_serviceusage_30_ControlIn",
        "ControlOut": "_serviceusage_31_ControlOut",
        "ImportAdminOverridesResponseIn": "_serviceusage_32_ImportAdminOverridesResponseIn",
        "ImportAdminOverridesResponseOut": "_serviceusage_33_ImportAdminOverridesResponseOut",
        "MethodIn": "_serviceusage_34_MethodIn",
        "MethodOut": "_serviceusage_35_MethodOut",
        "EmptyIn": "_serviceusage_36_EmptyIn",
        "EmptyOut": "_serviceusage_37_EmptyOut",
        "GetServiceIdentityMetadataIn": "_serviceusage_38_GetServiceIdentityMetadataIn",
        "GetServiceIdentityMetadataOut": "_serviceusage_39_GetServiceIdentityMetadataOut",
        "PythonSettingsIn": "_serviceusage_40_PythonSettingsIn",
        "PythonSettingsOut": "_serviceusage_41_PythonSettingsOut",
        "LogDescriptorIn": "_serviceusage_42_LogDescriptorIn",
        "LogDescriptorOut": "_serviceusage_43_LogDescriptorOut",
        "BatchGetServicesResponseIn": "_serviceusage_44_BatchGetServicesResponseIn",
        "BatchGetServicesResponseOut": "_serviceusage_45_BatchGetServicesResponseOut",
        "QuotaOverrideIn": "_serviceusage_46_QuotaOverrideIn",
        "QuotaOverrideOut": "_serviceusage_47_QuotaOverrideOut",
        "CppSettingsIn": "_serviceusage_48_CppSettingsIn",
        "CppSettingsOut": "_serviceusage_49_CppSettingsOut",
        "PageIn": "_serviceusage_50_PageIn",
        "PageOut": "_serviceusage_51_PageOut",
        "GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn": "_serviceusage_52_GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn",
        "GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut": "_serviceusage_53_GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut",
        "ImportAdminOverridesMetadataIn": "_serviceusage_54_ImportAdminOverridesMetadataIn",
        "ImportAdminOverridesMetadataOut": "_serviceusage_55_ImportAdminOverridesMetadataOut",
        "ContextIn": "_serviceusage_56_ContextIn",
        "ContextOut": "_serviceusage_57_ContextOut",
        "DocumentationRuleIn": "_serviceusage_58_DocumentationRuleIn",
        "DocumentationRuleOut": "_serviceusage_59_DocumentationRuleOut",
        "GroupValueIn": "_serviceusage_60_GroupValueIn",
        "GroupValueOut": "_serviceusage_61_GroupValueOut",
        "MixinIn": "_serviceusage_62_MixinIn",
        "MixinOut": "_serviceusage_63_MixinOut",
        "ImportConsumerOverridesResponseIn": "_serviceusage_64_ImportConsumerOverridesResponseIn",
        "ImportConsumerOverridesResponseOut": "_serviceusage_65_ImportConsumerOverridesResponseOut",
        "LongRunningIn": "_serviceusage_66_LongRunningIn",
        "LongRunningOut": "_serviceusage_67_LongRunningOut",
        "GoogleApiServiceusageV1ServiceConfigIn": "_serviceusage_68_GoogleApiServiceusageV1ServiceConfigIn",
        "GoogleApiServiceusageV1ServiceConfigOut": "_serviceusage_69_GoogleApiServiceusageV1ServiceConfigOut",
        "GetServiceIdentityResponseIn": "_serviceusage_70_GetServiceIdentityResponseIn",
        "GetServiceIdentityResponseOut": "_serviceusage_71_GetServiceIdentityResponseOut",
        "SourceInfoIn": "_serviceusage_72_SourceInfoIn",
        "SourceInfoOut": "_serviceusage_73_SourceInfoOut",
        "LoggingDestinationIn": "_serviceusage_74_LoggingDestinationIn",
        "LoggingDestinationOut": "_serviceusage_75_LoggingDestinationOut",
        "ListOperationsResponseIn": "_serviceusage_76_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_serviceusage_77_ListOperationsResponseOut",
        "EndpointIn": "_serviceusage_78_EndpointIn",
        "EndpointOut": "_serviceusage_79_EndpointOut",
        "GoogleApiServiceusageV1ServiceIn": "_serviceusage_80_GoogleApiServiceusageV1ServiceIn",
        "GoogleApiServiceusageV1ServiceOut": "_serviceusage_81_GoogleApiServiceusageV1ServiceOut",
        "LabelDescriptorIn": "_serviceusage_82_LabelDescriptorIn",
        "LabelDescriptorOut": "_serviceusage_83_LabelDescriptorOut",
        "AdminQuotaPolicyIn": "_serviceusage_84_AdminQuotaPolicyIn",
        "AdminQuotaPolicyOut": "_serviceusage_85_AdminQuotaPolicyOut",
        "AuthenticationIn": "_serviceusage_86_AuthenticationIn",
        "AuthenticationOut": "_serviceusage_87_AuthenticationOut",
        "GoogleApiServiceusageV1OperationMetadataIn": "_serviceusage_88_GoogleApiServiceusageV1OperationMetadataIn",
        "GoogleApiServiceusageV1OperationMetadataOut": "_serviceusage_89_GoogleApiServiceusageV1OperationMetadataOut",
        "GoSettingsIn": "_serviceusage_90_GoSettingsIn",
        "GoSettingsOut": "_serviceusage_91_GoSettingsOut",
        "ValueInfoIn": "_serviceusage_92_ValueInfoIn",
        "ValueInfoOut": "_serviceusage_93_ValueInfoOut",
        "HttpIn": "_serviceusage_94_HttpIn",
        "HttpOut": "_serviceusage_95_HttpOut",
        "ClientLibrarySettingsIn": "_serviceusage_96_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_serviceusage_97_ClientLibrarySettingsOut",
        "MonitoringIn": "_serviceusage_98_MonitoringIn",
        "MonitoringOut": "_serviceusage_99_MonitoringOut",
        "ServiceIdentityIn": "_serviceusage_100_ServiceIdentityIn",
        "ServiceIdentityOut": "_serviceusage_101_ServiceIdentityOut",
        "CreateAdminQuotaPolicyMetadataIn": "_serviceusage_102_CreateAdminQuotaPolicyMetadataIn",
        "CreateAdminQuotaPolicyMetadataOut": "_serviceusage_103_CreateAdminQuotaPolicyMetadataOut",
        "BillingIn": "_serviceusage_104_BillingIn",
        "BillingOut": "_serviceusage_105_BillingOut",
        "BatchCreateAdminOverridesResponseIn": "_serviceusage_106_BatchCreateAdminOverridesResponseIn",
        "BatchCreateAdminOverridesResponseOut": "_serviceusage_107_BatchCreateAdminOverridesResponseOut",
        "FieldIn": "_serviceusage_108_FieldIn",
        "FieldOut": "_serviceusage_109_FieldOut",
        "EnableRuleIn": "_serviceusage_110_EnableRuleIn",
        "EnableRuleOut": "_serviceusage_111_EnableRuleOut",
        "CustomErrorIn": "_serviceusage_112_CustomErrorIn",
        "CustomErrorOut": "_serviceusage_113_CustomErrorOut",
        "CustomHttpPatternIn": "_serviceusage_114_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_serviceusage_115_CustomHttpPatternOut",
        "GoogleApiServiceIn": "_serviceusage_116_GoogleApiServiceIn",
        "GoogleApiServiceOut": "_serviceusage_117_GoogleApiServiceOut",
        "EnableFailureIn": "_serviceusage_118_EnableFailureIn",
        "EnableFailureOut": "_serviceusage_119_EnableFailureOut",
        "DisableServiceRequestIn": "_serviceusage_120_DisableServiceRequestIn",
        "DisableServiceRequestOut": "_serviceusage_121_DisableServiceRequestOut",
        "RubySettingsIn": "_serviceusage_122_RubySettingsIn",
        "RubySettingsOut": "_serviceusage_123_RubySettingsOut",
        "UsageRuleIn": "_serviceusage_124_UsageRuleIn",
        "UsageRuleOut": "_serviceusage_125_UsageRuleOut",
        "DocumentationIn": "_serviceusage_126_DocumentationIn",
        "DocumentationOut": "_serviceusage_127_DocumentationOut",
        "MonitoredResourceDescriptorIn": "_serviceusage_128_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_serviceusage_129_MonitoredResourceDescriptorOut",
        "MonitoringDestinationIn": "_serviceusage_130_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_serviceusage_131_MonitoringDestinationOut",
        "QuotaIn": "_serviceusage_132_QuotaIn",
        "QuotaOut": "_serviceusage_133_QuotaOut",
        "NodeSettingsIn": "_serviceusage_134_NodeSettingsIn",
        "NodeSettingsOut": "_serviceusage_135_NodeSettingsOut",
        "BackendIn": "_serviceusage_136_BackendIn",
        "BackendOut": "_serviceusage_137_BackendOut",
        "SystemParametersIn": "_serviceusage_138_SystemParametersIn",
        "SystemParametersOut": "_serviceusage_139_SystemParametersOut",
        "ContextRuleIn": "_serviceusage_140_ContextRuleIn",
        "ContextRuleOut": "_serviceusage_141_ContextRuleOut",
        "ListServicesResponseIn": "_serviceusage_142_ListServicesResponseIn",
        "ListServicesResponseOut": "_serviceusage_143_ListServicesResponseOut",
        "BatchEnableServicesRequestIn": "_serviceusage_144_BatchEnableServicesRequestIn",
        "BatchEnableServicesRequestOut": "_serviceusage_145_BatchEnableServicesRequestOut",
        "OperationIn": "_serviceusage_146_OperationIn",
        "OperationOut": "_serviceusage_147_OperationOut",
        "MetricRuleIn": "_serviceusage_148_MetricRuleIn",
        "MetricRuleOut": "_serviceusage_149_MetricRuleOut",
        "SourceContextIn": "_serviceusage_150_SourceContextIn",
        "SourceContextOut": "_serviceusage_151_SourceContextOut",
        "PublishingIn": "_serviceusage_152_PublishingIn",
        "PublishingOut": "_serviceusage_153_PublishingOut",
        "MetricDescriptorMetadataIn": "_serviceusage_154_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_serviceusage_155_MetricDescriptorMetadataOut",
        "AuthenticationRuleIn": "_serviceusage_156_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_serviceusage_157_AuthenticationRuleOut",
        "GoogleApiServiceusageV1beta1ServiceIdentityIn": "_serviceusage_158_GoogleApiServiceusageV1beta1ServiceIdentityIn",
        "GoogleApiServiceusageV1beta1ServiceIdentityOut": "_serviceusage_159_GoogleApiServiceusageV1beta1ServiceIdentityOut",
        "HttpRuleIn": "_serviceusage_160_HttpRuleIn",
        "HttpRuleOut": "_serviceusage_161_HttpRuleOut",
        "UsageIn": "_serviceusage_162_UsageIn",
        "UsageOut": "_serviceusage_163_UsageOut",
        "UpdateAdminQuotaPolicyMetadataIn": "_serviceusage_164_UpdateAdminQuotaPolicyMetadataIn",
        "UpdateAdminQuotaPolicyMetadataOut": "_serviceusage_165_UpdateAdminQuotaPolicyMetadataOut",
        "TermsOfServiceIn": "_serviceusage_166_TermsOfServiceIn",
        "TermsOfServiceOut": "_serviceusage_167_TermsOfServiceOut",
        "CancelOperationRequestIn": "_serviceusage_168_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_serviceusage_169_CancelOperationRequestOut",
        "LoggingIn": "_serviceusage_170_LoggingIn",
        "LoggingOut": "_serviceusage_171_LoggingOut",
        "SystemParameterIn": "_serviceusage_172_SystemParameterIn",
        "SystemParameterOut": "_serviceusage_173_SystemParameterOut",
        "DeleteAdminQuotaPolicyMetadataIn": "_serviceusage_174_DeleteAdminQuotaPolicyMetadataIn",
        "DeleteAdminQuotaPolicyMetadataOut": "_serviceusage_175_DeleteAdminQuotaPolicyMetadataOut",
        "ConsumerPolicyIn": "_serviceusage_176_ConsumerPolicyIn",
        "ConsumerPolicyOut": "_serviceusage_177_ConsumerPolicyOut",
        "ApiIn": "_serviceusage_178_ApiIn",
        "ApiOut": "_serviceusage_179_ApiOut",
        "ServiceValueIn": "_serviceusage_180_ServiceValueIn",
        "ServiceValueOut": "_serviceusage_181_ServiceValueOut",
        "OAuthRequirementsIn": "_serviceusage_182_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_serviceusage_183_OAuthRequirementsOut",
        "BillingDestinationIn": "_serviceusage_184_BillingDestinationIn",
        "BillingDestinationOut": "_serviceusage_185_BillingDestinationOut",
        "CommonLanguageSettingsIn": "_serviceusage_186_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_serviceusage_187_CommonLanguageSettingsOut",
        "BatchEnableServicesResponseIn": "_serviceusage_188_BatchEnableServicesResponseIn",
        "BatchEnableServicesResponseOut": "_serviceusage_189_BatchEnableServicesResponseOut",
        "EnumIn": "_serviceusage_190_EnumIn",
        "EnumOut": "_serviceusage_191_EnumOut",
        "AuthProviderIn": "_serviceusage_192_AuthProviderIn",
        "AuthProviderOut": "_serviceusage_193_AuthProviderOut",
        "EnumValueIn": "_serviceusage_194_EnumValueIn",
        "EnumValueOut": "_serviceusage_195_EnumValueOut",
        "StatusIn": "_serviceusage_196_StatusIn",
        "StatusOut": "_serviceusage_197_StatusOut",
        "DisableServiceResponseIn": "_serviceusage_198_DisableServiceResponseIn",
        "DisableServiceResponseOut": "_serviceusage_199_DisableServiceResponseOut",
        "ImportAdminQuotaPoliciesResponseIn": "_serviceusage_200_ImportAdminQuotaPoliciesResponseIn",
        "ImportAdminQuotaPoliciesResponseOut": "_serviceusage_201_ImportAdminQuotaPoliciesResponseOut",
        "OperationMetadataIn": "_serviceusage_202_OperationMetadataIn",
        "OperationMetadataOut": "_serviceusage_203_OperationMetadataOut",
        "MethodSettingsIn": "_serviceusage_204_MethodSettingsIn",
        "MethodSettingsOut": "_serviceusage_205_MethodSettingsOut",
        "EnableServiceResponseIn": "_serviceusage_206_EnableServiceResponseIn",
        "EnableServiceResponseOut": "_serviceusage_207_EnableServiceResponseOut",
        "AddEnableRulesMetadataIn": "_serviceusage_208_AddEnableRulesMetadataIn",
        "AddEnableRulesMetadataOut": "_serviceusage_209_AddEnableRulesMetadataOut",
        "CustomErrorRuleIn": "_serviceusage_210_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_serviceusage_211_CustomErrorRuleOut",
        "UpdateConsumerPolicyLROMetadataIn": "_serviceusage_212_UpdateConsumerPolicyLROMetadataIn",
        "UpdateConsumerPolicyLROMetadataOut": "_serviceusage_213_UpdateConsumerPolicyLROMetadataOut",
        "TypeIn": "_serviceusage_214_TypeIn",
        "TypeOut": "_serviceusage_215_TypeOut",
        "OptionIn": "_serviceusage_216_OptionIn",
        "OptionOut": "_serviceusage_217_OptionOut",
        "ImportAdminQuotaPoliciesMetadataIn": "_serviceusage_218_ImportAdminQuotaPoliciesMetadataIn",
        "ImportAdminQuotaPoliciesMetadataOut": "_serviceusage_219_ImportAdminQuotaPoliciesMetadataOut",
        "JwtLocationIn": "_serviceusage_220_JwtLocationIn",
        "JwtLocationOut": "_serviceusage_221_JwtLocationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["RemoveEnableRulesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveEnableRulesMetadataIn"]
    )
    types["RemoveEnableRulesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveEnableRulesMetadataOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "ignoredResources": t.array(t.string()).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "ignoredResources": t.array(t.string()).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
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
    types["QuotaLimitIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "freeTier": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "maxLimit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "freeTier": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "maxLimit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["AddEnableRulesResponseIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "values": t.array(t.proxy(renames["ValueInfoIn"])).optional(),
        }
    ).named(renames["AddEnableRulesResponseIn"])
    types["AddEnableRulesResponseOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "values": t.array(t.proxy(renames["ValueInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddEnableRulesResponseOut"])
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
    types["BackendRuleIn"] = t.struct(
        {
            "deadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "address": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "protocol": t.string().optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "deadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "address": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "protocol": t.string().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
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
    types["RemoveEnableRulesResponseIn"] = t.struct(
        {"parent": t.string().optional()}
    ).named(renames["RemoveEnableRulesResponseIn"])
    types["RemoveEnableRulesResponseOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveEnableRulesResponseOut"])
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
    types["BatchCreateConsumerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["BatchCreateConsumerOverridesResponseIn"])
    types["BatchCreateConsumerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateConsumerOverridesResponseOut"])
    types["EnableServiceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableServiceRequestIn"]
    )
    types["EnableServiceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableServiceRequestOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "type": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "valueType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "displayName": t.string().optional(),
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "type": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "valueType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "displayName": t.string().optional(),
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["ImportAdminOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["ImportAdminOverridesResponseIn"])
    types["ImportAdminOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAdminOverridesResponseOut"])
    types["MethodIn"] = t.struct(
        {
            "name": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "syntax": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "name": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "syntax": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GetServiceIdentityMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetServiceIdentityMetadataIn"])
    types["GetServiceIdentityMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GetServiceIdentityMetadataOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
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
    types["QuotaOverrideIn"] = t.struct(
        {
            "adminOverrideAncestor": t.string().optional(),
            "unit": t.string().optional(),
            "overrideValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["QuotaOverrideIn"])
    types["QuotaOverrideOut"] = t.struct(
        {
            "adminOverrideAncestor": t.string().optional(),
            "unit": t.string().optional(),
            "overrideValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOverrideOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
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
    types["GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn"] = t.struct(
        {
            "identity": t.proxy(
                renames["GoogleApiServiceusageV1beta1ServiceIdentityIn"]
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn"])
    types["GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(
                renames["GoogleApiServiceusageV1beta1ServiceIdentityOut"]
            ).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut"])
    types["ImportAdminOverridesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAdminOverridesMetadataIn"])
    types["ImportAdminOverridesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAdminOverridesMetadataOut"])
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["DocumentationRuleIn"] = t.struct(
        {
            "description": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "selector": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "description": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "selector": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
    types["GroupValueIn"] = t.struct({"name": t.string().optional()}).named(
        renames["GroupValueIn"]
    )
    types["GroupValueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupValueOut"])
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
    types["ImportConsumerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["ImportConsumerOverridesResponseIn"])
    types["ImportConsumerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportConsumerOverridesResponseOut"])
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
    types["GoogleApiServiceusageV1ServiceConfigIn"] = t.struct(
        {
            "title": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "name": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceConfigIn"])
    types["GoogleApiServiceusageV1ServiceConfigOut"] = t.struct(
        {
            "title": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "name": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceConfigOut"])
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
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
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
    types["EndpointIn"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "target": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["GoogleApiServiceusageV1ServiceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "config": t.proxy(
                renames["GoogleApiServiceusageV1ServiceConfigIn"]
            ).optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceIn"])
    types["GoogleApiServiceusageV1ServiceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "state": t.string().optional(),
            "config": t.proxy(
                renames["GoogleApiServiceusageV1ServiceConfigOut"]
            ).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceOut"])
    types["LabelDescriptorIn"] = t.struct(
        {
            "key": t.string().optional(),
            "valueType": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LabelDescriptorIn"])
    types["LabelDescriptorOut"] = t.struct(
        {
            "key": t.string().optional(),
            "valueType": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LabelDescriptorOut"])
    types["AdminQuotaPolicyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "container": t.string().optional(),
            "unit": t.string().optional(),
            "policyValue": t.string().optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["AdminQuotaPolicyIn"])
    types["AdminQuotaPolicyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "container": t.string().optional(),
            "unit": t.string().optional(),
            "policyValue": t.string().optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminQuotaPolicyOut"])
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
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["ValueInfoIn"] = t.struct(
        {
            "summary": t.string().optional(),
            "learnmoreLink": t.string().optional(),
            "title": t.string().optional(),
            "serviceValue": t.proxy(renames["ServiceValueIn"]).optional(),
            "groupValue": t.proxy(renames["GroupValueIn"]).optional(),
        }
    ).named(renames["ValueInfoIn"])
    types["ValueInfoOut"] = t.struct(
        {
            "summary": t.string().optional(),
            "learnmoreLink": t.string().optional(),
            "title": t.string().optional(),
            "serviceValue": t.proxy(renames["ServiceValueOut"]).optional(),
            "groupValue": t.proxy(renames["GroupValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueInfoOut"])
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
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "launchStage": t.string().optional(),
            "version": t.string().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "version": t.string().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
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
    types["CreateAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateAdminQuotaPolicyMetadataIn"])
    types["CreateAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateAdminQuotaPolicyMetadataOut"])
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
    types["BatchCreateAdminOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["BatchCreateAdminOverridesResponseIn"])
    types["BatchCreateAdminOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateAdminOverridesResponseOut"])
    types["FieldIn"] = t.struct(
        {
            "oneofIndex": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "number": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "kind": t.string().optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "jsonName": t.string().optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "oneofIndex": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "number": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "kind": t.string().optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "jsonName": t.string().optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["EnableRuleIn"] = t.struct(
        {
            "enableType": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "services": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
        }
    ).named(renames["EnableRuleIn"])
    types["EnableRuleOut"] = t.struct(
        {
            "enableType": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "services": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableRuleOut"])
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
    types["GoogleApiServiceIn"] = t.struct(
        {
            "context": t.proxy(renames["ContextIn"]).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "producerProjectId": t.string().optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "title": t.string().optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "name": t.string().optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "id": t.string().optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "configVersion": t.integer().optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
        }
    ).named(renames["GoogleApiServiceIn"])
    types["GoogleApiServiceOut"] = t.struct(
        {
            "context": t.proxy(renames["ContextOut"]).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "producerProjectId": t.string().optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "title": t.string().optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "name": t.string().optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "id": t.string().optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "configVersion": t.integer().optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceOut"])
    types["EnableFailureIn"] = t.struct(
        {"errorMessage": t.string().optional(), "serviceId": t.string().optional()}
    ).named(renames["EnableFailureIn"])
    types["EnableFailureOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "serviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableFailureOut"])
    types["DisableServiceRequestIn"] = t.struct(
        {
            "disableDependentServices": t.boolean().optional(),
            "checkIfServiceHasUsage": t.string().optional(),
        }
    ).named(renames["DisableServiceRequestIn"])
    types["DisableServiceRequestOut"] = t.struct(
        {
            "disableDependentServices": t.boolean().optional(),
            "checkIfServiceHasUsage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableServiceRequestOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
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
    types["DocumentationIn"] = t.struct(
        {
            "summary": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "summary": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "displayName": t.string().optional(),
            "type": t.string(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "displayName": t.string().optional(),
            "type": t.string(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
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
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "provided": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "provided": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["BatchEnableServicesRequestIn"] = t.struct(
        {"serviceIds": t.array(t.string()).optional()}
    ).named(renames["BatchEnableServicesRequestIn"])
    types["BatchEnableServicesRequestOut"] = t.struct(
        {
            "serviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchEnableServicesRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["PublishingIn"] = t.struct(
        {
            "docTagPrefix": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "githubLabel": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "organization": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "documentationUri": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "docTagPrefix": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "githubLabel": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "organization": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "documentationUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
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
    types["AuthenticationRuleIn"] = t.struct(
        {
            "allowWithoutCredential": t.boolean().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
            "selector": t.string().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "allowWithoutCredential": t.boolean().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "selector": t.string().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
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
    types["HttpRuleIn"] = t.struct(
        {
            "get": t.string().optional(),
            "post": t.string().optional(),
            "delete": t.string().optional(),
            "body": t.string().optional(),
            "selector": t.string().optional(),
            "put": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "responseBody": t.string().optional(),
            "patch": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "get": t.string().optional(),
            "post": t.string().optional(),
            "delete": t.string().optional(),
            "body": t.string().optional(),
            "selector": t.string().optional(),
            "put": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "responseBody": t.string().optional(),
            "patch": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
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
    types["UpdateAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateAdminQuotaPolicyMetadataIn"])
    types["UpdateAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateAdminQuotaPolicyMetadataOut"])
    types["TermsOfServiceIn"] = t.struct(
        {"title": t.string().optional(), "uri": t.string().optional()}
    ).named(renames["TermsOfServiceIn"])
    types["TermsOfServiceOut"] = t.struct(
        {
            "title": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TermsOfServiceOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["DeleteAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteAdminQuotaPolicyMetadataIn"])
    types["DeleteAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteAdminQuotaPolicyMetadataOut"])
    types["ConsumerPolicyIn"] = t.struct(
        {
            "enableRules": t.array(t.proxy(renames["EnableRuleIn"])).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["ConsumerPolicyIn"])
    types["ConsumerPolicyOut"] = t.struct(
        {
            "enableRules": t.array(t.proxy(renames["EnableRuleOut"])).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerPolicyOut"])
    types["ApiIn"] = t.struct(
        {
            "version": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "version": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["ServiceValueIn"] = t.struct(
        {
            "dnsAddress": t.string().optional(),
            "name": t.string().optional(),
            "tos": t.array(t.proxy(renames["TermsOfServiceIn"])).optional(),
            "pricingLink": t.string().optional(),
        }
    ).named(renames["ServiceValueIn"])
    types["ServiceValueOut"] = t.struct(
        {
            "dnsAddress": t.string().optional(),
            "name": t.string().optional(),
            "tos": t.array(t.proxy(renames["TermsOfServiceOut"])).optional(),
            "pricingLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceValueOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
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
    types["EnumIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "edition": t.string().optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "edition": t.string().optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "authorizationUrl": t.string().optional(),
            "audiences": t.string().optional(),
            "jwksUri": t.string().optional(),
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "authorizationUrl": t.string().optional(),
            "audiences": t.string().optional(),
            "jwksUri": t.string().optional(),
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["DisableServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["GoogleApiServiceusageV1ServiceIn"]).optional()}
    ).named(renames["DisableServiceResponseIn"])
    types["DisableServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableServiceResponseOut"])
    types["ImportAdminQuotaPoliciesResponseIn"] = t.struct(
        {"policies": t.array(t.proxy(renames["AdminQuotaPolicyIn"])).optional()}
    ).named(renames["ImportAdminQuotaPoliciesResponseIn"])
    types["ImportAdminQuotaPoliciesResponseOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["AdminQuotaPolicyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAdminQuotaPoliciesResponseOut"])
    types["OperationMetadataIn"] = t.struct(
        {"resourceNames": t.array(t.string()).optional()}
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["EnableServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["GoogleApiServiceusageV1ServiceIn"]).optional()}
    ).named(renames["EnableServiceResponseIn"])
    types["EnableServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableServiceResponseOut"])
    types["AddEnableRulesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddEnableRulesMetadataIn"]
    )
    types["AddEnableRulesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddEnableRulesMetadataOut"])
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
    types["UpdateConsumerPolicyLROMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateConsumerPolicyLROMetadataIn"])
    types["UpdateConsumerPolicyLROMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateConsumerPolicyLROMetadataOut"])
    types["TypeIn"] = t.struct(
        {
            "edition": t.string().optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "oneofs": t.array(t.string()).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "edition": t.string().optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "oneofs": t.array(t.string()).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["ImportAdminQuotaPoliciesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAdminQuotaPoliciesMetadataIn"])
    types["ImportAdminQuotaPoliciesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAdminQuotaPoliciesMetadataOut"])
    types["JwtLocationIn"] = t.struct(
        {
            "query": t.string().optional(),
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "query": t.string().optional(),
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])

    functions = {}
    functions["servicesDisable"] = serviceusage.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesBatchEnable"] = serviceusage.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = serviceusage.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = serviceusage.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesBatchGet"] = serviceusage.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesEnable"] = serviceusage.post(
        "v1/{name}:enable",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = serviceusage.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = serviceusage.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = serviceusage.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = serviceusage.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="serviceusage",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
