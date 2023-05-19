from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_serviceusage() -> Import:
    serviceusage = HTTPRuntime("https://serviceusage.googleapis.com/")

    renames = {
        "ErrorResponse": "_serviceusage_1_ErrorResponse",
        "JwtLocationIn": "_serviceusage_2_JwtLocationIn",
        "JwtLocationOut": "_serviceusage_3_JwtLocationOut",
        "PythonSettingsIn": "_serviceusage_4_PythonSettingsIn",
        "PythonSettingsOut": "_serviceusage_5_PythonSettingsOut",
        "JavaSettingsIn": "_serviceusage_6_JavaSettingsIn",
        "JavaSettingsOut": "_serviceusage_7_JavaSettingsOut",
        "CustomErrorIn": "_serviceusage_8_CustomErrorIn",
        "CustomErrorOut": "_serviceusage_9_CustomErrorOut",
        "CustomHttpPatternIn": "_serviceusage_10_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_serviceusage_11_CustomHttpPatternOut",
        "BatchEnableServicesRequestIn": "_serviceusage_12_BatchEnableServicesRequestIn",
        "BatchEnableServicesRequestOut": "_serviceusage_13_BatchEnableServicesRequestOut",
        "BillingIn": "_serviceusage_14_BillingIn",
        "BillingOut": "_serviceusage_15_BillingOut",
        "ImportAdminOverridesResponseIn": "_serviceusage_16_ImportAdminOverridesResponseIn",
        "ImportAdminOverridesResponseOut": "_serviceusage_17_ImportAdminOverridesResponseOut",
        "RemoveEnableRulesMetadataIn": "_serviceusage_18_RemoveEnableRulesMetadataIn",
        "RemoveEnableRulesMetadataOut": "_serviceusage_19_RemoveEnableRulesMetadataOut",
        "GetServiceIdentityResponseIn": "_serviceusage_20_GetServiceIdentityResponseIn",
        "GetServiceIdentityResponseOut": "_serviceusage_21_GetServiceIdentityResponseOut",
        "MetricDescriptorIn": "_serviceusage_22_MetricDescriptorIn",
        "MetricDescriptorOut": "_serviceusage_23_MetricDescriptorOut",
        "ListOperationsResponseIn": "_serviceusage_24_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_serviceusage_25_ListOperationsResponseOut",
        "SourceContextIn": "_serviceusage_26_SourceContextIn",
        "SourceContextOut": "_serviceusage_27_SourceContextOut",
        "BatchCreateConsumerOverridesResponseIn": "_serviceusage_28_BatchCreateConsumerOverridesResponseIn",
        "BatchCreateConsumerOverridesResponseOut": "_serviceusage_29_BatchCreateConsumerOverridesResponseOut",
        "ClientLibrarySettingsIn": "_serviceusage_30_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_serviceusage_31_ClientLibrarySettingsOut",
        "AddEnableRulesMetadataIn": "_serviceusage_32_AddEnableRulesMetadataIn",
        "AddEnableRulesMetadataOut": "_serviceusage_33_AddEnableRulesMetadataOut",
        "MethodIn": "_serviceusage_34_MethodIn",
        "MethodOut": "_serviceusage_35_MethodOut",
        "GoSettingsIn": "_serviceusage_36_GoSettingsIn",
        "GoSettingsOut": "_serviceusage_37_GoSettingsOut",
        "FieldIn": "_serviceusage_38_FieldIn",
        "FieldOut": "_serviceusage_39_FieldOut",
        "GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn": "_serviceusage_40_GoogleApiServiceusageV1beta1GetServiceIdentityResponseIn",
        "GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut": "_serviceusage_41_GoogleApiServiceusageV1beta1GetServiceIdentityResponseOut",
        "QuotaLimitIn": "_serviceusage_42_QuotaLimitIn",
        "QuotaLimitOut": "_serviceusage_43_QuotaLimitOut",
        "SystemParameterIn": "_serviceusage_44_SystemParameterIn",
        "SystemParameterOut": "_serviceusage_45_SystemParameterOut",
        "EnableRuleIn": "_serviceusage_46_EnableRuleIn",
        "EnableRuleOut": "_serviceusage_47_EnableRuleOut",
        "PageIn": "_serviceusage_48_PageIn",
        "PageOut": "_serviceusage_49_PageOut",
        "DocumentationRuleIn": "_serviceusage_50_DocumentationRuleIn",
        "DocumentationRuleOut": "_serviceusage_51_DocumentationRuleOut",
        "EnableFailureIn": "_serviceusage_52_EnableFailureIn",
        "EnableFailureOut": "_serviceusage_53_EnableFailureOut",
        "HttpIn": "_serviceusage_54_HttpIn",
        "HttpOut": "_serviceusage_55_HttpOut",
        "GoogleApiServiceusageV1ServiceIn": "_serviceusage_56_GoogleApiServiceusageV1ServiceIn",
        "GoogleApiServiceusageV1ServiceOut": "_serviceusage_57_GoogleApiServiceusageV1ServiceOut",
        "OperationIn": "_serviceusage_58_OperationIn",
        "OperationOut": "_serviceusage_59_OperationOut",
        "SourceInfoIn": "_serviceusage_60_SourceInfoIn",
        "SourceInfoOut": "_serviceusage_61_SourceInfoOut",
        "BatchEnableServicesResponseIn": "_serviceusage_62_BatchEnableServicesResponseIn",
        "BatchEnableServicesResponseOut": "_serviceusage_63_BatchEnableServicesResponseOut",
        "CommonLanguageSettingsIn": "_serviceusage_64_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_serviceusage_65_CommonLanguageSettingsOut",
        "DeleteAdminQuotaPolicyMetadataIn": "_serviceusage_66_DeleteAdminQuotaPolicyMetadataIn",
        "DeleteAdminQuotaPolicyMetadataOut": "_serviceusage_67_DeleteAdminQuotaPolicyMetadataOut",
        "EnumIn": "_serviceusage_68_EnumIn",
        "EnumOut": "_serviceusage_69_EnumOut",
        "BackendIn": "_serviceusage_70_BackendIn",
        "BackendOut": "_serviceusage_71_BackendOut",
        "PhpSettingsIn": "_serviceusage_72_PhpSettingsIn",
        "PhpSettingsOut": "_serviceusage_73_PhpSettingsOut",
        "DisableServiceResponseIn": "_serviceusage_74_DisableServiceResponseIn",
        "DisableServiceResponseOut": "_serviceusage_75_DisableServiceResponseOut",
        "ContextRuleIn": "_serviceusage_76_ContextRuleIn",
        "ContextRuleOut": "_serviceusage_77_ContextRuleOut",
        "AuthProviderIn": "_serviceusage_78_AuthProviderIn",
        "AuthProviderOut": "_serviceusage_79_AuthProviderOut",
        "QuotaIn": "_serviceusage_80_QuotaIn",
        "QuotaOut": "_serviceusage_81_QuotaOut",
        "UsageIn": "_serviceusage_82_UsageIn",
        "UsageOut": "_serviceusage_83_UsageOut",
        "GoogleApiServiceusageV1beta1ServiceIdentityIn": "_serviceusage_84_GoogleApiServiceusageV1beta1ServiceIdentityIn",
        "GoogleApiServiceusageV1beta1ServiceIdentityOut": "_serviceusage_85_GoogleApiServiceusageV1beta1ServiceIdentityOut",
        "GoogleApiServiceusageV1ServiceConfigIn": "_serviceusage_86_GoogleApiServiceusageV1ServiceConfigIn",
        "GoogleApiServiceusageV1ServiceConfigOut": "_serviceusage_87_GoogleApiServiceusageV1ServiceConfigOut",
        "NodeSettingsIn": "_serviceusage_88_NodeSettingsIn",
        "NodeSettingsOut": "_serviceusage_89_NodeSettingsOut",
        "EmptyIn": "_serviceusage_90_EmptyIn",
        "EmptyOut": "_serviceusage_91_EmptyOut",
        "DotnetSettingsIn": "_serviceusage_92_DotnetSettingsIn",
        "DotnetSettingsOut": "_serviceusage_93_DotnetSettingsOut",
        "CreateAdminQuotaPolicyMetadataIn": "_serviceusage_94_CreateAdminQuotaPolicyMetadataIn",
        "CreateAdminQuotaPolicyMetadataOut": "_serviceusage_95_CreateAdminQuotaPolicyMetadataOut",
        "CppSettingsIn": "_serviceusage_96_CppSettingsIn",
        "CppSettingsOut": "_serviceusage_97_CppSettingsOut",
        "BatchCreateAdminOverridesResponseIn": "_serviceusage_98_BatchCreateAdminOverridesResponseIn",
        "BatchCreateAdminOverridesResponseOut": "_serviceusage_99_BatchCreateAdminOverridesResponseOut",
        "GroupValueIn": "_serviceusage_100_GroupValueIn",
        "GroupValueOut": "_serviceusage_101_GroupValueOut",
        "LabelDescriptorIn": "_serviceusage_102_LabelDescriptorIn",
        "LabelDescriptorOut": "_serviceusage_103_LabelDescriptorOut",
        "MonitoringIn": "_serviceusage_104_MonitoringIn",
        "MonitoringOut": "_serviceusage_105_MonitoringOut",
        "EnableServiceRequestIn": "_serviceusage_106_EnableServiceRequestIn",
        "EnableServiceRequestOut": "_serviceusage_107_EnableServiceRequestOut",
        "CustomErrorRuleIn": "_serviceusage_108_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_serviceusage_109_CustomErrorRuleOut",
        "ImportAdminOverridesMetadataIn": "_serviceusage_110_ImportAdminOverridesMetadataIn",
        "ImportAdminOverridesMetadataOut": "_serviceusage_111_ImportAdminOverridesMetadataOut",
        "ListServicesResponseIn": "_serviceusage_112_ListServicesResponseIn",
        "ListServicesResponseOut": "_serviceusage_113_ListServicesResponseOut",
        "AuthenticationRuleIn": "_serviceusage_114_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_serviceusage_115_AuthenticationRuleOut",
        "OperationMetadataIn": "_serviceusage_116_OperationMetadataIn",
        "OperationMetadataOut": "_serviceusage_117_OperationMetadataOut",
        "ImportConsumerOverridesResponseIn": "_serviceusage_118_ImportConsumerOverridesResponseIn",
        "ImportConsumerOverridesResponseOut": "_serviceusage_119_ImportConsumerOverridesResponseOut",
        "ServiceValueIn": "_serviceusage_120_ServiceValueIn",
        "ServiceValueOut": "_serviceusage_121_ServiceValueOut",
        "GetServiceIdentityMetadataIn": "_serviceusage_122_GetServiceIdentityMetadataIn",
        "GetServiceIdentityMetadataOut": "_serviceusage_123_GetServiceIdentityMetadataOut",
        "MixinIn": "_serviceusage_124_MixinIn",
        "MixinOut": "_serviceusage_125_MixinOut",
        "AuthRequirementIn": "_serviceusage_126_AuthRequirementIn",
        "AuthRequirementOut": "_serviceusage_127_AuthRequirementOut",
        "DocumentationIn": "_serviceusage_128_DocumentationIn",
        "DocumentationOut": "_serviceusage_129_DocumentationOut",
        "ValueInfoIn": "_serviceusage_130_ValueInfoIn",
        "ValueInfoOut": "_serviceusage_131_ValueInfoOut",
        "StatusIn": "_serviceusage_132_StatusIn",
        "StatusOut": "_serviceusage_133_StatusOut",
        "CancelOperationRequestIn": "_serviceusage_134_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_serviceusage_135_CancelOperationRequestOut",
        "AdminQuotaPolicyIn": "_serviceusage_136_AdminQuotaPolicyIn",
        "AdminQuotaPolicyOut": "_serviceusage_137_AdminQuotaPolicyOut",
        "UsageRuleIn": "_serviceusage_138_UsageRuleIn",
        "UsageRuleOut": "_serviceusage_139_UsageRuleOut",
        "GoogleApiServiceusageV1OperationMetadataIn": "_serviceusage_140_GoogleApiServiceusageV1OperationMetadataIn",
        "GoogleApiServiceusageV1OperationMetadataOut": "_serviceusage_141_GoogleApiServiceusageV1OperationMetadataOut",
        "ControlIn": "_serviceusage_142_ControlIn",
        "ControlOut": "_serviceusage_143_ControlOut",
        "AddEnableRulesResponseIn": "_serviceusage_144_AddEnableRulesResponseIn",
        "AddEnableRulesResponseOut": "_serviceusage_145_AddEnableRulesResponseOut",
        "EndpointIn": "_serviceusage_146_EndpointIn",
        "EndpointOut": "_serviceusage_147_EndpointOut",
        "LongRunningIn": "_serviceusage_148_LongRunningIn",
        "LongRunningOut": "_serviceusage_149_LongRunningOut",
        "UpdateConsumerPolicyLROMetadataIn": "_serviceusage_150_UpdateConsumerPolicyLROMetadataIn",
        "UpdateConsumerPolicyLROMetadataOut": "_serviceusage_151_UpdateConsumerPolicyLROMetadataOut",
        "TermsOfServiceIn": "_serviceusage_152_TermsOfServiceIn",
        "TermsOfServiceOut": "_serviceusage_153_TermsOfServiceOut",
        "BillingDestinationIn": "_serviceusage_154_BillingDestinationIn",
        "BillingDestinationOut": "_serviceusage_155_BillingDestinationOut",
        "MethodSettingsIn": "_serviceusage_156_MethodSettingsIn",
        "MethodSettingsOut": "_serviceusage_157_MethodSettingsOut",
        "GoogleApiServiceIn": "_serviceusage_158_GoogleApiServiceIn",
        "GoogleApiServiceOut": "_serviceusage_159_GoogleApiServiceOut",
        "ServiceIdentityIn": "_serviceusage_160_ServiceIdentityIn",
        "ServiceIdentityOut": "_serviceusage_161_ServiceIdentityOut",
        "HttpRuleIn": "_serviceusage_162_HttpRuleIn",
        "HttpRuleOut": "_serviceusage_163_HttpRuleOut",
        "ImportAdminQuotaPoliciesMetadataIn": "_serviceusage_164_ImportAdminQuotaPoliciesMetadataIn",
        "ImportAdminQuotaPoliciesMetadataOut": "_serviceusage_165_ImportAdminQuotaPoliciesMetadataOut",
        "MetricDescriptorMetadataIn": "_serviceusage_166_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_serviceusage_167_MetricDescriptorMetadataOut",
        "ContextIn": "_serviceusage_168_ContextIn",
        "ContextOut": "_serviceusage_169_ContextOut",
        "RemoveEnableRulesResponseIn": "_serviceusage_170_RemoveEnableRulesResponseIn",
        "RemoveEnableRulesResponseOut": "_serviceusage_171_RemoveEnableRulesResponseOut",
        "TypeIn": "_serviceusage_172_TypeIn",
        "TypeOut": "_serviceusage_173_TypeOut",
        "SystemParameterRuleIn": "_serviceusage_174_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_serviceusage_175_SystemParameterRuleOut",
        "ImportAdminQuotaPoliciesResponseIn": "_serviceusage_176_ImportAdminQuotaPoliciesResponseIn",
        "ImportAdminQuotaPoliciesResponseOut": "_serviceusage_177_ImportAdminQuotaPoliciesResponseOut",
        "OAuthRequirementsIn": "_serviceusage_178_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_serviceusage_179_OAuthRequirementsOut",
        "LogDescriptorIn": "_serviceusage_180_LogDescriptorIn",
        "LogDescriptorOut": "_serviceusage_181_LogDescriptorOut",
        "MetricRuleIn": "_serviceusage_182_MetricRuleIn",
        "MetricRuleOut": "_serviceusage_183_MetricRuleOut",
        "LoggingIn": "_serviceusage_184_LoggingIn",
        "LoggingOut": "_serviceusage_185_LoggingOut",
        "PublishingIn": "_serviceusage_186_PublishingIn",
        "PublishingOut": "_serviceusage_187_PublishingOut",
        "MonitoringDestinationIn": "_serviceusage_188_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_serviceusage_189_MonitoringDestinationOut",
        "MonitoredResourceDescriptorIn": "_serviceusage_190_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_serviceusage_191_MonitoredResourceDescriptorOut",
        "EnableServiceResponseIn": "_serviceusage_192_EnableServiceResponseIn",
        "EnableServiceResponseOut": "_serviceusage_193_EnableServiceResponseOut",
        "UpdateAdminQuotaPolicyMetadataIn": "_serviceusage_194_UpdateAdminQuotaPolicyMetadataIn",
        "UpdateAdminQuotaPolicyMetadataOut": "_serviceusage_195_UpdateAdminQuotaPolicyMetadataOut",
        "DisableServiceRequestIn": "_serviceusage_196_DisableServiceRequestIn",
        "DisableServiceRequestOut": "_serviceusage_197_DisableServiceRequestOut",
        "EnumValueIn": "_serviceusage_198_EnumValueIn",
        "EnumValueOut": "_serviceusage_199_EnumValueOut",
        "SystemParametersIn": "_serviceusage_200_SystemParametersIn",
        "SystemParametersOut": "_serviceusage_201_SystemParametersOut",
        "ConsumerPolicyIn": "_serviceusage_202_ConsumerPolicyIn",
        "ConsumerPolicyOut": "_serviceusage_203_ConsumerPolicyOut",
        "AuthenticationIn": "_serviceusage_204_AuthenticationIn",
        "AuthenticationOut": "_serviceusage_205_AuthenticationOut",
        "ImportConsumerOverridesMetadataIn": "_serviceusage_206_ImportConsumerOverridesMetadataIn",
        "ImportConsumerOverridesMetadataOut": "_serviceusage_207_ImportConsumerOverridesMetadataOut",
        "OptionIn": "_serviceusage_208_OptionIn",
        "OptionOut": "_serviceusage_209_OptionOut",
        "ApiIn": "_serviceusage_210_ApiIn",
        "ApiOut": "_serviceusage_211_ApiOut",
        "LoggingDestinationIn": "_serviceusage_212_LoggingDestinationIn",
        "LoggingDestinationOut": "_serviceusage_213_LoggingDestinationOut",
        "BackendRuleIn": "_serviceusage_214_BackendRuleIn",
        "BackendRuleOut": "_serviceusage_215_BackendRuleOut",
        "BatchGetServicesResponseIn": "_serviceusage_216_BatchGetServicesResponseIn",
        "BatchGetServicesResponseOut": "_serviceusage_217_BatchGetServicesResponseOut",
        "RubySettingsIn": "_serviceusage_218_RubySettingsIn",
        "RubySettingsOut": "_serviceusage_219_RubySettingsOut",
        "QuotaOverrideIn": "_serviceusage_220_QuotaOverrideIn",
        "QuotaOverrideOut": "_serviceusage_221_QuotaOverrideOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["JwtLocationIn"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "query": t.string().optional(),
            "cookie": t.string().optional(),
            "header": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "query": t.string().optional(),
            "cookie": t.string().optional(),
            "header": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
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
        {"kind": t.string().optional(), "path": t.string().optional()}
    ).named(renames["CustomHttpPatternIn"])
    types["CustomHttpPatternOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomHttpPatternOut"])
    types["BatchEnableServicesRequestIn"] = t.struct(
        {"serviceIds": t.array(t.string()).optional()}
    ).named(renames["BatchEnableServicesRequestIn"])
    types["BatchEnableServicesRequestOut"] = t.struct(
        {
            "serviceIds": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchEnableServicesRequestOut"])
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
    types["ImportAdminOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["ImportAdminOverridesResponseIn"])
    types["ImportAdminOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAdminOverridesResponseOut"])
    types["RemoveEnableRulesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveEnableRulesMetadataIn"]
    )
    types["RemoveEnableRulesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveEnableRulesMetadataOut"])
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
    types["MetricDescriptorIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "valueType": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "displayName": t.string().optional(),
            "metricKind": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "valueType": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "displayName": t.string().optional(),
            "metricKind": t.string().optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["BatchCreateConsumerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["BatchCreateConsumerOverridesResponseIn"])
    types["BatchCreateConsumerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateConsumerOverridesResponseOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "launchStage": t.string().optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["AddEnableRulesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddEnableRulesMetadataIn"]
    )
    types["AddEnableRulesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddEnableRulesMetadataOut"])
    types["MethodIn"] = t.struct(
        {
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "requestTypeUrl": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "requestTypeUrl": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["FieldIn"] = t.struct(
        {
            "packed": t.boolean().optional(),
            "name": t.string().optional(),
            "typeUrl": t.string().optional(),
            "kind": t.string().optional(),
            "defaultValue": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "number": t.integer().optional(),
            "jsonName": t.string().optional(),
            "cardinality": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "packed": t.boolean().optional(),
            "name": t.string().optional(),
            "typeUrl": t.string().optional(),
            "kind": t.string().optional(),
            "defaultValue": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "number": t.integer().optional(),
            "jsonName": t.string().optional(),
            "cardinality": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
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
    types["QuotaLimitIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "freeTier": t.string().optional(),
            "metric": t.string().optional(),
            "description": t.string().optional(),
            "duration": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "maxLimit": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "freeTier": t.string().optional(),
            "metric": t.string().optional(),
            "description": t.string().optional(),
            "duration": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "maxLimit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
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
    types["EnableRuleIn"] = t.struct(
        {
            "enableType": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["EnableRuleIn"])
    types["EnableRuleOut"] = t.struct(
        {
            "enableType": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "groups": t.array(t.string()).optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableRuleOut"])
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
    types["DocumentationRuleIn"] = t.struct(
        {
            "disableReplacementWords": t.string().optional(),
            "description": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "disableReplacementWords": t.string().optional(),
            "description": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
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
    types["GoogleApiServiceusageV1ServiceIn"] = t.struct(
        {
            "name": t.string().optional(),
            "config": t.proxy(
                renames["GoogleApiServiceusageV1ServiceConfigIn"]
            ).optional(),
            "parent": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceIn"])
    types["GoogleApiServiceusageV1ServiceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "config": t.proxy(
                renames["GoogleApiServiceusageV1ServiceConfigOut"]
            ).optional(),
            "parent": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
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
    types["DeleteAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteAdminQuotaPolicyMetadataIn"])
    types["DeleteAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteAdminQuotaPolicyMetadataOut"])
    types["EnumIn"] = t.struct(
        {
            "edition": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "edition": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
    types["DisableServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["GoogleApiServiceusageV1ServiceIn"]).optional()}
    ).named(renames["DisableServiceResponseIn"])
    types["DisableServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableServiceResponseOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "authorizationUrl": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "audiences": t.string().optional(),
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "authorizationUrl": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "audiences": t.string().optional(),
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
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
    types["UsageIn"] = t.struct(
        {
            "producerNotificationChannel": t.string().optional(),
            "requirements": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["UsageRuleIn"])).optional(),
        }
    ).named(renames["UsageIn"])
    types["UsageOut"] = t.struct(
        {
            "producerNotificationChannel": t.string().optional(),
            "requirements": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["UsageRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageOut"])
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
    types["GoogleApiServiceusageV1ServiceConfigIn"] = t.struct(
        {
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "title": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "name": t.string().optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceConfigIn"])
    types["GoogleApiServiceusageV1ServiceConfigOut"] = t.struct(
        {
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "title": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "name": t.string().optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1ServiceConfigOut"])
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["CreateAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CreateAdminQuotaPolicyMetadataIn"])
    types["CreateAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateAdminQuotaPolicyMetadataOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["BatchCreateAdminOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["BatchCreateAdminOverridesResponseIn"])
    types["BatchCreateAdminOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchCreateAdminOverridesResponseOut"])
    types["GroupValueIn"] = t.struct({"name": t.string().optional()}).named(
        renames["GroupValueIn"]
    )
    types["GroupValueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupValueOut"])
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
    types["EnableServiceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EnableServiceRequestIn"]
    )
    types["EnableServiceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableServiceRequestOut"])
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
    types["ImportAdminOverridesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAdminOverridesMetadataIn"])
    types["ImportAdminOverridesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAdminOverridesMetadataOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {"resourceNames": t.array(t.string()).optional()}
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ImportConsumerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["QuotaOverrideIn"])).optional()}
    ).named(renames["ImportConsumerOverridesResponseIn"])
    types["ImportConsumerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(t.proxy(renames["QuotaOverrideOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportConsumerOverridesResponseOut"])
    types["ServiceValueIn"] = t.struct(
        {
            "tos": t.array(t.proxy(renames["TermsOfServiceIn"])).optional(),
            "dnsAddress": t.string().optional(),
            "name": t.string().optional(),
            "pricingLink": t.string().optional(),
        }
    ).named(renames["ServiceValueIn"])
    types["ServiceValueOut"] = t.struct(
        {
            "tos": t.array(t.proxy(renames["TermsOfServiceOut"])).optional(),
            "dnsAddress": t.string().optional(),
            "name": t.string().optional(),
            "pricingLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceValueOut"])
    types["GetServiceIdentityMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GetServiceIdentityMetadataIn"])
    types["GetServiceIdentityMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GetServiceIdentityMetadataOut"])
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
    types["DocumentationIn"] = t.struct(
        {
            "serviceRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
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
            "summary": t.string().optional(),
            "overview": t.string().optional(),
            "documentationRootUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["ValueInfoIn"] = t.struct(
        {
            "learnmoreLink": t.string().optional(),
            "title": t.string().optional(),
            "summary": t.string().optional(),
            "groupValue": t.proxy(renames["GroupValueIn"]).optional(),
            "serviceValue": t.proxy(renames["ServiceValueIn"]).optional(),
        }
    ).named(renames["ValueInfoIn"])
    types["ValueInfoOut"] = t.struct(
        {
            "learnmoreLink": t.string().optional(),
            "title": t.string().optional(),
            "summary": t.string().optional(),
            "groupValue": t.proxy(renames["GroupValueOut"]).optional(),
            "serviceValue": t.proxy(renames["ServiceValueOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueInfoOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["AdminQuotaPolicyIn"] = t.struct(
        {
            "container": t.string().optional(),
            "unit": t.string().optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "policyValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AdminQuotaPolicyIn"])
    types["AdminQuotaPolicyOut"] = t.struct(
        {
            "container": t.string().optional(),
            "unit": t.string().optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "policyValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdminQuotaPolicyOut"])
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
    types["GoogleApiServiceusageV1OperationMetadataIn"] = t.struct(
        {"resourceNames": t.array(t.string()).optional()}
    ).named(renames["GoogleApiServiceusageV1OperationMetadataIn"])
    types["GoogleApiServiceusageV1OperationMetadataOut"] = t.struct(
        {
            "resourceNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceusageV1OperationMetadataOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
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
    types["UpdateConsumerPolicyLROMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateConsumerPolicyLROMetadataIn"])
    types["UpdateConsumerPolicyLROMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateConsumerPolicyLROMetadataOut"])
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
    types["GoogleApiServiceIn"] = t.struct(
        {
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "producerProjectId": t.string().optional(),
            "name": t.string().optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "title": t.string().optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "configVersion": t.integer().optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "id": t.string().optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
        }
    ).named(renames["GoogleApiServiceIn"])
    types["GoogleApiServiceOut"] = t.struct(
        {
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "producerProjectId": t.string().optional(),
            "name": t.string().optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "title": t.string().optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "configVersion": t.integer().optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "id": t.string().optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleApiServiceOut"])
    types["ServiceIdentityIn"] = t.struct(
        {"uniqueId": t.string().optional(), "email": t.string().optional()}
    ).named(renames["ServiceIdentityIn"])
    types["ServiceIdentityOut"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceIdentityOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "patch": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "put": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "selector": t.string().optional(),
            "post": t.string().optional(),
            "get": t.string().optional(),
            "body": t.string().optional(),
            "responseBody": t.string().optional(),
            "delete": t.string().optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "patch": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "put": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "selector": t.string().optional(),
            "post": t.string().optional(),
            "get": t.string().optional(),
            "body": t.string().optional(),
            "responseBody": t.string().optional(),
            "delete": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["ImportAdminQuotaPoliciesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportAdminQuotaPoliciesMetadataIn"])
    types["ImportAdminQuotaPoliciesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportAdminQuotaPoliciesMetadataOut"])
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
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["RemoveEnableRulesResponseIn"] = t.struct(
        {"parent": t.string().optional()}
    ).named(renames["RemoveEnableRulesResponseIn"])
    types["RemoveEnableRulesResponseOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveEnableRulesResponseOut"])
    types["TypeIn"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "edition": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "name": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "edition": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "name": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["ImportAdminQuotaPoliciesResponseIn"] = t.struct(
        {"policies": t.array(t.proxy(renames["AdminQuotaPolicyIn"])).optional()}
    ).named(renames["ImportAdminQuotaPoliciesResponseIn"])
    types["ImportAdminQuotaPoliciesResponseOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["AdminQuotaPolicyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportAdminQuotaPoliciesResponseOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
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
    types["PublishingIn"] = t.struct(
        {
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "githubLabel": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "organization": t.string().optional(),
            "documentationUri": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "githubLabel": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "organization": t.string().optional(),
            "documentationUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
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
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "type": t.string(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "type": t.string(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["EnableServiceResponseIn"] = t.struct(
        {"service": t.proxy(renames["GoogleApiServiceusageV1ServiceIn"]).optional()}
    ).named(renames["EnableServiceResponseIn"])
    types["EnableServiceResponseOut"] = t.struct(
        {
            "service": t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableServiceResponseOut"])
    types["UpdateAdminQuotaPolicyMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateAdminQuotaPolicyMetadataIn"])
    types["UpdateAdminQuotaPolicyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateAdminQuotaPolicyMetadataOut"])
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
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["ConsumerPolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "enableRules": t.array(t.proxy(renames["EnableRuleIn"])).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["ConsumerPolicyIn"])
    types["ConsumerPolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "enableRules": t.array(t.proxy(renames["EnableRuleOut"])).optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerPolicyOut"])
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
    types["ImportConsumerOverridesMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ImportConsumerOverridesMetadataIn"])
    types["ImportConsumerOverridesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ImportConsumerOverridesMetadataOut"])
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
    types["ApiIn"] = t.struct(
        {
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "version": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "version": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
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
    types["BackendRuleIn"] = t.struct(
        {
            "disableAuth": t.boolean().optional(),
            "jwtAudience": t.string().optional(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
            "minDeadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "deadline": t.number().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "pathTranslation": t.string(),
            "address": t.string().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "disableAuth": t.boolean().optional(),
            "jwtAudience": t.string().optional(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
            "minDeadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "deadline": t.number().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "pathTranslation": t.string(),
            "address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
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
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["QuotaOverrideIn"] = t.struct(
        {
            "adminOverrideAncestor": t.string().optional(),
            "overrideValue": t.string().optional(),
            "name": t.string().optional(),
            "unit": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["QuotaOverrideIn"])
    types["QuotaOverrideOut"] = t.struct(
        {
            "adminOverrideAncestor": t.string().optional(),
            "overrideValue": t.string().optional(),
            "name": t.string().optional(),
            "unit": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaOverrideOut"])

    functions = {}
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
    functions["operationsDelete"] = serviceusage.get(
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
    functions["servicesEnable"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesBatchEnable"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDisable"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesBatchGet"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesList"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesGet"] = serviceusage.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleApiServiceusageV1ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="serviceusage",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
