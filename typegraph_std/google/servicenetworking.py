from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_servicenetworking() -> Import:
    servicenetworking = HTTPRuntime("https://servicenetworking.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicenetworking_1_ErrorResponse",
        "AddDnsRecordSetMetadataIn": "_servicenetworking_2_AddDnsRecordSetMetadataIn",
        "AddDnsRecordSetMetadataOut": "_servicenetworking_3_AddDnsRecordSetMetadataOut",
        "PeeredDnsDomainIn": "_servicenetworking_4_PeeredDnsDomainIn",
        "PeeredDnsDomainOut": "_servicenetworking_5_PeeredDnsDomainOut",
        "DocumentationIn": "_servicenetworking_6_DocumentationIn",
        "DocumentationOut": "_servicenetworking_7_DocumentationOut",
        "DocumentationRuleIn": "_servicenetworking_8_DocumentationRuleIn",
        "DocumentationRuleOut": "_servicenetworking_9_DocumentationRuleOut",
        "ClientLibrarySettingsIn": "_servicenetworking_10_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_servicenetworking_11_ClientLibrarySettingsOut",
        "MetricRuleIn": "_servicenetworking_12_MetricRuleIn",
        "MetricRuleOut": "_servicenetworking_13_MetricRuleOut",
        "ListPeeredDnsDomainsResponseIn": "_servicenetworking_14_ListPeeredDnsDomainsResponseIn",
        "ListPeeredDnsDomainsResponseOut": "_servicenetworking_15_ListPeeredDnsDomainsResponseOut",
        "SourceInfoIn": "_servicenetworking_16_SourceInfoIn",
        "SourceInfoOut": "_servicenetworking_17_SourceInfoOut",
        "HttpRuleIn": "_servicenetworking_18_HttpRuleIn",
        "HttpRuleOut": "_servicenetworking_19_HttpRuleOut",
        "MonitoredResourceDescriptorIn": "_servicenetworking_20_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_servicenetworking_21_MonitoredResourceDescriptorOut",
        "StatusIn": "_servicenetworking_22_StatusIn",
        "StatusOut": "_servicenetworking_23_StatusOut",
        "UpdateDnsRecordSetRequestIn": "_servicenetworking_24_UpdateDnsRecordSetRequestIn",
        "UpdateDnsRecordSetRequestOut": "_servicenetworking_25_UpdateDnsRecordSetRequestOut",
        "MonitoringIn": "_servicenetworking_26_MonitoringIn",
        "MonitoringOut": "_servicenetworking_27_MonitoringOut",
        "ContextIn": "_servicenetworking_28_ContextIn",
        "ContextOut": "_servicenetworking_29_ContextOut",
        "PolicyBindingIn": "_servicenetworking_30_PolicyBindingIn",
        "PolicyBindingOut": "_servicenetworking_31_PolicyBindingOut",
        "BillingIn": "_servicenetworking_32_BillingIn",
        "BillingOut": "_servicenetworking_33_BillingOut",
        "OptionIn": "_servicenetworking_34_OptionIn",
        "OptionOut": "_servicenetworking_35_OptionOut",
        "EnumIn": "_servicenetworking_36_EnumIn",
        "EnumOut": "_servicenetworking_37_EnumOut",
        "PublishingIn": "_servicenetworking_38_PublishingIn",
        "PublishingOut": "_servicenetworking_39_PublishingOut",
        "QuotaLimitIn": "_servicenetworking_40_QuotaLimitIn",
        "QuotaLimitOut": "_servicenetworking_41_QuotaLimitOut",
        "SearchRangeRequestIn": "_servicenetworking_42_SearchRangeRequestIn",
        "SearchRangeRequestOut": "_servicenetworking_43_SearchRangeRequestOut",
        "PythonSettingsIn": "_servicenetworking_44_PythonSettingsIn",
        "PythonSettingsOut": "_servicenetworking_45_PythonSettingsOut",
        "CustomErrorRuleIn": "_servicenetworking_46_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_servicenetworking_47_CustomErrorRuleOut",
        "AddSubnetworkRequestIn": "_servicenetworking_48_AddSubnetworkRequestIn",
        "AddSubnetworkRequestOut": "_servicenetworking_49_AddSubnetworkRequestOut",
        "SubnetworkIn": "_servicenetworking_50_SubnetworkIn",
        "SubnetworkOut": "_servicenetworking_51_SubnetworkOut",
        "ConsumerProjectIn": "_servicenetworking_52_ConsumerProjectIn",
        "ConsumerProjectOut": "_servicenetworking_53_ConsumerProjectOut",
        "CppSettingsIn": "_servicenetworking_54_CppSettingsIn",
        "CppSettingsOut": "_servicenetworking_55_CppSettingsOut",
        "SourceContextIn": "_servicenetworking_56_SourceContextIn",
        "SourceContextOut": "_servicenetworking_57_SourceContextOut",
        "NodeSettingsIn": "_servicenetworking_58_NodeSettingsIn",
        "NodeSettingsOut": "_servicenetworking_59_NodeSettingsOut",
        "AuthProviderIn": "_servicenetworking_60_AuthProviderIn",
        "AuthProviderOut": "_servicenetworking_61_AuthProviderOut",
        "SecondaryIpRangeSpecIn": "_servicenetworking_62_SecondaryIpRangeSpecIn",
        "SecondaryIpRangeSpecOut": "_servicenetworking_63_SecondaryIpRangeSpecOut",
        "ConsumerConfigIn": "_servicenetworking_64_ConsumerConfigIn",
        "ConsumerConfigOut": "_servicenetworking_65_ConsumerConfigOut",
        "RemoveDnsRecordSetRequestIn": "_servicenetworking_66_RemoveDnsRecordSetRequestIn",
        "RemoveDnsRecordSetRequestOut": "_servicenetworking_67_RemoveDnsRecordSetRequestOut",
        "JwtLocationIn": "_servicenetworking_68_JwtLocationIn",
        "JwtLocationOut": "_servicenetworking_69_JwtLocationOut",
        "AddRolesRequestIn": "_servicenetworking_70_AddRolesRequestIn",
        "AddRolesRequestOut": "_servicenetworking_71_AddRolesRequestOut",
        "DeleteConnectionRequestIn": "_servicenetworking_72_DeleteConnectionRequestIn",
        "DeleteConnectionRequestOut": "_servicenetworking_73_DeleteConnectionRequestOut",
        "MetricDescriptorMetadataIn": "_servicenetworking_74_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_servicenetworking_75_MetricDescriptorMetadataOut",
        "LoggingDestinationIn": "_servicenetworking_76_LoggingDestinationIn",
        "LoggingDestinationOut": "_servicenetworking_77_LoggingDestinationOut",
        "LongRunningIn": "_servicenetworking_78_LongRunningIn",
        "LongRunningOut": "_servicenetworking_79_LongRunningOut",
        "JavaSettingsIn": "_servicenetworking_80_JavaSettingsIn",
        "JavaSettingsOut": "_servicenetworking_81_JavaSettingsOut",
        "UpdateConsumerConfigRequestIn": "_servicenetworking_82_UpdateConsumerConfigRequestIn",
        "UpdateConsumerConfigRequestOut": "_servicenetworking_83_UpdateConsumerConfigRequestOut",
        "OAuthRequirementsIn": "_servicenetworking_84_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_servicenetworking_85_OAuthRequirementsOut",
        "OperationIn": "_servicenetworking_86_OperationIn",
        "OperationOut": "_servicenetworking_87_OperationOut",
        "AddDnsZoneMetadataIn": "_servicenetworking_88_AddDnsZoneMetadataIn",
        "AddDnsZoneMetadataOut": "_servicenetworking_89_AddDnsZoneMetadataOut",
        "DnsRecordSetIn": "_servicenetworking_90_DnsRecordSetIn",
        "DnsRecordSetOut": "_servicenetworking_91_DnsRecordSetOut",
        "ListConnectionsResponseIn": "_servicenetworking_92_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_servicenetworking_93_ListConnectionsResponseOut",
        "SystemParametersIn": "_servicenetworking_94_SystemParametersIn",
        "SystemParametersOut": "_servicenetworking_95_SystemParametersOut",
        "SystemParameterIn": "_servicenetworking_96_SystemParameterIn",
        "SystemParameterOut": "_servicenetworking_97_SystemParameterOut",
        "ServiceIn": "_servicenetworking_98_ServiceIn",
        "ServiceOut": "_servicenetworking_99_ServiceOut",
        "DotnetSettingsIn": "_servicenetworking_100_DotnetSettingsIn",
        "DotnetSettingsOut": "_servicenetworking_101_DotnetSettingsOut",
        "UsageIn": "_servicenetworking_102_UsageIn",
        "UsageOut": "_servicenetworking_103_UsageOut",
        "PartialDeleteConnectionMetadataIn": "_servicenetworking_104_PartialDeleteConnectionMetadataIn",
        "PartialDeleteConnectionMetadataOut": "_servicenetworking_105_PartialDeleteConnectionMetadataOut",
        "UpdateDnsRecordSetMetadataIn": "_servicenetworking_106_UpdateDnsRecordSetMetadataIn",
        "UpdateDnsRecordSetMetadataOut": "_servicenetworking_107_UpdateDnsRecordSetMetadataOut",
        "ValidateConsumerConfigRequestIn": "_servicenetworking_108_ValidateConsumerConfigRequestIn",
        "ValidateConsumerConfigRequestOut": "_servicenetworking_109_ValidateConsumerConfigRequestOut",
        "DisableVpcServiceControlsRequestIn": "_servicenetworking_110_DisableVpcServiceControlsRequestIn",
        "DisableVpcServiceControlsRequestOut": "_servicenetworking_111_DisableVpcServiceControlsRequestOut",
        "AuthenticationIn": "_servicenetworking_112_AuthenticationIn",
        "AuthenticationOut": "_servicenetworking_113_AuthenticationOut",
        "MonitoringDestinationIn": "_servicenetworking_114_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_servicenetworking_115_MonitoringDestinationOut",
        "RemoveDnsZoneMetadataIn": "_servicenetworking_116_RemoveDnsZoneMetadataIn",
        "RemoveDnsZoneMetadataOut": "_servicenetworking_117_RemoveDnsZoneMetadataOut",
        "RubySettingsIn": "_servicenetworking_118_RubySettingsIn",
        "RubySettingsOut": "_servicenetworking_119_RubySettingsOut",
        "GoogleCloudServicenetworkingV1betaConnectionIn": "_servicenetworking_120_GoogleCloudServicenetworkingV1betaConnectionIn",
        "GoogleCloudServicenetworkingV1betaConnectionOut": "_servicenetworking_121_GoogleCloudServicenetworkingV1betaConnectionOut",
        "AddDnsRecordSetRequestIn": "_servicenetworking_122_AddDnsRecordSetRequestIn",
        "AddDnsRecordSetRequestOut": "_servicenetworking_123_AddDnsRecordSetRequestOut",
        "EmptyIn": "_servicenetworking_124_EmptyIn",
        "EmptyOut": "_servicenetworking_125_EmptyOut",
        "CommonLanguageSettingsIn": "_servicenetworking_126_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_servicenetworking_127_CommonLanguageSettingsOut",
        "ApiIn": "_servicenetworking_128_ApiIn",
        "ApiOut": "_servicenetworking_129_ApiOut",
        "LoggingIn": "_servicenetworking_130_LoggingIn",
        "LoggingOut": "_servicenetworking_131_LoggingOut",
        "PhpSettingsIn": "_servicenetworking_132_PhpSettingsIn",
        "PhpSettingsOut": "_servicenetworking_133_PhpSettingsOut",
        "RouteIn": "_servicenetworking_134_RouteIn",
        "RouteOut": "_servicenetworking_135_RouteOut",
        "LabelDescriptorIn": "_servicenetworking_136_LabelDescriptorIn",
        "LabelDescriptorOut": "_servicenetworking_137_LabelDescriptorOut",
        "AddRolesMetadataIn": "_servicenetworking_138_AddRolesMetadataIn",
        "AddRolesMetadataOut": "_servicenetworking_139_AddRolesMetadataOut",
        "DnsZoneIn": "_servicenetworking_140_DnsZoneIn",
        "DnsZoneOut": "_servicenetworking_141_DnsZoneOut",
        "MethodSettingsIn": "_servicenetworking_142_MethodSettingsIn",
        "MethodSettingsOut": "_servicenetworking_143_MethodSettingsOut",
        "DeleteConnectionMetadataIn": "_servicenetworking_144_DeleteConnectionMetadataIn",
        "DeleteConnectionMetadataOut": "_servicenetworking_145_DeleteConnectionMetadataOut",
        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn": "_servicenetworking_146_GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn",
        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut": "_servicenetworking_147_GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut",
        "BackendIn": "_servicenetworking_148_BackendIn",
        "BackendOut": "_servicenetworking_149_BackendOut",
        "GoSettingsIn": "_servicenetworking_150_GoSettingsIn",
        "GoSettingsOut": "_servicenetworking_151_GoSettingsOut",
        "RemoveDnsRecordSetMetadataIn": "_servicenetworking_152_RemoveDnsRecordSetMetadataIn",
        "RemoveDnsRecordSetMetadataOut": "_servicenetworking_153_RemoveDnsRecordSetMetadataOut",
        "AddDnsZoneResponseIn": "_servicenetworking_154_AddDnsZoneResponseIn",
        "AddDnsZoneResponseOut": "_servicenetworking_155_AddDnsZoneResponseOut",
        "EnableVpcServiceControlsRequestIn": "_servicenetworking_156_EnableVpcServiceControlsRequestIn",
        "EnableVpcServiceControlsRequestOut": "_servicenetworking_157_EnableVpcServiceControlsRequestOut",
        "CustomErrorIn": "_servicenetworking_158_CustomErrorIn",
        "CustomErrorOut": "_servicenetworking_159_CustomErrorOut",
        "TypeIn": "_servicenetworking_160_TypeIn",
        "TypeOut": "_servicenetworking_161_TypeOut",
        "RemoveDnsRecordSetResponseIn": "_servicenetworking_162_RemoveDnsRecordSetResponseIn",
        "RemoveDnsRecordSetResponseOut": "_servicenetworking_163_RemoveDnsRecordSetResponseOut",
        "MethodIn": "_servicenetworking_164_MethodIn",
        "MethodOut": "_servicenetworking_165_MethodOut",
        "FieldIn": "_servicenetworking_166_FieldIn",
        "FieldOut": "_servicenetworking_167_FieldOut",
        "EnumValueIn": "_servicenetworking_168_EnumValueIn",
        "EnumValueOut": "_servicenetworking_169_EnumValueOut",
        "PeeredDnsDomainMetadataIn": "_servicenetworking_170_PeeredDnsDomainMetadataIn",
        "PeeredDnsDomainMetadataOut": "_servicenetworking_171_PeeredDnsDomainMetadataOut",
        "SystemParameterRuleIn": "_servicenetworking_172_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_servicenetworking_173_SystemParameterRuleOut",
        "AddRolesResponseIn": "_servicenetworking_174_AddRolesResponseIn",
        "AddRolesResponseOut": "_servicenetworking_175_AddRolesResponseOut",
        "RangeReservationIn": "_servicenetworking_176_RangeReservationIn",
        "RangeReservationOut": "_servicenetworking_177_RangeReservationOut",
        "CustomHttpPatternIn": "_servicenetworking_178_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_servicenetworking_179_CustomHttpPatternOut",
        "UsageRuleIn": "_servicenetworking_180_UsageRuleIn",
        "UsageRuleOut": "_servicenetworking_181_UsageRuleOut",
        "CancelOperationRequestIn": "_servicenetworking_182_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_servicenetworking_183_CancelOperationRequestOut",
        "QuotaIn": "_servicenetworking_184_QuotaIn",
        "QuotaOut": "_servicenetworking_185_QuotaOut",
        "LogDescriptorIn": "_servicenetworking_186_LogDescriptorIn",
        "LogDescriptorOut": "_servicenetworking_187_LogDescriptorOut",
        "RangeIn": "_servicenetworking_188_RangeIn",
        "RangeOut": "_servicenetworking_189_RangeOut",
        "RemoveDnsZoneResponseIn": "_servicenetworking_190_RemoveDnsZoneResponseIn",
        "RemoveDnsZoneResponseOut": "_servicenetworking_191_RemoveDnsZoneResponseOut",
        "ConnectionIn": "_servicenetworking_192_ConnectionIn",
        "ConnectionOut": "_servicenetworking_193_ConnectionOut",
        "AddDnsZoneRequestIn": "_servicenetworking_194_AddDnsZoneRequestIn",
        "AddDnsZoneRequestOut": "_servicenetworking_195_AddDnsZoneRequestOut",
        "ValidateConsumerConfigResponseIn": "_servicenetworking_196_ValidateConsumerConfigResponseIn",
        "ValidateConsumerConfigResponseOut": "_servicenetworking_197_ValidateConsumerConfigResponseOut",
        "BackendRuleIn": "_servicenetworking_198_BackendRuleIn",
        "BackendRuleOut": "_servicenetworking_199_BackendRuleOut",
        "BillingDestinationIn": "_servicenetworking_200_BillingDestinationIn",
        "BillingDestinationOut": "_servicenetworking_201_BillingDestinationOut",
        "ControlIn": "_servicenetworking_202_ControlIn",
        "ControlOut": "_servicenetworking_203_ControlOut",
        "AuthenticationRuleIn": "_servicenetworking_204_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_servicenetworking_205_AuthenticationRuleOut",
        "SecondaryIpRangeIn": "_servicenetworking_206_SecondaryIpRangeIn",
        "SecondaryIpRangeOut": "_servicenetworking_207_SecondaryIpRangeOut",
        "ContextRuleIn": "_servicenetworking_208_ContextRuleIn",
        "ContextRuleOut": "_servicenetworking_209_ContextRuleOut",
        "HttpIn": "_servicenetworking_210_HttpIn",
        "HttpOut": "_servicenetworking_211_HttpOut",
        "MixinIn": "_servicenetworking_212_MixinIn",
        "MixinOut": "_servicenetworking_213_MixinOut",
        "DeletePeeredDnsDomainMetadataIn": "_servicenetworking_214_DeletePeeredDnsDomainMetadataIn",
        "DeletePeeredDnsDomainMetadataOut": "_servicenetworking_215_DeletePeeredDnsDomainMetadataOut",
        "CloudSQLConfigIn": "_servicenetworking_216_CloudSQLConfigIn",
        "CloudSQLConfigOut": "_servicenetworking_217_CloudSQLConfigOut",
        "ListOperationsResponseIn": "_servicenetworking_218_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_servicenetworking_219_ListOperationsResponseOut",
        "MetricDescriptorIn": "_servicenetworking_220_MetricDescriptorIn",
        "MetricDescriptorOut": "_servicenetworking_221_MetricDescriptorOut",
        "GoogleCloudServicenetworkingV1betaSubnetworkIn": "_servicenetworking_222_GoogleCloudServicenetworkingV1betaSubnetworkIn",
        "GoogleCloudServicenetworkingV1betaSubnetworkOut": "_servicenetworking_223_GoogleCloudServicenetworkingV1betaSubnetworkOut",
        "AuthRequirementIn": "_servicenetworking_224_AuthRequirementIn",
        "AuthRequirementOut": "_servicenetworking_225_AuthRequirementOut",
        "PageIn": "_servicenetworking_226_PageIn",
        "PageOut": "_servicenetworking_227_PageOut",
        "RemoveDnsZoneRequestIn": "_servicenetworking_228_RemoveDnsZoneRequestIn",
        "RemoveDnsZoneRequestOut": "_servicenetworking_229_RemoveDnsZoneRequestOut",
        "EndpointIn": "_servicenetworking_230_EndpointIn",
        "EndpointOut": "_servicenetworking_231_EndpointOut",
        "ConsumerConfigMetadataIn": "_servicenetworking_232_ConsumerConfigMetadataIn",
        "ConsumerConfigMetadataOut": "_servicenetworking_233_ConsumerConfigMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AddDnsRecordSetMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddDnsRecordSetMetadataIn"]
    )
    types["AddDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddDnsRecordSetMetadataOut"])
    types["PeeredDnsDomainIn"] = t.struct(
        {"name": t.string().optional(), "dnsSuffix": t.string().optional()}
    ).named(renames["PeeredDnsDomainIn"])
    types["PeeredDnsDomainOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dnsSuffix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeeredDnsDomainOut"])
    types["DocumentationIn"] = t.struct(
        {
            "summary": t.string().optional(),
            "documentationRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "overview": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "summary": t.string().optional(),
            "documentationRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "overview": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["DocumentationRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "deprecationDescription": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "restNumericEnums": t.boolean().optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "launchStage": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "version": t.string().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "restNumericEnums": t.boolean().optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "version": t.string().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
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
    types["ListPeeredDnsDomainsResponseIn"] = t.struct(
        {"peeredDnsDomains": t.array(t.proxy(renames["PeeredDnsDomainIn"])).optional()}
    ).named(renames["ListPeeredDnsDomainsResponseIn"])
    types["ListPeeredDnsDomainsResponseOut"] = t.struct(
        {
            "peeredDnsDomains": t.array(
                t.proxy(renames["PeeredDnsDomainOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListPeeredDnsDomainsResponseOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "post": t.string().optional(),
            "get": t.string().optional(),
            "body": t.string().optional(),
            "responseBody": t.string().optional(),
            "delete": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "put": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "post": t.string().optional(),
            "get": t.string().optional(),
            "body": t.string().optional(),
            "responseBody": t.string().optional(),
            "delete": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "put": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "launchStage": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "launchStage": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
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
    types["UpdateDnsRecordSetRequestIn"] = t.struct(
        {
            "zone": t.string(),
            "existingDnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "consumerNetwork": t.string(),
            "newDnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
        }
    ).named(renames["UpdateDnsRecordSetRequestIn"])
    types["UpdateDnsRecordSetRequestOut"] = t.struct(
        {
            "zone": t.string(),
            "existingDnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "consumerNetwork": t.string(),
            "newDnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDnsRecordSetRequestOut"])
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
        {"member": t.string(), "role": t.string()}
    ).named(renames["PolicyBindingIn"])
    types["PolicyBindingOut"] = t.struct(
        {
            "member": t.string(),
            "role": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyBindingOut"])
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
    types["EnumIn"] = t.struct(
        {
            "edition": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "edition": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["PublishingIn"] = t.struct(
        {
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "docTagPrefix": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "githubLabel": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "newIssueUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "documentationUri": t.string().optional(),
            "organization": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "docTagPrefix": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "githubLabel": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "newIssueUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "documentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "name": t.string().optional(),
            "maxLimit": t.string().optional(),
            "displayName": t.string().optional(),
            "duration": t.string().optional(),
            "unit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "freeTier": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "metric": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "name": t.string().optional(),
            "maxLimit": t.string().optional(),
            "displayName": t.string().optional(),
            "duration": t.string().optional(),
            "unit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "freeTier": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "metric": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["SearchRangeRequestIn"] = t.struct(
        {"ipPrefixLength": t.integer(), "network": t.string().optional()}
    ).named(renames["SearchRangeRequestIn"])
    types["SearchRangeRequestOut"] = t.struct(
        {
            "ipPrefixLength": t.integer(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchRangeRequestOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
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
    types["AddSubnetworkRequestIn"] = t.struct(
        {
            "description": t.string().optional(),
            "ipPrefixLength": t.integer(),
            "consumer": t.string(),
            "secondaryIpRangeSpecs": t.array(
                t.proxy(renames["SecondaryIpRangeSpecIn"])
            ).optional(),
            "subnetworkUsers": t.array(t.string()).optional(),
            "region": t.string(),
            "purpose": t.string().optional(),
            "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "computeIdempotencyWindow": t.string().optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "subnetwork": t.string(),
            "consumerNetwork": t.string(),
            "useCustomComputeIdempotencyWindow": t.boolean().optional(),
            "role": t.string().optional(),
            "requestedAddress": t.string().optional(),
        }
    ).named(renames["AddSubnetworkRequestIn"])
    types["AddSubnetworkRequestOut"] = t.struct(
        {
            "description": t.string().optional(),
            "ipPrefixLength": t.integer(),
            "consumer": t.string(),
            "secondaryIpRangeSpecs": t.array(
                t.proxy(renames["SecondaryIpRangeSpecOut"])
            ).optional(),
            "subnetworkUsers": t.array(t.string()).optional(),
            "region": t.string(),
            "purpose": t.string().optional(),
            "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "computeIdempotencyWindow": t.string().optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "subnetwork": t.string(),
            "consumerNetwork": t.string(),
            "useCustomComputeIdempotencyWindow": t.boolean().optional(),
            "role": t.string().optional(),
            "requestedAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSubnetworkRequestOut"])
    types["SubnetworkIn"] = t.struct(
        {
            "secondaryIpRanges": t.array(
                t.proxy(renames["SecondaryIpRangeIn"])
            ).optional(),
            "name": t.string().optional(),
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "region": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
        }
    ).named(renames["SubnetworkIn"])
    types["SubnetworkOut"] = t.struct(
        {
            "secondaryIpRanges": t.array(
                t.proxy(renames["SecondaryIpRangeOut"])
            ).optional(),
            "name": t.string().optional(),
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "region": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubnetworkOut"])
    types["ConsumerProjectIn"] = t.struct({"projectNum": t.string()}).named(
        renames["ConsumerProjectIn"]
    )
    types["ConsumerProjectOut"] = t.struct(
        {
            "projectNum": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerProjectOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "audiences": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwksUri": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "audiences": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwksUri": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["SecondaryIpRangeSpecIn"] = t.struct(
        {
            "rangeName": t.string(),
            "requestedAddress": t.string().optional(),
            "ipPrefixLength": t.integer(),
            "outsideAllocationPublicIpRange": t.string().optional(),
        }
    ).named(renames["SecondaryIpRangeSpecIn"])
    types["SecondaryIpRangeSpecOut"] = t.struct(
        {
            "rangeName": t.string(),
            "requestedAddress": t.string().optional(),
            "ipPrefixLength": t.integer(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecondaryIpRangeSpecOut"])
    types["ConsumerConfigIn"] = t.struct(
        {
            "consumerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerImportCustomRoutes": t.boolean().optional(),
            "producerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportCustomRoutes": t.boolean().optional(),
            "consumerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "consumerImportCustomRoutes": t.boolean().optional(),
            "cloudsqlConfigs": t.array(t.proxy(renames["CloudSQLConfigIn"])).optional(),
            "consumerExportCustomRoutes": t.boolean().optional(),
        }
    ).named(renames["ConsumerConfigIn"])
    types["ConsumerConfigOut"] = t.struct(
        {
            "consumerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerImportCustomRoutes": t.boolean().optional(),
            "reservedRanges": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"
                    ]
                )
            ).optional(),
            "producerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportCustomRoutes": t.boolean().optional(),
            "consumerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "vpcScReferenceArchitectureEnabled": t.boolean().optional(),
            "consumerImportCustomRoutes": t.boolean().optional(),
            "usedIpRanges": t.array(t.string()).optional(),
            "cloudsqlConfigs": t.array(
                t.proxy(renames["CloudSQLConfigOut"])
            ).optional(),
            "producerNetwork": t.string().optional(),
            "consumerExportCustomRoutes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerConfigOut"])
    types["RemoveDnsRecordSetRequestIn"] = t.struct(
        {
            "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "zone": t.string(),
            "consumerNetwork": t.string(),
        }
    ).named(renames["RemoveDnsRecordSetRequestIn"])
    types["RemoveDnsRecordSetRequestOut"] = t.struct(
        {
            "dnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "zone": t.string(),
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveDnsRecordSetRequestOut"])
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
    types["AddRolesRequestIn"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "policyBinding": t.array(t.proxy(renames["PolicyBindingIn"])),
        }
    ).named(renames["AddRolesRequestIn"])
    types["AddRolesRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "policyBinding": t.array(t.proxy(renames["PolicyBindingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddRolesRequestOut"])
    types["DeleteConnectionRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["DeleteConnectionRequestIn"])
    types["DeleteConnectionRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConnectionRequestOut"])
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
    types["LongRunningIn"] = t.struct(
        {
            "pollDelayMultiplier": t.number().optional(),
            "maxPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
            "initialPollDelay": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "pollDelayMultiplier": t.number().optional(),
            "maxPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
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
    types["UpdateConsumerConfigRequestIn"] = t.struct(
        {"consumerConfig": t.proxy(renames["ConsumerConfigIn"])}
    ).named(renames["UpdateConsumerConfigRequestIn"])
    types["UpdateConsumerConfigRequestOut"] = t.struct(
        {
            "consumerConfig": t.proxy(renames["ConsumerConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConsumerConfigRequestOut"])
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
    types["AddDnsZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddDnsZoneMetadataIn"]
    )
    types["AddDnsZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddDnsZoneMetadataOut"])
    types["DnsRecordSetIn"] = t.struct(
        {
            "domain": t.string(),
            "data": t.array(t.string()),
            "type": t.string(),
            "ttl": t.string(),
        }
    ).named(renames["DnsRecordSetIn"])
    types["DnsRecordSetOut"] = t.struct(
        {
            "domain": t.string(),
            "data": t.array(t.string()),
            "type": t.string(),
            "ttl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsRecordSetOut"])
    types["ListConnectionsResponseIn"] = t.struct(
        {"connections": t.array(t.proxy(renames["ConnectionIn"])).optional()}
    ).named(renames["ListConnectionsResponseIn"])
    types["ListConnectionsResponseOut"] = t.struct(
        {
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionsResponseOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
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
    types["ServiceIn"] = t.struct(
        {
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "title": t.string().optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "name": t.string().optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "configVersion": t.integer().optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "producerProjectId": t.string().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "title": t.string().optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "name": t.string().optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "configVersion": t.integer().optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "producerProjectId": t.string().optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
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
    types["PartialDeleteConnectionMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PartialDeleteConnectionMetadataIn"])
    types["PartialDeleteConnectionMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PartialDeleteConnectionMetadataOut"])
    types["UpdateDnsRecordSetMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateDnsRecordSetMetadataIn"])
    types["UpdateDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateDnsRecordSetMetadataOut"])
    types["ValidateConsumerConfigRequestIn"] = t.struct(
        {
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerNetwork": t.string(),
            "rangeReservation": t.proxy(renames["RangeReservationIn"]).optional(),
            "validateNetwork": t.boolean().optional(),
            "consumerProject": t.proxy(renames["ConsumerProjectIn"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigRequestIn"])
    types["ValidateConsumerConfigRequestOut"] = t.struct(
        {
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerNetwork": t.string(),
            "rangeReservation": t.proxy(renames["RangeReservationOut"]).optional(),
            "validateNetwork": t.boolean().optional(),
            "consumerProject": t.proxy(renames["ConsumerProjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigRequestOut"])
    types["DisableVpcServiceControlsRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["DisableVpcServiceControlsRequestIn"])
    types["DisableVpcServiceControlsRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableVpcServiceControlsRequestOut"])
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
    types["RemoveDnsZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveDnsZoneMetadataIn"]
    )
    types["RemoveDnsZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsZoneMetadataOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["GoogleCloudServicenetworkingV1betaConnectionIn"] = t.struct(
        {
            "service": t.string().optional(),
            "network": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "peering": t.string().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaConnectionIn"])
    types["GoogleCloudServicenetworkingV1betaConnectionOut"] = t.struct(
        {
            "service": t.string().optional(),
            "network": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "peering": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaConnectionOut"])
    types["AddDnsRecordSetRequestIn"] = t.struct(
        {
            "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "zone": t.string(),
            "consumerNetwork": t.string(),
        }
    ).named(renames["AddDnsRecordSetRequestIn"])
    types["AddDnsRecordSetRequestOut"] = t.struct(
        {
            "dnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "zone": t.string(),
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDnsRecordSetRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ApiIn"] = t.struct(
        {
            "name": t.string().optional(),
            "version": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "name": t.string().optional(),
            "version": t.string().optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
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
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
    types["RouteIn"] = t.struct(
        {
            "network": t.string().optional(),
            "destRange": t.string().optional(),
            "name": t.string().optional(),
            "nextHopGateway": t.string().optional(),
        }
    ).named(renames["RouteIn"])
    types["RouteOut"] = t.struct(
        {
            "network": t.string().optional(),
            "destRange": t.string().optional(),
            "name": t.string().optional(),
            "nextHopGateway": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteOut"])
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
    types["AddRolesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddRolesMetadataIn"]
    )
    types["AddRolesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddRolesMetadataOut"])
    types["DnsZoneIn"] = t.struct(
        {"dnsSuffix": t.string().optional(), "name": t.string().optional()}
    ).named(renames["DnsZoneIn"])
    types["DnsZoneOut"] = t.struct(
        {
            "dnsSuffix": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsZoneOut"])
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
    types["DeleteConnectionMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteConnectionMetadataIn"]
    )
    types["DeleteConnectionMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteConnectionMetadataOut"])
    types["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn"] = t.struct(
        {
            "address": t.string().optional(),
            "name": t.string().optional(),
            "ipPrefixLength": t.integer().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn"])
    types["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"] = t.struct(
        {
            "address": t.string().optional(),
            "name": t.string().optional(),
            "ipPrefixLength": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"])
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
    types["RemoveDnsRecordSetMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RemoveDnsRecordSetMetadataIn"])
    types["RemoveDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsRecordSetMetadataOut"])
    types["AddDnsZoneResponseIn"] = t.struct(
        {
            "consumerPeeringZone": t.proxy(renames["DnsZoneIn"]).optional(),
            "producerPrivateZone": t.proxy(renames["DnsZoneIn"]).optional(),
        }
    ).named(renames["AddDnsZoneResponseIn"])
    types["AddDnsZoneResponseOut"] = t.struct(
        {
            "consumerPeeringZone": t.proxy(renames["DnsZoneOut"]).optional(),
            "producerPrivateZone": t.proxy(renames["DnsZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDnsZoneResponseOut"])
    types["EnableVpcServiceControlsRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["EnableVpcServiceControlsRequestIn"])
    types["EnableVpcServiceControlsRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableVpcServiceControlsRequestOut"])
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
    types["TypeIn"] = t.struct(
        {
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "syntax": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["RemoveDnsRecordSetResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RemoveDnsRecordSetResponseIn"])
    types["RemoveDnsRecordSetResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsRecordSetResponseOut"])
    types["MethodIn"] = t.struct(
        {
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "requestTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "requestTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["FieldIn"] = t.struct(
        {
            "jsonName": t.string().optional(),
            "number": t.integer().optional(),
            "kind": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "jsonName": t.string().optional(),
            "number": t.integer().optional(),
            "kind": t.string().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "typeUrl": t.string().optional(),
            "packed": t.boolean().optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
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
    types["PeeredDnsDomainMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PeeredDnsDomainMetadataIn"]
    )
    types["PeeredDnsDomainMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PeeredDnsDomainMetadataOut"])
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
    types["AddRolesResponseIn"] = t.struct(
        {"policyBinding": t.array(t.proxy(renames["PolicyBindingIn"]))}
    ).named(renames["AddRolesResponseIn"])
    types["AddRolesResponseOut"] = t.struct(
        {
            "policyBinding": t.array(t.proxy(renames["PolicyBindingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddRolesResponseOut"])
    types["RangeReservationIn"] = t.struct(
        {
            "requestedRanges": t.array(t.string()).optional(),
            "ipPrefixLength": t.integer(),
            "subnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkIn"])
            ).optional(),
            "secondaryRangeIpPrefixLengths": t.array(t.integer()).optional(),
        }
    ).named(renames["RangeReservationIn"])
    types["RangeReservationOut"] = t.struct(
        {
            "requestedRanges": t.array(t.string()).optional(),
            "ipPrefixLength": t.integer(),
            "subnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkOut"])
            ).optional(),
            "secondaryRangeIpPrefixLengths": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeReservationOut"])
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
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["RangeIn"] = t.struct(
        {"ipCidrRange": t.string().optional(), "network": t.string().optional()}
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "ipCidrRange": t.string().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])
    types["RemoveDnsZoneResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveDnsZoneResponseIn"]
    )
    types["RemoveDnsZoneResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsZoneResponseOut"])
    types["ConnectionIn"] = t.struct(
        {
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "network": t.string().optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "service": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "network": t.string().optional(),
            "peering": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["AddDnsZoneRequestIn"] = t.struct(
        {"consumerNetwork": t.string(), "name": t.string(), "dnsSuffix": t.string()}
    ).named(renames["AddDnsZoneRequestIn"])
    types["AddDnsZoneRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "name": t.string(),
            "dnsSuffix": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDnsZoneRequestOut"])
    types["ValidateConsumerConfigResponseIn"] = t.struct(
        {
            "validationError": t.string().optional(),
            "existingSubnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkIn"])
            ).optional(),
            "isValid": t.boolean().optional(),
        }
    ).named(renames["ValidateConsumerConfigResponseIn"])
    types["ValidateConsumerConfigResponseOut"] = t.struct(
        {
            "validationError": t.string().optional(),
            "existingSubnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkOut"])
            ).optional(),
            "isValid": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigResponseOut"])
    types["BackendRuleIn"] = t.struct(
        {
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "minDeadline": t.number().optional(),
            "deadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "protocol": t.string().optional(),
            "selector": t.string().optional(),
            "address": t.string().optional(),
            "disableAuth": t.boolean().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "minDeadline": t.number().optional(),
            "deadline": t.number().optional(),
            "operationDeadline": t.number().optional(),
            "protocol": t.string().optional(),
            "selector": t.string().optional(),
            "address": t.string().optional(),
            "disableAuth": t.boolean().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
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
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["AuthenticationRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
            "allowWithoutCredential": t.boolean().optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
    types["SecondaryIpRangeIn"] = t.struct(
        {"rangeName": t.string().optional(), "ipCidrRange": t.string().optional()}
    ).named(renames["SecondaryIpRangeIn"])
    types["SecondaryIpRangeOut"] = t.struct(
        {
            "rangeName": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecondaryIpRangeOut"])
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
    types["DeletePeeredDnsDomainMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeletePeeredDnsDomainMetadataIn"])
    types["DeletePeeredDnsDomainMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeletePeeredDnsDomainMetadataOut"])
    types["CloudSQLConfigIn"] = t.struct(
        {
            "umbrellaProject": t.string().optional(),
            "service": t.string().optional(),
            "umbrellaNetwork": t.string().optional(),
        }
    ).named(renames["CloudSQLConfigIn"])
    types["CloudSQLConfigOut"] = t.struct(
        {
            "umbrellaProject": t.string().optional(),
            "service": t.string().optional(),
            "umbrellaNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSQLConfigOut"])
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
    types["MetricDescriptorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "launchStage": t.string().optional(),
            "valueType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "description": t.string().optional(),
            "unit": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metricKind": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "launchStage": t.string().optional(),
            "valueType": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "unit": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metricKind": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["GoogleCloudServicenetworkingV1betaSubnetworkIn"] = t.struct(
        {
            "name": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaSubnetworkIn"])
    types["GoogleCloudServicenetworkingV1betaSubnetworkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaSubnetworkOut"])
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
    types["RemoveDnsZoneRequestIn"] = t.struct(
        {"name": t.string(), "consumerNetwork": t.string()}
    ).named(renames["RemoveDnsZoneRequestIn"])
    types["RemoveDnsZoneRequestOut"] = t.struct(
        {
            "name": t.string(),
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveDnsZoneRequestOut"])
    types["EndpointIn"] = t.struct(
        {
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "name": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["ConsumerConfigMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ConsumerConfigMetadataIn"]
    )
    types["ConsumerConfigMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ConsumerConfigMetadataOut"])

    functions = {}
    functions["operationsDelete"] = servicenetworking.get(
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
    functions["operationsGet"] = servicenetworking.get(
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
    functions["operationsCancel"] = servicenetworking.get(
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
    functions["operationsList"] = servicenetworking.get(
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
    functions["servicesValidate"] = servicenetworking.post(
        "v1/{parent}:searchRange",
        t.struct(
            {
                "parent": t.string(),
                "ipPrefixLength": t.integer(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesEnableVpcServiceControls"] = servicenetworking.post(
        "v1/{parent}:searchRange",
        t.struct(
            {
                "parent": t.string(),
                "ipPrefixLength": t.integer(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesAddSubnetwork"] = servicenetworking.post(
        "v1/{parent}:searchRange",
        t.struct(
            {
                "parent": t.string(),
                "ipPrefixLength": t.integer(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDisableVpcServiceControls"] = servicenetworking.post(
        "v1/{parent}:searchRange",
        t.struct(
            {
                "parent": t.string(),
                "ipPrefixLength": t.integer(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesSearchRange"] = servicenetworking.post(
        "v1/{parent}:searchRange",
        t.struct(
            {
                "parent": t.string(),
                "ipPrefixLength": t.integer(),
                "network": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesProjectsGlobalNetworksGet"] = servicenetworking.patch(
        "v1/{parent}:updateConsumerConfig",
        t.struct(
            {
                "parent": t.string(),
                "consumerConfig": t.proxy(renames["ConsumerConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksUpdateConsumerConfig"
    ] = servicenetworking.patch(
        "v1/{parent}:updateConsumerConfig",
        t.struct(
            {
                "parent": t.string(),
                "consumerConfig": t.proxy(renames["ConsumerConfigIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksPeeredDnsDomainsCreate"
    ] = servicenetworking.get(
        "v1/{parent}/peeredDnsDomains",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListPeeredDnsDomainsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksPeeredDnsDomainsDelete"
    ] = servicenetworking.get(
        "v1/{parent}/peeredDnsDomains",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListPeeredDnsDomainsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksPeeredDnsDomainsList"
    ] = servicenetworking.get(
        "v1/{parent}/peeredDnsDomains",
        t.struct({"parent": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ListPeeredDnsDomainsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsZonesRemove"] = servicenetworking.post(
        "v1/{parent}/dnsZones:add",
        t.struct(
            {
                "parent": t.string(),
                "consumerNetwork": t.string(),
                "name": t.string(),
                "dnsSuffix": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsZonesAdd"] = servicenetworking.post(
        "v1/{parent}/dnsZones:add",
        t.struct(
            {
                "parent": t.string(),
                "consumerNetwork": t.string(),
                "name": t.string(),
                "dnsSuffix": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesRolesAdd"] = servicenetworking.post(
        "v1/{parent}/roles:add",
        t.struct(
            {
                "parent": t.string(),
                "consumerNetwork": t.string(),
                "policyBinding": t.array(t.proxy(renames["PolicyBindingIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsRecordSetsUpdate"] = servicenetworking.post(
        "v1/{parent}/dnsRecordSets:remove",
        t.struct(
            {
                "parent": t.string(),
                "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
                "zone": t.string(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsRecordSetsAdd"] = servicenetworking.post(
        "v1/{parent}/dnsRecordSets:remove",
        t.struct(
            {
                "parent": t.string(),
                "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
                "zone": t.string(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsRecordSetsRemove"] = servicenetworking.post(
        "v1/{parent}/dnsRecordSets:remove",
        t.struct(
            {
                "parent": t.string(),
                "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
                "zone": t.string(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConnectionsList"] = servicenetworking.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConnectionsPatch"] = servicenetworking.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConnectionsCreate"] = servicenetworking.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConnectionsDeleteConnection"] = servicenetworking.post(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="servicenetworking",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
