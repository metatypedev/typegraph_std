from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_servicenetworking() -> Import:
    servicenetworking = HTTPRuntime("https://servicenetworking.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicenetworking_1_ErrorResponse",
        "BackendRuleIn": "_servicenetworking_2_BackendRuleIn",
        "BackendRuleOut": "_servicenetworking_3_BackendRuleOut",
        "RemoveDnsZoneResponseIn": "_servicenetworking_4_RemoveDnsZoneResponseIn",
        "RemoveDnsZoneResponseOut": "_servicenetworking_5_RemoveDnsZoneResponseOut",
        "EnumIn": "_servicenetworking_6_EnumIn",
        "EnumOut": "_servicenetworking_7_EnumOut",
        "DnsRecordSetIn": "_servicenetworking_8_DnsRecordSetIn",
        "DnsRecordSetOut": "_servicenetworking_9_DnsRecordSetOut",
        "ConsumerConfigIn": "_servicenetworking_10_ConsumerConfigIn",
        "ConsumerConfigOut": "_servicenetworking_11_ConsumerConfigOut",
        "ApiIn": "_servicenetworking_12_ApiIn",
        "ApiOut": "_servicenetworking_13_ApiOut",
        "EnableVpcServiceControlsRequestIn": "_servicenetworking_14_EnableVpcServiceControlsRequestIn",
        "EnableVpcServiceControlsRequestOut": "_servicenetworking_15_EnableVpcServiceControlsRequestOut",
        "ServiceIn": "_servicenetworking_16_ServiceIn",
        "ServiceOut": "_servicenetworking_17_ServiceOut",
        "MixinIn": "_servicenetworking_18_MixinIn",
        "MixinOut": "_servicenetworking_19_MixinOut",
        "PeeredDnsDomainIn": "_servicenetworking_20_PeeredDnsDomainIn",
        "PeeredDnsDomainOut": "_servicenetworking_21_PeeredDnsDomainOut",
        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn": "_servicenetworking_22_GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn",
        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut": "_servicenetworking_23_GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut",
        "EndpointIn": "_servicenetworking_24_EndpointIn",
        "EndpointOut": "_servicenetworking_25_EndpointOut",
        "MethodSettingsIn": "_servicenetworking_26_MethodSettingsIn",
        "MethodSettingsOut": "_servicenetworking_27_MethodSettingsOut",
        "LoggingIn": "_servicenetworking_28_LoggingIn",
        "LoggingOut": "_servicenetworking_29_LoggingOut",
        "RangeReservationIn": "_servicenetworking_30_RangeReservationIn",
        "RangeReservationOut": "_servicenetworking_31_RangeReservationOut",
        "AddSubnetworkRequestIn": "_servicenetworking_32_AddSubnetworkRequestIn",
        "AddSubnetworkRequestOut": "_servicenetworking_33_AddSubnetworkRequestOut",
        "JwtLocationIn": "_servicenetworking_34_JwtLocationIn",
        "JwtLocationOut": "_servicenetworking_35_JwtLocationOut",
        "AddDnsZoneResponseIn": "_servicenetworking_36_AddDnsZoneResponseIn",
        "AddDnsZoneResponseOut": "_servicenetworking_37_AddDnsZoneResponseOut",
        "MonitoringIn": "_servicenetworking_38_MonitoringIn",
        "MonitoringOut": "_servicenetworking_39_MonitoringOut",
        "LabelDescriptorIn": "_servicenetworking_40_LabelDescriptorIn",
        "LabelDescriptorOut": "_servicenetworking_41_LabelDescriptorOut",
        "ListConnectionsResponseIn": "_servicenetworking_42_ListConnectionsResponseIn",
        "ListConnectionsResponseOut": "_servicenetworking_43_ListConnectionsResponseOut",
        "UpdateConsumerConfigRequestIn": "_servicenetworking_44_UpdateConsumerConfigRequestIn",
        "UpdateConsumerConfigRequestOut": "_servicenetworking_45_UpdateConsumerConfigRequestOut",
        "UpdateDnsRecordSetRequestIn": "_servicenetworking_46_UpdateDnsRecordSetRequestIn",
        "UpdateDnsRecordSetRequestOut": "_servicenetworking_47_UpdateDnsRecordSetRequestOut",
        "DocumentationIn": "_servicenetworking_48_DocumentationIn",
        "DocumentationOut": "_servicenetworking_49_DocumentationOut",
        "NodeSettingsIn": "_servicenetworking_50_NodeSettingsIn",
        "NodeSettingsOut": "_servicenetworking_51_NodeSettingsOut",
        "BillingDestinationIn": "_servicenetworking_52_BillingDestinationIn",
        "BillingDestinationOut": "_servicenetworking_53_BillingDestinationOut",
        "AuthRequirementIn": "_servicenetworking_54_AuthRequirementIn",
        "AuthRequirementOut": "_servicenetworking_55_AuthRequirementOut",
        "StatusIn": "_servicenetworking_56_StatusIn",
        "StatusOut": "_servicenetworking_57_StatusOut",
        "SystemParameterRuleIn": "_servicenetworking_58_SystemParameterRuleIn",
        "SystemParameterRuleOut": "_servicenetworking_59_SystemParameterRuleOut",
        "DisableVpcServiceControlsRequestIn": "_servicenetworking_60_DisableVpcServiceControlsRequestIn",
        "DisableVpcServiceControlsRequestOut": "_servicenetworking_61_DisableVpcServiceControlsRequestOut",
        "MonitoredResourceDescriptorIn": "_servicenetworking_62_MonitoredResourceDescriptorIn",
        "MonitoredResourceDescriptorOut": "_servicenetworking_63_MonitoredResourceDescriptorOut",
        "ValidateConsumerConfigResponseIn": "_servicenetworking_64_ValidateConsumerConfigResponseIn",
        "ValidateConsumerConfigResponseOut": "_servicenetworking_65_ValidateConsumerConfigResponseOut",
        "MetricDescriptorIn": "_servicenetworking_66_MetricDescriptorIn",
        "MetricDescriptorOut": "_servicenetworking_67_MetricDescriptorOut",
        "SubnetworkIn": "_servicenetworking_68_SubnetworkIn",
        "SubnetworkOut": "_servicenetworking_69_SubnetworkOut",
        "MethodIn": "_servicenetworking_70_MethodIn",
        "MethodOut": "_servicenetworking_71_MethodOut",
        "AddRolesMetadataIn": "_servicenetworking_72_AddRolesMetadataIn",
        "AddRolesMetadataOut": "_servicenetworking_73_AddRolesMetadataOut",
        "LongRunningIn": "_servicenetworking_74_LongRunningIn",
        "LongRunningOut": "_servicenetworking_75_LongRunningOut",
        "CustomErrorIn": "_servicenetworking_76_CustomErrorIn",
        "CustomErrorOut": "_servicenetworking_77_CustomErrorOut",
        "CustomHttpPatternIn": "_servicenetworking_78_CustomHttpPatternIn",
        "CustomHttpPatternOut": "_servicenetworking_79_CustomHttpPatternOut",
        "MetricDescriptorMetadataIn": "_servicenetworking_80_MetricDescriptorMetadataIn",
        "MetricDescriptorMetadataOut": "_servicenetworking_81_MetricDescriptorMetadataOut",
        "PythonSettingsIn": "_servicenetworking_82_PythonSettingsIn",
        "PythonSettingsOut": "_servicenetworking_83_PythonSettingsOut",
        "RangeIn": "_servicenetworking_84_RangeIn",
        "RangeOut": "_servicenetworking_85_RangeOut",
        "CancelOperationRequestIn": "_servicenetworking_86_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_servicenetworking_87_CancelOperationRequestOut",
        "QuotaIn": "_servicenetworking_88_QuotaIn",
        "QuotaOut": "_servicenetworking_89_QuotaOut",
        "UsageIn": "_servicenetworking_90_UsageIn",
        "UsageOut": "_servicenetworking_91_UsageOut",
        "SourceInfoIn": "_servicenetworking_92_SourceInfoIn",
        "SourceInfoOut": "_servicenetworking_93_SourceInfoOut",
        "PartialDeleteConnectionMetadataIn": "_servicenetworking_94_PartialDeleteConnectionMetadataIn",
        "PartialDeleteConnectionMetadataOut": "_servicenetworking_95_PartialDeleteConnectionMetadataOut",
        "LogDescriptorIn": "_servicenetworking_96_LogDescriptorIn",
        "LogDescriptorOut": "_servicenetworking_97_LogDescriptorOut",
        "PageIn": "_servicenetworking_98_PageIn",
        "PageOut": "_servicenetworking_99_PageOut",
        "CppSettingsIn": "_servicenetworking_100_CppSettingsIn",
        "CppSettingsOut": "_servicenetworking_101_CppSettingsOut",
        "SourceContextIn": "_servicenetworking_102_SourceContextIn",
        "SourceContextOut": "_servicenetworking_103_SourceContextOut",
        "AddDnsRecordSetMetadataIn": "_servicenetworking_104_AddDnsRecordSetMetadataIn",
        "AddDnsRecordSetMetadataOut": "_servicenetworking_105_AddDnsRecordSetMetadataOut",
        "CustomErrorRuleIn": "_servicenetworking_106_CustomErrorRuleIn",
        "CustomErrorRuleOut": "_servicenetworking_107_CustomErrorRuleOut",
        "RemoveDnsZoneRequestIn": "_servicenetworking_108_RemoveDnsZoneRequestIn",
        "RemoveDnsZoneRequestOut": "_servicenetworking_109_RemoveDnsZoneRequestOut",
        "AddRolesRequestIn": "_servicenetworking_110_AddRolesRequestIn",
        "AddRolesRequestOut": "_servicenetworking_111_AddRolesRequestOut",
        "GoogleCloudServicenetworkingV1betaSubnetworkIn": "_servicenetworking_112_GoogleCloudServicenetworkingV1betaSubnetworkIn",
        "GoogleCloudServicenetworkingV1betaSubnetworkOut": "_servicenetworking_113_GoogleCloudServicenetworkingV1betaSubnetworkOut",
        "RubySettingsIn": "_servicenetworking_114_RubySettingsIn",
        "RubySettingsOut": "_servicenetworking_115_RubySettingsOut",
        "SecondaryIpRangeSpecIn": "_servicenetworking_116_SecondaryIpRangeSpecIn",
        "SecondaryIpRangeSpecOut": "_servicenetworking_117_SecondaryIpRangeSpecOut",
        "AuthenticationRuleIn": "_servicenetworking_118_AuthenticationRuleIn",
        "AuthenticationRuleOut": "_servicenetworking_119_AuthenticationRuleOut",
        "RouteIn": "_servicenetworking_120_RouteIn",
        "RouteOut": "_servicenetworking_121_RouteOut",
        "OAuthRequirementsIn": "_servicenetworking_122_OAuthRequirementsIn",
        "OAuthRequirementsOut": "_servicenetworking_123_OAuthRequirementsOut",
        "RemoveDnsRecordSetRequestIn": "_servicenetworking_124_RemoveDnsRecordSetRequestIn",
        "RemoveDnsRecordSetRequestOut": "_servicenetworking_125_RemoveDnsRecordSetRequestOut",
        "ContextIn": "_servicenetworking_126_ContextIn",
        "ContextOut": "_servicenetworking_127_ContextOut",
        "PublishingIn": "_servicenetworking_128_PublishingIn",
        "PublishingOut": "_servicenetworking_129_PublishingOut",
        "AddDnsRecordSetRequestIn": "_servicenetworking_130_AddDnsRecordSetRequestIn",
        "AddDnsRecordSetRequestOut": "_servicenetworking_131_AddDnsRecordSetRequestOut",
        "SearchRangeRequestIn": "_servicenetworking_132_SearchRangeRequestIn",
        "SearchRangeRequestOut": "_servicenetworking_133_SearchRangeRequestOut",
        "FieldIn": "_servicenetworking_134_FieldIn",
        "FieldOut": "_servicenetworking_135_FieldOut",
        "RemoveDnsRecordSetResponseIn": "_servicenetworking_136_RemoveDnsRecordSetResponseIn",
        "RemoveDnsRecordSetResponseOut": "_servicenetworking_137_RemoveDnsRecordSetResponseOut",
        "ConnectionIn": "_servicenetworking_138_ConnectionIn",
        "ConnectionOut": "_servicenetworking_139_ConnectionOut",
        "ContextRuleIn": "_servicenetworking_140_ContextRuleIn",
        "ContextRuleOut": "_servicenetworking_141_ContextRuleOut",
        "UpdateDnsRecordSetMetadataIn": "_servicenetworking_142_UpdateDnsRecordSetMetadataIn",
        "UpdateDnsRecordSetMetadataOut": "_servicenetworking_143_UpdateDnsRecordSetMetadataOut",
        "ListPeeredDnsDomainsResponseIn": "_servicenetworking_144_ListPeeredDnsDomainsResponseIn",
        "ListPeeredDnsDomainsResponseOut": "_servicenetworking_145_ListPeeredDnsDomainsResponseOut",
        "CommonLanguageSettingsIn": "_servicenetworking_146_CommonLanguageSettingsIn",
        "CommonLanguageSettingsOut": "_servicenetworking_147_CommonLanguageSettingsOut",
        "ValidateConsumerConfigRequestIn": "_servicenetworking_148_ValidateConsumerConfigRequestIn",
        "ValidateConsumerConfigRequestOut": "_servicenetworking_149_ValidateConsumerConfigRequestOut",
        "LoggingDestinationIn": "_servicenetworking_150_LoggingDestinationIn",
        "LoggingDestinationOut": "_servicenetworking_151_LoggingDestinationOut",
        "BillingIn": "_servicenetworking_152_BillingIn",
        "BillingOut": "_servicenetworking_153_BillingOut",
        "DeletePeeredDnsDomainMetadataIn": "_servicenetworking_154_DeletePeeredDnsDomainMetadataIn",
        "DeletePeeredDnsDomainMetadataOut": "_servicenetworking_155_DeletePeeredDnsDomainMetadataOut",
        "SystemParametersIn": "_servicenetworking_156_SystemParametersIn",
        "SystemParametersOut": "_servicenetworking_157_SystemParametersOut",
        "HttpRuleIn": "_servicenetworking_158_HttpRuleIn",
        "HttpRuleOut": "_servicenetworking_159_HttpRuleOut",
        "ConsumerConfigMetadataIn": "_servicenetworking_160_ConsumerConfigMetadataIn",
        "ConsumerConfigMetadataOut": "_servicenetworking_161_ConsumerConfigMetadataOut",
        "QuotaLimitIn": "_servicenetworking_162_QuotaLimitIn",
        "QuotaLimitOut": "_servicenetworking_163_QuotaLimitOut",
        "JavaSettingsIn": "_servicenetworking_164_JavaSettingsIn",
        "JavaSettingsOut": "_servicenetworking_165_JavaSettingsOut",
        "ConsumerProjectIn": "_servicenetworking_166_ConsumerProjectIn",
        "ConsumerProjectOut": "_servicenetworking_167_ConsumerProjectOut",
        "DeleteConnectionRequestIn": "_servicenetworking_168_DeleteConnectionRequestIn",
        "DeleteConnectionRequestOut": "_servicenetworking_169_DeleteConnectionRequestOut",
        "AddRolesResponseIn": "_servicenetworking_170_AddRolesResponseIn",
        "AddRolesResponseOut": "_servicenetworking_171_AddRolesResponseOut",
        "AddDnsZoneRequestIn": "_servicenetworking_172_AddDnsZoneRequestIn",
        "AddDnsZoneRequestOut": "_servicenetworking_173_AddDnsZoneRequestOut",
        "EnumValueIn": "_servicenetworking_174_EnumValueIn",
        "EnumValueOut": "_servicenetworking_175_EnumValueOut",
        "DeleteConnectionMetadataIn": "_servicenetworking_176_DeleteConnectionMetadataIn",
        "DeleteConnectionMetadataOut": "_servicenetworking_177_DeleteConnectionMetadataOut",
        "AuthProviderIn": "_servicenetworking_178_AuthProviderIn",
        "AuthProviderOut": "_servicenetworking_179_AuthProviderOut",
        "PeeredDnsDomainMetadataIn": "_servicenetworking_180_PeeredDnsDomainMetadataIn",
        "PeeredDnsDomainMetadataOut": "_servicenetworking_181_PeeredDnsDomainMetadataOut",
        "AddDnsZoneMetadataIn": "_servicenetworking_182_AddDnsZoneMetadataIn",
        "AddDnsZoneMetadataOut": "_servicenetworking_183_AddDnsZoneMetadataOut",
        "OptionIn": "_servicenetworking_184_OptionIn",
        "OptionOut": "_servicenetworking_185_OptionOut",
        "MonitoringDestinationIn": "_servicenetworking_186_MonitoringDestinationIn",
        "MonitoringDestinationOut": "_servicenetworking_187_MonitoringDestinationOut",
        "MetricRuleIn": "_servicenetworking_188_MetricRuleIn",
        "MetricRuleOut": "_servicenetworking_189_MetricRuleOut",
        "TypeIn": "_servicenetworking_190_TypeIn",
        "TypeOut": "_servicenetworking_191_TypeOut",
        "DocumentationRuleIn": "_servicenetworking_192_DocumentationRuleIn",
        "DocumentationRuleOut": "_servicenetworking_193_DocumentationRuleOut",
        "GoSettingsIn": "_servicenetworking_194_GoSettingsIn",
        "GoSettingsOut": "_servicenetworking_195_GoSettingsOut",
        "SystemParameterIn": "_servicenetworking_196_SystemParameterIn",
        "SystemParameterOut": "_servicenetworking_197_SystemParameterOut",
        "AuthenticationIn": "_servicenetworking_198_AuthenticationIn",
        "AuthenticationOut": "_servicenetworking_199_AuthenticationOut",
        "ClientLibrarySettingsIn": "_servicenetworking_200_ClientLibrarySettingsIn",
        "ClientLibrarySettingsOut": "_servicenetworking_201_ClientLibrarySettingsOut",
        "ControlIn": "_servicenetworking_202_ControlIn",
        "ControlOut": "_servicenetworking_203_ControlOut",
        "ListOperationsResponseIn": "_servicenetworking_204_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_servicenetworking_205_ListOperationsResponseOut",
        "PhpSettingsIn": "_servicenetworking_206_PhpSettingsIn",
        "PhpSettingsOut": "_servicenetworking_207_PhpSettingsOut",
        "UsageRuleIn": "_servicenetworking_208_UsageRuleIn",
        "UsageRuleOut": "_servicenetworking_209_UsageRuleOut",
        "DotnetSettingsIn": "_servicenetworking_210_DotnetSettingsIn",
        "DotnetSettingsOut": "_servicenetworking_211_DotnetSettingsOut",
        "DnsZoneIn": "_servicenetworking_212_DnsZoneIn",
        "DnsZoneOut": "_servicenetworking_213_DnsZoneOut",
        "GoogleCloudServicenetworkingV1betaConnectionIn": "_servicenetworking_214_GoogleCloudServicenetworkingV1betaConnectionIn",
        "GoogleCloudServicenetworkingV1betaConnectionOut": "_servicenetworking_215_GoogleCloudServicenetworkingV1betaConnectionOut",
        "OperationIn": "_servicenetworking_216_OperationIn",
        "OperationOut": "_servicenetworking_217_OperationOut",
        "RemoveDnsZoneMetadataIn": "_servicenetworking_218_RemoveDnsZoneMetadataIn",
        "RemoveDnsZoneMetadataOut": "_servicenetworking_219_RemoveDnsZoneMetadataOut",
        "PolicyBindingIn": "_servicenetworking_220_PolicyBindingIn",
        "PolicyBindingOut": "_servicenetworking_221_PolicyBindingOut",
        "HttpIn": "_servicenetworking_222_HttpIn",
        "HttpOut": "_servicenetworking_223_HttpOut",
        "BackendIn": "_servicenetworking_224_BackendIn",
        "BackendOut": "_servicenetworking_225_BackendOut",
        "EmptyIn": "_servicenetworking_226_EmptyIn",
        "EmptyOut": "_servicenetworking_227_EmptyOut",
        "CloudSQLConfigIn": "_servicenetworking_228_CloudSQLConfigIn",
        "CloudSQLConfigOut": "_servicenetworking_229_CloudSQLConfigOut",
        "SecondaryIpRangeIn": "_servicenetworking_230_SecondaryIpRangeIn",
        "SecondaryIpRangeOut": "_servicenetworking_231_SecondaryIpRangeOut",
        "RemoveDnsRecordSetMetadataIn": "_servicenetworking_232_RemoveDnsRecordSetMetadataIn",
        "RemoveDnsRecordSetMetadataOut": "_servicenetworking_233_RemoveDnsRecordSetMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BackendRuleIn"] = t.struct(
        {
            "selector": t.string().optional(),
            "jwtAudience": t.string().optional(),
            "pathTranslation": t.string(),
            "address": t.string().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "protocol": t.string().optional(),
            "operationDeadline": t.number().optional(),
        }
    ).named(renames["BackendRuleIn"])
    types["BackendRuleOut"] = t.struct(
        {
            "selector": t.string().optional(),
            "jwtAudience": t.string().optional(),
            "pathTranslation": t.string(),
            "address": t.string().optional(),
            "deadline": t.number().optional(),
            "minDeadline": t.number().optional(),
            "disableAuth": t.boolean().optional(),
            "overridesByRequestProtocol": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "protocol": t.string().optional(),
            "operationDeadline": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendRuleOut"])
    types["RemoveDnsZoneResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveDnsZoneResponseIn"]
    )
    types["RemoveDnsZoneResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsZoneResponseOut"])
    types["EnumIn"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueIn"])).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "edition": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EnumIn"])
    types["EnumOut"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "enumvalue": t.array(t.proxy(renames["EnumValueOut"])).optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "edition": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnumOut"])
    types["DnsRecordSetIn"] = t.struct(
        {
            "data": t.array(t.string()),
            "domain": t.string(),
            "type": t.string(),
            "ttl": t.string(),
        }
    ).named(renames["DnsRecordSetIn"])
    types["DnsRecordSetOut"] = t.struct(
        {
            "data": t.array(t.string()),
            "domain": t.string(),
            "type": t.string(),
            "ttl": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsRecordSetOut"])
    types["ConsumerConfigIn"] = t.struct(
        {
            "producerImportCustomRoutes": t.boolean().optional(),
            "producerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportCustomRoutes": t.boolean().optional(),
            "producerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "consumerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "cloudsqlConfigs": t.array(t.proxy(renames["CloudSQLConfigIn"])).optional(),
            "consumerExportCustomRoutes": t.boolean().optional(),
            "consumerImportCustomRoutes": t.boolean().optional(),
            "consumerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
        }
    ).named(renames["ConsumerConfigIn"])
    types["ConsumerConfigOut"] = t.struct(
        {
            "producerImportCustomRoutes": t.boolean().optional(),
            "producerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerExportCustomRoutes": t.boolean().optional(),
            "producerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "consumerExportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "usedIpRanges": t.array(t.string()).optional(),
            "cloudsqlConfigs": t.array(
                t.proxy(renames["CloudSQLConfigOut"])
            ).optional(),
            "reservedRanges": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"
                    ]
                )
            ).optional(),
            "consumerExportCustomRoutes": t.boolean().optional(),
            "consumerImportCustomRoutes": t.boolean().optional(),
            "consumerImportSubnetRoutesWithPublicIp": t.boolean().optional(),
            "producerNetwork": t.string().optional(),
            "vpcScReferenceArchitectureEnabled": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerConfigOut"])
    types["ApiIn"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "version": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinIn"])).optional(),
            "methods": t.array(t.proxy(renames["MethodIn"])).optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "version": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "mixins": t.array(t.proxy(renames["MixinOut"])).optional(),
            "methods": t.array(t.proxy(renames["MethodOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["EnableVpcServiceControlsRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["EnableVpcServiceControlsRequestIn"])
    types["EnableVpcServiceControlsRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EnableVpcServiceControlsRequestOut"])
    types["ServiceIn"] = t.struct(
        {
            "authentication": t.proxy(renames["AuthenticationIn"]).optional(),
            "configVersion": t.integer().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointIn"])).optional(),
            "documentation": t.proxy(renames["DocumentationIn"]).optional(),
            "enums": t.array(t.proxy(renames["EnumIn"])).optional(),
            "apis": t.array(t.proxy(renames["ApiIn"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersIn"]).optional(),
            "backend": t.proxy(renames["BackendIn"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorIn"])).optional(),
            "title": t.string().optional(),
            "billing": t.proxy(renames["BillingIn"]).optional(),
            "http": t.proxy(renames["HttpIn"]).optional(),
            "logging": t.proxy(renames["LoggingIn"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorIn"])
            ).optional(),
            "control": t.proxy(renames["ControlIn"]).optional(),
            "publishing": t.proxy(renames["PublishingIn"]).optional(),
            "customError": t.proxy(renames["CustomErrorIn"]).optional(),
            "quota": t.proxy(renames["QuotaIn"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeIn"])).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorIn"])).optional(),
            "producerProjectId": t.string().optional(),
            "usage": t.proxy(renames["UsageIn"]).optional(),
            "types": t.array(t.proxy(renames["TypeIn"])).optional(),
            "name": t.string().optional(),
            "monitoring": t.proxy(renames["MonitoringIn"]).optional(),
            "context": t.proxy(renames["ContextIn"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "authentication": t.proxy(renames["AuthenticationOut"]).optional(),
            "configVersion": t.integer().optional(),
            "endpoints": t.array(t.proxy(renames["EndpointOut"])).optional(),
            "documentation": t.proxy(renames["DocumentationOut"]).optional(),
            "enums": t.array(t.proxy(renames["EnumOut"])).optional(),
            "apis": t.array(t.proxy(renames["ApiOut"])).optional(),
            "systemParameters": t.proxy(renames["SystemParametersOut"]).optional(),
            "backend": t.proxy(renames["BackendOut"]).optional(),
            "metrics": t.array(t.proxy(renames["MetricDescriptorOut"])).optional(),
            "title": t.string().optional(),
            "billing": t.proxy(renames["BillingOut"]).optional(),
            "http": t.proxy(renames["HttpOut"]).optional(),
            "logging": t.proxy(renames["LoggingOut"]).optional(),
            "monitoredResources": t.array(
                t.proxy(renames["MonitoredResourceDescriptorOut"])
            ).optional(),
            "control": t.proxy(renames["ControlOut"]).optional(),
            "publishing": t.proxy(renames["PublishingOut"]).optional(),
            "customError": t.proxy(renames["CustomErrorOut"]).optional(),
            "quota": t.proxy(renames["QuotaOut"]).optional(),
            "systemTypes": t.array(t.proxy(renames["TypeOut"])).optional(),
            "logs": t.array(t.proxy(renames["LogDescriptorOut"])).optional(),
            "producerProjectId": t.string().optional(),
            "usage": t.proxy(renames["UsageOut"]).optional(),
            "types": t.array(t.proxy(renames["TypeOut"])).optional(),
            "name": t.string().optional(),
            "monitoring": t.proxy(renames["MonitoringOut"]).optional(),
            "context": t.proxy(renames["ContextOut"]).optional(),
            "sourceInfo": t.proxy(renames["SourceInfoOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
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
    types["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn"] = t.struct(
        {
            "ipPrefixLength": t.integer().optional(),
            "address": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeIn"])
    types["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"] = t.struct(
        {
            "ipPrefixLength": t.integer().optional(),
            "address": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1ConsumerConfigReservedRangeOut"])
    types["EndpointIn"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["EndpointIn"])
    types["EndpointOut"] = t.struct(
        {
            "aliases": t.array(t.string()).optional(),
            "target": t.string().optional(),
            "allowCors": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointOut"])
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
    types["RangeReservationIn"] = t.struct(
        {
            "ipPrefixLength": t.integer(),
            "secondaryRangeIpPrefixLengths": t.array(t.integer()).optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "subnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkIn"])
            ).optional(),
        }
    ).named(renames["RangeReservationIn"])
    types["RangeReservationOut"] = t.struct(
        {
            "ipPrefixLength": t.integer(),
            "secondaryRangeIpPrefixLengths": t.array(t.integer()).optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "subnetworkCandidates": t.array(
                t.proxy(renames["SubnetworkOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RangeReservationOut"])
    types["AddSubnetworkRequestIn"] = t.struct(
        {
            "useCustomComputeIdempotencyWindow": t.boolean().optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerNetwork": t.string(),
            "subnetworkUsers": t.array(t.string()).optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "purpose": t.string().optional(),
            "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
            "region": t.string(),
            "ipPrefixLength": t.integer(),
            "secondaryIpRangeSpecs": t.array(
                t.proxy(renames["SecondaryIpRangeSpecIn"])
            ).optional(),
            "subnetwork": t.string(),
            "requestedAddress": t.string().optional(),
            "consumer": t.string(),
            "role": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "computeIdempotencyWindow": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["AddSubnetworkRequestIn"])
    types["AddSubnetworkRequestOut"] = t.struct(
        {
            "useCustomComputeIdempotencyWindow": t.boolean().optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerNetwork": t.string(),
            "subnetworkUsers": t.array(t.string()).optional(),
            "requestedRanges": t.array(t.string()).optional(),
            "purpose": t.string().optional(),
            "allowSubnetCidrRoutesOverlap": t.boolean().optional(),
            "region": t.string(),
            "ipPrefixLength": t.integer(),
            "secondaryIpRangeSpecs": t.array(
                t.proxy(renames["SecondaryIpRangeSpecOut"])
            ).optional(),
            "subnetwork": t.string(),
            "requestedAddress": t.string().optional(),
            "consumer": t.string(),
            "role": t.string().optional(),
            "privateIpv6GoogleAccess": t.string().optional(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "computeIdempotencyWindow": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddSubnetworkRequestOut"])
    types["JwtLocationIn"] = t.struct(
        {
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "query": t.string().optional(),
            "cookie": t.string().optional(),
        }
    ).named(renames["JwtLocationIn"])
    types["JwtLocationOut"] = t.struct(
        {
            "header": t.string().optional(),
            "valuePrefix": t.string().optional(),
            "query": t.string().optional(),
            "cookie": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtLocationOut"])
    types["AddDnsZoneResponseIn"] = t.struct(
        {
            "producerPrivateZone": t.proxy(renames["DnsZoneIn"]).optional(),
            "consumerPeeringZone": t.proxy(renames["DnsZoneIn"]).optional(),
        }
    ).named(renames["AddDnsZoneResponseIn"])
    types["AddDnsZoneResponseOut"] = t.struct(
        {
            "producerPrivateZone": t.proxy(renames["DnsZoneOut"]).optional(),
            "consumerPeeringZone": t.proxy(renames["DnsZoneOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddDnsZoneResponseOut"])
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
    types["ListConnectionsResponseIn"] = t.struct(
        {"connections": t.array(t.proxy(renames["ConnectionIn"])).optional()}
    ).named(renames["ListConnectionsResponseIn"])
    types["ListConnectionsResponseOut"] = t.struct(
        {
            "connections": t.array(t.proxy(renames["ConnectionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListConnectionsResponseOut"])
    types["UpdateConsumerConfigRequestIn"] = t.struct(
        {"consumerConfig": t.proxy(renames["ConsumerConfigIn"])}
    ).named(renames["UpdateConsumerConfigRequestIn"])
    types["UpdateConsumerConfigRequestOut"] = t.struct(
        {
            "consumerConfig": t.proxy(renames["ConsumerConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateConsumerConfigRequestOut"])
    types["UpdateDnsRecordSetRequestIn"] = t.struct(
        {
            "existingDnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "consumerNetwork": t.string(),
            "newDnsRecordSet": t.proxy(renames["DnsRecordSetIn"]),
            "zone": t.string(),
        }
    ).named(renames["UpdateDnsRecordSetRequestIn"])
    types["UpdateDnsRecordSetRequestOut"] = t.struct(
        {
            "existingDnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "consumerNetwork": t.string(),
            "newDnsRecordSet": t.proxy(renames["DnsRecordSetOut"]),
            "zone": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateDnsRecordSetRequestOut"])
    types["DocumentationIn"] = t.struct(
        {
            "documentationRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageIn"])).optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleIn"])).optional(),
            "summary": t.string().optional(),
            "overview": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
        }
    ).named(renames["DocumentationIn"])
    types["DocumentationOut"] = t.struct(
        {
            "documentationRootUrl": t.string().optional(),
            "pages": t.array(t.proxy(renames["PageOut"])).optional(),
            "rules": t.array(t.proxy(renames["DocumentationRuleOut"])).optional(),
            "summary": t.string().optional(),
            "overview": t.string().optional(),
            "serviceRootUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationOut"])
    types["NodeSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["NodeSettingsIn"])
    types["NodeSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeSettingsOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
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
    types["DisableVpcServiceControlsRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["DisableVpcServiceControlsRequestIn"])
    types["DisableVpcServiceControlsRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DisableVpcServiceControlsRequestOut"])
    types["MonitoredResourceDescriptorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])),
            "type": t.string(),
            "launchStage": t.string().optional(),
        }
    ).named(renames["MonitoredResourceDescriptorIn"])
    types["MonitoredResourceDescriptorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])),
            "type": t.string(),
            "launchStage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MonitoredResourceDescriptorOut"])
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
    types["MetricDescriptorIn"] = t.struct(
        {
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
            "valueType": t.string().optional(),
            "unit": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataIn"]).optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorIn"])).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MetricDescriptorIn"])
    types["MetricDescriptorOut"] = t.struct(
        {
            "type": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "monitoredResourceTypes": t.array(t.string()).optional(),
            "metricKind": t.string().optional(),
            "launchStage": t.string().optional(),
            "valueType": t.string().optional(),
            "unit": t.string().optional(),
            "metadata": t.proxy(renames["MetricDescriptorMetadataOut"]).optional(),
            "labels": t.array(t.proxy(renames["LabelDescriptorOut"])).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MetricDescriptorOut"])
    types["SubnetworkIn"] = t.struct(
        {
            "region": t.string().optional(),
            "network": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["SecondaryIpRangeIn"])
            ).optional(),
            "name": t.string().optional(),
            "ipCidrRange": t.string().optional(),
        }
    ).named(renames["SubnetworkIn"])
    types["SubnetworkOut"] = t.struct(
        {
            "region": t.string().optional(),
            "network": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "secondaryIpRanges": t.array(
                t.proxy(renames["SecondaryIpRangeOut"])
            ).optional(),
            "name": t.string().optional(),
            "ipCidrRange": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubnetworkOut"])
    types["MethodIn"] = t.struct(
        {
            "responseStreaming": t.boolean().optional(),
            "requestStreaming": t.boolean().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "requestTypeUrl": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["MethodIn"])
    types["MethodOut"] = t.struct(
        {
            "responseStreaming": t.boolean().optional(),
            "requestStreaming": t.boolean().optional(),
            "syntax": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "requestTypeUrl": t.string().optional(),
            "responseTypeUrl": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodOut"])
    types["AddRolesMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddRolesMetadataIn"]
    )
    types["AddRolesMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddRolesMetadataOut"])
    types["LongRunningIn"] = t.struct(
        {
            "totalPollTimeout": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
        }
    ).named(renames["LongRunningIn"])
    types["LongRunningOut"] = t.struct(
        {
            "totalPollTimeout": t.string().optional(),
            "maxPollDelay": t.string().optional(),
            "initialPollDelay": t.string().optional(),
            "pollDelayMultiplier": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LongRunningOut"])
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
    types["PythonSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PythonSettingsIn"])
    types["PythonSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PythonSettingsOut"])
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
    types["SourceInfoIn"] = t.struct(
        {"sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional()}
    ).named(renames["SourceInfoIn"])
    types["SourceInfoOut"] = t.struct(
        {
            "sourceFiles": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceInfoOut"])
    types["PartialDeleteConnectionMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["PartialDeleteConnectionMetadataIn"])
    types["PartialDeleteConnectionMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PartialDeleteConnectionMetadataOut"])
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
    types["AddDnsRecordSetMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddDnsRecordSetMetadataIn"]
    )
    types["AddDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddDnsRecordSetMetadataOut"])
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
    types["GoogleCloudServicenetworkingV1betaSubnetworkIn"] = t.struct(
        {
            "name": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "ipCidrRange": t.string().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaSubnetworkIn"])
    types["GoogleCloudServicenetworkingV1betaSubnetworkOut"] = t.struct(
        {
            "name": t.string().optional(),
            "outsideAllocation": t.boolean().optional(),
            "ipCidrRange": t.string().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaSubnetworkOut"])
    types["RubySettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["RubySettingsIn"])
    types["RubySettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RubySettingsOut"])
    types["SecondaryIpRangeSpecIn"] = t.struct(
        {
            "ipPrefixLength": t.integer(),
            "rangeName": t.string(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "requestedAddress": t.string().optional(),
        }
    ).named(renames["SecondaryIpRangeSpecIn"])
    types["SecondaryIpRangeSpecOut"] = t.struct(
        {
            "ipPrefixLength": t.integer(),
            "rangeName": t.string(),
            "outsideAllocationPublicIpRange": t.string().optional(),
            "requestedAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SecondaryIpRangeSpecOut"])
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
    types["OAuthRequirementsIn"] = t.struct(
        {"canonicalScopes": t.string().optional()}
    ).named(renames["OAuthRequirementsIn"])
    types["OAuthRequirementsOut"] = t.struct(
        {
            "canonicalScopes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OAuthRequirementsOut"])
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
    types["ContextIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["ContextRuleIn"])).optional()}
    ).named(renames["ContextIn"])
    types["ContextOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["ContextRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextOut"])
    types["PublishingIn"] = t.struct(
        {
            "documentationUri": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsIn"])).optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsIn"])
            ).optional(),
            "githubLabel": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "apiShortName": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "docTagPrefix": t.string().optional(),
        }
    ).named(renames["PublishingIn"])
    types["PublishingOut"] = t.struct(
        {
            "documentationUri": t.string().optional(),
            "methodSettings": t.array(t.proxy(renames["MethodSettingsOut"])).optional(),
            "librarySettings": t.array(
                t.proxy(renames["ClientLibrarySettingsOut"])
            ).optional(),
            "githubLabel": t.string().optional(),
            "codeownerGithubTeams": t.array(t.string()).optional(),
            "apiShortName": t.string().optional(),
            "newIssueUri": t.string().optional(),
            "protoReferenceDocumentationUri": t.string().optional(),
            "organization": t.string().optional(),
            "docTagPrefix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PublishingOut"])
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
    types["SearchRangeRequestIn"] = t.struct(
        {"network": t.string().optional(), "ipPrefixLength": t.integer()}
    ).named(renames["SearchRangeRequestIn"])
    types["SearchRangeRequestOut"] = t.struct(
        {
            "network": t.string().optional(),
            "ipPrefixLength": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchRangeRequestOut"])
    types["FieldIn"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
            "number": t.integer().optional(),
            "typeUrl": t.string().optional(),
            "defaultValue": t.string().optional(),
            "cardinality": t.string().optional(),
            "kind": t.string().optional(),
            "packed": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "jsonName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["FieldIn"])
    types["FieldOut"] = t.struct(
        {
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "number": t.integer().optional(),
            "typeUrl": t.string().optional(),
            "defaultValue": t.string().optional(),
            "cardinality": t.string().optional(),
            "kind": t.string().optional(),
            "packed": t.boolean().optional(),
            "oneofIndex": t.integer().optional(),
            "jsonName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FieldOut"])
    types["RemoveDnsRecordSetResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RemoveDnsRecordSetResponseIn"])
    types["RemoveDnsRecordSetResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsRecordSetResponseOut"])
    types["ConnectionIn"] = t.struct(
        {
            "network": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
        }
    ).named(renames["ConnectionIn"])
    types["ConnectionOut"] = t.struct(
        {
            "network": t.string().optional(),
            "service": t.string().optional(),
            "peering": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConnectionOut"])
    types["ContextRuleIn"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
        }
    ).named(renames["ContextRuleIn"])
    types["ContextRuleOut"] = t.struct(
        {
            "allowedRequestExtensions": t.array(t.string()).optional(),
            "allowedResponseExtensions": t.array(t.string()).optional(),
            "selector": t.string().optional(),
            "provided": t.array(t.string()).optional(),
            "requested": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContextRuleOut"])
    types["UpdateDnsRecordSetMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UpdateDnsRecordSetMetadataIn"])
    types["UpdateDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateDnsRecordSetMetadataOut"])
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
    types["ValidateConsumerConfigRequestIn"] = t.struct(
        {
            "rangeReservation": t.proxy(renames["RangeReservationIn"]).optional(),
            "consumerNetwork": t.string(),
            "validateNetwork": t.boolean().optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerProject": t.proxy(renames["ConsumerProjectIn"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigRequestIn"])
    types["ValidateConsumerConfigRequestOut"] = t.struct(
        {
            "rangeReservation": t.proxy(renames["RangeReservationOut"]).optional(),
            "consumerNetwork": t.string(),
            "validateNetwork": t.boolean().optional(),
            "checkServiceNetworkingUsePermission": t.boolean().optional(),
            "consumerProject": t.proxy(renames["ConsumerProjectOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateConsumerConfigRequestOut"])
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
    types["DeletePeeredDnsDomainMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeletePeeredDnsDomainMetadataIn"])
    types["DeletePeeredDnsDomainMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeletePeeredDnsDomainMetadataOut"])
    types["SystemParametersIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["SystemParameterRuleIn"])).optional()}
    ).named(renames["SystemParametersIn"])
    types["SystemParametersOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["SystemParameterRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SystemParametersOut"])
    types["HttpRuleIn"] = t.struct(
        {
            "post": t.string().optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "responseBody": t.string().optional(),
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "body": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternIn"]).optional(),
            "delete": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleIn"])).optional(),
        }
    ).named(renames["HttpRuleIn"])
    types["HttpRuleOut"] = t.struct(
        {
            "post": t.string().optional(),
            "get": t.string().optional(),
            "put": t.string().optional(),
            "responseBody": t.string().optional(),
            "patch": t.string().optional(),
            "selector": t.string().optional(),
            "body": t.string().optional(),
            "custom": t.proxy(renames["CustomHttpPatternOut"]).optional(),
            "delete": t.string().optional(),
            "additionalBindings": t.array(t.proxy(renames["HttpRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HttpRuleOut"])
    types["ConsumerConfigMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ConsumerConfigMetadataIn"]
    )
    types["ConsumerConfigMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ConsumerConfigMetadataOut"])
    types["QuotaLimitIn"] = t.struct(
        {
            "metric": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "freeTier": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "duration": t.string().optional(),
            "unit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "maxLimit": t.string().optional(),
        }
    ).named(renames["QuotaLimitIn"])
    types["QuotaLimitOut"] = t.struct(
        {
            "metric": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "freeTier": t.string().optional(),
            "defaultLimit": t.string().optional(),
            "duration": t.string().optional(),
            "unit": t.string().optional(),
            "values": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "maxLimit": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QuotaLimitOut"])
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
    types["ConsumerProjectIn"] = t.struct({"projectNum": t.string()}).named(
        renames["ConsumerProjectIn"]
    )
    types["ConsumerProjectOut"] = t.struct(
        {
            "projectNum": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConsumerProjectOut"])
    types["DeleteConnectionRequestIn"] = t.struct(
        {"consumerNetwork": t.string()}
    ).named(renames["DeleteConnectionRequestIn"])
    types["DeleteConnectionRequestOut"] = t.struct(
        {
            "consumerNetwork": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeleteConnectionRequestOut"])
    types["AddRolesResponseIn"] = t.struct(
        {"policyBinding": t.array(t.proxy(renames["PolicyBindingIn"]))}
    ).named(renames["AddRolesResponseIn"])
    types["AddRolesResponseOut"] = t.struct(
        {
            "policyBinding": t.array(t.proxy(renames["PolicyBindingOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddRolesResponseOut"])
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
    types["DeleteConnectionMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteConnectionMetadataIn"]
    )
    types["DeleteConnectionMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteConnectionMetadataOut"])
    types["AuthProviderIn"] = t.struct(
        {
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "jwksUri": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationIn"])).optional(),
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
        }
    ).named(renames["AuthProviderIn"])
    types["AuthProviderOut"] = t.struct(
        {
            "id": t.string().optional(),
            "issuer": t.string().optional(),
            "jwksUri": t.string().optional(),
            "jwtLocations": t.array(t.proxy(renames["JwtLocationOut"])).optional(),
            "audiences": t.string().optional(),
            "authorizationUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthProviderOut"])
    types["PeeredDnsDomainMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PeeredDnsDomainMetadataIn"]
    )
    types["PeeredDnsDomainMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PeeredDnsDomainMetadataOut"])
    types["AddDnsZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddDnsZoneMetadataIn"]
    )
    types["AddDnsZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddDnsZoneMetadataOut"])
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
    types["TypeIn"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldIn"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "sourceContext": t.proxy(renames["SourceContextIn"]).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionIn"])).optional(),
        }
    ).named(renames["TypeIn"])
    types["TypeOut"] = t.struct(
        {
            "fields": t.array(t.proxy(renames["FieldOut"])).optional(),
            "oneofs": t.array(t.string()).optional(),
            "sourceContext": t.proxy(renames["SourceContextOut"]).optional(),
            "syntax": t.string().optional(),
            "name": t.string().optional(),
            "edition": t.string().optional(),
            "options": t.array(t.proxy(renames["OptionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TypeOut"])
    types["DocumentationRuleIn"] = t.struct(
        {
            "deprecationDescription": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "description": t.string().optional(),
            "selector": t.string().optional(),
        }
    ).named(renames["DocumentationRuleIn"])
    types["DocumentationRuleOut"] = t.struct(
        {
            "deprecationDescription": t.string().optional(),
            "disableReplacementWords": t.string().optional(),
            "description": t.string().optional(),
            "selector": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentationRuleOut"])
    types["GoSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["GoSettingsIn"])
    types["GoSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoSettingsOut"])
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
    types["ClientLibrarySettingsIn"] = t.struct(
        {
            "nodeSettings": t.proxy(renames["NodeSettingsIn"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsIn"]).optional(),
            "launchStage": t.string().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsIn"]).optional(),
            "version": t.string().optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsIn"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsIn"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsIn"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsIn"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsIn"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsIn"])
    types["ClientLibrarySettingsOut"] = t.struct(
        {
            "nodeSettings": t.proxy(renames["NodeSettingsOut"]).optional(),
            "restNumericEnums": t.boolean().optional(),
            "pythonSettings": t.proxy(renames["PythonSettingsOut"]).optional(),
            "launchStage": t.string().optional(),
            "javaSettings": t.proxy(renames["JavaSettingsOut"]).optional(),
            "version": t.string().optional(),
            "dotnetSettings": t.proxy(renames["DotnetSettingsOut"]).optional(),
            "phpSettings": t.proxy(renames["PhpSettingsOut"]).optional(),
            "goSettings": t.proxy(renames["GoSettingsOut"]).optional(),
            "cppSettings": t.proxy(renames["CppSettingsOut"]).optional(),
            "rubySettings": t.proxy(renames["RubySettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientLibrarySettingsOut"])
    types["ControlIn"] = t.struct({"environment": t.string().optional()}).named(
        renames["ControlIn"]
    )
    types["ControlOut"] = t.struct(
        {
            "environment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ControlOut"])
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
    types["PhpSettingsIn"] = t.struct(
        {"common": t.proxy(renames["CommonLanguageSettingsIn"]).optional()}
    ).named(renames["PhpSettingsIn"])
    types["PhpSettingsOut"] = t.struct(
        {
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PhpSettingsOut"])
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
    types["DotnetSettingsIn"] = t.struct(
        {
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsIn"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
        }
    ).named(renames["DotnetSettingsIn"])
    types["DotnetSettingsOut"] = t.struct(
        {
            "renamedServices": t.struct({"_": t.string().optional()}).optional(),
            "handwrittenSignatures": t.array(t.string()).optional(),
            "ignoredResources": t.array(t.string()).optional(),
            "common": t.proxy(renames["CommonLanguageSettingsOut"]).optional(),
            "renamedResources": t.struct({"_": t.string().optional()}).optional(),
            "forcedNamespaceAliases": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DotnetSettingsOut"])
    types["DnsZoneIn"] = t.struct(
        {"name": t.string().optional(), "dnsSuffix": t.string().optional()}
    ).named(renames["DnsZoneIn"])
    types["DnsZoneOut"] = t.struct(
        {
            "name": t.string().optional(),
            "dnsSuffix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsZoneOut"])
    types["GoogleCloudServicenetworkingV1betaConnectionIn"] = t.struct(
        {
            "peering": t.string().optional(),
            "network": t.string().optional(),
            "service": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaConnectionIn"])
    types["GoogleCloudServicenetworkingV1betaConnectionOut"] = t.struct(
        {
            "peering": t.string().optional(),
            "network": t.string().optional(),
            "service": t.string().optional(),
            "reservedPeeringRanges": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudServicenetworkingV1betaConnectionOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["RemoveDnsZoneMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveDnsZoneMetadataIn"]
    )
    types["RemoveDnsZoneMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsZoneMetadataOut"])
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
    types["BackendIn"] = t.struct(
        {"rules": t.array(t.proxy(renames["BackendRuleIn"])).optional()}
    ).named(renames["BackendIn"])
    types["BackendOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["BackendRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BackendOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CloudSQLConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "umbrellaProject": t.string().optional(),
            "umbrellaNetwork": t.string().optional(),
        }
    ).named(renames["CloudSQLConfigIn"])
    types["CloudSQLConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "umbrellaProject": t.string().optional(),
            "umbrellaNetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSQLConfigOut"])
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
    types["RemoveDnsRecordSetMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RemoveDnsRecordSetMetadataIn"])
    types["RemoveDnsRecordSetMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveDnsRecordSetMetadataOut"])

    functions = {}
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
    functions["servicesConnectionsCreate"] = servicenetworking.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
                "network": t.string().optional(),
                "reservedPeeringRanges": t.array(t.string()).optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
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
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "force": t.boolean().optional(),
                "network": t.string().optional(),
                "reservedPeeringRanges": t.array(t.string()).optional(),
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
        "servicesProjectsGlobalNetworksPeeredDnsDomainsCreate"
    ] = servicenetworking.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
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
        "servicesProjectsGlobalNetworksPeeredDnsDomainsDelete"
    ] = servicenetworking.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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

    return Import(
        importer="servicenetworking", renames=renames, types=types, functions=functions
    )
