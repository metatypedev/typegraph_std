from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_vmmigration() -> Import:
    vmmigration = HTTPRuntime("https://vmmigration.googleapis.com/")

    renames = {
        "ErrorResponse": "_vmmigration_1_ErrorResponse",
        "SchedulePolicyIn": "_vmmigration_2_SchedulePolicyIn",
        "SchedulePolicyOut": "_vmmigration_3_SchedulePolicyOut",
        "VmUtilizationMetricsIn": "_vmmigration_4_VmUtilizationMetricsIn",
        "VmUtilizationMetricsOut": "_vmmigration_5_VmUtilizationMetricsOut",
        "InitializingReplicationStepIn": "_vmmigration_6_InitializingReplicationStepIn",
        "InitializingReplicationStepOut": "_vmmigration_7_InitializingReplicationStepOut",
        "LocationIn": "_vmmigration_8_LocationIn",
        "LocationOut": "_vmmigration_9_LocationOut",
        "CutoverJobIn": "_vmmigration_10_CutoverJobIn",
        "CutoverJobOut": "_vmmigration_11_CutoverJobOut",
        "SourceIn": "_vmmigration_12_SourceIn",
        "SourceOut": "_vmmigration_13_SourceOut",
        "ShuttingDownSourceVMStepIn": "_vmmigration_14_ShuttingDownSourceVMStepIn",
        "ShuttingDownSourceVMStepOut": "_vmmigration_15_ShuttingDownSourceVMStepOut",
        "ComputeEngineTargetDetailsIn": "_vmmigration_16_ComputeEngineTargetDetailsIn",
        "ComputeEngineTargetDetailsOut": "_vmmigration_17_ComputeEngineTargetDetailsOut",
        "CutoverStepIn": "_vmmigration_18_CutoverStepIn",
        "CutoverStepOut": "_vmmigration_19_CutoverStepOut",
        "FinalizeMigrationRequestIn": "_vmmigration_20_FinalizeMigrationRequestIn",
        "FinalizeMigrationRequestOut": "_vmmigration_21_FinalizeMigrationRequestOut",
        "LinkIn": "_vmmigration_22_LinkIn",
        "LinkOut": "_vmmigration_23_LinkOut",
        "AwsVmsDetailsIn": "_vmmigration_24_AwsVmsDetailsIn",
        "AwsVmsDetailsOut": "_vmmigration_25_AwsVmsDetailsOut",
        "PostProcessingStepIn": "_vmmigration_26_PostProcessingStepIn",
        "PostProcessingStepOut": "_vmmigration_27_PostProcessingStepOut",
        "ListOperationsResponseIn": "_vmmigration_28_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vmmigration_29_ListOperationsResponseOut",
        "SchedulingNodeAffinityIn": "_vmmigration_30_SchedulingNodeAffinityIn",
        "SchedulingNodeAffinityOut": "_vmmigration_31_SchedulingNodeAffinityOut",
        "ReplicatingStepIn": "_vmmigration_32_ReplicatingStepIn",
        "ReplicatingStepOut": "_vmmigration_33_ReplicatingStepOut",
        "InstantiatingMigratedVMStepIn": "_vmmigration_34_InstantiatingMigratedVMStepIn",
        "InstantiatingMigratedVMStepOut": "_vmmigration_35_InstantiatingMigratedVMStepOut",
        "ListCloneJobsResponseIn": "_vmmigration_36_ListCloneJobsResponseIn",
        "ListCloneJobsResponseOut": "_vmmigration_37_ListCloneJobsResponseOut",
        "ApplianceVersionIn": "_vmmigration_38_ApplianceVersionIn",
        "ApplianceVersionOut": "_vmmigration_39_ApplianceVersionOut",
        "StartMigrationRequestIn": "_vmmigration_40_StartMigrationRequestIn",
        "StartMigrationRequestOut": "_vmmigration_41_StartMigrationRequestOut",
        "ListReplicationCyclesResponseIn": "_vmmigration_42_ListReplicationCyclesResponseIn",
        "ListReplicationCyclesResponseOut": "_vmmigration_43_ListReplicationCyclesResponseOut",
        "AdaptingOSStepIn": "_vmmigration_44_AdaptingOSStepIn",
        "AdaptingOSStepOut": "_vmmigration_45_AdaptingOSStepOut",
        "ListMigratingVmsResponseIn": "_vmmigration_46_ListMigratingVmsResponseIn",
        "ListMigratingVmsResponseOut": "_vmmigration_47_ListMigratingVmsResponseOut",
        "ReplicationCycleIn": "_vmmigration_48_ReplicationCycleIn",
        "ReplicationCycleOut": "_vmmigration_49_ReplicationCycleOut",
        "ReplicationSyncIn": "_vmmigration_50_ReplicationSyncIn",
        "ReplicationSyncOut": "_vmmigration_51_ReplicationSyncOut",
        "CutoverForecastIn": "_vmmigration_52_CutoverForecastIn",
        "CutoverForecastOut": "_vmmigration_53_CutoverForecastOut",
        "CancelCloneJobRequestIn": "_vmmigration_54_CancelCloneJobRequestIn",
        "CancelCloneJobRequestOut": "_vmmigration_55_CancelCloneJobRequestOut",
        "FetchInventoryResponseIn": "_vmmigration_56_FetchInventoryResponseIn",
        "FetchInventoryResponseOut": "_vmmigration_57_FetchInventoryResponseOut",
        "ListSourcesResponseIn": "_vmmigration_58_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_vmmigration_59_ListSourcesResponseOut",
        "UtilizationReportIn": "_vmmigration_60_UtilizationReportIn",
        "UtilizationReportOut": "_vmmigration_61_UtilizationReportOut",
        "GroupIn": "_vmmigration_62_GroupIn",
        "GroupOut": "_vmmigration_63_GroupOut",
        "VmwareSourceDetailsIn": "_vmmigration_64_VmwareSourceDetailsIn",
        "VmwareSourceDetailsOut": "_vmmigration_65_VmwareSourceDetailsOut",
        "ListLocationsResponseIn": "_vmmigration_66_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_vmmigration_67_ListLocationsResponseOut",
        "UpgradeApplianceRequestIn": "_vmmigration_68_UpgradeApplianceRequestIn",
        "UpgradeApplianceRequestOut": "_vmmigration_69_UpgradeApplianceRequestOut",
        "AvailableUpdatesIn": "_vmmigration_70_AvailableUpdatesIn",
        "AvailableUpdatesOut": "_vmmigration_71_AvailableUpdatesOut",
        "NetworkInterfaceIn": "_vmmigration_72_NetworkInterfaceIn",
        "NetworkInterfaceOut": "_vmmigration_73_NetworkInterfaceOut",
        "OperationIn": "_vmmigration_74_OperationIn",
        "OperationOut": "_vmmigration_75_OperationOut",
        "DatacenterConnectorIn": "_vmmigration_76_DatacenterConnectorIn",
        "DatacenterConnectorOut": "_vmmigration_77_DatacenterConnectorOut",
        "AwsSourceVmDetailsIn": "_vmmigration_78_AwsSourceVmDetailsIn",
        "AwsSourceVmDetailsOut": "_vmmigration_79_AwsSourceVmDetailsOut",
        "StatusIn": "_vmmigration_80_StatusIn",
        "StatusOut": "_vmmigration_81_StatusOut",
        "MigratingVmIn": "_vmmigration_82_MigratingVmIn",
        "MigratingVmOut": "_vmmigration_83_MigratingVmOut",
        "TagIn": "_vmmigration_84_TagIn",
        "TagOut": "_vmmigration_85_TagOut",
        "ResumeMigrationRequestIn": "_vmmigration_86_ResumeMigrationRequestIn",
        "ResumeMigrationRequestOut": "_vmmigration_87_ResumeMigrationRequestOut",
        "ListDatacenterConnectorsResponseIn": "_vmmigration_88_ListDatacenterConnectorsResponseIn",
        "ListDatacenterConnectorsResponseOut": "_vmmigration_89_ListDatacenterConnectorsResponseOut",
        "ListCutoverJobsResponseIn": "_vmmigration_90_ListCutoverJobsResponseIn",
        "ListCutoverJobsResponseOut": "_vmmigration_91_ListCutoverJobsResponseOut",
        "ComputeEngineTargetDefaultsIn": "_vmmigration_92_ComputeEngineTargetDefaultsIn",
        "ComputeEngineTargetDefaultsOut": "_vmmigration_93_ComputeEngineTargetDefaultsOut",
        "ListUtilizationReportsResponseIn": "_vmmigration_94_ListUtilizationReportsResponseIn",
        "ListUtilizationReportsResponseOut": "_vmmigration_95_ListUtilizationReportsResponseOut",
        "VmwareVmsDetailsIn": "_vmmigration_96_VmwareVmsDetailsIn",
        "VmwareVmsDetailsOut": "_vmmigration_97_VmwareVmsDetailsOut",
        "CloneJobIn": "_vmmigration_98_CloneJobIn",
        "CloneJobOut": "_vmmigration_99_CloneJobOut",
        "UpgradeStatusIn": "_vmmigration_100_UpgradeStatusIn",
        "UpgradeStatusOut": "_vmmigration_101_UpgradeStatusOut",
        "TargetProjectIn": "_vmmigration_102_TargetProjectIn",
        "TargetProjectOut": "_vmmigration_103_TargetProjectOut",
        "MigrationErrorIn": "_vmmigration_104_MigrationErrorIn",
        "MigrationErrorOut": "_vmmigration_105_MigrationErrorOut",
        "AccessKeyCredentialsIn": "_vmmigration_106_AccessKeyCredentialsIn",
        "AccessKeyCredentialsOut": "_vmmigration_107_AccessKeyCredentialsOut",
        "VmwareVmDetailsIn": "_vmmigration_108_VmwareVmDetailsIn",
        "VmwareVmDetailsOut": "_vmmigration_109_VmwareVmDetailsOut",
        "PauseMigrationRequestIn": "_vmmigration_110_PauseMigrationRequestIn",
        "PauseMigrationRequestOut": "_vmmigration_111_PauseMigrationRequestOut",
        "OperationMetadataIn": "_vmmigration_112_OperationMetadataIn",
        "OperationMetadataOut": "_vmmigration_113_OperationMetadataOut",
        "RemoveGroupMigrationRequestIn": "_vmmigration_114_RemoveGroupMigrationRequestIn",
        "RemoveGroupMigrationRequestOut": "_vmmigration_115_RemoveGroupMigrationRequestOut",
        "VmUtilizationInfoIn": "_vmmigration_116_VmUtilizationInfoIn",
        "VmUtilizationInfoOut": "_vmmigration_117_VmUtilizationInfoOut",
        "ListTargetProjectsResponseIn": "_vmmigration_118_ListTargetProjectsResponseIn",
        "ListTargetProjectsResponseOut": "_vmmigration_119_ListTargetProjectsResponseOut",
        "AwsVmDetailsIn": "_vmmigration_120_AwsVmDetailsIn",
        "AwsVmDetailsOut": "_vmmigration_121_AwsVmDetailsOut",
        "AppliedLicenseIn": "_vmmigration_122_AppliedLicenseIn",
        "AppliedLicenseOut": "_vmmigration_123_AppliedLicenseOut",
        "CycleStepIn": "_vmmigration_124_CycleStepIn",
        "CycleStepOut": "_vmmigration_125_CycleStepOut",
        "CancelCutoverJobRequestIn": "_vmmigration_126_CancelCutoverJobRequestIn",
        "CancelCutoverJobRequestOut": "_vmmigration_127_CancelCutoverJobRequestOut",
        "MigrationWarningIn": "_vmmigration_128_MigrationWarningIn",
        "MigrationWarningOut": "_vmmigration_129_MigrationWarningOut",
        "AwsSecurityGroupIn": "_vmmigration_130_AwsSecurityGroupIn",
        "AwsSecurityGroupOut": "_vmmigration_131_AwsSecurityGroupOut",
        "PreparingVMDisksStepIn": "_vmmigration_132_PreparingVMDisksStepIn",
        "PreparingVMDisksStepOut": "_vmmigration_133_PreparingVMDisksStepOut",
        "CloneStepIn": "_vmmigration_134_CloneStepIn",
        "CloneStepOut": "_vmmigration_135_CloneStepOut",
        "ListGroupsResponseIn": "_vmmigration_136_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_vmmigration_137_ListGroupsResponseOut",
        "CancelOperationRequestIn": "_vmmigration_138_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vmmigration_139_CancelOperationRequestOut",
        "AwsSourceDetailsIn": "_vmmigration_140_AwsSourceDetailsIn",
        "AwsSourceDetailsOut": "_vmmigration_141_AwsSourceDetailsOut",
        "AddGroupMigrationRequestIn": "_vmmigration_142_AddGroupMigrationRequestIn",
        "AddGroupMigrationRequestOut": "_vmmigration_143_AddGroupMigrationRequestOut",
        "ComputeSchedulingIn": "_vmmigration_144_ComputeSchedulingIn",
        "ComputeSchedulingOut": "_vmmigration_145_ComputeSchedulingOut",
        "EmptyIn": "_vmmigration_146_EmptyIn",
        "EmptyOut": "_vmmigration_147_EmptyOut",
        "LocalizedMessageIn": "_vmmigration_148_LocalizedMessageIn",
        "LocalizedMessageOut": "_vmmigration_149_LocalizedMessageOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["VmUtilizationMetricsIn"] = t.struct(
        {
            "cpuMaxPercent": t.integer().optional(),
            "networkThroughputAverageKbps": t.string().optional(),
            "memoryAveragePercent": t.integer().optional(),
            "cpuAveragePercent": t.integer().optional(),
            "memoryMaxPercent": t.integer().optional(),
            "diskIoRateAverageKbps": t.string().optional(),
            "networkThroughputMaxKbps": t.string().optional(),
            "diskIoRateMaxKbps": t.string().optional(),
        }
    ).named(renames["VmUtilizationMetricsIn"])
    types["VmUtilizationMetricsOut"] = t.struct(
        {
            "cpuMaxPercent": t.integer().optional(),
            "networkThroughputAverageKbps": t.string().optional(),
            "memoryAveragePercent": t.integer().optional(),
            "cpuAveragePercent": t.integer().optional(),
            "memoryMaxPercent": t.integer().optional(),
            "diskIoRateAverageKbps": t.string().optional(),
            "networkThroughputMaxKbps": t.string().optional(),
            "diskIoRateMaxKbps": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmUtilizationMetricsOut"])
    types["InitializingReplicationStepIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InitializingReplicationStepIn"])
    types["InitializingReplicationStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InitializingReplicationStepOut"])
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["CutoverJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CutoverJobIn"]
    )
    types["CutoverJobOut"] = t.struct(
        {
            "progressPercent": t.integer().optional(),
            "computeEngineTargetDetails": t.proxy(
                renames["ComputeEngineTargetDetailsOut"]
            ).optional(),
            "stateMessage": t.string().optional(),
            "steps": t.array(t.proxy(renames["CutoverStepOut"])).optional(),
            "stateTime": t.string().optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoverJobOut"])
    types["SourceIn"] = t.struct(
        {
            "description": t.string().optional(),
            "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
            "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "aws": t.proxy(renames["AwsSourceDetailsOut"]).optional(),
            "vmware": t.proxy(renames["VmwareSourceDetailsOut"]).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["ShuttingDownSourceVMStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ShuttingDownSourceVMStepIn"]
    )
    types["ShuttingDownSourceVMStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ShuttingDownSourceVMStepOut"])
    types["ComputeEngineTargetDetailsIn"] = t.struct(
        {
            "appliedLicense": t.proxy(renames["AppliedLicenseIn"]).optional(),
            "machineTypeSeries": t.string().optional(),
            "project": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "machineType": t.string().optional(),
            "licenseType": t.string().optional(),
            "hostname": t.string().optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingIn"]).optional(),
            "secureBoot": t.boolean().optional(),
            "bootOption": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "zone": t.string().optional(),
            "vmName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "diskType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceIn"])
            ).optional(),
        }
    ).named(renames["ComputeEngineTargetDetailsIn"])
    types["ComputeEngineTargetDetailsOut"] = t.struct(
        {
            "appliedLicense": t.proxy(renames["AppliedLicenseOut"]).optional(),
            "machineTypeSeries": t.string().optional(),
            "project": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "machineType": t.string().optional(),
            "licenseType": t.string().optional(),
            "hostname": t.string().optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingOut"]).optional(),
            "secureBoot": t.boolean().optional(),
            "bootOption": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "zone": t.string().optional(),
            "vmName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "diskType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineTargetDetailsOut"])
    types["CutoverStepIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "previousReplicationCycle": t.proxy(
                renames["ReplicationCycleIn"]
            ).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepIn"]).optional(),
            "endTime": t.string().optional(),
            "finalSync": t.proxy(renames["ReplicationCycleIn"]).optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepIn"]
            ).optional(),
            "shuttingDownSourceVm": t.proxy(
                renames["ShuttingDownSourceVMStepIn"]
            ).optional(),
        }
    ).named(renames["CutoverStepIn"])
    types["CutoverStepOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "previousReplicationCycle": t.proxy(
                renames["ReplicationCycleOut"]
            ).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepOut"]).optional(),
            "endTime": t.string().optional(),
            "finalSync": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepOut"]
            ).optional(),
            "shuttingDownSourceVm": t.proxy(
                renames["ShuttingDownSourceVMStepOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoverStepOut"])
    types["FinalizeMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FinalizeMigrationRequestIn"]
    )
    types["FinalizeMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FinalizeMigrationRequestOut"])
    types["LinkIn"] = t.struct(
        {"description": t.string().optional(), "url": t.string().optional()}
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "description": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["AwsVmsDetailsIn"] = t.struct(
        {"details": t.array(t.proxy(renames["AwsVmDetailsIn"])).optional()}
    ).named(renames["AwsVmsDetailsIn"])
    types["AwsVmsDetailsOut"] = t.struct(
        {
            "details": t.array(t.proxy(renames["AwsVmDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsVmsDetailsOut"])
    types["PostProcessingStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PostProcessingStepIn"]
    )
    types["PostProcessingStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PostProcessingStepOut"])
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
    types["SchedulingNodeAffinityIn"] = t.struct(
        {
            "key": t.string().optional(),
            "operator": t.string().optional(),
            "values": t.array(t.string()).optional(),
        }
    ).named(renames["SchedulingNodeAffinityIn"])
    types["SchedulingNodeAffinityOut"] = t.struct(
        {
            "key": t.string().optional(),
            "operator": t.string().optional(),
            "values": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulingNodeAffinityOut"])
    types["ReplicatingStepIn"] = t.struct(
        {
            "replicatedBytes": t.string().optional(),
            "lastTwoMinutesAverageBytesPerSecond": t.string().optional(),
            "lastThirtyMinutesAverageBytesPerSecond": t.string().optional(),
            "totalBytes": t.string().optional(),
        }
    ).named(renames["ReplicatingStepIn"])
    types["ReplicatingStepOut"] = t.struct(
        {
            "replicatedBytes": t.string().optional(),
            "lastTwoMinutesAverageBytesPerSecond": t.string().optional(),
            "lastThirtyMinutesAverageBytesPerSecond": t.string().optional(),
            "totalBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicatingStepOut"])
    types["InstantiatingMigratedVMStepIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InstantiatingMigratedVMStepIn"])
    types["InstantiatingMigratedVMStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InstantiatingMigratedVMStepOut"])
    types["ListCloneJobsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListCloneJobsResponseIn"]
    )
    types["ListCloneJobsResponseOut"] = t.struct(
        {
            "cloneJobs": t.array(t.proxy(renames["CloneJobOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCloneJobsResponseOut"])
    types["ApplianceVersionIn"] = t.struct(
        {
            "critical": t.boolean().optional(),
            "version": t.string().optional(),
            "uri": t.string().optional(),
            "releaseNotesUri": t.string().optional(),
        }
    ).named(renames["ApplianceVersionIn"])
    types["ApplianceVersionOut"] = t.struct(
        {
            "critical": t.boolean().optional(),
            "version": t.string().optional(),
            "uri": t.string().optional(),
            "releaseNotesUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplianceVersionOut"])
    types["StartMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartMigrationRequestIn"]
    )
    types["StartMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartMigrationRequestOut"])
    types["ListReplicationCyclesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListReplicationCyclesResponseIn"])
    types["ListReplicationCyclesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "replicationCycles": t.array(
                t.proxy(renames["ReplicationCycleOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReplicationCyclesResponseOut"])
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
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "migratingVms": t.array(t.proxy(renames["MigratingVmOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMigratingVmsResponseOut"])
    types["ReplicationCycleIn"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["CycleStepIn"])).optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "totalPauseDuration": t.string().optional(),
            "cycleNumber": t.integer().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
        }
    ).named(renames["ReplicationCycleIn"])
    types["ReplicationCycleOut"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["CycleStepOut"])).optional(),
            "endTime": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "totalPauseDuration": t.string().optional(),
            "cycleNumber": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "startTime": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "warnings": t.array(t.proxy(renames["MigrationWarningOut"])).optional(),
        }
    ).named(renames["ReplicationCycleOut"])
    types["ReplicationSyncIn"] = t.struct(
        {"lastSyncTime": t.string().optional()}
    ).named(renames["ReplicationSyncIn"])
    types["ReplicationSyncOut"] = t.struct(
        {
            "lastSyncTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicationSyncOut"])
    types["CutoverForecastIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CutoverForecastIn"]
    )
    types["CutoverForecastOut"] = t.struct(
        {
            "estimatedCutoverJobDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoverForecastOut"])
    types["CancelCloneJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelCloneJobRequestIn"]
    )
    types["CancelCloneJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelCloneJobRequestOut"])
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
    types["UtilizationReportIn"] = t.struct(
        {
            "vms": t.array(t.proxy(renames["VmUtilizationInfoIn"])).optional(),
            "displayName": t.string().optional(),
            "timeFrame": t.string().optional(),
        }
    ).named(renames["UtilizationReportIn"])
    types["UtilizationReportOut"] = t.struct(
        {
            "vms": t.array(t.proxy(renames["VmUtilizationInfoOut"])).optional(),
            "vmCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "timeFrame": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "frameEndTime": t.string().optional(),
            "stateTime": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["UtilizationReportOut"])
    types["GroupIn"] = t.struct(
        {"displayName": t.string().optional(), "description": t.string().optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["VmwareSourceDetailsIn"] = t.struct(
        {
            "password": t.string().optional(),
            "thumbprint": t.string().optional(),
            "username": t.string().optional(),
            "vcenterIp": t.string().optional(),
            "resolvedVcenterHost": t.string().optional(),
        }
    ).named(renames["VmwareSourceDetailsIn"])
    types["VmwareSourceDetailsOut"] = t.struct(
        {
            "password": t.string().optional(),
            "thumbprint": t.string().optional(),
            "username": t.string().optional(),
            "vcenterIp": t.string().optional(),
            "resolvedVcenterHost": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareSourceDetailsOut"])
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
    types["UpgradeApplianceRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["UpgradeApplianceRequestIn"])
    types["UpgradeApplianceRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeApplianceRequestOut"])
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
    types["NetworkInterfaceIn"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "internalIp": t.string().optional(),
            "externalIp": t.string().optional(),
            "network": t.string().optional(),
        }
    ).named(renames["NetworkInterfaceIn"])
    types["NetworkInterfaceOut"] = t.struct(
        {
            "subnetwork": t.string().optional(),
            "internalIp": t.string().optional(),
            "externalIp": t.string().optional(),
            "network": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInterfaceOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["DatacenterConnectorIn"] = t.struct(
        {
            "registrationId": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["DatacenterConnectorIn"])
    types["DatacenterConnectorOut"] = t.struct(
        {
            "bucket": t.string().optional(),
            "upgradeStatus": t.proxy(renames["UpgradeStatusOut"]).optional(),
            "updateTime": t.string().optional(),
            "registrationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "stateTime": t.string().optional(),
            "availableVersions": t.proxy(renames["AvailableUpdatesOut"]).optional(),
            "applianceSoftwareVersion": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "version": t.string().optional(),
            "createTime": t.string().optional(),
            "applianceInfrastructureVersion": t.string().optional(),
        }
    ).named(renames["DatacenterConnectorOut"])
    types["AwsSourceVmDetailsIn"] = t.struct(
        {
            "firmware": t.string().optional(),
            "committedStorageBytes": t.string().optional(),
        }
    ).named(renames["AwsSourceVmDetailsIn"])
    types["AwsSourceVmDetailsOut"] = t.struct(
        {
            "firmware": t.string().optional(),
            "committedStorageBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsSourceVmDetailsOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["MigratingVmIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
            "computeEngineTargetDefaults": t.proxy(
                renames["ComputeEngineTargetDefaultsIn"]
            ).optional(),
            "sourceVmId": t.string().optional(),
        }
    ).named(renames["MigratingVmIn"])
    types["MigratingVmOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "cutoverForecast": t.proxy(renames["CutoverForecastOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "recentCloneJobs": t.array(t.proxy(renames["CloneJobOut"])).optional(),
            "recentCutoverJobs": t.array(t.proxy(renames["CutoverJobOut"])).optional(),
            "policy": t.proxy(renames["SchedulePolicyOut"]).optional(),
            "awsSourceVmDetails": t.proxy(renames["AwsSourceVmDetailsOut"]).optional(),
            "computeEngineTargetDefaults": t.proxy(
                renames["ComputeEngineTargetDefaultsOut"]
            ).optional(),
            "sourceVmId": t.string().optional(),
            "stateTime": t.string().optional(),
            "name": t.string().optional(),
            "lastSync": t.proxy(renames["ReplicationSyncOut"]).optional(),
            "state": t.string().optional(),
            "currentSyncInfo": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "group": t.string().optional(),
            "lastReplicationCycle": t.proxy(renames["ReplicationCycleOut"]).optional(),
        }
    ).named(renames["MigratingVmOut"])
    types["TagIn"] = t.struct(
        {"value": t.string().optional(), "key": t.string().optional()}
    ).named(renames["TagIn"])
    types["TagOut"] = t.struct(
        {
            "value": t.string().optional(),
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagOut"])
    types["ResumeMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeMigrationRequestIn"]
    )
    types["ResumeMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeMigrationRequestOut"])
    types["ListDatacenterConnectorsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListDatacenterConnectorsResponseIn"])
    types["ListDatacenterConnectorsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "datacenterConnectors": t.array(
                t.proxy(renames["DatacenterConnectorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatacenterConnectorsResponseOut"])
    types["ListCutoverJobsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListCutoverJobsResponseIn"]
    )
    types["ListCutoverJobsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "cutoverJobs": t.array(t.proxy(renames["CutoverJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCutoverJobsResponseOut"])
    types["ComputeEngineTargetDefaultsIn"] = t.struct(
        {
            "machineType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "secureBoot": t.boolean().optional(),
            "licenseType": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "diskType": t.string().optional(),
            "hostname": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "machineTypeSeries": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "vmName": t.string().optional(),
            "zone": t.string().optional(),
            "targetProject": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceIn"])
            ).optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingIn"]).optional(),
        }
    ).named(renames["ComputeEngineTargetDefaultsIn"])
    types["ComputeEngineTargetDefaultsOut"] = t.struct(
        {
            "machineType": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "secureBoot": t.boolean().optional(),
            "licenseType": t.string().optional(),
            "appliedLicense": t.proxy(renames["AppliedLicenseOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "diskType": t.string().optional(),
            "hostname": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "machineTypeSeries": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "vmName": t.string().optional(),
            "zone": t.string().optional(),
            "targetProject": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceOut"])
            ).optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingOut"]).optional(),
            "bootOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineTargetDefaultsOut"])
    types["ListUtilizationReportsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListUtilizationReportsResponseIn"])
    types["ListUtilizationReportsResponseOut"] = t.struct(
        {
            "utilizationReports": t.array(
                t.proxy(renames["UtilizationReportOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListUtilizationReportsResponseOut"])
    types["VmwareVmsDetailsIn"] = t.struct(
        {"details": t.array(t.proxy(renames["VmwareVmDetailsIn"])).optional()}
    ).named(renames["VmwareVmsDetailsIn"])
    types["VmwareVmsDetailsOut"] = t.struct(
        {
            "details": t.array(t.proxy(renames["VmwareVmDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVmsDetailsOut"])
    types["CloneJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloneJobIn"]
    )
    types["CloneJobOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "endTime": t.string().optional(),
            "computeEngineTargetDetails": t.proxy(
                renames["ComputeEngineTargetDetailsOut"]
            ).optional(),
            "steps": t.array(t.proxy(renames["CloneStepOut"])).optional(),
            "stateTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["CloneJobOut"])
    types["UpgradeStatusIn"] = t.struct(
        {
            "version": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "state": t.string().optional(),
            "previousVersion": t.string().optional(),
        }
    ).named(renames["UpgradeStatusIn"])
    types["UpgradeStatusOut"] = t.struct(
        {
            "version": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
            "previousVersion": t.string().optional(),
        }
    ).named(renames["UpgradeStatusOut"])
    types["TargetProjectIn"] = t.struct(
        {"project": t.string().optional(), "description": t.string().optional()}
    ).named(renames["TargetProjectIn"])
    types["TargetProjectOut"] = t.struct(
        {
            "name": t.string().optional(),
            "project": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetProjectOut"])
    types["MigrationErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MigrationErrorIn"]
    )
    types["MigrationErrorOut"] = t.struct(
        {
            "errorMessage": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "helpLinks": t.array(t.proxy(renames["LinkOut"])).optional(),
            "errorTime": t.string().optional(),
            "code": t.string().optional(),
            "actionItem": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationErrorOut"])
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
    types["VmwareVmDetailsIn"] = t.struct(
        {
            "committedStorageMb": t.string().optional(),
            "datacenterDescription": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "diskCount": t.integer().optional(),
            "vmId": t.string().optional(),
            "uuid": t.string().optional(),
            "guestDescription": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "datacenterId": t.string().optional(),
            "displayName": t.string().optional(),
            "powerState": t.string().optional(),
        }
    ).named(renames["VmwareVmDetailsIn"])
    types["VmwareVmDetailsOut"] = t.struct(
        {
            "bootOption": t.string().optional(),
            "committedStorageMb": t.string().optional(),
            "datacenterDescription": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "diskCount": t.integer().optional(),
            "vmId": t.string().optional(),
            "uuid": t.string().optional(),
            "guestDescription": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "datacenterId": t.string().optional(),
            "displayName": t.string().optional(),
            "powerState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVmDetailsOut"])
    types["PauseMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseMigrationRequestIn"]
    )
    types["PauseMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseMigrationRequestOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["RemoveGroupMigrationRequestIn"] = t.struct(
        {"migratingVm": t.string().optional()}
    ).named(renames["RemoveGroupMigrationRequestIn"])
    types["RemoveGroupMigrationRequestOut"] = t.struct(
        {
            "migratingVm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveGroupMigrationRequestOut"])
    types["VmUtilizationInfoIn"] = t.struct(
        {
            "vmId": t.string().optional(),
            "vmwareVmDetails": t.proxy(renames["VmwareVmDetailsIn"]).optional(),
            "utilization": t.proxy(renames["VmUtilizationMetricsIn"]).optional(),
        }
    ).named(renames["VmUtilizationInfoIn"])
    types["VmUtilizationInfoOut"] = t.struct(
        {
            "vmId": t.string().optional(),
            "vmwareVmDetails": t.proxy(renames["VmwareVmDetailsOut"]).optional(),
            "utilization": t.proxy(renames["VmUtilizationMetricsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmUtilizationInfoOut"])
    types["ListTargetProjectsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListTargetProjectsResponseIn"])
    types["ListTargetProjectsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "targetProjects": t.array(t.proxy(renames["TargetProjectOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTargetProjectsResponseOut"])
    types["AwsVmDetailsIn"] = t.struct(
        {
            "committedStorageMb": t.string().optional(),
            "osDescription": t.string().optional(),
            "virtualizationType": t.string().optional(),
            "sourceId": t.string().optional(),
            "securityGroups": t.array(
                t.proxy(renames["AwsSecurityGroupIn"])
            ).optional(),
            "instanceType": t.string().optional(),
            "vpcId": t.string().optional(),
            "diskCount": t.integer().optional(),
            "architecture": t.string().optional(),
            "tags": t.struct({"_": t.string().optional()}).optional(),
            "cpuCount": t.integer().optional(),
            "sourceDescription": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "displayName": t.string().optional(),
            "zone": t.string().optional(),
            "vmId": t.string().optional(),
            "bootOption": t.string().optional(),
        }
    ).named(renames["AwsVmDetailsIn"])
    types["AwsVmDetailsOut"] = t.struct(
        {
            "committedStorageMb": t.string().optional(),
            "osDescription": t.string().optional(),
            "virtualizationType": t.string().optional(),
            "sourceId": t.string().optional(),
            "securityGroups": t.array(
                t.proxy(renames["AwsSecurityGroupOut"])
            ).optional(),
            "instanceType": t.string().optional(),
            "vpcId": t.string().optional(),
            "diskCount": t.integer().optional(),
            "architecture": t.string().optional(),
            "powerState": t.string().optional(),
            "tags": t.struct({"_": t.string().optional()}).optional(),
            "cpuCount": t.integer().optional(),
            "sourceDescription": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "displayName": t.string().optional(),
            "zone": t.string().optional(),
            "vmId": t.string().optional(),
            "bootOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsVmDetailsOut"])
    types["AppliedLicenseIn"] = t.struct(
        {"type": t.string().optional(), "osLicense": t.string().optional()}
    ).named(renames["AppliedLicenseIn"])
    types["AppliedLicenseOut"] = t.struct(
        {
            "type": t.string().optional(),
            "osLicense": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppliedLicenseOut"])
    types["CycleStepIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "postProcessing": t.proxy(renames["PostProcessingStepIn"]).optional(),
            "replicating": t.proxy(renames["ReplicatingStepIn"]).optional(),
            "startTime": t.string().optional(),
            "initializingReplication": t.proxy(
                renames["InitializingReplicationStepIn"]
            ).optional(),
        }
    ).named(renames["CycleStepIn"])
    types["CycleStepOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "postProcessing": t.proxy(renames["PostProcessingStepOut"]).optional(),
            "replicating": t.proxy(renames["ReplicatingStepOut"]).optional(),
            "startTime": t.string().optional(),
            "initializingReplication": t.proxy(
                renames["InitializingReplicationStepOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CycleStepOut"])
    types["CancelCutoverJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelCutoverJobRequestIn"]
    )
    types["CancelCutoverJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelCutoverJobRequestOut"])
    types["MigrationWarningIn"] = t.struct(
        {
            "helpLinks": t.array(t.proxy(renames["LinkIn"])).optional(),
            "code": t.string().optional(),
            "warningMessage": t.proxy(renames["LocalizedMessageIn"]).optional(),
            "actionItem": t.proxy(renames["LocalizedMessageIn"]).optional(),
            "warningTime": t.string().optional(),
        }
    ).named(renames["MigrationWarningIn"])
    types["MigrationWarningOut"] = t.struct(
        {
            "helpLinks": t.array(t.proxy(renames["LinkOut"])).optional(),
            "code": t.string().optional(),
            "warningMessage": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "actionItem": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "warningTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationWarningOut"])
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
    types["PreparingVMDisksStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PreparingVMDisksStepIn"]
    )
    types["PreparingVMDisksStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PreparingVMDisksStepOut"])
    types["CloneStepIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "adaptingOs": t.proxy(renames["AdaptingOSStepIn"]).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepIn"]).optional(),
            "endTime": t.string().optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepIn"]
            ).optional(),
        }
    ).named(renames["CloneStepIn"])
    types["CloneStepOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "adaptingOs": t.proxy(renames["AdaptingOSStepOut"]).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepOut"]).optional(),
            "endTime": t.string().optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneStepOut"])
    types["ListGroupsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListGroupsResponseIn"]
    )
    types["ListGroupsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["AwsSourceDetailsIn"] = t.struct(
        {
            "inventoryTagList": t.array(t.proxy(renames["TagIn"])).optional(),
            "inventorySecurityGroupNames": t.array(t.string()).optional(),
            "migrationResourcesUserTags": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "accessKeyCreds": t.proxy(renames["AccessKeyCredentialsIn"]).optional(),
            "awsRegion": t.string().optional(),
        }
    ).named(renames["AwsSourceDetailsIn"])
    types["AwsSourceDetailsOut"] = t.struct(
        {
            "inventoryTagList": t.array(t.proxy(renames["TagOut"])).optional(),
            "inventorySecurityGroupNames": t.array(t.string()).optional(),
            "migrationResourcesUserTags": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "state": t.string().optional(),
            "accessKeyCreds": t.proxy(renames["AccessKeyCredentialsOut"]).optional(),
            "awsRegion": t.string().optional(),
            "publicIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsSourceDetailsOut"])
    types["AddGroupMigrationRequestIn"] = t.struct(
        {"migratingVm": t.string().optional()}
    ).named(renames["AddGroupMigrationRequestIn"])
    types["AddGroupMigrationRequestOut"] = t.struct(
        {
            "migratingVm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddGroupMigrationRequestOut"])
    types["ComputeSchedulingIn"] = t.struct(
        {
            "onHostMaintenance": t.string().optional(),
            "nodeAffinities": t.array(
                t.proxy(renames["SchedulingNodeAffinityIn"])
            ).optional(),
            "restartType": t.string().optional(),
            "minNodeCpus": t.integer().optional(),
        }
    ).named(renames["ComputeSchedulingIn"])
    types["ComputeSchedulingOut"] = t.struct(
        {
            "onHostMaintenance": t.string().optional(),
            "nodeAffinities": t.array(
                t.proxy(renames["SchedulingNodeAffinityOut"])
            ).optional(),
            "restartType": t.string().optional(),
            "minNodeCpus": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeSchedulingOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LocalizedMessageIn"] = t.struct(
        {"locale": t.string().optional(), "message": t.string().optional()}
    ).named(renames["LocalizedMessageIn"])
    types["LocalizedMessageOut"] = t.struct(
        {
            "locale": t.string().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalizedMessageOut"])

    functions = {}
    functions["projectsLocationsList"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsDelete"] = vmmigration.post(
        "v1/{parent}/targetProjects",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "targetProjectId": t.string(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsGet"] = vmmigration.post(
        "v1/{parent}/targetProjects",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "targetProjectId": t.string(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsList"] = vmmigration.post(
        "v1/{parent}/targetProjects",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "targetProjectId": t.string(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsPatch"] = vmmigration.post(
        "v1/{parent}/targetProjects",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "targetProjectId": t.string(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsCreate"] = vmmigration.post(
        "v1/{parent}/targetProjects",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "targetProjectId": t.string(),
                "project": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsGroupsDelete"] = vmmigration.get(
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
    functions["projectsLocationsGroupsRemoveGroupMigration"] = vmmigration.get(
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
    functions["projectsLocationsGroupsAddGroupMigration"] = vmmigration.get(
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
    functions["projectsLocationsOperationsList"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesPatch"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesList"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesCreate"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDelete"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesFetchInventory"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SourceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesGet"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["SourceOut"]),
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
    functions["projectsLocationsSourcesDatacenterConnectorsGet"] = vmmigration.delete(
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
    functions[
        "projectsLocationsSourcesDatacenterConnectorsUpgradeAppliance"
    ] = vmmigration.delete(
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
    functions[
        "projectsLocationsSourcesDatacenterConnectorsCreate"
    ] = vmmigration.delete(
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
    functions["projectsLocationsSourcesDatacenterConnectorsList"] = vmmigration.delete(
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
    functions[
        "projectsLocationsSourcesDatacenterConnectorsDelete"
    ] = vmmigration.delete(
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
    functions["projectsLocationsSourcesMigratingVmsDelete"] = vmmigration.post(
        "v1/{migratingVm}:finalizeMigration",
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
        "v1/{migratingVm}:finalizeMigration",
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
        "v1/{migratingVm}:finalizeMigration",
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
    functions["projectsLocationsSourcesMigratingVmsResumeMigration"] = vmmigration.post(
        "v1/{migratingVm}:finalizeMigration",
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
        "v1/{migratingVm}:finalizeMigration",
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
        "v1/{migratingVm}:finalizeMigration",
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
        "v1/{migratingVm}:finalizeMigration",
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
        "v1/{migratingVm}:finalizeMigration",
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
        "v1/{migratingVm}:finalizeMigration",
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
        "projectsLocationsSourcesMigratingVmsReplicationCyclesGet"
    ] = vmmigration.get(
        "v1/{parent}/replicationCycles",
        t.struct(
            {
                "orderBy": t.string().optional(),
                "pageToken": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
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
                "orderBy": t.string().optional(),
                "pageToken": t.string(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListReplicationCyclesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCutoverJobsList"] = vmmigration.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
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
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCutoverJobsGet"] = vmmigration.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
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
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string(),
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

    return Import(
        importer="vmmigration",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
