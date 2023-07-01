from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_serviceconsumermanagement():
    serviceconsumermanagement = HTTPRuntime(
        "https://serviceconsumermanagement.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_serviceconsumermanagement_1_ErrorResponse",
        "EnumValueIn": "_serviceconsumermanagement_2_EnumValueIn",
        "EnumValueOut": "_serviceconsumermanagement_3_EnumValueOut",
        "BillingIn": "_serviceconsumermanagement_4_BillingIn",
        "BillingOut": "_serviceconsumermanagement_5_BillingOut",
        "MetricDescriptorMetadataIn": "_serviceconsumermanagement_6_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_serviceconsumermanagement_7_MetricDescriptorMetadataOut",
        "BillingConfigIn": "_serviceconsumermanagement_8_BillingConfigIn",
        "BillingConfigOut": "_serviceconsumermanagement_9_BillingConfigOut",
        "TenantResourceIn": "_serviceconsumermanagement_10_TenantResourceIn",
        "TenantResourceOut": "_serviceconsumermanagement_11_TenantResourceOut",
        "LoggingIn": "_serviceconsumermanagement_12_LoggingIn",
        "LoggingOut": "_serviceconsumermanagement_13_LoggingOut",
        "V1Beta1ImportProducerOverridesResponseIn": "_serviceconsumermanagement_14_V1Beta1ImportProducerOverridesResponseIn",
        "V1Beta1ImportProducerOverridesResponseOut": "_serviceconsumermanagement_15_V1Beta1ImportProducerOverridesResponseOut",
        "UsageRuleIn": "_serviceconsumermanagement_16_UsageRuleIn",
        "UsageRuleOut": "_serviceconsumermanagement_17_UsageRuleOut",
        "SourceContextIn": "_serviceconsumermanagement_18_SourceContextIn",
        "SourceContextOut": "_serviceconsumermanagement_19_SourceContextOut",
        "TenantProjectPolicyIn": "_serviceconsumermanagement_20_TenantProjectPolicyIn",
        "TenantProjectPolicyOut": "_serviceconsumermanagement_21_TenantProjectPolicyOut",
        "V1Beta1ProducerQuotaPolicyIn": "_serviceconsumermanagement_22_V1Beta1ProducerQuotaPolicyIn",
        "V1Beta1ProducerQuotaPolicyOut": "_serviceconsumermanagement_23_V1Beta1ProducerQuotaPolicyOut",
        "BackendIn": "_serviceconsumermanagement_24_BackendIn",
        "BackendOut": "_serviceconsumermanagement_25_BackendOut",
        "CustomErrorIn": "_serviceconsumermanagement_26_CustomErrorIn",
        "CustomErrorOut": "_serviceconsumermanagement_27_CustomErrorOut",
        "AuthRequirementIn": "_serviceconsumermanagement_28_AuthRequirementIn",
        "AuthRequirementOut": "_serviceconsumermanagement_29_AuthRequirementOut",
        "V1Beta1GenerateServiceIdentityResponseIn": "_serviceconsumermanagement_30_V1Beta1GenerateServiceIdentityResponseIn",
        "V1Beta1GenerateServiceIdentityResponseOut": "_serviceconsumermanagement_31_V1Beta1GenerateServiceIdentityResponseOut",
        "CustomHttpPatternIn": "_serviceconsumermanagement_32_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_serviceconsumermanagement_33_CustomHttpPatternOut",
        "CancelOperationRequestIn": "_serviceconsumermanagement_34_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_serviceconsumermanagement_35_CancelOperationRequestOut",
        "OAuthRequirementsIn": "_serviceconsumermanagement_36_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_serviceconsumermanagement_37_OAuthRequirementsOut",
        "MethodIn": "_serviceconsumermanagement_38_MethodIn",
        "MethodOut": "_serviceconsumermanagement_39_MethodOut",
        "DotnetSettingsIn": "_serviceconsumermanagement_40_DotnetSettingsIn",
        "DotnetSettingsOut": "_serviceconsumermanagement_41_DotnetSettingsOut",
        "EmptyIn": "_serviceconsumermanagement_42_EmptyIn",
        "EmptyOut": "_serviceconsumermanagement_43_EmptyOut",
        "CustomErrorRuleIn": "_serviceconsumermanagement_44_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_serviceconsumermanagement_45_CustomErrorRuleOut",
        "ContextIn": "_serviceconsumermanagement_46_ContextIn",
        "ContextOut": "_serviceconsumermanagement_47_ContextOut",
        "TenancyUnitIn": "_serviceconsumermanagement_48_TenancyUnitIn",
        "TenancyUnitOut": "_serviceconsumermanagement_49_TenancyUnitOut",
        "V1Beta1EnableConsumerResponseIn": "_serviceconsumermanagement_50_V1Beta1EnableConsumerResponseIn",
        "V1Beta1EnableConsumerResponseOut": "_serviceconsumermanagement_51_V1Beta1EnableConsumerResponseOut",
        "ControlIn": "_serviceconsumermanagement_52_ControlIn",
        "ControlOut": "_serviceconsumermanagement_53_ControlOut",
        "SystemParameterRuleIn": "_serviceconsumermanagement_54_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_serviceconsumermanagement_55_SystemParameterRuleOut",
        "ListTenancyUnitsResponseIn": "_serviceconsumermanagement_56_ListTenancyUnitsResponseIn",
        "ListTenancyUnitsResponseOut": "_serviceconsumermanagement_57_ListTenancyUnitsResponseOut",
        "AddTenantProjectRequestIn": "_serviceconsumermanagement_58_AddTenantProjectRequestIn",
        "AddTenantProjectRequestOut": "_serviceconsumermanagement_59_AddTenantProjectRequestOut",
        "UsageIn": "_serviceconsumermanagement_60_UsageIn",
        "UsageOut": "_serviceconsumermanagement_61_UsageOut",
        "V1GenerateDefaultIdentityResponseIn": "_serviceconsumermanagement_62_V1GenerateDefaultIdentityResponseIn",
        "V1GenerateDefaultIdentityResponseOut": "_serviceconsumermanagement_63_V1GenerateDefaultIdentityResponseOut",
        "ServiceIn": "_serviceconsumermanagement_64_ServiceIn",
        "ServiceOut": "_serviceconsumermanagement_65_ServiceOut",
        "OperationIn": "_serviceconsumermanagement_66_OperationIn",
        "OperationOut": "_serviceconsumermanagement_67_OperationOut",
        "ClientLibrarySettingsIn": "_serviceconsumermanagement_68_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_serviceconsumermanagement_69_ClientLibrarySettingsOut",
        "CreateTenancyUnitRequestIn": "_serviceconsumermanagement_70_CreateTenancyUnitRequestIn",
        "CreateTenancyUnitRequestOut": "_serviceconsumermanagement_71_CreateTenancyUnitRequestOut",
        "CommonLanguageSettingsIn": "_serviceconsumermanagement_72_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_serviceconsumermanagement_73_CommonLanguageSettingsOut",
        "AuthProviderIn": "_serviceconsumermanagement_74_AuthProviderIn",
        "AuthProviderOut": "_serviceconsumermanagement_75_AuthProviderOut",
        "GoSettingsIn": "_serviceconsumermanagement_76_GoSettingsIn",
        "GoSettingsOut": "_serviceconsumermanagement_77_GoSettingsOut",
        "V1RemoveVisibilityLabelsResponseIn": "_serviceconsumermanagement_78_V1RemoveVisibilityLabelsResponseIn",
        "V1RemoveVisibilityLabelsResponseOut": "_serviceconsumermanagement_79_V1RemoveVisibilityLabelsResponseOut",
        "EnumIn": "_serviceconsumermanagement_80_EnumIn",
        "EnumOut": "_serviceconsumermanagement_81_EnumOut",
        "RemoveTenantProjectRequestIn": "_serviceconsumermanagement_82_RemoveTenantProjectRequestIn",
        "RemoveTenantProjectRequestOut": "_serviceconsumermanagement_83_RemoveTenantProjectRequestOut",
        "ApplyTenantProjectConfigRequestIn": "_serviceconsumermanagement_84_ApplyTenantProjectConfigRequestIn",
        "ApplyTenantProjectConfigRequestOut": "_serviceconsumermanagement_85_ApplyTenantProjectConfigRequestOut",
        "UndeleteTenantProjectRequestIn": "_serviceconsumermanagement_86_UndeleteTenantProjectRequestIn",
        "UndeleteTenantProjectRequestOut": "_serviceconsumermanagement_87_UndeleteTenantProjectRequestOut",
        "ServiceAccountConfigIn": "_serviceconsumermanagement_88_ServiceAccountConfigIn",
        "ServiceAccountConfigOut": "_serviceconsumermanagement_89_ServiceAccountConfigOut",
        "LogDescriptorIn": "_serviceconsumermanagement_90_LogDescriptorIn",
        "LogDescriptorOut": "_serviceconsumermanagement_91_LogDescriptorOut",
        "JwtLocationIn": "_serviceconsumermanagement_92_JwtLocationIn",
        "JwtLocationOut": "_serviceconsumermanagement_93_JwtLocationOut",
        "PageIn": "_serviceconsumermanagement_94_PageIn",
        "PageOut": "_serviceconsumermanagement_95_PageOut",
        "DocumentationRuleIn": "_serviceconsumermanagement_96_DocumentationRuleIn",
        "DocumentationRuleOut": "_serviceconsumermanagement_97_DocumentationRuleOut",
        "V1DefaultIdentityIn": "_serviceconsumermanagement_98_V1DefaultIdentityIn",
        "V1DefaultIdentityOut": "_serviceconsumermanagement_99_V1DefaultIdentityOut",
        "RubySettingsIn": "_serviceconsumermanagement_100_RubySettingsIn",
        "RubySettingsOut": "_serviceconsumermanagement_101_RubySettingsOut",
        "AttachTenantProjectRequestIn": "_serviceconsumermanagement_102_AttachTenantProjectRequestIn",
        "AttachTenantProjectRequestOut": "_serviceconsumermanagement_103_AttachTenantProjectRequestOut",
        "ContextRuleIn": "_serviceconsumermanagement_104_ContextRuleIn",
        "ContextRuleOut": "_serviceconsumermanagement_105_ContextRuleOut",
        "LabelDescriptorIn": "_serviceconsumermanagement_106_LabelDescriptorIn",
        "LabelDescriptorOut": "_serviceconsumermanagement_107_LabelDescriptorOut",
        "V1Beta1DisableConsumerResponseIn": "_serviceconsumermanagement_108_V1Beta1DisableConsumerResponseIn",
        "V1Beta1DisableConsumerResponseOut": "_serviceconsumermanagement_109_V1Beta1DisableConsumerResponseOut",
        "QuotaLimitIn": "_serviceconsumermanagement_110_QuotaLimitIn",
        "QuotaLimitOut": "_serviceconsumermanagement_111_QuotaLimitOut",
        "FieldIn": "_serviceconsumermanagement_112_FieldIn",
        "FieldOut": "_serviceconsumermanagement_113_FieldOut",
        "StatusIn": "_serviceconsumermanagement_114_StatusIn",
        "StatusOut": "_serviceconsumermanagement_115_StatusOut",
        "V1Beta1BatchCreateProducerOverridesResponseIn": "_serviceconsumermanagement_116_V1Beta1BatchCreateProducerOverridesResponseIn",
        "V1Beta1BatchCreateProducerOverridesResponseOut": "_serviceconsumermanagement_117_V1Beta1BatchCreateProducerOverridesResponseOut",
        "V1Beta1RefreshConsumerResponseIn": "_serviceconsumermanagement_118_V1Beta1RefreshConsumerResponseIn",
        "V1Beta1RefreshConsumerResponseOut": "_serviceconsumermanagement_119_V1Beta1RefreshConsumerResponseOut",
        "AuthenticationIn": "_serviceconsumermanagement_120_AuthenticationIn",
        "AuthenticationOut": "_serviceconsumermanagement_121_AuthenticationOut",
        "MethodSettingsIn": "_serviceconsumermanagement_122_MethodSettingsIn",
        "MethodSettingsOut": "_serviceconsumermanagement_123_MethodSettingsOut",
        "PolicyBindingIn": "_serviceconsumermanagement_124_PolicyBindingIn",
        "PolicyBindingOut": "_serviceconsumermanagement_125_PolicyBindingOut",
        "V1EnableConsumerResponseIn": "_serviceconsumermanagement_126_V1EnableConsumerResponseIn",
        "V1EnableConsumerResponseOut": "_serviceconsumermanagement_127_V1EnableConsumerResponseOut",
        "MetricDescriptorIn": "_serviceconsumermanagement_128_MetricDescriptorIn",
        "MetricDescriptorOut": "_serviceconsumermanagement_129_MetricDescriptorOut",
        "MonitoringIn": "_serviceconsumermanagement_130_MonitoringIn",
        "MonitoringOut": "_serviceconsumermanagement_131_MonitoringOut",
        "SystemParameterIn": "_serviceconsumermanagement_132_SystemParameterIn",
        "SystemParameterOut": "_serviceconsumermanagement_133_SystemParameterOut",
        "V1ServiceAccountIn": "_serviceconsumermanagement_134_V1ServiceAccountIn",
        "V1ServiceAccountOut": "_serviceconsumermanagement_135_V1ServiceAccountOut",
        "EndpointIn": "_serviceconsumermanagement_136_EndpointIn",
        "EndpointOut": "_serviceconsumermanagement_137_EndpointOut",
        "DocumentationIn": "_serviceconsumermanagement_138_DocumentationIn",
        "DocumentationOut": "_serviceconsumermanagement_139_DocumentationOut",
        "SearchTenancyUnitsResponseIn": "_serviceconsumermanagement_140_SearchTenancyUnitsResponseIn",
        "SearchTenancyUnitsResponseOut": "_serviceconsumermanagement_141_SearchTenancyUnitsResponseOut",
        "ApiIn": "_serviceconsumermanagement_142_ApiIn",
        "ApiOut": "_serviceconsumermanagement_143_ApiOut",
        "LoggingDestinationIn": "_serviceconsumermanagement_144_LoggingDestinationIn",
        "LoggingDestinationOut": "_serviceconsumermanagement_145_LoggingDestinationOut",
        "V1DisableConsumerResponseIn": "_serviceconsumermanagement_146_V1DisableConsumerResponseIn",
        "V1DisableConsumerResponseOut": "_serviceconsumermanagement_147_V1DisableConsumerResponseOut",
        "MetricRuleIn": "_serviceconsumermanagement_148_MetricRuleIn",
        "MetricRuleOut": "_serviceconsumermanagement_149_MetricRuleOut",
        "BillingDestinationIn": "_serviceconsumermanagement_150_BillingDestinationIn",
        "BillingDestinationOut": "_serviceconsumermanagement_151_BillingDestinationOut",
        "JavaSettingsIn": "_serviceconsumermanagement_152_JavaSettingsIn",
        "JavaSettingsOut": "_serviceconsumermanagement_153_JavaSettingsOut",
        "OptionIn": "_serviceconsumermanagement_154_OptionIn",
        "OptionOut": "_serviceconsumermanagement_155_OptionOut",
        "QuotaIn": "_serviceconsumermanagement_156_QuotaIn",
        "QuotaOut": "_serviceconsumermanagement_157_QuotaOut",
        "TypeIn": "_serviceconsumermanagement_158_TypeIn",
        "TypeOut": "_serviceconsumermanagement_159_TypeOut",
        "CppSettingsIn": "_serviceconsumermanagement_160_CppSettingsIn",
        "CppSettingsOut": "_serviceconsumermanagement_161_CppSettingsOut",
        "PhpSettingsIn": "_serviceconsumermanagement_162_PhpSettingsIn",
        "PhpSettingsOut": "_serviceconsumermanagement_163_PhpSettingsOut",
        "V1RefreshConsumerResponseIn": "_serviceconsumermanagement_164_V1RefreshConsumerResponseIn",
        "V1RefreshConsumerResponseOut": "_serviceconsumermanagement_165_V1RefreshConsumerResponseOut",
        "HttpIn": "_serviceconsumermanagement_166_HttpIn",
        "HttpOut": "_serviceconsumermanagement_167_HttpOut",
        "MixinIn": "_serviceconsumermanagement_168_MixinIn",
        "MixinOut": "_serviceconsumermanagement_169_MixinOut",
        "NodeSettingsIn": "_serviceconsumermanagement_170_NodeSettingsIn",
        "NodeSettingsOut": "_serviceconsumermanagement_171_NodeSettingsOut",
        "V1AddVisibilityLabelsResponseIn": "_serviceconsumermanagement_172_V1AddVisibilityLabelsResponseIn",
        "V1AddVisibilityLabelsResponseOut": "_serviceconsumermanagement_173_V1AddVisibilityLabelsResponseOut",
        "SourceInfoIn": "_serviceconsumermanagement_174_SourceInfoIn",
        "SourceInfoOut": "_serviceconsumermanagement_175_SourceInfoOut",
        "V1Beta1QuotaOverrideIn": "_serviceconsumermanagement_176_V1Beta1QuotaOverrideIn",
        "V1Beta1QuotaOverrideOut": "_serviceconsumermanagement_177_V1Beta1QuotaOverrideOut",
        "TenantProjectConfigIn": "_serviceconsumermanagement_178_TenantProjectConfigIn",
        "TenantProjectConfigOut": "_serviceconsumermanagement_179_TenantProjectConfigOut",
        "MonitoredResourceDescriptorIn": "_serviceconsumermanagement_180_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_serviceconsumermanagement_181_MonitoredResourceDescriptorOut",
        "PublishingIn": "_serviceconsumermanagement_182_PublishingIn",
        "PublishingOut": "_serviceconsumermanagement_183_PublishingOut",
        "DeleteTenantProjectRequestIn": "_serviceconsumermanagement_184_DeleteTenantProjectRequestIn",
        "DeleteTenantProjectRequestOut": "_serviceconsumermanagement_185_DeleteTenantProjectRequestOut",
        "SystemParametersIn": "_serviceconsumermanagement_186_SystemParametersIn",
        "SystemParametersOut": "_serviceconsumermanagement_187_SystemParametersOut",
        "AuthenticationRuleIn": "_serviceconsumermanagement_188_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_serviceconsumermanagement_189_AuthenticationRuleOut",
        "MonitoringDestinationIn": "_serviceconsumermanagement_190_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_serviceconsumermanagement_191_MonitoringDestinationOut",
        "BackendRuleIn": "_serviceconsumermanagement_192_BackendRuleIn",
        "BackendRuleOut": "_serviceconsumermanagement_193_BackendRuleOut",
        "V1GenerateServiceAccountResponseIn": "_serviceconsumermanagement_194_V1GenerateServiceAccountResponseIn",
        "V1GenerateServiceAccountResponseOut": "_serviceconsumermanagement_195_V1GenerateServiceAccountResponseOut",
        "LongRunningIn": "_serviceconsumermanagement_196_LongRunningIn",
        "LongRunningOut": "_serviceconsumermanagement_197_LongRunningOut",
        "V1Beta1ImportProducerQuotaPoliciesResponseIn": "_serviceconsumermanagement_198_V1Beta1ImportProducerQuotaPoliciesResponseIn",
        "V1Beta1ImportProducerQuotaPoliciesResponseOut": "_serviceconsumermanagement_199_V1Beta1ImportProducerQuotaPoliciesResponseOut",
        "PythonSettingsIn": "_serviceconsumermanagement_200_PythonSettingsIn",
        "PythonSettingsOut": "_serviceconsumermanagement_201_PythonSettingsOut",
        "ListOperationsResponseIn": "_serviceconsumermanagement_202_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_serviceconsumermanagement_203_ListOperationsResponseOut",
        "V1Beta1ServiceIdentityIn": "_serviceconsumermanagement_204_V1Beta1ServiceIdentityIn",
        "V1Beta1ServiceIdentityOut": "_serviceconsumermanagement_205_V1Beta1ServiceIdentityOut",
        "HttpRuleIn": "_serviceconsumermanagement_206_HttpRuleIn",
        "HttpRuleOut": "_serviceconsumermanagement_207_HttpRuleOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["BillingConfigIn"] = t.struct(
        {"billingAccount": t.string().optional()}
    ).named(renames["BillingConfigIn"])
    types["BillingConfigOut"] = t.struct(
        {
            "billingAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingConfigOut"])
    types["TenantResourceIn"] = t.struct(
        {"status": t.string().optional(), "tag": t.string().optional()}
    ).named(renames["TenantResourceIn"])
    types["TenantResourceOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "status": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantResourceOut"])
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
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["TenantProjectPolicyIn"] = t.struct(
        {"policyBindings": t.array(t.proxy(renames["PolicyBindingIn"])).optional()}
    ).named(renames["TenantProjectPolicyIn"])
    types["TenantProjectPolicyOut"] = t.struct(
        {
            "policyBindings": t.array(t.proxy(renames["PolicyBindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantProjectPolicyOut"])
    types["V1Beta1ProducerQuotaPolicyIn"] = t.struct(
        {
            "policyValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "container": t.string().optional(),
        }
    ).named(renames["V1Beta1ProducerQuotaPolicyIn"])
    types["V1Beta1ProducerQuotaPolicyOut"] = t.struct(
        {
            "policyValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "container": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1ProducerQuotaPolicyOut"])
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
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
    types["V1Beta1GenerateServiceIdentityResponseIn"] = t.struct(
        {"identity": t.proxy(renames["V1Beta1ServiceIdentityIn"]).optional()}
    ).named(renames["V1Beta1GenerateServiceIdentityResponseIn"])
    types["V1Beta1GenerateServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["V1Beta1ServiceIdentityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1GenerateServiceIdentityResponseOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
    types["MethodIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "responseStreaming": t.boolean().optional(),
            "requestStreaming": t.boolean().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "responseStreaming": t.boolean().optional(),
            "requestStreaming": t.boolean().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["TenancyUnitIn"] = t.struct(
        {
            "tenantResources": t.array(t.proxy(renames["TenantResourceIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TenancyUnitIn"])
    types["TenancyUnitOut"] = t.struct(
        {
            "tenantResources": t.array(
                t.proxy(renames["TenantResourceOut"])
            ).optional(),
            "createTime": t.string().optional(),
            "service": t.string().optional(),
            "consumer": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenancyUnitOut"])
    types["V1Beta1EnableConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1EnableConsumerResponseIn"])
    types["V1Beta1EnableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1EnableConsumerResponseOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
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
    types["ServiceIn"] = t.struct(
        {
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "id": t.string().optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "configVersion": t.integer().optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "name": t.string().optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "title": t.string().optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "producerProjectId": t.string().optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "id": t.string().optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "configVersion": t.integer().optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "name": t.string().optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "title": t.string().optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "producerProjectId": t.string().optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "version": t.string().optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "version": t.string().optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["CreateTenancyUnitRequestIn"] = t.struct(
        {"tenancyUnitId": t.string().optional()}
    ).named(renames["CreateTenancyUnitRequestIn"])
    types["CreateTenancyUnitRequestOut"] = t.struct(
        {
            "tenancyUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTenancyUnitRequestOut"])
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
    types["AuthProviderIn"] = t.struct(
        {
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "jwksUri": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "id": t.string().optional(),
            "audiences": t.string().optional(),
            "issuer": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "jwksUri": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "id": t.string().optional(),
            "audiences": t.string().optional(),
            "issuer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["V1RemoveVisibilityLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["V1RemoveVisibilityLabelsResponseIn"])
    types["V1RemoveVisibilityLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1RemoveVisibilityLabelsResponseOut"])
    types["EnumIn"] = t.struct(
        {
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["RemoveTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["RemoveTenantProjectRequestIn"]
    )
    types["RemoveTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveTenantProjectRequestOut"])
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
    types["UndeleteTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["UndeleteTenantProjectRequestIn"]
    )
    types["UndeleteTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteTenantProjectRequestOut"])
    types["ServiceAccountConfigIn"] = t.struct(
        {
            "accountId": t.string().optional(),
            "tenantProjectRoles": t.array(t.string()).optional(),
        }
    ).named(renames["ServiceAccountConfigIn"])
    types["ServiceAccountConfigOut"] = t.struct(
        {
            "accountId": t.string().optional(),
            "tenantProjectRoles": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountConfigOut"])
    types["LogDescriptorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
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
    types["DocumentationRuleIn"] = t.struct(
        {
            "disableReplacementWords": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "description": t.string().optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "disableReplacementWords": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "description": t.string().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
    types["V1DefaultIdentityIn"] = t.struct(
        {
            "name": t.string().optional(),
            "tag": t.string().optional(),
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
        }
    ).named(renames["V1DefaultIdentityIn"])
    types["V1DefaultIdentityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "tag": t.string().optional(),
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1DefaultIdentityOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["AttachTenantProjectRequestIn"] = t.struct(
        {
            "externalResource": t.string().optional(),
            "reservedResource": t.string().optional(),
            "tag": t.string(),
        }
    ).named(renames["AttachTenantProjectRequestIn"])
    types["AttachTenantProjectRequestOut"] = t.struct(
        {
            "externalResource": t.string().optional(),
            "reservedResource": t.string().optional(),
            "tag": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachTenantProjectRequestOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "requested": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "requested": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
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
    types["V1Beta1DisableConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1DisableConsumerResponseIn"])
    types["V1Beta1DisableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1DisableConsumerResponseOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "duration": t.string().optional(),
            "freeTier": t.string().optional(),
            "name": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "maxLimit": t.string().optional(),
            "description": t.string().optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "duration": t.string().optional(),
            "freeTier": t.string().optional(),
            "name": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "maxLimit": t.string().optional(),
            "description": t.string().optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["FieldIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "cardinality": t.string().optional(),
            "defaultValue": t.string().optional(),
            "packed": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "name": t.string().optional(),
            "number": t.integer().optional(),
            "kind": t.string().optional(),
            "jsonName": t.string().optional(),
            "typeUrl": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "cardinality": t.string().optional(),
            "defaultValue": t.string().optional(),
            "packed": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "name": t.string().optional(),
            "number": t.integer().optional(),
            "kind": t.string().optional(),
            "jsonName": t.string().optional(),
            "typeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
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
    types["V1Beta1RefreshConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1RefreshConsumerResponseIn"])
    types["V1Beta1RefreshConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1RefreshConsumerResponseOut"])
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
    types["PolicyBindingIn"] = t.struct(
        {"role": t.string().optional(), "members": t.array(t.string()).optional()}
    ).named(renames["PolicyBindingIn"])
    types["PolicyBindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyBindingOut"])
    types["V1EnableConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1EnableConsumerResponseIn"]
    )
    types["V1EnableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1EnableConsumerResponseOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "unit": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "metricKind": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "unit": t.string().optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "metricKind": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["SystemParameterIn"] = t.struct(
        {
            "urlQueryParameter": t.string().optional(),
            "name": t.string().optional(),
            "httpHeader": t.string().optional(),
        }
    ).named(renames["SystemParameterIn"])
    types["SystemParameterOut"] = t.struct(
        {
            "urlQueryParameter": t.string().optional(),
            "name": t.string().optional(),
            "httpHeader": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParameterOut"])
    types["V1ServiceAccountIn"] = t.struct(
        {
            "iamAccountName": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "uniqueId": t.string().optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["V1ServiceAccountIn"])
    types["V1ServiceAccountOut"] = t.struct(
        {
            "iamAccountName": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "uniqueId": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1ServiceAccountOut"])
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
    types["DocumentationIn"] = t.struct(
        {
            "documentationRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "summary": t.string().optional(),
            "sectionOverrides": t.array(t.proxy(renames["PageIn"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "documentationRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "summary": t.string().optional(),
            "sectionOverrides": t.array(t.proxy(renames["PageOut"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
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
    types["ApiIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "version": t.string().optional(),
            "syntax": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "version": t.string().optional(),
            "syntax": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
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
    types["V1DisableConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1DisableConsumerResponseIn"]
    )
    types["V1DisableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1DisableConsumerResponseOut"])
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
    types["JavaSettingsIn"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "libraryPackage": t.string().optional(),
        }
    ).named(renames["JavaSettingsIn"])
    types["JavaSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "libraryPackage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JavaSettingsOut"])
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
    types["TypeIn"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
    types["V1RefreshConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1RefreshConsumerResponseIn"]
    )
    types["V1RefreshConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1RefreshConsumerResponseOut"])
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
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["V1AddVisibilityLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["V1AddVisibilityLabelsResponseIn"])
    types["V1AddVisibilityLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1AddVisibilityLabelsResponseOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
    types["V1Beta1QuotaOverrideIn"] = t.struct(
        {
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "adminOverrideAncestor": t.string().optional(),
            "overrideValue": t.string().optional(),
            "name": t.string().optional(),
            "unit": t.string().optional(),
        }
    ).named(renames["V1Beta1QuotaOverrideIn"])
    types["V1Beta1QuotaOverrideOut"] = t.struct(
        {
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "metric": t.string().optional(),
            "adminOverrideAncestor": t.string().optional(),
            "overrideValue": t.string().optional(),
            "name": t.string().optional(),
            "unit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1QuotaOverrideOut"])
    types["TenantProjectConfigIn"] = t.struct(
        {
            "billingConfig": t.proxy(renames["BillingConfigIn"]).optional(),
            "tenantProjectPolicy": t.proxy(renames["TenantProjectPolicyIn"]).optional(),
            "folder": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountConfig": t.proxy(
                renames["ServiceAccountConfigIn"]
            ).optional(),
        }
    ).named(renames["TenantProjectConfigIn"])
    types["TenantProjectConfigOut"] = t.struct(
        {
            "billingConfig": t.proxy(renames["BillingConfigOut"]).optional(),
            "tenantProjectPolicy": t.proxy(
                renames["TenantProjectPolicyOut"]
            ).optional(),
            "folder": t.string().optional(),
            "services": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountConfig": t.proxy(
                renames["ServiceAccountConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantProjectConfigOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["PublishingIn"] = t.struct(
        {
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "organization": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "docTagPrefix": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "githubLabel": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "documentationUri": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "organization": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "docTagPrefix": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "githubLabel": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "documentationUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["DeleteTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["DeleteTenantProjectRequestIn"]
    )
    types["DeleteTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTenantProjectRequestOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
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
    types["BackendRuleIn"] = t.struct(
        {
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "address": t.string().optional(),
            "jwtAudience": t.string().optional(),
            "operationDeadline": t.number().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "pathTranslation": t.string(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
            "disableAuth": t.boolean().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "address": t.string().optional(),
            "jwtAudience": t.string().optional(),
            "operationDeadline": t.number().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "pathTranslation": t.string(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
            "disableAuth": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["V1GenerateServiceAccountResponseIn"] = t.struct(
        {"account": t.proxy(renames["V1ServiceAccountIn"]).optional()}
    ).named(renames["V1GenerateServiceAccountResponseIn"])
    types["V1GenerateServiceAccountResponseOut"] = t.struct(
        {
            "account": t.proxy(renames["V1ServiceAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1GenerateServiceAccountResponseOut"])
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
    types["V1Beta1ServiceIdentityIn"] = t.struct(
        {
            "tag": t.string().optional(),
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["V1Beta1ServiceIdentityIn"])
    types["V1Beta1ServiceIdentityOut"] = t.struct(
        {
            "tag": t.string().optional(),
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1ServiceIdentityOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "delete": t.string().optional(),
            "body": t.string().optional(),
            "patch": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "post": t.string().optional(),
            "selector": t.string().optional(),
            "responseBody": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "delete": t.string().optional(),
            "body": t.string().optional(),
            "patch": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "post": t.string().optional(),
            "selector": t.string().optional(),
            "responseBody": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])

    functions = {}
    functions["operationsCancel"] = serviceconsumermanagement.get(
        "v1/{name}",
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
    functions["operationsGet"] = serviceconsumermanagement.get(
        "v1/{name}",
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
    functions["operationsDelete"] = serviceconsumermanagement.get(
        "v1/{name}",
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
    functions["operationsList"] = serviceconsumermanagement.get(
        "v1/{name}",
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
    functions["servicesSearch"] = serviceconsumermanagement.get(
        "v1/{parent}:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "query": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTenancyUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsList"] = serviceconsumermanagement.post(
        "v1/{name}:removeProject",
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
        "v1/{name}:removeProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsCreate"] = serviceconsumermanagement.post(
        "v1/{name}:removeProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsAddProject"] = serviceconsumermanagement.post(
        "v1/{name}:removeProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsDelete"] = serviceconsumermanagement.post(
        "v1/{name}:removeProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsUndeleteProject"] = serviceconsumermanagement.post(
        "v1/{name}:removeProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsDeleteProject"] = serviceconsumermanagement.post(
        "v1/{name}:removeProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsAttachProject"] = serviceconsumermanagement.post(
        "v1/{name}:removeProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsRemoveProject"] = serviceconsumermanagement.post(
        "v1/{name}:removeProject",
        t.struct(
            {"name": t.string(), "tag": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="serviceconsumermanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
