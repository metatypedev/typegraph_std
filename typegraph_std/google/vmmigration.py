from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_vmmigration():
    vmmigration = HTTPRuntime("https://vmmigration.googleapis.com/")

    renames = {
        "ErrorResponse": "_vmmigration_1_ErrorResponse",
        "CancelCloneJobRequestIn": "_vmmigration_2_CancelCloneJobRequestIn",
        "CancelCloneJobRequestOut": "_vmmigration_3_CancelCloneJobRequestOut",
        "ListSourcesResponseIn": "_vmmigration_4_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_vmmigration_5_ListSourcesResponseOut",
        "ShuttingDownSourceVMStepIn": "_vmmigration_6_ShuttingDownSourceVMStepIn",
        "ShuttingDownSourceVMStepOut": "_vmmigration_7_ShuttingDownSourceVMStepOut",
        "AwsDiskDetailsIn": "_vmmigration_8_AwsDiskDetailsIn",
        "AwsDiskDetailsOut": "_vmmigration_9_AwsDiskDetailsOut",
        "AwsSourceVmDetailsIn": "_vmmigration_10_AwsSourceVmDetailsIn",
        "AwsSourceVmDetailsOut": "_vmmigration_11_AwsSourceVmDetailsOut",
        "UpgradeApplianceRequestIn": "_vmmigration_12_UpgradeApplianceRequestIn",
        "UpgradeApplianceRequestOut": "_vmmigration_13_UpgradeApplianceRequestOut",
        "LocationIn": "_vmmigration_14_LocationIn",
        "LocationOut": "_vmmigration_15_LocationOut",
        "AwsVmsDetailsIn": "_vmmigration_16_AwsVmsDetailsIn",
        "AwsVmsDetailsOut": "_vmmigration_17_AwsVmsDetailsOut",
        "VmUtilizationMetricsIn": "_vmmigration_18_VmUtilizationMetricsIn",
        "VmUtilizationMetricsOut": "_vmmigration_19_VmUtilizationMetricsOut",
        "InstantiatingMigratedVMStepIn": "_vmmigration_20_InstantiatingMigratedVMStepIn",
        "InstantiatingMigratedVMStepOut": "_vmmigration_21_InstantiatingMigratedVMStepOut",
        "StartMigrationRequestIn": "_vmmigration_22_StartMigrationRequestIn",
        "StartMigrationRequestOut": "_vmmigration_23_StartMigrationRequestOut",
        "SchedulePolicyIn": "_vmmigration_24_SchedulePolicyIn",
        "SchedulePolicyOut": "_vmmigration_25_SchedulePolicyOut",
        "LinkIn": "_vmmigration_26_LinkIn",
        "LinkOut": "_vmmigration_27_LinkOut",
        "AppliedLicenseIn": "_vmmigration_28_AppliedLicenseIn",
        "AppliedLicenseOut": "_vmmigration_29_AppliedLicenseOut",
        "CloneJobIn": "_vmmigration_30_CloneJobIn",
        "CloneJobOut": "_vmmigration_31_CloneJobOut",
        "VmUtilizationInfoIn": "_vmmigration_32_VmUtilizationInfoIn",
        "VmUtilizationInfoOut": "_vmmigration_33_VmUtilizationInfoOut",
        "ComputeSchedulingIn": "_vmmigration_34_ComputeSchedulingIn",
        "ComputeSchedulingOut": "_vmmigration_35_ComputeSchedulingOut",
        "NetworkInterfaceIn": "_vmmigration_36_NetworkInterfaceIn",
        "NetworkInterfaceOut": "_vmmigration_37_NetworkInterfaceOut",
        "ListOperationsResponseIn": "_vmmigration_38_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vmmigration_39_ListOperationsResponseOut",
        "TargetProjectIn": "_vmmigration_40_TargetProjectIn",
        "TargetProjectOut": "_vmmigration_41_TargetProjectOut",
        "AdaptingOSStepIn": "_vmmigration_42_AdaptingOSStepIn",
        "AdaptingOSStepOut": "_vmmigration_43_AdaptingOSStepOut",
        "ListMigratingVmsResponseIn": "_vmmigration_44_ListMigratingVmsResponseIn",
        "ListMigratingVmsResponseOut": "_vmmigration_45_ListMigratingVmsResponseOut",
        "CloneStepIn": "_vmmigration_46_CloneStepIn",
        "CloneStepOut": "_vmmigration_47_CloneStepOut",
        "AddGroupMigrationRequestIn": "_vmmigration_48_AddGroupMigrationRequestIn",
        "AddGroupMigrationRequestOut": "_vmmigration_49_AddGroupMigrationRequestOut",
        "VmwareVmsDetailsIn": "_vmmigration_50_VmwareVmsDetailsIn",
        "VmwareVmsDetailsOut": "_vmmigration_51_VmwareVmsDetailsOut",
        "RemoveGroupMigrationRequestIn": "_vmmigration_52_RemoveGroupMigrationRequestIn",
        "RemoveGroupMigrationRequestOut": "_vmmigration_53_RemoveGroupMigrationRequestOut",
        "LocalizedMessageIn": "_vmmigration_54_LocalizedMessageIn",
        "LocalizedMessageOut": "_vmmigration_55_LocalizedMessageOut",
        "ResumeMigrationRequestIn": "_vmmigration_56_ResumeMigrationRequestIn",
        "ResumeMigrationRequestOut": "_vmmigration_57_ResumeMigrationRequestOut",
        "AwsSourceDetailsIn": "_vmmigration_58_AwsSourceDetailsIn",
        "AwsSourceDetailsOut": "_vmmigration_59_AwsSourceDetailsOut",
        "PauseMigrationRequestIn": "_vmmigration_60_PauseMigrationRequestIn",
        "PauseMigrationRequestOut": "_vmmigration_61_PauseMigrationRequestOut",
        "MigrationWarningIn": "_vmmigration_62_MigrationWarningIn",
        "MigrationWarningOut": "_vmmigration_63_MigrationWarningOut",
        "ListDatacenterConnectorsResponseIn": "_vmmigration_64_ListDatacenterConnectorsResponseIn",
        "ListDatacenterConnectorsResponseOut": "_vmmigration_65_ListDatacenterConnectorsResponseOut",
        "ComputeEngineTargetDetailsIn": "_vmmigration_66_ComputeEngineTargetDetailsIn",
        "ComputeEngineTargetDetailsOut": "_vmmigration_67_ComputeEngineTargetDetailsOut",
        "CutoverJobIn": "_vmmigration_68_CutoverJobIn",
        "CutoverJobOut": "_vmmigration_69_CutoverJobOut",
        "InitializingReplicationStepIn": "_vmmigration_70_InitializingReplicationStepIn",
        "InitializingReplicationStepOut": "_vmmigration_71_InitializingReplicationStepOut",
        "ListCutoverJobsResponseIn": "_vmmigration_72_ListCutoverJobsResponseIn",
        "ListCutoverJobsResponseOut": "_vmmigration_73_ListCutoverJobsResponseOut",
        "ListCloneJobsResponseIn": "_vmmigration_74_ListCloneJobsResponseIn",
        "ListCloneJobsResponseOut": "_vmmigration_75_ListCloneJobsResponseOut",
        "EmptyIn": "_vmmigration_76_EmptyIn",
        "EmptyOut": "_vmmigration_77_EmptyOut",
        "CutoverForecastIn": "_vmmigration_78_CutoverForecastIn",
        "CutoverForecastOut": "_vmmigration_79_CutoverForecastOut",
        "MigratingVmIn": "_vmmigration_80_MigratingVmIn",
        "MigratingVmOut": "_vmmigration_81_MigratingVmOut",
        "AvailableUpdatesIn": "_vmmigration_82_AvailableUpdatesIn",
        "AvailableUpdatesOut": "_vmmigration_83_AvailableUpdatesOut",
        "StatusIn": "_vmmigration_84_StatusIn",
        "StatusOut": "_vmmigration_85_StatusOut",
        "ApplianceVersionIn": "_vmmigration_86_ApplianceVersionIn",
        "ApplianceVersionOut": "_vmmigration_87_ApplianceVersionOut",
        "ListLocationsResponseIn": "_vmmigration_88_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_vmmigration_89_ListLocationsResponseOut",
        "DatacenterConnectorIn": "_vmmigration_90_DatacenterConnectorIn",
        "DatacenterConnectorOut": "_vmmigration_91_DatacenterConnectorOut",
        "VmwareVmDetailsIn": "_vmmigration_92_VmwareVmDetailsIn",
        "VmwareVmDetailsOut": "_vmmigration_93_VmwareVmDetailsOut",
        "FetchInventoryResponseIn": "_vmmigration_94_FetchInventoryResponseIn",
        "FetchInventoryResponseOut": "_vmmigration_95_FetchInventoryResponseOut",
        "ListUtilizationReportsResponseIn": "_vmmigration_96_ListUtilizationReportsResponseIn",
        "ListUtilizationReportsResponseOut": "_vmmigration_97_ListUtilizationReportsResponseOut",
        "AwsSecurityGroupIn": "_vmmigration_98_AwsSecurityGroupIn",
        "AwsSecurityGroupOut": "_vmmigration_99_AwsSecurityGroupOut",
        "UpgradeStatusIn": "_vmmigration_100_UpgradeStatusIn",
        "UpgradeStatusOut": "_vmmigration_101_UpgradeStatusOut",
        "ListReplicationCyclesResponseIn": "_vmmigration_102_ListReplicationCyclesResponseIn",
        "ListReplicationCyclesResponseOut": "_vmmigration_103_ListReplicationCyclesResponseOut",
        "CutoverStepIn": "_vmmigration_104_CutoverStepIn",
        "CutoverStepOut": "_vmmigration_105_CutoverStepOut",
        "SourceIn": "_vmmigration_106_SourceIn",
        "SourceOut": "_vmmigration_107_SourceOut",
        "ComputeEngineTargetDefaultsIn": "_vmmigration_108_ComputeEngineTargetDefaultsIn",
        "ComputeEngineTargetDefaultsOut": "_vmmigration_109_ComputeEngineTargetDefaultsOut",
        "PostProcessingStepIn": "_vmmigration_110_PostProcessingStepIn",
        "PostProcessingStepOut": "_vmmigration_111_PostProcessingStepOut",
        "AwsVmDetailsIn": "_vmmigration_112_AwsVmDetailsIn",
        "AwsVmDetailsOut": "_vmmigration_113_AwsVmDetailsOut",
        "ReplicatingStepIn": "_vmmigration_114_ReplicatingStepIn",
        "ReplicatingStepOut": "_vmmigration_115_ReplicatingStepOut",
        "OperationIn": "_vmmigration_116_OperationIn",
        "OperationOut": "_vmmigration_117_OperationOut",
        "ReplicationSyncIn": "_vmmigration_118_ReplicationSyncIn",
        "ReplicationSyncOut": "_vmmigration_119_ReplicationSyncOut",
        "CancelCutoverJobRequestIn": "_vmmigration_120_CancelCutoverJobRequestIn",
        "CancelCutoverJobRequestOut": "_vmmigration_121_CancelCutoverJobRequestOut",
        "UtilizationReportIn": "_vmmigration_122_UtilizationReportIn",
        "UtilizationReportOut": "_vmmigration_123_UtilizationReportOut",
        "ReplicationCycleIn": "_vmmigration_124_ReplicationCycleIn",
        "ReplicationCycleOut": "_vmmigration_125_ReplicationCycleOut",
        "CycleStepIn": "_vmmigration_126_CycleStepIn",
        "CycleStepOut": "_vmmigration_127_CycleStepOut",
        "MigrationErrorIn": "_vmmigration_128_MigrationErrorIn",
        "MigrationErrorOut": "_vmmigration_129_MigrationErrorOut",
        "OperationMetadataIn": "_vmmigration_130_OperationMetadataIn",
        "OperationMetadataOut": "_vmmigration_131_OperationMetadataOut",
        "TagIn": "_vmmigration_132_TagIn",
        "TagOut": "_vmmigration_133_TagOut",
        "ListGroupsResponseIn": "_vmmigration_134_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_vmmigration_135_ListGroupsResponseOut",
        "AccessKeyCredentialsIn": "_vmmigration_136_AccessKeyCredentialsIn",
        "AccessKeyCredentialsOut": "_vmmigration_137_AccessKeyCredentialsOut",
        "SchedulingNodeAffinityIn": "_vmmigration_138_SchedulingNodeAffinityIn",
        "SchedulingNodeAffinityOut": "_vmmigration_139_SchedulingNodeAffinityOut",
        "CancelOperationRequestIn": "_vmmigration_140_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vmmigration_141_CancelOperationRequestOut",
        "ListTargetProjectsResponseIn": "_vmmigration_142_ListTargetProjectsResponseIn",
        "ListTargetProjectsResponseOut": "_vmmigration_143_ListTargetProjectsResponseOut",
        "VmwareSourceDetailsIn": "_vmmigration_144_VmwareSourceDetailsIn",
        "VmwareSourceDetailsOut": "_vmmigration_145_VmwareSourceDetailsOut",
        "PreparingVMDisksStepIn": "_vmmigration_146_PreparingVMDisksStepIn",
        "PreparingVMDisksStepOut": "_vmmigration_147_PreparingVMDisksStepOut",
        "FinalizeMigrationRequestIn": "_vmmigration_148_FinalizeMigrationRequestIn",
        "FinalizeMigrationRequestOut": "_vmmigration_149_FinalizeMigrationRequestOut",
        "GroupIn": "_vmmigration_150_GroupIn",
        "GroupOut": "_vmmigration_151_GroupOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CancelCloneJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelCloneJobRequestIn"]
    )
    types["CancelCloneJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelCloneJobRequestOut"])
    types["ListSourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListSourcesResponseIn"]
    )
    types["ListSourcesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSourcesResponseOut"])
    types["ShuttingDownSourceVMStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ShuttingDownSourceVMStepIn"]
    )
    types["ShuttingDownSourceVMStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ShuttingDownSourceVMStepOut"])
    types["AwsDiskDetailsIn"] = t.struct(
        {
            "diskNumber": t.integer().optional(),
            "sizeGb": t.string().optional(),
            "volumeId": t.string().optional(),
        }
    ).named(renames["AwsDiskDetailsIn"])
    types["AwsDiskDetailsOut"] = t.struct(
        {
            "diskNumber": t.integer().optional(),
            "sizeGb": t.string().optional(),
            "volumeId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsDiskDetailsOut"])
    types["AwsSourceVmDetailsIn"] = t.struct(
        {
            "firmware": t.string().optional(),
            "disks": t.array(t.proxy(renames["AwsDiskDetailsIn"])).optional(),
            "committedStorageBytes": t.string().optional(),
        }
    ).named(renames["AwsSourceVmDetailsIn"])
    types["AwsSourceVmDetailsOut"] = t.struct(
        {
            "firmware": t.string().optional(),
            "disks": t.array(t.proxy(renames["AwsDiskDetailsOut"])).optional(),
            "committedStorageBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsSourceVmDetailsOut"])
    types["UpgradeApplianceRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["UpgradeApplianceRequestIn"])
    types["UpgradeApplianceRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeApplianceRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["AwsVmsDetailsIn"] = t.struct(
        {"details": t.array(t.proxy(renames["AwsVmDetailsIn"])).optional()}
    ).named(renames["AwsVmsDetailsIn"])
    types["AwsVmsDetailsOut"] = t.struct(
        {
            "details": t.array(t.proxy(renames["AwsVmDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsVmsDetailsOut"])
    types["VmUtilizationMetricsIn"] = t.struct(
        {
            "memoryMaxPercent": t.integer().optional(),
            "networkThroughputMaxKbps": t.string().optional(),
            "networkThroughputAverageKbps": t.string().optional(),
            "diskIoRateMaxKbps": t.string().optional(),
            "memoryAveragePercent": t.integer().optional(),
            "cpuAveragePercent": t.integer().optional(),
            "diskIoRateAverageKbps": t.string().optional(),
            "cpuMaxPercent": t.integer().optional(),
        }
    ).named(renames["VmUtilizationMetricsIn"])
    types["VmUtilizationMetricsOut"] = t.struct(
        {
            "memoryMaxPercent": t.integer().optional(),
            "networkThroughputMaxKbps": t.string().optional(),
            "networkThroughputAverageKbps": t.string().optional(),
            "diskIoRateMaxKbps": t.string().optional(),
            "memoryAveragePercent": t.integer().optional(),
            "cpuAveragePercent": t.integer().optional(),
            "diskIoRateAverageKbps": t.string().optional(),
            "cpuMaxPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmUtilizationMetricsOut"])
    types["InstantiatingMigratedVMStepIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InstantiatingMigratedVMStepIn"])
    types["InstantiatingMigratedVMStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InstantiatingMigratedVMStepOut"])
    types["StartMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartMigrationRequestIn"]
    )
    types["StartMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartMigrationRequestOut"])
    types["SchedulePolicyIn"] = t.struct(
        {
            "skipOsAdaptation": t.boolean().optional(),
            "idleDuration": t.string().optional(),
        }
    ).named(renames["SchedulePolicyIn"])
    types["SchedulePolicyOut"] = t.struct(
        {
            "skipOsAdaptation": t.boolean().optional(),
            "idleDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulePolicyOut"])
    types["LinkIn"] = t.struct(
        {"url": t.string().optional(), "description": t.string().optional()}
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "url": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["AppliedLicenseIn"] = t.struct(
        {"osLicense": t.string().optional(), "type": t.string().optional()}
    ).named(renames["AppliedLicenseIn"])
    types["AppliedLicenseOut"] = t.struct(
        {
            "osLicense": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppliedLicenseOut"])
    types["CloneJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloneJobIn"]
    )
    types["CloneJobOut"] = t.struct(
        {
            "state": t.string().optional(),
            "stateTime": t.string().optional(),
            "steps": t.array(t.proxy(renames["CloneStepOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "endTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "computeEngineTargetDetails": t.proxy(
                renames["ComputeEngineTargetDetailsOut"]
            ).optional(),
        }
    ).named(renames["CloneJobOut"])
    types["VmUtilizationInfoIn"] = t.struct(
        {
            "vmwareVmDetails": t.proxy(renames["VmwareVmDetailsIn"]).optional(),
            "utilization": t.proxy(renames["VmUtilizationMetricsIn"]).optional(),
            "vmId": t.string().optional(),
        }
    ).named(renames["VmUtilizationInfoIn"])
    types["VmUtilizationInfoOut"] = t.struct(
        {
            "vmwareVmDetails": t.proxy(renames["VmwareVmDetailsOut"]).optional(),
            "utilization": t.proxy(renames["VmUtilizationMetricsOut"]).optional(),
            "vmId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmUtilizationInfoOut"])
    types["ComputeSchedulingIn"] = t.struct(
        {
            "nodeAffinities": t.array(
                t.proxy(renames["SchedulingNodeAffinityIn"])
            ).optional(),
            "restartType": t.string().optional(),
            "minNodeCpus": t.integer().optional(),
            "onHostMaintenance": t.string().optional(),
        }
    ).named(renames["ComputeSchedulingIn"])
    types["ComputeSchedulingOut"] = t.struct(
        {
            "nodeAffinities": t.array(
                t.proxy(renames["SchedulingNodeAffinityOut"])
            ).optional(),
            "restartType": t.string().optional(),
            "minNodeCpus": t.integer().optional(),
            "onHostMaintenance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeSchedulingOut"])
    types["NetworkInterfaceIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "externalIp": t.string().optional(),
            "network": t.string().optional(),
            "internalIp": t.string().optional(),
        }
    ).named(renames["NetworkInterfaceIn"])
    types["NetworkInterfaceOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "externalIp": t.string().optional(),
            "network": t.string().optional(),
            "internalIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInterfaceOut"])
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
    types["TargetProjectIn"] = t.struct(
        {"project": t.string().optional(), "description": t.string().optional()}
    ).named(renames["TargetProjectIn"])
    types["TargetProjectOut"] = t.struct(
        {
            "project": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetProjectOut"])
    types["AdaptingOSStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdaptingOSStepIn"]
    )
    types["AdaptingOSStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdaptingOSStepOut"])
    types["ListMigratingVmsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListMigratingVmsResponseIn"]
    )
    types["ListMigratingVmsResponseOut"] = t.struct(
        {
            "migratingVms": t.array(t.proxy(renames["MigratingVmOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMigratingVmsResponseOut"])
    types["CloneStepIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepIn"]).optional(),
            "adaptingOs": t.proxy(renames["AdaptingOSStepIn"]).optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepIn"]
            ).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["CloneStepIn"])
    types["CloneStepOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepOut"]).optional(),
            "adaptingOs": t.proxy(renames["AdaptingOSStepOut"]).optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneStepOut"])
    types["AddGroupMigrationRequestIn"] = t.struct(
        {"migratingVm": t.string().optional()}
    ).named(renames["AddGroupMigrationRequestIn"])
    types["AddGroupMigrationRequestOut"] = t.struct(
        {
            "migratingVm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddGroupMigrationRequestOut"])
    types["VmwareVmsDetailsIn"] = t.struct(
        {"details": t.array(t.proxy(renames["VmwareVmDetailsIn"])).optional()}
    ).named(renames["VmwareVmsDetailsIn"])
    types["VmwareVmsDetailsOut"] = t.struct(
        {
            "details": t.array(t.proxy(renames["VmwareVmDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVmsDetailsOut"])
    types["RemoveGroupMigrationRequestIn"] = t.struct(
        {"migratingVm": t.string().optional()}
    ).named(renames["RemoveGroupMigrationRequestIn"])
    types["RemoveGroupMigrationRequestOut"] = t.struct(
        {
            "migratingVm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveGroupMigrationRequestOut"])
    types["LocalizedMessageIn"] = t.struct(
        {"message": t.string().optional(), "locale": t.string().optional()}
    ).named(renames["LocalizedMessageIn"])
    types["LocalizedMessageOut"] = t.struct(
        {
            "message": t.string().optional(),
            "locale": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedMessageOut"])
    types["ResumeMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeMigrationRequestIn"]
    )
    types["ResumeMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeMigrationRequestOut"])
    types["AwsSourceDetailsIn"] = t.struct(
        {
            "inventoryTagList": t.array(t.proxy(renames["TagIn"])).optional(),
            "awsRegion": t.string().optional(),
            "inventorySecurityGroupNames": t.array(t.string()).optional(),
            "migrationResourcesUserTags": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "accessKeyCreds": t.proxy(renames["AccessKeyCredentialsIn"]).optional(),
        }
    ).named(renames["AwsSourceDetailsIn"])
    types["AwsSourceDetailsOut"] = t.struct(
        {
            "publicIp": t.string().optional(),
            "inventoryTagList": t.array(t.proxy(renames["TagOut"])).optional(),
            "state": t.string().optional(),
            "awsRegion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "inventorySecurityGroupNames": t.array(t.string()).optional(),
            "migrationResourcesUserTags": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "accessKeyCreds": t.proxy(renames["AccessKeyCredentialsOut"]).optional(),
        }
    ).named(renames["AwsSourceDetailsOut"])
    types["PauseMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseMigrationRequestIn"]
    )
    types["PauseMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseMigrationRequestOut"])
    types["MigrationWarningIn"] = t.struct(
        {
            "helpLinks": t.array(t.proxy(renames["LinkIn"])).optional(),
            "code": t.string().optional(),
            "warningMessage": t.proxy(renames["LocalizedMessageIn"]).optional(),
            "warningTime": t.string().optional(),
            "actionItem": t.proxy(renames["LocalizedMessageIn"]).optional(),
        }
    ).named(renames["MigrationWarningIn"])
    types["MigrationWarningOut"] = t.struct(
        {
            "helpLinks": t.array(t.proxy(renames["LinkOut"])).optional(),
            "code": t.string().optional(),
            "warningMessage": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "warningTime": t.string().optional(),
            "actionItem": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationWarningOut"])
    types["ListDatacenterConnectorsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListDatacenterConnectorsResponseIn"])
    types["ListDatacenterConnectorsResponseOut"] = t.struct(
        {
            "datacenterConnectors": t.array(
                t.proxy(renames["DatacenterConnectorOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatacenterConnectorsResponseOut"])
    types["ComputeEngineTargetDetailsIn"] = t.struct(
        {
            "bootOption": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "hostname": t.string().optional(),
            "licenseType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "appliedLicense": t.proxy(renames["AppliedLicenseIn"]).optional(),
            "vmName": t.string().optional(),
            "machineType": t.string().optional(),
            "project": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceIn"])
            ).optional(),
            "secureBoot": t.boolean().optional(),
            "zone": t.string().optional(),
            "diskType": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingIn"]).optional(),
            "machineTypeSeries": t.string().optional(),
        }
    ).named(renames["ComputeEngineTargetDetailsIn"])
    types["ComputeEngineTargetDetailsOut"] = t.struct(
        {
            "bootOption": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "hostname": t.string().optional(),
            "licenseType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "appliedLicense": t.proxy(renames["AppliedLicenseOut"]).optional(),
            "vmName": t.string().optional(),
            "machineType": t.string().optional(),
            "project": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceOut"])
            ).optional(),
            "secureBoot": t.boolean().optional(),
            "zone": t.string().optional(),
            "diskType": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingOut"]).optional(),
            "machineTypeSeries": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineTargetDetailsOut"])
    types["CutoverJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CutoverJobIn"]
    )
    types["CutoverJobOut"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["CutoverStepOut"])).optional(),
            "state": t.string().optional(),
            "stateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "stateMessage": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "computeEngineTargetDetails": t.proxy(
                renames["ComputeEngineTargetDetailsOut"]
            ).optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["CutoverJobOut"])
    types["InitializingReplicationStepIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InitializingReplicationStepIn"])
    types["InitializingReplicationStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InitializingReplicationStepOut"])
    types["ListCutoverJobsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListCutoverJobsResponseIn"]
    )
    types["ListCutoverJobsResponseOut"] = t.struct(
        {
            "cutoverJobs": t.array(t.proxy(renames["CutoverJobOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCutoverJobsResponseOut"])
    types["ListCloneJobsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListCloneJobsResponseIn"]
    )
    types["ListCloneJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "cloneJobs": t.array(t.proxy(renames["CloneJobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCloneJobsResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CutoverForecastIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CutoverForecastIn"]
    )
    types["CutoverForecastOut"] = t.struct(
        {
            "estimatedCutoverJobDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoverForecastOut"])
    types["MigratingVmIn"] = t.struct(
        {
            "sourceVmId": t.string().optional(),
            "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
            "displayName": t.string().optional(),
            "computeEngineTargetDefaults": t.proxy(
                renames["ComputeEngineTargetDefaultsIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["MigratingVmIn"])
    types["MigratingVmOut"] = t.struct(
        {
            "sourceVmId": t.string().optional(),
            "awsSourceVmDetails": t.proxy(renames["AwsSourceVmDetailsOut"]).optional(),
            "stateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "recentCloneJobs": t.array(t.proxy(renames["CloneJobOut"])).optional(),
            "updateTime": t.string().optional(),
            "policy": t.proxy(renames["SchedulePolicyOut"]).optional(),
            "currentSyncInfo": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "cutoverForecast": t.proxy(renames["CutoverForecastOut"]).optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "lastSync": t.proxy(renames["ReplicationSyncOut"]).optional(),
            "computeEngineTargetDefaults": t.proxy(
                renames["ComputeEngineTargetDefaultsOut"]
            ).optional(),
            "lastReplicationCycle": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "group": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "recentCutoverJobs": t.array(t.proxy(renames["CutoverJobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigratingVmOut"])
    types["AvailableUpdatesIn"] = t.struct(
        {
            "newDeployableAppliance": t.proxy(renames["ApplianceVersionIn"]).optional(),
            "inPlaceUpdate": t.proxy(renames["ApplianceVersionIn"]).optional(),
        }
    ).named(renames["AvailableUpdatesIn"])
    types["AvailableUpdatesOut"] = t.struct(
        {
            "newDeployableAppliance": t.proxy(
                renames["ApplianceVersionOut"]
            ).optional(),
            "inPlaceUpdate": t.proxy(renames["ApplianceVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvailableUpdatesOut"])
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
    types["ApplianceVersionIn"] = t.struct(
        {
            "uri": t.string().optional(),
            "critical": t.boolean().optional(),
            "version": t.string().optional(),
            "releaseNotesUri": t.string().optional(),
        }
    ).named(renames["ApplianceVersionIn"])
    types["ApplianceVersionOut"] = t.struct(
        {
            "uri": t.string().optional(),
            "critical": t.boolean().optional(),
            "version": t.string().optional(),
            "releaseNotesUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplianceVersionOut"])
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
    types["DatacenterConnectorIn"] = t.struct(
        {
            "registrationId": t.string().optional(),
            "version": t.string().optional(),
            "serviceAccount": t.string().optional(),
        }
    ).named(renames["DatacenterConnectorIn"])
    types["DatacenterConnectorOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "registrationId": t.string().optional(),
            "applianceInfrastructureVersion": t.string().optional(),
            "availableVersions": t.proxy(renames["AvailableUpdatesOut"]).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "serviceAccount": t.string().optional(),
            "applianceSoftwareVersion": t.string().optional(),
            "bucket": t.string().optional(),
            "name": t.string().optional(),
            "stateTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "upgradeStatus": t.proxy(renames["UpgradeStatusOut"]).optional(),
        }
    ).named(renames["DatacenterConnectorOut"])
    types["VmwareVmDetailsIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "diskCount": t.integer().optional(),
            "cpuCount": t.integer().optional(),
            "vmId": t.string().optional(),
            "uuid": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "committedStorageMb": t.string().optional(),
            "datacenterDescription": t.string().optional(),
            "guestDescription": t.string().optional(),
            "datacenterId": t.string().optional(),
            "powerState": t.string().optional(),
        }
    ).named(renames["VmwareVmDetailsIn"])
    types["VmwareVmDetailsOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "diskCount": t.integer().optional(),
            "cpuCount": t.integer().optional(),
            "vmId": t.string().optional(),
            "uuid": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "committedStorageMb": t.string().optional(),
            "datacenterDescription": t.string().optional(),
            "guestDescription": t.string().optional(),
            "datacenterId": t.string().optional(),
            "bootOption": t.string().optional(),
            "powerState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVmDetailsOut"])
    types["FetchInventoryResponseIn"] = t.struct(
        {
            "vmwareVms": t.proxy(renames["VmwareVmsDetailsIn"]).optional(),
            "awsVms": t.proxy(renames["AwsVmsDetailsIn"]).optional(),
        }
    ).named(renames["FetchInventoryResponseIn"])
    types["FetchInventoryResponseOut"] = t.struct(
        {
            "vmwareVms": t.proxy(renames["VmwareVmsDetailsOut"]).optional(),
            "awsVms": t.proxy(renames["AwsVmsDetailsOut"]).optional(),
            "updateTime": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchInventoryResponseOut"])
    types["ListUtilizationReportsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListUtilizationReportsResponseIn"])
    types["ListUtilizationReportsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "utilizationReports": t.array(
                t.proxy(renames["UtilizationReportOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUtilizationReportsResponseOut"])
    types["AwsSecurityGroupIn"] = t.struct(
        {"name": t.string().optional(), "id": t.string().optional()}
    ).named(renames["AwsSecurityGroupIn"])
    types["AwsSecurityGroupOut"] = t.struct(
        {
            "name": t.string().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsSecurityGroupOut"])
    types["UpgradeStatusIn"] = t.struct(
        {
            "previousVersion": t.string().optional(),
            "startTime": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["UpgradeStatusIn"])
    types["UpgradeStatusOut"] = t.struct(
        {
            "previousVersion": t.string().optional(),
            "startTime": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["UpgradeStatusOut"])
    types["ListReplicationCyclesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListReplicationCyclesResponseIn"])
    types["ListReplicationCyclesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "replicationCycles": t.array(
                t.proxy(renames["ReplicationCycleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReplicationCyclesResponseOut"])
    types["CutoverStepIn"] = t.struct(
        {
            "finalSync": t.proxy(renames["ReplicationCycleIn"]).optional(),
            "previousReplicationCycle": t.proxy(
                renames["ReplicationCycleIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepIn"]
            ).optional(),
            "shuttingDownSourceVm": t.proxy(
                renames["ShuttingDownSourceVMStepIn"]
            ).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepIn"]).optional(),
        }
    ).named(renames["CutoverStepIn"])
    types["CutoverStepOut"] = t.struct(
        {
            "finalSync": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "previousReplicationCycle": t.proxy(
                renames["ReplicationCycleOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepOut"]
            ).optional(),
            "shuttingDownSourceVm": t.proxy(
                renames["ShuttingDownSourceVMStepOut"]
            ).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoverStepOut"])
    types["SourceIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
            "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "vmware": t.proxy(renames["VmwareSourceDetailsOut"]).optional(),
            "aws": t.proxy(renames["AwsSourceDetailsOut"]).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["ComputeEngineTargetDefaultsIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "hostname": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingIn"]).optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "targetProject": t.string().optional(),
            "vmName": t.string().optional(),
            "machineType": t.string().optional(),
            "zone": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceIn"])
            ).optional(),
            "licenseType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "machineTypeSeries": t.string().optional(),
            "secureBoot": t.boolean().optional(),
            "diskType": t.string().optional(),
        }
    ).named(renames["ComputeEngineTargetDefaultsIn"])
    types["ComputeEngineTargetDefaultsOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "hostname": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingOut"]).optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "targetProject": t.string().optional(),
            "vmName": t.string().optional(),
            "bootOption": t.string().optional(),
            "machineType": t.string().optional(),
            "zone": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceOut"])
            ).optional(),
            "appliedLicense": t.proxy(renames["AppliedLicenseOut"]).optional(),
            "licenseType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "machineTypeSeries": t.string().optional(),
            "secureBoot": t.boolean().optional(),
            "diskType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineTargetDefaultsOut"])
    types["PostProcessingStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PostProcessingStepIn"]
    )
    types["PostProcessingStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PostProcessingStepOut"])
    types["AwsVmDetailsIn"] = t.struct(
        {
            "committedStorageMb": t.string().optional(),
            "osDescription": t.string().optional(),
            "sourceDescription": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "zone": t.string().optional(),
            "bootOption": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "vpcId": t.string().optional(),
            "sourceId": t.string().optional(),
            "securityGroups": t.array(
                t.proxy(renames["AwsSecurityGroupIn"])
            ).optional(),
            "architecture": t.string().optional(),
            "diskCount": t.integer().optional(),
            "virtualizationType": t.string().optional(),
            "instanceType": t.string().optional(),
            "tags": t.struct({"_": t.string().optional()}).optional(),
            "vmId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["AwsVmDetailsIn"])
    types["AwsVmDetailsOut"] = t.struct(
        {
            "committedStorageMb": t.string().optional(),
            "osDescription": t.string().optional(),
            "sourceDescription": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "zone": t.string().optional(),
            "bootOption": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "vpcId": t.string().optional(),
            "sourceId": t.string().optional(),
            "securityGroups": t.array(
                t.proxy(renames["AwsSecurityGroupOut"])
            ).optional(),
            "architecture": t.string().optional(),
            "diskCount": t.integer().optional(),
            "powerState": t.string().optional(),
            "virtualizationType": t.string().optional(),
            "instanceType": t.string().optional(),
            "tags": t.struct({"_": t.string().optional()}).optional(),
            "vmId": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsVmDetailsOut"])
    types["ReplicatingStepIn"] = t.struct(
        {
            "replicatedBytes": t.string().optional(),
            "totalBytes": t.string().optional(),
            "lastTwoMinutesAverageBytesPerSecond": t.string().optional(),
            "lastThirtyMinutesAverageBytesPerSecond": t.string().optional(),
        }
    ).named(renames["ReplicatingStepIn"])
    types["ReplicatingStepOut"] = t.struct(
        {
            "replicatedBytes": t.string().optional(),
            "totalBytes": t.string().optional(),
            "lastTwoMinutesAverageBytesPerSecond": t.string().optional(),
            "lastThirtyMinutesAverageBytesPerSecond": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicatingStepOut"])
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
    types["ReplicationSyncIn"] = t.struct(
        {"lastSyncTime": t.string().optional()}
    ).named(renames["ReplicationSyncIn"])
    types["ReplicationSyncOut"] = t.struct(
        {
            "lastSyncTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicationSyncOut"])
    types["CancelCutoverJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelCutoverJobRequestIn"]
    )
    types["CancelCutoverJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelCutoverJobRequestOut"])
    types["UtilizationReportIn"] = t.struct(
        {
            "vms": t.array(t.proxy(renames["VmUtilizationInfoIn"])).optional(),
            "displayName": t.string().optional(),
            "timeFrame": t.string().optional(),
        }
    ).named(renames["UtilizationReportIn"])
    types["UtilizationReportOut"] = t.struct(
        {
            "state": t.string().optional(),
            "vms": t.array(t.proxy(renames["VmUtilizationInfoOut"])).optional(),
            "vmCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "stateTime": t.string().optional(),
            "timeFrame": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "frameEndTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["UtilizationReportOut"])
    types["ReplicationCycleIn"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "totalPauseDuration": t.string().optional(),
            "steps": t.array(t.proxy(renames["CycleStepIn"])).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "progressPercent": t.integer().optional(),
            "cycleNumber": t.integer().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ReplicationCycleIn"])
    types["ReplicationCycleOut"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "totalPauseDuration": t.string().optional(),
            "steps": t.array(t.proxy(renames["CycleStepOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "progressPercent": t.integer().optional(),
            "cycleNumber": t.integer().optional(),
            "startTime": t.string().optional(),
            "name": t.string().optional(),
            "warnings": t.array(t.proxy(renames["MigrationWarningOut"])).optional(),
        }
    ).named(renames["ReplicationCycleOut"])
    types["CycleStepIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "initializingReplication": t.proxy(
                renames["InitializingReplicationStepIn"]
            ).optional(),
            "postProcessing": t.proxy(renames["PostProcessingStepIn"]).optional(),
            "replicating": t.proxy(renames["ReplicatingStepIn"]).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["CycleStepIn"])
    types["CycleStepOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "initializingReplication": t.proxy(
                renames["InitializingReplicationStepOut"]
            ).optional(),
            "postProcessing": t.proxy(renames["PostProcessingStepOut"]).optional(),
            "replicating": t.proxy(renames["ReplicatingStepOut"]).optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CycleStepOut"])
    types["MigrationErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MigrationErrorIn"]
    )
    types["MigrationErrorOut"] = t.struct(
        {
            "errorMessage": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "helpLinks": t.array(t.proxy(renames["LinkOut"])).optional(),
            "code": t.string().optional(),
            "errorTime": t.string().optional(),
            "actionItem": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationErrorOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["TagIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["TagIn"])
    types["TagOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagOut"])
    types["ListGroupsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListGroupsResponseIn"]
    )
    types["ListGroupsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["AccessKeyCredentialsIn"] = t.struct(
        {
            "accessKeyId": t.string().optional(),
            "sessionToken": t.string().optional(),
            "secretAccessKey": t.string().optional(),
        }
    ).named(renames["AccessKeyCredentialsIn"])
    types["AccessKeyCredentialsOut"] = t.struct(
        {
            "accessKeyId": t.string().optional(),
            "sessionToken": t.string().optional(),
            "secretAccessKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessKeyCredentialsOut"])
    types["SchedulingNodeAffinityIn"] = t.struct(
        {
            "operator": t.string().optional(),
            "key": t.string().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["SchedulingNodeAffinityIn"])
    types["SchedulingNodeAffinityOut"] = t.struct(
        {
            "operator": t.string().optional(),
            "key": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulingNodeAffinityOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["ListTargetProjectsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListTargetProjectsResponseIn"])
    types["ListTargetProjectsResponseOut"] = t.struct(
        {
            "targetProjects": t.array(t.proxy(renames["TargetProjectOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTargetProjectsResponseOut"])
    types["VmwareSourceDetailsIn"] = t.struct(
        {
            "resolvedVcenterHost": t.string().optional(),
            "thumbprint": t.string().optional(),
            "password": t.string().optional(),
            "vcenterIp": t.string().optional(),
            "username": t.string().optional(),
        }
    ).named(renames["VmwareSourceDetailsIn"])
    types["VmwareSourceDetailsOut"] = t.struct(
        {
            "resolvedVcenterHost": t.string().optional(),
            "thumbprint": t.string().optional(),
            "password": t.string().optional(),
            "vcenterIp": t.string().optional(),
            "username": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareSourceDetailsOut"])
    types["PreparingVMDisksStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PreparingVMDisksStepIn"]
    )
    types["PreparingVMDisksStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PreparingVMDisksStepOut"])
    types["FinalizeMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FinalizeMigrationRequestIn"]
    )
    types["FinalizeMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FinalizeMigrationRequestOut"])
    types["GroupIn"] = t.struct(
        {"description": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])

    functions = {}
    functions["projectsLocationsGet"] = vmmigration.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = vmmigration.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesPatch"] = vmmigration.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDelete"] = vmmigration.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesCreate"] = vmmigration.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesGet"] = vmmigration.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesFetchInventory"] = vmmigration.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesList"] = vmmigration.get(
        "v1/{parent}/sources",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListSourcesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsList"] = vmmigration.post(
        "v1/{datacenterConnector}:upgradeAppliance",
        t.struct(
            {
                "datacenterConnector": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsCreate"] = vmmigration.post(
        "v1/{datacenterConnector}:upgradeAppliance",
        t.struct(
            {
                "datacenterConnector": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsGet"] = vmmigration.post(
        "v1/{datacenterConnector}:upgradeAppliance",
        t.struct(
            {
                "datacenterConnector": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsDelete"] = vmmigration.post(
        "v1/{datacenterConnector}:upgradeAppliance",
        t.struct(
            {
                "datacenterConnector": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesDatacenterConnectorsUpgradeAppliance"
    ] = vmmigration.post(
        "v1/{datacenterConnector}:upgradeAppliance",
        t.struct(
            {
                "datacenterConnector": t.string(),
                "requestId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsList"] = vmmigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsCreate"] = vmmigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsGet"] = vmmigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsDelete"] = vmmigration.delete(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsResumeMigration"] = vmmigration.post(
        "v1/{migratingVm}:pauseMigration",
        t.struct(
            {
                "migratingVm": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesMigratingVmsFinalizeMigration"
    ] = vmmigration.post(
        "v1/{migratingVm}:pauseMigration",
        t.struct(
            {
                "migratingVm": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCreate"] = vmmigration.post(
        "v1/{migratingVm}:pauseMigration",
        t.struct(
            {
                "migratingVm": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsStartMigration"] = vmmigration.post(
        "v1/{migratingVm}:pauseMigration",
        t.struct(
            {
                "migratingVm": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsPatch"] = vmmigration.post(
        "v1/{migratingVm}:pauseMigration",
        t.struct(
            {
                "migratingVm": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsDelete"] = vmmigration.post(
        "v1/{migratingVm}:pauseMigration",
        t.struct(
            {
                "migratingVm": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsGet"] = vmmigration.post(
        "v1/{migratingVm}:pauseMigration",
        t.struct(
            {
                "migratingVm": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsList"] = vmmigration.post(
        "v1/{migratingVm}:pauseMigration",
        t.struct(
            {
                "migratingVm": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsPauseMigration"] = vmmigration.post(
        "v1/{migratingVm}:pauseMigration",
        t.struct(
            {
                "migratingVm": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCloneJobsCancel"] = vmmigration.post(
        "v1/{parent}/cloneJobs",
        t.struct(
            {
                "cloneJobId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCloneJobsList"] = vmmigration.post(
        "v1/{parent}/cloneJobs",
        t.struct(
            {
                "cloneJobId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCloneJobsGet"] = vmmigration.post(
        "v1/{parent}/cloneJobs",
        t.struct(
            {
                "cloneJobId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCloneJobsCreate"] = vmmigration.post(
        "v1/{parent}/cloneJobs",
        t.struct(
            {
                "cloneJobId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesMigratingVmsReplicationCyclesGet"
    ] = vmmigration.get(
        "v1/{parent}/replicationCycles",
        t.struct(
            {
                "pageToken": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReplicationCyclesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesMigratingVmsReplicationCyclesList"
    ] = vmmigration.get(
        "v1/{parent}/replicationCycles",
        t.struct(
            {
                "pageToken": t.string(),
                "pageSize": t.integer().optional(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReplicationCyclesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCutoverJobsList"] = vmmigration.post(
        "v1/{parent}/cutoverJobs",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "cutoverJobId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCutoverJobsGet"] = vmmigration.post(
        "v1/{parent}/cutoverJobs",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "cutoverJobId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesMigratingVmsCutoverJobsCancel"
    ] = vmmigration.post(
        "v1/{parent}/cutoverJobs",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "cutoverJobId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesMigratingVmsCutoverJobsCreate"
    ] = vmmigration.post(
        "v1/{parent}/cutoverJobs",
        t.struct(
            {
                "requestId": t.string().optional(),
                "parent": t.string(),
                "cutoverJobId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsRemoveGroupMigration"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsDelete"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsAddGroupMigration"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsList"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsCreate"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsPatch"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsGet"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GroupOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsCreate"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsDelete"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsGet"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsList"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsPatch"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string().optional(),
                "name": t.string().optional(),
                "requestId": t.string().optional(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = vmmigration.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = vmmigration.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = vmmigration.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = vmmigration.get(
        "v1/{name}/operations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="vmmigration",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
