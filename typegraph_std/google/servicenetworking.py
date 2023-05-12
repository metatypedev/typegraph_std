from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_servicenetworking() -> Import:
    servicenetworking = HTTPRuntime("https://servicenetworking.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicenetworking_1_ErrorResponse",
        "LoggingDestinationIn": "_servicenetworking_2_LoggingDestinationIn",
        "LoggingDestinationOut": "_servicenetworking_3_LoggingDestinationOut",
        "ValidateConsumerConfigRequestIn": "_servicenetworking_4_ValidateConsumerConfigRequestIn",
        "ValidateConsumerConfigRequestOut": "_servicenetworking_5_ValidateConsumerConfigRequestOut",
        "OperationIn": "_servicenetworking_6_OperationIn",
        "OperationOut": "_servicenetworking_7_OperationOut",
        "StatusIn": "_servicenetworking_8_StatusIn",
        "StatusOut": "_servicenetworking_9_StatusOut",
        "AddRolesRequestIn": "_servicenetworking_10_AddRolesRequestIn",
        "AddRolesRequestOut": "_servicenetworking_11_AddRolesRequestOut",
        "AddDnsZoneResponseIn": "_servicenetworking_12_AddDnsZoneResponseIn",
        "AddDnsZoneResponseOut": "_servicenetworking_13_AddDnsZoneResponseOut",
        "AddRolesResponseIn": "_servicenetworking_14_AddRolesResponseIn",
        "AddRolesResponseOut": "_servicenetworking_15_AddRolesResponseOut",
        "MonitoringDestinationIn": "_servicenetworking_16_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_servicenetworking_17_MonitoringDestinationOut",
        "AddDnsZoneRequestIn": "_servicenetworking_18_AddDnsZoneRequestIn",
        "AddDnsZoneRequestOut": "_servicenetworking_19_AddDnsZoneRequestOut",
        "AddDnsRecordSetMetadataIn": "_servicenetworking_20_AddDnsRecordSetMetadataIn",
        "AddDnsRecordSetMetadataOut": "_servicenetworking_21_AddDnsRecordSetMetadataOut",
        "PythonSettingsIn": "_servicenetworking_22_PythonSettingsIn",
        "PythonSettingsOut": "_servicenetworking_23_PythonSettingsOut",
        "ValidateConsumerConfigResponseIn": "_servicenetworking_24_ValidateConsumerConfigResponseIn",
        "ValidateConsumerConfigResponseOut": "_servicenetworking_25_ValidateConsumerConfigResponseOut",
        "BillingDestinationIn": "_servicenetworking_26_BillingDestinationIn",
        "BillingDestinationOut": "_servicenetworking_27_BillingDestinationOut",
        "AddRolesMetadataIn": "_servicenetworking_28_AddRolesMetadataIn",
        "AddRolesMetadataOut": "_servicenetworking_29_AddRolesMetadataOut",
        "UpdateDnsRecordSetRequestIn": "_servicenetworking_30_UpdateDnsRecordSetRequestIn",
        "UpdateDnsRecordSetRequestOut": "_servicenetworking_31_UpdateDnsRecordSetRequestOut",
        "CloudSQLConfigIn": "_servicenetworking_32_CloudSQLConfigIn",
        "CloudSQLConfigOut": "_servicenetworking_33_CloudSQLConfigOut",
        "AuthRequirementIn": "_servicenetworking_34_AuthRequirementIn",
        "AuthRequirementOut": "_servicenetworking_35_AuthRequirementOut",
        "QuotaLimitIn": "_servicenetworking_36_QuotaLimitIn",
        "QuotaLimitOut": "_servicenetworking_37_QuotaLimitOut",
        "SourceInfoIn": "_servicenetworking_38_SourceInfoIn",
        "SourceInfoOut": "_servicenetworking_39_SourceInfoOut",
        "OptionIn": "_servicenetworking_40_OptionIn",
        "OptionOut": "_servicenetworking_41_OptionOut",
        "ClientLibrarySettingsIn": "_servicenetworking_42_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_servicenetworking_43_ClientLibrarySettingsOut",
        "CancelOperationRequestIn": "_servicenetworking_44_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_servicenetworking_45_CancelOperationRequestOut",
        "CustomErrorRuleIn": "_servicenetworking_46_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_servicenetworking_47_CustomErrorRuleOut",
        "PartialDeleteConnectionMetadataIn": "_servicenetworking_48_PartialDeleteConnectionMetadataIn",
        "PartialDeleteConnectionMetadataOut": "_servicenetworking_49_PartialDeleteConnectionMetadataOut",
        "CommonLanguageSettingsIn": "_servicenetworking_50_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_servicenetworking_51_CommonLanguageSettingsOut",
        "SystemParameterIn": "_servicenetworking_52_SystemParameterIn",
        "SystemParameterOut": "_servicenetworking_53_SystemParameterOut",
        "ListOperationsResponseIn": "_servicenetworking_54_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_servicenetworking_55_ListOperationsResponseOut",
        "DisableVpcServiceControlsRequestIn": "_servicenetworking_56_DisableVpcServiceControlsRequestIn",
        "DisableVpcServiceControlsRequestOut": "_servicenetworking_57_DisableVpcServiceControlsRequestOut",
        "RangeReservationIn": "_servicenetworking_58_RangeReservationIn",
        "RangeReservationOut": "_servicenetworking_59_RangeReservationOut",
        "LoggingIn": "_servicenetworking_60_LoggingIn",
        "LoggingOut": "_servicenetworking_61_LoggingOut",
        "SystemParameterRuleIn": "_servicenetworking_62_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_servicenetworking_63_SystemParameterRuleOut",
        "PolicyBindingIn": "_servicenetworking_64_PolicyBindingIn",
        "PolicyBindingOut": "_servicenetworking_65_PolicyBindingOut",
        "PageIn": "_servicenetworking_66_PageIn",
        "PageOut": "_servicenetworking_67_PageOut",
        "AddSubnetworkRequestIn": "_servicenetworking_68_AddSubnetworkRequestIn",
        "AddSubnetworkRequestOut": "_servicenetworking_69_AddSubnetworkRequestOut",
        "CustomErrorIn": "_servicenetworking_70_CustomErrorIn",
        "CustomErrorOut": "_servicenetworking_71_CustomErrorOut",
        "CppSettingsIn": "_servicenetworking_72_CppSettingsIn",
        "CppSettingsOut": "_servicenetworking_73_CppSettingsOut",
        "MonitoredResourceDescriptorIn": "_servicenetworking_74_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_servicenetworking_75_MonitoredResourceDescriptorOut",
        "ConsumerProjectIn": "_servicenetworking_76_ConsumerProjectIn",
        "ConsumerProjectOut": "_servicenetworking_77_ConsumerProjectOut",
        "ListConnectionsResponseIn": "_servicenetworking_78_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_servicenetworking_79_ListConnectionsResponseOut",
        "HttpIn": "_servicenetworking_80_HttpIn",
        "HttpOut": "_servicenetworking_81_HttpOut",
        "LabelDescriptorIn": "_servicenetworking_82_LabelDescriptorIn",
        "LabelDescriptorOut": "_servicenetworking_83_LabelDescriptorOut",
        "AuthenticationIn": "_servicenetworking_84_AuthenticationIn",
        "AuthenticationOut": "_servicenetworking_85_AuthenticationOut",
        "NodeSettingsIn": "_servicenetworking_86_NodeSettingsIn",
        "NodeSettingsOut": "_servicenetworking_87_NodeSettingsOut",
        "EnableVpcServiceControlsRequestIn": "_servicenetworking_88_EnableVpcServiceControlsRequestIn",
        "EnableVpcServiceControlsRequestOut": "_servicenetworking_89_EnableVpcServiceControlsRequestOut",
        "ListPeeredDnsDomainsResponseIn": "_servicenetworking_90_ListPeeredDnsDomainsResponseIn",
        "ListPeeredDnsDomainsResponseOut": "_servicenetworking_91_ListPeeredDnsDomainsResponseOut",
        "PeeredDnsDomainMetadataIn": "_servicenetworking_92_PeeredDnsDomainMetadataIn",
        "PeeredDnsDomainMetadataOut": "_servicenetworking_93_PeeredDnsDomainMetadataOut",
        "GoogleCloudServicenetworkingV1betaSubnetworkIn": "_servicenetworking_94_GoogleCloudServicenetworkingV1betaSubnetworkIn",
        "GoogleCloudServicenetworkingV1betaSubnetworkOut": "_servicenetworking_95_GoogleCloudServicenetworkingV1betaSubnetworkOut",
        "ConnectionIn": "_servicenetworking_96_ConnectionIn",
        "ConnectionOut": "_servicenetworking_97_ConnectionOut",
        "AuthenticationRuleIn": "_servicenetworking_98_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_servicenetworking_99_AuthenticationRuleOut",
        "ContextIn": "_servicenetworking_100_ContextIn",
        "ContextOut": "_servicenetworking_101_ContextOut",
        "DeletePeeredDnsDomainMetadataIn": "_servicenetworking_102_DeletePeeredDnsDomainMetadataIn",
        "DeletePeeredDnsDomainMetadataOut": "_servicenetworking_103_DeletePeeredDnsDomainMetadataOut",
        "LogDescriptorIn": "_servicenetworking_104_LogDescriptorIn",
        "LogDescriptorOut": "_servicenetworking_105_LogDescriptorOut",
        "MonitoringIn": "_servicenetworking_106_MonitoringIn",
        "MonitoringOut": "_servicenetworking_107_MonitoringOut",
        "DnsZoneIn": "_servicenetworking_108_DnsZoneIn",
        "DnsZoneOut": "_servicenetworking_109_DnsZoneOut",
        "RemoveDnsZoneMetadataIn": "_servicenetworking_110_RemoveDnsZoneMetadataIn",
        "RemoveDnsZoneMetadataOut": "_servicenetworking_111_RemoveDnsZoneMetadataOut",
        "LongRunningIn": "_servicenetworking_112_LongRunningIn",
        "LongRunningOut": "_servicenetworking_113_LongRunningOut",
        "AuthProviderIn": "_servicenetworking_114_AuthProviderIn",
        "AuthProviderOut": "_servicenetworking_115_AuthProviderOut",
        "EnumIn": "_servicenetworking_116_EnumIn",
        "EnumOut": "_servicenetworking_117_EnumOut",
        "UsageRuleIn": "_servicenetworking_118_UsageRuleIn",
        "UsageRuleOut": "_servicenetworking_119_UsageRuleOut",
        "TypeIn": "_servicenetworking_120_TypeIn",
        "TypeOut": "_servicenetworking_121_TypeOut",
        "BillingIn": "_servicenetworking_122_BillingIn",
        "BillingOut": "_servicenetworking_123_BillingOut",
        "RemoveDnsZoneRequestIn": "_servicenetworking_124_RemoveDnsZoneRequestIn",
        "RemoveDnsZoneRequestOut": "_servicenetworking_125_RemoveDnsZoneRequestOut",
        "BackendRuleIn": "_servicenetworking_126_BackendRuleIn",
        "BackendRuleOut": "_servicenetworking_127_BackendRuleOut",
        "ApiIn": "_servicenetworking_128_ApiIn",
        "ApiOut": "_servicenetworking_129_ApiOut",
        "RemoveDnsZoneResponseIn": "_servicenetworking_130_RemoveDnsZoneResponseIn",
        "RemoveDnsZoneResponseOut": "_servicenetworking_131_RemoveDnsZoneResponseOut",
        "HttpRuleIn": "_servicenetworking_132_HttpRuleIn",
        "HttpRuleOut": "_servicenetworking_133_HttpRuleOut",
        "SecondaryIpRangeSpecIn": "_servicenetworking_134_SecondaryIpRangeSpecIn",
        "SecondaryIpRangeSpecOut": "_servicenetworking_135_SecondaryIpRangeSpecOut",
        "JavaSettingsIn": "_servicenetworking_136_JavaSettingsIn",
        "JavaSettingsOut": "_servicenetworking_137_JavaSettingsOut",
        "CustomHttpPatternIn": "_servicenetworking_138_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_servicenetworking_139_CustomHttpPatternOut",
        "RangeIn": "_servicenetworking_140_RangeIn",
        "RangeOut": "_servicenetworking_141_RangeOut",
        "ControlIn": "_servicenetworking_142_ControlIn",
        "ControlOut": "_servicenetworking_143_ControlOut",
        "MetricDescriptorMetadataIn": "_servicenetworking_144_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_servicenetworking_145_MetricDescriptorMetadataOut",
        "MetricRuleIn": "_servicenetworking_146_MetricRuleIn",
        "MetricRuleOut": "_servicenetworking_147_MetricRuleOut",
        "JwtLocationIn": "_servicenetworking_148_JwtLocationIn",
        "JwtLocationOut": "_servicenetworking_149_JwtLocationOut",
        "DotnetSettingsIn": "_servicenetworking_150_DotnetSettingsIn",
        "DotnetSettingsOut": "_servicenetworking_151_DotnetSettingsOut",
        "DeleteConnectionMetadataIn": "_servicenetworking_152_DeleteConnectionMetadataIn",
        "DeleteConnectionMetadataOut": "_servicenetworking_153_DeleteConnectionMetadataOut",
        "MethodIn": "_servicenetworking_154_MethodIn",
        "MethodOut": "_servicenetworking_155_MethodOut",
        "DocumentationRuleIn": "_servicenetworking_156_DocumentationRuleIn",
        "DocumentationRuleOut": "_servicenetworking_157_DocumentationRuleOut",
        "ConsumerConfigMetadataIn": "_servicenetworking_158_ConsumerConfigMetadataIn",
        "ConsumerConfigMetadataOut": "_servicenetworking_159_ConsumerConfigMetadataOut",
        "SecondaryIpRangeIn": "_servicenetworking_160_SecondaryIpRangeIn",
        "SecondaryIpRangeOut": "_servicenetworking_161_SecondaryIpRangeOut",
        "MethodSettingsIn": "_servicenetworking_162_MethodSettingsIn",
        "MethodSettingsOut": "_servicenetworking_163_MethodSettingsOut",
        "GoSettingsIn": "_servicenetworking_164_GoSettingsIn",
        "GoSettingsOut": "_servicenetworking_165_GoSettingsOut",
        "RemoveDnsRecordSetResponseIn": "_servicenetworking_166_RemoveDnsRecordSetResponseIn",
        "RemoveDnsRecordSetResponseOut": "_servicenetworking_167_RemoveDnsRecordSetResponseOut",
        "FieldIn": "_servicenetworking_168_FieldIn",
        "FieldOut": "_servicenetworking_169_FieldOut",
        "DeleteConnectionRequestIn": "_servicenetworking_170_DeleteConnectionRequestIn",
        "DeleteConnectionRequestOut": "_servicenetworking_171_DeleteConnectionRequestOut",
        "PublishingIn": "_servicenetworking_172_PublishingIn",
        "PublishingOut": "_servicenetworking_173_PublishingOut",
        "DnsRecordSetIn": "_servicenetworking_174_DnsRecordSetIn",
        "DnsRecordSetOut": "_servicenetworking_175_DnsRecordSetOut",
        "SubnetworkIn": "_servicenetworking_176_SubnetworkIn",
        "SubnetworkOut": "_servicenetworking_177_SubnetworkOut",
        "ServiceIn": "_servicenetworking_178_ServiceIn",
        "ServiceOut": "_servicenetworking_179_ServiceOut",
        "RubySettingsIn": "_servicenetworking_180_RubySettingsIn",
        "RubySettingsOut": "_servicenetworking_181_RubySettingsOut",
        "DocumentationIn": "_servicenetworking_182_DocumentationIn",
        "DocumentationOut": "_servicenetworking_183_DocumentationOut",
        "AddDnsRecordSetRequestIn": "_servicenetworking_184_AddDnsRecordSetRequestIn",
        "AddDnsRecordSetRequestOut": "_servicenetworking_185_AddDnsRecordSetRequestOut",
        "MixinIn": "_servicenetworking_186_MixinIn",
        "MixinOut": "_servicenetworking_187_MixinOut",
        "PeeredDnsDomainIn": "_servicenetworking_188_PeeredDnsDomainIn",
        "PeeredDnsDomainOut": "_servicenetworking_189_PeeredDnsDomainOut",
        "EmptyIn": "_servicenetworking_190_EmptyIn",
        "EmptyOut": "_servicenetworking_191_EmptyOut",
        "UpdateConsumerConfigRequestIn": "_servicenetworking_192_UpdateConsumerConfigRequestIn",
        "UpdateConsumerConfigRequestOut": "_servicenetworking_193_UpdateConsumerConfigRequestOut",
        "QuotaIn": "_servicenetworking_194_QuotaIn",
        "QuotaOut": "_servicenetworking_195_QuotaOut",
        "EndpointIn": "_servicenetworking_196_EndpointIn",
        "EndpointOut": "_servicenetworking_197_EndpointOut",
        "SystemParametersIn": "_servicenetworking_198_SystemParametersIn",
        "SystemParametersOut": "_servicenetworking_199_SystemParametersOut",
        "GoogleCloudServicenetworkingV1betaConnectionIn": "_servicenetworking_200_GoogleCloudServicenetworkingV1betaConnectionIn",
        "GoogleCloudServicenetworkingV1betaConnectionOut": "_servicenetworking_201_GoogleCloudServicenetworkingV1betaConnectionOut",
        "RemoveDnsRecordSetRequestIn": "_servicenetworking_202_RemoveDnsRecordSetRequestIn",
        "RemoveDnsRecordSetRequestOut": "_servicenetworking_203_RemoveDnsRecordSetRequestOut",
        "ContextRuleIn": "_servicenetworking_204_ContextRuleIn",
        "ContextRuleOut": "_servicenetworking_205_ContextRuleOut",
        "RouteIn": "_servicenetworking_206_RouteIn",
        "RouteOut": "_servicenetworking_207_RouteOut",
        "SearchRangeRequestIn": "_servicenetworking_208_SearchRangeRequestIn",
        "SearchRangeRequestOut": "_servicenetworking_209_SearchRangeRequestOut",
        "ConsumerConfigIn": "_servicenetworking_210_ConsumerConfigIn",
        "ConsumerConfigOut": "_servicenetworking_211_ConsumerConfigOut",
        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn": "_servicenetworking_212_GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn",
        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut": "_servicenetworking_213_GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut",
        "SourceContextIn": "_servicenetworking_214_SourceContextIn",
        "SourceContextOut": "_servicenetworking_215_SourceContextOut",
        "MetricDescriptorIn": "_servicenetworking_216_MetricDescriptorIn",
        "MetricDescriptorOut": "_servicenetworking_217_MetricDescriptorOut",
        "OAuthRequirementsIn": "_servicenetworking_218_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_servicenetworking_219_OAuthRequirementsOut",
        "EnumValueIn": "_servicenetworking_220_EnumValueIn",
        "EnumValueOut": "_servicenetworking_221_EnumValueOut",
        "RemoveDnsRecordSetMetadataIn": "_servicenetworking_222_RemoveDnsRecordSetMetadataIn",
        "RemoveDnsRecordSetMetadataOut": "_servicenetworking_223_RemoveDnsRecordSetMetadataOut",
        "UpdateDnsRecordSetMetadataIn": "_servicenetworking_224_UpdateDnsRecordSetMetadataIn",
        "UpdateDnsRecordSetMetadataOut": "_servicenetworking_225_UpdateDnsRecordSetMetadataOut",
        "UsageIn": "_servicenetworking_226_UsageIn",
        "UsageOut": "_servicenetworking_227_UsageOut",
        "BackendIn": "_servicenetworking_228_BackendIn",
        "BackendOut": "_servicenetworking_229_BackendOut",
        "PhpSettingsIn": "_servicenetworking_230_PhpSettingsIn",
        "PhpSettingsOut": "_servicenetworking_231_PhpSettingsOut",
        "AddDnsZoneMetadataIn": "_servicenetworking_232_AddDnsZoneMetadataIn",
        "AddDnsZoneMetadataOut": "_servicenetworking_233_AddDnsZoneMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ValidateConsumerConfigRequestIn"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerProject": t.proxy(renames["ConsumerProjectIn"]).optional(),
            "validateNetwork": t.boolean().optional(),
            "rangeReservation": t.proxy(renames["RangeReservationIn"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigRequestIn"])
    types["ValidateConsumerConfigRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerProject": t.proxy(renames["ConsumerProjectOut"]).optional(),
            "validateNetwork": t.boolean().optional(),
            "rangeReservation": t.proxy(renames["RangeReservationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["AddRolesResponseIn"] = t.struct(
        {"policyBinding": t.array(t.proxy(renames["PolicyBindingIn"]))}
    ).named(renames["AddRolesResponseIn"])
    types["AddRolesResponseOut"] = t.struct(
        {
            "policyBinding": t.array(t.proxy(renames["PolicyBindingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddRolesResponseOut"])
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
    types["AddDnsRecordSetMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddDnsRecordSetMetadataIn"]
    )
    types["AddDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddDnsRecordSetMetadataOut"])
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
    types["ValidateConsumerConfigResponseIn"] = t.struct(
        {
            "isValid": t.boolean().optional(),
            "existingSubnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkIn"])
            ).optional(),
            "validationError": t.string().optional(),
        }
    ).named(renames["ValidateConsumerConfigResponseIn"])
    types["ValidateConsumerConfigResponseOut"] = t.struct(
        {
            "isValid": t.boolean().optional(),
            "existingSubnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkOut"])
            ).optional(),
            "validationError": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigResponseOut"])
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
    types["AddRolesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddRolesMetadataIn"]
    )
    types["AddRolesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddRolesMetadataOut"])
    types["UpdateDnsRecordSetRequestIn"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "existingDnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "newDnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "zone": t.string(),
        }
    ).named(renames["UpdateDnsRecordSetRequestIn"])
    types["UpdateDnsRecordSetRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "existingDnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "newDnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "zone": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDnsRecordSetRequestOut"])
    types["CloudSQLConfigIn"] = t.struct(
        {
            "umbrellaNetwork": t.string().optional(),
            "service": t.string().optional(),
            "umbrellaProject": t.string().optional(),
        }
    ).named(renames["CloudSQLConfigIn"])
    types["CloudSQLConfigOut"] = t.struct(
        {
            "umbrellaNetwork": t.string().optional(),
            "service": t.string().optional(),
            "umbrellaProject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSQLConfigOut"])
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
    types["QuotaLimitIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "maxLimit": t.string().optional(),
            "metric": t.string().optional(),
            "duration": t.string().optional(),
            "description": t.string().optional(),
            "unit": t.string().optional(),
            "freeTier": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "maxLimit": t.string().optional(),
            "metric": t.string().optional(),
            "duration": t.string().optional(),
            "description": t.string().optional(),
            "unit": t.string().optional(),
            "freeTier": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
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
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "version": t.string().optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "version": t.string().optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "restNumericEnums": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["PartialDeleteConnectionMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PartialDeleteConnectionMetadataIn"])
    types["PartialDeleteConnectionMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PartialDeleteConnectionMetadataOut"])
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
    types["SystemParameterIn"] = t.struct(
        {
            "httpHeader": t.string().optional(),
            "name": t.string().optional(),
            "urlQueryParameter": t.string().optional(),
        }
    ).named(renames["SystemParameterIn"])
    types["SystemParameterOut"] = t.struct(
        {
            "httpHeader": t.string().optional(),
            "name": t.string().optional(),
            "urlQueryParameter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParameterOut"])
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
    types["DisableVpcServiceControlsRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["DisableVpcServiceControlsRequestIn"])
    types["DisableVpcServiceControlsRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableVpcServiceControlsRequestOut"])
    types["RangeReservationIn"] = t.struct(
        {
            "ipPrefixLength": t.integer(),
            "subnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkIn"])
            ).optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "secondaryRangeIpPrefixLengths": t.array(t.integer()).optional(),
        }
    ).named(renames["RangeReservationIn"])
    types["RangeReservationOut"] = t.struct(
        {
            "ipPrefixLength": t.integer(),
            "subnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkOut"])
            ).optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "secondaryRangeIpPrefixLengths": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeReservationOut"])
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
    types["PolicyBindingIn"] = t.struct(
        {"role": t.string(), "member": t.string()}
    ).named(renames["PolicyBindingIn"])
    types["PolicyBindingOut"] = t.struct(
        {
            "role": t.string(),
            "member": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyBindingOut"])
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
    types["AddSubnetworkRequestIn"] = t.struct(
        {
            "description": t.string().optional(),
            "subnetwork": t.string(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "requestedAddress": t.string().optional(),
            "consumer": t.string(),
            "useCustomComputeIdempotencyWindow": t.boolean().optional(),
            "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
            "purpose": t.string().optional(),
            "role": t.string().optional(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "computeIdempotencyWindow": t.string().optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "region": t.string(),
            "ipPrefixLength": t.integer(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "subnetworkUsers": t.array(t.string()).optional(),
            "secondaryIpRangeSpecs": t.array(
                t.proxy(renames["SecondaryIpRangeSpecIn"])
            ).optional(),
            "consumerNetwork": t.string(),
        }
    ).named(renames["AddSubnetworkRequestIn"])
    types["AddSubnetworkRequestOut"] = t.struct(
        {
            "description": t.string().optional(),
            "subnetwork": t.string(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "requestedAddress": t.string().optional(),
            "consumer": t.string(),
            "useCustomComputeIdempotencyWindow": t.boolean().optional(),
            "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
            "purpose": t.string().optional(),
            "role": t.string().optional(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "computeIdempotencyWindow": t.string().optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "region": t.string(),
            "ipPrefixLength": t.integer(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "subnetworkUsers": t.array(t.string()).optional(),
            "secondaryIpRangeSpecs": t.array(
                t.proxy(renames["SecondaryIpRangeSpecOut"])
            ).optional(),
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSubnetworkRequestOut"])
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
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "name": t.string().optional(),
            "type": t.string(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "launchStage": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "name": t.string().optional(),
            "type": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
    types["ConsumerProjectIn"] = t.struct({"projectNum": t.string()}).named(
        renames["ConsumerProjectIn"]
    )
    types["ConsumerProjectOut"] = t.struct(
        {
            "projectNum": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerProjectOut"])
    types["ListConnectionsResponseIn"] = t.struct(
        {"connections": t.array(t.proxy(renames["ConnectionIn"])).optional()}
    ).named(renames["ListConnectionsResponseIn"])
    types["ListConnectionsResponseOut"] = t.struct(
        {
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionsResponseOut"])
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
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
    types["EnableVpcServiceControlsRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["EnableVpcServiceControlsRequestIn"])
    types["EnableVpcServiceControlsRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableVpcServiceControlsRequestOut"])
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
    types["PeeredDnsDomainMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PeeredDnsDomainMetadataIn"]
    )
    types["PeeredDnsDomainMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PeeredDnsDomainMetadataOut"])
    types["GoogleCloudServicenetworkingV1betaSubnetworkIn"] = t.struct(
        {
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "name": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaSubnetworkIn"])
    types["GoogleCloudServicenetworkingV1betaSubnetworkOut"] = t.struct(
        {
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "name": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaSubnetworkOut"])
    types["ConnectionIn"] = t.struct(
        {
            "network": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "service": t.string().optional(),
            "network": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "peering": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["AuthenticationRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsIn"]).optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementIn"])).optional(),
        }
    ).named(renames["AuthenticationRuleIn"])
    types["AuthenticationRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "allowWithoutCredential": t.boolean().optional(),
            "oauth": t.proxy(renames["OAuthRequirementsOut"]).optional(),
            "requirements": t.array(t.proxy(renames["AuthRequirementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationRuleOut"])
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["DeletePeeredDnsDomainMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeletePeeredDnsDomainMetadataIn"])
    types["DeletePeeredDnsDomainMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeletePeeredDnsDomainMetadataOut"])
    types["LogDescriptorIn"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["LogDescriptorIn"])
    types["LogDescriptorOut"] = t.struct(
        {
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogDescriptorOut"])
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
    types["RemoveDnsZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveDnsZoneMetadataIn"]
    )
    types["RemoveDnsZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsZoneMetadataOut"])
    types["LongRunningIn"] = t.struct(
        {
            "initialPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "initialPollDelay": t.string().optional(),
            "totalPollTimeout": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "jwksUri": t.string().optional(),
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["EnumIn"] = t.struct(
        {
            "edition": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "edition": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "name": t.string().optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
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
    types["TypeIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "name": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "name": t.string().optional(),
            "oneofs": t.array(t.string()).optional(),
            "edition": t.string().optional(),
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "syntax": t.string().optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
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
    types["RemoveDnsZoneRequestIn"] = t.struct(
        {"consumerNetwork": t.string(), "name": t.string()}
    ).named(renames["RemoveDnsZoneRequestIn"])
    types["RemoveDnsZoneRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveDnsZoneRequestOut"])
    types["BackendRuleIn"] = t.struct(
        {
            "minDeadline": t.number().optional(),
            "jwtAudience": t.string().optional(),
            "operationDeadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "protocol": t.string().optional(),
            "address": t.string().optional(),
            "selector": t.string().optional(),
            "deadline": t.number().optional(),
            "pathTranslation": t.string(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "minDeadline": t.number().optional(),
            "jwtAudience": t.string().optional(),
            "operationDeadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "protocol": t.string().optional(),
            "address": t.string().optional(),
            "selector": t.string().optional(),
            "deadline": t.number().optional(),
            "pathTranslation": t.string(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["ApiIn"] = t.struct(
        {
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
            "version": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "version": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["RemoveDnsZoneResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveDnsZoneResponseIn"]
    )
    types["RemoveDnsZoneResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsZoneResponseOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "get": t.string().optional(),
            "delete": t.string().optional(),
            "put": t.string().optional(),
            "body": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
            "patch": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "post": t.string().optional(),
            "responseBody": t.string().optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "get": t.string().optional(),
            "delete": t.string().optional(),
            "put": t.string().optional(),
            "body": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "patch": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "post": t.string().optional(),
            "responseBody": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
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
    types["RangeIn"] = t.struct(
        {"network": t.string().optional(), "ipCidrRange": t.string().optional()}
    ).named(renames["RangeIn"])
    types["RangeOut"] = t.struct(
        {
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
    types["MetricDescriptorMetadataIn"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
        }
    ).named(renames["MetricDescriptorMetadataIn"])
    types["MetricDescriptorMetadataOut"] = t.struct(
        {
            "samplePeriod": t.string().optional(),
            "launchStage": t.string().optional(),
            "ingestDelay": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorMetadataOut"])
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
    types["JwtLocationIn"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
            "header": t.string().optional(),
            "query": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "valuePrefix": t.string().optional(),
            "cookie": t.string().optional(),
            "header": t.string().optional(),
            "query": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["DotnetSettingsIn"] = t.struct(
        {
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["DeleteConnectionMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteConnectionMetadataIn"]
    )
    types["DeleteConnectionMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteConnectionMetadataOut"])
    types["MethodIn"] = t.struct(
        {
            "responseTypeUrl": t.string().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "requestTypeUrl": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "responseTypeUrl": t.string().optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "requestTypeUrl": t.string().optional(),
            "requestStreaming": t.boolean().optional(),
            "responseStreaming": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
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
    types["ConsumerConfigMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ConsumerConfigMetadataIn"]
    )
    types["ConsumerConfigMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ConsumerConfigMetadataOut"])
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
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
    types["RemoveDnsRecordSetResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RemoveDnsRecordSetResponseIn"])
    types["RemoveDnsRecordSetResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsRecordSetResponseOut"])
    types["FieldIn"] = t.struct(
        {
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "oneofIndex": t.integer().optional(),
            "jsonName": t.string().optional(),
            "packed": t.boolean().optional(),
            "kind": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "typeUrl": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "defaultValue": t.string().optional(),
            "name": t.string().optional(),
            "cardinality": t.string().optional(),
            "number": t.integer().optional(),
            "oneofIndex": t.integer().optional(),
            "jsonName": t.string().optional(),
            "packed": t.boolean().optional(),
            "kind": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "typeUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["DeleteConnectionRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["DeleteConnectionRequestIn"])
    types["DeleteConnectionRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConnectionRequestOut"])
    types["PublishingIn"] = t.struct(
        {
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "docTagPrefix": t.string().optional(),
            "organization": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "githubLabel": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "documentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "docTagPrefix": t.string().optional(),
            "organization": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "githubLabel": t.string().optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "documentationUri": t.string().optional(),
            "apiShortName": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
    types["DnsRecordSetIn"] = t.struct(
        {
            "ttl": t.string(),
            "type": t.string(),
            "data": t.array(t.string()),
            "domain": t.string(),
        }
    ).named(renames["DnsRecordSetIn"])
    types["DnsRecordSetOut"] = t.struct(
        {
            "ttl": t.string(),
            "type": t.string(),
            "data": t.array(t.string()),
            "domain": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsRecordSetOut"])
    types["SubnetworkIn"] = t.struct(
        {
            "secondaryIpRanges": t.array(
                t.proxy(renames["SecondaryIpRangeIn"])
            ).optional(),
            "region": t.string().optional(),
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["SubnetworkIn"])
    types["SubnetworkOut"] = t.struct(
        {
            "secondaryIpRanges": t.array(
                t.proxy(renames["SecondaryIpRangeOut"])
            ).optional(),
            "region": t.string().optional(),
            "network": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubnetworkOut"])
    types["ServiceIn"] = t.struct(
        {
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "configVersion": t.integer().optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "title": t.string().optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "name": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "id": t.string().optional(),
            "producerProjectId": t.string().optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "configVersion": t.integer().optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "title": t.string().optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "name": t.string().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "id": t.string().optional(),
            "producerProjectId": t.string().optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["DocumentationIn"] = t.struct(
        {
            "serviceRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "overview": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "serviceRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "documentationRootUrl": t.string().optional(),
            "summary": t.string().optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "overview": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
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
    types["PeeredDnsDomainIn"] = t.struct(
        {"dnsSuffix": t.string().optional(), "name": t.string().optional()}
    ).named(renames["PeeredDnsDomainIn"])
    types["PeeredDnsDomainOut"] = t.struct(
        {
            "dnsSuffix": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeeredDnsDomainOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["UpdateConsumerConfigRequestIn"] = t.struct(
        {"consumerConfig": t.proxy(renames["ConsumerConfigIn"])}
    ).named(renames["UpdateConsumerConfigRequestIn"])
    types["UpdateConsumerConfigRequestOut"] = t.struct(
        {
            "consumerConfig": t.proxy(renames["ConsumerConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConsumerConfigRequestOut"])
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
    types["EndpointIn"] = t.struct(
        {
            "target": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "allowCors": t.boolean().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "target": t.string().optional(),
            "aliases": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["GoogleCloudServicenetworkingV1betaConnectionIn"] = t.struct(
        {
            "peering": t.string().optional(),
            "network": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaConnectionIn"])
    types["GoogleCloudServicenetworkingV1betaConnectionOut"] = t.struct(
        {
            "peering": t.string().optional(),
            "network": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaConnectionOut"])
    types["RemoveDnsRecordSetRequestIn"] = t.struct(
        {
            "dnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "consumerNetwork": t.string(),
            "zone": t.string(),
        }
    ).named(renames["RemoveDnsRecordSetRequestIn"])
    types["RemoveDnsRecordSetRequestOut"] = t.struct(
        {
            "dnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "consumerNetwork": t.string(),
            "zone": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveDnsRecordSetRequestOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["RouteIn"] = t.struct(
        {
            "name": t.string().optional(),
            "nextHopGateway": t.string().optional(),
            "destRange": t.string().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["RouteIn"])
    types["RouteOut"] = t.struct(
        {
            "name": t.string().optional(),
            "nextHopGateway": t.string().optional(),
            "destRange": t.string().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RouteOut"])
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
    types["ConsumerConfigIn"] = t.struct(
        {
            "producerImportCustomRoutes": t.boolean().optional(),
            "consumerImportCustomRoutes": t.boolean().optional(),
            "consumerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "cloudsqlConfigs": t.array(t.proxy(renames["CloudSQLConfigIn"])).optional(),
            "consumerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportCustomRoutes": t.boolean().optional(),
            "consumerExportCustomRoutes": t.boolean().optional(),
        }
    ).named(renames["ConsumerConfigIn"])
    types["ConsumerConfigOut"] = t.struct(
        {
            "producerImportCustomRoutes": t.boolean().optional(),
            "consumerImportCustomRoutes": t.boolean().optional(),
            "usedIpRanges": t.array(t.string()).optional(),
            "vpcScReferenceArchitectureEnabled": t.boolean().optional(),
            "reservedRanges": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"
                    ]
                )
            ).optional(),
            "consumerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerNetwork": t.string().optional(),
            "producerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "cloudsqlConfigs": t.array(
                t.proxy(renames["CloudSQLConfigOut"])
            ).optional(),
            "consumerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportCustomRoutes": t.boolean().optional(),
            "consumerExportCustomRoutes": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerConfigOut"])
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
    types["SourceContextIn"] = t.struct({"fileName": t.string().optional()}).named(
        renames["SourceContextIn"]
    )
    types["SourceContextOut"] = t.struct(
        {
            "fileName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceContextOut"])
    types["MetricDescriptorIn"] = t.struct(
        {
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "description": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "unit": t.string().optional(),
            "metricKind": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "type": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "launchStage": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "valueType": t.string().optional(),
            "description": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
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
    types["RemoveDnsRecordSetMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RemoveDnsRecordSetMetadataIn"])
    types["RemoveDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsRecordSetMetadataOut"])
    types["UpdateDnsRecordSetMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateDnsRecordSetMetadataIn"])
    types["UpdateDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateDnsRecordSetMetadataOut"])
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
    types["AddDnsZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddDnsZoneMetadataIn"]
    )
    types["AddDnsZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddDnsZoneMetadataOut"])

    functions = {}
    functions["servicesDisableVpcServiceControls"] = servicenetworking.post(
        "v1/{parent}:addSubnetwork",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "subnetwork": t.string(),
                "privateIpv6GoogleAccess": t.string().optional(),
                "requestedAddress": t.string().optional(),
                "consumer": t.string(),
                "useCustomComputeIdempotencyWindow": t.boolean().optional(),
                "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
                "purpose": t.string().optional(),
                "role": t.string().optional(),
                "outsideAllocationPublicIpRange": t.string().optional(),
                "computeIdempotencyWindow": t.string().optional(),
                "requestedRanges": t.array(t.string()).optional(),
                "region": t.string(),
                "ipPrefixLength": t.integer(),
                "checkServiceNetworkingUsePermission": t.boolean().optional(),
                "subnetworkUsers": t.array(t.string()).optional(),
                "secondaryIpRangeSpecs": t.array(
                    t.proxy(renames["SecondaryIpRangeSpecIn"])
                ).optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesEnableVpcServiceControls"] = servicenetworking.post(
        "v1/{parent}:addSubnetwork",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "subnetwork": t.string(),
                "privateIpv6GoogleAccess": t.string().optional(),
                "requestedAddress": t.string().optional(),
                "consumer": t.string(),
                "useCustomComputeIdempotencyWindow": t.boolean().optional(),
                "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
                "purpose": t.string().optional(),
                "role": t.string().optional(),
                "outsideAllocationPublicIpRange": t.string().optional(),
                "computeIdempotencyWindow": t.string().optional(),
                "requestedRanges": t.array(t.string()).optional(),
                "region": t.string(),
                "ipPrefixLength": t.integer(),
                "checkServiceNetworkingUsePermission": t.boolean().optional(),
                "subnetworkUsers": t.array(t.string()).optional(),
                "secondaryIpRangeSpecs": t.array(
                    t.proxy(renames["SecondaryIpRangeSpecIn"])
                ).optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesValidate"] = servicenetworking.post(
        "v1/{parent}:addSubnetwork",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "subnetwork": t.string(),
                "privateIpv6GoogleAccess": t.string().optional(),
                "requestedAddress": t.string().optional(),
                "consumer": t.string(),
                "useCustomComputeIdempotencyWindow": t.boolean().optional(),
                "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
                "purpose": t.string().optional(),
                "role": t.string().optional(),
                "outsideAllocationPublicIpRange": t.string().optional(),
                "computeIdempotencyWindow": t.string().optional(),
                "requestedRanges": t.array(t.string()).optional(),
                "region": t.string(),
                "ipPrefixLength": t.integer(),
                "checkServiceNetworkingUsePermission": t.boolean().optional(),
                "subnetworkUsers": t.array(t.string()).optional(),
                "secondaryIpRangeSpecs": t.array(
                    t.proxy(renames["SecondaryIpRangeSpecIn"])
                ).optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesSearchRange"] = servicenetworking.post(
        "v1/{parent}:addSubnetwork",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "subnetwork": t.string(),
                "privateIpv6GoogleAccess": t.string().optional(),
                "requestedAddress": t.string().optional(),
                "consumer": t.string(),
                "useCustomComputeIdempotencyWindow": t.boolean().optional(),
                "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
                "purpose": t.string().optional(),
                "role": t.string().optional(),
                "outsideAllocationPublicIpRange": t.string().optional(),
                "computeIdempotencyWindow": t.string().optional(),
                "requestedRanges": t.array(t.string()).optional(),
                "region": t.string(),
                "ipPrefixLength": t.integer(),
                "checkServiceNetworkingUsePermission": t.boolean().optional(),
                "subnetworkUsers": t.array(t.string()).optional(),
                "secondaryIpRangeSpecs": t.array(
                    t.proxy(renames["SecondaryIpRangeSpecIn"])
                ).optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesAddSubnetwork"] = servicenetworking.post(
        "v1/{parent}:addSubnetwork",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "subnetwork": t.string(),
                "privateIpv6GoogleAccess": t.string().optional(),
                "requestedAddress": t.string().optional(),
                "consumer": t.string(),
                "useCustomComputeIdempotencyWindow": t.boolean().optional(),
                "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
                "purpose": t.string().optional(),
                "role": t.string().optional(),
                "outsideAllocationPublicIpRange": t.string().optional(),
                "computeIdempotencyWindow": t.string().optional(),
                "requestedRanges": t.array(t.string()).optional(),
                "region": t.string(),
                "ipPrefixLength": t.integer(),
                "checkServiceNetworkingUsePermission": t.boolean().optional(),
                "subnetworkUsers": t.array(t.string()).optional(),
                "secondaryIpRangeSpecs": t.array(
                    t.proxy(renames["SecondaryIpRangeSpecIn"])
                ).optional(),
                "consumerNetwork": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConnectionsDeleteConnection"] = servicenetworking.patch(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "network": t.string().optional(),
                "reservedPeeringRanges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConnectionsList"] = servicenetworking.patch(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "network": t.string().optional(),
                "reservedPeeringRanges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConnectionsCreate"] = servicenetworking.patch(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "network": t.string().optional(),
                "reservedPeeringRanges": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesConnectionsPatch"] = servicenetworking.patch(
        "v1/{name}",
        t.struct(
            {
                "force": t.boolean().optional(),
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "network": t.string().optional(),
                "reservedPeeringRanges": t.array(t.string()).optional(),
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
                "consumerNetwork": t.string(),
                "name": t.string(),
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
                "consumerNetwork": t.string(),
                "name": t.string(),
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
        "v1/{parent}/dnsRecordSets:remove",
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
    functions["servicesDnsRecordSetsRemove"] = servicenetworking.post(
        "v1/{parent}/dnsRecordSets:remove",
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
        "servicesProjectsGlobalNetworksPeeredDnsDomainsDelete"
    ] = servicenetworking.post(
        "v1/{parent}/peeredDnsDomains",
        t.struct(
            {
                "parent": t.string(),
                "dnsSuffix": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksPeeredDnsDomainsList"
    ] = servicenetworking.post(
        "v1/{parent}/peeredDnsDomains",
        t.struct(
            {
                "parent": t.string(),
                "dnsSuffix": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "servicesProjectsGlobalNetworksPeeredDnsDomainsCreate"
    ] = servicenetworking.post(
        "v1/{parent}/peeredDnsDomains",
        t.struct(
            {
                "parent": t.string(),
                "dnsSuffix": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = servicenetworking.post(
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
    functions["operationsList"] = servicenetworking.post(
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
    functions["operationsGet"] = servicenetworking.post(
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
    functions["operationsCancel"] = servicenetworking.post(
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
        importer="servicenetworking",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
