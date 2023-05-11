from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_serviceconsumermanagement() -> Import:
    serviceconsumermanagement = HTTPRuntime(
        "https://serviceconsumermanagement.googleapis.com/"
    )

    renames = {
        "ErrorResponse": "_serviceconsumermanagement_1_ErrorResponse",
        "ContextIn": "_serviceconsumermanagement_2_ContextIn",
        "ContextOut": "_serviceconsumermanagement_3_ContextOut",
        "EnumValueIn": "_serviceconsumermanagement_4_EnumValueIn",
        "EnumValueOut": "_serviceconsumermanagement_5_EnumValueOut",
        "OperationIn": "_serviceconsumermanagement_6_OperationIn",
        "OperationOut": "_serviceconsumermanagement_7_OperationOut",
        "V1Beta1DisableConsumerResponseIn": "_serviceconsumermanagement_8_V1Beta1DisableConsumerResponseIn",
        "V1Beta1DisableConsumerResponseOut": "_serviceconsumermanagement_9_V1Beta1DisableConsumerResponseOut",
        "EmptyIn": "_serviceconsumermanagement_10_EmptyIn",
        "EmptyOut": "_serviceconsumermanagement_11_EmptyOut",
        "DocumentationIn": "_serviceconsumermanagement_12_DocumentationIn",
        "DocumentationOut": "_serviceconsumermanagement_13_DocumentationOut",
        "SearchTenancyUnitsResponseIn": "_serviceconsumermanagement_14_SearchTenancyUnitsResponseIn",
        "SearchTenancyUnitsResponseOut": "_serviceconsumermanagement_15_SearchTenancyUnitsResponseOut",
        "EnumIn": "_serviceconsumermanagement_16_EnumIn",
        "EnumOut": "_serviceconsumermanagement_17_EnumOut",
        "FieldIn": "_serviceconsumermanagement_18_FieldIn",
        "FieldOut": "_serviceconsumermanagement_19_FieldOut",
        "UndeleteTenantProjectRequestIn": "_serviceconsumermanagement_20_UndeleteTenantProjectRequestIn",
        "UndeleteTenantProjectRequestOut": "_serviceconsumermanagement_21_UndeleteTenantProjectRequestOut",
        "V1GenerateDefaultIdentityResponseIn": "_serviceconsumermanagement_22_V1GenerateDefaultIdentityResponseIn",
        "V1GenerateDefaultIdentityResponseOut": "_serviceconsumermanagement_23_V1GenerateDefaultIdentityResponseOut",
        "TenantResourceIn": "_serviceconsumermanagement_24_TenantResourceIn",
        "TenantResourceOut": "_serviceconsumermanagement_25_TenantResourceOut",
        "MonitoringDestinationIn": "_serviceconsumermanagement_26_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_serviceconsumermanagement_27_MonitoringDestinationOut",
        "HttpRuleIn": "_serviceconsumermanagement_28_HttpRuleIn",
        "HttpRuleOut": "_serviceconsumermanagement_29_HttpRuleOut",
        "GoSettingsIn": "_serviceconsumermanagement_30_GoSettingsIn",
        "GoSettingsOut": "_serviceconsumermanagement_31_GoSettingsOut",
        "DeleteTenantProjectRequestIn": "_serviceconsumermanagement_32_DeleteTenantProjectRequestIn",
        "DeleteTenantProjectRequestOut": "_serviceconsumermanagement_33_DeleteTenantProjectRequestOut",
        "UsageRuleIn": "_serviceconsumermanagement_34_UsageRuleIn",
        "UsageRuleOut": "_serviceconsumermanagement_35_UsageRuleOut",
        "V1Beta1ImportProducerOverridesResponseIn": "_serviceconsumermanagement_36_V1Beta1ImportProducerOverridesResponseIn",
        "V1Beta1ImportProducerOverridesResponseOut": "_serviceconsumermanagement_37_V1Beta1ImportProducerOverridesResponseOut",
        "SystemParameterIn": "_serviceconsumermanagement_38_SystemParameterIn",
        "SystemParameterOut": "_serviceconsumermanagement_39_SystemParameterOut",
        "MetricDescriptorMetadataIn": "_serviceconsumermanagement_40_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_serviceconsumermanagement_41_MetricDescriptorMetadataOut",
        "BackendRuleIn": "_serviceconsumermanagement_42_BackendRuleIn",
        "BackendRuleOut": "_serviceconsumermanagement_43_BackendRuleOut",
        "V1AddVisibilityLabelsResponseIn": "_serviceconsumermanagement_44_V1AddVisibilityLabelsResponseIn",
        "V1AddVisibilityLabelsResponseOut": "_serviceconsumermanagement_45_V1AddVisibilityLabelsResponseOut",
        "BillingIn": "_serviceconsumermanagement_46_BillingIn",
        "BillingOut": "_serviceconsumermanagement_47_BillingOut",
        "V1Beta1RefreshConsumerResponseIn": "_serviceconsumermanagement_48_V1Beta1RefreshConsumerResponseIn",
        "V1Beta1RefreshConsumerResponseOut": "_serviceconsumermanagement_49_V1Beta1RefreshConsumerResponseOut",
        "UsageIn": "_serviceconsumermanagement_50_UsageIn",
        "UsageOut": "_serviceconsumermanagement_51_UsageOut",
        "CppSettingsIn": "_serviceconsumermanagement_52_CppSettingsIn",
        "CppSettingsOut": "_serviceconsumermanagement_53_CppSettingsOut",
        "MonitoredResourceDescriptorIn": "_serviceconsumermanagement_54_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_serviceconsumermanagement_55_MonitoredResourceDescriptorOut",
        "BillingDestinationIn": "_serviceconsumermanagement_56_BillingDestinationIn",
        "BillingDestinationOut": "_serviceconsumermanagement_57_BillingDestinationOut",
        "V1EnableConsumerResponseIn": "_serviceconsumermanagement_58_V1EnableConsumerResponseIn",
        "V1EnableConsumerResponseOut": "_serviceconsumermanagement_59_V1EnableConsumerResponseOut",
        "JwtLocationIn": "_serviceconsumermanagement_60_JwtLocationIn",
        "JwtLocationOut": "_serviceconsumermanagement_61_JwtLocationOut",
        "TenantProjectPolicyIn": "_serviceconsumermanagement_62_TenantProjectPolicyIn",
        "TenantProjectPolicyOut": "_serviceconsumermanagement_63_TenantProjectPolicyOut",
        "TypeIn": "_serviceconsumermanagement_64_TypeIn",
        "TypeOut": "_serviceconsumermanagement_65_TypeOut",
        "ListTenancyUnitsResponseIn": "_serviceconsumermanagement_66_ListTenancyUnitsResponseIn",
        "ListTenancyUnitsResponseOut": "_serviceconsumermanagement_67_ListTenancyUnitsResponseOut",
        "NodeSettingsIn": "_serviceconsumermanagement_68_NodeSettingsIn",
        "NodeSettingsOut": "_serviceconsumermanagement_69_NodeSettingsOut",
        "DotnetSettingsIn": "_serviceconsumermanagement_70_DotnetSettingsIn",
        "DotnetSettingsOut": "_serviceconsumermanagement_71_DotnetSettingsOut",
        "ContextRuleIn": "_serviceconsumermanagement_72_ContextRuleIn",
        "ContextRuleOut": "_serviceconsumermanagement_73_ContextRuleOut",
        "MetricRuleIn": "_serviceconsumermanagement_74_MetricRuleIn",
        "MetricRuleOut": "_serviceconsumermanagement_75_MetricRuleOut",
        "V1DisableConsumerResponseIn": "_serviceconsumermanagement_76_V1DisableConsumerResponseIn",
        "V1DisableConsumerResponseOut": "_serviceconsumermanagement_77_V1DisableConsumerResponseOut",
        "PageIn": "_serviceconsumermanagement_78_PageIn",
        "PageOut": "_serviceconsumermanagement_79_PageOut",
        "LabelDescriptorIn": "_serviceconsumermanagement_80_LabelDescriptorIn",
        "LabelDescriptorOut": "_serviceconsumermanagement_81_LabelDescriptorOut",
        "V1Beta1ServiceIdentityIn": "_serviceconsumermanagement_82_V1Beta1ServiceIdentityIn",
        "V1Beta1ServiceIdentityOut": "_serviceconsumermanagement_83_V1Beta1ServiceIdentityOut",
        "V1Beta1QuotaOverrideIn": "_serviceconsumermanagement_84_V1Beta1QuotaOverrideIn",
        "V1Beta1QuotaOverrideOut": "_serviceconsumermanagement_85_V1Beta1QuotaOverrideOut",
        "V1Beta1GenerateServiceIdentityResponseIn": "_serviceconsumermanagement_86_V1Beta1GenerateServiceIdentityResponseIn",
        "V1Beta1GenerateServiceIdentityResponseOut": "_serviceconsumermanagement_87_V1Beta1GenerateServiceIdentityResponseOut",
        "RubySettingsIn": "_serviceconsumermanagement_88_RubySettingsIn",
        "RubySettingsOut": "_serviceconsumermanagement_89_RubySettingsOut",
        "V1Beta1ProducerQuotaPolicyIn": "_serviceconsumermanagement_90_V1Beta1ProducerQuotaPolicyIn",
        "V1Beta1ProducerQuotaPolicyOut": "_serviceconsumermanagement_91_V1Beta1ProducerQuotaPolicyOut",
        "PublishingIn": "_serviceconsumermanagement_92_PublishingIn",
        "PublishingOut": "_serviceconsumermanagement_93_PublishingOut",
        "SystemParametersIn": "_serviceconsumermanagement_94_SystemParametersIn",
        "SystemParametersOut": "_serviceconsumermanagement_95_SystemParametersOut",
        "OptionIn": "_serviceconsumermanagement_96_OptionIn",
        "OptionOut": "_serviceconsumermanagement_97_OptionOut",
        "LogDescriptorIn": "_serviceconsumermanagement_98_LogDescriptorIn",
        "LogDescriptorOut": "_serviceconsumermanagement_99_LogDescriptorOut",
        "QuotaLimitIn": "_serviceconsumermanagement_100_QuotaLimitIn",
        "QuotaLimitOut": "_serviceconsumermanagement_101_QuotaLimitOut",
        "AddTenantProjectRequestIn": "_serviceconsumermanagement_102_AddTenantProjectRequestIn",
        "AddTenantProjectRequestOut": "_serviceconsumermanagement_103_AddTenantProjectRequestOut",
        "LongRunningIn": "_serviceconsumermanagement_104_LongRunningIn",
        "LongRunningOut": "_serviceconsumermanagement_105_LongRunningOut",
        "BackendIn": "_serviceconsumermanagement_106_BackendIn",
        "BackendOut": "_serviceconsumermanagement_107_BackendOut",
        "V1RefreshConsumerResponseIn": "_serviceconsumermanagement_108_V1RefreshConsumerResponseIn",
        "V1RefreshConsumerResponseOut": "_serviceconsumermanagement_109_V1RefreshConsumerResponseOut",
        "V1Beta1BatchCreateProducerOverridesResponseIn": "_serviceconsumermanagement_110_V1Beta1BatchCreateProducerOverridesResponseIn",
        "V1Beta1BatchCreateProducerOverridesResponseOut": "_serviceconsumermanagement_111_V1Beta1BatchCreateProducerOverridesResponseOut",
        "ListOperationsResponseIn": "_serviceconsumermanagement_112_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_serviceconsumermanagement_113_ListOperationsResponseOut",
        "DocumentationRuleIn": "_serviceconsumermanagement_114_DocumentationRuleIn",
        "DocumentationRuleOut": "_serviceconsumermanagement_115_DocumentationRuleOut",
        "QuotaIn": "_serviceconsumermanagement_116_QuotaIn",
        "QuotaOut": "_serviceconsumermanagement_117_QuotaOut",
        "CancelOperationRequestIn": "_serviceconsumermanagement_118_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_serviceconsumermanagement_119_CancelOperationRequestOut",
        "MetricDescriptorIn": "_serviceconsumermanagement_120_MetricDescriptorIn",
        "MetricDescriptorOut": "_serviceconsumermanagement_121_MetricDescriptorOut",
        "PolicyBindingIn": "_serviceconsumermanagement_122_PolicyBindingIn",
        "PolicyBindingOut": "_serviceconsumermanagement_123_PolicyBindingOut",
        "ApiIn": "_serviceconsumermanagement_124_ApiIn",
        "ApiOut": "_serviceconsumermanagement_125_ApiOut",
        "CustomHttpPatternIn": "_serviceconsumermanagement_126_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_serviceconsumermanagement_127_CustomHttpPatternOut",
        "PythonSettingsIn": "_serviceconsumermanagement_128_PythonSettingsIn",
        "PythonSettingsOut": "_serviceconsumermanagement_129_PythonSettingsOut",
        "MixinIn": "_serviceconsumermanagement_130_MixinIn",
        "MixinOut": "_serviceconsumermanagement_131_MixinOut",
        "V1GenerateServiceAccountResponseIn": "_serviceconsumermanagement_132_V1GenerateServiceAccountResponseIn",
        "V1GenerateServiceAccountResponseOut": "_serviceconsumermanagement_133_V1GenerateServiceAccountResponseOut",
        "LoggingIn": "_serviceconsumermanagement_134_LoggingIn",
        "LoggingOut": "_serviceconsumermanagement_135_LoggingOut",
        "MethodSettingsIn": "_serviceconsumermanagement_136_MethodSettingsIn",
        "MethodSettingsOut": "_serviceconsumermanagement_137_MethodSettingsOut",
        "V1ServiceAccountIn": "_serviceconsumermanagement_138_V1ServiceAccountIn",
        "V1ServiceAccountOut": "_serviceconsumermanagement_139_V1ServiceAccountOut",
        "MonitoringIn": "_serviceconsumermanagement_140_MonitoringIn",
        "MonitoringOut": "_serviceconsumermanagement_141_MonitoringOut",
        "AuthenticationIn": "_serviceconsumermanagement_142_AuthenticationIn",
        "AuthenticationOut": "_serviceconsumermanagement_143_AuthenticationOut",
        "TenantProjectConfigIn": "_serviceconsumermanagement_144_TenantProjectConfigIn",
        "TenantProjectConfigOut": "_serviceconsumermanagement_145_TenantProjectConfigOut",
        "ServiceAccountConfigIn": "_serviceconsumermanagement_146_ServiceAccountConfigIn",
        "ServiceAccountConfigOut": "_serviceconsumermanagement_147_ServiceAccountConfigOut",
        "V1RemoveVisibilityLabelsResponseIn": "_serviceconsumermanagement_148_V1RemoveVisibilityLabelsResponseIn",
        "V1RemoveVisibilityLabelsResponseOut": "_serviceconsumermanagement_149_V1RemoveVisibilityLabelsResponseOut",
        "ApplyTenantProjectConfigRequestIn": "_serviceconsumermanagement_150_ApplyTenantProjectConfigRequestIn",
        "ApplyTenantProjectConfigRequestOut": "_serviceconsumermanagement_151_ApplyTenantProjectConfigRequestOut",
        "EndpointIn": "_serviceconsumermanagement_152_EndpointIn",
        "EndpointOut": "_serviceconsumermanagement_153_EndpointOut",
        "LoggingDestinationIn": "_serviceconsumermanagement_154_LoggingDestinationIn",
        "LoggingDestinationOut": "_serviceconsumermanagement_155_LoggingDestinationOut",
        "TenancyUnitIn": "_serviceconsumermanagement_156_TenancyUnitIn",
        "TenancyUnitOut": "_serviceconsumermanagement_157_TenancyUnitOut",
        "SourceInfoIn": "_serviceconsumermanagement_158_SourceInfoIn",
        "SourceInfoOut": "_serviceconsumermanagement_159_SourceInfoOut",
        "SourceContextIn": "_serviceconsumermanagement_160_SourceContextIn",
        "SourceContextOut": "_serviceconsumermanagement_161_SourceContextOut",
        "AuthenticationRuleIn": "_serviceconsumermanagement_162_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_serviceconsumermanagement_163_AuthenticationRuleOut",
        "V1DefaultIdentityIn": "_serviceconsumermanagement_164_V1DefaultIdentityIn",
        "V1DefaultIdentityOut": "_serviceconsumermanagement_165_V1DefaultIdentityOut",
        "OAuthRequirementsIn": "_serviceconsumermanagement_166_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_serviceconsumermanagement_167_OAuthRequirementsOut",
        "HttpIn": "_serviceconsumermanagement_168_HttpIn",
        "HttpOut": "_serviceconsumermanagement_169_HttpOut",
        "AttachTenantProjectRequestIn": "_serviceconsumermanagement_170_AttachTenantProjectRequestIn",
        "AttachTenantProjectRequestOut": "_serviceconsumermanagement_171_AttachTenantProjectRequestOut",
        "JavaSettingsIn": "_serviceconsumermanagement_172_JavaSettingsIn",
        "JavaSettingsOut": "_serviceconsumermanagement_173_JavaSettingsOut",
        "V1Beta1ImportProducerQuotaPoliciesResponseIn": "_serviceconsumermanagement_174_V1Beta1ImportProducerQuotaPoliciesResponseIn",
        "V1Beta1ImportProducerQuotaPoliciesResponseOut": "_serviceconsumermanagement_175_V1Beta1ImportProducerQuotaPoliciesResponseOut",
        "AuthProviderIn": "_serviceconsumermanagement_176_AuthProviderIn",
        "AuthProviderOut": "_serviceconsumermanagement_177_AuthProviderOut",
        "ControlIn": "_serviceconsumermanagement_178_ControlIn",
        "ControlOut": "_serviceconsumermanagement_179_ControlOut",
        "BillingConfigIn": "_serviceconsumermanagement_180_BillingConfigIn",
        "BillingConfigOut": "_serviceconsumermanagement_181_BillingConfigOut",
        "ClientLibrarySettingsIn": "_serviceconsumermanagement_182_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_serviceconsumermanagement_183_ClientLibrarySettingsOut",
        "AuthRequirementIn": "_serviceconsumermanagement_184_AuthRequirementIn",
        "AuthRequirementOut": "_serviceconsumermanagement_185_AuthRequirementOut",
        "V1Beta1EnableConsumerResponseIn": "_serviceconsumermanagement_186_V1Beta1EnableConsumerResponseIn",
        "V1Beta1EnableConsumerResponseOut": "_serviceconsumermanagement_187_V1Beta1EnableConsumerResponseOut",
        "RemoveTenantProjectRequestIn": "_serviceconsumermanagement_188_RemoveTenantProjectRequestIn",
        "RemoveTenantProjectRequestOut": "_serviceconsumermanagement_189_RemoveTenantProjectRequestOut",
        "StatusIn": "_serviceconsumermanagement_190_StatusIn",
        "StatusOut": "_serviceconsumermanagement_191_StatusOut",
        "ServiceIn": "_serviceconsumermanagement_192_ServiceIn",
        "ServiceOut": "_serviceconsumermanagement_193_ServiceOut",
        "CommonLanguageSettingsIn": "_serviceconsumermanagement_194_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_serviceconsumermanagement_195_CommonLanguageSettingsOut",
        "MethodIn": "_serviceconsumermanagement_196_MethodIn",
        "MethodOut": "_serviceconsumermanagement_197_MethodOut",
        "CustomErrorRuleIn": "_serviceconsumermanagement_198_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_serviceconsumermanagement_199_CustomErrorRuleOut",
        "CreateTenancyUnitRequestIn": "_serviceconsumermanagement_200_CreateTenancyUnitRequestIn",
        "CreateTenancyUnitRequestOut": "_serviceconsumermanagement_201_CreateTenancyUnitRequestOut",
        "SystemParameterRuleIn": "_serviceconsumermanagement_202_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_serviceconsumermanagement_203_SystemParameterRuleOut",
        "PhpSettingsIn": "_serviceconsumermanagement_204_PhpSettingsIn",
        "PhpSettingsOut": "_serviceconsumermanagement_205_PhpSettingsOut",
        "CustomErrorIn": "_serviceconsumermanagement_206_CustomErrorIn",
        "CustomErrorOut": "_serviceconsumermanagement_207_CustomErrorOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
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
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["V1Beta1DisableConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1DisableConsumerResponseIn"])
    types["V1Beta1DisableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1DisableConsumerResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DocumentationIn"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "overview": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "summary": t.string().optional(),
            "documentationRootUrl": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "overview": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "summary": t.string().optional(),
            "documentationRootUrl": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
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
    types["EnumIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["FieldIn"] = t.struct(
        {
            "name": t.string().optional(),
            "packed": t.boolean().optional(),
            "typeUrl": t.string().optional(),
            "jsonName": t.string().optional(),
            "kind": t.string().optional(),
            "cardinality": t.string().optional(),
            "defaultValue": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "oneofIndex": t.integer().optional(),
            "number": t.integer().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "name": t.string().optional(),
            "packed": t.boolean().optional(),
            "typeUrl": t.string().optional(),
            "jsonName": t.string().optional(),
            "kind": t.string().optional(),
            "cardinality": t.string().optional(),
            "defaultValue": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "oneofIndex": t.integer().optional(),
            "number": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["UndeleteTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["UndeleteTenantProjectRequestIn"]
    )
    types["UndeleteTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteTenantProjectRequestOut"])
    types["V1GenerateDefaultIdentityResponseIn"] = t.struct(
        {
            "identity": t.proxy(renames["V1DefaultIdentityIn"]).optional(),
            "role": t.string().optional(),
            "attachStatus": t.string().optional(),
        }
    ).named(renames["V1GenerateDefaultIdentityResponseIn"])
    types["V1GenerateDefaultIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["V1DefaultIdentityOut"]).optional(),
            "role": t.string().optional(),
            "attachStatus": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1GenerateDefaultIdentityResponseOut"])
    types["TenantResourceIn"] = t.struct(
        {"status": t.string().optional(), "tag": t.string().optional()}
    ).named(renames["TenantResourceIn"])
    types["TenantResourceOut"] = t.struct(
        {
            "status": t.string().optional(),
            "resource": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantResourceOut"])
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
    types["HttpRuleIn"] = t.struct(
        {
            "body": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "delete": t.string().optional(),
            "post": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "selector": t.string().optional(),
            "responseBody": t.string().optional(),
            "patch": t.string().optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "body": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "delete": t.string().optional(),
            "post": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "selector": t.string().optional(),
            "responseBody": t.string().optional(),
            "patch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["DeleteTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["DeleteTenantProjectRequestIn"]
    )
    types["DeleteTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTenantProjectRequestOut"])
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
    types["BackendRuleIn"] = t.struct(
        {
            "protocol": t.string().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "pathTranslation": t.string(),
            "disableAuth": t.boolean().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "jwtAudience": t.string().optional(),
            "address": t.string().optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "protocol": t.string().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "pathTranslation": t.string(),
            "disableAuth": t.boolean().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "jwtAudience": t.string().optional(),
            "address": t.string().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["V1AddVisibilityLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["V1AddVisibilityLabelsResponseIn"])
    types["V1AddVisibilityLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1AddVisibilityLabelsResponseOut"])
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
    types["V1Beta1RefreshConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1RefreshConsumerResponseIn"])
    types["V1Beta1RefreshConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1RefreshConsumerResponseOut"])
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
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
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
    types["V1EnableConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1EnableConsumerResponseIn"]
    )
    types["V1EnableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1EnableConsumerResponseOut"])
    types["JwtLocationIn"] = t.struct(
        {
            "query": t.string().optional(),
            "header": t.string().optional(),
            "cookie": t.string().optional(),
            "valuePrefix": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "query": t.string().optional(),
            "header": t.string().optional(),
            "cookie": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["TenantProjectPolicyIn"] = t.struct(
        {"policyBindings": t.array(t.proxy(renames["PolicyBindingIn"])).optional()}
    ).named(renames["TenantProjectPolicyIn"])
    types["TenantProjectPolicyOut"] = t.struct(
        {
            "policyBindings": t.array(t.proxy(renames["PolicyBindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantProjectPolicyOut"])
    types["TypeIn"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "edition": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "edition": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
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
    types["V1DisableConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1DisableConsumerResponseIn"]
    )
    types["V1DisableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1DisableConsumerResponseOut"])
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
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "overrideValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
            "adminOverrideAncestor": t.string().optional(),
        }
    ).named(renames["V1Beta1QuotaOverrideIn"])
    types["V1Beta1QuotaOverrideOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "overrideValue": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
            "adminOverrideAncestor": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1QuotaOverrideOut"])
    types["V1Beta1GenerateServiceIdentityResponseIn"] = t.struct(
        {"identity": t.proxy(renames["V1Beta1ServiceIdentityIn"]).optional()}
    ).named(renames["V1Beta1GenerateServiceIdentityResponseIn"])
    types["V1Beta1GenerateServiceIdentityResponseOut"] = t.struct(
        {
            "identity": t.proxy(renames["V1Beta1ServiceIdentityOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1GenerateServiceIdentityResponseOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["V1Beta1ProducerQuotaPolicyIn"] = t.struct(
        {
            "policyValue": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "container": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["V1Beta1ProducerQuotaPolicyIn"])
    types["V1Beta1ProducerQuotaPolicyOut"] = t.struct(
        {
            "policyValue": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "container": t.string().optional(),
            "dimensions": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1Beta1ProducerQuotaPolicyOut"])
    types["PublishingIn"] = t.struct(
        {
            "newIssueUri": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "docTagPrefix": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "apiShortName": t.string().optional(),
            "githubLabel": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "documentationUri": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "newIssueUri": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "docTagPrefix": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "apiShortName": t.string().optional(),
            "githubLabel": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "documentationUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
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
    types["LogDescriptorIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "description": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "duration": t.string().optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "maxLimit": t.string().optional(),
            "freeTier": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "description": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "duration": t.string().optional(),
            "name": t.string().optional(),
            "metric": t.string().optional(),
            "unit": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "maxLimit": t.string().optional(),
            "freeTier": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
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
    types["LongRunningIn"] = t.struct(
        {
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "totalPollTimeout": t.string().optional(),
            "initialPollDelay": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "totalPollTimeout": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
    types["V1RefreshConsumerResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1RefreshConsumerResponseIn"]
    )
    types["V1RefreshConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1RefreshConsumerResponseOut"])
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
    types["DocumentationRuleIn"] = t.struct(
        {
            "disableReplacementWords": t.string().optional(),
            "description": t.string().optional(),
            "selector": t.string().optional(),
            "deprecationDescription": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "disableReplacementWords": t.string().optional(),
            "description": t.string().optional(),
            "selector": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "launchStage": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "metricKind": t.string().optional(),
            "valueType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["ApiIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "version": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "syntax": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "version": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "syntax": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
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
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
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
    types["V1GenerateServiceAccountResponseIn"] = t.struct(
        {"account": t.proxy(renames["V1ServiceAccountIn"]).optional()}
    ).named(renames["V1GenerateServiceAccountResponseIn"])
    types["V1GenerateServiceAccountResponseOut"] = t.struct(
        {
            "account": t.proxy(renames["V1ServiceAccountOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1GenerateServiceAccountResponseOut"])
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
    types["V1ServiceAccountIn"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "name": t.string().optional(),
            "iamAccountName": t.string().optional(),
            "email": t.string().optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["V1ServiceAccountIn"])
    types["V1ServiceAccountOut"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "name": t.string().optional(),
            "iamAccountName": t.string().optional(),
            "email": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1ServiceAccountOut"])
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
    types["TenantProjectConfigIn"] = t.struct(
        {
            "billingConfig": t.proxy(renames["BillingConfigIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "services": t.array(t.string()).optional(),
            "tenantProjectPolicy": t.proxy(renames["TenantProjectPolicyIn"]).optional(),
            "serviceAccountConfig": t.proxy(
                renames["ServiceAccountConfigIn"]
            ).optional(),
            "folder": t.string().optional(),
        }
    ).named(renames["TenantProjectConfigIn"])
    types["TenantProjectConfigOut"] = t.struct(
        {
            "billingConfig": t.proxy(renames["BillingConfigOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "services": t.array(t.string()).optional(),
            "tenantProjectPolicy": t.proxy(
                renames["TenantProjectPolicyOut"]
            ).optional(),
            "serviceAccountConfig": t.proxy(
                renames["ServiceAccountConfigOut"]
            ).optional(),
            "folder": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenantProjectConfigOut"])
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
    types["V1RemoveVisibilityLabelsResponseIn"] = t.struct(
        {"labels": t.array(t.string()).optional()}
    ).named(renames["V1RemoveVisibilityLabelsResponseIn"])
    types["V1RemoveVisibilityLabelsResponseOut"] = t.struct(
        {
            "labels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1RemoveVisibilityLabelsResponseOut"])
    types["ApplyTenantProjectConfigRequestIn"] = t.struct(
        {
            "tag": t.string(),
            "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
        }
    ).named(renames["ApplyTenantProjectConfigRequestIn"])
    types["ApplyTenantProjectConfigRequestOut"] = t.struct(
        {
            "tag": t.string(),
            "projectConfig": t.proxy(renames["TenantProjectConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplyTenantProjectConfigRequestOut"])
    types["EndpointIn"] = t.struct(
        {
            "allowCors": t.boolean().optional(),
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "target": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "allowCors": t.boolean().optional(),
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
            "service": t.string().optional(),
            "consumer": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TenancyUnitOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
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
    types["V1DefaultIdentityIn"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "tag": t.string().optional(),
        }
    ).named(renames["V1DefaultIdentityIn"])
    types["V1DefaultIdentityOut"] = t.struct(
        {
            "uniqueId": t.string().optional(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "tag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V1DefaultIdentityOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
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
    types["AuthProviderIn"] = t.struct(
        {
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "jwksUri": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "jwksUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["BillingConfigIn"] = t.struct(
        {"billingAccount": t.string().optional()}
    ).named(renames["BillingConfigIn"])
    types["BillingConfigOut"] = t.struct(
        {
            "billingAccount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BillingConfigOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "launchStage": t.string().optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "version": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "restNumericEnums": t.boolean().optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "version": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
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
    types["V1Beta1EnableConsumerResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["V1Beta1EnableConsumerResponseIn"])
    types["V1Beta1EnableConsumerResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1Beta1EnableConsumerResponseOut"])
    types["RemoveTenantProjectRequestIn"] = t.struct({"tag": t.string()}).named(
        renames["RemoveTenantProjectRequestIn"]
    )
    types["RemoveTenantProjectRequestOut"] = t.struct(
        {"tag": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveTenantProjectRequestOut"])
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
    types["ServiceIn"] = t.struct(
        {
            "control": t.proxy(renames["ControlIn"]).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "producerProjectId": t.string().optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "title": t.string().optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "id": t.string().optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "configVersion": t.integer().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "control": t.proxy(renames["ControlOut"]).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "producerProjectId": t.string().optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "title": t.string().optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "id": t.string().optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "configVersion": t.integer().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
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
    types["MethodIn"] = t.struct(
        {
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
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
    types["CreateTenancyUnitRequestIn"] = t.struct(
        {"tenancyUnitId": t.string().optional()}
    ).named(renames["CreateTenancyUnitRequestIn"])
    types["CreateTenancyUnitRequestOut"] = t.struct(
        {
            "tenancyUnitId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateTenancyUnitRequestOut"])
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
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
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

    functions = {}
    functions["operationsGet"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = serviceconsumermanagement.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
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
    functions["servicesTenancyUnitsCreate"] = serviceconsumermanagement.post(
        "v1/{parent}:addProject",
        t.struct(
            {
                "parent": t.string(),
                "tag": t.string(),
                "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsDelete"] = serviceconsumermanagement.post(
        "v1/{parent}:addProject",
        t.struct(
            {
                "parent": t.string(),
                "tag": t.string(),
                "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsList"] = serviceconsumermanagement.post(
        "v1/{parent}:addProject",
        t.struct(
            {
                "parent": t.string(),
                "tag": t.string(),
                "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsRemoveProject"] = serviceconsumermanagement.post(
        "v1/{parent}:addProject",
        t.struct(
            {
                "parent": t.string(),
                "tag": t.string(),
                "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsDeleteProject"] = serviceconsumermanagement.post(
        "v1/{parent}:addProject",
        t.struct(
            {
                "parent": t.string(),
                "tag": t.string(),
                "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsAttachProject"] = serviceconsumermanagement.post(
        "v1/{parent}:addProject",
        t.struct(
            {
                "parent": t.string(),
                "tag": t.string(),
                "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesTenancyUnitsApplyProjectConfig"
    ] = serviceconsumermanagement.post(
        "v1/{parent}:addProject",
        t.struct(
            {
                "parent": t.string(),
                "tag": t.string(),
                "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsUndeleteProject"] = serviceconsumermanagement.post(
        "v1/{parent}:addProject",
        t.struct(
            {
                "parent": t.string(),
                "tag": t.string(),
                "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesTenancyUnitsAddProject"] = serviceconsumermanagement.post(
        "v1/{parent}:addProject",
        t.struct(
            {
                "parent": t.string(),
                "tag": t.string(),
                "projectConfig": t.proxy(renames["TenantProjectConfigIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="serviceconsumermanagement",
        renames=renames,
        types=types,
        functions=functions,
    )
