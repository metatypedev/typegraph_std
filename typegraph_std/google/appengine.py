from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_appengine():
    appengine = HTTPRuntime("https://appengine.googleapis.com/")

    renames = {
        "ErrorResponse": "_appengine_1_ErrorResponse",
        "BatchUpdateIngressRulesRequestIn": "_appengine_2_BatchUpdateIngressRulesRequestIn",
        "BatchUpdateIngressRulesRequestOut": "_appengine_3_BatchUpdateIngressRulesRequestOut",
        "ServiceIn": "_appengine_4_ServiceIn",
        "ServiceOut": "_appengine_5_ServiceOut",
        "ListVersionsResponseIn": "_appengine_6_ListVersionsResponseIn",
        "ListVersionsResponseOut": "_appengine_7_ListVersionsResponseOut",
        "AuthorizedCertificateIn": "_appengine_8_AuthorizedCertificateIn",
        "AuthorizedCertificateOut": "_appengine_9_AuthorizedCertificateOut",
        "CertificateRawDataIn": "_appengine_10_CertificateRawDataIn",
        "CertificateRawDataOut": "_appengine_11_CertificateRawDataOut",
        "ListAuthorizedDomainsResponseIn": "_appengine_12_ListAuthorizedDomainsResponseIn",
        "ListAuthorizedDomainsResponseOut": "_appengine_13_ListAuthorizedDomainsResponseOut",
        "DiskUtilizationIn": "_appengine_14_DiskUtilizationIn",
        "DiskUtilizationOut": "_appengine_15_DiskUtilizationOut",
        "ApiConfigHandlerIn": "_appengine_16_ApiConfigHandlerIn",
        "ApiConfigHandlerOut": "_appengine_17_ApiConfigHandlerOut",
        "VersionIn": "_appengine_18_VersionIn",
        "VersionOut": "_appengine_19_VersionOut",
        "AutomaticScalingIn": "_appengine_20_AutomaticScalingIn",
        "AutomaticScalingOut": "_appengine_21_AutomaticScalingOut",
        "ScriptHandlerIn": "_appengine_22_ScriptHandlerIn",
        "ScriptHandlerOut": "_appengine_23_ScriptHandlerOut",
        "EntrypointIn": "_appengine_24_EntrypointIn",
        "EntrypointOut": "_appengine_25_EntrypointOut",
        "FlexibleRuntimeSettingsIn": "_appengine_26_FlexibleRuntimeSettingsIn",
        "FlexibleRuntimeSettingsOut": "_appengine_27_FlexibleRuntimeSettingsOut",
        "NetworkSettingsIn": "_appengine_28_NetworkSettingsIn",
        "NetworkSettingsOut": "_appengine_29_NetworkSettingsOut",
        "NetworkIn": "_appengine_30_NetworkIn",
        "NetworkOut": "_appengine_31_NetworkOut",
        "ProjectsMetadataIn": "_appengine_32_ProjectsMetadataIn",
        "ProjectsMetadataOut": "_appengine_33_ProjectsMetadataOut",
        "SslSettingsIn": "_appengine_34_SslSettingsIn",
        "SslSettingsOut": "_appengine_35_SslSettingsOut",
        "ReasonsIn": "_appengine_36_ReasonsIn",
        "ReasonsOut": "_appengine_37_ReasonsOut",
        "NetworkUtilizationIn": "_appengine_38_NetworkUtilizationIn",
        "NetworkUtilizationOut": "_appengine_39_NetworkUtilizationOut",
        "ListOperationsResponseIn": "_appengine_40_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_appengine_41_ListOperationsResponseOut",
        "DomainMappingIn": "_appengine_42_DomainMappingIn",
        "DomainMappingOut": "_appengine_43_DomainMappingOut",
        "CreateVersionMetadataV1In": "_appengine_44_CreateVersionMetadataV1In",
        "CreateVersionMetadataV1Out": "_appengine_45_CreateVersionMetadataV1Out",
        "OperationIn": "_appengine_46_OperationIn",
        "OperationOut": "_appengine_47_OperationOut",
        "InstanceIn": "_appengine_48_InstanceIn",
        "InstanceOut": "_appengine_49_InstanceOut",
        "CloudBuildOptionsIn": "_appengine_50_CloudBuildOptionsIn",
        "CloudBuildOptionsOut": "_appengine_51_CloudBuildOptionsOut",
        "RequestUtilizationIn": "_appengine_52_RequestUtilizationIn",
        "RequestUtilizationOut": "_appengine_53_RequestUtilizationOut",
        "StandardSchedulerSettingsIn": "_appengine_54_StandardSchedulerSettingsIn",
        "StandardSchedulerSettingsOut": "_appengine_55_StandardSchedulerSettingsOut",
        "ManualScalingIn": "_appengine_56_ManualScalingIn",
        "ManualScalingOut": "_appengine_57_ManualScalingOut",
        "LivenessCheckIn": "_appengine_58_LivenessCheckIn",
        "LivenessCheckOut": "_appengine_59_LivenessCheckOut",
        "ListIngressRulesResponseIn": "_appengine_60_ListIngressRulesResponseIn",
        "ListIngressRulesResponseOut": "_appengine_61_ListIngressRulesResponseOut",
        "ReadinessCheckIn": "_appengine_62_ReadinessCheckIn",
        "ReadinessCheckOut": "_appengine_63_ReadinessCheckOut",
        "CreateVersionMetadataV1AlphaIn": "_appengine_64_CreateVersionMetadataV1AlphaIn",
        "CreateVersionMetadataV1AlphaOut": "_appengine_65_CreateVersionMetadataV1AlphaOut",
        "ErrorHandlerIn": "_appengine_66_ErrorHandlerIn",
        "ErrorHandlerOut": "_appengine_67_ErrorHandlerOut",
        "EndpointsApiServiceIn": "_appengine_68_EndpointsApiServiceIn",
        "EndpointsApiServiceOut": "_appengine_69_EndpointsApiServiceOut",
        "ApiEndpointHandlerIn": "_appengine_70_ApiEndpointHandlerIn",
        "ApiEndpointHandlerOut": "_appengine_71_ApiEndpointHandlerOut",
        "ProjectStateIn": "_appengine_72_ProjectStateIn",
        "ProjectStateOut": "_appengine_73_ProjectStateOut",
        "FeatureSettingsIn": "_appengine_74_FeatureSettingsIn",
        "FeatureSettingsOut": "_appengine_75_FeatureSettingsOut",
        "LibraryIn": "_appengine_76_LibraryIn",
        "LibraryOut": "_appengine_77_LibraryOut",
        "VolumeIn": "_appengine_78_VolumeIn",
        "VolumeOut": "_appengine_79_VolumeOut",
        "ZipInfoIn": "_appengine_80_ZipInfoIn",
        "ZipInfoOut": "_appengine_81_ZipInfoOut",
        "RepairApplicationRequestIn": "_appengine_82_RepairApplicationRequestIn",
        "RepairApplicationRequestOut": "_appengine_83_RepairApplicationRequestOut",
        "LocationMetadataIn": "_appengine_84_LocationMetadataIn",
        "LocationMetadataOut": "_appengine_85_LocationMetadataOut",
        "ListLocationsResponseIn": "_appengine_86_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_appengine_87_ListLocationsResponseOut",
        "UrlDispatchRuleIn": "_appengine_88_UrlDispatchRuleIn",
        "UrlDispatchRuleOut": "_appengine_89_UrlDispatchRuleOut",
        "ListInstancesResponseIn": "_appengine_90_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_appengine_91_ListInstancesResponseOut",
        "FileInfoIn": "_appengine_92_FileInfoIn",
        "FileInfoOut": "_appengine_93_FileInfoOut",
        "CreateVersionMetadataV1BetaIn": "_appengine_94_CreateVersionMetadataV1BetaIn",
        "CreateVersionMetadataV1BetaOut": "_appengine_95_CreateVersionMetadataV1BetaOut",
        "ResourcesIn": "_appengine_96_ResourcesIn",
        "ResourcesOut": "_appengine_97_ResourcesOut",
        "LocationIn": "_appengine_98_LocationIn",
        "LocationOut": "_appengine_99_LocationOut",
        "BasicScalingIn": "_appengine_100_BasicScalingIn",
        "BasicScalingOut": "_appengine_101_BasicScalingOut",
        "ListAuthorizedCertificatesResponseIn": "_appengine_102_ListAuthorizedCertificatesResponseIn",
        "ListAuthorizedCertificatesResponseOut": "_appengine_103_ListAuthorizedCertificatesResponseOut",
        "FirewallRuleIn": "_appengine_104_FirewallRuleIn",
        "FirewallRuleOut": "_appengine_105_FirewallRuleOut",
        "OperationMetadataV1BetaIn": "_appengine_106_OperationMetadataV1BetaIn",
        "OperationMetadataV1BetaOut": "_appengine_107_OperationMetadataV1BetaOut",
        "DeploymentIn": "_appengine_108_DeploymentIn",
        "DeploymentOut": "_appengine_109_DeploymentOut",
        "CpuUtilizationIn": "_appengine_110_CpuUtilizationIn",
        "CpuUtilizationOut": "_appengine_111_CpuUtilizationOut",
        "TrafficSplitIn": "_appengine_112_TrafficSplitIn",
        "TrafficSplitOut": "_appengine_113_TrafficSplitOut",
        "DebugInstanceRequestIn": "_appengine_114_DebugInstanceRequestIn",
        "DebugInstanceRequestOut": "_appengine_115_DebugInstanceRequestOut",
        "ResourceRecordIn": "_appengine_116_ResourceRecordIn",
        "ResourceRecordOut": "_appengine_117_ResourceRecordOut",
        "OperationMetadataV1AlphaIn": "_appengine_118_OperationMetadataV1AlphaIn",
        "OperationMetadataV1AlphaOut": "_appengine_119_OperationMetadataV1AlphaOut",
        "ProjectEventIn": "_appengine_120_ProjectEventIn",
        "ProjectEventOut": "_appengine_121_ProjectEventOut",
        "IdentityAwareProxyIn": "_appengine_122_IdentityAwareProxyIn",
        "IdentityAwareProxyOut": "_appengine_123_IdentityAwareProxyOut",
        "UrlMapIn": "_appengine_124_UrlMapIn",
        "UrlMapOut": "_appengine_125_UrlMapOut",
        "StatusIn": "_appengine_126_StatusIn",
        "StatusOut": "_appengine_127_StatusOut",
        "StaticFilesHandlerIn": "_appengine_128_StaticFilesHandlerIn",
        "StaticFilesHandlerOut": "_appengine_129_StaticFilesHandlerOut",
        "GoogleAppengineV1betaLocationMetadataIn": "_appengine_130_GoogleAppengineV1betaLocationMetadataIn",
        "GoogleAppengineV1betaLocationMetadataOut": "_appengine_131_GoogleAppengineV1betaLocationMetadataOut",
        "ContainerInfoIn": "_appengine_132_ContainerInfoIn",
        "ContainerInfoOut": "_appengine_133_ContainerInfoOut",
        "AuthorizedDomainIn": "_appengine_134_AuthorizedDomainIn",
        "AuthorizedDomainOut": "_appengine_135_AuthorizedDomainOut",
        "OperationMetadataV1In": "_appengine_136_OperationMetadataV1In",
        "OperationMetadataV1Out": "_appengine_137_OperationMetadataV1Out",
        "ManagedCertificateIn": "_appengine_138_ManagedCertificateIn",
        "ManagedCertificateOut": "_appengine_139_ManagedCertificateOut",
        "ApplicationIn": "_appengine_140_ApplicationIn",
        "ApplicationOut": "_appengine_141_ApplicationOut",
        "BatchUpdateIngressRulesResponseIn": "_appengine_142_BatchUpdateIngressRulesResponseIn",
        "BatchUpdateIngressRulesResponseOut": "_appengine_143_BatchUpdateIngressRulesResponseOut",
        "ListDomainMappingsResponseIn": "_appengine_144_ListDomainMappingsResponseIn",
        "ListDomainMappingsResponseOut": "_appengine_145_ListDomainMappingsResponseOut",
        "VpcAccessConnectorIn": "_appengine_146_VpcAccessConnectorIn",
        "VpcAccessConnectorOut": "_appengine_147_VpcAccessConnectorOut",
        "EmptyIn": "_appengine_148_EmptyIn",
        "EmptyOut": "_appengine_149_EmptyOut",
        "ListServicesResponseIn": "_appengine_150_ListServicesResponseIn",
        "ListServicesResponseOut": "_appengine_151_ListServicesResponseOut",
        "HealthCheckIn": "_appengine_152_HealthCheckIn",
        "HealthCheckOut": "_appengine_153_HealthCheckOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BatchUpdateIngressRulesRequestIn"] = t.struct(
        {"ingressRules": t.array(t.proxy(renames["FirewallRuleIn"])).optional()}
    ).named(renames["BatchUpdateIngressRulesRequestIn"])
    types["BatchUpdateIngressRulesRequestOut"] = t.struct(
        {
            "ingressRules": t.array(t.proxy(renames["FirewallRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateIngressRulesRequestOut"])
    types["ServiceIn"] = t.struct(
        {
            "id": t.string().optional(),
            "split": t.proxy(renames["TrafficSplitIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "networkSettings": t.proxy(renames["NetworkSettingsIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ServiceIn"])
    types["ServiceOut"] = t.struct(
        {
            "id": t.string().optional(),
            "split": t.proxy(renames["TrafficSplitOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "networkSettings": t.proxy(renames["NetworkSettingsOut"]).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceOut"])
    types["ListVersionsResponseIn"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VersionIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVersionsResponseIn"])
    types["ListVersionsResponseOut"] = t.struct(
        {
            "versions": t.array(t.proxy(renames["VersionOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVersionsResponseOut"])
    types["AuthorizedCertificateIn"] = t.struct(
        {
            "name": t.string().optional(),
            "domainNames": t.array(t.string()).optional(),
            "domainMappingsCount": t.integer().optional(),
            "expireTime": t.string().optional(),
            "visibleDomainMappings": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "certificateRawData": t.proxy(renames["CertificateRawDataIn"]).optional(),
            "displayName": t.string().optional(),
            "managedCertificate": t.proxy(renames["ManagedCertificateIn"]).optional(),
        }
    ).named(renames["AuthorizedCertificateIn"])
    types["AuthorizedCertificateOut"] = t.struct(
        {
            "name": t.string().optional(),
            "domainNames": t.array(t.string()).optional(),
            "domainMappingsCount": t.integer().optional(),
            "expireTime": t.string().optional(),
            "visibleDomainMappings": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "certificateRawData": t.proxy(renames["CertificateRawDataOut"]).optional(),
            "displayName": t.string().optional(),
            "managedCertificate": t.proxy(renames["ManagedCertificateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedCertificateOut"])
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
    types["DiskUtilizationIn"] = t.struct(
        {
            "targetWriteBytesPerSecond": t.integer().optional(),
            "targetWriteOpsPerSecond": t.integer().optional(),
            "targetReadOpsPerSecond": t.integer().optional(),
            "targetReadBytesPerSecond": t.integer().optional(),
        }
    ).named(renames["DiskUtilizationIn"])
    types["DiskUtilizationOut"] = t.struct(
        {
            "targetWriteBytesPerSecond": t.integer().optional(),
            "targetWriteOpsPerSecond": t.integer().optional(),
            "targetReadOpsPerSecond": t.integer().optional(),
            "targetReadBytesPerSecond": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DiskUtilizationOut"])
    types["ApiConfigHandlerIn"] = t.struct(
        {
            "securityLevel": t.string().optional(),
            "login": t.string().optional(),
            "url": t.string().optional(),
            "script": t.string().optional(),
            "authFailAction": t.string().optional(),
        }
    ).named(renames["ApiConfigHandlerIn"])
    types["ApiConfigHandlerOut"] = t.struct(
        {
            "securityLevel": t.string().optional(),
            "login": t.string().optional(),
            "url": t.string().optional(),
            "script": t.string().optional(),
            "authFailAction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiConfigHandlerOut"])
    types["VersionIn"] = t.struct(
        {
            "servingStatus": t.string().optional(),
            "endpointsApiService": t.proxy(renames["EndpointsApiServiceIn"]).optional(),
            "instanceClass": t.string().optional(),
            "libraries": t.array(t.proxy(renames["LibraryIn"])).optional(),
            "env": t.string().optional(),
            "nobuildFilesRegex": t.string().optional(),
            "manualScaling": t.proxy(renames["ManualScalingIn"]).optional(),
            "handlers": t.array(t.proxy(renames["UrlMapIn"])).optional(),
            "errorHandlers": t.array(t.proxy(renames["ErrorHandlerIn"])).optional(),
            "runtimeApiVersion": t.string().optional(),
            "betaSettings": t.struct({"_": t.string().optional()}).optional(),
            "runtimeMainExecutablePath": t.string().optional(),
            "vpcAccessConnector": t.proxy(renames["VpcAccessConnectorIn"]).optional(),
            "createTime": t.string().optional(),
            "runtime": t.string().optional(),
            "createdBy": t.string().optional(),
            "id": t.string().optional(),
            "automaticScaling": t.proxy(renames["AutomaticScalingIn"]).optional(),
            "basicScaling": t.proxy(renames["BasicScalingIn"]).optional(),
            "healthCheck": t.proxy(renames["HealthCheckIn"]).optional(),
            "versionUrl": t.string().optional(),
            "readinessCheck": t.proxy(renames["ReadinessCheckIn"]).optional(),
            "entrypoint": t.proxy(renames["EntrypointIn"]).optional(),
            "serviceAccount": t.string().optional(),
            "buildEnvVariables": t.struct({"_": t.string().optional()}).optional(),
            "apiConfig": t.proxy(renames["ApiConfigHandlerIn"]).optional(),
            "threadsafe": t.boolean().optional(),
            "name": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentIn"]).optional(),
            "appEngineApis": t.boolean().optional(),
            "inboundServices": t.array(t.string()).optional(),
            "diskUsageBytes": t.string().optional(),
            "livenessCheck": t.proxy(renames["LivenessCheckIn"]).optional(),
            "flexibleRuntimeSettings": t.proxy(
                renames["FlexibleRuntimeSettingsIn"]
            ).optional(),
            "defaultExpiration": t.string().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "zones": t.array(t.string()).optional(),
            "network": t.proxy(renames["NetworkIn"]).optional(),
            "resources": t.proxy(renames["ResourcesIn"]).optional(),
            "runtimeChannel": t.string().optional(),
            "vm": t.boolean().optional(),
        }
    ).named(renames["VersionIn"])
    types["VersionOut"] = t.struct(
        {
            "servingStatus": t.string().optional(),
            "endpointsApiService": t.proxy(
                renames["EndpointsApiServiceOut"]
            ).optional(),
            "instanceClass": t.string().optional(),
            "libraries": t.array(t.proxy(renames["LibraryOut"])).optional(),
            "env": t.string().optional(),
            "nobuildFilesRegex": t.string().optional(),
            "manualScaling": t.proxy(renames["ManualScalingOut"]).optional(),
            "handlers": t.array(t.proxy(renames["UrlMapOut"])).optional(),
            "errorHandlers": t.array(t.proxy(renames["ErrorHandlerOut"])).optional(),
            "runtimeApiVersion": t.string().optional(),
            "betaSettings": t.struct({"_": t.string().optional()}).optional(),
            "runtimeMainExecutablePath": t.string().optional(),
            "vpcAccessConnector": t.proxy(renames["VpcAccessConnectorOut"]).optional(),
            "createTime": t.string().optional(),
            "runtime": t.string().optional(),
            "createdBy": t.string().optional(),
            "id": t.string().optional(),
            "automaticScaling": t.proxy(renames["AutomaticScalingOut"]).optional(),
            "basicScaling": t.proxy(renames["BasicScalingOut"]).optional(),
            "healthCheck": t.proxy(renames["HealthCheckOut"]).optional(),
            "versionUrl": t.string().optional(),
            "readinessCheck": t.proxy(renames["ReadinessCheckOut"]).optional(),
            "entrypoint": t.proxy(renames["EntrypointOut"]).optional(),
            "serviceAccount": t.string().optional(),
            "buildEnvVariables": t.struct({"_": t.string().optional()}).optional(),
            "apiConfig": t.proxy(renames["ApiConfigHandlerOut"]).optional(),
            "threadsafe": t.boolean().optional(),
            "name": t.string().optional(),
            "deployment": t.proxy(renames["DeploymentOut"]).optional(),
            "appEngineApis": t.boolean().optional(),
            "inboundServices": t.array(t.string()).optional(),
            "diskUsageBytes": t.string().optional(),
            "livenessCheck": t.proxy(renames["LivenessCheckOut"]).optional(),
            "flexibleRuntimeSettings": t.proxy(
                renames["FlexibleRuntimeSettingsOut"]
            ).optional(),
            "defaultExpiration": t.string().optional(),
            "envVariables": t.struct({"_": t.string().optional()}).optional(),
            "zones": t.array(t.string()).optional(),
            "network": t.proxy(renames["NetworkOut"]).optional(),
            "resources": t.proxy(renames["ResourcesOut"]).optional(),
            "runtimeChannel": t.string().optional(),
            "vm": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VersionOut"])
    types["AutomaticScalingIn"] = t.struct(
        {
            "minPendingLatency": t.string().optional(),
            "coolDownPeriod": t.string().optional(),
            "minIdleInstances": t.integer().optional(),
            "maxPendingLatency": t.string().optional(),
            "cpuUtilization": t.proxy(renames["CpuUtilizationIn"]).optional(),
            "maxIdleInstances": t.integer().optional(),
            "standardSchedulerSettings": t.proxy(
                renames["StandardSchedulerSettingsIn"]
            ).optional(),
            "minTotalInstances": t.integer().optional(),
            "diskUtilization": t.proxy(renames["DiskUtilizationIn"]).optional(),
            "networkUtilization": t.proxy(renames["NetworkUtilizationIn"]).optional(),
            "maxTotalInstances": t.integer().optional(),
            "maxConcurrentRequests": t.integer().optional(),
            "requestUtilization": t.proxy(renames["RequestUtilizationIn"]).optional(),
        }
    ).named(renames["AutomaticScalingIn"])
    types["AutomaticScalingOut"] = t.struct(
        {
            "minPendingLatency": t.string().optional(),
            "coolDownPeriod": t.string().optional(),
            "minIdleInstances": t.integer().optional(),
            "maxPendingLatency": t.string().optional(),
            "cpuUtilization": t.proxy(renames["CpuUtilizationOut"]).optional(),
            "maxIdleInstances": t.integer().optional(),
            "standardSchedulerSettings": t.proxy(
                renames["StandardSchedulerSettingsOut"]
            ).optional(),
            "minTotalInstances": t.integer().optional(),
            "diskUtilization": t.proxy(renames["DiskUtilizationOut"]).optional(),
            "networkUtilization": t.proxy(renames["NetworkUtilizationOut"]).optional(),
            "maxTotalInstances": t.integer().optional(),
            "maxConcurrentRequests": t.integer().optional(),
            "requestUtilization": t.proxy(renames["RequestUtilizationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AutomaticScalingOut"])
    types["ScriptHandlerIn"] = t.struct({"scriptPath": t.string().optional()}).named(
        renames["ScriptHandlerIn"]
    )
    types["ScriptHandlerOut"] = t.struct(
        {
            "scriptPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScriptHandlerOut"])
    types["EntrypointIn"] = t.struct({"shell": t.string().optional()}).named(
        renames["EntrypointIn"]
    )
    types["EntrypointOut"] = t.struct(
        {
            "shell": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntrypointOut"])
    types["FlexibleRuntimeSettingsIn"] = t.struct(
        {
            "operatingSystem": t.string().optional(),
            "runtimeVersion": t.string().optional(),
        }
    ).named(renames["FlexibleRuntimeSettingsIn"])
    types["FlexibleRuntimeSettingsOut"] = t.struct(
        {
            "operatingSystem": t.string().optional(),
            "runtimeVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FlexibleRuntimeSettingsOut"])
    types["NetworkSettingsIn"] = t.struct(
        {"ingressTrafficAllowed": t.string().optional()}
    ).named(renames["NetworkSettingsIn"])
    types["NetworkSettingsOut"] = t.struct(
        {
            "ingressTrafficAllowed": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkSettingsOut"])
    types["NetworkIn"] = t.struct(
        {
            "subnetworkName": t.string().optional(),
            "name": t.string().optional(),
            "instanceIpMode": t.string().optional(),
            "forwardedPorts": t.array(t.string()).optional(),
            "instanceTag": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
        }
    ).named(renames["NetworkIn"])
    types["NetworkOut"] = t.struct(
        {
            "subnetworkName": t.string().optional(),
            "name": t.string().optional(),
            "instanceIpMode": t.string().optional(),
            "forwardedPorts": t.array(t.string()).optional(),
            "instanceTag": t.string().optional(),
            "sessionAffinity": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkOut"])
    types["ProjectsMetadataIn"] = t.struct(
        {
            "consumerProjectNumber": t.string().optional(),
            "producerProjectNumber": t.string().optional(),
            "consumerProjectState": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "producerProjectId": t.string().optional(),
            "p4ServiceAccount": t.string().optional(),
            "consumerProjectId": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
        }
    ).named(renames["ProjectsMetadataIn"])
    types["ProjectsMetadataOut"] = t.struct(
        {
            "consumerProjectNumber": t.string().optional(),
            "producerProjectNumber": t.string().optional(),
            "consumerProjectState": t.string().optional(),
            "tenantProjectId": t.string().optional(),
            "producerProjectId": t.string().optional(),
            "p4ServiceAccount": t.string().optional(),
            "consumerProjectId": t.string().optional(),
            "tenantProjectNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectsMetadataOut"])
    types["SslSettingsIn"] = t.struct(
        {
            "pendingManagedCertificateId": t.string().optional(),
            "certificateId": t.string().optional(),
            "sslManagementType": t.string().optional(),
        }
    ).named(renames["SslSettingsIn"])
    types["SslSettingsOut"] = t.struct(
        {
            "pendingManagedCertificateId": t.string().optional(),
            "certificateId": t.string().optional(),
            "sslManagementType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SslSettingsOut"])
    types["ReasonsIn"] = t.struct(
        {
            "abuse": t.string(),
            "billing": t.string(),
            "dataGovernance": t.string(),
            "serviceManagement": t.string(),
        }
    ).named(renames["ReasonsIn"])
    types["ReasonsOut"] = t.struct(
        {
            "abuse": t.string(),
            "billing": t.string(),
            "dataGovernance": t.string(),
            "serviceManagement": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReasonsOut"])
    types["NetworkUtilizationIn"] = t.struct(
        {
            "targetSentPacketsPerSecond": t.integer().optional(),
            "targetReceivedBytesPerSecond": t.integer().optional(),
            "targetReceivedPacketsPerSecond": t.integer().optional(),
            "targetSentBytesPerSecond": t.integer().optional(),
        }
    ).named(renames["NetworkUtilizationIn"])
    types["NetworkUtilizationOut"] = t.struct(
        {
            "targetSentPacketsPerSecond": t.integer().optional(),
            "targetReceivedBytesPerSecond": t.integer().optional(),
            "targetReceivedPacketsPerSecond": t.integer().optional(),
            "targetSentBytesPerSecond": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkUtilizationOut"])
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
    types["DomainMappingIn"] = t.struct(
        {
            "sslSettings": t.proxy(renames["SslSettingsIn"]).optional(),
            "resourceRecords": t.array(t.proxy(renames["ResourceRecordIn"])).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DomainMappingIn"])
    types["DomainMappingOut"] = t.struct(
        {
            "sslSettings": t.proxy(renames["SslSettingsOut"]).optional(),
            "resourceRecords": t.array(
                t.proxy(renames["ResourceRecordOut"])
            ).optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainMappingOut"])
    types["CreateVersionMetadataV1In"] = t.struct(
        {"cloudBuildId": t.string().optional()}
    ).named(renames["CreateVersionMetadataV1In"])
    types["CreateVersionMetadataV1Out"] = t.struct(
        {
            "cloudBuildId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVersionMetadataV1Out"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["InstanceIn"] = t.struct({"_": t.string().optional()}).named(
        renames["InstanceIn"]
    )
    types["InstanceOut"] = t.struct(
        {
            "vmIp": t.string().optional(),
            "errors": t.integer().optional(),
            "availability": t.string().optional(),
            "memoryUsage": t.string().optional(),
            "vmName": t.string().optional(),
            "qps": t.number().optional(),
            "averageLatency": t.integer().optional(),
            "name": t.string().optional(),
            "startTime": t.string().optional(),
            "vmZoneName": t.string().optional(),
            "vmLiveness": t.string().optional(),
            "vmDebugEnabled": t.boolean().optional(),
            "appEngineRelease": t.string().optional(),
            "id": t.string().optional(),
            "vmStatus": t.string().optional(),
            "vmId": t.string().optional(),
            "requests": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
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
    types["StandardSchedulerSettingsIn"] = t.struct(
        {
            "maxInstances": t.integer().optional(),
            "targetThroughputUtilization": t.number().optional(),
            "minInstances": t.integer().optional(),
            "targetCpuUtilization": t.number().optional(),
        }
    ).named(renames["StandardSchedulerSettingsIn"])
    types["StandardSchedulerSettingsOut"] = t.struct(
        {
            "maxInstances": t.integer().optional(),
            "targetThroughputUtilization": t.number().optional(),
            "minInstances": t.integer().optional(),
            "targetCpuUtilization": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StandardSchedulerSettingsOut"])
    types["ManualScalingIn"] = t.struct({"instances": t.integer().optional()}).named(
        renames["ManualScalingIn"]
    )
    types["ManualScalingOut"] = t.struct(
        {
            "instances": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManualScalingOut"])
    types["LivenessCheckIn"] = t.struct(
        {
            "initialDelay": t.string().optional(),
            "failureThreshold": t.integer().optional(),
            "successThreshold": t.integer().optional(),
            "host": t.string().optional(),
            "path": t.string().optional(),
            "timeout": t.string().optional(),
            "checkInterval": t.string().optional(),
        }
    ).named(renames["LivenessCheckIn"])
    types["LivenessCheckOut"] = t.struct(
        {
            "initialDelay": t.string().optional(),
            "failureThreshold": t.integer().optional(),
            "successThreshold": t.integer().optional(),
            "host": t.string().optional(),
            "path": t.string().optional(),
            "timeout": t.string().optional(),
            "checkInterval": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LivenessCheckOut"])
    types["ListIngressRulesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "ingressRules": t.array(t.proxy(renames["FirewallRuleIn"])).optional(),
        }
    ).named(renames["ListIngressRulesResponseIn"])
    types["ListIngressRulesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "ingressRules": t.array(t.proxy(renames["FirewallRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListIngressRulesResponseOut"])
    types["ReadinessCheckIn"] = t.struct(
        {
            "failureThreshold": t.integer().optional(),
            "checkInterval": t.string().optional(),
            "appStartTimeout": t.string().optional(),
            "successThreshold": t.integer().optional(),
            "path": t.string().optional(),
            "host": t.string().optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["ReadinessCheckIn"])
    types["ReadinessCheckOut"] = t.struct(
        {
            "failureThreshold": t.integer().optional(),
            "checkInterval": t.string().optional(),
            "appStartTimeout": t.string().optional(),
            "successThreshold": t.integer().optional(),
            "path": t.string().optional(),
            "host": t.string().optional(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReadinessCheckOut"])
    types["CreateVersionMetadataV1AlphaIn"] = t.struct(
        {"cloudBuildId": t.string().optional()}
    ).named(renames["CreateVersionMetadataV1AlphaIn"])
    types["CreateVersionMetadataV1AlphaOut"] = t.struct(
        {
            "cloudBuildId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVersionMetadataV1AlphaOut"])
    types["ErrorHandlerIn"] = t.struct(
        {
            "staticFile": t.string().optional(),
            "mimeType": t.string().optional(),
            "errorCode": t.string().optional(),
        }
    ).named(renames["ErrorHandlerIn"])
    types["ErrorHandlerOut"] = t.struct(
        {
            "staticFile": t.string().optional(),
            "mimeType": t.string().optional(),
            "errorCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ErrorHandlerOut"])
    types["EndpointsApiServiceIn"] = t.struct(
        {
            "rolloutStrategy": t.string().optional(),
            "name": t.string().optional(),
            "configId": t.string().optional(),
            "disableTraceSampling": t.boolean().optional(),
        }
    ).named(renames["EndpointsApiServiceIn"])
    types["EndpointsApiServiceOut"] = t.struct(
        {
            "rolloutStrategy": t.string().optional(),
            "name": t.string().optional(),
            "configId": t.string().optional(),
            "disableTraceSampling": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EndpointsApiServiceOut"])
    types["ApiEndpointHandlerIn"] = t.struct(
        {"scriptPath": t.string().optional()}
    ).named(renames["ApiEndpointHandlerIn"])
    types["ApiEndpointHandlerOut"] = t.struct(
        {
            "scriptPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiEndpointHandlerOut"])
    types["ProjectStateIn"] = t.struct(
        {
            "currentReasons": t.proxy(renames["ReasonsIn"]),
            "previousReasons": t.proxy(renames["ReasonsIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["ProjectStateIn"])
    types["ProjectStateOut"] = t.struct(
        {
            "currentReasons": t.proxy(renames["ReasonsOut"]),
            "previousReasons": t.proxy(renames["ReasonsOut"]).optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectStateOut"])
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
    types["LibraryIn"] = t.struct(
        {"version": t.string().optional(), "name": t.string().optional()}
    ).named(renames["LibraryIn"])
    types["LibraryOut"] = t.struct(
        {
            "version": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LibraryOut"])
    types["VolumeIn"] = t.struct(
        {
            "sizeGb": t.number().optional(),
            "volumeType": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "sizeGb": t.number().optional(),
            "volumeType": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["ZipInfoIn"] = t.struct(
        {"sourceUrl": t.string().optional(), "filesCount": t.integer().optional()}
    ).named(renames["ZipInfoIn"])
    types["ZipInfoOut"] = t.struct(
        {
            "sourceUrl": t.string().optional(),
            "filesCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ZipInfoOut"])
    types["RepairApplicationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RepairApplicationRequestIn"]
    )
    types["RepairApplicationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RepairApplicationRequestOut"])
    types["LocationMetadataIn"] = t.struct(
        {
            "standardEnvironmentAvailable": t.boolean().optional(),
            "flexibleEnvironmentAvailable": t.boolean().optional(),
        }
    ).named(renames["LocationMetadataIn"])
    types["LocationMetadataOut"] = t.struct(
        {
            "searchApiAvailable": t.boolean().optional(),
            "standardEnvironmentAvailable": t.boolean().optional(),
            "flexibleEnvironmentAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationMetadataOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["UrlDispatchRuleIn"] = t.struct(
        {
            "domain": t.string().optional(),
            "service": t.string().optional(),
            "path": t.string().optional(),
        }
    ).named(renames["UrlDispatchRuleIn"])
    types["UrlDispatchRuleOut"] = t.struct(
        {
            "domain": t.string().optional(),
            "service": t.string().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlDispatchRuleOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
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
    types["CreateVersionMetadataV1BetaIn"] = t.struct(
        {"cloudBuildId": t.string().optional()}
    ).named(renames["CreateVersionMetadataV1BetaIn"])
    types["CreateVersionMetadataV1BetaOut"] = t.struct(
        {
            "cloudBuildId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateVersionMetadataV1BetaOut"])
    types["ResourcesIn"] = t.struct(
        {
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "diskGb": t.number().optional(),
            "cpu": t.number().optional(),
            "kmsKeyReference": t.string().optional(),
            "memoryGb": t.number().optional(),
        }
    ).named(renames["ResourcesIn"])
    types["ResourcesOut"] = t.struct(
        {
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "diskGb": t.number().optional(),
            "cpu": t.number().optional(),
            "kmsKeyReference": t.string().optional(),
            "memoryGb": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourcesOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["BasicScalingIn"] = t.struct(
        {"idleTimeout": t.string().optional(), "maxInstances": t.integer().optional()}
    ).named(renames["BasicScalingIn"])
    types["BasicScalingOut"] = t.struct(
        {
            "idleTimeout": t.string().optional(),
            "maxInstances": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicScalingOut"])
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
    types["FirewallRuleIn"] = t.struct(
        {
            "description": t.string().optional(),
            "priority": t.integer().optional(),
            "sourceRange": t.string().optional(),
            "action": t.string().optional(),
        }
    ).named(renames["FirewallRuleIn"])
    types["FirewallRuleOut"] = t.struct(
        {
            "description": t.string().optional(),
            "priority": t.integer().optional(),
            "sourceRange": t.string().optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirewallRuleOut"])
    types["OperationMetadataV1BetaIn"] = t.struct(
        {
            "insertTime": t.string().optional(),
            "target": t.string().optional(),
            "method": t.string().optional(),
            "user": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1BetaIn"]),
            "warning": t.array(t.string()).optional(),
        }
    ).named(renames["OperationMetadataV1BetaIn"])
    types["OperationMetadataV1BetaOut"] = t.struct(
        {
            "insertTime": t.string().optional(),
            "target": t.string().optional(),
            "method": t.string().optional(),
            "user": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1BetaOut"]),
            "warning": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1BetaOut"])
    types["DeploymentIn"] = t.struct(
        {
            "files": t.struct({"_": t.string().optional()}).optional(),
            "zip": t.proxy(renames["ZipInfoIn"]).optional(),
            "container": t.proxy(renames["ContainerInfoIn"]).optional(),
            "cloudBuildOptions": t.proxy(renames["CloudBuildOptionsIn"]).optional(),
        }
    ).named(renames["DeploymentIn"])
    types["DeploymentOut"] = t.struct(
        {
            "files": t.struct({"_": t.string().optional()}).optional(),
            "zip": t.proxy(renames["ZipInfoOut"]).optional(),
            "container": t.proxy(renames["ContainerInfoOut"]).optional(),
            "cloudBuildOptions": t.proxy(renames["CloudBuildOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeploymentOut"])
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
    types["ResourceRecordIn"] = t.struct(
        {
            "type": t.string().optional(),
            "rrdata": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ResourceRecordIn"])
    types["ResourceRecordOut"] = t.struct(
        {
            "type": t.string().optional(),
            "rrdata": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceRecordOut"])
    types["OperationMetadataV1AlphaIn"] = t.struct(
        {
            "user": t.string().optional(),
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1AlphaIn"]),
            "warning": t.array(t.string()).optional(),
            "endTime": t.string().optional(),
            "insertTime": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "method": t.string().optional(),
            "target": t.string().optional(),
        }
    ).named(renames["OperationMetadataV1AlphaIn"])
    types["OperationMetadataV1AlphaOut"] = t.struct(
        {
            "user": t.string().optional(),
            "createVersionMetadata": t.proxy(
                renames["CreateVersionMetadataV1AlphaOut"]
            ),
            "warning": t.array(t.string()).optional(),
            "endTime": t.string().optional(),
            "insertTime": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "method": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1AlphaOut"])
    types["ProjectEventIn"] = t.struct(
        {
            "projectMetadata": t.proxy(renames["ProjectsMetadataIn"]).optional(),
            "phase": t.string(),
            "eventId": t.string().optional(),
            "state": t.proxy(renames["ProjectStateIn"]).optional(),
        }
    ).named(renames["ProjectEventIn"])
    types["ProjectEventOut"] = t.struct(
        {
            "projectMetadata": t.proxy(renames["ProjectsMetadataOut"]).optional(),
            "phase": t.string(),
            "eventId": t.string().optional(),
            "state": t.proxy(renames["ProjectStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectEventOut"])
    types["IdentityAwareProxyIn"] = t.struct(
        {
            "enabled": t.boolean().optional(),
            "oauth2ClientSecret": t.string().optional(),
            "oauth2ClientId": t.string().optional(),
        }
    ).named(renames["IdentityAwareProxyIn"])
    types["IdentityAwareProxyOut"] = t.struct(
        {
            "oauth2ClientSecretSha256": t.string().optional(),
            "enabled": t.boolean().optional(),
            "oauth2ClientSecret": t.string().optional(),
            "oauth2ClientId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IdentityAwareProxyOut"])
    types["UrlMapIn"] = t.struct(
        {
            "login": t.string().optional(),
            "urlRegex": t.string().optional(),
            "authFailAction": t.string().optional(),
            "redirectHttpResponseCode": t.string().optional(),
            "script": t.proxy(renames["ScriptHandlerIn"]).optional(),
            "securityLevel": t.string().optional(),
            "apiEndpoint": t.proxy(renames["ApiEndpointHandlerIn"]).optional(),
            "staticFiles": t.proxy(renames["StaticFilesHandlerIn"]).optional(),
        }
    ).named(renames["UrlMapIn"])
    types["UrlMapOut"] = t.struct(
        {
            "login": t.string().optional(),
            "urlRegex": t.string().optional(),
            "authFailAction": t.string().optional(),
            "redirectHttpResponseCode": t.string().optional(),
            "script": t.proxy(renames["ScriptHandlerOut"]).optional(),
            "securityLevel": t.string().optional(),
            "apiEndpoint": t.proxy(renames["ApiEndpointHandlerOut"]).optional(),
            "staticFiles": t.proxy(renames["StaticFilesHandlerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UrlMapOut"])
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
    types["StaticFilesHandlerIn"] = t.struct(
        {
            "path": t.string().optional(),
            "uploadPathRegex": t.string().optional(),
            "applicationReadable": t.boolean().optional(),
            "mimeType": t.string().optional(),
            "requireMatchingFile": t.boolean().optional(),
            "httpHeaders": t.struct({"_": t.string().optional()}).optional(),
            "expiration": t.string().optional(),
        }
    ).named(renames["StaticFilesHandlerIn"])
    types["StaticFilesHandlerOut"] = t.struct(
        {
            "path": t.string().optional(),
            "uploadPathRegex": t.string().optional(),
            "applicationReadable": t.boolean().optional(),
            "mimeType": t.string().optional(),
            "requireMatchingFile": t.boolean().optional(),
            "httpHeaders": t.struct({"_": t.string().optional()}).optional(),
            "expiration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StaticFilesHandlerOut"])
    types["GoogleAppengineV1betaLocationMetadataIn"] = t.struct(
        {
            "standardEnvironmentAvailable": t.boolean().optional(),
            "flexibleEnvironmentAvailable": t.boolean().optional(),
        }
    ).named(renames["GoogleAppengineV1betaLocationMetadataIn"])
    types["GoogleAppengineV1betaLocationMetadataOut"] = t.struct(
        {
            "standardEnvironmentAvailable": t.boolean().optional(),
            "flexibleEnvironmentAvailable": t.boolean().optional(),
            "searchApiAvailable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleAppengineV1betaLocationMetadataOut"])
    types["ContainerInfoIn"] = t.struct({"image": t.string().optional()}).named(
        renames["ContainerInfoIn"]
    )
    types["ContainerInfoOut"] = t.struct(
        {
            "image": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContainerInfoOut"])
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
    types["OperationMetadataV1In"] = t.struct(
        {
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1In"]),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "warning": t.array(t.string()).optional(),
            "method": t.string().optional(),
            "user": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "insertTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataV1In"])
    types["OperationMetadataV1Out"] = t.struct(
        {
            "createVersionMetadata": t.proxy(renames["CreateVersionMetadataV1Out"]),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "warning": t.array(t.string()).optional(),
            "method": t.string().optional(),
            "user": t.string().optional(),
            "ephemeralMessage": t.string().optional(),
            "insertTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataV1Out"])
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
    types["ApplicationIn"] = t.struct(
        {
            "id": t.string().optional(),
            "servingStatus": t.string().optional(),
            "defaultCookieExpiration": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "authDomain": t.string().optional(),
            "dispatchRules": t.array(t.proxy(renames["UrlDispatchRuleIn"])).optional(),
            "featureSettings": t.proxy(renames["FeatureSettingsIn"]).optional(),
            "locationId": t.string().optional(),
            "databaseType": t.string().optional(),
            "iap": t.proxy(renames["IdentityAwareProxyIn"]),
        }
    ).named(renames["ApplicationIn"])
    types["ApplicationOut"] = t.struct(
        {
            "id": t.string().optional(),
            "servingStatus": t.string().optional(),
            "defaultCookieExpiration": t.string().optional(),
            "name": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "gcrDomain": t.string().optional(),
            "authDomain": t.string().optional(),
            "dispatchRules": t.array(t.proxy(renames["UrlDispatchRuleOut"])).optional(),
            "codeBucket": t.string().optional(),
            "featureSettings": t.proxy(renames["FeatureSettingsOut"]).optional(),
            "locationId": t.string().optional(),
            "defaultHostname": t.string().optional(),
            "defaultBucket": t.string().optional(),
            "databaseType": t.string().optional(),
            "iap": t.proxy(renames["IdentityAwareProxyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplicationOut"])
    types["BatchUpdateIngressRulesResponseIn"] = t.struct(
        {"ingressRules": t.array(t.proxy(renames["FirewallRuleIn"])).optional()}
    ).named(renames["BatchUpdateIngressRulesResponseIn"])
    types["BatchUpdateIngressRulesResponseOut"] = t.struct(
        {
            "ingressRules": t.array(t.proxy(renames["FirewallRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchUpdateIngressRulesResponseOut"])
    types["ListDomainMappingsResponseIn"] = t.struct(
        {
            "domainMappings": t.array(t.proxy(renames["DomainMappingIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListDomainMappingsResponseIn"])
    types["ListDomainMappingsResponseOut"] = t.struct(
        {
            "domainMappings": t.array(t.proxy(renames["DomainMappingOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDomainMappingsResponseOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListServicesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(t.proxy(renames["ServiceIn"])).optional(),
        }
    ).named(renames["ListServicesResponseIn"])
    types["ListServicesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "services": t.array(t.proxy(renames["ServiceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicesResponseOut"])
    types["HealthCheckIn"] = t.struct(
        {
            "unhealthyThreshold": t.integer().optional(),
            "host": t.string().optional(),
            "disableHealthCheck": t.boolean().optional(),
            "restartThreshold": t.integer().optional(),
            "checkInterval": t.string().optional(),
            "healthyThreshold": t.integer().optional(),
            "timeout": t.string().optional(),
        }
    ).named(renames["HealthCheckIn"])
    types["HealthCheckOut"] = t.struct(
        {
            "unhealthyThreshold": t.integer().optional(),
            "host": t.string().optional(),
            "disableHealthCheck": t.boolean().optional(),
            "restartThreshold": t.integer().optional(),
            "checkInterval": t.string().optional(),
            "healthyThreshold": t.integer().optional(),
            "timeout": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HealthCheckOut"])

    functions = {}
    functions["projectsLocationsApplicationsCreate"] = appengine.post(
        "v1/projects/{projectsId}/locations/{locationsId}/applications/{applicationsId}:repair",
        t.struct(
            {
                "applicationsId": t.string().optional(),
                "locationsId": t.string().optional(),
                "projectsId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApplicationsGet"] = appengine.post(
        "v1/projects/{projectsId}/locations/{locationsId}/applications/{applicationsId}:repair",
        t.struct(
            {
                "applicationsId": t.string().optional(),
                "locationsId": t.string().optional(),
                "projectsId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApplicationsRepair"] = appengine.post(
        "v1/projects/{projectsId}/locations/{locationsId}/applications/{applicationsId}:repair",
        t.struct(
            {
                "applicationsId": t.string().optional(),
                "locationsId": t.string().optional(),
                "projectsId": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApplicationsServicesGet"] = appengine.get(
        "v1/projects/{projectsId}/locations/{locationsId}/applications/{applicationsId}/services",
        t.struct(
            {
                "projectsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "applicationsId": t.string().optional(),
                "locationsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsApplicationsServicesList"] = appengine.get(
        "v1/projects/{projectsId}/locations/{locationsId}/applications/{applicationsId}/services",
        t.struct(
            {
                "projectsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "applicationsId": t.string().optional(),
                "locationsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsGet"] = appengine.patch(
        "v1/apps/{appsId}",
        t.struct(
            {
                "updateMask": t.string(),
                "appsId": t.string().optional(),
                "id": t.string().optional(),
                "servingStatus": t.string().optional(),
                "defaultCookieExpiration": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "authDomain": t.string().optional(),
                "dispatchRules": t.array(
                    t.proxy(renames["UrlDispatchRuleIn"])
                ).optional(),
                "featureSettings": t.proxy(renames["FeatureSettingsIn"]).optional(),
                "locationId": t.string().optional(),
                "databaseType": t.string().optional(),
                "iap": t.proxy(renames["IdentityAwareProxyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsRepair"] = appengine.patch(
        "v1/apps/{appsId}",
        t.struct(
            {
                "updateMask": t.string(),
                "appsId": t.string().optional(),
                "id": t.string().optional(),
                "servingStatus": t.string().optional(),
                "defaultCookieExpiration": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "authDomain": t.string().optional(),
                "dispatchRules": t.array(
                    t.proxy(renames["UrlDispatchRuleIn"])
                ).optional(),
                "featureSettings": t.proxy(renames["FeatureSettingsIn"]).optional(),
                "locationId": t.string().optional(),
                "databaseType": t.string().optional(),
                "iap": t.proxy(renames["IdentityAwareProxyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsCreate"] = appengine.patch(
        "v1/apps/{appsId}",
        t.struct(
            {
                "updateMask": t.string(),
                "appsId": t.string().optional(),
                "id": t.string().optional(),
                "servingStatus": t.string().optional(),
                "defaultCookieExpiration": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "authDomain": t.string().optional(),
                "dispatchRules": t.array(
                    t.proxy(renames["UrlDispatchRuleIn"])
                ).optional(),
                "featureSettings": t.proxy(renames["FeatureSettingsIn"]).optional(),
                "locationId": t.string().optional(),
                "databaseType": t.string().optional(),
                "iap": t.proxy(renames["IdentityAwareProxyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsPatch"] = appengine.patch(
        "v1/apps/{appsId}",
        t.struct(
            {
                "updateMask": t.string(),
                "appsId": t.string().optional(),
                "id": t.string().optional(),
                "servingStatus": t.string().optional(),
                "defaultCookieExpiration": t.string().optional(),
                "serviceAccount": t.string().optional(),
                "authDomain": t.string().optional(),
                "dispatchRules": t.array(
                    t.proxy(renames["UrlDispatchRuleIn"])
                ).optional(),
                "featureSettings": t.proxy(renames["FeatureSettingsIn"]).optional(),
                "locationId": t.string().optional(),
                "databaseType": t.string().optional(),
                "iap": t.proxy(renames["IdentityAwareProxyIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsLocationsGet"] = appengine.get(
        "v1/apps/{appsId}/locations",
        t.struct(
            {
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsLocationsList"] = appengine.get(
        "v1/apps/{appsId}/locations",
        t.struct(
            {
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsFirewallIngressRulesPatch"] = appengine.get(
        "v1/apps/{appsId}/firewall/ingressRules",
        t.struct(
            {
                "matchingAddress": t.string().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "matchingAddress": t.string().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "matchingAddress": t.string().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIngressRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsFirewallIngressRulesGet"] = appengine.get(
        "v1/apps/{appsId}/firewall/ingressRules",
        t.struct(
            {
                "matchingAddress": t.string().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "matchingAddress": t.string().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "matchingAddress": t.string().optional(),
                "appsId": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListIngressRulesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesGet"] = appengine.patch(
        "v1/apps/{appsId}/services/{servicesId}",
        t.struct(
            {
                "migrateTraffic": t.boolean().optional(),
                "updateMask": t.string(),
                "servicesId": t.string().optional(),
                "appsId": t.string().optional(),
                "id": t.string().optional(),
                "split": t.proxy(renames["TrafficSplitIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "networkSettings": t.proxy(renames["NetworkSettingsIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesList"] = appengine.patch(
        "v1/apps/{appsId}/services/{servicesId}",
        t.struct(
            {
                "migrateTraffic": t.boolean().optional(),
                "updateMask": t.string(),
                "servicesId": t.string().optional(),
                "appsId": t.string().optional(),
                "id": t.string().optional(),
                "split": t.proxy(renames["TrafficSplitIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "networkSettings": t.proxy(renames["NetworkSettingsIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesDelete"] = appengine.patch(
        "v1/apps/{appsId}/services/{servicesId}",
        t.struct(
            {
                "migrateTraffic": t.boolean().optional(),
                "updateMask": t.string(),
                "servicesId": t.string().optional(),
                "appsId": t.string().optional(),
                "id": t.string().optional(),
                "split": t.proxy(renames["TrafficSplitIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "networkSettings": t.proxy(renames["NetworkSettingsIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesPatch"] = appengine.patch(
        "v1/apps/{appsId}/services/{servicesId}",
        t.struct(
            {
                "migrateTraffic": t.boolean().optional(),
                "updateMask": t.string(),
                "servicesId": t.string().optional(),
                "appsId": t.string().optional(),
                "id": t.string().optional(),
                "split": t.proxy(renames["TrafficSplitIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "networkSettings": t.proxy(renames["NetworkSettingsIn"]).optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsDelete"] = appengine.patch(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "updateMask": t.string().optional(),
                "servingStatus": t.string().optional(),
                "endpointsApiService": t.proxy(
                    renames["EndpointsApiServiceIn"]
                ).optional(),
                "instanceClass": t.string().optional(),
                "libraries": t.array(t.proxy(renames["LibraryIn"])).optional(),
                "env": t.string().optional(),
                "nobuildFilesRegex": t.string().optional(),
                "manualScaling": t.proxy(renames["ManualScalingIn"]).optional(),
                "handlers": t.array(t.proxy(renames["UrlMapIn"])).optional(),
                "errorHandlers": t.array(t.proxy(renames["ErrorHandlerIn"])).optional(),
                "runtimeApiVersion": t.string().optional(),
                "betaSettings": t.struct({"_": t.string().optional()}).optional(),
                "runtimeMainExecutablePath": t.string().optional(),
                "vpcAccessConnector": t.proxy(
                    renames["VpcAccessConnectorIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "runtime": t.string().optional(),
                "createdBy": t.string().optional(),
                "id": t.string().optional(),
                "automaticScaling": t.proxy(renames["AutomaticScalingIn"]).optional(),
                "basicScaling": t.proxy(renames["BasicScalingIn"]).optional(),
                "healthCheck": t.proxy(renames["HealthCheckIn"]).optional(),
                "versionUrl": t.string().optional(),
                "readinessCheck": t.proxy(renames["ReadinessCheckIn"]).optional(),
                "entrypoint": t.proxy(renames["EntrypointIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "buildEnvVariables": t.struct({"_": t.string().optional()}).optional(),
                "apiConfig": t.proxy(renames["ApiConfigHandlerIn"]).optional(),
                "threadsafe": t.boolean().optional(),
                "name": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "appEngineApis": t.boolean().optional(),
                "inboundServices": t.array(t.string()).optional(),
                "diskUsageBytes": t.string().optional(),
                "livenessCheck": t.proxy(renames["LivenessCheckIn"]).optional(),
                "flexibleRuntimeSettings": t.proxy(
                    renames["FlexibleRuntimeSettingsIn"]
                ).optional(),
                "defaultExpiration": t.string().optional(),
                "envVariables": t.struct({"_": t.string().optional()}).optional(),
                "zones": t.array(t.string()).optional(),
                "network": t.proxy(renames["NetworkIn"]).optional(),
                "resources": t.proxy(renames["ResourcesIn"]).optional(),
                "runtimeChannel": t.string().optional(),
                "vm": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsList"] = appengine.patch(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "updateMask": t.string().optional(),
                "servingStatus": t.string().optional(),
                "endpointsApiService": t.proxy(
                    renames["EndpointsApiServiceIn"]
                ).optional(),
                "instanceClass": t.string().optional(),
                "libraries": t.array(t.proxy(renames["LibraryIn"])).optional(),
                "env": t.string().optional(),
                "nobuildFilesRegex": t.string().optional(),
                "manualScaling": t.proxy(renames["ManualScalingIn"]).optional(),
                "handlers": t.array(t.proxy(renames["UrlMapIn"])).optional(),
                "errorHandlers": t.array(t.proxy(renames["ErrorHandlerIn"])).optional(),
                "runtimeApiVersion": t.string().optional(),
                "betaSettings": t.struct({"_": t.string().optional()}).optional(),
                "runtimeMainExecutablePath": t.string().optional(),
                "vpcAccessConnector": t.proxy(
                    renames["VpcAccessConnectorIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "runtime": t.string().optional(),
                "createdBy": t.string().optional(),
                "id": t.string().optional(),
                "automaticScaling": t.proxy(renames["AutomaticScalingIn"]).optional(),
                "basicScaling": t.proxy(renames["BasicScalingIn"]).optional(),
                "healthCheck": t.proxy(renames["HealthCheckIn"]).optional(),
                "versionUrl": t.string().optional(),
                "readinessCheck": t.proxy(renames["ReadinessCheckIn"]).optional(),
                "entrypoint": t.proxy(renames["EntrypointIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "buildEnvVariables": t.struct({"_": t.string().optional()}).optional(),
                "apiConfig": t.proxy(renames["ApiConfigHandlerIn"]).optional(),
                "threadsafe": t.boolean().optional(),
                "name": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "appEngineApis": t.boolean().optional(),
                "inboundServices": t.array(t.string()).optional(),
                "diskUsageBytes": t.string().optional(),
                "livenessCheck": t.proxy(renames["LivenessCheckIn"]).optional(),
                "flexibleRuntimeSettings": t.proxy(
                    renames["FlexibleRuntimeSettingsIn"]
                ).optional(),
                "defaultExpiration": t.string().optional(),
                "envVariables": t.struct({"_": t.string().optional()}).optional(),
                "zones": t.array(t.string()).optional(),
                "network": t.proxy(renames["NetworkIn"]).optional(),
                "resources": t.proxy(renames["ResourcesIn"]).optional(),
                "runtimeChannel": t.string().optional(),
                "vm": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsCreate"] = appengine.patch(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "updateMask": t.string().optional(),
                "servingStatus": t.string().optional(),
                "endpointsApiService": t.proxy(
                    renames["EndpointsApiServiceIn"]
                ).optional(),
                "instanceClass": t.string().optional(),
                "libraries": t.array(t.proxy(renames["LibraryIn"])).optional(),
                "env": t.string().optional(),
                "nobuildFilesRegex": t.string().optional(),
                "manualScaling": t.proxy(renames["ManualScalingIn"]).optional(),
                "handlers": t.array(t.proxy(renames["UrlMapIn"])).optional(),
                "errorHandlers": t.array(t.proxy(renames["ErrorHandlerIn"])).optional(),
                "runtimeApiVersion": t.string().optional(),
                "betaSettings": t.struct({"_": t.string().optional()}).optional(),
                "runtimeMainExecutablePath": t.string().optional(),
                "vpcAccessConnector": t.proxy(
                    renames["VpcAccessConnectorIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "runtime": t.string().optional(),
                "createdBy": t.string().optional(),
                "id": t.string().optional(),
                "automaticScaling": t.proxy(renames["AutomaticScalingIn"]).optional(),
                "basicScaling": t.proxy(renames["BasicScalingIn"]).optional(),
                "healthCheck": t.proxy(renames["HealthCheckIn"]).optional(),
                "versionUrl": t.string().optional(),
                "readinessCheck": t.proxy(renames["ReadinessCheckIn"]).optional(),
                "entrypoint": t.proxy(renames["EntrypointIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "buildEnvVariables": t.struct({"_": t.string().optional()}).optional(),
                "apiConfig": t.proxy(renames["ApiConfigHandlerIn"]).optional(),
                "threadsafe": t.boolean().optional(),
                "name": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "appEngineApis": t.boolean().optional(),
                "inboundServices": t.array(t.string()).optional(),
                "diskUsageBytes": t.string().optional(),
                "livenessCheck": t.proxy(renames["LivenessCheckIn"]).optional(),
                "flexibleRuntimeSettings": t.proxy(
                    renames["FlexibleRuntimeSettingsIn"]
                ).optional(),
                "defaultExpiration": t.string().optional(),
                "envVariables": t.struct({"_": t.string().optional()}).optional(),
                "zones": t.array(t.string()).optional(),
                "network": t.proxy(renames["NetworkIn"]).optional(),
                "resources": t.proxy(renames["ResourcesIn"]).optional(),
                "runtimeChannel": t.string().optional(),
                "vm": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsGet"] = appengine.patch(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "updateMask": t.string().optional(),
                "servingStatus": t.string().optional(),
                "endpointsApiService": t.proxy(
                    renames["EndpointsApiServiceIn"]
                ).optional(),
                "instanceClass": t.string().optional(),
                "libraries": t.array(t.proxy(renames["LibraryIn"])).optional(),
                "env": t.string().optional(),
                "nobuildFilesRegex": t.string().optional(),
                "manualScaling": t.proxy(renames["ManualScalingIn"]).optional(),
                "handlers": t.array(t.proxy(renames["UrlMapIn"])).optional(),
                "errorHandlers": t.array(t.proxy(renames["ErrorHandlerIn"])).optional(),
                "runtimeApiVersion": t.string().optional(),
                "betaSettings": t.struct({"_": t.string().optional()}).optional(),
                "runtimeMainExecutablePath": t.string().optional(),
                "vpcAccessConnector": t.proxy(
                    renames["VpcAccessConnectorIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "runtime": t.string().optional(),
                "createdBy": t.string().optional(),
                "id": t.string().optional(),
                "automaticScaling": t.proxy(renames["AutomaticScalingIn"]).optional(),
                "basicScaling": t.proxy(renames["BasicScalingIn"]).optional(),
                "healthCheck": t.proxy(renames["HealthCheckIn"]).optional(),
                "versionUrl": t.string().optional(),
                "readinessCheck": t.proxy(renames["ReadinessCheckIn"]).optional(),
                "entrypoint": t.proxy(renames["EntrypointIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "buildEnvVariables": t.struct({"_": t.string().optional()}).optional(),
                "apiConfig": t.proxy(renames["ApiConfigHandlerIn"]).optional(),
                "threadsafe": t.boolean().optional(),
                "name": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "appEngineApis": t.boolean().optional(),
                "inboundServices": t.array(t.string()).optional(),
                "diskUsageBytes": t.string().optional(),
                "livenessCheck": t.proxy(renames["LivenessCheckIn"]).optional(),
                "flexibleRuntimeSettings": t.proxy(
                    renames["FlexibleRuntimeSettingsIn"]
                ).optional(),
                "defaultExpiration": t.string().optional(),
                "envVariables": t.struct({"_": t.string().optional()}).optional(),
                "zones": t.array(t.string()).optional(),
                "network": t.proxy(renames["NetworkIn"]).optional(),
                "resources": t.proxy(renames["ResourcesIn"]).optional(),
                "runtimeChannel": t.string().optional(),
                "vm": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsPatch"] = appengine.patch(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}",
        t.struct(
            {
                "versionsId": t.string().optional(),
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "updateMask": t.string().optional(),
                "servingStatus": t.string().optional(),
                "endpointsApiService": t.proxy(
                    renames["EndpointsApiServiceIn"]
                ).optional(),
                "instanceClass": t.string().optional(),
                "libraries": t.array(t.proxy(renames["LibraryIn"])).optional(),
                "env": t.string().optional(),
                "nobuildFilesRegex": t.string().optional(),
                "manualScaling": t.proxy(renames["ManualScalingIn"]).optional(),
                "handlers": t.array(t.proxy(renames["UrlMapIn"])).optional(),
                "errorHandlers": t.array(t.proxy(renames["ErrorHandlerIn"])).optional(),
                "runtimeApiVersion": t.string().optional(),
                "betaSettings": t.struct({"_": t.string().optional()}).optional(),
                "runtimeMainExecutablePath": t.string().optional(),
                "vpcAccessConnector": t.proxy(
                    renames["VpcAccessConnectorIn"]
                ).optional(),
                "createTime": t.string().optional(),
                "runtime": t.string().optional(),
                "createdBy": t.string().optional(),
                "id": t.string().optional(),
                "automaticScaling": t.proxy(renames["AutomaticScalingIn"]).optional(),
                "basicScaling": t.proxy(renames["BasicScalingIn"]).optional(),
                "healthCheck": t.proxy(renames["HealthCheckIn"]).optional(),
                "versionUrl": t.string().optional(),
                "readinessCheck": t.proxy(renames["ReadinessCheckIn"]).optional(),
                "entrypoint": t.proxy(renames["EntrypointIn"]).optional(),
                "serviceAccount": t.string().optional(),
                "buildEnvVariables": t.struct({"_": t.string().optional()}).optional(),
                "apiConfig": t.proxy(renames["ApiConfigHandlerIn"]).optional(),
                "threadsafe": t.boolean().optional(),
                "name": t.string().optional(),
                "deployment": t.proxy(renames["DeploymentIn"]).optional(),
                "appEngineApis": t.boolean().optional(),
                "inboundServices": t.array(t.string()).optional(),
                "diskUsageBytes": t.string().optional(),
                "livenessCheck": t.proxy(renames["LivenessCheckIn"]).optional(),
                "flexibleRuntimeSettings": t.proxy(
                    renames["FlexibleRuntimeSettingsIn"]
                ).optional(),
                "defaultExpiration": t.string().optional(),
                "envVariables": t.struct({"_": t.string().optional()}).optional(),
                "zones": t.array(t.string()).optional(),
                "network": t.proxy(renames["NetworkIn"]).optional(),
                "resources": t.proxy(renames["ResourcesIn"]).optional(),
                "runtimeChannel": t.string().optional(),
                "vm": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsInstancesList"] = appengine.get(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}",
        t.struct(
            {
                "instancesId": t.string().optional(),
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "versionsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsInstancesDelete"] = appengine.get(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}",
        t.struct(
            {
                "instancesId": t.string().optional(),
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "versionsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsInstancesDebug"] = appengine.get(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}",
        t.struct(
            {
                "instancesId": t.string().optional(),
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "versionsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsServicesVersionsInstancesGet"] = appengine.get(
        "v1/apps/{appsId}/services/{servicesId}/versions/{versionsId}/instances/{instancesId}",
        t.struct(
            {
                "instancesId": t.string().optional(),
                "appsId": t.string().optional(),
                "servicesId": t.string().optional(),
                "versionsId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsDelete"] = appengine.patch(
        "v1/apps/{appsId}/domainMappings/{domainMappingsId}",
        t.struct(
            {
                "appsId": t.string().optional(),
                "updateMask": t.string(),
                "domainMappingsId": t.string().optional(),
                "sslSettings": t.proxy(renames["SslSettingsIn"]).optional(),
                "resourceRecords": t.array(
                    t.proxy(renames["ResourceRecordIn"])
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsGet"] = appengine.patch(
        "v1/apps/{appsId}/domainMappings/{domainMappingsId}",
        t.struct(
            {
                "appsId": t.string().optional(),
                "updateMask": t.string(),
                "domainMappingsId": t.string().optional(),
                "sslSettings": t.proxy(renames["SslSettingsIn"]).optional(),
                "resourceRecords": t.array(
                    t.proxy(renames["ResourceRecordIn"])
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsList"] = appengine.patch(
        "v1/apps/{appsId}/domainMappings/{domainMappingsId}",
        t.struct(
            {
                "appsId": t.string().optional(),
                "updateMask": t.string(),
                "domainMappingsId": t.string().optional(),
                "sslSettings": t.proxy(renames["SslSettingsIn"]).optional(),
                "resourceRecords": t.array(
                    t.proxy(renames["ResourceRecordIn"])
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsCreate"] = appengine.patch(
        "v1/apps/{appsId}/domainMappings/{domainMappingsId}",
        t.struct(
            {
                "appsId": t.string().optional(),
                "updateMask": t.string(),
                "domainMappingsId": t.string().optional(),
                "sslSettings": t.proxy(renames["SslSettingsIn"]).optional(),
                "resourceRecords": t.array(
                    t.proxy(renames["ResourceRecordIn"])
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsDomainMappingsPatch"] = appengine.patch(
        "v1/apps/{appsId}/domainMappings/{domainMappingsId}",
        t.struct(
            {
                "appsId": t.string().optional(),
                "updateMask": t.string(),
                "domainMappingsId": t.string().optional(),
                "sslSettings": t.proxy(renames["SslSettingsIn"]).optional(),
                "resourceRecords": t.array(
                    t.proxy(renames["ResourceRecordIn"])
                ).optional(),
                "id": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["appsAuthorizedDomainsList"] = appengine.get(
        "v1/apps/{appsId}/authorizedDomains",
        t.struct(
            {
                "appsId": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAuthorizedDomainsResponseOut"]),
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

    return Import(
        importer="appengine",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
