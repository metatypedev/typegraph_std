from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_serviceconsumermanagement() -> Import:
    serviceconsumermanagement = HTTPRuntime(
        "https://serviceconsumermanagement.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_serviceconsumermanagement_1_ErrorResponse",
        "BackendRuleIn": "_serviceconsumermanagement_2_BackendRuleIn",
        "BackendRuleOut": "_serviceconsumermanagement_3_BackendRuleOut",
        "UndeleteTenantProjectRequestIn": "_serviceconsumermanagement_4_UndeleteTenantProjectRequestIn",
        "UndeleteTenantProjectRequestOut": "_serviceconsumermanagement_5_UndeleteTenantProjectRequestOut",
        "AddTenantProjectRequestIn": "_serviceconsumermanagement_6_AddTenantProjectRequestIn",
        "AddTenantProjectRequestOut": "_serviceconsumermanagement_7_AddTenantProjectRequestOut",
        "ControlIn": "_serviceconsumermanagement_8_ControlIn",
        "ControlOut": "_serviceconsumermanagement_9_ControlOut",
        "QuotaLimitIn": "_serviceconsumermanagement_10_QuotaLimitIn",
        "QuotaLimitOut": "_serviceconsumermanagement_11_QuotaLimitOut",
        "MethodIn": "_serviceconsumermanagement_12_MethodIn",
        "MethodOut": "_serviceconsumermanagement_13_MethodOut",
        "V1Beta1ImportProducerQuotaPoliciesResponseIn": "_serviceconsumermanagement_14_V1Beta1ImportProducerQuotaPoliciesResponseIn",
        "V1Beta1ImportProducerQuotaPoliciesResponseOut": "_serviceconsumermanagement_15_V1Beta1ImportProducerQuotaPoliciesResponseOut",
        "CustomHttpPatternIn": "_serviceconsumermanagement_16_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_serviceconsumermanagement_17_CustomHttpPatternOut",
        "JwtLocationIn": "_serviceconsumermanagement_18_JwtLocationIn",
        "JwtLocationOut": "_serviceconsumermanagement_19_JwtLocationOut",
        "LoggingIn": "_serviceconsumermanagement_20_LoggingIn",
        "LoggingOut": "_serviceconsumermanagement_21_LoggingOut",
        "EnumIn": "_serviceconsumermanagement_22_EnumIn",
        "EnumOut": "_serviceconsumermanagement_23_EnumOut",
        "MonitoringIn": "_serviceconsumermanagement_24_MonitoringIn",
        "MonitoringOut": "_serviceconsumermanagement_25_MonitoringOut",
        "ClientLibrarySettingsIn": "_serviceconsumermanagement_26_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_serviceconsumermanagement_27_ClientLibrarySettingsOut",
        "OperationIn": "_serviceconsumermanagement_28_OperationIn",
        "OperationOut": "_serviceconsumermanagement_29_OperationOut",
        "ServiceIn": "_serviceconsumermanagement_30_ServiceIn",
        "ServiceOut": "_serviceconsumermanagement_31_ServiceOut",
        "V1RemoveVisibilityLabelsResponseIn": "_serviceconsumermanagement_32_V1RemoveVisibilityLabelsResponseIn",
        "V1RemoveVisibilityLabelsResponseOut": "_serviceconsumermanagement_33_V1RemoveVisibilityLabelsResponseOut",
        "CustomErrorIn": "_serviceconsumermanagement_34_CustomErrorIn",
        "CustomErrorOut": "_serviceconsumermanagement_35_CustomErrorOut",
        "V1Beta1RefreshConsumerResponseIn": "_serviceconsumermanagement_36_V1Beta1RefreshConsumerResponseIn",
        "V1Beta1RefreshConsumerResponseOut": "_serviceconsumermanagement_37_V1Beta1RefreshConsumerResponseOut",
        "FieldIn": "_serviceconsumermanagement_38_FieldIn",
        "FieldOut": "_serviceconsumermanagement_39_FieldOut",
        "TenantProjectConfigIn": "_serviceconsumermanagement_40_TenantProjectConfigIn",
        "TenantProjectConfigOut": "_serviceconsumermanagement_41_TenantProjectConfigOut",
        "HttpRuleIn": "_serviceconsumermanagement_42_HttpRuleIn",
        "HttpRuleOut": "_serviceconsumermanagement_43_HttpRuleOut",
        "RubySettingsIn": "_serviceconsumermanagement_44_RubySettingsIn",
        "RubySettingsOut": "_serviceconsumermanagement_45_RubySettingsOut",
        "V1EnableConsumerResponseIn": "_serviceconsumermanagement_46_V1EnableConsumerResponseIn",
        "V1EnableConsumerResponseOut": "_serviceconsumermanagement_47_V1EnableConsumerResponseOut",
        "LongRunningIn": "_serviceconsumermanagement_48_LongRunningIn",
        "LongRunningOut": "_serviceconsumermanagement_49_LongRunningOut",
        "ServiceAccountConfigIn": "_serviceconsumermanagement_50_ServiceAccountConfigIn",
        "ServiceAccountConfigOut": "_serviceconsumermanagement_51_ServiceAccountConfigOut",
        "ContextRuleIn": "_serviceconsumermanagement_52_ContextRuleIn",
        "ContextRuleOut": "_serviceconsumermanagement_53_ContextRuleOut",
        "MetricDescriptorMetadataIn": "_serviceconsumermanagement_54_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_serviceconsumermanagement_55_MetricDescriptorMetadataOut",
        "BackendIn": "_serviceconsumermanagement_56_BackendIn",
        "BackendOut": "_serviceconsumermanagement_57_BackendOut",
        "MonitoredResourceDescriptorIn": "_serviceconsumermanagement_58_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_serviceconsumermanagement_59_MonitoredResourceDescriptorOut",
        "SourceContextIn": "_serviceconsumermanagement_60_SourceContextIn",
        "SourceContextOut": "_serviceconsumermanagement_61_SourceContextOut",
        "DotnetSettingsIn": "_serviceconsumermanagement_62_DotnetSettingsIn",
        "DotnetSettingsOut": "_serviceconsumermanagement_63_DotnetSettingsOut",
        "EmptyIn": "_serviceconsumermanagement_64_EmptyIn",
        "EmptyOut": "_serviceconsumermanagement_65_EmptyOut",
        "LabelDescriptorIn": "_serviceconsumermanagement_66_LabelDescriptorIn",
        "LabelDescriptorOut": "_serviceconsumermanagement_67_LabelDescriptorOut",
        "AuthProviderIn": "_serviceconsumermanagement_68_AuthProviderIn",
        "AuthProviderOut": "_serviceconsumermanagement_69_AuthProviderOut",
        "BillingConfigIn": "_serviceconsumermanagement_70_BillingConfigIn",
        "BillingConfigOut": "_serviceconsumermanagement_71_BillingConfigOut",
        "MetricRuleIn": "_serviceconsumermanagement_72_MetricRuleIn",
        "MetricRuleOut": "_serviceconsumermanagement_73_MetricRuleOut",
        "ListOperationsResponseIn": "_serviceconsumermanagement_74_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_serviceconsumermanagement_75_ListOperationsResponseOut",
        "CustomErrorRuleIn": "_serviceconsumermanagement_76_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_serviceconsumermanagement_77_CustomErrorRuleOut",
        "ApplyTenantProjectConfigRequestIn": "_serviceconsumermanagement_78_ApplyTenantProjectConfigRequestIn",
        "ApplyTenantProjectConfigRequestOut": "_serviceconsumermanagement_79_ApplyTenantProjectConfigRequestOut",
        "DeleteTenantProjectRequestIn": "_serviceconsumermanagement_80_DeleteTenantProjectRequestIn",
        "DeleteTenantProjectRequestOut": "_serviceconsumermanagement_81_DeleteTenantProjectRequestOut",
        "JavaSettingsIn": "_serviceconsumermanagement_82_JavaSettingsIn",
        "JavaSettingsOut": "_serviceconsumermanagement_83_JavaSettingsOut",
        "ApiIn": "_serviceconsumermanagement_84_ApiIn",
        "ApiOut": "_serviceconsumermanagement_85_ApiOut",
        "SystemParameterRuleIn": "_serviceconsumermanagement_86_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_serviceconsumermanagement_87_SystemParameterRuleOut",
        "AuthRequirementIn": "_serviceconsumermanagement_88_AuthRequirementIn",
        "AuthRequirementOut": "_serviceconsumermanagement_89_AuthRequirementOut",
        "PageIn": "_serviceconsumermanagement_90_PageIn",
        "PageOut": "_serviceconsumermanagement_91_PageOut",
        "V1GenerateDefaultIdentityResponseIn": "_serviceconsumermanagement_92_V1GenerateDefaultIdentityResponseIn",
        "V1GenerateDefaultIdentityResponseOut": "_serviceconsumermanagement_93_V1GenerateDefaultIdentityResponseOut",
        "OAuthRequirementsIn": "_serviceconsumermanagement_94_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_serviceconsumermanagement_95_OAuthRequirementsOut",
        "ListTenancyUnitsResponseIn": "_serviceconsumermanagement_96_ListTenancyUnitsResponseIn",
        "ListTenancyUnitsResponseOut": "_serviceconsumermanagement_97_ListTenancyUnitsResponseOut",
        "V1RefreshConsumerResponseIn": "_serviceconsumermanagement_98_V1RefreshConsumerResponseIn",
        "V1RefreshConsumerResponseOut": "_serviceconsumermanagement_99_V1RefreshConsumerResponseOut",
        "RemoveTenantProjectRequestIn": "_serviceconsumermanagement_100_RemoveTenantProjectRequestIn",
        "RemoveTenantProjectRequestOut": "_serviceconsumermanagement_101_RemoveTenantProjectRequestOut",
        "TenantProjectPolicyIn": "_serviceconsumermanagement_102_TenantProjectPolicyIn",
        "TenantProjectPolicyOut": "_serviceconsumermanagement_103_TenantProjectPolicyOut",
        "PythonSettingsIn": "_serviceconsumermanagement_104_PythonSettingsIn",
        "PythonSettingsOut": "_serviceconsumermanagement_105_PythonSettingsOut",
        "V1GenerateServiceAccountResponseIn": "_serviceconsumermanagement_106_V1GenerateServiceAccountResponseIn",
        "V1GenerateServiceAccountResponseOut": "_serviceconsumermanagement_107_V1GenerateServiceAccountResponseOut",
        "ContextIn": "_serviceconsumermanagement_108_ContextIn",
        "ContextOut": "_serviceconsumermanagement_109_ContextOut",
        "CreateTenancyUnitRequestIn": "_serviceconsumermanagement_110_CreateTenancyUnitRequestIn",
        "CreateTenancyUnitRequestOut": "_serviceconsumermanagement_111_CreateTenancyUnitRequestOut",
        "V1Beta1BatchCreateProducerOverridesResponseIn": "_serviceconsumermanagement_112_V1Beta1BatchCreateProducerOverridesResponseIn",
        "V1Beta1BatchCreateProducerOverridesResponseOut": "_serviceconsumermanagement_113_V1Beta1BatchCreateProducerOverridesResponseOut",
        "CancelOperationRequestIn": "_serviceconsumermanagement_114_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_serviceconsumermanagement_115_CancelOperationRequestOut",
        "V1DisableConsumerResponseIn": "_serviceconsumermanagement_116_V1DisableConsumerResponseIn",
        "V1DisableConsumerResponseOut": "_serviceconsumermanagement_117_V1DisableConsumerResponseOut",
        "SourceInfoIn": "_serviceconsumermanagement_118_SourceInfoIn",
        "SourceInfoOut": "_serviceconsumermanagement_119_SourceInfoOut",
        "UsageRuleIn": "_serviceconsumermanagement_120_UsageRuleIn",
        "UsageRuleOut": "_serviceconsumermanagement_121_UsageRuleOut",
        "V1Beta1ImportProducerOverridesResponseIn": "_serviceconsumermanagement_122_V1Beta1ImportProducerOverridesResponseIn",
        "V1Beta1ImportProducerOverridesResponseOut": "_serviceconsumermanagement_123_V1Beta1ImportProducerOverridesResponseOut",
        "V1Beta1EnableConsumerResponseIn": "_serviceconsumermanagement_124_V1Beta1EnableConsumerResponseIn",
        "V1Beta1EnableConsumerResponseOut": "_serviceconsumermanagement_125_V1Beta1EnableConsumerResponseOut",
        "AuthenticationIn": "_serviceconsumermanagement_126_AuthenticationIn",
        "AuthenticationOut": "_serviceconsumermanagement_127_AuthenticationOut",
        "PhpSettingsIn": "_serviceconsumermanagement_128_PhpSettingsIn",
        "PhpSettingsOut": "_serviceconsumermanagement_129_PhpSettingsOut",
        "MixinIn": "_serviceconsumermanagement_130_MixinIn",
        "MixinOut": "_serviceconsumermanagement_131_MixinOut",
        "V1Beta1ServiceIdentityIn": "_serviceconsumermanagement_132_V1Beta1ServiceIdentityIn",
        "V1Beta1ServiceIdentityOut": "_serviceconsumermanagement_133_V1Beta1ServiceIdentityOut",
        "V1Beta1QuotaOverrideIn": "_serviceconsumermanagement_134_V1Beta1QuotaOverrideIn",
        "V1Beta1QuotaOverrideOut": "_serviceconsumermanagement_135_V1Beta1QuotaOverrideOut",
        "TenantResourceIn": "_serviceconsumermanagement_136_TenantResourceIn",
        "TenantResourceOut": "_serviceconsumermanagement_137_TenantResourceOut",
        "CppSettingsIn": "_serviceconsumermanagement_138_CppSettingsIn",
        "CppSettingsOut": "_serviceconsumermanagement_139_CppSettingsOut",
        "UsageIn": "_serviceconsumermanagement_140_UsageIn",
        "UsageOut": "_serviceconsumermanagement_141_UsageOut",
        "AuthenticationRuleIn": "_serviceconsumermanagement_142_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_serviceconsumermanagement_143_AuthenticationRuleOut",
        "V1Beta1ProducerQuotaPolicyIn": "_serviceconsumermanagement_144_V1Beta1ProducerQuotaPolicyIn",
        "V1Beta1ProducerQuotaPolicyOut": "_serviceconsumermanagement_145_V1Beta1ProducerQuotaPolicyOut",
        "MetricDescriptorIn": "_serviceconsumermanagement_146_MetricDescriptorIn",
        "MetricDescriptorOut": "_serviceconsumermanagement_147_MetricDescriptorOut",
        "StatusIn": "_serviceconsumermanagement_148_StatusIn",
        "StatusOut": "_serviceconsumermanagement_149_StatusOut",
        "SystemParametersIn": "_serviceconsumermanagement_150_SystemParametersIn",
        "SystemParametersOut": "_serviceconsumermanagement_151_SystemParametersOut",
        "V1DefaultIdentityIn": "_serviceconsumermanagement_152_V1DefaultIdentityIn",
        "V1DefaultIdentityOut": "_serviceconsumermanagement_153_V1DefaultIdentityOut",
        "GoSettingsIn": "_serviceconsumermanagement_154_GoSettingsIn",
        "GoSettingsOut": "_serviceconsumermanagement_155_GoSettingsOut",
        "MethodSettingsIn": "_serviceconsumermanagement_156_MethodSettingsIn",
        "MethodSettingsOut": "_serviceconsumermanagement_157_MethodSettingsOut",
        "LoggingDestinationIn": "_serviceconsumermanagement_158_LoggingDestinationIn",
        "LoggingDestinationOut": "_serviceconsumermanagement_159_LoggingDestinationOut",
        "TypeIn": "_serviceconsumermanagement_160_TypeIn",
        "TypeOut": "_serviceconsumermanagement_161_TypeOut",
        "NodeSettingsIn": "_serviceconsumermanagement_162_NodeSettingsIn",
        "NodeSettingsOut": "_serviceconsumermanagement_163_NodeSettingsOut",
        "V1ServiceAccountIn": "_serviceconsumermanagement_164_V1ServiceAccountIn",
        "V1ServiceAccountOut": "_serviceconsumermanagement_165_V1ServiceAccountOut",
        "HttpIn": "_serviceconsumermanagement_166_HttpIn",
        "HttpOut": "_serviceconsumermanagement_167_HttpOut",
        "QuotaIn": "_serviceconsumermanagement_168_QuotaIn",
        "QuotaOut": "_serviceconsumermanagement_169_QuotaOut",
        "MonitoringDestinationIn": "_serviceconsumermanagement_170_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_serviceconsumermanagement_171_MonitoringDestinationOut",
        "V1Beta1GenerateServiceIdentityResponseIn": "_serviceconsumermanagement_172_V1Beta1GenerateServiceIdentityResponseIn",
        "V1Beta1GenerateServiceIdentityResponseOut": "_serviceconsumermanagement_173_V1Beta1GenerateServiceIdentityResponseOut",
        "CommonLanguageSettingsIn": "_serviceconsumermanagement_174_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_serviceconsumermanagement_175_CommonLanguageSettingsOut",
        "BillingDestinationIn": "_serviceconsumermanagement_176_BillingDestinationIn",
        "BillingDestinationOut": "_serviceconsumermanagement_177_BillingDestinationOut",
        "DocumentationRuleIn": "_serviceconsumermanagement_178_DocumentationRuleIn",
        "DocumentationRuleOut": "_serviceconsumermanagement_179_DocumentationRuleOut",
        "AttachTenantProjectRequestIn": "_serviceconsumermanagement_180_AttachTenantProjectRequestIn",
        "AttachTenantProjectRequestOut": "_serviceconsumermanagement_181_AttachTenantProjectRequestOut",
        "EnumValueIn": "_serviceconsumermanagement_182_EnumValueIn",
        "EnumValueOut": "_serviceconsumermanagement_183_EnumValueOut",
        "TenancyUnitIn": "_serviceconsumermanagement_184_TenancyUnitIn",
        "TenancyUnitOut": "_serviceconsumermanagement_185_TenancyUnitOut",
        "SystemParameterIn": "_serviceconsumermanagement_186_SystemParameterIn",
        "SystemParameterOut": "_serviceconsumermanagement_187_SystemParameterOut",
        "OptionIn": "_serviceconsumermanagement_188_OptionIn",
        "OptionOut": "_serviceconsumermanagement_189_OptionOut",
        "V1Beta1DisableConsumerResponseIn": "_serviceconsumermanagement_190_V1Beta1DisableConsumerResponseIn",
        "V1Beta1DisableConsumerResponseOut": "_serviceconsumermanagement_191_V1Beta1DisableConsumerResponseOut",
        "LogDescriptorIn": "_serviceconsumermanagement_192_LogDescriptorIn",
        "LogDescriptorOut": "_serviceconsumermanagement_193_LogDescriptorOut",
        "EndpointIn": "_serviceconsumermanagement_194_EndpointIn",
        "EndpointOut": "_serviceconsumermanagement_195_EndpointOut",
        "DocumentationIn": "_serviceconsumermanagement_196_DocumentationIn",
        "DocumentationOut": "_serviceconsumermanagement_197_DocumentationOut",
        "SearchTenancyUnitsResponseIn": "_serviceconsumermanagement_198_SearchTenancyUnitsResponseIn",
        "SearchTenancyUnitsResponseOut": "_serviceconsumermanagement_199_SearchTenancyUnitsResponseOut",
        "BillingIn": "_serviceconsumermanagement_200_BillingIn",
        "BillingOut": "_serviceconsumermanagement_201_BillingOut",
        "PolicyBindingIn": "_serviceconsumermanagement_202_PolicyBindingIn",
        "PolicyBindingOut": "_serviceconsumermanagement_203_PolicyBindingOut",
        "PublishingIn": "_serviceconsumermanagement_204_PublishingIn",
        "PublishingOut": "_serviceconsumermanagement_205_PublishingOut",
        "V1AddVisibilityLabelsResponseIn": "_serviceconsumermanagement_206_V1AddVisibilityLabelsResponseIn",
        "V1AddVisibilityLabelsResponseOut": "_serviceconsumermanagement_207_V1AddVisibilityLabelsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BackendRuleIn"] = t.struct(
        {
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "deadline": t.number().optional(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
            "jwtAudience": t.string().optional(),
            "minDeadline": t.number().optional(),
            "pathTranslation": t.string(),
            "disableAuth": t.boolean().optional(),
            "operationDeadline": t.number().optional(),
            "address": t.string().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "deadline": t.number().optional(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
            "jwtAudience": t.string().optional(),
            "minDeadline": t.number().optional(),
            "pathTranslation": t.string(),
            "disableAuth": t.boolean().optional(),
            "operationDeadline": t.number().optional(),
            "address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["UndeleteTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["UndeleteTenantProjectRequestIn"]
    )
    types["UndeleteTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteTenantProjectRequestOut"])
    types["AddTenantProjectRequestIn"] = t.struct(
        {
            "tag": t.string(),
            "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
        }
    ).named(renames["AddTenantProjectRequestIn"])
    types["AddTenantProjectRequestOut"] = t.struct(
        {
            "tag": t.string(),
            "projectConfig": t.proxy(renames["TenantProjectConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddTenantProjectRequestOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "maxLimit": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "duration": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "freeTier": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "maxLimit": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "duration": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "freeTier": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["MethodIn"] = t.struct(
        {
            "requestStreaming": t.boolean().optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "requestStreaming": t.boolean().optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["V1Beta1ImportProducerQuotaPoliciesResponseIn"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["V1Beta1ProducerQuotaPolicyIn"])
            ).optional()
        }
    ).named(renames["V1Beta1ImportProducerQuotaPoliciesResponseIn"])
    types["V1Beta1ImportProducerQuotaPoliciesResponseOut"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["V1Beta1ProducerQuotaPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1ImportProducerQuotaPoliciesResponseOut"])
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
    types["JwtLocationIn"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
            "query": t.string().optional(),
            "header": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
            "query": t.string().optional(),
            "header": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
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
    types["EnumIn"] = t.struct(
        {
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
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
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "version": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "version": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ServiceIn"] = t.struct(
        {
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "title": t.string().optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "name": t.string().optional(),
            "producerProjectId": t.string().optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "id": t.string().optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "configVersion": t.integer().optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "title": t.string().optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "name": t.string().optional(),
            "producerProjectId": t.string().optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "id": t.string().optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "configVersion": t.integer().optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["V1RemoveVisibilityLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["V1RemoveVisibilityLabelsResponseIn"])
    types["V1RemoveVisibilityLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1RemoveVisibilityLabelsResponseOut"])
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
    types["V1Beta1RefreshConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1RefreshConsumerResponseIn"])
    types["V1Beta1RefreshConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1RefreshConsumerResponseOut"])
    types["FieldIn"] = t.struct(
        {
            "name": t.string().optional(),
            "packed": t.boolean().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "jsonName": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "kind": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "typeUrl": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "name": t.string().optional(),
            "packed": t.boolean().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "jsonName": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "kind": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "typeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["TenantProjectConfigIn"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "tenantProjectPolicy": t.proxy(renames["TenantProjectPolicyIn"]).optional(),
            "serviceAccountConfig": t.proxy(
                renames["ServiceAccountConfigIn"]
            ).optional(),
            "folder": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "billingConfig": t.proxy(renames["BillingConfigIn"]).optional(),
        }
    ).named(renames["TenantProjectConfigIn"])
    types["TenantProjectConfigOut"] = t.struct(
        {
            "services": t.array(t.string()).optional(),
            "tenantProjectPolicy": t.proxy(
                renames["TenantProjectPolicyOut"]
            ).optional(),
            "serviceAccountConfig": t.proxy(
                renames["ServiceAccountConfigOut"]
            ).optional(),
            "folder": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "billingConfig": t.proxy(renames["BillingConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantProjectConfigOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "patch": t.string().optional(),
            "body": t.string().optional(),
            "get": t.string().optional(),
            "delete": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "post": t.string().optional(),
            "responseBody": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "put": t.string().optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "patch": t.string().optional(),
            "body": t.string().optional(),
            "get": t.string().optional(),
            "delete": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "post": t.string().optional(),
            "responseBody": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "put": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["V1EnableConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1EnableConsumerResponseIn"]
    )
    types["V1EnableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1EnableConsumerResponseOut"])
    types["LongRunningIn"] = t.struct(
        {
            "pollDelayMultiplier": t.number().optional(),
            "maxPollDelay": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "pollDelayMultiplier": t.number().optional(),
            "maxPollDelay": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["ServiceAccountConfigIn"] = t.struct(
        {
            "tenantProjectRoles": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
        }
    ).named(renames["ServiceAccountConfigIn"])
    types["ServiceAccountConfigOut"] = t.struct(
        {
            "tenantProjectRoles": t.array(t.string()).optional(),
            "accountId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountConfigOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "ingestDelay": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "ingestDelay": t.string().optional(),
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "name": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["AuthProviderIn"] = t.struct(
        {
            "authorizationUrl": t.string().optional(),
            "audiences": t.string().optional(),
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "id": t.string().optional(),
            "jwksUri": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "authorizationUrl": t.string().optional(),
            "audiences": t.string().optional(),
            "issuer": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "id": t.string().optional(),
            "jwksUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["BillingConfigIn"] = t.struct(
        {"billingAccount": t.string().optional()}
    ).named(renames["BillingConfigIn"])
    types["BillingConfigOut"] = t.struct(
        {
            "billingAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingConfigOut"])
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
    types["ApplyTenantProjectConfigRequestIn"] = t.struct(
        {
            "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
            "tag": t.string(),
        }
    ).named(renames["ApplyTenantProjectConfigRequestIn"])
    types["ApplyTenantProjectConfigRequestOut"] = t.struct(
        {
            "projectConfig": t.proxy(renames["TenantProjectConfigOut"]).optional(),
            "tag": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplyTenantProjectConfigRequestOut"])
    types["DeleteTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["DeleteTenantProjectRequestIn"]
    )
    types["DeleteTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTenantProjectRequestOut"])
    types["JavaSettingsIn"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "libraryPackage": t.string().optional(),
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["JavaSettingsIn"])
    types["JavaSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "libraryPackage": t.string().optional(),
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JavaSettingsOut"])
    types["ApiIn"] = t.struct(
        {
            "version": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "version": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
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
    types["PageIn"] = t.struct(
        {
            "content": t.string().optional(),
            "subpages": t.array(t.proxy(renames["PageIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["PageIn"])
    types["PageOut"] = t.struct(
        {
            "content": t.string().optional(),
            "subpages": t.array(t.proxy(renames["PageOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PageOut"])
    types["V1GenerateDefaultIdentityResponseIn"] = t.struct(
        {
            "attachStatus": t.string().optional(),
            "identity": t.proxy(renames["V1DefaultIdentityIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["V1GenerateDefaultIdentityResponseIn"])
    types["V1GenerateDefaultIdentityResponseOut"] = t.struct(
        {
            "attachStatus": t.string().optional(),
            "identity": t.proxy(renames["V1DefaultIdentityOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1GenerateDefaultIdentityResponseOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
    types["ListTenancyUnitsResponseIn"] = t.struct(
        {
            "tenancyUnits": t.array(t.proxy(renames["TenancyUnitIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTenancyUnitsResponseIn"])
    types["ListTenancyUnitsResponseOut"] = t.struct(
        {
            "tenancyUnits": t.array(t.proxy(renames["TenancyUnitOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTenancyUnitsResponseOut"])
    types["V1RefreshConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1RefreshConsumerResponseIn"]
    )
    types["V1RefreshConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1RefreshConsumerResponseOut"])
    types["RemoveTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["RemoveTenantProjectRequestIn"]
    )
    types["RemoveTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveTenantProjectRequestOut"])
    types["TenantProjectPolicyIn"] = t.struct(
        {"policyBindings": t.array(t.proxy(renames["PolicyBindingIn"])).optional()}
    ).named(renames["TenantProjectPolicyIn"])
    types["TenantProjectPolicyOut"] = t.struct(
        {
            "policyBindings": t.array(t.proxy(renames["PolicyBindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantProjectPolicyOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
    types["V1GenerateServiceAccountResponseIn"] = t.struct(
        {"account": t.proxy(renames["V1ServiceAccountIn"]).optional()}
    ).named(renames["V1GenerateServiceAccountResponseIn"])
    types["V1GenerateServiceAccountResponseOut"] = t.struct(
        {
            "account": t.proxy(renames["V1ServiceAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1GenerateServiceAccountResponseOut"])
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["CreateTenancyUnitRequestIn"] = t.struct(
        {"tenancyUnitId": t.string().optional()}
    ).named(renames["CreateTenancyUnitRequestIn"])
    types["CreateTenancyUnitRequestOut"] = t.struct(
        {
            "tenancyUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTenancyUnitRequestOut"])
    types["V1Beta1BatchCreateProducerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["V1Beta1QuotaOverrideIn"])).optional()}
    ).named(renames["V1Beta1BatchCreateProducerOverridesResponseIn"])
    types["V1Beta1BatchCreateProducerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(
                t.proxy(renames["V1Beta1QuotaOverrideOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1BatchCreateProducerOverridesResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["V1DisableConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1DisableConsumerResponseIn"]
    )
    types["V1DisableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1DisableConsumerResponseOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
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
    types["V1Beta1ImportProducerOverridesResponseIn"] = t.struct(
        {"overrides": t.array(t.proxy(renames["V1Beta1QuotaOverrideIn"])).optional()}
    ).named(renames["V1Beta1ImportProducerOverridesResponseIn"])
    types["V1Beta1ImportProducerOverridesResponseOut"] = t.struct(
        {
            "overrides": t.array(
                t.proxy(renames["V1Beta1QuotaOverrideOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1ImportProducerOverridesResponseOut"])
    types["V1Beta1EnableConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1EnableConsumerResponseIn"])
    types["V1Beta1EnableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1EnableConsumerResponseOut"])
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
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
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
    types["V1Beta1ServiceIdentityIn"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["V1Beta1ServiceIdentityIn"])
    types["V1Beta1ServiceIdentityOut"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1ServiceIdentityOut"])
    types["V1Beta1QuotaOverrideIn"] = t.struct(
        {
            "adminOverrideAncestor": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "overrideValue": t.string().optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["V1Beta1QuotaOverrideIn"])
    types["V1Beta1QuotaOverrideOut"] = t.struct(
        {
            "adminOverrideAncestor": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "overrideValue": t.string().optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1QuotaOverrideOut"])
    types["TenantResourceIn"] = t.struct(
        {"tag": t.string().optional(), "status": t.string().optional()}
    ).named(renames["TenantResourceIn"])
    types["TenantResourceOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "status": t.string().optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantResourceOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["UsageIn"] = t.struct(
        {
            "requirements": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["UsageRuleIn"])).optional(),
            "producerNotificationChannel": t.string().optional(),
        }
    ).named(renames["UsageIn"])
    types["UsageOut"] = t.struct(
        {
            "requirements": t.array(t.string()).optional(),
            "rules": t.array(t.proxy(renames["UsageRuleOut"])).optional(),
            "producerNotificationChannel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageOut"])
    types["AuthenticationRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
    types["V1Beta1ProducerQuotaPolicyIn"] = t.struct(
        {
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "container": t.string().optional(),
            "policyValue": t.string().optional(),
            "unit": t.string().optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["V1Beta1ProducerQuotaPolicyIn"])
    types["V1Beta1ProducerQuotaPolicyOut"] = t.struct(
        {
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "container": t.string().optional(),
            "policyValue": t.string().optional(),
            "unit": t.string().optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1ProducerQuotaPolicyOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "unit": t.string().optional(),
            "launchStage": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "valueType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "unit": t.string().optional(),
            "launchStage": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "valueType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["V1DefaultIdentityIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "uniqueId": t.string().optional(),
        }
    ).named(renames["V1DefaultIdentityIn"])
    types["V1DefaultIdentityOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "uniqueId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1DefaultIdentityOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
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
    types["TypeIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "edition": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "edition": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["V1ServiceAccountIn"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
            "tag": t.string().optional(),
            "name": t.string().optional(),
            "iamAccountName": t.string().optional(),
        }
    ).named(renames["V1ServiceAccountIn"])
    types["V1ServiceAccountOut"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
            "tag": t.string().optional(),
            "name": t.string().optional(),
            "iamAccountName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1ServiceAccountOut"])
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
    types["V1Beta1GenerateServiceIdentityResponseIn"] = t.struct(
        {"identity": t.proxy(renames["V1Beta1ServiceIdentityIn"]).optional()}
    ).named(renames["V1Beta1GenerateServiceIdentityResponseIn"])
    types["V1Beta1GenerateServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["V1Beta1ServiceIdentityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1GenerateServiceIdentityResponseOut"])
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
    types["DocumentationRuleIn"] = t.struct(
        {
            "disableReplacementWords": t.string().optional(),
            "selector": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "disableReplacementWords": t.string().optional(),
            "selector": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
    types["AttachTenantProjectRequestIn"] = t.struct(
        {
            "tag": t.string(),
            "externalResource": t.string().optional(),
            "reservedResource": t.string().optional(),
        }
    ).named(renames["AttachTenantProjectRequestIn"])
    types["AttachTenantProjectRequestOut"] = t.struct(
        {
            "tag": t.string(),
            "externalResource": t.string().optional(),
            "reservedResource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachTenantProjectRequestOut"])
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
    types["TenancyUnitIn"] = t.struct(
        {
            "tenantResources": t.array(t.proxy(renames["TenantResourceIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TenancyUnitIn"])
    types["TenancyUnitOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "service": t.string().optional(),
            "tenantResources": t.array(
                t.proxy(renames["TenantResourceOut"])
            ).optional(),
            "name": t.string().optional(),
            "consumer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenancyUnitOut"])
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
    types["V1Beta1DisableConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1DisableConsumerResponseIn"])
    types["V1Beta1DisableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1DisableConsumerResponseOut"])
    types["LogDescriptorIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
    types["EndpointIn"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["DocumentationIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "overview": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["SearchTenancyUnitsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tenancyUnits": t.array(t.proxy(renames["TenancyUnitIn"])).optional(),
        }
    ).named(renames["SearchTenancyUnitsResponseIn"])
    types["SearchTenancyUnitsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tenancyUnits": t.array(t.proxy(renames["TenancyUnitOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTenancyUnitsResponseOut"])
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
    types["PolicyBindingIn"] = t.struct(
        {"members": t.array(t.string()).optional(), "role": t.string().optional()}
    ).named(renames["PolicyBindingIn"])
    types["PolicyBindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyBindingOut"])
    types["PublishingIn"] = t.struct(
        {
            "githubLabel": t.string().optional(),
            "apiShortName": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "newIssueUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "documentationUri": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "organization": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "githubLabel": t.string().optional(),
            "apiShortName": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "newIssueUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "documentationUri": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "organization": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["V1AddVisibilityLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["V1AddVisibilityLabelsResponseIn"])
    types["V1AddVisibilityLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1AddVisibilityLabelsResponseOut"])

    functions = {}
    functions["servicesSearch"] = serviceconsumermanagement.get(
        "v1/{parent}:search",
        t.struct(
            {
                "parent": t.string(),
                "query": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTenancyUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsAddProject"] = serviceconsumermanagement.post(
        "v1/{name}:undeleteProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsCreate"] = serviceconsumermanagement.post(
        "v1/{name}:undeleteProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsRemoveProject"] = serviceconsumermanagement.post(
        "v1/{name}:undeleteProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsDeleteProject"] = serviceconsumermanagement.post(
        "v1/{name}:undeleteProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsList"] = serviceconsumermanagement.post(
        "v1/{name}:undeleteProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsDelete"] = serviceconsumermanagement.post(
        "v1/{name}:undeleteProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesTenancyUnitsApplyProjectConfig"
    ] = serviceconsumermanagement.post(
        "v1/{name}:undeleteProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsAttachProject"] = serviceconsumermanagement.post(
        "v1/{name}:undeleteProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsUndeleteProject"] = serviceconsumermanagement.post(
        "v1/{name}:undeleteProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = serviceconsumermanagement.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = serviceconsumermanagement.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = serviceconsumermanagement.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = serviceconsumermanagement.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="serviceconsumermanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
