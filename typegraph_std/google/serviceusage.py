from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_serviceusage():
    serviceusage = HTTPRuntime("https://serviceusage.googleapis.com/")

    renames = {
        "ErrorResponse": "_serviceusage_1_ErrorResponse",
        "ContextRuleIn": "_serviceusage_2_ContextRuleIn",
        "ContextRuleOut": "_serviceusage_3_ContextRuleOut",
        "JwtLocationIn": "_serviceusage_4_JwtLocationIn",
        "JwtLocationOut": "_serviceusage_5_JwtLocationOut",
        "JavaSettingsIn": "_serviceusage_6_JavaSettingsIn",
        "JavaSettingsOut": "_serviceusage_7_JavaSettingsOut",
        "DotnetSettingsIn": "_serviceusage_8_DotnetSettingsIn",
        "DotnetSettingsOut": "_serviceusage_9_DotnetSettingsOut",
        "GoogleApiServiceusageV1ServiceConfigIn": "_serviceusage_10_GoogleApiServiceusageV1ServiceConfigIn",
        "GoogleApiServiceusageV1ServiceConfigOut": "_serviceusage_11_GoogleApiServiceusageV1ServiceConfigOut",
        "LongRunningIn": "_serviceusage_12_LongRunningIn",
        "LongRunningOut": "_serviceusage_13_LongRunningOut",
        "RemoveEnableRulesResponseIn": "_serviceusage_14_RemoveEnableRulesResponseIn",
        "RemoveEnableRulesResponseOut": "_serviceusage_15_RemoveEnableRulesResponseOut",
        "MonitoringDestinationIn": "_serviceusage_16_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_serviceusage_17_MonitoringDestinationOut",
        "GoogleApiServiceusageV1beta1ServiceIdentityIn": "_serviceusage_18_GoogleApiServiceusageV1beta1ServiceIdentityIn",
        "GoogleApiServiceusageV1beta1ServiceIdentityOut": "_serviceusage_19_GoogleApiServiceusageV1beta1ServiceIdentityOut",
        "DeleteAdminQuotaPolicyMetadataIn": "_serviceusage_20_DeleteAdminQuotaPolicyMetadataIn",
        "DeleteAdminQuotaPolicyMetadataOut": "_serviceusage_21_DeleteAdminQuotaPolicyMetadataOut",
        "AdminQuotaPolicyIn": "_serviceusage_22_AdminQuotaPolicyIn",
        "AdminQuotaPolicyOut": "_serviceusage_23_AdminQuotaPolicyOut",
        "EnumIn": "_serviceusage_24_EnumIn",
        "EnumOut": "_serviceusage_25_EnumOut",
        "AuthRequirementIn": "_serviceusage_26_AuthRequirementIn",
        "AuthRequirementOut": "_serviceusage_27_AuthRequirementOut",
        "SourceContextIn": "_serviceusage_28_SourceContextIn",
        "SourceContextOut": "_serviceusage_29_SourceContextOut",
        "LogDescriptorIn": "_serviceusage_30_LogDescriptorIn",
        "LogDescriptorOut": "_serviceusage_31_LogDescriptorOut",
        "AuthenticationRuleIn": "_serviceusage_32_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_serviceusage_33_AuthenticationRuleOut",
        "EnableServiceResponseIn": "_serviceusage_34_EnableServiceResponseIn",
        "EnableServiceResponseOut": "_serviceusage_35_EnableServiceResponseOut",
        "CreateAdminQuotaPolicyMetadataIn": "_serviceusage_36_CreateAdminQuotaPolicyMetadataIn",
        "CreateAdminQuotaPolicyMetadataOut": "_serviceusage_37_CreateAdminQuotaPolicyMetadataOut",
        "UpdateAdminQuotaPolicyMetadataIn": "_serviceusage_38_UpdateAdminQuotaPolicyMetadataIn",
        "UpdateAdminQuotaPolicyMetadataOut": "_serviceusage_39_UpdateAdminQuotaPolicyMetadataOut",
        "ImportConsumerOverridesMetadataIn": "_serviceusage_40_ImportConsumerOverridesMetadataIn",
        "ImportConsumerOverridesMetadataOut": "_serviceusage_41_ImportConsumerOverridesMetadataOut",
        "DisableServiceRequestIn": "_serviceusage_42_DisableServiceRequestIn",
        "DisableServiceRequestOut": "_serviceusage_43_DisableServiceRequestOut",
        "ImportAdminOverridesResponseIn": "_serviceusage_44_ImportAdminOverridesResponseIn",
        "ImportAdminOverridesResponseOut": "_serviceusage_45_ImportAdminOverridesResponseOut",
        "LoggingIn": "_serviceusage_46_LoggingIn",
        "LoggingOut": "_serviceusage_47_LoggingOut",
        "CommonLanguageSettingsIn": "_serviceusage_48_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_serviceusage_49_CommonLanguageSettingsOut",
        "UpdateConsumerPolicyLROMetadataIn": "_serviceusage_50_UpdateConsumerPolicyLROMetadataIn",
        "UpdateConsumerPolicyLROMetadataOut": "_serviceusage_51_UpdateConsumerPolicyLROMetadataOut",
        "OptionIn": "_serviceusage_52_OptionIn",
        "OptionOut": "_serviceusage_53_OptionOut",
        "AuthenticationIn": "_serviceusage_54_AuthenticationIn",
        "AuthenticationOut": "_serviceusage_55_AuthenticationOut",
        "MetricDescriptorIn": "_serviceusage_56_MetricDescriptorIn",
        "MetricDescriptorOut": "_serviceusage_57_MetricDescriptorOut",
        "CustomHttpPatternIn": "_serviceusage_58_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_serviceusage_59_CustomHttpPatternOut",
        "ControlIn": "_serviceusage_60_ControlIn",
        "ControlOut": "_serviceusage_61_ControlOut",
        "MixinIn": "_serviceusage_62_MixinIn",
        "MixinOut": "_serviceusage_63_MixinOut",
        "GoogleApiServiceIn": "_serviceusage_64_GoogleApiServiceIn",
        "GoogleApiServiceOut": "_serviceusage_65_GoogleApiServiceOut",
        "AuthProviderIn": "_serviceusage_66_AuthProviderIn",
        "AuthProviderOut": "_serviceusage_67_AuthProviderOut",
        "MonitoredResourceDescriptorIn": "_serviceusage_68_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_serviceusage_69_MonitoredResourceDescriptorOut",
        "HttpIn": "_serviceusage_70_HttpIn",
        "HttpOut": "_serviceusage_71_HttpOut",
        "BillingDestinationIn": "_serviceusage_72_BillingDestinationIn",
        "BillingDestinationOut": "_serviceusage_73_BillingDestinationOut",
        "QuotaLimitIn": "_serviceusage_74_QuotaLimitIn",
        "QuotaLimitOut": "_serviceusage_75_QuotaLimitOut",
        "DocumentationIn": "_serviceusage_76_DocumentationIn",
        "DocumentationOut": "_serviceusage_77_DocumentationOut",
        "BatchCreateAdminOverridesResponseIn": "_serviceusage_78_BatchCreateAdminOverridesResponseIn",
        "BatchCreateAdminOverridesResponseOut": "_serviceusage_79_BatchCreateAdminOverridesResponseOut",
        "CppSettingsIn": "_serviceusage_80_CppSettingsIn",
        "CppSettingsOut": "_serviceusage_81_CppSettingsOut",
        "DocumentationRuleIn": "_serviceusage_82_DocumentationRuleIn",
        "DocumentationRuleOut": "_serviceusage_83_DocumentationRuleOut",
        "CustomErrorRuleIn": "_serviceusage_84_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_serviceusage_85_CustomErrorRuleOut",
        "PhpSettingsIn": "_serviceusage_86_PhpSettingsIn",
        "PhpSettingsOut": "_serviceusage_87_PhpSettingsOut",
        "BackendIn": "_serviceusage_88_BackendIn",
        "BackendOut": "_serviceusage_89_BackendOut",
        "EnumValueIn": "_serviceusage_90_EnumValueIn",
        "EnumValueOut": "_serviceusage_91_EnumValueOut",
        "CancelOperationRequestIn": "_serviceusage_92_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_serviceusage_93_CancelOperationRequestOut",
        "ListOperationsResponseIn": "_serviceusage_94_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_serviceusage_95_ListOperationsResponseOut",
        "MethodIn": "_serviceusage_96_MethodIn",
        "MethodOut": "_serviceusage_97_MethodOut",
        "StatusIn": "_serviceusage_98_StatusIn",
        "StatusOut": "_serviceusage_99_StatusOut",
        "ClientLibrarySettingsIn": "_serviceusage_100_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_serviceusage_101_ClientLibrarySettingsOut",
        "AddEnableRulesResponseIn": "_serviceusage_102_AddEnableRulesResponseIn",
        "AddEnableRulesResponseOut": "_serviceusage_103_AddEnableRulesResponseOut",
        "EnableRuleIn": "_serviceusage_104_EnableRuleIn",
        "EnableRuleOut": "_serviceusage_105_EnableRuleOut",
        "BillingIn": "_serviceusage_106_BillingIn",
        "BillingOut": "_serviceusage_107_BillingOut",
        "HttpRuleIn": "_serviceusage_108_HttpRuleIn",
        "HttpRuleOut": "_serviceusage_109_HttpRuleOut",
        "SystemParameterRuleIn": "_serviceusage_110_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_serviceusage_111_SystemParameterRuleOut",
        "UsageIn": "_serviceusage_112_UsageIn",
        "UsageOut": "_serviceusage_113_UsageOut",
        "GoSettingsIn": "_serviceusage_114_GoSettingsIn",
        "GoSettingsOut": "_serviceusage_115_GoSettingsOut",
        "MonitoringIn": "_serviceusage_116_MonitoringIn",
        "MonitoringOut": "_serviceusage_117_MonitoringOut",
        "BatchGetServicesResponseIn": "_serviceusage_118_BatchGetServicesResponseIn",
        "BatchGetServicesResponseOut": "_serviceusage_119_BatchGetServicesResponseOut",
        "ImportAdminQuotaPoliciesResponseIn": "_serviceusage_120_ImportAdminQuotaPoliciesResponseIn",
        "ImportAdminQuotaPoliciesResponseOut": "_serviceusage_121_ImportAdminQuotaPoliciesResponseOut",
        "SourceInfoIn": "_serviceusage_122_SourceInfoIn",
        "SourceInfoOut": "_serviceusage_123_SourceInfoOut",
        "ServiceIdentityIn": "_serviceusage_124_ServiceIdentityIn",
        "ServiceIdentityOut": "_serviceusage_125_ServiceIdentityOut",
        "AddEnableRulesMetadataIn": "_serviceusage_126_AddEnableRulesMetadataIn",
        "AddEnableRulesMetadataOut": "_serviceusage_127_AddEnableRulesMetadataOut",
        "UsageRuleIn": "_serviceusage_128_UsageRuleIn",
        "UsageRuleOut": "_serviceusage_129_UsageRuleOut",
        "GoogleApiServiceusageV1OperationMetadataIn": "_serviceusage_130_GoogleApiServiceusageV1OperationMetadataIn",
        "GoogleApiServiceusageV1OperationMetadataOut": "_serviceusage_131_GoogleApiServiceusageV1OperationMetadataOut",
        "SystemParameterIn": "_serviceusage_132_SystemParameterIn",
        "SystemParameterOut": "_serviceusage_133_SystemParameterOut",
        "ListServicesResponseIn": "_serviceusage_134_ListServicesResponseIn",
        "ListServicesResponseOut": "_serviceusage_135_ListServicesResponseOut",
        "ConsumerPolicyIn": "_serviceusage_136_ConsumerPolicyIn",
        "ConsumerPolicyOut": "_serviceusage_137_ConsumerPolicyOut",
        "OperationMetadataIn": "_serviceusage_138_OperationMetadataIn",
        "OperationMetadataOut": "_serviceusage_139_OperationMetadataOut",
        "MetricRuleIn": "_serviceusage_140_MetricRuleIn",
        "MetricRuleOut": "_serviceusage_141_MetricRuleOut",
        "BackendRuleIn": "_serviceusage_142_BackendRuleIn",
        "BackendRuleOut": "_serviceusage_143_BackendRuleOut",
        "PythonSettingsIn": "_serviceusage_144_PythonSettingsIn",
        "PythonSettingsOut": "_serviceusage_145_PythonSettingsOut",
        "ImportAdminQuotaPoliciesMetadataIn": "_serviceusage_146_ImportAdminQuotaPoliciesMetadataIn",
        "ImportAdminQuotaPoliciesMetadataOut": "_serviceusage_147_ImportAdminQuotaPoliciesMetadataOut",
        "RubySettingsIn": "_serviceusage_148_RubySettingsIn",
        "RubySettingsOut": "_serviceusage_149_RubySettingsOut",
        "BatchEnableServicesRequestIn": "_serviceusage_150_BatchEnableServicesRequestIn",
        "BatchEnableServicesRequestOut": "_serviceusage_151_BatchEnableServicesRequestOut",
        "EmptyIn": "_serviceusage_152_EmptyIn",
        "EmptyOut": "_serviceusage_153_EmptyOut",
        "QuotaIn": "_serviceusage_154_QuotaIn",
        "QuotaOut": "_serviceusage_155_QuotaOut",
        "MethodSettingsIn": "_serviceusage_156_MethodSettingsIn",
        "MethodSettingsOut": "_serviceusage_157_MethodSettingsOut",
        "BatchEnableServicesResponseIn": "_serviceusage_158_BatchEnableServicesResponseIn",
        "BatchEnableServicesResponseOut": "_serviceusage_159_BatchEnableServicesResponseOut",
        "FieldIn": "_serviceusage_160_FieldIn",
        "FieldOut": "_serviceusage_161_FieldOut",
        "TypeIn": "_serviceusage_162_TypeIn",
        "TypeOut": "_serviceusage_163_TypeOut",
        "GoogleApiServiceusageV1ServiceIn": "_serviceusage_164_GoogleApiServiceusageV1ServiceIn",
        "GoogleApiServiceusageV1ServiceOut": "_serviceusage_165_GoogleApiServiceusageV1ServiceOut",
        "EnableServiceRequestIn": "_serviceusage_166_EnableServiceRequestIn",
        "EnableServiceRequestOut": "_serviceusage_167_EnableServiceRequestOut",
        "SystemParametersIn": "_serviceusage_168_SystemParametersIn",
        "SystemParametersOut": "_serviceusage_169_SystemParametersOut",
        "ApiIn": "_serviceusage_170_ApiIn",
        "ApiOut": "_serviceusage_171_ApiOut",
        "ContextIn": "_serviceusage_172_ContextIn",
        "ContextOut": "_serviceusage_173_ContextOut",
        "OAuthRequirementsIn": "_serviceusage_174_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_serviceusage_175_OAuthRequirementsOut",
        "GetServiceIdentityResponseIn": "_serviceusage_176_GetServiceIdentityResponseIn",
        "GetServiceIdentityResponseOut": "_serviceusage_177_GetServiceIdentityResponseOut",
        "ImportConsumerOverridesResponseIn": "_serviceusage_178_ImportConsumerOverridesResponseIn",
        "ImportConsumerOverridesResponseOut": "_serviceusage_179_ImportConsumerOverridesResponseOut",
        "LoggingDestinationIn": "_serviceusage_180_LoggingDestinationIn",
        "LoggingDestinationOut": "_serviceusage_181_LoggingDestinationOut",
        "QuotaOverrideIn": "_serviceusage_182_QuotaOverrideIn",
        "QuotaOverrideOut": "_serviceusage_183_QuotaOverrideOut",
        "PageIn": "_serviceusage_184_PageIn",
        "PageOut": "_serviceusage_185_PageOut",
        "NodeSettingsIn": "_serviceusage_186_NodeSettingsIn",
        "NodeSettingsOut": "_serviceusage_187_NodeSettingsOut",
        "GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn": "_serviceusage_188_GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn",
        "GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut": "_serviceusage_189_GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut",
        "EndpointIn": "_serviceusage_190_EndpointIn",
        "EndpointOut": "_serviceusage_191_EndpointOut",
        "MetricDescriptorMetadataIn": "_serviceusage_192_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_serviceusage_193_MetricDescriptorMetadataOut",
        "DisableServiceResponseIn": "_serviceusage_194_DisableServiceResponseIn",
        "DisableServiceResponseOut": "_serviceusage_195_DisableServiceResponseOut",
        "GetServiceIdentityMetadataIn": "_serviceusage_196_GetServiceIdentityMetadataIn",
        "GetServiceIdentityMetadataOut": "_serviceusage_197_GetServiceIdentityMetadataOut",
        "LabelDescriptorIn": "_serviceusage_198_LabelDescriptorIn",
        "LabelDescriptorOut": "_serviceusage_199_LabelDescriptorOut",
        "CustomErrorIn": "_serviceusage_200_CustomErrorIn",
        "CustomErrorOut": "_serviceusage_201_CustomErrorOut",
        "EnableFailureIn": "_serviceusage_202_EnableFailureIn",
        "EnableFailureOut": "_serviceusage_203_EnableFailureOut",
        "PublishingIn": "_serviceusage_204_PublishingIn",
        "PublishingOut": "_serviceusage_205_PublishingOut",
        "ImportAdminOverridesMetadataIn": "_serviceusage_206_ImportAdminOverridesMetadataIn",
        "ImportAdminOverridesMetadataOut": "_serviceusage_207_ImportAdminOverridesMetadataOut",
        "RemoveEnableRulesMetadataIn": "_serviceusage_208_RemoveEnableRulesMetadataIn",
        "RemoveEnableRulesMetadataOut": "_serviceusage_209_RemoveEnableRulesMetadataOut",
        "OperationIn": "_serviceusage_210_OperationIn",
        "OperationOut": "_serviceusage_211_OperationOut",
        "BatchCreateConsumerOverridesResponseIn": "_serviceusage_212_BatchCreateConsumerOverridesResponseIn",
        "BatchCreateConsumerOverridesResponseOut": "_serviceusage_213_BatchCreateConsumerOverridesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ContextRuleIn"] = t.struct(
        {
            "requested": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "requested": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["JwtLocationIn"] = t.struct(
        {
            "cookie": t.string().optional(),
            "query": t.string().optional(),
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "cookie": t.string().optional(),
            "query": t.string().optional(),
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
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
    types["DotnetSettingsIn"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["GoogleApiServiceusageV1ServiceConfigIn"] = t.struct(
        {
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "name": t.string().optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "title": t.string().optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceConfigIn"])
    types["GoogleApiServiceusageV1ServiceConfigOut"] = t.struct(
        {
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "name": t.string().optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "title": t.string().optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceConfigOut"])
    types["LongRunningIn"] = t.struct(
        {
            "initialPollDelay": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "totalPollTimeout": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "initialPollDelay": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "totalPollTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["RemoveEnableRulesResponseIn"] = t.struct(
        {
            "removedValues": t.array(t.string()).optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["RemoveEnableRulesResponseIn"])
    types["RemoveEnableRulesResponseOut"] = t.struct(
        {
            "removedValues": t.array(t.string()).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveEnableRulesResponseOut"])
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
    types["GoogleApiServiceusageV1beta1ServiceIdentityIn"] = t.struct(
        {"uniqueId": t.string().optional(), "email": t.string().optional()}
    ).named(renames["GoogleApiServiceusageV1beta1ServiceIdentityIn"])
    types["GoogleApiServiceusageV1beta1ServiceIdentityOut"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1beta1ServiceIdentityOut"])
    types["DeleteAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteAdminQuotaPolicyMetadataIn"])
    types["DeleteAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteAdminQuotaPolicyMetadataOut"])
    types["AdminQuotaPolicyIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "policyValue": t.string().optional(),
            "name": t.string().optional(),
            "container": t.string().optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["AdminQuotaPolicyIn"])
    types["AdminQuotaPolicyOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "policyValue": t.string().optional(),
            "name": t.string().optional(),
            "container": t.string().optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminQuotaPolicyOut"])
    types["EnumIn"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "edition": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "edition": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
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
    types["LogDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
    types["AuthenticationRuleIn"] = t.struct(
        {
            "allowWithoutCredential": t.boolean().optional(),
            "selector": t.string().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "allowWithoutCredential": t.boolean().optional(),
            "selector": t.string().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
    types["EnableServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["GoogleApiServiceusageV1ServiceIn"]).optional()}
    ).named(renames["EnableServiceResponseIn"])
    types["EnableServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableServiceResponseOut"])
    types["CreateAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateAdminQuotaPolicyMetadataIn"])
    types["CreateAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateAdminQuotaPolicyMetadataOut"])
    types["UpdateAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateAdminQuotaPolicyMetadataIn"])
    types["UpdateAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateAdminQuotaPolicyMetadataOut"])
    types["ImportConsumerOverridesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportConsumerOverridesMetadataIn"])
    types["ImportConsumerOverridesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportConsumerOverridesMetadataOut"])
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
    types["ImportAdminOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["ImportAdminOverridesResponseIn"])
    types["ImportAdminOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAdminOverridesResponseOut"])
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
    types["UpdateConsumerPolicyLROMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateConsumerPolicyLROMetadataIn"])
    types["UpdateConsumerPolicyLROMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateConsumerPolicyLROMetadataOut"])
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
    types["MetricDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
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
    types["GoogleApiServiceIn"] = t.struct(
        {
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "configVersion": t.integer().optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "producerProjectId": t.string().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "id": t.string().optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
        }
    ).named(renames["GoogleApiServiceIn"])
    types["GoogleApiServiceOut"] = t.struct(
        {
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "configVersion": t.integer().optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "producerProjectId": t.string().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "id": t.string().optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "authorizationUrl": t.string().optional(),
            "issuer": t.string().optional(),
            "jwksUri": t.string().optional(),
            "audiences": t.string().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "authorizationUrl": t.string().optional(),
            "issuer": t.string().optional(),
            "jwksUri": t.string().optional(),
            "audiences": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "type": t.string(),
            "displayName": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "type": t.string(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
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
    types["QuotaLimitIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "unit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "freeTier": t.string().optional(),
            "maxLimit": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "unit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "freeTier": t.string().optional(),
            "maxLimit": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["DocumentationIn"] = t.struct(
        {
            "serviceRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "sectionOverrides": t.array(t.proxy(renames["PageIn"])).optional(),
            "summary": t.string().optional(),
            "overview": t.string().optional(),
            "documentationRootUrl": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "serviceRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "sectionOverrides": t.array(t.proxy(renames["PageOut"])).optional(),
            "summary": t.string().optional(),
            "overview": t.string().optional(),
            "documentationRootUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["BatchCreateAdminOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["BatchCreateAdminOverridesResponseIn"])
    types["BatchCreateAdminOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateAdminOverridesResponseOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
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
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
            "syntax": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
            "name": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "responseTypeUrl": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "syntax": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
            "name": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "responseTypeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "launchStage": t.string().optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "version": t.string().optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "version": t.string().optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["AddEnableRulesResponseIn"] = t.struct(
        {"addedValues": t.array(t.string()).optional(), "parent": t.string().optional()}
    ).named(renames["AddEnableRulesResponseIn"])
    types["AddEnableRulesResponseOut"] = t.struct(
        {
            "addedValues": t.array(t.string()).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddEnableRulesResponseOut"])
    types["EnableRuleIn"] = t.struct(
        {
            "enableType": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
            "services": t.array(t.string()).optional(),
        }
    ).named(renames["EnableRuleIn"])
    types["EnableRuleOut"] = t.struct(
        {
            "enableType": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
            "services": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableRuleOut"])
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
    types["HttpRuleIn"] = t.struct(
        {
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "delete": t.string().optional(),
            "responseBody": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "body": t.string().optional(),
            "post": t.string().optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "delete": t.string().optional(),
            "responseBody": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "body": t.string().optional(),
            "post": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
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
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
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
    types["ImportAdminQuotaPoliciesResponseIn"] = t.struct(
        {"policies": t.array(t.proxy(renames["AdminQuotaPolicyIn"])).optional()}
    ).named(renames["ImportAdminQuotaPoliciesResponseIn"])
    types["ImportAdminQuotaPoliciesResponseOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["AdminQuotaPolicyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAdminQuotaPoliciesResponseOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
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
    types["AddEnableRulesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddEnableRulesMetadataIn"]
    )
    types["AddEnableRulesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddEnableRulesMetadataOut"])
    types["UsageRuleIn"] = t.struct(
        {
            "skipServiceControl": t.boolean().optional(),
            "selector": t.string().optional(),
            "allowUnregisteredCalls": t.boolean().optional(),
        }
    ).named(renames["UsageRuleIn"])
    types["UsageRuleOut"] = t.struct(
        {
            "skipServiceControl": t.boolean().optional(),
            "selector": t.string().optional(),
            "allowUnregisteredCalls": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageRuleOut"])
    types["GoogleApiServiceusageV1OperationMetadataIn"] = t.struct(
        {"resourceNames": t.array(t.string()).optional()}
    ).named(renames["GoogleApiServiceusageV1OperationMetadataIn"])
    types["GoogleApiServiceusageV1OperationMetadataOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1OperationMetadataOut"])
    types["SystemParameterIn"] = t.struct(
        {
            "httpHeader": t.string().optional(),
            "urlQueryParameter": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SystemParameterIn"])
    types["SystemParameterOut"] = t.struct(
        {
            "httpHeader": t.string().optional(),
            "urlQueryParameter": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParameterOut"])
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
    types["ConsumerPolicyIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "enableRules": t.array(t.proxy(renames["EnableRuleIn"])).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ConsumerPolicyIn"])
    types["ConsumerPolicyOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "enableRules": t.array(t.proxy(renames["EnableRuleOut"])).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerPolicyOut"])
    types["OperationMetadataIn"] = t.struct(
        {"resourceNames": t.array(t.string()).optional()}
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["BackendRuleIn"] = t.struct(
        {
            "disableAuth": t.boolean().optional(),
            "protocol": t.string().optional(),
            "minDeadline": t.number().optional(),
            "selector": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "deadline": t.number().optional(),
            "address": t.string().optional(),
            "operationDeadline": t.number().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "disableAuth": t.boolean().optional(),
            "protocol": t.string().optional(),
            "minDeadline": t.number().optional(),
            "selector": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "deadline": t.number().optional(),
            "address": t.string().optional(),
            "operationDeadline": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
    types["ImportAdminQuotaPoliciesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAdminQuotaPoliciesMetadataIn"])
    types["ImportAdminQuotaPoliciesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAdminQuotaPoliciesMetadataOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["BatchEnableServicesRequestIn"] = t.struct(
        {"serviceIds": t.array(t.string()).optional()}
    ).named(renames["BatchEnableServicesRequestIn"])
    types["BatchEnableServicesRequestOut"] = t.struct(
        {
            "serviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchEnableServicesRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["BatchEnableServicesResponseIn"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceIn"])
            ).optional(),
            "failures": t.array(t.proxy(renames["EnableFailureIn"])).optional(),
        }
    ).named(renames["BatchEnableServicesResponseIn"])
    types["BatchEnableServicesResponseOut"] = t.struct(
        {
            "services": t.array(
                t.proxy(renames["GoogleApiServiceusageV1ServiceOut"])
            ).optional(),
            "failures": t.array(t.proxy(renames["EnableFailureOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchEnableServicesResponseOut"])
    types["FieldIn"] = t.struct(
        {
            "name": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "kind": t.string().optional(),
            "packed": t.boolean().optional(),
            "typeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "jsonName": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "name": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "kind": t.string().optional(),
            "packed": t.boolean().optional(),
            "typeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "jsonName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["TypeIn"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "syntax": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "syntax": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["GoogleApiServiceusageV1ServiceIn"] = t.struct(
        {
            "config": t.proxy(
                renames["GoogleApiServiceusageV1ServiceConfigIn"]
            ).optional(),
            "state": t.string().optional(),
            "parent": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceIn"])
    types["GoogleApiServiceusageV1ServiceOut"] = t.struct(
        {
            "config": t.proxy(
                renames["GoogleApiServiceusageV1ServiceConfigOut"]
            ).optional(),
            "state": t.string().optional(),
            "parent": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceOut"])
    types["EnableServiceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableServiceRequestIn"]
    )
    types["EnableServiceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableServiceRequestOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["ApiIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "version": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "version": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
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
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
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
    types["ImportConsumerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["ImportConsumerOverridesResponseIn"])
    types["ImportConsumerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportConsumerOverridesResponseOut"])
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
    types["QuotaOverrideIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
            "adminOverrideAncestor": t.string().optional(),
            "overrideValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["QuotaOverrideIn"])
    types["QuotaOverrideOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
            "adminOverrideAncestor": t.string().optional(),
            "overrideValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOverrideOut"])
    types["PageIn"] = t.struct(
        {
            "content": t.string().optional(),
            "name": t.string().optional(),
            "subpages": t.array(t.proxy(renames["PageIn"])).optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "content": t.string().optional(),
            "name": t.string().optional(),
            "subpages": t.array(t.proxy(renames["PageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
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
    types["EndpointIn"] = t.struct(
        {
            "target": t.string().optional(),
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "allowCors": t.boolean().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "target": t.string().optional(),
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "allowCors": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["DisableServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["GoogleApiServiceusageV1ServiceIn"]).optional()}
    ).named(renames["DisableServiceResponseIn"])
    types["DisableServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableServiceResponseOut"])
    types["GetServiceIdentityMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetServiceIdentityMetadataIn"])
    types["GetServiceIdentityMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GetServiceIdentityMetadataOut"])
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
    types["PublishingIn"] = t.struct(
        {
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "githubLabel": t.string().optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "documentationUri": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "newIssueUri": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "githubLabel": t.string().optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "documentationUri": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["ImportAdminOverridesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAdminOverridesMetadataIn"])
    types["ImportAdminOverridesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAdminOverridesMetadataOut"])
    types["RemoveEnableRulesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveEnableRulesMetadataIn"]
    )
    types["RemoveEnableRulesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveEnableRulesMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["BatchCreateConsumerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["BatchCreateConsumerOverridesResponseIn"])
    types["BatchCreateConsumerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateConsumerOverridesResponseOut"])

    functions = {}
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
    functions["operationsList"] = serviceusage.get(
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

    return Import(
        importer="serviceusage",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
