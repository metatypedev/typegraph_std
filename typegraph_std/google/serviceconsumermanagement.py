from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_serviceconsumermanagement() -> Import:
    serviceconsumermanagement = HTTPRuntime(
        "https://serviceconsumermanagement.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_serviceconsumermanagement_1_ErrorResponse",
        "OperationIn": "_serviceconsumermanagement_2_OperationIn",
        "OperationOut": "_serviceconsumermanagement_3_OperationOut",
        "EnumValueIn": "_serviceconsumermanagement_4_EnumValueIn",
        "EnumValueOut": "_serviceconsumermanagement_5_EnumValueOut",
        "ContextIn": "_serviceconsumermanagement_6_ContextIn",
        "ContextOut": "_serviceconsumermanagement_7_ContextOut",
        "PolicyBindingIn": "_serviceconsumermanagement_8_PolicyBindingIn",
        "PolicyBindingOut": "_serviceconsumermanagement_9_PolicyBindingOut",
        "V1GenerateDefaultIdentityResponseIn": "_serviceconsumermanagement_10_V1GenerateDefaultIdentityResponseIn",
        "V1GenerateDefaultIdentityResponseOut": "_serviceconsumermanagement_11_V1GenerateDefaultIdentityResponseOut",
        "AttachTenantProjectRequestIn": "_serviceconsumermanagement_12_AttachTenantProjectRequestIn",
        "AttachTenantProjectRequestOut": "_serviceconsumermanagement_13_AttachTenantProjectRequestOut",
        "ServiceIn": "_serviceconsumermanagement_14_ServiceIn",
        "ServiceOut": "_serviceconsumermanagement_15_ServiceOut",
        "AuthenticationIn": "_serviceconsumermanagement_16_AuthenticationIn",
        "AuthenticationOut": "_serviceconsumermanagement_17_AuthenticationOut",
        "UsageIn": "_serviceconsumermanagement_18_UsageIn",
        "UsageOut": "_serviceconsumermanagement_19_UsageOut",
        "FieldIn": "_serviceconsumermanagement_20_FieldIn",
        "FieldOut": "_serviceconsumermanagement_21_FieldOut",
        "PythonSettingsIn": "_serviceconsumermanagement_22_PythonSettingsIn",
        "PythonSettingsOut": "_serviceconsumermanagement_23_PythonSettingsOut",
        "V1Beta1GenerateServiceIdentityResponseIn": "_serviceconsumermanagement_24_V1Beta1GenerateServiceIdentityResponseIn",
        "V1Beta1GenerateServiceIdentityResponseOut": "_serviceconsumermanagement_25_V1Beta1GenerateServiceIdentityResponseOut",
        "PhpSettingsIn": "_serviceconsumermanagement_26_PhpSettingsIn",
        "PhpSettingsOut": "_serviceconsumermanagement_27_PhpSettingsOut",
        "CustomHttpPatternIn": "_serviceconsumermanagement_28_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_serviceconsumermanagement_29_CustomHttpPatternOut",
        "V1Beta1BatchCreateProducerOverridesResponseIn": "_serviceconsumermanagement_30_V1Beta1BatchCreateProducerOverridesResponseIn",
        "V1Beta1BatchCreateProducerOverridesResponseOut": "_serviceconsumermanagement_31_V1Beta1BatchCreateProducerOverridesResponseOut",
        "CustomErrorRuleIn": "_serviceconsumermanagement_32_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_serviceconsumermanagement_33_CustomErrorRuleOut",
        "V1Beta1ServiceIdentityIn": "_serviceconsumermanagement_34_V1Beta1ServiceIdentityIn",
        "V1Beta1ServiceIdentityOut": "_serviceconsumermanagement_35_V1Beta1ServiceIdentityOut",
        "RubySettingsIn": "_serviceconsumermanagement_36_RubySettingsIn",
        "RubySettingsOut": "_serviceconsumermanagement_37_RubySettingsOut",
        "LoggingIn": "_serviceconsumermanagement_38_LoggingIn",
        "LoggingOut": "_serviceconsumermanagement_39_LoggingOut",
        "LongRunningIn": "_serviceconsumermanagement_40_LongRunningIn",
        "LongRunningOut": "_serviceconsumermanagement_41_LongRunningOut",
        "SystemParameterRuleIn": "_serviceconsumermanagement_42_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_serviceconsumermanagement_43_SystemParameterRuleOut",
        "ListOperationsResponseIn": "_serviceconsumermanagement_44_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_serviceconsumermanagement_45_ListOperationsResponseOut",
        "DeleteTenantProjectRequestIn": "_serviceconsumermanagement_46_DeleteTenantProjectRequestIn",
        "DeleteTenantProjectRequestOut": "_serviceconsumermanagement_47_DeleteTenantProjectRequestOut",
        "MonitoringDestinationIn": "_serviceconsumermanagement_48_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_serviceconsumermanagement_49_MonitoringDestinationOut",
        "SystemParametersIn": "_serviceconsumermanagement_50_SystemParametersIn",
        "SystemParametersOut": "_serviceconsumermanagement_51_SystemParametersOut",
        "OptionIn": "_serviceconsumermanagement_52_OptionIn",
        "OptionOut": "_serviceconsumermanagement_53_OptionOut",
        "BillingIn": "_serviceconsumermanagement_54_BillingIn",
        "BillingOut": "_serviceconsumermanagement_55_BillingOut",
        "EmptyIn": "_serviceconsumermanagement_56_EmptyIn",
        "EmptyOut": "_serviceconsumermanagement_57_EmptyOut",
        "GoSettingsIn": "_serviceconsumermanagement_58_GoSettingsIn",
        "GoSettingsOut": "_serviceconsumermanagement_59_GoSettingsOut",
        "V1AddVisibilityLabelsResponseIn": "_serviceconsumermanagement_60_V1AddVisibilityLabelsResponseIn",
        "V1AddVisibilityLabelsResponseOut": "_serviceconsumermanagement_61_V1AddVisibilityLabelsResponseOut",
        "LabelDescriptorIn": "_serviceconsumermanagement_62_LabelDescriptorIn",
        "LabelDescriptorOut": "_serviceconsumermanagement_63_LabelDescriptorOut",
        "ClientLibrarySettingsIn": "_serviceconsumermanagement_64_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_serviceconsumermanagement_65_ClientLibrarySettingsOut",
        "AuthRequirementIn": "_serviceconsumermanagement_66_AuthRequirementIn",
        "AuthRequirementOut": "_serviceconsumermanagement_67_AuthRequirementOut",
        "MetricDescriptorMetadataIn": "_serviceconsumermanagement_68_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_serviceconsumermanagement_69_MetricDescriptorMetadataOut",
        "ServiceAccountConfigIn": "_serviceconsumermanagement_70_ServiceAccountConfigIn",
        "ServiceAccountConfigOut": "_serviceconsumermanagement_71_ServiceAccountConfigOut",
        "SourceContextIn": "_serviceconsumermanagement_72_SourceContextIn",
        "SourceContextOut": "_serviceconsumermanagement_73_SourceContextOut",
        "V1Beta1ImportProducerQuotaPoliciesResponseIn": "_serviceconsumermanagement_74_V1Beta1ImportProducerQuotaPoliciesResponseIn",
        "V1Beta1ImportProducerQuotaPoliciesResponseOut": "_serviceconsumermanagement_75_V1Beta1ImportProducerQuotaPoliciesResponseOut",
        "MethodSettingsIn": "_serviceconsumermanagement_76_MethodSettingsIn",
        "MethodSettingsOut": "_serviceconsumermanagement_77_MethodSettingsOut",
        "QuotaIn": "_serviceconsumermanagement_78_QuotaIn",
        "QuotaOut": "_serviceconsumermanagement_79_QuotaOut",
        "MetricRuleIn": "_serviceconsumermanagement_80_MetricRuleIn",
        "MetricRuleOut": "_serviceconsumermanagement_81_MetricRuleOut",
        "V1Beta1QuotaOverrideIn": "_serviceconsumermanagement_82_V1Beta1QuotaOverrideIn",
        "V1Beta1QuotaOverrideOut": "_serviceconsumermanagement_83_V1Beta1QuotaOverrideOut",
        "UsageRuleIn": "_serviceconsumermanagement_84_UsageRuleIn",
        "UsageRuleOut": "_serviceconsumermanagement_85_UsageRuleOut",
        "StatusIn": "_serviceconsumermanagement_86_StatusIn",
        "StatusOut": "_serviceconsumermanagement_87_StatusOut",
        "ApplyTenantProjectConfigRequestIn": "_serviceconsumermanagement_88_ApplyTenantProjectConfigRequestIn",
        "ApplyTenantProjectConfigRequestOut": "_serviceconsumermanagement_89_ApplyTenantProjectConfigRequestOut",
        "BackendIn": "_serviceconsumermanagement_90_BackendIn",
        "BackendOut": "_serviceconsumermanagement_91_BackendOut",
        "V1RemoveVisibilityLabelsResponseIn": "_serviceconsumermanagement_92_V1RemoveVisibilityLabelsResponseIn",
        "V1RemoveVisibilityLabelsResponseOut": "_serviceconsumermanagement_93_V1RemoveVisibilityLabelsResponseOut",
        "RemoveTenantProjectRequestIn": "_serviceconsumermanagement_94_RemoveTenantProjectRequestIn",
        "RemoveTenantProjectRequestOut": "_serviceconsumermanagement_95_RemoveTenantProjectRequestOut",
        "V1ServiceAccountIn": "_serviceconsumermanagement_96_V1ServiceAccountIn",
        "V1ServiceAccountOut": "_serviceconsumermanagement_97_V1ServiceAccountOut",
        "TenancyUnitIn": "_serviceconsumermanagement_98_TenancyUnitIn",
        "TenancyUnitOut": "_serviceconsumermanagement_99_TenancyUnitOut",
        "DocumentationRuleIn": "_serviceconsumermanagement_100_DocumentationRuleIn",
        "DocumentationRuleOut": "_serviceconsumermanagement_101_DocumentationRuleOut",
        "LogDescriptorIn": "_serviceconsumermanagement_102_LogDescriptorIn",
        "LogDescriptorOut": "_serviceconsumermanagement_103_LogDescriptorOut",
        "EndpointIn": "_serviceconsumermanagement_104_EndpointIn",
        "EndpointOut": "_serviceconsumermanagement_105_EndpointOut",
        "V1RefreshConsumerResponseIn": "_serviceconsumermanagement_106_V1RefreshConsumerResponseIn",
        "V1RefreshConsumerResponseOut": "_serviceconsumermanagement_107_V1RefreshConsumerResponseOut",
        "CancelOperationRequestIn": "_serviceconsumermanagement_108_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_serviceconsumermanagement_109_CancelOperationRequestOut",
        "TypeIn": "_serviceconsumermanagement_110_TypeIn",
        "TypeOut": "_serviceconsumermanagement_111_TypeOut",
        "AuthProviderIn": "_serviceconsumermanagement_112_AuthProviderIn",
        "AuthProviderOut": "_serviceconsumermanagement_113_AuthProviderOut",
        "TenantResourceIn": "_serviceconsumermanagement_114_TenantResourceIn",
        "TenantResourceOut": "_serviceconsumermanagement_115_TenantResourceOut",
        "EnumIn": "_serviceconsumermanagement_116_EnumIn",
        "EnumOut": "_serviceconsumermanagement_117_EnumOut",
        "MixinIn": "_serviceconsumermanagement_118_MixinIn",
        "MixinOut": "_serviceconsumermanagement_119_MixinOut",
        "CppSettingsIn": "_serviceconsumermanagement_120_CppSettingsIn",
        "CppSettingsOut": "_serviceconsumermanagement_121_CppSettingsOut",
        "BillingDestinationIn": "_serviceconsumermanagement_122_BillingDestinationIn",
        "BillingDestinationOut": "_serviceconsumermanagement_123_BillingDestinationOut",
        "OAuthRequirementsIn": "_serviceconsumermanagement_124_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_serviceconsumermanagement_125_OAuthRequirementsOut",
        "MethodIn": "_serviceconsumermanagement_126_MethodIn",
        "MethodOut": "_serviceconsumermanagement_127_MethodOut",
        "QuotaLimitIn": "_serviceconsumermanagement_128_QuotaLimitIn",
        "QuotaLimitOut": "_serviceconsumermanagement_129_QuotaLimitOut",
        "V1Beta1ProducerQuotaPolicyIn": "_serviceconsumermanagement_130_V1Beta1ProducerQuotaPolicyIn",
        "V1Beta1ProducerQuotaPolicyOut": "_serviceconsumermanagement_131_V1Beta1ProducerQuotaPolicyOut",
        "V1DisableConsumerResponseIn": "_serviceconsumermanagement_132_V1DisableConsumerResponseIn",
        "V1DisableConsumerResponseOut": "_serviceconsumermanagement_133_V1DisableConsumerResponseOut",
        "V1Beta1DisableConsumerResponseIn": "_serviceconsumermanagement_134_V1Beta1DisableConsumerResponseIn",
        "V1Beta1DisableConsumerResponseOut": "_serviceconsumermanagement_135_V1Beta1DisableConsumerResponseOut",
        "V1Beta1ImportProducerOverridesResponseIn": "_serviceconsumermanagement_136_V1Beta1ImportProducerOverridesResponseIn",
        "V1Beta1ImportProducerOverridesResponseOut": "_serviceconsumermanagement_137_V1Beta1ImportProducerOverridesResponseOut",
        "MetricDescriptorIn": "_serviceconsumermanagement_138_MetricDescriptorIn",
        "MetricDescriptorOut": "_serviceconsumermanagement_139_MetricDescriptorOut",
        "V1DefaultIdentityIn": "_serviceconsumermanagement_140_V1DefaultIdentityIn",
        "V1DefaultIdentityOut": "_serviceconsumermanagement_141_V1DefaultIdentityOut",
        "DocumentationIn": "_serviceconsumermanagement_142_DocumentationIn",
        "DocumentationOut": "_serviceconsumermanagement_143_DocumentationOut",
        "HttpIn": "_serviceconsumermanagement_144_HttpIn",
        "HttpOut": "_serviceconsumermanagement_145_HttpOut",
        "UndeleteTenantProjectRequestIn": "_serviceconsumermanagement_146_UndeleteTenantProjectRequestIn",
        "UndeleteTenantProjectRequestOut": "_serviceconsumermanagement_147_UndeleteTenantProjectRequestOut",
        "HttpRuleIn": "_serviceconsumermanagement_148_HttpRuleIn",
        "HttpRuleOut": "_serviceconsumermanagement_149_HttpRuleOut",
        "ContextRuleIn": "_serviceconsumermanagement_150_ContextRuleIn",
        "ContextRuleOut": "_serviceconsumermanagement_151_ContextRuleOut",
        "ApiIn": "_serviceconsumermanagement_152_ApiIn",
        "ApiOut": "_serviceconsumermanagement_153_ApiOut",
        "TenantProjectConfigIn": "_serviceconsumermanagement_154_TenantProjectConfigIn",
        "TenantProjectConfigOut": "_serviceconsumermanagement_155_TenantProjectConfigOut",
        "PublishingIn": "_serviceconsumermanagement_156_PublishingIn",
        "PublishingOut": "_serviceconsumermanagement_157_PublishingOut",
        "NodeSettingsIn": "_serviceconsumermanagement_158_NodeSettingsIn",
        "NodeSettingsOut": "_serviceconsumermanagement_159_NodeSettingsOut",
        "SystemParameterIn": "_serviceconsumermanagement_160_SystemParameterIn",
        "SystemParameterOut": "_serviceconsumermanagement_161_SystemParameterOut",
        "PageIn": "_serviceconsumermanagement_162_PageIn",
        "PageOut": "_serviceconsumermanagement_163_PageOut",
        "CreateTenancyUnitRequestIn": "_serviceconsumermanagement_164_CreateTenancyUnitRequestIn",
        "CreateTenancyUnitRequestOut": "_serviceconsumermanagement_165_CreateTenancyUnitRequestOut",
        "V1EnableConsumerResponseIn": "_serviceconsumermanagement_166_V1EnableConsumerResponseIn",
        "V1EnableConsumerResponseOut": "_serviceconsumermanagement_167_V1EnableConsumerResponseOut",
        "CustomErrorIn": "_serviceconsumermanagement_168_CustomErrorIn",
        "CustomErrorOut": "_serviceconsumermanagement_169_CustomErrorOut",
        "SourceInfoIn": "_serviceconsumermanagement_170_SourceInfoIn",
        "SourceInfoOut": "_serviceconsumermanagement_171_SourceInfoOut",
        "V1GenerateServiceAccountResponseIn": "_serviceconsumermanagement_172_V1GenerateServiceAccountResponseIn",
        "V1GenerateServiceAccountResponseOut": "_serviceconsumermanagement_173_V1GenerateServiceAccountResponseOut",
        "LoggingDestinationIn": "_serviceconsumermanagement_174_LoggingDestinationIn",
        "LoggingDestinationOut": "_serviceconsumermanagement_175_LoggingDestinationOut",
        "ListTenancyUnitsResponseIn": "_serviceconsumermanagement_176_ListTenancyUnitsResponseIn",
        "ListTenancyUnitsResponseOut": "_serviceconsumermanagement_177_ListTenancyUnitsResponseOut",
        "JavaSettingsIn": "_serviceconsumermanagement_178_JavaSettingsIn",
        "JavaSettingsOut": "_serviceconsumermanagement_179_JavaSettingsOut",
        "V1Beta1EnableConsumerResponseIn": "_serviceconsumermanagement_180_V1Beta1EnableConsumerResponseIn",
        "V1Beta1EnableConsumerResponseOut": "_serviceconsumermanagement_181_V1Beta1EnableConsumerResponseOut",
        "SearchTenancyUnitsResponseIn": "_serviceconsumermanagement_182_SearchTenancyUnitsResponseIn",
        "SearchTenancyUnitsResponseOut": "_serviceconsumermanagement_183_SearchTenancyUnitsResponseOut",
        "BackendRuleIn": "_serviceconsumermanagement_184_BackendRuleIn",
        "BackendRuleOut": "_serviceconsumermanagement_185_BackendRuleOut",
        "TenantProjectPolicyIn": "_serviceconsumermanagement_186_TenantProjectPolicyIn",
        "TenantProjectPolicyOut": "_serviceconsumermanagement_187_TenantProjectPolicyOut",
        "JwtLocationIn": "_serviceconsumermanagement_188_JwtLocationIn",
        "JwtLocationOut": "_serviceconsumermanagement_189_JwtLocationOut",
        "AuthenticationRuleIn": "_serviceconsumermanagement_190_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_serviceconsumermanagement_191_AuthenticationRuleOut",
        "V1Beta1RefreshConsumerResponseIn": "_serviceconsumermanagement_192_V1Beta1RefreshConsumerResponseIn",
        "V1Beta1RefreshConsumerResponseOut": "_serviceconsumermanagement_193_V1Beta1RefreshConsumerResponseOut",
        "AddTenantProjectRequestIn": "_serviceconsumermanagement_194_AddTenantProjectRequestIn",
        "AddTenantProjectRequestOut": "_serviceconsumermanagement_195_AddTenantProjectRequestOut",
        "ControlIn": "_serviceconsumermanagement_196_ControlIn",
        "ControlOut": "_serviceconsumermanagement_197_ControlOut",
        "MonitoredResourceDescriptorIn": "_serviceconsumermanagement_198_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_serviceconsumermanagement_199_MonitoredResourceDescriptorOut",
        "BillingConfigIn": "_serviceconsumermanagement_200_BillingConfigIn",
        "BillingConfigOut": "_serviceconsumermanagement_201_BillingConfigOut",
        "CommonLanguageSettingsIn": "_serviceconsumermanagement_202_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_serviceconsumermanagement_203_CommonLanguageSettingsOut",
        "MonitoringIn": "_serviceconsumermanagement_204_MonitoringIn",
        "MonitoringOut": "_serviceconsumermanagement_205_MonitoringOut",
        "DotnetSettingsIn": "_serviceconsumermanagement_206_DotnetSettingsIn",
        "DotnetSettingsOut": "_serviceconsumermanagement_207_DotnetSettingsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
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
    types["V1GenerateDefaultIdentityResponseIn"] = t.struct(
        {
            "role": t.string().optional(),
            "attachStatus": t.string().optional(),
            "identity": t.proxy(renames["V1DefaultIdentityIn"]).optional(),
        }
    ).named(renames["V1GenerateDefaultIdentityResponseIn"])
    types["V1GenerateDefaultIdentityResponseOut"] = t.struct(
        {
            "role": t.string().optional(),
            "attachStatus": t.string().optional(),
            "identity": t.proxy(renames["V1DefaultIdentityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1GenerateDefaultIdentityResponseOut"])
    types["AttachTenantProjectRequestIn"] = t.struct(
        {
            "reservedResource": t.string().optional(),
            "externalResource": t.string().optional(),
            "tag": t.string(),
        }
    ).named(renames["AttachTenantProjectRequestIn"])
    types["AttachTenantProjectRequestOut"] = t.struct(
        {
            "reservedResource": t.string().optional(),
            "externalResource": t.string().optional(),
            "tag": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttachTenantProjectRequestOut"])
    types["ServiceIn"] = t.struct(
        {
            "http": t.proxy(renames["HttpIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "name": t.string().optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "producerProjectId": t.string().optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "id": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "title": t.string().optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "configVersion": t.integer().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "http": t.proxy(renames["HttpOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "name": t.string().optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "producerProjectId": t.string().optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "id": t.string().optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "title": t.string().optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "configVersion": t.integer().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
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
    types["FieldIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "cardinality": t.string().optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "jsonName": t.string().optional(),
            "number": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "cardinality": t.string().optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "kind": t.string().optional(),
            "jsonName": t.string().optional(),
            "number": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
    types["V1Beta1GenerateServiceIdentityResponseIn"] = t.struct(
        {"identity": t.proxy(renames["V1Beta1ServiceIdentityIn"]).optional()}
    ).named(renames["V1Beta1GenerateServiceIdentityResponseIn"])
    types["V1Beta1GenerateServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["V1Beta1ServiceIdentityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1GenerateServiceIdentityResponseOut"])
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
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
    types["V1Beta1ServiceIdentityIn"] = t.struct(
        {
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
            "name": t.string().optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["V1Beta1ServiceIdentityIn"])
    types["V1Beta1ServiceIdentityOut"] = t.struct(
        {
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
            "name": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1ServiceIdentityOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
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
    types["LongRunningIn"] = t.struct(
        {
            "totalPollTimeout": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "initialPollDelay": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "totalPollTimeout": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "initialPollDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
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
    types["DeleteTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["DeleteTenantProjectRequestIn"]
    )
    types["DeleteTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTenantProjectRequestOut"])
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
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["V1AddVisibilityLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["V1AddVisibilityLabelsResponseIn"])
    types["V1AddVisibilityLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1AddVisibilityLabelsResponseOut"])
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
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "version": t.string().optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "version": t.string().optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
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
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
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
    types["V1Beta1QuotaOverrideIn"] = t.struct(
        {
            "adminOverrideAncestor": t.string().optional(),
            "unit": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "overrideValue": t.string().optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["V1Beta1QuotaOverrideIn"])
    types["V1Beta1QuotaOverrideOut"] = t.struct(
        {
            "adminOverrideAncestor": t.string().optional(),
            "unit": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "overrideValue": t.string().optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1QuotaOverrideOut"])
    types["UsageRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "allowUnregisteredCalls": t.boolean().optional(),
            "skipServiceControl": t.boolean().optional(),
        }
    ).named(renames["UsageRuleIn"])
    types["UsageRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "allowUnregisteredCalls": t.boolean().optional(),
            "skipServiceControl": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UsageRuleOut"])
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
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
    types["V1RemoveVisibilityLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["V1RemoveVisibilityLabelsResponseIn"])
    types["V1RemoveVisibilityLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1RemoveVisibilityLabelsResponseOut"])
    types["RemoveTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["RemoveTenantProjectRequestIn"]
    )
    types["RemoveTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveTenantProjectRequestOut"])
    types["V1ServiceAccountIn"] = t.struct(
        {
            "iamAccountName": t.string().optional(),
            "tag": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
        }
    ).named(renames["V1ServiceAccountIn"])
    types["V1ServiceAccountOut"] = t.struct(
        {
            "iamAccountName": t.string().optional(),
            "tag": t.string().optional(),
            "name": t.string().optional(),
            "email": t.string().optional(),
            "uniqueId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1ServiceAccountOut"])
    types["TenancyUnitIn"] = t.struct(
        {
            "tenantResources": t.array(t.proxy(renames["TenantResourceIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TenancyUnitIn"])
    types["TenancyUnitOut"] = t.struct(
        {
            "consumer": t.string().optional(),
            "createTime": t.string().optional(),
            "service": t.string().optional(),
            "tenantResources": t.array(
                t.proxy(renames["TenantResourceOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenancyUnitOut"])
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
    types["LogDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
    types["EndpointIn"] = t.struct(
        {
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["V1RefreshConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1RefreshConsumerResponseIn"]
    )
    types["V1RefreshConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1RefreshConsumerResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["TypeIn"] = t.struct(
        {
            "syntax": t.string().optional(),
            "edition": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "syntax": t.string().optional(),
            "edition": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
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
    types["EnumIn"] = t.struct(
        {
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
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
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
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
            "requestStreaming": t.boolean().optional(),
            "requestTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "requestStreaming": t.boolean().optional(),
            "requestTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "responseStreaming": t.boolean().optional(),
            "responseTypeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "freeTier": t.string().optional(),
            "duration": t.string().optional(),
            "description": t.string().optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "defaultLimit": t.string().optional(),
            "maxLimit": t.string().optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "freeTier": t.string().optional(),
            "duration": t.string().optional(),
            "description": t.string().optional(),
            "metric": t.string().optional(),
            "name": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "defaultLimit": t.string().optional(),
            "maxLimit": t.string().optional(),
            "unit": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["V1Beta1ProducerQuotaPolicyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
            "policyValue": t.string().optional(),
            "container": t.string().optional(),
            "metric": t.string().optional(),
        }
    ).named(renames["V1Beta1ProducerQuotaPolicyIn"])
    types["V1Beta1ProducerQuotaPolicyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
            "policyValue": t.string().optional(),
            "container": t.string().optional(),
            "metric": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1ProducerQuotaPolicyOut"])
    types["V1DisableConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1DisableConsumerResponseIn"]
    )
    types["V1DisableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1DisableConsumerResponseOut"])
    types["V1Beta1DisableConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1DisableConsumerResponseIn"])
    types["V1Beta1DisableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1DisableConsumerResponseOut"])
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
    types["MetricDescriptorIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "description": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["V1DefaultIdentityIn"] = t.struct(
        {
            "name": t.string().optional(),
            "tag": t.string().optional(),
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["V1DefaultIdentityIn"])
    types["V1DefaultIdentityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "tag": t.string().optional(),
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1DefaultIdentityOut"])
    types["DocumentationIn"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "overview": t.string().optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "serviceRootUrl": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "overview": t.string().optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
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
    types["UndeleteTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["UndeleteTenantProjectRequestIn"]
    )
    types["UndeleteTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteTenantProjectRequestOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "get": t.string().optional(),
            "body": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "delete": t.string().optional(),
            "post": t.string().optional(),
            "responseBody": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "patch": t.string().optional(),
            "put": t.string().optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "get": t.string().optional(),
            "body": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "delete": t.string().optional(),
            "post": t.string().optional(),
            "responseBody": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "patch": t.string().optional(),
            "put": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["ApiIn"] = t.struct(
        {
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
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
    types["PublishingIn"] = t.struct(
        {
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "docTagPrefix": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "newIssueUri": t.string().optional(),
            "documentationUri": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "organization": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "githubLabel": t.string().optional(),
            "apiShortName": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "docTagPrefix": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "newIssueUri": t.string().optional(),
            "documentationUri": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "organization": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "githubLabel": t.string().optional(),
            "apiShortName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
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
    types["CreateTenancyUnitRequestIn"] = t.struct(
        {"tenancyUnitId": t.string().optional()}
    ).named(renames["CreateTenancyUnitRequestIn"])
    types["CreateTenancyUnitRequestOut"] = t.struct(
        {
            "tenancyUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTenancyUnitRequestOut"])
    types["V1EnableConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1EnableConsumerResponseIn"]
    )
    types["V1EnableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1EnableConsumerResponseOut"])
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
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
    types["V1GenerateServiceAccountResponseIn"] = t.struct(
        {"account": t.proxy(renames["V1ServiceAccountIn"]).optional()}
    ).named(renames["V1GenerateServiceAccountResponseIn"])
    types["V1GenerateServiceAccountResponseOut"] = t.struct(
        {
            "account": t.proxy(renames["V1ServiceAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1GenerateServiceAccountResponseOut"])
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
    types["JavaSettingsIn"] = t.struct(
        {
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "libraryPackage": t.string().optional(),
        }
    ).named(renames["JavaSettingsIn"])
    types["JavaSettingsOut"] = t.struct(
        {
            "serviceClassNames": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "libraryPackage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JavaSettingsOut"])
    types["V1Beta1EnableConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1EnableConsumerResponseIn"])
    types["V1Beta1EnableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1EnableConsumerResponseOut"])
    types["SearchTenancyUnitsResponseIn"] = t.struct(
        {
            "tenancyUnits": t.array(t.proxy(renames["TenancyUnitIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchTenancyUnitsResponseIn"])
    types["SearchTenancyUnitsResponseOut"] = t.struct(
        {
            "tenancyUnits": t.array(t.proxy(renames["TenancyUnitOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchTenancyUnitsResponseOut"])
    types["BackendRuleIn"] = t.struct(
        {
            "minDeadline": t.number().optional(),
            "protocol": t.string().optional(),
            "disableAuth": t.boolean().optional(),
            "operationDeadline": t.number().optional(),
            "jwtAudience": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "deadline": t.number().optional(),
            "pathTranslation": t.string(),
            "address": t.string().optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "minDeadline": t.number().optional(),
            "protocol": t.string().optional(),
            "disableAuth": t.boolean().optional(),
            "operationDeadline": t.number().optional(),
            "jwtAudience": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "deadline": t.number().optional(),
            "pathTranslation": t.string(),
            "address": t.string().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["TenantProjectPolicyIn"] = t.struct(
        {"policyBindings": t.array(t.proxy(renames["PolicyBindingIn"])).optional()}
    ).named(renames["TenantProjectPolicyIn"])
    types["TenantProjectPolicyOut"] = t.struct(
        {
            "policyBindings": t.array(t.proxy(renames["PolicyBindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantProjectPolicyOut"])
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
    types["AuthenticationRuleIn"] = t.struct(
        {
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "selector": t.string().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "selector": t.string().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
    types["V1Beta1RefreshConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1RefreshConsumerResponseIn"])
    types["V1Beta1RefreshConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1RefreshConsumerResponseOut"])
    types["AddTenantProjectRequestIn"] = t.struct(
        {
            "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
            "tag": t.string(),
        }
    ).named(renames["AddTenantProjectRequestIn"])
    types["AddTenantProjectRequestOut"] = t.struct(
        {
            "projectConfig": t.proxy(renames["TenantProjectConfigOut"]).optional(),
            "tag": t.string(),
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
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["BillingConfigIn"] = t.struct(
        {"billingAccount": t.string().optional()}
    ).named(renames["BillingConfigIn"])
    types["BillingConfigOut"] = t.struct(
        {
            "billingAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingConfigOut"])
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
    types["DotnetSettingsIn"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])

    functions = {}
    functions["servicesSearch"] = serviceconsumermanagement.get(
        "v1/{parent}:search",
        t.struct(
            {
                "parent": t.string(),
                "query": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchTenancyUnitsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsAddProject"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesTenancyUnitsApplyProjectConfig"
    ] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsList"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsAttachProject"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsDeleteProject"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsUndeleteProject"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsRemoveProject"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsCreate"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsDelete"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = serviceconsumermanagement.get(
        "v1/{name}",
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
    functions["operationsDelete"] = serviceconsumermanagement.get(
        "v1/{name}",
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
    functions["operationsGet"] = serviceconsumermanagement.get(
        "v1/{name}",
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
    functions["operationsList"] = serviceconsumermanagement.get(
        "v1/{name}",
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

    return Import(
        importer="serviceconsumermanagement",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
