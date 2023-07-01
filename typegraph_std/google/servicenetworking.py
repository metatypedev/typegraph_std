from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_servicenetworking():
    servicenetworking = HTTPRuntime("https://servicenetworking.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicenetworking_1_ErrorResponse",
        "ListConnectionsResponseIn": "_servicenetworking_2_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_servicenetworking_3_ListConnectionsResponseOut",
        "AuthenticationIn": "_servicenetworking_4_AuthenticationIn",
        "AuthenticationOut": "_servicenetworking_5_AuthenticationOut",
        "AddDnsZoneRequestIn": "_servicenetworking_6_AddDnsZoneRequestIn",
        "AddDnsZoneRequestOut": "_servicenetworking_7_AddDnsZoneRequestOut",
        "BackendRuleIn": "_servicenetworking_8_BackendRuleIn",
        "BackendRuleOut": "_servicenetworking_9_BackendRuleOut",
        "UpdateConsumerConfigRequestIn": "_servicenetworking_10_UpdateConsumerConfigRequestIn",
        "UpdateConsumerConfigRequestOut": "_servicenetworking_11_UpdateConsumerConfigRequestOut",
        "CancelOperationRequestIn": "_servicenetworking_12_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_servicenetworking_13_CancelOperationRequestOut",
        "SubnetworkIn": "_servicenetworking_14_SubnetworkIn",
        "SubnetworkOut": "_servicenetworking_15_SubnetworkOut",
        "MethodIn": "_servicenetworking_16_MethodIn",
        "MethodOut": "_servicenetworking_17_MethodOut",
        "ConsumerProjectIn": "_servicenetworking_18_ConsumerProjectIn",
        "ConsumerProjectOut": "_servicenetworking_19_ConsumerProjectOut",
        "PartialDeleteConnectionMetadataIn": "_servicenetworking_20_PartialDeleteConnectionMetadataIn",
        "PartialDeleteConnectionMetadataOut": "_servicenetworking_21_PartialDeleteConnectionMetadataOut",
        "MetricDescriptorIn": "_servicenetworking_22_MetricDescriptorIn",
        "MetricDescriptorOut": "_servicenetworking_23_MetricDescriptorOut",
        "CommonLanguageSettingsIn": "_servicenetworking_24_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_servicenetworking_25_CommonLanguageSettingsOut",
        "EmptyIn": "_servicenetworking_26_EmptyIn",
        "EmptyOut": "_servicenetworking_27_EmptyOut",
        "AddSubnetworkRequestIn": "_servicenetworking_28_AddSubnetworkRequestIn",
        "AddSubnetworkRequestOut": "_servicenetworking_29_AddSubnetworkRequestOut",
        "PythonSettingsIn": "_servicenetworking_30_PythonSettingsIn",
        "PythonSettingsOut": "_servicenetworking_31_PythonSettingsOut",
        "PeeredDnsDomainMetadataIn": "_servicenetworking_32_PeeredDnsDomainMetadataIn",
        "PeeredDnsDomainMetadataOut": "_servicenetworking_33_PeeredDnsDomainMetadataOut",
        "DeleteConnectionMetadataIn": "_servicenetworking_34_DeleteConnectionMetadataIn",
        "DeleteConnectionMetadataOut": "_servicenetworking_35_DeleteConnectionMetadataOut",
        "ContextRuleIn": "_servicenetworking_36_ContextRuleIn",
        "ContextRuleOut": "_servicenetworking_37_ContextRuleOut",
        "ConsumerConfigMetadataIn": "_servicenetworking_38_ConsumerConfigMetadataIn",
        "ConsumerConfigMetadataOut": "_servicenetworking_39_ConsumerConfigMetadataOut",
        "ClientLibrarySettingsIn": "_servicenetworking_40_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_servicenetworking_41_ClientLibrarySettingsOut",
        "OAuthRequirementsIn": "_servicenetworking_42_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_servicenetworking_43_OAuthRequirementsOut",
        "EnumValueIn": "_servicenetworking_44_EnumValueIn",
        "EnumValueOut": "_servicenetworking_45_EnumValueOut",
        "SearchRangeRequestIn": "_servicenetworking_46_SearchRangeRequestIn",
        "SearchRangeRequestOut": "_servicenetworking_47_SearchRangeRequestOut",
        "SourceInfoIn": "_servicenetworking_48_SourceInfoIn",
        "SourceInfoOut": "_servicenetworking_49_SourceInfoOut",
        "RemoveDnsRecordSetRequestIn": "_servicenetworking_50_RemoveDnsRecordSetRequestIn",
        "RemoveDnsRecordSetRequestOut": "_servicenetworking_51_RemoveDnsRecordSetRequestOut",
        "ControlIn": "_servicenetworking_52_ControlIn",
        "ControlOut": "_servicenetworking_53_ControlOut",
        "PolicyBindingIn": "_servicenetworking_54_PolicyBindingIn",
        "PolicyBindingOut": "_servicenetworking_55_PolicyBindingOut",
        "ListOperationsResponseIn": "_servicenetworking_56_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_servicenetworking_57_ListOperationsResponseOut",
        "AuthRequirementIn": "_servicenetworking_58_AuthRequirementIn",
        "AuthRequirementOut": "_servicenetworking_59_AuthRequirementOut",
        "LabelDescriptorIn": "_servicenetworking_60_LabelDescriptorIn",
        "LabelDescriptorOut": "_servicenetworking_61_LabelDescriptorOut",
        "CustomErrorRuleIn": "_servicenetworking_62_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_servicenetworking_63_CustomErrorRuleOut",
        "SourceContextIn": "_servicenetworking_64_SourceContextIn",
        "SourceContextOut": "_servicenetworking_65_SourceContextOut",
        "CustomErrorIn": "_servicenetworking_66_CustomErrorIn",
        "CustomErrorOut": "_servicenetworking_67_CustomErrorOut",
        "AddDnsZoneResponseIn": "_servicenetworking_68_AddDnsZoneResponseIn",
        "AddDnsZoneResponseOut": "_servicenetworking_69_AddDnsZoneResponseOut",
        "ConsumerConfigIn": "_servicenetworking_70_ConsumerConfigIn",
        "ConsumerConfigOut": "_servicenetworking_71_ConsumerConfigOut",
        "SecondaryIpRangeSpecIn": "_servicenetworking_72_SecondaryIpRangeSpecIn",
        "SecondaryIpRangeSpecOut": "_servicenetworking_73_SecondaryIpRangeSpecOut",
        "CppSettingsIn": "_servicenetworking_74_CppSettingsIn",
        "CppSettingsOut": "_servicenetworking_75_CppSettingsOut",
        "AuthProviderIn": "_servicenetworking_76_AuthProviderIn",
        "AuthProviderOut": "_servicenetworking_77_AuthProviderOut",
        "DnsZoneIn": "_servicenetworking_78_DnsZoneIn",
        "DnsZoneOut": "_servicenetworking_79_DnsZoneOut",
        "AddRolesResponseIn": "_servicenetworking_80_AddRolesResponseIn",
        "AddRolesResponseOut": "_servicenetworking_81_AddRolesResponseOut",
        "UsageRuleIn": "_servicenetworking_82_UsageRuleIn",
        "UsageRuleOut": "_servicenetworking_83_UsageRuleOut",
        "LongRunningIn": "_servicenetworking_84_LongRunningIn",
        "LongRunningOut": "_servicenetworking_85_LongRunningOut",
        "AddRolesRequestIn": "_servicenetworking_86_AddRolesRequestIn",
        "AddRolesRequestOut": "_servicenetworking_87_AddRolesRequestOut",
        "OperationIn": "_servicenetworking_88_OperationIn",
        "OperationOut": "_servicenetworking_89_OperationOut",
        "MetricRuleIn": "_servicenetworking_90_MetricRuleIn",
        "MetricRuleOut": "_servicenetworking_91_MetricRuleOut",
        "AddDnsRecordSetRequestIn": "_servicenetworking_92_AddDnsRecordSetRequestIn",
        "AddDnsRecordSetRequestOut": "_servicenetworking_93_AddDnsRecordSetRequestOut",
        "PublishingIn": "_servicenetworking_94_PublishingIn",
        "PublishingOut": "_servicenetworking_95_PublishingOut",
        "RemoveDnsRecordSetResponseIn": "_servicenetworking_96_RemoveDnsRecordSetResponseIn",
        "RemoveDnsRecordSetResponseOut": "_servicenetworking_97_RemoveDnsRecordSetResponseOut",
        "DocumentationRuleIn": "_servicenetworking_98_DocumentationRuleIn",
        "DocumentationRuleOut": "_servicenetworking_99_DocumentationRuleOut",
        "RouteIn": "_servicenetworking_100_RouteIn",
        "RouteOut": "_servicenetworking_101_RouteOut",
        "ContextIn": "_servicenetworking_102_ContextIn",
        "ContextOut": "_servicenetworking_103_ContextOut",
        "QuotaLimitIn": "_servicenetworking_104_QuotaLimitIn",
        "QuotaLimitOut": "_servicenetworking_105_QuotaLimitOut",
        "JavaSettingsIn": "_servicenetworking_106_JavaSettingsIn",
        "JavaSettingsOut": "_servicenetworking_107_JavaSettingsOut",
        "JwtLocationIn": "_servicenetworking_108_JwtLocationIn",
        "JwtLocationOut": "_servicenetworking_109_JwtLocationOut",
        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn": "_servicenetworking_110_GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn",
        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut": "_servicenetworking_111_GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut",
        "MetricDescriptorMetadataIn": "_servicenetworking_112_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_servicenetworking_113_MetricDescriptorMetadataOut",
        "RangeIn": "_servicenetworking_114_RangeIn",
        "RangeOut": "_servicenetworking_115_RangeOut",
        "NodeSettingsIn": "_servicenetworking_116_NodeSettingsIn",
        "NodeSettingsOut": "_servicenetworking_117_NodeSettingsOut",
        "CustomHttpPatternIn": "_servicenetworking_118_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_servicenetworking_119_CustomHttpPatternOut",
        "EnumIn": "_servicenetworking_120_EnumIn",
        "EnumOut": "_servicenetworking_121_EnumOut",
        "GoogleCloudServicenetworkingV1betaSubnetworkIn": "_servicenetworking_122_GoogleCloudServicenetworkingV1betaSubnetworkIn",
        "GoogleCloudServicenetworkingV1betaSubnetworkOut": "_servicenetworking_123_GoogleCloudServicenetworkingV1betaSubnetworkOut",
        "SystemParameterIn": "_servicenetworking_124_SystemParameterIn",
        "SystemParameterOut": "_servicenetworking_125_SystemParameterOut",
        "RemoveDnsRecordSetMetadataIn": "_servicenetworking_126_RemoveDnsRecordSetMetadataIn",
        "RemoveDnsRecordSetMetadataOut": "_servicenetworking_127_RemoveDnsRecordSetMetadataOut",
        "AddDnsRecordSetMetadataIn": "_servicenetworking_128_AddDnsRecordSetMetadataIn",
        "AddDnsRecordSetMetadataOut": "_servicenetworking_129_AddDnsRecordSetMetadataOut",
        "RemoveDnsZoneResponseIn": "_servicenetworking_130_RemoveDnsZoneResponseIn",
        "RemoveDnsZoneResponseOut": "_servicenetworking_131_RemoveDnsZoneResponseOut",
        "LoggingIn": "_servicenetworking_132_LoggingIn",
        "LoggingOut": "_servicenetworking_133_LoggingOut",
        "PageIn": "_servicenetworking_134_PageIn",
        "PageOut": "_servicenetworking_135_PageOut",
        "MonitoredResourceDescriptorIn": "_servicenetworking_136_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_servicenetworking_137_MonitoredResourceDescriptorOut",
        "EnableVpcServiceControlsRequestIn": "_servicenetworking_138_EnableVpcServiceControlsRequestIn",
        "EnableVpcServiceControlsRequestOut": "_servicenetworking_139_EnableVpcServiceControlsRequestOut",
        "BillingIn": "_servicenetworking_140_BillingIn",
        "BillingOut": "_servicenetworking_141_BillingOut",
        "LogDescriptorIn": "_servicenetworking_142_LogDescriptorIn",
        "LogDescriptorOut": "_servicenetworking_143_LogDescriptorOut",
        "TypeIn": "_servicenetworking_144_TypeIn",
        "TypeOut": "_servicenetworking_145_TypeOut",
        "ListPeeredDnsDomainsResponseIn": "_servicenetworking_146_ListPeeredDnsDomainsResponseIn",
        "ListPeeredDnsDomainsResponseOut": "_servicenetworking_147_ListPeeredDnsDomainsResponseOut",
        "CloudSQLConfigIn": "_servicenetworking_148_CloudSQLConfigIn",
        "CloudSQLConfigOut": "_servicenetworking_149_CloudSQLConfigOut",
        "LoggingDestinationIn": "_servicenetworking_150_LoggingDestinationIn",
        "LoggingDestinationOut": "_servicenetworking_151_LoggingDestinationOut",
        "DeleteConnectionRequestIn": "_servicenetworking_152_DeleteConnectionRequestIn",
        "DeleteConnectionRequestOut": "_servicenetworking_153_DeleteConnectionRequestOut",
        "DotnetSettingsIn": "_servicenetworking_154_DotnetSettingsIn",
        "DotnetSettingsOut": "_servicenetworking_155_DotnetSettingsOut",
        "OptionIn": "_servicenetworking_156_OptionIn",
        "OptionOut": "_servicenetworking_157_OptionOut",
        "EndpointIn": "_servicenetworking_158_EndpointIn",
        "EndpointOut": "_servicenetworking_159_EndpointOut",
        "UpdateDnsRecordSetMetadataIn": "_servicenetworking_160_UpdateDnsRecordSetMetadataIn",
        "UpdateDnsRecordSetMetadataOut": "_servicenetworking_161_UpdateDnsRecordSetMetadataOut",
        "ConnectionIn": "_servicenetworking_162_ConnectionIn",
        "ConnectionOut": "_servicenetworking_163_ConnectionOut",
        "ValidateConsumerConfigResponseIn": "_servicenetworking_164_ValidateConsumerConfigResponseIn",
        "ValidateConsumerConfigResponseOut": "_servicenetworking_165_ValidateConsumerConfigResponseOut",
        "AddDnsZoneMetadataIn": "_servicenetworking_166_AddDnsZoneMetadataIn",
        "AddDnsZoneMetadataOut": "_servicenetworking_167_AddDnsZoneMetadataOut",
        "FieldIn": "_servicenetworking_168_FieldIn",
        "FieldOut": "_servicenetworking_169_FieldOut",
        "DnsRecordSetIn": "_servicenetworking_170_DnsRecordSetIn",
        "DnsRecordSetOut": "_servicenetworking_171_DnsRecordSetOut",
        "UpdateDnsRecordSetRequestIn": "_servicenetworking_172_UpdateDnsRecordSetRequestIn",
        "UpdateDnsRecordSetRequestOut": "_servicenetworking_173_UpdateDnsRecordSetRequestOut",
        "UsageIn": "_servicenetworking_174_UsageIn",
        "UsageOut": "_servicenetworking_175_UsageOut",
        "SystemParameterRuleIn": "_servicenetworking_176_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_servicenetworking_177_SystemParameterRuleOut",
        "RubySettingsIn": "_servicenetworking_178_RubySettingsIn",
        "RubySettingsOut": "_servicenetworking_179_RubySettingsOut",
        "ApiIn": "_servicenetworking_180_ApiIn",
        "ApiOut": "_servicenetworking_181_ApiOut",
        "MonitoringIn": "_servicenetworking_182_MonitoringIn",
        "MonitoringOut": "_servicenetworking_183_MonitoringOut",
        "AuthenticationRuleIn": "_servicenetworking_184_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_servicenetworking_185_AuthenticationRuleOut",
        "QuotaIn": "_servicenetworking_186_QuotaIn",
        "QuotaOut": "_servicenetworking_187_QuotaOut",
        "SystemParametersIn": "_servicenetworking_188_SystemParametersIn",
        "SystemParametersOut": "_servicenetworking_189_SystemParametersOut",
        "PhpSettingsIn": "_servicenetworking_190_PhpSettingsIn",
        "PhpSettingsOut": "_servicenetworking_191_PhpSettingsOut",
        "AddRolesMetadataIn": "_servicenetworking_192_AddRolesMetadataIn",
        "AddRolesMetadataOut": "_servicenetworking_193_AddRolesMetadataOut",
        "GoogleCloudServicenetworkingV1betaConnectionIn": "_servicenetworking_194_GoogleCloudServicenetworkingV1betaConnectionIn",
        "GoogleCloudServicenetworkingV1betaConnectionOut": "_servicenetworking_195_GoogleCloudServicenetworkingV1betaConnectionOut",
        "PeeredDnsDomainIn": "_servicenetworking_196_PeeredDnsDomainIn",
        "PeeredDnsDomainOut": "_servicenetworking_197_PeeredDnsDomainOut",
        "SecondaryIpRangeIn": "_servicenetworking_198_SecondaryIpRangeIn",
        "SecondaryIpRangeOut": "_servicenetworking_199_SecondaryIpRangeOut",
        "BillingDestinationIn": "_servicenetworking_200_BillingDestinationIn",
        "BillingDestinationOut": "_servicenetworking_201_BillingDestinationOut",
        "DocumentationIn": "_servicenetworking_202_DocumentationIn",
        "DocumentationOut": "_servicenetworking_203_DocumentationOut",
        "DisableVpcServiceControlsRequestIn": "_servicenetworking_204_DisableVpcServiceControlsRequestIn",
        "DisableVpcServiceControlsRequestOut": "_servicenetworking_205_DisableVpcServiceControlsRequestOut",
        "MethodSettingsIn": "_servicenetworking_206_MethodSettingsIn",
        "MethodSettingsOut": "_servicenetworking_207_MethodSettingsOut",
        "ValidateConsumerConfigRequestIn": "_servicenetworking_208_ValidateConsumerConfigRequestIn",
        "ValidateConsumerConfigRequestOut": "_servicenetworking_209_ValidateConsumerConfigRequestOut",
        "MixinIn": "_servicenetworking_210_MixinIn",
        "MixinOut": "_servicenetworking_211_MixinOut",
        "HttpRuleIn": "_servicenetworking_212_HttpRuleIn",
        "HttpRuleOut": "_servicenetworking_213_HttpRuleOut",
        "HttpIn": "_servicenetworking_214_HttpIn",
        "HttpOut": "_servicenetworking_215_HttpOut",
        "RemoveDnsZoneMetadataIn": "_servicenetworking_216_RemoveDnsZoneMetadataIn",
        "RemoveDnsZoneMetadataOut": "_servicenetworking_217_RemoveDnsZoneMetadataOut",
        "StatusIn": "_servicenetworking_218_StatusIn",
        "StatusOut": "_servicenetworking_219_StatusOut",
        "ServiceIn": "_servicenetworking_220_ServiceIn",
        "ServiceOut": "_servicenetworking_221_ServiceOut",
        "DeletePeeredDnsDomainMetadataIn": "_servicenetworking_222_DeletePeeredDnsDomainMetadataIn",
        "DeletePeeredDnsDomainMetadataOut": "_servicenetworking_223_DeletePeeredDnsDomainMetadataOut",
        "RangeReservationIn": "_servicenetworking_224_RangeReservationIn",
        "RangeReservationOut": "_servicenetworking_225_RangeReservationOut",
        "GoSettingsIn": "_servicenetworking_226_GoSettingsIn",
        "GoSettingsOut": "_servicenetworking_227_GoSettingsOut",
        "MonitoringDestinationIn": "_servicenetworking_228_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_servicenetworking_229_MonitoringDestinationOut",
        "RemoveDnsZoneRequestIn": "_servicenetworking_230_RemoveDnsZoneRequestIn",
        "RemoveDnsZoneRequestOut": "_servicenetworking_231_RemoveDnsZoneRequestOut",
        "BackendIn": "_servicenetworking_232_BackendIn",
        "BackendOut": "_servicenetworking_233_BackendOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListConnectionsResponseIn"] = t.struct(
        {"connections": t.array(t.proxy(renames["ConnectionIn"])).optional()}
    ).named(renames["ListConnectionsResponseIn"])
    types["ListConnectionsResponseOut"] = t.struct(
        {
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionsResponseOut"])
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
    types["AddDnsZoneRequestIn"] = t.struct(
        {"dnsSuffix": t.string(), "consumerNetwork": t.string(), "name": t.string()}
    ).named(renames["AddDnsZoneRequestIn"])
    types["AddDnsZoneRequestOut"] = t.struct(
        {
            "dnsSuffix": t.string(),
            "consumerNetwork": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDnsZoneRequestOut"])
    types["BackendRuleIn"] = t.struct(
        {
            "operationDeadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "deadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "operationDeadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "address": t.string().optional(),
            "pathTranslation": t.string(),
            "jwtAudience": t.string().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "deadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "selector": t.string().optional(),
            "protocol": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["UpdateConsumerConfigRequestIn"] = t.struct(
        {"consumerConfig": t.proxy(renames["ConsumerConfigIn"])}
    ).named(renames["UpdateConsumerConfigRequestIn"])
    types["UpdateConsumerConfigRequestOut"] = t.struct(
        {
            "consumerConfig": t.proxy(renames["ConsumerConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConsumerConfigRequestOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["SubnetworkIn"] = t.struct(
        {
            "network": t.string().optional(),
            "name": t.string().optional(),
            "region": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["SecondaryIpRangeIn"])
            ).optional(),
            "outsideAllocation": t.boolean().optional(),
            "ipCidrRange": t.string().optional(),
        }
    ).named(renames["SubnetworkIn"])
    types["SubnetworkOut"] = t.struct(
        {
            "network": t.string().optional(),
            "name": t.string().optional(),
            "region": t.string().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["SecondaryIpRangeOut"])
            ).optional(),
            "outsideAllocation": t.boolean().optional(),
            "ipCidrRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubnetworkOut"])
    types["MethodIn"] = t.struct(
        {
            "responseTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "syntax": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
            "name": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "responseTypeUrl": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "syntax": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
            "name": t.string().optional(),
            "requestTypeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["ConsumerProjectIn"] = t.struct({"projectNum": t.string()}).named(
        renames["ConsumerProjectIn"]
    )
    types["ConsumerProjectOut"] = t.struct(
        {
            "projectNum": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerProjectOut"])
    types["PartialDeleteConnectionMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PartialDeleteConnectionMetadataIn"])
    types["PartialDeleteConnectionMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PartialDeleteConnectionMetadataOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "launchStage": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "metricKind": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "unit": t.string().optional(),
            "description": t.string().optional(),
            "valueType": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "launchStage": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AddSubnetworkRequestIn"] = t.struct(
        {
            "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
            "useCustomComputeIdempotencyWindow": t.boolean().optional(),
            "computeIdempotencyWindow": t.string().optional(),
            "requestedAddress": t.string().optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "subnetworkUsers": t.array(t.string()).optional(),
            "secondaryIpRangeSpecs": t.array(
                t.proxy(renames["SecondaryIpRangeSpecIn"])
            ).optional(),
            "subnetwork": t.string(),
            "description": t.string().optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerNetwork": t.string(),
            "role": t.string().optional(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "consumer": t.string(),
            "purpose": t.string().optional(),
            "ipPrefixLength": t.integer(),
            "region": t.string(),
        }
    ).named(renames["AddSubnetworkRequestIn"])
    types["AddSubnetworkRequestOut"] = t.struct(
        {
            "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
            "useCustomComputeIdempotencyWindow": t.boolean().optional(),
            "computeIdempotencyWindow": t.string().optional(),
            "requestedAddress": t.string().optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "subnetworkUsers": t.array(t.string()).optional(),
            "secondaryIpRangeSpecs": t.array(
                t.proxy(renames["SecondaryIpRangeSpecOut"])
            ).optional(),
            "subnetwork": t.string(),
            "description": t.string().optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerNetwork": t.string(),
            "role": t.string().optional(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "consumer": t.string(),
            "purpose": t.string().optional(),
            "ipPrefixLength": t.integer(),
            "region": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSubnetworkRequestOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
    types["PeeredDnsDomainMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PeeredDnsDomainMetadataIn"]
    )
    types["PeeredDnsDomainMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PeeredDnsDomainMetadataOut"])
    types["DeleteConnectionMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteConnectionMetadataIn"]
    )
    types["DeleteConnectionMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteConnectionMetadataOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "provided": t.array(t.string()).optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["ConsumerConfigMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ConsumerConfigMetadataIn"]
    )
    types["ConsumerConfigMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ConsumerConfigMetadataOut"])
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "version": t.string().optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "version": t.string().optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
    types["EnumValueIn"] = t.struct(
        {
            "name": t.string().optional(),
            "number": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["EnumValueIn"])
    types["EnumValueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "number": t.integer().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumValueOut"])
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
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
    types["RemoveDnsRecordSetRequestIn"] = t.struct(
        {
            "zone": t.string(),
            "consumerNetwork": t.string(),
            "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
        }
    ).named(renames["RemoveDnsRecordSetRequestIn"])
    types["RemoveDnsRecordSetRequestOut"] = t.struct(
        {
            "zone": t.string(),
            "consumerNetwork": t.string(),
            "dnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveDnsRecordSetRequestOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
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
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
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
    types["ConsumerConfigIn"] = t.struct(
        {
            "producerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportCustomRoutes": t.boolean().optional(),
            "cloudsqlConfigs": t.array(t.proxy(renames["CloudSQLConfigIn"])).optional(),
            "consumerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerImportCustomRoutes": t.boolean().optional(),
            "consumerExportCustomRoutes": t.boolean().optional(),
            "consumerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "consumerImportCustomRoutes": t.boolean().optional(),
        }
    ).named(renames["ConsumerConfigIn"])
    types["ConsumerConfigOut"] = t.struct(
        {
            "producerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportCustomRoutes": t.boolean().optional(),
            "cloudsqlConfigs": t.array(
                t.proxy(renames["CloudSQLConfigOut"])
            ).optional(),
            "consumerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "vpcScReferenceArchitectureEnabled": t.boolean().optional(),
            "producerImportCustomRoutes": t.boolean().optional(),
            "usedIpRanges": t.array(t.string()).optional(),
            "reservedRanges": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"
                    ]
                )
            ).optional(),
            "producerNetwork": t.string().optional(),
            "consumerExportCustomRoutes": t.boolean().optional(),
            "consumerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "consumerImportCustomRoutes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerConfigOut"])
    types["SecondaryIpRangeSpecIn"] = t.struct(
        {
            "outsideAllocationPublicIpRange": t.string().optional(),
            "rangeName": t.string(),
            "requestedAddress": t.string().optional(),
            "ipPrefixLength": t.integer(),
        }
    ).named(renames["SecondaryIpRangeSpecIn"])
    types["SecondaryIpRangeSpecOut"] = t.struct(
        {
            "outsideAllocationPublicIpRange": t.string().optional(),
            "rangeName": t.string(),
            "requestedAddress": t.string().optional(),
            "ipPrefixLength": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecondaryIpRangeSpecOut"])
    types["CppSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["CppSettingsIn"])
    types["CppSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CppSettingsOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "jwksUri": t.string().optional(),
            "issuer": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "id": t.string().optional(),
            "audiences": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "jwksUri": t.string().optional(),
            "issuer": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "id": t.string().optional(),
            "audiences": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
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
    types["AddRolesResponseIn"] = t.struct(
        {"policyBinding": t.array(t.proxy(renames["PolicyBindingIn"]))}
    ).named(renames["AddRolesResponseIn"])
    types["AddRolesResponseOut"] = t.struct(
        {
            "policyBinding": t.array(t.proxy(renames["PolicyBindingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddRolesResponseOut"])
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
    types["LongRunningIn"] = t.struct(
        {
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "initialPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "initialPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["AddRolesRequestIn"] = t.struct(
        {
            "policyBinding": t.array(t.proxy(renames["PolicyBindingIn"])),
            "consumerNetwork": t.string(),
        }
    ).named(renames["AddRolesRequestIn"])
    types["AddRolesRequestOut"] = t.struct(
        {
            "policyBinding": t.array(t.proxy(renames["PolicyBindingOut"])),
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddRolesRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["AddDnsRecordSetRequestIn"] = t.struct(
        {
            "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "consumerNetwork": t.string(),
            "zone": t.string(),
        }
    ).named(renames["AddDnsRecordSetRequestIn"])
    types["AddDnsRecordSetRequestOut"] = t.struct(
        {
            "dnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "consumerNetwork": t.string(),
            "zone": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDnsRecordSetRequestOut"])
    types["PublishingIn"] = t.struct(
        {
            "documentationUri": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "githubLabel": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "newIssueUri": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "documentationUri": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "githubLabel": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["RemoveDnsRecordSetResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RemoveDnsRecordSetResponseIn"])
    types["RemoveDnsRecordSetResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsRecordSetResponseOut"])
    types["DocumentationRuleIn"] = t.struct(
        {
            "deprecationDescription": t.string().optional(),
            "description": t.string().optional(),
            "selector": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "deprecationDescription": t.string().optional(),
            "description": t.string().optional(),
            "selector": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
    types["RouteIn"] = t.struct(
        {
            "destRange": t.string().optional(),
            "network": t.string().optional(),
            "nextHopGateway": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["RouteIn"])
    types["RouteOut"] = t.struct(
        {
            "destRange": t.string().optional(),
            "network": t.string().optional(),
            "nextHopGateway": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteOut"])
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
            "freeTier": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "name": t.string().optional(),
            "duration": t.string().optional(),
            "maxLimit": t.string().optional(),
            "metric": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "values": t.struct({"_": t.string().optional()}).optional(),
            "unit": t.string().optional(),
            "freeTier": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "name": t.string().optional(),
            "duration": t.string().optional(),
            "maxLimit": t.string().optional(),
            "metric": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
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
    types["JwtLocationIn"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "query": t.string().optional(),
            "header": t.string().optional(),
            "cookie": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "query": t.string().optional(),
            "header": t.string().optional(),
            "cookie": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn"] = t.struct(
        {
            "ipPrefixLength": t.integer().optional(),
            "name": t.string().optional(),
            "address": t.string().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn"])
    types["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"] = t.struct(
        {
            "ipPrefixLength": t.integer().optional(),
            "name": t.string().optional(),
            "address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"])
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
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
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
    types["EnumIn"] = t.struct(
        {
            "syntax": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "syntax": t.string().optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["GoogleCloudServicenetworkingV1betaSubnetworkIn"] = t.struct(
        {
            "network": t.string().optional(),
            "name": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaSubnetworkIn"])
    types["GoogleCloudServicenetworkingV1betaSubnetworkOut"] = t.struct(
        {
            "network": t.string().optional(),
            "name": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaSubnetworkOut"])
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
    types["RemoveDnsRecordSetMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RemoveDnsRecordSetMetadataIn"])
    types["RemoveDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsRecordSetMetadataOut"])
    types["AddDnsRecordSetMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddDnsRecordSetMetadataIn"]
    )
    types["AddDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddDnsRecordSetMetadataOut"])
    types["RemoveDnsZoneResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveDnsZoneResponseIn"]
    )
    types["RemoveDnsZoneResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsZoneResponseOut"])
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
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "type": t.string(),
            "name": t.string().optional(),
            "launchStage": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["EnableVpcServiceControlsRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["EnableVpcServiceControlsRequestIn"])
    types["EnableVpcServiceControlsRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableVpcServiceControlsRequestOut"])
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
    types["TypeIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["DeleteConnectionRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["DeleteConnectionRequestIn"])
    types["DeleteConnectionRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConnectionRequestOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
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
    types["EndpointIn"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "allowCors": t.boolean().optional(),
            "target": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "allowCors": t.boolean().optional(),
            "target": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["UpdateDnsRecordSetMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateDnsRecordSetMetadataIn"])
    types["UpdateDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateDnsRecordSetMetadataOut"])
    types["ConnectionIn"] = t.struct(
        {
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "network": t.string().optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "peering": t.string().optional(),
            "network": t.string().optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["ValidateConsumerConfigResponseIn"] = t.struct(
        {
            "validationError": t.string().optional(),
            "isValid": t.boolean().optional(),
            "existingSubnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkIn"])
            ).optional(),
        }
    ).named(renames["ValidateConsumerConfigResponseIn"])
    types["ValidateConsumerConfigResponseOut"] = t.struct(
        {
            "validationError": t.string().optional(),
            "isValid": t.boolean().optional(),
            "existingSubnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigResponseOut"])
    types["AddDnsZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddDnsZoneMetadataIn"]
    )
    types["AddDnsZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddDnsZoneMetadataOut"])
    types["FieldIn"] = t.struct(
        {
            "packed": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
            "jsonName": t.string().optional(),
            "number": t.integer().optional(),
            "typeUrl": t.string().optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "packed": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "defaultValue": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "cardinality": t.string().optional(),
            "name": t.string().optional(),
            "jsonName": t.string().optional(),
            "number": t.integer().optional(),
            "typeUrl": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["DnsRecordSetIn"] = t.struct(
        {
            "type": t.string(),
            "domain": t.string(),
            "data": t.array(t.string()),
            "ttl": t.string(),
        }
    ).named(renames["DnsRecordSetIn"])
    types["DnsRecordSetOut"] = t.struct(
        {
            "type": t.string(),
            "domain": t.string(),
            "data": t.array(t.string()),
            "ttl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsRecordSetOut"])
    types["UpdateDnsRecordSetRequestIn"] = t.struct(
        {
            "newDnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "consumerNetwork": t.string(),
            "existingDnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "zone": t.string(),
        }
    ).named(renames["UpdateDnsRecordSetRequestIn"])
    types["UpdateDnsRecordSetRequestOut"] = t.struct(
        {
            "newDnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "consumerNetwork": t.string(),
            "existingDnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "zone": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDnsRecordSetRequestOut"])
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
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["ApiIn"] = t.struct(
        {
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "name": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
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
    types["AuthenticationRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
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
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
    types["AddRolesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddRolesMetadataIn"]
    )
    types["AddRolesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddRolesMetadataOut"])
    types["GoogleCloudServicenetworkingV1betaConnectionIn"] = t.struct(
        {
            "network": t.string().optional(),
            "service": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "peering": t.string().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaConnectionIn"])
    types["GoogleCloudServicenetworkingV1betaConnectionOut"] = t.struct(
        {
            "network": t.string().optional(),
            "service": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "peering": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaConnectionOut"])
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
    types["SecondaryIpRangeIn"] = t.struct(
        {"ipCidrRange": t.string().optional(), "rangeName": t.string().optional()}
    ).named(renames["SecondaryIpRangeIn"])
    types["SecondaryIpRangeOut"] = t.struct(
        {
            "ipCidrRange": t.string().optional(),
            "rangeName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecondaryIpRangeOut"])
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
    types["DocumentationIn"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "sectionOverrides": t.array(t.proxy(renames["PageIn"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "serviceRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "sectionOverrides": t.array(t.proxy(renames["PageOut"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "overview": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["DisableVpcServiceControlsRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["DisableVpcServiceControlsRequestIn"])
    types["DisableVpcServiceControlsRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableVpcServiceControlsRequestOut"])
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
    types["ValidateConsumerConfigRequestIn"] = t.struct(
        {
            "validateNetwork": t.boolean().optional(),
            "rangeReservation": t.proxy(renames["RangeReservationIn"]).optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerNetwork": t.string(),
            "consumerProject": t.proxy(renames["ConsumerProjectIn"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigRequestIn"])
    types["ValidateConsumerConfigRequestOut"] = t.struct(
        {
            "validateNetwork": t.boolean().optional(),
            "rangeReservation": t.proxy(renames["RangeReservationOut"]).optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerNetwork": t.string(),
            "consumerProject": t.proxy(renames["ConsumerProjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigRequestOut"])
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
    types["HttpRuleIn"] = t.struct(
        {
            "responseBody": t.string().optional(),
            "get": t.string().optional(),
            "post": t.string().optional(),
            "put": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "delete": t.string().optional(),
            "body": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "responseBody": t.string().optional(),
            "get": t.string().optional(),
            "post": t.string().optional(),
            "put": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "delete": t.string().optional(),
            "body": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
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
    types["RemoveDnsZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveDnsZoneMetadataIn"]
    )
    types["RemoveDnsZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsZoneMetadataOut"])
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
    types["ServiceIn"] = t.struct(
        {
            "context": t.proxy(renames["ContextIn"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "title": t.string().optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "id": t.string().optional(),
            "configVersion": t.integer().optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "name": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "producerProjectId": t.string().optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "context": t.proxy(renames["ContextOut"]).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "title": t.string().optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "id": t.string().optional(),
            "configVersion": t.integer().optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "name": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "producerProjectId": t.string().optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["DeletePeeredDnsDomainMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeletePeeredDnsDomainMetadataIn"])
    types["DeletePeeredDnsDomainMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeletePeeredDnsDomainMetadataOut"])
    types["RangeReservationIn"] = t.struct(
        {
            "ipPrefixLength": t.integer(),
            "subnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkIn"])
            ).optional(),
            "secondaryRangeIpPrefixLengths": t.array(t.integer()).optional(),
            "requestedRanges": t.array(t.string()).optional(),
        }
    ).named(renames["RangeReservationIn"])
    types["RangeReservationOut"] = t.struct(
        {
            "ipPrefixLength": t.integer(),
            "subnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkOut"])
            ).optional(),
            "secondaryRangeIpPrefixLengths": t.array(t.integer()).optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeReservationOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
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
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])

    functions = {}
    functions["servicesEnableVpcServiceControls"] = servicenetworking.patch(
        "v1/{parent}:disableVpcServiceControls",
        t.struct(
            {
                "parent": t.string().optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesValidate"] = servicenetworking.patch(
        "v1/{parent}:disableVpcServiceControls",
        t.struct(
            {
                "parent": t.string().optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesAddSubnetwork"] = servicenetworking.patch(
        "v1/{parent}:disableVpcServiceControls",
        t.struct(
            {
                "parent": t.string().optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesSearchRange"] = servicenetworking.patch(
        "v1/{parent}:disableVpcServiceControls",
        t.struct(
            {
                "parent": t.string().optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDisableVpcServiceControls"] = servicenetworking.patch(
        "v1/{parent}:disableVpcServiceControls",
        t.struct(
            {
                "parent": t.string().optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsRecordSetsRemove"] = servicenetworking.post(
        "v1/{parent}/dnsRecordSets:add",
        t.struct(
            {
                "parent": t.string(),
                "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
                "consumerNetwork": t.string(),
                "zone": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsRecordSetsUpdate"] = servicenetworking.post(
        "v1/{parent}/dnsRecordSets:add",
        t.struct(
            {
                "parent": t.string(),
                "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
                "consumerNetwork": t.string(),
                "zone": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsRecordSetsAdd"] = servicenetworking.post(
        "v1/{parent}/dnsRecordSets:add",
        t.struct(
            {
                "parent": t.string(),
                "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
                "consumerNetwork": t.string(),
                "zone": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsZonesAdd"] = servicenetworking.post(
        "v1/{parent}/dnsZones:remove",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesDnsZonesRemove"] = servicenetworking.post(
        "v1/{parent}/dnsZones:remove",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksUpdateConsumerConfig"
    ] = servicenetworking.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "includeUsedIpRanges": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsumerConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesProjectsGlobalNetworksGet"] = servicenetworking.get(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "includeUsedIpRanges": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ConsumerConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksPeeredDnsDomainsList"
    ] = servicenetworking.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksPeeredDnsDomainsCreate"
    ] = servicenetworking.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksPeeredDnsDomainsDelete"
    ] = servicenetworking.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
    functions["servicesRolesAdd"] = servicenetworking.post(
        "v1/{parent}/roles:add",
        t.struct(
            {
                "parent": t.string(),
                "policyBinding": t.array(t.proxy(renames["PolicyBindingIn"])),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = servicenetworking.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = servicenetworking.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = servicenetworking.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = servicenetworking.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
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
