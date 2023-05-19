from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_appengine() -> Import:
    appengine = HTTPRuntime("https://appengine.googleapis.com/")

    renames = {
        "ErrorResponse": "_appengine_1_ErrorResponse",
        "ListAuthorizedDomainsResponseIn": "_appengine_2_ListAuthorizedDomainsResponseIn",
        "ListAuthorizedDomainsResponseOut": "_appengine_3_ListAuthorizedDomainsResponseOut",
        "ListLocationsResponseIn": "_appengine_4_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_appengine_5_ListLocationsResponseOut",
        "LocationMetadataIn": "_appengine_6_LocationMetadataIn",
        "LocationMetadataOut": "_appengine_7_LocationMetadataOut",
        "AutomaticScalingIn": "_appengine_8_AutomaticScalingIn",
        "AutomaticScalingOut": "_appengine_9_AutomaticScalingOut",
        "ApiEndpointHandlerIn": "_appengine_10_ApiEndpointHandlerIn",
        "ApiEndpointHandlerOut": "_appengine_11_ApiEndpointHandlerOut",
        "ApplicationIn": "_appengine_12_ApplicationIn",
        "ApplicationOut": "_appengine_13_ApplicationOut",
        "ProjectStateIn": "_appengine_14_ProjectStateIn",
        "ProjectStateOut": "_appengine_15_ProjectStateOut",
        "EmptyIn": "_appengine_16_EmptyIn",
        "EmptyOut": "_appengine_17_EmptyOut",
        "DiskUtilizationIn": "_appengine_18_DiskUtilizationIn",
        "DiskUtilizationOut": "_appengine_19_DiskUtilizationOut",
        "UrlDispatchRuleIn": "_appengine_20_UrlDispatchRuleIn",
        "UrlDispatchRuleOut": "_appengine_21_UrlDispatchRuleOut",
        "FirewallRuleIn": "_appengine_22_FirewallRuleIn",
        "FirewallRuleOut": "_appengine_23_FirewallRuleOut",
        "ProjectsMetadataIn": "_appengine_24_ProjectsMetadataIn",
        "ProjectsMetadataOut": "_appengine_25_ProjectsMetadataOut",
        "RepairApplicationRequestIn": "_appengine_26_RepairApplicationRequestIn",
        "RepairApplicationRequestOut": "_appengine_27_RepairApplicationRequestOut",
        "ApiConfigHandlerIn": "_appengine_28_ApiConfigHandlerIn",
        "ApiConfigHandlerOut": "_appengine_29_ApiConfigHandlerOut",
        "GoogleAppengineV1betaLocationMetadataIn": "_appengine_30_GoogleAppengineV1betaLocationMetadataIn",
        "GoogleAppengineV1betaLocationMetadataOut": "_appengine_31_GoogleAppengineV1betaLocationMetadataOut",
        "AuthorizedCertificateIn": "_appengine_32_AuthorizedCertificateIn",
        "AuthorizedCertificateOut": "_appengine_33_AuthorizedCertificateOut",
        "ProjectEventIn": "_appengine_34_ProjectEventIn",
        "ProjectEventOut": "_appengine_35_ProjectEventOut",
        "VersionIn": "_appengine_36_VersionIn",
        "VersionOut": "_appengine_37_VersionOut",
        "ListVersionsResponseIn": "_appengine_38_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_appengine_39_ListVersionsResponseOut",
        "ErrorHandlerIn": "_appengine_40_ErrorHandlerIn",
        "ErrorHandlerOut": "_appengine_41_ErrorHandlerOut",
        "CreateVersionMetadataV1In": "_appengine_42_CreateVersionMetadataV1In",
        "CreateVersionMetadataV1Out": "_appengine_43_CreateVersionMetadataV1Out",
        "LivenessCheckIn": "_appengine_44_LivenessCheckIn",
        "LivenessCheckOut": "_appengine_45_LivenessCheckOut",
        "VolumeIn": "_appengine_46_VolumeIn",
        "VolumeOut": "_appengine_47_VolumeOut",
        "StatusIn": "_appengine_48_StatusIn",
        "StatusOut": "_appengine_49_StatusOut",
        "ReasonsIn": "_appengine_50_ReasonsIn",
        "ReasonsOut": "_appengine_51_ReasonsOut",
        "CpuUtilizationIn": "_appengine_52_CpuUtilizationIn",
        "CpuUtilizationOut": "_appengine_53_CpuUtilizationOut",
        "CreateVersionMetadataV1BetaIn": "_appengine_54_CreateVersionMetadataV1BetaIn",
        "CreateVersionMetadataV1BetaOut": "_appengine_55_CreateVersionMetadataV1BetaOut",
        "AuthorizedDomainIn": "_appengine_56_AuthorizedDomainIn",
        "AuthorizedDomainOut": "_appengine_57_AuthorizedDomainOut",
        "ListDomainMappingsResponseIn": "_appengine_58_ListDomainMappingsResponseIn",
        "ListDomainMappingsResponseOut": "_appengine_59_ListDomainMappingsResponseOut",
        "FlexibleRuntimeSettingsIn": "_appengine_60_FlexibleRuntimeSettingsIn",
        "FlexibleRuntimeSettingsOut": "_appengine_61_FlexibleRuntimeSettingsOut",
        "OperationMetadataV1AlphaIn": "_appengine_62_OperationMetadataV1AlphaIn",
        "OperationMetadataV1AlphaOut": "_appengine_63_OperationMetadataV1AlphaOut",
        "DomainMappingIn": "_appengine_64_DomainMappingIn",
        "DomainMappingOut": "_appengine_65_DomainMappingOut",
        "TrafficSplitIn": "_appengine_66_TrafficSplitIn",
        "TrafficSplitOut": "_appengine_67_TrafficSplitOut",
        "DebugInstanceRequestIn": "_appengine_68_DebugInstanceRequestIn",
        "DebugInstanceRequestOut": "_appengine_69_DebugInstanceRequestOut",
        "StandardSchedulerSettingsIn": "_appengine_70_StandardSchedulerSettingsIn",
        "StandardSchedulerSettingsOut": "_appengine_71_StandardSchedulerSettingsOut",
        "StaticFilesHandlerIn": "_appengine_72_StaticFilesHandlerIn",
        "StaticFilesHandlerOut": "_appengine_73_StaticFilesHandlerOut",
        "IdentityAwareProxyIn": "_appengine_74_IdentityAwareProxyIn",
        "IdentityAwareProxyOut": "_appengine_75_IdentityAwareProxyOut",
        "LocationIn": "_appengine_76_LocationIn",
        "LocationOut": "_appengine_77_LocationOut",
        "CertificateRawDataIn": "_appengine_78_CertificateRawDataIn",
        "CertificateRawDataOut": "_appengine_79_CertificateRawDataOut",
        "ResourcesIn": "_appengine_80_ResourcesIn",
        "ResourcesOut": "_appengine_81_ResourcesOut",
        "ResourceRecordIn": "_appengine_82_ResourceRecordIn",
        "ResourceRecordOut": "_appengine_83_ResourceRecordOut",
        "ServiceIn": "_appengine_84_ServiceIn",
        "ServiceOut": "_appengine_85_ServiceOut",
        "UrlMapIn": "_appengine_86_UrlMapIn",
        "UrlMapOut": "_appengine_87_UrlMapOut",
        "DeploymentIn": "_appengine_88_DeploymentIn",
        "DeploymentOut": "_appengine_89_DeploymentOut",
        "ListInstancesResponseIn": "_appengine_90_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_appengine_91_ListInstancesResponseOut",
        "VpcAccessConnectorIn": "_appengine_92_VpcAccessConnectorIn",
        "VpcAccessConnectorOut": "_appengine_93_VpcAccessConnectorOut",
        "OperationIn": "_appengine_94_OperationIn",
        "OperationOut": "_appengine_95_OperationOut",
        "RequestUtilizationIn": "_appengine_96_RequestUtilizationIn",
        "RequestUtilizationOut": "_appengine_97_RequestUtilizationOut",
        "ScriptHandlerIn": "_appengine_98_ScriptHandlerIn",
        "ScriptHandlerOut": "_appengine_99_ScriptHandlerOut",
        "ManagedCertificateIn": "_appengine_100_ManagedCertificateIn",
        "ManagedCertificateOut": "_appengine_101_ManagedCertificateOut",
        "EndpointsApiServiceIn": "_appengine_102_EndpointsApiServiceIn",
        "EndpointsApiServiceOut": "_appengine_103_EndpointsApiServiceOut",
        "OperationMetadataV1BetaIn": "_appengine_104_OperationMetadataV1BetaIn",
        "OperationMetadataV1BetaOut": "_appengine_105_OperationMetadataV1BetaOut",
        "LibraryIn": "_appengine_106_LibraryIn",
        "LibraryOut": "_appengine_107_LibraryOut",
        "BasicScalingIn": "_appengine_108_BasicScalingIn",
        "BasicScalingOut": "_appengine_109_BasicScalingOut",
        "InstanceIn": "_appengine_110_InstanceIn",
        "InstanceOut": "_appengine_111_InstanceOut",
        "FeatureSettingsIn": "_appengine_112_FeatureSettingsIn",
        "FeatureSettingsOut": "_appengine_113_FeatureSettingsOut",
        "CreateVersionMetadataV1AlphaIn": "_appengine_114_CreateVersionMetadataV1AlphaIn",
        "CreateVersionMetadataV1AlphaOut": "_appengine_115_CreateVersionMetadataV1AlphaOut",
        "ManualScalingIn": "_appengine_116_ManualScalingIn",
        "ManualScalingOut": "_appengine_117_ManualScalingOut",
        "ListAuthorizedCertificatesResponseIn": "_appengine_118_ListAuthorizedCertificatesResponseIn",
        "ListAuthorizedCertificatesResponseOut": "_appengine_119_ListAuthorizedCertificatesResponseOut",
        "HealthCheckIn": "_appengine_120_HealthCheckIn",
        "HealthCheckOut": "_appengine_121_HealthCheckOut",
        "BatchUpdateIngressRulesResponseIn": "_appengine_122_BatchUpdateIngressRulesResponseIn",
        "BatchUpdateIngressRulesResponseOut": "_appengine_123_BatchUpdateIngressRulesResponseOut",
        "ListOperationsResponseIn": "_appengine_124_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_appengine_125_ListOperationsResponseOut",
        "CloudBuildOptionsIn": "_appengine_126_CloudBuildOptionsIn",
        "CloudBuildOptionsOut": "_appengine_127_CloudBuildOptionsOut",
        "BatchUpdateIngressRulesRequestIn": "_appengine_128_BatchUpdateIngressRulesRequestIn",
        "BatchUpdateIngressRulesRequestOut": "_appengine_129_BatchUpdateIngressRulesRequestOut",
        "OperationMetadataV1In": "_appengine_130_OperationMetadataV1In",
        "OperationMetadataV1Out": "_appengine_131_OperationMetadataV1Out",
        "NetworkSettingsIn": "_appengine_132_NetworkSettingsIn",
        "NetworkSettingsOut": "_appengine_133_NetworkSettingsOut",
        "EntrypointIn": "_appengine_134_EntrypointIn",
        "EntrypointOut": "_appengine_135_EntrypointOut",
        "ListIngressRulesResponseIn": "_appengine_136_ListIngressRulesResponseIn",
        "ListIngressRulesResponseOut": "_appengine_137_ListIngressRulesResponseOut",
        "FileInfoIn": "_appengine_138_FileInfoIn",
        "FileInfoOut": "_appengine_139_FileInfoOut",
        "SslSettingsIn": "_appengine_140_SslSettingsIn",
        "SslSettingsOut": "_appengine_141_SslSettingsOut",
        "NetworkIn": "_appengine_142_NetworkIn",
        "NetworkOut": "_appengine_143_NetworkOut",
        "ReadinessCheckIn": "_appengine_144_ReadinessCheckIn",
        "ReadinessCheckOut": "_appengine_145_ReadinessCheckOut",
        "ZipInfoIn": "_appengine_146_ZipInfoIn",
        "ZipInfoOut": "_appengine_147_ZipInfoOut",
        "ContainerInfoIn": "_appengine_148_ContainerInfoIn",
        "ContainerInfoOut": "_appengine_149_ContainerInfoOut",
        "NetworkUtilizationIn": "_appengine_150_NetworkUtilizationIn",
        "NetworkUtilizationOut": "_appengine_151_NetworkUtilizationOut",
        "ListServicesResponseIn": "_appengine_152_ListServicesResponseIn",
        "ListServicesResponseOut": "_appengine_153_ListServicesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ListAuthorizedDomainsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "domains": t.array(t.proxy(renames["AuthorizedDomainIn"])).optional(),
        }
    ).named(renames["ListAuthorizedDomainsResponseIn"])
    types["ListAuthorizedDomainsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "domains": t.array(t.proxy(renames["AuthorizedDomainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAuthorizedDomainsResponseOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["LocationMetadataIn"] = t.struct(
        {
            "standardEnvironmentAvailable": t.boolean().optional(),
            "flexibleEnvironmentAvailable": t.boolean().optional(),
        }
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "standardEnvironmentAvailable": t.boolean().optional(),
            "searchApiAvailable": t.boolean().optional(),
            "flexibleEnvironmentAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["AutomaticScalingIn"] = t.struct(
        {
            "cpuUtilization": t.proxy(renames["CpuUtilizationIn"]).optional(),
            "maxConcurrentRequests": t.integer().optional(),
            "maxTotalInstances": t.integer().optional(),
            "diskUtilization": t.proxy(renames["DiskUtilizationIn"]).optional(),
            "requestUtilization": t.proxy(renames["RequestUtilizationIn"]).optional(),
            "minTotalInstances": t.integer().optional(),
            "maxIdleInstances": t.integer().optional(),
            "maxPendingLatency": t.string().optional(),
            "minIdleInstances": t.integer().optional(),
            "networkUtilization": t.proxy(renames["NetworkUtilizationIn"]).optional(),
            "minPendingLatency": t.string().optional(),
            "standardSchedulerSettings": t.proxy(
                renames["StandardSchedulerSettingsIn"]
            ).optional(),
            "coolDownPeriod": t.string().optional(),
        }
    ).named(renames["AutomaticScalingIn"])
    types["AutomaticScalingOut"] = t.struct(
        {
            "cpuUtilization": t.proxy(renames["CpuUtilizationOut"]).optional(),
            "maxConcurrentRequests": t.integer().optional(),
            "maxTotalInstances": t.integer().optional(),
            "diskUtilization": t.proxy(renames["DiskUtilizationOut"]).optional(),
            "requestUtilization": t.proxy(renames["RequestUtilizationOut"]).optional(),
            "minTotalInstances": t.integer().optional(),
            "maxIdleInstances": t.integer().optional(),
            "maxPendingLatency": t.string().optional(),
            "minIdleInstances": t.integer().optional(),
            "networkUtilization": t.proxy(renames["NetworkUtilizationOut"]).optional(),
            "minPendingLatency": t.string().optional(),
            "standardSchedulerSettings": t.proxy(
                renames["StandardSchedulerSettingsOut"]
            ).optional(),
            "coolDownPeriod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutomaticScalingOut"])
    types["ApiEndpointHandlerIn"] = t.struct(
        {"scriptPath": t.string().optional()}
    ).named(renames["ApiEndpointHandlerIn"])
    types["ApiEndpointHandlerOut"] = t.struct(
        {
            "scriptPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiEndpointHandlerOut"])
    types["ApplicationIn"] = t.struct(
        {
            "id": t.string().optional(),
            "iap": t.proxy(renames["IdentityAwareProxyIn"]),
            "servingStatus": t.string().optional(),
            "dispatchRules": t.array(t.proxy(renames["UrlDispatchRuleIn"])).optional(),
            "authDomain": t.string().optional(),
            "databaseType": t.string().optional(),
            "locationId": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "featureSettings": t.proxy(renames["FeatureSettingsIn"]).optional(),
            "defaultCookieExpiration": t.string().optional(),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "id": t.string().optional(),
            "iap": t.proxy(renames["IdentityAwareProxyOut"]),
            "gcrDomain": t.string().optional(),
            "servingStatus": t.string().optional(),
            "dispatchRules": t.array(t.proxy(renames["UrlDispatchRuleOut"])).optional(),
            "name": t.string().optional(),
            "authDomain": t.string().optional(),
            "defaultBucket": t.string().optional(),
            "databaseType": t.string().optional(),
            "locationId": t.string().optional(),
            "defaultHostname": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "codeBucket": t.string().optional(),
            "featureSettings": t.proxy(renames["FeatureSettingsOut"]).optional(),
            "defaultCookieExpiration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
    types["ProjectStateIn"] = t.struct(
        {
            "currentReasons": t.proxy(renames["ReasonsIn"]),
            "state": t.string().optional(),
            "previousReasons": t.proxy(renames["ReasonsIn"]).optional(),
        }
    ).named(renames["ProjectStateIn"])
    types["ProjectStateOut"] = t.struct(
        {
            "currentReasons": t.proxy(renames["ReasonsOut"]),
            "state": t.string().optional(),
            "previousReasons": t.proxy(renames["ReasonsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectStateOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["DiskUtilizationIn"] = t.struct(
        {
            "targetReadBytesPerSecond": t.integer().optional(),
            "targetWriteOpsPerSecond": t.integer().optional(),
            "targetReadOpsPerSecond": t.integer().optional(),
            "targetWriteBytesPerSecond": t.integer().optional(),
        }
    ).named(renames["DiskUtilizationIn"])
    types["DiskUtilizationOut"] = t.struct(
        {
            "targetReadBytesPerSecond": t.integer().optional(),
            "targetWriteOpsPerSecond": t.integer().optional(),
            "targetReadOpsPerSecond": t.integer().optional(),
            "targetWriteBytesPerSecond": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskUtilizationOut"])
    types["UrlDispatchRuleIn"] = t.struct(
        {
            "path": t.string().optional(),
            "service": t.string().optional(),
            "domain": t.string().optional(),
        }
    ).named(renames["UrlDispatchRuleIn"])
    types["UrlDispatchRuleOut"] = t.struct(
        {
            "path": t.string().optional(),
            "service": t.string().optional(),
            "domain": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlDispatchRuleOut"])
    types["FirewallRuleIn"] = t.struct(
        {
            "action": t.string().optional(),
            "description": t.string().optional(),
            "sourceRange": t.string().optional(),
            "priority": t.integer().optional(),
        }
    ).named(renames["FirewallRuleIn"])
    types["FirewallRuleOut"] = t.struct(
        {
            "action": t.string().optional(),
            "description": t.string().optional(),
            "sourceRange": t.string().optional(),
            "priority": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirewallRuleOut"])
    types["ProjectsMetadataIn"] = t.struct(
        {
            "consumerProjectNumber": t.string().optional(),
            "consumerProjectId": t.string().optional(),
            "producerProjectNumber": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "producerProjectId": t.string().optional(),
            "consumerProjectState": t.string().optional(),
            "p4ServiceAccount": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
        }
    ).named(renames["ProjectsMetadataIn"])
    types["ProjectsMetadataOut"] = t.struct(
        {
            "consumerProjectNumber": t.string().optional(),
            "consumerProjectId": t.string().optional(),
            "producerProjectNumber": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "producerProjectId": t.string().optional(),
            "consumerProjectState": t.string().optional(),
            "p4ServiceAccount": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectsMetadataOut"])
    types["RepairApplicationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RepairApplicationRequestIn"]
    )
    types["RepairApplicationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RepairApplicationRequestOut"])
    types["ApiConfigHandlerIn"] = t.struct(
        {
            "script": t.string().optional(),
            "login": t.string().optional(),
            "securityLevel": t.string().optional(),
            "authFailAction": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["ApiConfigHandlerIn"])
    types["ApiConfigHandlerOut"] = t.struct(
        {
            "script": t.string().optional(),
            "login": t.string().optional(),
            "securityLevel": t.string().optional(),
            "authFailAction": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiConfigHandlerOut"])
    types["GoogleAppengineV1betaLocationMetadataIn"] = t.struct(
        {
            "flexibleEnvironmentAvailable": t.boolean().optional(),
            "standardEnvironmentAvailable": t.boolean().optional(),
        }
    ).named(renames["GoogleAppengineV1betaLocationMetadataIn"])
    types["GoogleAppengineV1betaLocationMetadataOut"] = t.struct(
        {
            "flexibleEnvironmentAvailable": t.boolean().optional(),
            "searchApiAvailable": t.boolean().optional(),
            "standardEnvironmentAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppengineV1betaLocationMetadataOut"])
    types["AuthorizedCertificateIn"] = t.struct(
        {
            "domainMappingsCount": t.integer().optional(),
            "name": t.string().optional(),
            "domainNames": t.array(t.string()).optional(),
            "visibleDomainMappings": t.array(t.string()).optional(),
            "managedCertificate": t.proxy(renames["ManagedCertificateIn"]).optional(),
            "certificateRawData": t.proxy(renames["CertificateRawDataIn"]).optional(),
            "id": t.string().optional(),
            "displayName": t.string().optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["AuthorizedCertificateIn"])
    types["AuthorizedCertificateOut"] = t.struct(
        {
            "domainMappingsCount": t.integer().optional(),
            "name": t.string().optional(),
            "domainNames": t.array(t.string()).optional(),
            "visibleDomainMappings": t.array(t.string()).optional(),
            "managedCertificate": t.proxy(renames["ManagedCertificateOut"]).optional(),
            "certificateRawData": t.proxy(renames["CertificateRawDataOut"]).optional(),
            "id": t.string().optional(),
            "displayName": t.string().optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedCertificateOut"])
    types["ProjectEventIn"] = t.struct(
        {
            "phase": t.string(),
            "projectMetadata": t.proxy(renames["ProjectsMetadataIn"]).optional(),
            "state": t.proxy(renames["ProjectStateIn"]).optional(),
            "eventId": t.string().optional(),
        }
    ).named(renames["ProjectEventIn"])
    types["ProjectEventOut"] = t.struct(
        {
            "phase": t.string(),
            "projectMetadata": t.proxy(renames["ProjectsMetadataOut"]).optional(),
            "state": t.proxy(renames["ProjectStateOut"]).optional(),
            "eventId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectEventOut"])
    types["VersionIn"] = t.struct(
        {
            "healthCheck": t.proxy(renames["HealthCheckIn"]).optional(),
            "zones": t.array(t.string()).optional(),
            "runtimeChannel": t.string().optional(),
            "inboundServices": t.array(t.string()).optional(),
            "resources": t.proxy(renames["ResourcesIn"]).optional(),
            "errorHandlers": t.array(t.proxy(renames["ErrorHandlerIn"])).optional(),
            "endpointsApiService": t.proxy(renames["EndpointsApiServiceIn"]).optional(),
            "deployment": t.proxy(renames["DeploymentIn"]).optional(),
            "betaSettings": t.struct({"_": t.string().optional()}).optional(),
            "basicScaling": t.proxy(renames["BasicScalingIn"]).optional(),
            "handlers": t.array(t.proxy(renames["UrlMapIn"])).optional(),
            "readinessCheck": t.proxy(renames["ReadinessCheckIn"]).optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "createdBy": t.string().optional(),
            "appEngineApis": t.boolean().optional(),
            "env": t.string().optional(),
            "diskUsageBytes": t.string().optional(),
            "runtimeMainExecutablePath": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "livenessCheck": t.proxy(renames["LivenessCheckIn"]).optional(),
            "createTime": t.string().optional(),
            "buildEnvVariables": t.struct({"_": t.string().optional()}).optional(),
            "entrypoint": t.proxy(renames["EntrypointIn"]).optional(),
            "nobuildFilesRegex": t.string().optional(),
            "automaticScaling": t.proxy(renames["AutomaticScalingIn"]).optional(),
            "versionUrl": t.string().optional(),
            "runtime": t.string().optional(),
            "apiConfig": t.proxy(renames["ApiConfigHandlerIn"]).optional(),
            "threadsafe": t.boolean().optional(),
            "libraries": t.array(t.proxy(renames["LibraryIn"])).optional(),
            "vpcAccessConnector": t.proxy(renames["VpcAccessConnectorIn"]).optional(),
            "flexibleRuntimeSettings": t.proxy(
                renames["FlexibleRuntimeSettingsIn"]
            ).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "runtimeApiVersion": t.string().optional(),
            "vm": t.boolean().optional(),
            "defaultExpiration": t.string().optional(),
            "network": t.proxy(renames["NetworkIn"]).optional(),
            "instanceClass": t.string().optional(),
            "servingStatus": t.string().optional(),
            "manualScaling": t.proxy(renames["ManualScalingIn"]).optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "healthCheck": t.proxy(renames["HealthCheckOut"]).optional(),
            "zones": t.array(t.string()).optional(),
            "runtimeChannel": t.string().optional(),
            "inboundServices": t.array(t.string()).optional(),
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "errorHandlers": t.array(t.proxy(renames["ErrorHandlerOut"])).optional(),
            "endpointsApiService": t.proxy(
                renames["EndpointsApiServiceOut"]
            ).optional(),
            "deployment": t.proxy(renames["DeploymentOut"]).optional(),
            "betaSettings": t.struct({"_": t.string().optional()}).optional(),
            "basicScaling": t.proxy(renames["BasicScalingOut"]).optional(),
            "handlers": t.array(t.proxy(renames["UrlMapOut"])).optional(),
            "readinessCheck": t.proxy(renames["ReadinessCheckOut"]).optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "createdBy": t.string().optional(),
            "appEngineApis": t.boolean().optional(),
            "env": t.string().optional(),
            "diskUsageBytes": t.string().optional(),
            "runtimeMainExecutablePath": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "livenessCheck": t.proxy(renames["LivenessCheckOut"]).optional(),
            "createTime": t.string().optional(),
            "buildEnvVariables": t.struct({"_": t.string().optional()}).optional(),
            "entrypoint": t.proxy(renames["EntrypointOut"]).optional(),
            "nobuildFilesRegex": t.string().optional(),
            "automaticScaling": t.proxy(renames["AutomaticScalingOut"]).optional(),
            "versionUrl": t.string().optional(),
            "runtime": t.string().optional(),
            "apiConfig": t.proxy(renames["ApiConfigHandlerOut"]).optional(),
            "threadsafe": t.boolean().optional(),
            "libraries": t.array(t.proxy(renames["LibraryOut"])).optional(),
            "vpcAccessConnector": t.proxy(renames["VpcAccessConnectorOut"]).optional(),
            "flexibleRuntimeSettings": t.proxy(
                renames["FlexibleRuntimeSettingsOut"]
            ).optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "runtimeApiVersion": t.string().optional(),
            "vm": t.boolean().optional(),
            "defaultExpiration": t.string().optional(),
            "network": t.proxy(renames["NetworkOut"]).optional(),
            "instanceClass": t.string().optional(),
            "servingStatus": t.string().optional(),
            "manualScaling": t.proxy(renames["ManualScalingOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["ListVersionsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(t.proxy(renames["VersionIn"])).optional(),
        }
    ).named(renames["ListVersionsResponseIn"])
    types["ListVersionsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "versions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVersionsResponseOut"])
    types["ErrorHandlerIn"] = t.struct(
        {
            "staticFile": t.string().optional(),
            "errorCode": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["ErrorHandlerIn"])
    types["ErrorHandlerOut"] = t.struct(
        {
            "staticFile": t.string().optional(),
            "errorCode": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorHandlerOut"])
    types["CreateVersionMetadataV1In"] = t.struct(
        {"cloudBuildId": t.string().optional()}
    ).named(renames["CreateVersionMetadataV1In"])
    types["CreateVersionMetadataV1Out"] = t.struct(
        {
            "cloudBuildId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVersionMetadataV1Out"])
    types["LivenessCheckIn"] = t.struct(
        {
            "path": t.string().optional(),
            "failureThreshold": t.integer().optional(),
            "initialDelay": t.string().optional(),
            "host": t.string().optional(),
            "successThreshold": t.integer().optional(),
            "timeout": t.string().optional(),
            "checkInterval": t.string().optional(),
        }
    ).named(renames["LivenessCheckIn"])
    types["LivenessCheckOut"] = t.struct(
        {
            "path": t.string().optional(),
            "failureThreshold": t.integer().optional(),
            "initialDelay": t.string().optional(),
            "host": t.string().optional(),
            "successThreshold": t.integer().optional(),
            "timeout": t.string().optional(),
            "checkInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivenessCheckOut"])
    types["VolumeIn"] = t.struct(
        {
            "volumeType": t.string().optional(),
            "sizeGb": t.number().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "volumeType": t.string().optional(),
            "sizeGb": t.number().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
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
    types["ReasonsIn"] = t.struct(
        {
            "abuse": t.string(),
            "billing": t.string(),
            "serviceManagement": t.string(),
            "dataGovernance": t.string(),
        }
    ).named(renames["ReasonsIn"])
    types["ReasonsOut"] = t.struct(
        {
            "abuse": t.string(),
            "billing": t.string(),
            "serviceManagement": t.string(),
            "dataGovernance": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReasonsOut"])
    types["CpuUtilizationIn"] = t.struct(
        {
            "targetUtilization": t.number().optional(),
            "aggregationWindowLength": t.string().optional(),
        }
    ).named(renames["CpuUtilizationIn"])
    types["CpuUtilizationOut"] = t.struct(
        {
            "targetUtilization": t.number().optional(),
            "aggregationWindowLength": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CpuUtilizationOut"])
    types["CreateVersionMetadataV1BetaIn"] = t.struct(
        {"cloudBuildId": t.string().optional()}
    ).named(renames["CreateVersionMetadataV1BetaIn"])
    types["CreateVersionMetadataV1BetaOut"] = t.struct(
        {
            "cloudBuildId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVersionMetadataV1BetaOut"])
    types["AuthorizedDomainIn"] = t.struct(
        {"name": t.string().optional(), "id": t.string().optional()}
    ).named(renames["AuthorizedDomainIn"])
    types["AuthorizedDomainOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedDomainOut"])
    types["ListDomainMappingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "domainMappings": t.array(t.proxy(renames["DomainMappingIn"])).optional(),
        }
    ).named(renames["ListDomainMappingsResponseIn"])
    types["ListDomainMappingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "domainMappings": t.array(t.proxy(renames["DomainMappingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDomainMappingsResponseOut"])
    types["FlexibleRuntimeSettingsIn"] = t.struct(
        {
            "runtimeVersion": t.string().optional(),
            "operatingSystem": t.string().optional(),
        }
    ).named(renames["FlexibleRuntimeSettingsIn"])
    types["FlexibleRuntimeSettingsOut"] = t.struct(
        {
            "runtimeVersion": t.string().optional(),
            "operatingSystem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlexibleRuntimeSettingsOut"])
    types["OperationMetadataV1AlphaIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "warning": t.array(t.string()).optional(),
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1AlphaIn"]),
            "target": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "user": t.string().optional(),
            "insertTime": t.string().optional(),
            "method": t.string().optional(),
        }
    ).named(renames["OperationMetadataV1AlphaIn"])
    types["OperationMetadataV1AlphaOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "warning": t.array(t.string()).optional(),
            "createVersionMetadata": t.proxy(
                renames["CreateVersionMetadataV1AlphaOut"]
            ),
            "target": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "user": t.string().optional(),
            "insertTime": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1AlphaOut"])
    types["DomainMappingIn"] = t.struct(
        {
            "id": t.string().optional(),
            "sslSettings": t.proxy(renames["SslSettingsIn"]).optional(),
            "resourceRecords": t.array(t.proxy(renames["ResourceRecordIn"])).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DomainMappingIn"])
    types["DomainMappingOut"] = t.struct(
        {
            "id": t.string().optional(),
            "sslSettings": t.proxy(renames["SslSettingsOut"]).optional(),
            "resourceRecords": t.array(
                t.proxy(renames["ResourceRecordOut"])
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainMappingOut"])
    types["TrafficSplitIn"] = t.struct(
        {
            "shardBy": t.string().optional(),
            "allocations": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TrafficSplitIn"])
    types["TrafficSplitOut"] = t.struct(
        {
            "shardBy": t.string().optional(),
            "allocations": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TrafficSplitOut"])
    types["DebugInstanceRequestIn"] = t.struct({"sshKey": t.string().optional()}).named(
        renames["DebugInstanceRequestIn"]
    )
    types["DebugInstanceRequestOut"] = t.struct(
        {
            "sshKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DebugInstanceRequestOut"])
    types["StandardSchedulerSettingsIn"] = t.struct(
        {
            "minInstances": t.integer().optional(),
            "maxInstances": t.integer().optional(),
            "targetThroughputUtilization": t.number().optional(),
            "targetCpuUtilization": t.number().optional(),
        }
    ).named(renames["StandardSchedulerSettingsIn"])
    types["StandardSchedulerSettingsOut"] = t.struct(
        {
            "minInstances": t.integer().optional(),
            "maxInstances": t.integer().optional(),
            "targetThroughputUtilization": t.number().optional(),
            "targetCpuUtilization": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSchedulerSettingsOut"])
    types["StaticFilesHandlerIn"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "applicationReadable": t.boolean().optional(),
            "requireMatchingFile": t.boolean().optional(),
            "uploadPathRegex": t.string().optional(),
            "httpHeaders": t.struct({"_": t.string().optional()}).optional(),
            "expiration": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["StaticFilesHandlerIn"])
    types["StaticFilesHandlerOut"] = t.struct(
        {
            "mimeType": t.string().optional(),
            "applicationReadable": t.boolean().optional(),
            "requireMatchingFile": t.boolean().optional(),
            "uploadPathRegex": t.string().optional(),
            "httpHeaders": t.struct({"_": t.string().optional()}).optional(),
            "expiration": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StaticFilesHandlerOut"])
    types["IdentityAwareProxyIn"] = t.struct(
        {
            "oauth2ClientSecret": t.string().optional(),
            "enabled": t.boolean().optional(),
            "oauth2ClientId": t.string().optional(),
        }
    ).named(renames["IdentityAwareProxyIn"])
    types["IdentityAwareProxyOut"] = t.struct(
        {
            "oauth2ClientSecretSha256": t.string().optional(),
            "oauth2ClientSecret": t.string().optional(),
            "enabled": t.boolean().optional(),
            "oauth2ClientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityAwareProxyOut"])
    types["LocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CertificateRawDataIn"] = t.struct(
        {
            "privateKey": t.string().optional(),
            "publicCertificate": t.string().optional(),
        }
    ).named(renames["CertificateRawDataIn"])
    types["CertificateRawDataOut"] = t.struct(
        {
            "privateKey": t.string().optional(),
            "publicCertificate": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateRawDataOut"])
    types["ResourcesIn"] = t.struct(
        {
            "cpu": t.number().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "kmsKeyReference": t.string().optional(),
            "diskGb": t.number().optional(),
            "memoryGb": t.number().optional(),
        }
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "cpu": t.number().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "kmsKeyReference": t.string().optional(),
            "diskGb": t.number().optional(),
            "memoryGb": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
    types["ResourceRecordIn"] = t.struct(
        {
            "name": t.string().optional(),
            "rrdata": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ResourceRecordIn"])
    types["ResourceRecordOut"] = t.struct(
        {
            "name": t.string().optional(),
            "rrdata": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceRecordOut"])
    types["ServiceIn"] = t.struct(
        {
            "id": t.string().optional(),
            "networkSettings": t.proxy(renames["NetworkSettingsIn"]).optional(),
            "split": t.proxy(renames["TrafficSplitIn"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "id": t.string().optional(),
            "networkSettings": t.proxy(renames["NetworkSettingsOut"]).optional(),
            "split": t.proxy(renames["TrafficSplitOut"]).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["UrlMapIn"] = t.struct(
        {
            "authFailAction": t.string().optional(),
            "urlRegex": t.string().optional(),
            "staticFiles": t.proxy(renames["StaticFilesHandlerIn"]).optional(),
            "login": t.string().optional(),
            "redirectHttpResponseCode": t.string().optional(),
            "securityLevel": t.string().optional(),
            "script": t.proxy(renames["ScriptHandlerIn"]).optional(),
            "apiEndpoint": t.proxy(renames["ApiEndpointHandlerIn"]).optional(),
        }
    ).named(renames["UrlMapIn"])
    types["UrlMapOut"] = t.struct(
        {
            "authFailAction": t.string().optional(),
            "urlRegex": t.string().optional(),
            "staticFiles": t.proxy(renames["StaticFilesHandlerOut"]).optional(),
            "login": t.string().optional(),
            "redirectHttpResponseCode": t.string().optional(),
            "securityLevel": t.string().optional(),
            "script": t.proxy(renames["ScriptHandlerOut"]).optional(),
            "apiEndpoint": t.proxy(renames["ApiEndpointHandlerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlMapOut"])
    types["DeploymentIn"] = t.struct(
        {
            "zip": t.proxy(renames["ZipInfoIn"]).optional(),
            "container": t.proxy(renames["ContainerInfoIn"]).optional(),
            "cloudBuildOptions": t.proxy(renames["CloudBuildOptionsIn"]).optional(),
            "files": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "zip": t.proxy(renames["ZipInfoOut"]).optional(),
            "container": t.proxy(renames["ContainerInfoOut"]).optional(),
            "cloudBuildOptions": t.proxy(renames["CloudBuildOptionsOut"]).optional(),
            "files": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["VpcAccessConnectorIn"] = t.struct(
        {"name": t.string().optional(), "egressSetting": t.string().optional()}
    ).named(renames["VpcAccessConnectorIn"])
    types["VpcAccessConnectorOut"] = t.struct(
        {
            "name": t.string().optional(),
            "egressSetting": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcAccessConnectorOut"])
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
    types["RequestUtilizationIn"] = t.struct(
        {
            "targetRequestCountPerSecond": t.integer().optional(),
            "targetConcurrentRequests": t.integer().optional(),
        }
    ).named(renames["RequestUtilizationIn"])
    types["RequestUtilizationOut"] = t.struct(
        {
            "targetRequestCountPerSecond": t.integer().optional(),
            "targetConcurrentRequests": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestUtilizationOut"])
    types["ScriptHandlerIn"] = t.struct({"scriptPath": t.string().optional()}).named(
        renames["ScriptHandlerIn"]
    )
    types["ScriptHandlerOut"] = t.struct(
        {
            "scriptPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptHandlerOut"])
    types["ManagedCertificateIn"] = t.struct(
        {"status": t.string().optional(), "lastRenewalTime": t.string().optional()}
    ).named(renames["ManagedCertificateIn"])
    types["ManagedCertificateOut"] = t.struct(
        {
            "status": t.string().optional(),
            "lastRenewalTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagedCertificateOut"])
    types["EndpointsApiServiceIn"] = t.struct(
        {
            "disableTraceSampling": t.boolean().optional(),
            "name": t.string().optional(),
            "rolloutStrategy": t.string().optional(),
            "configId": t.string().optional(),
        }
    ).named(renames["EndpointsApiServiceIn"])
    types["EndpointsApiServiceOut"] = t.struct(
        {
            "disableTraceSampling": t.boolean().optional(),
            "name": t.string().optional(),
            "rolloutStrategy": t.string().optional(),
            "configId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointsApiServiceOut"])
    types["OperationMetadataV1BetaIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "insertTime": t.string().optional(),
            "method": t.string().optional(),
            "warning": t.array(t.string()).optional(),
            "target": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1BetaIn"]),
            "user": t.string().optional(),
        }
    ).named(renames["OperationMetadataV1BetaIn"])
    types["OperationMetadataV1BetaOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "insertTime": t.string().optional(),
            "method": t.string().optional(),
            "warning": t.array(t.string()).optional(),
            "target": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1BetaOut"]),
            "user": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1BetaOut"])
    types["LibraryIn"] = t.struct(
        {"name": t.string().optional(), "version": t.string().optional()}
    ).named(renames["LibraryIn"])
    types["LibraryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LibraryOut"])
    types["BasicScalingIn"] = t.struct(
        {"maxInstances": t.integer().optional(), "idleTimeout": t.string().optional()}
    ).named(renames["BasicScalingIn"])
    types["BasicScalingOut"] = t.struct(
        {
            "maxInstances": t.integer().optional(),
            "idleTimeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicScalingOut"])
    types["InstanceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InstanceIn"]
    )
    types["InstanceOut"] = t.struct(
        {
            "vmLiveness": t.string().optional(),
            "vmId": t.string().optional(),
            "memoryUsage": t.string().optional(),
            "requests": t.integer().optional(),
            "vmDebugEnabled": t.boolean().optional(),
            "appEngineRelease": t.string().optional(),
            "vmZoneName": t.string().optional(),
            "vmStatus": t.string().optional(),
            "availability": t.string().optional(),
            "averageLatency": t.integer().optional(),
            "vmName": t.string().optional(),
            "id": t.string().optional(),
            "errors": t.integer().optional(),
            "name": t.string().optional(),
            "vmIp": t.string().optional(),
            "qps": t.number().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["FeatureSettingsIn"] = t.struct(
        {
            "splitHealthChecks": t.boolean().optional(),
            "useContainerOptimizedOs": t.boolean().optional(),
        }
    ).named(renames["FeatureSettingsIn"])
    types["FeatureSettingsOut"] = t.struct(
        {
            "splitHealthChecks": t.boolean().optional(),
            "useContainerOptimizedOs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeatureSettingsOut"])
    types["CreateVersionMetadataV1AlphaIn"] = t.struct(
        {"cloudBuildId": t.string().optional()}
    ).named(renames["CreateVersionMetadataV1AlphaIn"])
    types["CreateVersionMetadataV1AlphaOut"] = t.struct(
        {
            "cloudBuildId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVersionMetadataV1AlphaOut"])
    types["ManualScalingIn"] = t.struct({"instances": t.integer().optional()}).named(
        renames["ManualScalingIn"]
    )
    types["ManualScalingOut"] = t.struct(
        {
            "instances": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualScalingOut"])
    types["ListAuthorizedCertificatesResponseIn"] = t.struct(
        {
            "certificates": t.array(
                t.proxy(renames["AuthorizedCertificateIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAuthorizedCertificatesResponseIn"])
    types["ListAuthorizedCertificatesResponseOut"] = t.struct(
        {
            "certificates": t.array(
                t.proxy(renames["AuthorizedCertificateOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAuthorizedCertificatesResponseOut"])
    types["HealthCheckIn"] = t.struct(
        {
            "host": t.string().optional(),
            "healthyThreshold": t.integer().optional(),
            "checkInterval": t.string().optional(),
            "restartThreshold": t.integer().optional(),
            "timeout": t.string().optional(),
            "disableHealthCheck": t.boolean().optional(),
            "unhealthyThreshold": t.integer().optional(),
        }
    ).named(renames["HealthCheckIn"])
    types["HealthCheckOut"] = t.struct(
        {
            "host": t.string().optional(),
            "healthyThreshold": t.integer().optional(),
            "checkInterval": t.string().optional(),
            "restartThreshold": t.integer().optional(),
            "timeout": t.string().optional(),
            "disableHealthCheck": t.boolean().optional(),
            "unhealthyThreshold": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HealthCheckOut"])
    types["BatchUpdateIngressRulesResponseIn"] = t.struct(
        {"ingressRules": t.array(t.proxy(renames["FirewallRuleIn"])).optional()}
    ).named(renames["BatchUpdateIngressRulesResponseIn"])
    types["BatchUpdateIngressRulesResponseOut"] = t.struct(
        {
            "ingressRules": t.array(t.proxy(renames["FirewallRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateIngressRulesResponseOut"])
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
    types["CloudBuildOptionsIn"] = t.struct(
        {
            "cloudBuildTimeout": t.string().optional(),
            "appYamlPath": t.string().optional(),
        }
    ).named(renames["CloudBuildOptionsIn"])
    types["CloudBuildOptionsOut"] = t.struct(
        {
            "cloudBuildTimeout": t.string().optional(),
            "appYamlPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudBuildOptionsOut"])
    types["BatchUpdateIngressRulesRequestIn"] = t.struct(
        {"ingressRules": t.array(t.proxy(renames["FirewallRuleIn"])).optional()}
    ).named(renames["BatchUpdateIngressRulesRequestIn"])
    types["BatchUpdateIngressRulesRequestOut"] = t.struct(
        {
            "ingressRules": t.array(t.proxy(renames["FirewallRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateIngressRulesRequestOut"])
    types["OperationMetadataV1In"] = t.struct(
        {
            "warning": t.array(t.string()).optional(),
            "insertTime": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "user": t.string().optional(),
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1In"]),
            "method": t.string().optional(),
        }
    ).named(renames["OperationMetadataV1In"])
    types["OperationMetadataV1Out"] = t.struct(
        {
            "warning": t.array(t.string()).optional(),
            "insertTime": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "user": t.string().optional(),
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1Out"]),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Out"])
    types["NetworkSettingsIn"] = t.struct(
        {"ingressTrafficAllowed": t.string().optional()}
    ).named(renames["NetworkSettingsIn"])
    types["NetworkSettingsOut"] = t.struct(
        {
            "ingressTrafficAllowed": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkSettingsOut"])
    types["EntrypointIn"] = t.struct({"shell": t.string().optional()}).named(
        renames["EntrypointIn"]
    )
    types["EntrypointOut"] = t.struct(
        {
            "shell": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntrypointOut"])
    types["ListIngressRulesResponseIn"] = t.struct(
        {
            "ingressRules": t.array(t.proxy(renames["FirewallRuleIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListIngressRulesResponseIn"])
    types["ListIngressRulesResponseOut"] = t.struct(
        {
            "ingressRules": t.array(t.proxy(renames["FirewallRuleOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListIngressRulesResponseOut"])
    types["FileInfoIn"] = t.struct(
        {
            "sourceUrl": t.string().optional(),
            "sha1Sum": t.string().optional(),
            "mimeType": t.string().optional(),
        }
    ).named(renames["FileInfoIn"])
    types["FileInfoOut"] = t.struct(
        {
            "sourceUrl": t.string().optional(),
            "sha1Sum": t.string().optional(),
            "mimeType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FileInfoOut"])
    types["SslSettingsIn"] = t.struct(
        {
            "pendingManagedCertificateId": t.string().optional(),
            "sslManagementType": t.string().optional(),
            "certificateId": t.string().optional(),
        }
    ).named(renames["SslSettingsIn"])
    types["SslSettingsOut"] = t.struct(
        {
            "pendingManagedCertificateId": t.string().optional(),
            "sslManagementType": t.string().optional(),
            "certificateId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslSettingsOut"])
    types["NetworkIn"] = t.struct(
        {
            "instanceTag": t.string().optional(),
            "name": t.string().optional(),
            "forwardedPorts": t.array(t.string()).optional(),
            "instanceIpMode": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "subnetworkName": t.string().optional(),
        }
    ).named(renames["NetworkIn"])
    types["NetworkOut"] = t.struct(
        {
            "instanceTag": t.string().optional(),
            "name": t.string().optional(),
            "forwardedPorts": t.array(t.string()).optional(),
            "instanceIpMode": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "subnetworkName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkOut"])
    types["ReadinessCheckIn"] = t.struct(
        {
            "failureThreshold": t.integer().optional(),
            "successThreshold": t.integer().optional(),
            "checkInterval": t.string().optional(),
            "appStartTimeout": t.string().optional(),
            "host": t.string().optional(),
            "path": t.string().optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["ReadinessCheckIn"])
    types["ReadinessCheckOut"] = t.struct(
        {
            "failureThreshold": t.integer().optional(),
            "successThreshold": t.integer().optional(),
            "checkInterval": t.string().optional(),
            "appStartTimeout": t.string().optional(),
            "host": t.string().optional(),
            "path": t.string().optional(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadinessCheckOut"])
    types["ZipInfoIn"] = t.struct(
        {"filesCount": t.integer().optional(), "sourceUrl": t.string().optional()}
    ).named(renames["ZipInfoIn"])
    types["ZipInfoOut"] = t.struct(
        {
            "filesCount": t.integer().optional(),
            "sourceUrl": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZipInfoOut"])
    types["ContainerInfoIn"] = t.struct({"image": t.string().optional()}).named(
        renames["ContainerInfoIn"]
    )
    types["ContainerInfoOut"] = t.struct(
        {
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerInfoOut"])
    types["NetworkUtilizationIn"] = t.struct(
        {
            "targetSentBytesPerSecond": t.integer().optional(),
            "targetReceivedPacketsPerSecond": t.integer().optional(),
            "targetSentPacketsPerSecond": t.integer().optional(),
            "targetReceivedBytesPerSecond": t.integer().optional(),
        }
    ).named(renames["NetworkUtilizationIn"])
    types["NetworkUtilizationOut"] = t.struct(
        {
            "targetSentBytesPerSecond": t.integer().optional(),
            "targetReceivedPacketsPerSecond": t.integer().optional(),
            "targetSentPacketsPerSecond": t.integer().optional(),
            "targetReceivedBytesPerSecond": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkUtilizationOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])

    functions = {}
    functions["appsRepair"] = appengine.get(
        "v1/apps/{appsId}",
        t.struct({"appsId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsPatch"] = appengine.get(
        "v1/apps/{appsId}",
        t.struct({"appsId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsCreate"] = appengine.get(
        "v1/apps/{appsId}",
        t.struct({"appsId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsGet"] = appengine.get(
        "v1/apps/{appsId}",
        t.struct({"appsId": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ApplicationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsAuthorizedCertificatesGet"] = appengine.delete(
        "v1/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}",
        t.struct(
            {
                "authorizedCertificatesId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsAuthorizedCertificatesCreate"] = appengine.delete(
        "v1/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}",
        t.struct(
            {
                "authorizedCertificatesId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsAuthorizedCertificatesList"] = appengine.delete(
        "v1/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}",
        t.struct(
            {
                "authorizedCertificatesId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsAuthorizedCertificatesPatch"] = appengine.delete(
        "v1/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}",
        t.struct(
            {
                "authorizedCertificatesId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsAuthorizedCertificatesDelete"] = appengine.delete(
        "v1/apps/{appsId}/authorizedCertificates/{authorizedCertificatesId}",
        t.struct(
            {
                "authorizedCertificatesId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsFirewallIngressRulesGet"] = appengine.get(
        "v1/apps/{appsId}/firewall/ingressRules",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "appsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matchingAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIngressRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsFirewallIngressRulesDelete"] = appengine.get(
        "v1/apps/{appsId}/firewall/ingressRules",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "appsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matchingAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIngressRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsFirewallIngressRulesPatch"] = appengine.get(
        "v1/apps/{appsId}/firewall/ingressRules",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "appsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matchingAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIngressRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsFirewallIngressRulesBatchUpdate"] = appengine.get(
        "v1/apps/{appsId}/firewall/ingressRules",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "appsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matchingAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIngressRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsFirewallIngressRulesCreate"] = appengine.get(
        "v1/apps/{appsId}/firewall/ingressRules",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "appsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matchingAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIngressRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsFirewallIngressRulesList"] = appengine.get(
        "v1/apps/{appsId}/firewall/ingressRules",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "appsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "matchingAddress": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIngressRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsLocationsList"] = appengine.get(
        "v1/apps/{appsId}/locations/{locationsId}",
        t.struct(
            {
                "locationsId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsLocationsGet"] = appengine.get(
        "v1/apps/{appsId}/locations/{locationsId}",
        t.struct(
            {
                "locationsId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsGet"] = appengine.get(
        "v1/apps/{appsId}/domainMappings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDomainMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsPatch"] = appengine.get(
        "v1/apps/{appsId}/domainMappings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDomainMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsCreate"] = appengine.get(
        "v1/apps/{appsId}/domainMappings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDomainMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsDelete"] = appengine.get(
        "v1/apps/{appsId}/domainMappings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDomainMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsList"] = appengine.get(
        "v1/apps/{appsId}/domainMappings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDomainMappingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsAuthorizedDomainsList"] = appengine.get(
        "v1/apps/{appsId}/authorizedDomains",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "appsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAuthorizedDomainsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsOperationsList"] = appengine.get(
        "v1/apps/{appsId}/operations/{operationsId}",
        t.struct(
            {
                "operationsId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsOperationsGet"] = appengine.get(
        "v1/apps/{appsId}/operations/{operationsId}",
        t.struct(
            {
                "operationsId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesPatch"] = appengine.get(
        "v1/apps/{appsId}/services/{servicesId}",
        t.struct(
            {
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesList"] = appengine.get(
        "v1/apps/{appsId}/services/{servicesId}",
        t.struct(
            {
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesDelete"] = appengine.get(
        "v1/apps/{appsId}/services/{servicesId}",
        t.struct(
            {
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesGet"] = appengine.get(
        "v1/apps/{appsId}/services/{servicesId}",
        t.struct(
            {
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsList"] = appengine.delete(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "servicesId": t.string().optional(),
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsCreate"] = appengine.delete(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "servicesId": t.string().optional(),
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsPatch"] = appengine.delete(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "servicesId": t.string().optional(),
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsGet"] = appengine.delete(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "servicesId": t.string().optional(),
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsDelete"] = appengine.delete(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "servicesId": t.string().optional(),
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsInstancesList"] = appengine.post(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}:debug",
        t.struct(
            {
                "versionsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "appsId": t.string().optional(),
                "instancesId": t.string().optional(),
                "sshKey": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsInstancesGet"] = appengine.post(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}:debug",
        t.struct(
            {
                "versionsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "appsId": t.string().optional(),
                "instancesId": t.string().optional(),
                "sshKey": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsInstancesDelete"] = appengine.post(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}:debug",
        t.struct(
            {
                "versionsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "appsId": t.string().optional(),
                "instancesId": t.string().optional(),
                "sshKey": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsInstancesDebug"] = appengine.post(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}:debug",
        t.struct(
            {
                "versionsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "appsId": t.string().optional(),
                "instancesId": t.string().optional(),
                "sshKey": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApplicationsGet"] = appengine.post(
        "v1/projects/{projectsId}/locations/{locationsId}/applications",
        t.struct(
            {
                "locationsId": t.string().optional(),
                "projectsId": t.string().optional(),
                "id": t.string().optional(),
                "iap": t.proxy(renames["IdentityAwareProxyIn"]),
                "servingStatus": t.string().optional(),
                "dispatchRules": t.array(
                    t.proxy(renames["UrlDispatchRuleIn"])
                ).optional(),
                "authDomain": t.string().optional(),
                "databaseType": t.string().optional(),
                "locationId": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "featureSettings": t.proxy(renames["FeatureSettingsIn"]).optional(),
                "defaultCookieExpiration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApplicationsCreate"] = appengine.post(
        "v1/projects/{projectsId}/locations/{locationsId}/applications",
        t.struct(
            {
                "locationsId": t.string().optional(),
                "projectsId": t.string().optional(),
                "id": t.string().optional(),
                "iap": t.proxy(renames["IdentityAwareProxyIn"]),
                "servingStatus": t.string().optional(),
                "dispatchRules": t.array(
                    t.proxy(renames["UrlDispatchRuleIn"])
                ).optional(),
                "authDomain": t.string().optional(),
                "databaseType": t.string().optional(),
                "locationId": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "featureSettings": t.proxy(renames["FeatureSettingsIn"]).optional(),
                "defaultCookieExpiration": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="appengine",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
