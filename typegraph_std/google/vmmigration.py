from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_vmmigration() -> Import:
    vmmigration = HTTPRuntime("https://vmmigration.googleapis.com/")

    renames = {
        "ErrorResponse": "_vmmigration_1_ErrorResponse",
        "TargetProjectIn": "_vmmigration_2_TargetProjectIn",
        "TargetProjectOut": "_vmmigration_3_TargetProjectOut",
        "ListDatacenterConnectorsResponseIn": "_vmmigration_4_ListDatacenterConnectorsResponseIn",
        "ListDatacenterConnectorsResponseOut": "_vmmigration_5_ListDatacenterConnectorsResponseOut",
        "AddGroupMigrationRequestIn": "_vmmigration_6_AddGroupMigrationRequestIn",
        "AddGroupMigrationRequestOut": "_vmmigration_7_AddGroupMigrationRequestOut",
        "CutoverJobIn": "_vmmigration_8_CutoverJobIn",
        "CutoverJobOut": "_vmmigration_9_CutoverJobOut",
        "AdaptingOSStepIn": "_vmmigration_10_AdaptingOSStepIn",
        "AdaptingOSStepOut": "_vmmigration_11_AdaptingOSStepOut",
        "UtilizationReportIn": "_vmmigration_12_UtilizationReportIn",
        "UtilizationReportOut": "_vmmigration_13_UtilizationReportOut",
        "UpgradeApplianceRequestIn": "_vmmigration_14_UpgradeApplianceRequestIn",
        "UpgradeApplianceRequestOut": "_vmmigration_15_UpgradeApplianceRequestOut",
        "AwsVmsDetailsIn": "_vmmigration_16_AwsVmsDetailsIn",
        "AwsVmsDetailsOut": "_vmmigration_17_AwsVmsDetailsOut",
        "ListReplicationCyclesResponseIn": "_vmmigration_18_ListReplicationCyclesResponseIn",
        "ListReplicationCyclesResponseOut": "_vmmigration_19_ListReplicationCyclesResponseOut",
        "ListGroupsResponseIn": "_vmmigration_20_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_vmmigration_21_ListGroupsResponseOut",
        "CutoverStepIn": "_vmmigration_22_CutoverStepIn",
        "CutoverStepOut": "_vmmigration_23_CutoverStepOut",
        "AppliedLicenseIn": "_vmmigration_24_AppliedLicenseIn",
        "AppliedLicenseOut": "_vmmigration_25_AppliedLicenseOut",
        "AwsVmDetailsIn": "_vmmigration_26_AwsVmDetailsIn",
        "AwsVmDetailsOut": "_vmmigration_27_AwsVmDetailsOut",
        "CloneStepIn": "_vmmigration_28_CloneStepIn",
        "CloneStepOut": "_vmmigration_29_CloneStepOut",
        "ReplicationCycleIn": "_vmmigration_30_ReplicationCycleIn",
        "ReplicationCycleOut": "_vmmigration_31_ReplicationCycleOut",
        "AccessKeyCredentialsIn": "_vmmigration_32_AccessKeyCredentialsIn",
        "AccessKeyCredentialsOut": "_vmmigration_33_AccessKeyCredentialsOut",
        "PauseMigrationRequestIn": "_vmmigration_34_PauseMigrationRequestIn",
        "PauseMigrationRequestOut": "_vmmigration_35_PauseMigrationRequestOut",
        "LinkIn": "_vmmigration_36_LinkIn",
        "LinkOut": "_vmmigration_37_LinkOut",
        "VmUtilizationInfoIn": "_vmmigration_38_VmUtilizationInfoIn",
        "VmUtilizationInfoOut": "_vmmigration_39_VmUtilizationInfoOut",
        "AvailableUpdatesIn": "_vmmigration_40_AvailableUpdatesIn",
        "AvailableUpdatesOut": "_vmmigration_41_AvailableUpdatesOut",
        "TagIn": "_vmmigration_42_TagIn",
        "TagOut": "_vmmigration_43_TagOut",
        "ListOperationsResponseIn": "_vmmigration_44_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vmmigration_45_ListOperationsResponseOut",
        "FinalizeMigrationRequestIn": "_vmmigration_46_FinalizeMigrationRequestIn",
        "FinalizeMigrationRequestOut": "_vmmigration_47_FinalizeMigrationRequestOut",
        "LocationIn": "_vmmigration_48_LocationIn",
        "LocationOut": "_vmmigration_49_LocationOut",
        "AwsSourceVmDetailsIn": "_vmmigration_50_AwsSourceVmDetailsIn",
        "AwsSourceVmDetailsOut": "_vmmigration_51_AwsSourceVmDetailsOut",
        "PostProcessingStepIn": "_vmmigration_52_PostProcessingStepIn",
        "PostProcessingStepOut": "_vmmigration_53_PostProcessingStepOut",
        "LocalizedMessageIn": "_vmmigration_54_LocalizedMessageIn",
        "LocalizedMessageOut": "_vmmigration_55_LocalizedMessageOut",
        "ListSourcesResponseIn": "_vmmigration_56_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_vmmigration_57_ListSourcesResponseOut",
        "ReplicationSyncIn": "_vmmigration_58_ReplicationSyncIn",
        "ReplicationSyncOut": "_vmmigration_59_ReplicationSyncOut",
        "CancelCloneJobRequestIn": "_vmmigration_60_CancelCloneJobRequestIn",
        "CancelCloneJobRequestOut": "_vmmigration_61_CancelCloneJobRequestOut",
        "CancelCutoverJobRequestIn": "_vmmigration_62_CancelCutoverJobRequestIn",
        "CancelCutoverJobRequestOut": "_vmmigration_63_CancelCutoverJobRequestOut",
        "UpgradeStatusIn": "_vmmigration_64_UpgradeStatusIn",
        "UpgradeStatusOut": "_vmmigration_65_UpgradeStatusOut",
        "RemoveGroupMigrationRequestIn": "_vmmigration_66_RemoveGroupMigrationRequestIn",
        "RemoveGroupMigrationRequestOut": "_vmmigration_67_RemoveGroupMigrationRequestOut",
        "StatusIn": "_vmmigration_68_StatusIn",
        "StatusOut": "_vmmigration_69_StatusOut",
        "VmwareVmDetailsIn": "_vmmigration_70_VmwareVmDetailsIn",
        "VmwareVmDetailsOut": "_vmmigration_71_VmwareVmDetailsOut",
        "CancelOperationRequestIn": "_vmmigration_72_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vmmigration_73_CancelOperationRequestOut",
        "ListLocationsResponseIn": "_vmmigration_74_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_vmmigration_75_ListLocationsResponseOut",
        "VmUtilizationMetricsIn": "_vmmigration_76_VmUtilizationMetricsIn",
        "VmUtilizationMetricsOut": "_vmmigration_77_VmUtilizationMetricsOut",
        "ShuttingDownSourceVMStepIn": "_vmmigration_78_ShuttingDownSourceVMStepIn",
        "ShuttingDownSourceVMStepOut": "_vmmigration_79_ShuttingDownSourceVMStepOut",
        "MigrationErrorIn": "_vmmigration_80_MigrationErrorIn",
        "MigrationErrorOut": "_vmmigration_81_MigrationErrorOut",
        "InitializingReplicationStepIn": "_vmmigration_82_InitializingReplicationStepIn",
        "InitializingReplicationStepOut": "_vmmigration_83_InitializingReplicationStepOut",
        "OperationIn": "_vmmigration_84_OperationIn",
        "OperationOut": "_vmmigration_85_OperationOut",
        "OperationMetadataIn": "_vmmigration_86_OperationMetadataIn",
        "OperationMetadataOut": "_vmmigration_87_OperationMetadataOut",
        "SchedulingNodeAffinityIn": "_vmmigration_88_SchedulingNodeAffinityIn",
        "SchedulingNodeAffinityOut": "_vmmigration_89_SchedulingNodeAffinityOut",
        "DatacenterConnectorIn": "_vmmigration_90_DatacenterConnectorIn",
        "DatacenterConnectorOut": "_vmmigration_91_DatacenterConnectorOut",
        "ResumeMigrationRequestIn": "_vmmigration_92_ResumeMigrationRequestIn",
        "ResumeMigrationRequestOut": "_vmmigration_93_ResumeMigrationRequestOut",
        "CutoverForecastIn": "_vmmigration_94_CutoverForecastIn",
        "CutoverForecastOut": "_vmmigration_95_CutoverForecastOut",
        "ListMigratingVmsResponseIn": "_vmmigration_96_ListMigratingVmsResponseIn",
        "ListMigratingVmsResponseOut": "_vmmigration_97_ListMigratingVmsResponseOut",
        "VmwareVmsDetailsIn": "_vmmigration_98_VmwareVmsDetailsIn",
        "VmwareVmsDetailsOut": "_vmmigration_99_VmwareVmsDetailsOut",
        "MigrationWarningIn": "_vmmigration_100_MigrationWarningIn",
        "MigrationWarningOut": "_vmmigration_101_MigrationWarningOut",
        "MigratingVmIn": "_vmmigration_102_MigratingVmIn",
        "MigratingVmOut": "_vmmigration_103_MigratingVmOut",
        "ListTargetProjectsResponseIn": "_vmmigration_104_ListTargetProjectsResponseIn",
        "ListTargetProjectsResponseOut": "_vmmigration_105_ListTargetProjectsResponseOut",
        "AwsSourceDetailsIn": "_vmmigration_106_AwsSourceDetailsIn",
        "AwsSourceDetailsOut": "_vmmigration_107_AwsSourceDetailsOut",
        "ListCutoverJobsResponseIn": "_vmmigration_108_ListCutoverJobsResponseIn",
        "ListCutoverJobsResponseOut": "_vmmigration_109_ListCutoverJobsResponseOut",
        "SchedulePolicyIn": "_vmmigration_110_SchedulePolicyIn",
        "SchedulePolicyOut": "_vmmigration_111_SchedulePolicyOut",
        "SourceIn": "_vmmigration_112_SourceIn",
        "SourceOut": "_vmmigration_113_SourceOut",
        "ComputeSchedulingIn": "_vmmigration_114_ComputeSchedulingIn",
        "ComputeSchedulingOut": "_vmmigration_115_ComputeSchedulingOut",
        "AwsSecurityGroupIn": "_vmmigration_116_AwsSecurityGroupIn",
        "AwsSecurityGroupOut": "_vmmigration_117_AwsSecurityGroupOut",
        "StartMigrationRequestIn": "_vmmigration_118_StartMigrationRequestIn",
        "StartMigrationRequestOut": "_vmmigration_119_StartMigrationRequestOut",
        "NetworkInterfaceIn": "_vmmigration_120_NetworkInterfaceIn",
        "NetworkInterfaceOut": "_vmmigration_121_NetworkInterfaceOut",
        "EmptyIn": "_vmmigration_122_EmptyIn",
        "EmptyOut": "_vmmigration_123_EmptyOut",
        "ListCloneJobsResponseIn": "_vmmigration_124_ListCloneJobsResponseIn",
        "ListCloneJobsResponseOut": "_vmmigration_125_ListCloneJobsResponseOut",
        "CloneJobIn": "_vmmigration_126_CloneJobIn",
        "CloneJobOut": "_vmmigration_127_CloneJobOut",
        "ComputeEngineTargetDefaultsIn": "_vmmigration_128_ComputeEngineTargetDefaultsIn",
        "ComputeEngineTargetDefaultsOut": "_vmmigration_129_ComputeEngineTargetDefaultsOut",
        "FetchInventoryResponseIn": "_vmmigration_130_FetchInventoryResponseIn",
        "FetchInventoryResponseOut": "_vmmigration_131_FetchInventoryResponseOut",
        "ComputeEngineTargetDetailsIn": "_vmmigration_132_ComputeEngineTargetDetailsIn",
        "ComputeEngineTargetDetailsOut": "_vmmigration_133_ComputeEngineTargetDetailsOut",
        "ReplicatingStepIn": "_vmmigration_134_ReplicatingStepIn",
        "ReplicatingStepOut": "_vmmigration_135_ReplicatingStepOut",
        "ApplianceVersionIn": "_vmmigration_136_ApplianceVersionIn",
        "ApplianceVersionOut": "_vmmigration_137_ApplianceVersionOut",
        "CycleStepIn": "_vmmigration_138_CycleStepIn",
        "CycleStepOut": "_vmmigration_139_CycleStepOut",
        "PreparingVMDisksStepIn": "_vmmigration_140_PreparingVMDisksStepIn",
        "PreparingVMDisksStepOut": "_vmmigration_141_PreparingVMDisksStepOut",
        "GroupIn": "_vmmigration_142_GroupIn",
        "GroupOut": "_vmmigration_143_GroupOut",
        "ListUtilizationReportsResponseIn": "_vmmigration_144_ListUtilizationReportsResponseIn",
        "ListUtilizationReportsResponseOut": "_vmmigration_145_ListUtilizationReportsResponseOut",
        "InstantiatingMigratedVMStepIn": "_vmmigration_146_InstantiatingMigratedVMStepIn",
        "InstantiatingMigratedVMStepOut": "_vmmigration_147_InstantiatingMigratedVMStepOut",
        "VmwareSourceDetailsIn": "_vmmigration_148_VmwareSourceDetailsIn",
        "VmwareSourceDetailsOut": "_vmmigration_149_VmwareSourceDetailsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TargetProjectIn"] = t.struct(
        {"description": t.string().optional(), "project": t.string().optional()}
    ).named(renames["TargetProjectIn"])
    types["TargetProjectOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetProjectOut"])
    types["ListDatacenterConnectorsResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListDatacenterConnectorsResponseIn"])
    types["ListDatacenterConnectorsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "datacenterConnectors": t.array(
                t.proxy(renames["DatacenterConnectorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListDatacenterConnectorsResponseOut"])
    types["AddGroupMigrationRequestIn"] = t.struct(
        {"migratingVm": t.string().optional()}
    ).named(renames["AddGroupMigrationRequestIn"])
    types["AddGroupMigrationRequestOut"] = t.struct(
        {
            "migratingVm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddGroupMigrationRequestOut"])
    types["CutoverJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CutoverJobIn"]
    )
    types["CutoverJobOut"] = t.struct(
        {
            "computeEngineTargetDetails": t.proxy(
                renames["ComputeEngineTargetDetailsOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "stateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "stateMessage": t.string().optional(),
            "steps": t.array(t.proxy(renames["CutoverStepOut"])).optional(),
            "progressPercent": t.integer().optional(),
        }
    ).named(renames["CutoverJobOut"])
    types["AdaptingOSStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdaptingOSStepIn"]
    )
    types["AdaptingOSStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdaptingOSStepOut"])
    types["UtilizationReportIn"] = t.struct(
        {
            "timeFrame": t.string().optional(),
            "displayName": t.string().optional(),
            "vms": t.array(t.proxy(renames["VmUtilizationInfoIn"])).optional(),
        }
    ).named(renames["UtilizationReportIn"])
    types["UtilizationReportOut"] = t.struct(
        {
            "timeFrame": t.string().optional(),
            "vmCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "frameEndTime": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "vms": t.array(t.proxy(renames["VmUtilizationInfoOut"])).optional(),
            "name": t.string().optional(),
            "stateTime": t.string().optional(),
        }
    ).named(renames["UtilizationReportOut"])
    types["UpgradeApplianceRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["UpgradeApplianceRequestIn"])
    types["UpgradeApplianceRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeApplianceRequestOut"])
    types["AwsVmsDetailsIn"] = t.struct(
        {"details": t.array(t.proxy(renames["AwsVmDetailsIn"])).optional()}
    ).named(renames["AwsVmsDetailsIn"])
    types["AwsVmsDetailsOut"] = t.struct(
        {
            "details": t.array(t.proxy(renames["AwsVmDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsVmsDetailsOut"])
    types["ListReplicationCyclesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListReplicationCyclesResponseIn"])
    types["ListReplicationCyclesResponseOut"] = t.struct(
        {
            "replicationCycles": t.array(
                t.proxy(renames["ReplicationCycleOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReplicationCyclesResponseOut"])
    types["ListGroupsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListGroupsResponseIn"]
    )
    types["ListGroupsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["CutoverStepIn"] = t.struct(
        {
            "finalSync": t.proxy(renames["ReplicationCycleIn"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "previousReplicationCycle": t.proxy(
                renames["ReplicationCycleIn"]
            ).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepIn"]).optional(),
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
            "finalSync": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "previousReplicationCycle": t.proxy(
                renames["ReplicationCycleOut"]
            ).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepOut"]).optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepOut"]
            ).optional(),
            "shuttingDownSourceVm": t.proxy(
                renames["ShuttingDownSourceVMStepOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoverStepOut"])
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
    types["AwsVmDetailsIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "virtualizationType": t.string().optional(),
            "sourceId": t.string().optional(),
            "instanceType": t.string().optional(),
            "committedStorageMb": t.string().optional(),
            "diskCount": t.integer().optional(),
            "memoryMb": t.integer().optional(),
            "osDescription": t.string().optional(),
            "bootOption": t.string().optional(),
            "securityGroups": t.array(
                t.proxy(renames["AwsSecurityGroupIn"])
            ).optional(),
            "tags": t.struct({"_": t.string().optional()}).optional(),
            "vmId": t.string().optional(),
            "architecture": t.string().optional(),
            "vpcId": t.string().optional(),
            "sourceDescription": t.string().optional(),
        }
    ).named(renames["AwsVmDetailsIn"])
    types["AwsVmDetailsOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "virtualizationType": t.string().optional(),
            "sourceId": t.string().optional(),
            "instanceType": t.string().optional(),
            "committedStorageMb": t.string().optional(),
            "diskCount": t.integer().optional(),
            "memoryMb": t.integer().optional(),
            "osDescription": t.string().optional(),
            "bootOption": t.string().optional(),
            "securityGroups": t.array(
                t.proxy(renames["AwsSecurityGroupOut"])
            ).optional(),
            "tags": t.struct({"_": t.string().optional()}).optional(),
            "vmId": t.string().optional(),
            "architecture": t.string().optional(),
            "vpcId": t.string().optional(),
            "powerState": t.string().optional(),
            "sourceDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsVmDetailsOut"])
    types["CloneStepIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "adaptingOs": t.proxy(renames["AdaptingOSStepIn"]).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepIn"]).optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepIn"]
            ).optional(),
        }
    ).named(renames["CloneStepIn"])
    types["CloneStepOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "adaptingOs": t.proxy(renames["AdaptingOSStepOut"]).optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepOut"]).optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneStepOut"])
    types["ReplicationCycleIn"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["CycleStepIn"])).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "totalPauseDuration": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "cycleNumber": t.integer().optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["ReplicationCycleIn"])
    types["ReplicationCycleOut"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["CycleStepOut"])).optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "totalPauseDuration": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "cycleNumber": t.integer().optional(),
            "warnings": t.array(t.proxy(renames["MigrationWarningOut"])).optional(),
            "startTime": t.string().optional(),
        }
    ).named(renames["ReplicationCycleOut"])
    types["AccessKeyCredentialsIn"] = t.struct(
        {
            "accessKeyId": t.string().optional(),
            "secretAccessKey": t.string().optional(),
            "sessionToken": t.string().optional(),
        }
    ).named(renames["AccessKeyCredentialsIn"])
    types["AccessKeyCredentialsOut"] = t.struct(
        {
            "accessKeyId": t.string().optional(),
            "secretAccessKey": t.string().optional(),
            "sessionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessKeyCredentialsOut"])
    types["PauseMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseMigrationRequestIn"]
    )
    types["PauseMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseMigrationRequestOut"])
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
    types["AvailableUpdatesIn"] = t.struct(
        {
            "inPlaceUpdate": t.proxy(renames["ApplianceVersionIn"]).optional(),
            "newDeployableAppliance": t.proxy(renames["ApplianceVersionIn"]).optional(),
        }
    ).named(renames["AvailableUpdatesIn"])
    types["AvailableUpdatesOut"] = t.struct(
        {
            "inPlaceUpdate": t.proxy(renames["ApplianceVersionOut"]).optional(),
            "newDeployableAppliance": t.proxy(
                renames["ApplianceVersionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AvailableUpdatesOut"])
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
    types["FinalizeMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FinalizeMigrationRequestIn"]
    )
    types["FinalizeMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FinalizeMigrationRequestOut"])
    types["LocationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["PostProcessingStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PostProcessingStepIn"]
    )
    types["PostProcessingStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PostProcessingStepOut"])
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
    types["ListSourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListSourcesResponseIn"]
    )
    types["ListSourcesResponseOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSourcesResponseOut"])
    types["ReplicationSyncIn"] = t.struct(
        {"lastSyncTime": t.string().optional()}
    ).named(renames["ReplicationSyncIn"])
    types["ReplicationSyncOut"] = t.struct(
        {
            "lastSyncTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicationSyncOut"])
    types["CancelCloneJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelCloneJobRequestIn"]
    )
    types["CancelCloneJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelCloneJobRequestOut"])
    types["CancelCutoverJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelCutoverJobRequestIn"]
    )
    types["CancelCutoverJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelCutoverJobRequestOut"])
    types["UpgradeStatusIn"] = t.struct(
        {
            "state": t.string().optional(),
            "version": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "previousVersion": t.string().optional(),
        }
    ).named(renames["UpgradeStatusIn"])
    types["UpgradeStatusOut"] = t.struct(
        {
            "state": t.string().optional(),
            "version": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "previousVersion": t.string().optional(),
        }
    ).named(renames["UpgradeStatusOut"])
    types["RemoveGroupMigrationRequestIn"] = t.struct(
        {"migratingVm": t.string().optional()}
    ).named(renames["RemoveGroupMigrationRequestIn"])
    types["RemoveGroupMigrationRequestOut"] = t.struct(
        {
            "migratingVm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveGroupMigrationRequestOut"])
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
    types["VmwareVmDetailsIn"] = t.struct(
        {
            "powerState": t.string().optional(),
            "datacenterDescription": t.string().optional(),
            "guestDescription": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "cpuCount": t.integer().optional(),
            "datacenterId": t.string().optional(),
            "uuid": t.string().optional(),
            "diskCount": t.integer().optional(),
            "vmId": t.string().optional(),
            "committedStorageMb": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["VmwareVmDetailsIn"])
    types["VmwareVmDetailsOut"] = t.struct(
        {
            "powerState": t.string().optional(),
            "datacenterDescription": t.string().optional(),
            "guestDescription": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "cpuCount": t.integer().optional(),
            "datacenterId": t.string().optional(),
            "uuid": t.string().optional(),
            "diskCount": t.integer().optional(),
            "vmId": t.string().optional(),
            "committedStorageMb": t.string().optional(),
            "displayName": t.string().optional(),
            "bootOption": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVmDetailsOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["VmUtilizationMetricsIn"] = t.struct(
        {
            "cpuAveragePercent": t.integer().optional(),
            "diskIoRateAverageKbps": t.string().optional(),
            "networkThroughputAverageKbps": t.string().optional(),
            "memoryAveragePercent": t.integer().optional(),
            "networkThroughputMaxKbps": t.string().optional(),
            "diskIoRateMaxKbps": t.string().optional(),
            "memoryMaxPercent": t.integer().optional(),
            "cpuMaxPercent": t.integer().optional(),
        }
    ).named(renames["VmUtilizationMetricsIn"])
    types["VmUtilizationMetricsOut"] = t.struct(
        {
            "cpuAveragePercent": t.integer().optional(),
            "diskIoRateAverageKbps": t.string().optional(),
            "networkThroughputAverageKbps": t.string().optional(),
            "memoryAveragePercent": t.integer().optional(),
            "networkThroughputMaxKbps": t.string().optional(),
            "diskIoRateMaxKbps": t.string().optional(),
            "memoryMaxPercent": t.integer().optional(),
            "cpuMaxPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmUtilizationMetricsOut"])
    types["ShuttingDownSourceVMStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ShuttingDownSourceVMStepIn"]
    )
    types["ShuttingDownSourceVMStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ShuttingDownSourceVMStepOut"])
    types["MigrationErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MigrationErrorIn"]
    )
    types["MigrationErrorOut"] = t.struct(
        {
            "code": t.string().optional(),
            "errorMessage": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "errorTime": t.string().optional(),
            "actionItem": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "helpLinks": t.array(t.proxy(renames["LinkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationErrorOut"])
    types["InitializingReplicationStepIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InitializingReplicationStepIn"])
    types["InitializingReplicationStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InitializingReplicationStepOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["SchedulingNodeAffinityIn"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "operator": t.string().optional(),
        }
    ).named(renames["SchedulingNodeAffinityIn"])
    types["SchedulingNodeAffinityOut"] = t.struct(
        {
            "values": t.array(t.string()).optional(),
            "key": t.string().optional(),
            "operator": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulingNodeAffinityOut"])
    types["DatacenterConnectorIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "registrationId": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["DatacenterConnectorIn"])
    types["DatacenterConnectorOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "name": t.string().optional(),
            "registrationId": t.string().optional(),
            "version": t.string().optional(),
            "upgradeStatus": t.proxy(renames["UpgradeStatusOut"]).optional(),
            "stateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "applianceSoftwareVersion": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
            "applianceInfrastructureVersion": t.string().optional(),
            "availableVersions": t.proxy(renames["AvailableUpdatesOut"]).optional(),
            "bucket": t.string().optional(),
        }
    ).named(renames["DatacenterConnectorOut"])
    types["ResumeMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeMigrationRequestIn"]
    )
    types["ResumeMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeMigrationRequestOut"])
    types["CutoverForecastIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CutoverForecastIn"]
    )
    types["CutoverForecastOut"] = t.struct(
        {
            "estimatedCutoverJobDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoverForecastOut"])
    types["ListMigratingVmsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListMigratingVmsResponseIn"]
    )
    types["ListMigratingVmsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "migratingVms": t.array(t.proxy(renames["MigratingVmOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMigratingVmsResponseOut"])
    types["VmwareVmsDetailsIn"] = t.struct(
        {"details": t.array(t.proxy(renames["VmwareVmDetailsIn"])).optional()}
    ).named(renames["VmwareVmsDetailsIn"])
    types["VmwareVmsDetailsOut"] = t.struct(
        {
            "details": t.array(t.proxy(renames["VmwareVmDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVmsDetailsOut"])
    types["MigrationWarningIn"] = t.struct(
        {
            "helpLinks": t.array(t.proxy(renames["LinkIn"])).optional(),
            "warningMessage": t.proxy(renames["LocalizedMessageIn"]).optional(),
            "code": t.string().optional(),
            "actionItem": t.proxy(renames["LocalizedMessageIn"]).optional(),
            "warningTime": t.string().optional(),
        }
    ).named(renames["MigrationWarningIn"])
    types["MigrationWarningOut"] = t.struct(
        {
            "helpLinks": t.array(t.proxy(renames["LinkOut"])).optional(),
            "warningMessage": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "code": t.string().optional(),
            "actionItem": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "warningTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationWarningOut"])
    types["MigratingVmIn"] = t.struct(
        {
            "description": t.string().optional(),
            "sourceVmId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
            "computeEngineTargetDefaults": t.proxy(
                renames["ComputeEngineTargetDefaultsIn"]
            ).optional(),
        }
    ).named(renames["MigratingVmIn"])
    types["MigratingVmOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "group": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "lastReplicationCycle": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "sourceVmId": t.string().optional(),
            "recentCutoverJobs": t.array(t.proxy(renames["CutoverJobOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "policy": t.proxy(renames["SchedulePolicyOut"]).optional(),
            "currentSyncInfo": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "stateTime": t.string().optional(),
            "awsSourceVmDetails": t.proxy(renames["AwsSourceVmDetailsOut"]).optional(),
            "recentCloneJobs": t.array(t.proxy(renames["CloneJobOut"])).optional(),
            "lastSync": t.proxy(renames["ReplicationSyncOut"]).optional(),
            "cutoverForecast": t.proxy(renames["CutoverForecastOut"]).optional(),
            "computeEngineTargetDefaults": t.proxy(
                renames["ComputeEngineTargetDefaultsOut"]
            ).optional(),
            "updateTime": t.string().optional(),
        }
    ).named(renames["MigratingVmOut"])
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
    types["AwsSourceDetailsIn"] = t.struct(
        {
            "inventorySecurityGroupNames": t.array(t.string()).optional(),
            "awsRegion": t.string().optional(),
            "inventoryTagList": t.array(t.proxy(renames["TagIn"])).optional(),
            "accessKeyCreds": t.proxy(renames["AccessKeyCredentialsIn"]).optional(),
            "migrationResourcesUserTags": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["AwsSourceDetailsIn"])
    types["AwsSourceDetailsOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "inventorySecurityGroupNames": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "awsRegion": t.string().optional(),
            "inventoryTagList": t.array(t.proxy(renames["TagOut"])).optional(),
            "publicIp": t.string().optional(),
            "accessKeyCreds": t.proxy(renames["AccessKeyCredentialsOut"]).optional(),
            "migrationResourcesUserTags": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["AwsSourceDetailsOut"])
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
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "aws": t.proxy(renames["AwsSourceDetailsOut"]).optional(),
            "vmware": t.proxy(renames["VmwareSourceDetailsOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
    types["ComputeSchedulingIn"] = t.struct(
        {
            "restartType": t.string().optional(),
            "nodeAffinities": t.array(
                t.proxy(renames["SchedulingNodeAffinityIn"])
            ).optional(),
            "onHostMaintenance": t.string().optional(),
            "minNodeCpus": t.integer().optional(),
        }
    ).named(renames["ComputeSchedulingIn"])
    types["ComputeSchedulingOut"] = t.struct(
        {
            "restartType": t.string().optional(),
            "nodeAffinities": t.array(
                t.proxy(renames["SchedulingNodeAffinityOut"])
            ).optional(),
            "onHostMaintenance": t.string().optional(),
            "minNodeCpus": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeSchedulingOut"])
    types["AwsSecurityGroupIn"] = t.struct(
        {"id": t.string().optional(), "name": t.string().optional()}
    ).named(renames["AwsSecurityGroupIn"])
    types["AwsSecurityGroupOut"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsSecurityGroupOut"])
    types["StartMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartMigrationRequestIn"]
    )
    types["StartMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartMigrationRequestOut"])
    types["NetworkInterfaceIn"] = t.struct(
        {
            "externalIp": t.string().optional(),
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "internalIp": t.string().optional(),
        }
    ).named(renames["NetworkInterfaceIn"])
    types["NetworkInterfaceOut"] = t.struct(
        {
            "externalIp": t.string().optional(),
            "subnetwork": t.string().optional(),
            "network": t.string().optional(),
            "internalIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInterfaceOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListCloneJobsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListCloneJobsResponseIn"]
    )
    types["ListCloneJobsResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "cloneJobs": t.array(t.proxy(renames["CloneJobOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCloneJobsResponseOut"])
    types["CloneJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloneJobIn"]
    )
    types["CloneJobOut"] = t.struct(
        {
            "steps": t.array(t.proxy(renames["CloneStepOut"])).optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "stateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "computeEngineTargetDetails": t.proxy(
                renames["ComputeEngineTargetDetailsOut"]
            ).optional(),
        }
    ).named(renames["CloneJobOut"])
    types["ComputeEngineTargetDefaultsIn"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceIn"])
            ).optional(),
            "licenseType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "secureBoot": t.boolean().optional(),
            "targetProject": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "diskType": t.string().optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingIn"]).optional(),
            "machineTypeSeries": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "hostname": t.string().optional(),
            "machineType": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "vmName": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["ComputeEngineTargetDefaultsIn"])
    types["ComputeEngineTargetDefaultsOut"] = t.struct(
        {
            "serviceAccount": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceOut"])
            ).optional(),
            "licenseType": t.string().optional(),
            "appliedLicense": t.proxy(renames["AppliedLicenseOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "secureBoot": t.boolean().optional(),
            "targetProject": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "diskType": t.string().optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingOut"]).optional(),
            "machineTypeSeries": t.string().optional(),
            "bootOption": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "hostname": t.string().optional(),
            "machineType": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "vmName": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineTargetDefaultsOut"])
    types["FetchInventoryResponseIn"] = t.struct(
        {
            "vmwareVms": t.proxy(renames["VmwareVmsDetailsIn"]).optional(),
            "awsVms": t.proxy(renames["AwsVmsDetailsIn"]).optional(),
        }
    ).named(renames["FetchInventoryResponseIn"])
    types["FetchInventoryResponseOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "vmwareVms": t.proxy(renames["VmwareVmsDetailsOut"]).optional(),
            "awsVms": t.proxy(renames["AwsVmsDetailsOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchInventoryResponseOut"])
    types["ComputeEngineTargetDetailsIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "project": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "bootOption": t.string().optional(),
            "licenseType": t.string().optional(),
            "hostname": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceIn"])
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "zone": t.string().optional(),
            "secureBoot": t.boolean().optional(),
            "appliedLicense": t.proxy(renames["AppliedLicenseIn"]).optional(),
            "diskType": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "serviceAccount": t.string().optional(),
            "vmName": t.string().optional(),
            "machineType": t.string().optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingIn"]).optional(),
            "machineTypeSeries": t.string().optional(),
        }
    ).named(renames["ComputeEngineTargetDetailsIn"])
    types["ComputeEngineTargetDetailsOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "project": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "bootOption": t.string().optional(),
            "licenseType": t.string().optional(),
            "hostname": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceOut"])
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "zone": t.string().optional(),
            "secureBoot": t.boolean().optional(),
            "appliedLicense": t.proxy(renames["AppliedLicenseOut"]).optional(),
            "diskType": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "serviceAccount": t.string().optional(),
            "vmName": t.string().optional(),
            "machineType": t.string().optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingOut"]).optional(),
            "machineTypeSeries": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineTargetDetailsOut"])
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
    types["ApplianceVersionIn"] = t.struct(
        {
            "version": t.string().optional(),
            "uri": t.string().optional(),
            "critical": t.boolean().optional(),
            "releaseNotesUri": t.string().optional(),
        }
    ).named(renames["ApplianceVersionIn"])
    types["ApplianceVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "uri": t.string().optional(),
            "critical": t.boolean().optional(),
            "releaseNotesUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplianceVersionOut"])
    types["CycleStepIn"] = t.struct(
        {
            "replicating": t.proxy(renames["ReplicatingStepIn"]).optional(),
            "initializingReplication": t.proxy(
                renames["InitializingReplicationStepIn"]
            ).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "postProcessing": t.proxy(renames["PostProcessingStepIn"]).optional(),
        }
    ).named(renames["CycleStepIn"])
    types["CycleStepOut"] = t.struct(
        {
            "replicating": t.proxy(renames["ReplicatingStepOut"]).optional(),
            "initializingReplication": t.proxy(
                renames["InitializingReplicationStepOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "postProcessing": t.proxy(renames["PostProcessingStepOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CycleStepOut"])
    types["PreparingVMDisksStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PreparingVMDisksStepIn"]
    )
    types["PreparingVMDisksStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PreparingVMDisksStepOut"])
    types["GroupIn"] = t.struct(
        {"description": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
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
    types["InstantiatingMigratedVMStepIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InstantiatingMigratedVMStepIn"])
    types["InstantiatingMigratedVMStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InstantiatingMigratedVMStepOut"])
    types["VmwareSourceDetailsIn"] = t.struct(
        {
            "password": t.string().optional(),
            "username": t.string().optional(),
            "vcenterIp": t.string().optional(),
            "thumbprint": t.string().optional(),
            "resolvedVcenterHost": t.string().optional(),
        }
    ).named(renames["VmwareSourceDetailsIn"])
    types["VmwareSourceDetailsOut"] = t.struct(
        {
            "password": t.string().optional(),
            "username": t.string().optional(),
            "vcenterIp": t.string().optional(),
            "thumbprint": t.string().optional(),
            "resolvedVcenterHost": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareSourceDetailsOut"])

    functions = {}
    functions["projectsLocationsGet"] = vmmigration.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsGet"] = vmmigration.post(
        "v1/{group}:addGroupMigration",
        t.struct(
            {
                "group": t.string(),
                "migratingVm": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsPatch"] = vmmigration.post(
        "v1/{group}:addGroupMigration",
        t.struct(
            {
                "group": t.string(),
                "migratingVm": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsRemoveGroupMigration"] = vmmigration.post(
        "v1/{group}:addGroupMigration",
        t.struct(
            {
                "group": t.string(),
                "migratingVm": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsCreate"] = vmmigration.post(
        "v1/{group}:addGroupMigration",
        t.struct(
            {
                "group": t.string(),
                "migratingVm": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsDelete"] = vmmigration.post(
        "v1/{group}:addGroupMigration",
        t.struct(
            {
                "group": t.string(),
                "migratingVm": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsList"] = vmmigration.post(
        "v1/{group}:addGroupMigration",
        t.struct(
            {
                "group": t.string(),
                "migratingVm": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGroupsAddGroupMigration"] = vmmigration.post(
        "v1/{group}:addGroupMigration",
        t.struct(
            {
                "group": t.string(),
                "migratingVm": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsCreate"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "project": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "project": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "project": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "project": t.string().optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "requestId": t.string().optional(),
                "description": t.string().optional(),
                "project": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
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
    functions["projectsLocationsOperationsList"] = vmmigration.get(
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
    functions["projectsLocationsSourcesGet"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesFetchInventory"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesCreate"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesList"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDelete"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesPatch"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsDelete"] = vmmigration.post(
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "datacenterConnectorId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceAccount": t.string().optional(),
                "registrationId": t.string().optional(),
                "version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsList"] = vmmigration.post(
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "datacenterConnectorId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceAccount": t.string().optional(),
                "registrationId": t.string().optional(),
                "version": t.string().optional(),
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
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "datacenterConnectorId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceAccount": t.string().optional(),
                "registrationId": t.string().optional(),
                "version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsGet"] = vmmigration.post(
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "datacenterConnectorId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceAccount": t.string().optional(),
                "registrationId": t.string().optional(),
                "version": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsCreate"] = vmmigration.post(
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "datacenterConnectorId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "serviceAccount": t.string().optional(),
                "registrationId": t.string().optional(),
                "version": t.string().optional(),
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
        "v1/{parent}/migratingVms",
        t.struct(
            {
                "requestId": t.string().optional(),
                "migratingVmId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "sourceVmId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsStartMigration"] = vmmigration.post(
        "v1/{parent}/migratingVms",
        t.struct(
            {
                "requestId": t.string().optional(),
                "migratingVmId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "sourceVmId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsPatch"] = vmmigration.post(
        "v1/{parent}/migratingVms",
        t.struct(
            {
                "requestId": t.string().optional(),
                "migratingVmId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "sourceVmId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsPauseMigration"] = vmmigration.post(
        "v1/{parent}/migratingVms",
        t.struct(
            {
                "requestId": t.string().optional(),
                "migratingVmId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "sourceVmId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsResumeMigration"] = vmmigration.post(
        "v1/{parent}/migratingVms",
        t.struct(
            {
                "requestId": t.string().optional(),
                "migratingVmId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "sourceVmId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsList"] = vmmigration.post(
        "v1/{parent}/migratingVms",
        t.struct(
            {
                "requestId": t.string().optional(),
                "migratingVmId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "sourceVmId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsGet"] = vmmigration.post(
        "v1/{parent}/migratingVms",
        t.struct(
            {
                "requestId": t.string().optional(),
                "migratingVmId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "sourceVmId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsDelete"] = vmmigration.post(
        "v1/{parent}/migratingVms",
        t.struct(
            {
                "requestId": t.string().optional(),
                "migratingVmId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "sourceVmId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCreate"] = vmmigration.post(
        "v1/{parent}/migratingVms",
        t.struct(
            {
                "requestId": t.string().optional(),
                "migratingVmId": t.string(),
                "parent": t.string(),
                "description": t.string().optional(),
                "sourceVmId": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
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
                "requestId": t.string().optional(),
                "parent": t.string(),
                "cloneJobId": t.string(),
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
                "requestId": t.string().optional(),
                "parent": t.string(),
                "cloneJobId": t.string(),
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
                "requestId": t.string().optional(),
                "parent": t.string(),
                "cloneJobId": t.string(),
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
                "requestId": t.string().optional(),
                "parent": t.string(),
                "cloneJobId": t.string(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string(),
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "pageToken": t.string(),
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
                "parent": t.string(),
                "requestId": t.string().optional(),
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
                "parent": t.string(),
                "requestId": t.string().optional(),
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
                "parent": t.string(),
                "requestId": t.string().optional(),
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
                "parent": t.string(),
                "requestId": t.string().optional(),
                "cutoverJobId": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsDelete"] = vmmigration.post(
        "v1/{parent}/utilizationReports",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "utilizationReportId": t.string(),
                "timeFrame": t.string().optional(),
                "displayName": t.string().optional(),
                "vms": t.array(t.proxy(renames["VmUtilizationInfoIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsGet"] = vmmigration.post(
        "v1/{parent}/utilizationReports",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "utilizationReportId": t.string(),
                "timeFrame": t.string().optional(),
                "displayName": t.string().optional(),
                "vms": t.array(t.proxy(renames["VmUtilizationInfoIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsList"] = vmmigration.post(
        "v1/{parent}/utilizationReports",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "utilizationReportId": t.string(),
                "timeFrame": t.string().optional(),
                "displayName": t.string().optional(),
                "vms": t.array(t.proxy(renames["VmUtilizationInfoIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsCreate"] = vmmigration.post(
        "v1/{parent}/utilizationReports",
        t.struct(
            {
                "parent": t.string(),
                "requestId": t.string().optional(),
                "utilizationReportId": t.string(),
                "timeFrame": t.string().optional(),
                "displayName": t.string().optional(),
                "vms": t.array(t.proxy(renames["VmUtilizationInfoIn"])).optional(),
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
