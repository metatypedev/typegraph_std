from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_vmmigration() -> Import:
    vmmigration = HTTPRuntime("https://vmmigration.googleapis.com/")

    renames = {
        "ErrorResponse": "_vmmigration_1_ErrorResponse",
        "VmwareSourceDetailsIn": "_vmmigration_2_VmwareSourceDetailsIn",
        "VmwareSourceDetailsOut": "_vmmigration_3_VmwareSourceDetailsOut",
        "AddGroupMigrationRequestIn": "_vmmigration_4_AddGroupMigrationRequestIn",
        "AddGroupMigrationRequestOut": "_vmmigration_5_AddGroupMigrationRequestOut",
        "SourceIn": "_vmmigration_6_SourceIn",
        "SourceOut": "_vmmigration_7_SourceOut",
        "TagIn": "_vmmigration_8_TagIn",
        "TagOut": "_vmmigration_9_TagOut",
        "ListCloneJobsResponseIn": "_vmmigration_10_ListCloneJobsResponseIn",
        "ListCloneJobsResponseOut": "_vmmigration_11_ListCloneJobsResponseOut",
        "PauseMigrationRequestIn": "_vmmigration_12_PauseMigrationRequestIn",
        "PauseMigrationRequestOut": "_vmmigration_13_PauseMigrationRequestOut",
        "ShuttingDownSourceVMStepIn": "_vmmigration_14_ShuttingDownSourceVMStepIn",
        "ShuttingDownSourceVMStepOut": "_vmmigration_15_ShuttingDownSourceVMStepOut",
        "InitializingReplicationStepIn": "_vmmigration_16_InitializingReplicationStepIn",
        "InitializingReplicationStepOut": "_vmmigration_17_InitializingReplicationStepOut",
        "CutoverJobIn": "_vmmigration_18_CutoverJobIn",
        "CutoverJobOut": "_vmmigration_19_CutoverJobOut",
        "CancelCutoverJobRequestIn": "_vmmigration_20_CancelCutoverJobRequestIn",
        "CancelCutoverJobRequestOut": "_vmmigration_21_CancelCutoverJobRequestOut",
        "EmptyIn": "_vmmigration_22_EmptyIn",
        "EmptyOut": "_vmmigration_23_EmptyOut",
        "AwsSecurityGroupIn": "_vmmigration_24_AwsSecurityGroupIn",
        "AwsSecurityGroupOut": "_vmmigration_25_AwsSecurityGroupOut",
        "SchedulingNodeAffinityIn": "_vmmigration_26_SchedulingNodeAffinityIn",
        "SchedulingNodeAffinityOut": "_vmmigration_27_SchedulingNodeAffinityOut",
        "ResumeMigrationRequestIn": "_vmmigration_28_ResumeMigrationRequestIn",
        "ResumeMigrationRequestOut": "_vmmigration_29_ResumeMigrationRequestOut",
        "OperationMetadataIn": "_vmmigration_30_OperationMetadataIn",
        "OperationMetadataOut": "_vmmigration_31_OperationMetadataOut",
        "NetworkInterfaceIn": "_vmmigration_32_NetworkInterfaceIn",
        "NetworkInterfaceOut": "_vmmigration_33_NetworkInterfaceOut",
        "ListCutoverJobsResponseIn": "_vmmigration_34_ListCutoverJobsResponseIn",
        "ListCutoverJobsResponseOut": "_vmmigration_35_ListCutoverJobsResponseOut",
        "VmwareVmsDetailsIn": "_vmmigration_36_VmwareVmsDetailsIn",
        "VmwareVmsDetailsOut": "_vmmigration_37_VmwareVmsDetailsOut",
        "AwsSourceDetailsIn": "_vmmigration_38_AwsSourceDetailsIn",
        "AwsSourceDetailsOut": "_vmmigration_39_AwsSourceDetailsOut",
        "StartMigrationRequestIn": "_vmmigration_40_StartMigrationRequestIn",
        "StartMigrationRequestOut": "_vmmigration_41_StartMigrationRequestOut",
        "CloneStepIn": "_vmmigration_42_CloneStepIn",
        "CloneStepOut": "_vmmigration_43_CloneStepOut",
        "LocationIn": "_vmmigration_44_LocationIn",
        "LocationOut": "_vmmigration_45_LocationOut",
        "AvailableUpdatesIn": "_vmmigration_46_AvailableUpdatesIn",
        "AvailableUpdatesOut": "_vmmigration_47_AvailableUpdatesOut",
        "MigrationWarningIn": "_vmmigration_48_MigrationWarningIn",
        "MigrationWarningOut": "_vmmigration_49_MigrationWarningOut",
        "ReplicatingStepIn": "_vmmigration_50_ReplicatingStepIn",
        "ReplicatingStepOut": "_vmmigration_51_ReplicatingStepOut",
        "AccessKeyCredentialsIn": "_vmmigration_52_AccessKeyCredentialsIn",
        "AccessKeyCredentialsOut": "_vmmigration_53_AccessKeyCredentialsOut",
        "ReplicationCycleIn": "_vmmigration_54_ReplicationCycleIn",
        "ReplicationCycleOut": "_vmmigration_55_ReplicationCycleOut",
        "VmwareVmDetailsIn": "_vmmigration_56_VmwareVmDetailsIn",
        "VmwareVmDetailsOut": "_vmmigration_57_VmwareVmDetailsOut",
        "ComputeEngineTargetDefaultsIn": "_vmmigration_58_ComputeEngineTargetDefaultsIn",
        "ComputeEngineTargetDefaultsOut": "_vmmigration_59_ComputeEngineTargetDefaultsOut",
        "PostProcessingStepIn": "_vmmigration_60_PostProcessingStepIn",
        "PostProcessingStepOut": "_vmmigration_61_PostProcessingStepOut",
        "FinalizeMigrationRequestIn": "_vmmigration_62_FinalizeMigrationRequestIn",
        "FinalizeMigrationRequestOut": "_vmmigration_63_FinalizeMigrationRequestOut",
        "ListDatacenterConnectorsResponseIn": "_vmmigration_64_ListDatacenterConnectorsResponseIn",
        "ListDatacenterConnectorsResponseOut": "_vmmigration_65_ListDatacenterConnectorsResponseOut",
        "ListSourcesResponseIn": "_vmmigration_66_ListSourcesResponseIn",
        "ListSourcesResponseOut": "_vmmigration_67_ListSourcesResponseOut",
        "TargetProjectIn": "_vmmigration_68_TargetProjectIn",
        "TargetProjectOut": "_vmmigration_69_TargetProjectOut",
        "ComputeSchedulingIn": "_vmmigration_70_ComputeSchedulingIn",
        "ComputeSchedulingOut": "_vmmigration_71_ComputeSchedulingOut",
        "ListTargetProjectsResponseIn": "_vmmigration_72_ListTargetProjectsResponseIn",
        "ListTargetProjectsResponseOut": "_vmmigration_73_ListTargetProjectsResponseOut",
        "CloneJobIn": "_vmmigration_74_CloneJobIn",
        "CloneJobOut": "_vmmigration_75_CloneJobOut",
        "OperationIn": "_vmmigration_76_OperationIn",
        "OperationOut": "_vmmigration_77_OperationOut",
        "LocalizedMessageIn": "_vmmigration_78_LocalizedMessageIn",
        "LocalizedMessageOut": "_vmmigration_79_LocalizedMessageOut",
        "CancelCloneJobRequestIn": "_vmmigration_80_CancelCloneJobRequestIn",
        "CancelCloneJobRequestOut": "_vmmigration_81_CancelCloneJobRequestOut",
        "RemoveGroupMigrationRequestIn": "_vmmigration_82_RemoveGroupMigrationRequestIn",
        "RemoveGroupMigrationRequestOut": "_vmmigration_83_RemoveGroupMigrationRequestOut",
        "GroupIn": "_vmmigration_84_GroupIn",
        "GroupOut": "_vmmigration_85_GroupOut",
        "UpgradeApplianceRequestIn": "_vmmigration_86_UpgradeApplianceRequestIn",
        "UpgradeApplianceRequestOut": "_vmmigration_87_UpgradeApplianceRequestOut",
        "UpgradeStatusIn": "_vmmigration_88_UpgradeStatusIn",
        "UpgradeStatusOut": "_vmmigration_89_UpgradeStatusOut",
        "ListLocationsResponseIn": "_vmmigration_90_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_vmmigration_91_ListLocationsResponseOut",
        "DatacenterConnectorIn": "_vmmigration_92_DatacenterConnectorIn",
        "DatacenterConnectorOut": "_vmmigration_93_DatacenterConnectorOut",
        "MigratingVmIn": "_vmmigration_94_MigratingVmIn",
        "MigratingVmOut": "_vmmigration_95_MigratingVmOut",
        "ComputeEngineTargetDetailsIn": "_vmmigration_96_ComputeEngineTargetDetailsIn",
        "ComputeEngineTargetDetailsOut": "_vmmigration_97_ComputeEngineTargetDetailsOut",
        "ListOperationsResponseIn": "_vmmigration_98_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_vmmigration_99_ListOperationsResponseOut",
        "CutoverStepIn": "_vmmigration_100_CutoverStepIn",
        "CutoverStepOut": "_vmmigration_101_CutoverStepOut",
        "FetchInventoryResponseIn": "_vmmigration_102_FetchInventoryResponseIn",
        "FetchInventoryResponseOut": "_vmmigration_103_FetchInventoryResponseOut",
        "ListReplicationCyclesResponseIn": "_vmmigration_104_ListReplicationCyclesResponseIn",
        "ListReplicationCyclesResponseOut": "_vmmigration_105_ListReplicationCyclesResponseOut",
        "CancelOperationRequestIn": "_vmmigration_106_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_vmmigration_107_CancelOperationRequestOut",
        "ListUtilizationReportsResponseIn": "_vmmigration_108_ListUtilizationReportsResponseIn",
        "ListUtilizationReportsResponseOut": "_vmmigration_109_ListUtilizationReportsResponseOut",
        "AdaptingOSStepIn": "_vmmigration_110_AdaptingOSStepIn",
        "AdaptingOSStepOut": "_vmmigration_111_AdaptingOSStepOut",
        "MigrationErrorIn": "_vmmigration_112_MigrationErrorIn",
        "MigrationErrorOut": "_vmmigration_113_MigrationErrorOut",
        "ApplianceVersionIn": "_vmmigration_114_ApplianceVersionIn",
        "ApplianceVersionOut": "_vmmigration_115_ApplianceVersionOut",
        "AwsVmsDetailsIn": "_vmmigration_116_AwsVmsDetailsIn",
        "AwsVmsDetailsOut": "_vmmigration_117_AwsVmsDetailsOut",
        "ListGroupsResponseIn": "_vmmigration_118_ListGroupsResponseIn",
        "ListGroupsResponseOut": "_vmmigration_119_ListGroupsResponseOut",
        "CycleStepIn": "_vmmigration_120_CycleStepIn",
        "CycleStepOut": "_vmmigration_121_CycleStepOut",
        "ListMigratingVmsResponseIn": "_vmmigration_122_ListMigratingVmsResponseIn",
        "ListMigratingVmsResponseOut": "_vmmigration_123_ListMigratingVmsResponseOut",
        "StatusIn": "_vmmigration_124_StatusIn",
        "StatusOut": "_vmmigration_125_StatusOut",
        "AppliedLicenseIn": "_vmmigration_126_AppliedLicenseIn",
        "AppliedLicenseOut": "_vmmigration_127_AppliedLicenseOut",
        "LinkIn": "_vmmigration_128_LinkIn",
        "LinkOut": "_vmmigration_129_LinkOut",
        "InstantiatingMigratedVMStepIn": "_vmmigration_130_InstantiatingMigratedVMStepIn",
        "InstantiatingMigratedVMStepOut": "_vmmigration_131_InstantiatingMigratedVMStepOut",
        "CutoverForecastIn": "_vmmigration_132_CutoverForecastIn",
        "CutoverForecastOut": "_vmmigration_133_CutoverForecastOut",
        "PreparingVMDisksStepIn": "_vmmigration_134_PreparingVMDisksStepIn",
        "PreparingVMDisksStepOut": "_vmmigration_135_PreparingVMDisksStepOut",
        "AwsSourceVmDetailsIn": "_vmmigration_136_AwsSourceVmDetailsIn",
        "AwsSourceVmDetailsOut": "_vmmigration_137_AwsSourceVmDetailsOut",
        "UtilizationReportIn": "_vmmigration_138_UtilizationReportIn",
        "UtilizationReportOut": "_vmmigration_139_UtilizationReportOut",
        "ReplicationSyncIn": "_vmmigration_140_ReplicationSyncIn",
        "ReplicationSyncOut": "_vmmigration_141_ReplicationSyncOut",
        "VmUtilizationMetricsIn": "_vmmigration_142_VmUtilizationMetricsIn",
        "VmUtilizationMetricsOut": "_vmmigration_143_VmUtilizationMetricsOut",
        "SchedulePolicyIn": "_vmmigration_144_SchedulePolicyIn",
        "SchedulePolicyOut": "_vmmigration_145_SchedulePolicyOut",
        "VmUtilizationInfoIn": "_vmmigration_146_VmUtilizationInfoIn",
        "VmUtilizationInfoOut": "_vmmigration_147_VmUtilizationInfoOut",
        "AwsVmDetailsIn": "_vmmigration_148_AwsVmDetailsIn",
        "AwsVmDetailsOut": "_vmmigration_149_AwsVmDetailsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AddGroupMigrationRequestIn"] = t.struct(
        {"migratingVm": t.string().optional()}
    ).named(renames["AddGroupMigrationRequestIn"])
    types["AddGroupMigrationRequestOut"] = t.struct(
        {
            "migratingVm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddGroupMigrationRequestOut"])
    types["SourceIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
            "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
        }
    ).named(renames["SourceIn"])
    types["SourceOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "vmware": t.proxy(renames["VmwareSourceDetailsOut"]).optional(),
            "aws": t.proxy(renames["AwsSourceDetailsOut"]).optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SourceOut"])
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
    types["ListCloneJobsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListCloneJobsResponseIn"]
    )
    types["ListCloneJobsResponseOut"] = t.struct(
        {
            "cloneJobs": t.array(t.proxy(renames["CloneJobOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCloneJobsResponseOut"])
    types["PauseMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PauseMigrationRequestIn"]
    )
    types["PauseMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PauseMigrationRequestOut"])
    types["ShuttingDownSourceVMStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ShuttingDownSourceVMStepIn"]
    )
    types["ShuttingDownSourceVMStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ShuttingDownSourceVMStepOut"])
    types["InitializingReplicationStepIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InitializingReplicationStepIn"])
    types["InitializingReplicationStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InitializingReplicationStepOut"])
    types["CutoverJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CutoverJobIn"]
    )
    types["CutoverJobOut"] = t.struct(
        {
            "stateTime": t.string().optional(),
            "computeEngineTargetDetails": t.proxy(
                renames["ComputeEngineTargetDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "steps": t.array(t.proxy(renames["CutoverStepOut"])).optional(),
            "stateMessage": t.string().optional(),
        }
    ).named(renames["CutoverJobOut"])
    types["CancelCutoverJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelCutoverJobRequestIn"]
    )
    types["CancelCutoverJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelCutoverJobRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ResumeMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResumeMigrationRequestIn"]
    )
    types["ResumeMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResumeMigrationRequestOut"])
    types["OperationMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["OperationMetadataIn"]
    )
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["NetworkInterfaceIn"] = t.struct(
        {
            "externalIp": t.string().optional(),
            "internalIp": t.string().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
        }
    ).named(renames["NetworkInterfaceIn"])
    types["NetworkInterfaceOut"] = t.struct(
        {
            "externalIp": t.string().optional(),
            "internalIp": t.string().optional(),
            "network": t.string().optional(),
            "subnetwork": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkInterfaceOut"])
    types["ListCutoverJobsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListCutoverJobsResponseIn"]
    )
    types["ListCutoverJobsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cutoverJobs": t.array(t.proxy(renames["CutoverJobOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListCutoverJobsResponseOut"])
    types["VmwareVmsDetailsIn"] = t.struct(
        {"details": t.array(t.proxy(renames["VmwareVmDetailsIn"])).optional()}
    ).named(renames["VmwareVmsDetailsIn"])
    types["VmwareVmsDetailsOut"] = t.struct(
        {
            "details": t.array(t.proxy(renames["VmwareVmDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVmsDetailsOut"])
    types["AwsSourceDetailsIn"] = t.struct(
        {
            "migrationResourcesUserTags": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "accessKeyCreds": t.proxy(renames["AccessKeyCredentialsIn"]).optional(),
            "awsRegion": t.string().optional(),
            "inventoryTagList": t.array(t.proxy(renames["TagIn"])).optional(),
            "inventorySecurityGroupNames": t.array(t.string()).optional(),
        }
    ).named(renames["AwsSourceDetailsIn"])
    types["AwsSourceDetailsOut"] = t.struct(
        {
            "migrationResourcesUserTags": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "publicIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "accessKeyCreds": t.proxy(renames["AccessKeyCredentialsOut"]).optional(),
            "awsRegion": t.string().optional(),
            "inventoryTagList": t.array(t.proxy(renames["TagOut"])).optional(),
            "state": t.string().optional(),
            "inventorySecurityGroupNames": t.array(t.string()).optional(),
        }
    ).named(renames["AwsSourceDetailsOut"])
    types["StartMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartMigrationRequestIn"]
    )
    types["StartMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartMigrationRequestOut"])
    types["CloneStepIn"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepIn"]).optional(),
            "adaptingOs": t.proxy(renames["AdaptingOSStepIn"]).optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepIn"]
            ).optional(),
        }
    ).named(renames["CloneStepIn"])
    types["CloneStepOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "endTime": t.string().optional(),
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepOut"]).optional(),
            "adaptingOs": t.proxy(renames["AdaptingOSStepOut"]).optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloneStepOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    types["MigrationWarningIn"] = t.struct(
        {
            "actionItem": t.proxy(renames["LocalizedMessageIn"]).optional(),
            "warningTime": t.string().optional(),
            "warningMessage": t.proxy(renames["LocalizedMessageIn"]).optional(),
            "code": t.string().optional(),
            "helpLinks": t.array(t.proxy(renames["LinkIn"])).optional(),
        }
    ).named(renames["MigrationWarningIn"])
    types["MigrationWarningOut"] = t.struct(
        {
            "actionItem": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "warningTime": t.string().optional(),
            "warningMessage": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "code": t.string().optional(),
            "helpLinks": t.array(t.proxy(renames["LinkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationWarningOut"])
    types["ReplicatingStepIn"] = t.struct(
        {
            "replicatedBytes": t.string().optional(),
            "totalBytes": t.string().optional(),
            "lastThirtyMinutesAverageBytesPerSecond": t.string().optional(),
            "lastTwoMinutesAverageBytesPerSecond": t.string().optional(),
        }
    ).named(renames["ReplicatingStepIn"])
    types["ReplicatingStepOut"] = t.struct(
        {
            "replicatedBytes": t.string().optional(),
            "totalBytes": t.string().optional(),
            "lastThirtyMinutesAverageBytesPerSecond": t.string().optional(),
            "lastTwoMinutesAverageBytesPerSecond": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicatingStepOut"])
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
    types["ReplicationCycleIn"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "cycleNumber": t.integer().optional(),
            "name": t.string().optional(),
            "totalPauseDuration": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "steps": t.array(t.proxy(renames["CycleStepIn"])).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["ReplicationCycleIn"])
    types["ReplicationCycleOut"] = t.struct(
        {
            "state": t.string().optional(),
            "endTime": t.string().optional(),
            "startTime": t.string().optional(),
            "cycleNumber": t.integer().optional(),
            "name": t.string().optional(),
            "totalPauseDuration": t.string().optional(),
            "progressPercent": t.integer().optional(),
            "warnings": t.array(t.proxy(renames["MigrationWarningOut"])).optional(),
            "steps": t.array(t.proxy(renames["CycleStepOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicationCycleOut"])
    types["VmwareVmDetailsIn"] = t.struct(
        {
            "committedStorageMb": t.string().optional(),
            "diskCount": t.integer().optional(),
            "datacenterId": t.string().optional(),
            "powerState": t.string().optional(),
            "uuid": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "vmId": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "guestDescription": t.string().optional(),
            "datacenterDescription": t.string().optional(),
        }
    ).named(renames["VmwareVmDetailsIn"])
    types["VmwareVmDetailsOut"] = t.struct(
        {
            "committedStorageMb": t.string().optional(),
            "diskCount": t.integer().optional(),
            "datacenterId": t.string().optional(),
            "powerState": t.string().optional(),
            "uuid": t.string().optional(),
            "memoryMb": t.integer().optional(),
            "bootOption": t.string().optional(),
            "vmId": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "displayName": t.string().optional(),
            "guestDescription": t.string().optional(),
            "datacenterDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmwareVmDetailsOut"])
    types["ComputeEngineTargetDefaultsIn"] = t.struct(
        {
            "machineTypeSeries": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceIn"])
            ).optional(),
            "licenseType": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "targetProject": t.string().optional(),
            "secureBoot": t.boolean().optional(),
            "vmName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingIn"]).optional(),
            "diskType": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "hostname": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["ComputeEngineTargetDefaultsIn"])
    types["ComputeEngineTargetDefaultsOut"] = t.struct(
        {
            "machineTypeSeries": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceOut"])
            ).optional(),
            "licenseType": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "targetProject": t.string().optional(),
            "secureBoot": t.boolean().optional(),
            "vmName": t.string().optional(),
            "appliedLicense": t.proxy(renames["AppliedLicenseOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingOut"]).optional(),
            "bootOption": t.string().optional(),
            "diskType": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "hostname": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineTargetDefaultsOut"])
    types["PostProcessingStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PostProcessingStepIn"]
    )
    types["PostProcessingStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PostProcessingStepOut"])
    types["FinalizeMigrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["FinalizeMigrationRequestIn"]
    )
    types["FinalizeMigrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["FinalizeMigrationRequestOut"])
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
    types["ListSourcesResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListSourcesResponseIn"]
    )
    types["ListSourcesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "sources": t.array(t.proxy(renames["SourceOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSourcesResponseOut"])
    types["TargetProjectIn"] = t.struct(
        {"description": t.string().optional(), "project": t.string().optional()}
    ).named(renames["TargetProjectIn"])
    types["TargetProjectOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TargetProjectOut"])
    types["ComputeSchedulingIn"] = t.struct(
        {
            "minNodeCpus": t.integer().optional(),
            "restartType": t.string().optional(),
            "nodeAffinities": t.array(
                t.proxy(renames["SchedulingNodeAffinityIn"])
            ).optional(),
            "onHostMaintenance": t.string().optional(),
        }
    ).named(renames["ComputeSchedulingIn"])
    types["ComputeSchedulingOut"] = t.struct(
        {
            "minNodeCpus": t.integer().optional(),
            "restartType": t.string().optional(),
            "nodeAffinities": t.array(
                t.proxy(renames["SchedulingNodeAffinityOut"])
            ).optional(),
            "onHostMaintenance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeSchedulingOut"])
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
    types["CloneJobIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CloneJobIn"]
    )
    types["CloneJobOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "steps": t.array(t.proxy(renames["CloneStepOut"])).optional(),
            "createTime": t.string().optional(),
            "computeEngineTargetDetails": t.proxy(
                renames["ComputeEngineTargetDetailsOut"]
            ).optional(),
            "name": t.string().optional(),
            "stateTime": t.string().optional(),
            "state": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["CloneJobOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
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
    types["CancelCloneJobRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelCloneJobRequestIn"]
    )
    types["CancelCloneJobRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelCloneJobRequestOut"])
    types["RemoveGroupMigrationRequestIn"] = t.struct(
        {"migratingVm": t.string().optional()}
    ).named(renames["RemoveGroupMigrationRequestIn"])
    types["RemoveGroupMigrationRequestOut"] = t.struct(
        {
            "migratingVm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RemoveGroupMigrationRequestOut"])
    types["GroupIn"] = t.struct(
        {"description": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["GroupIn"])
    types["GroupOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GroupOut"])
    types["UpgradeApplianceRequestIn"] = t.struct(
        {"requestId": t.string().optional()}
    ).named(renames["UpgradeApplianceRequestIn"])
    types["UpgradeApplianceRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpgradeApplianceRequestOut"])
    types["UpgradeStatusIn"] = t.struct(
        {
            "version": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "previousVersion": t.string().optional(),
        }
    ).named(renames["UpgradeStatusIn"])
    types["UpgradeStatusOut"] = t.struct(
        {
            "version": t.string().optional(),
            "state": t.string().optional(),
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "previousVersion": t.string().optional(),
        }
    ).named(renames["UpgradeStatusOut"])
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
            "serviceAccount": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["DatacenterConnectorIn"])
    types["DatacenterConnectorOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "registrationId": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "upgradeStatus": t.proxy(renames["UpgradeStatusOut"]).optional(),
            "stateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "bucket": t.string().optional(),
            "serviceAccount": t.string().optional(),
            "availableVersions": t.proxy(renames["AvailableUpdatesOut"]).optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "applianceInfrastructureVersion": t.string().optional(),
            "applianceSoftwareVersion": t.string().optional(),
        }
    ).named(renames["DatacenterConnectorOut"])
    types["MigratingVmIn"] = t.struct(
        {
            "description": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
            "computeEngineTargetDefaults": t.proxy(
                renames["ComputeEngineTargetDefaultsIn"]
            ).optional(),
            "sourceVmId": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["MigratingVmIn"])
    types["MigratingVmOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "stateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "awsSourceVmDetails": t.proxy(renames["AwsSourceVmDetailsOut"]).optional(),
            "state": t.string().optional(),
            "group": t.string().optional(),
            "lastReplicationCycle": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "description": t.string().optional(),
            "recentCloneJobs": t.array(t.proxy(renames["CloneJobOut"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "policy": t.proxy(renames["SchedulePolicyOut"]).optional(),
            "currentSyncInfo": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "updateTime": t.string().optional(),
            "computeEngineTargetDefaults": t.proxy(
                renames["ComputeEngineTargetDefaultsOut"]
            ).optional(),
            "name": t.string().optional(),
            "sourceVmId": t.string().optional(),
            "cutoverForecast": t.proxy(renames["CutoverForecastOut"]).optional(),
            "lastSync": t.proxy(renames["ReplicationSyncOut"]).optional(),
            "displayName": t.string().optional(),
            "recentCutoverJobs": t.array(t.proxy(renames["CutoverJobOut"])).optional(),
        }
    ).named(renames["MigratingVmOut"])
    types["ComputeEngineTargetDetailsIn"] = t.struct(
        {
            "appliedLicense": t.proxy(renames["AppliedLicenseIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "bootOption": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceIn"])
            ).optional(),
            "secureBoot": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "diskType": t.string().optional(),
            "hostname": t.string().optional(),
            "vmName": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingIn"]).optional(),
            "zone": t.string().optional(),
            "machineTypeSeries": t.string().optional(),
            "project": t.string().optional(),
            "licenseType": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
        }
    ).named(renames["ComputeEngineTargetDetailsIn"])
    types["ComputeEngineTargetDetailsOut"] = t.struct(
        {
            "appliedLicense": t.proxy(renames["AppliedLicenseOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccount": t.string().optional(),
            "bootOption": t.string().optional(),
            "networkInterfaces": t.array(
                t.proxy(renames["NetworkInterfaceOut"])
            ).optional(),
            "secureBoot": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "diskType": t.string().optional(),
            "hostname": t.string().optional(),
            "vmName": t.string().optional(),
            "networkTags": t.array(t.string()).optional(),
            "computeScheduling": t.proxy(renames["ComputeSchedulingOut"]).optional(),
            "zone": t.string().optional(),
            "machineTypeSeries": t.string().optional(),
            "project": t.string().optional(),
            "licenseType": t.string().optional(),
            "additionalLicenses": t.array(t.string()).optional(),
            "machineType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComputeEngineTargetDetailsOut"])
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
    types["CutoverStepIn"] = t.struct(
        {
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepIn"]).optional(),
            "previousReplicationCycle": t.proxy(
                renames["ReplicationCycleIn"]
            ).optional(),
            "shuttingDownSourceVm": t.proxy(
                renames["ShuttingDownSourceVMStepIn"]
            ).optional(),
            "endTime": t.string().optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepIn"]
            ).optional(),
            "startTime": t.string().optional(),
            "finalSync": t.proxy(renames["ReplicationCycleIn"]).optional(),
        }
    ).named(renames["CutoverStepIn"])
    types["CutoverStepOut"] = t.struct(
        {
            "preparingVmDisks": t.proxy(renames["PreparingVMDisksStepOut"]).optional(),
            "previousReplicationCycle": t.proxy(
                renames["ReplicationCycleOut"]
            ).optional(),
            "shuttingDownSourceVm": t.proxy(
                renames["ShuttingDownSourceVMStepOut"]
            ).optional(),
            "endTime": t.string().optional(),
            "instantiatingMigratedVm": t.proxy(
                renames["InstantiatingMigratedVMStepOut"]
            ).optional(),
            "startTime": t.string().optional(),
            "finalSync": t.proxy(renames["ReplicationCycleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoverStepOut"])
    types["FetchInventoryResponseIn"] = t.struct(
        {
            "awsVms": t.proxy(renames["AwsVmsDetailsIn"]).optional(),
            "vmwareVms": t.proxy(renames["VmwareVmsDetailsIn"]).optional(),
        }
    ).named(renames["FetchInventoryResponseIn"])
    types["FetchInventoryResponseOut"] = t.struct(
        {
            "awsVms": t.proxy(renames["AwsVmsDetailsOut"]).optional(),
            "updateTime": t.string().optional(),
            "vmwareVms": t.proxy(renames["VmwareVmsDetailsOut"]).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchInventoryResponseOut"])
    types["ListReplicationCyclesResponseIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ListReplicationCyclesResponseIn"])
    types["ListReplicationCyclesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "replicationCycles": t.array(
                t.proxy(renames["ReplicationCycleOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListReplicationCyclesResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
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
    types["AdaptingOSStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AdaptingOSStepIn"]
    )
    types["AdaptingOSStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AdaptingOSStepOut"])
    types["MigrationErrorIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MigrationErrorIn"]
    )
    types["MigrationErrorOut"] = t.struct(
        {
            "actionItem": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "code": t.string().optional(),
            "errorMessage": t.proxy(renames["LocalizedMessageOut"]).optional(),
            "helpLinks": t.array(t.proxy(renames["LinkOut"])).optional(),
            "errorTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MigrationErrorOut"])
    types["ApplianceVersionIn"] = t.struct(
        {
            "version": t.string().optional(),
            "critical": t.boolean().optional(),
            "releaseNotesUri": t.string().optional(),
            "uri": t.string().optional(),
        }
    ).named(renames["ApplianceVersionIn"])
    types["ApplianceVersionOut"] = t.struct(
        {
            "version": t.string().optional(),
            "critical": t.boolean().optional(),
            "releaseNotesUri": t.string().optional(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApplianceVersionOut"])
    types["AwsVmsDetailsIn"] = t.struct(
        {"details": t.array(t.proxy(renames["AwsVmDetailsIn"])).optional()}
    ).named(renames["AwsVmsDetailsIn"])
    types["AwsVmsDetailsOut"] = t.struct(
        {
            "details": t.array(t.proxy(renames["AwsVmDetailsOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsVmsDetailsOut"])
    types["ListGroupsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListGroupsResponseIn"]
    )
    types["ListGroupsResponseOut"] = t.struct(
        {
            "groups": t.array(t.proxy(renames["GroupOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGroupsResponseOut"])
    types["CycleStepIn"] = t.struct(
        {
            "replicating": t.proxy(renames["ReplicatingStepIn"]).optional(),
            "startTime": t.string().optional(),
            "postProcessing": t.proxy(renames["PostProcessingStepIn"]).optional(),
            "endTime": t.string().optional(),
            "initializingReplication": t.proxy(
                renames["InitializingReplicationStepIn"]
            ).optional(),
        }
    ).named(renames["CycleStepIn"])
    types["CycleStepOut"] = t.struct(
        {
            "replicating": t.proxy(renames["ReplicatingStepOut"]).optional(),
            "startTime": t.string().optional(),
            "postProcessing": t.proxy(renames["PostProcessingStepOut"]).optional(),
            "endTime": t.string().optional(),
            "initializingReplication": t.proxy(
                renames["InitializingReplicationStepOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CycleStepOut"])
    types["ListMigratingVmsResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ListMigratingVmsResponseIn"]
    )
    types["ListMigratingVmsResponseOut"] = t.struct(
        {
            "migratingVms": t.array(t.proxy(renames["MigratingVmOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMigratingVmsResponseOut"])
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
    types["InstantiatingMigratedVMStepIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["InstantiatingMigratedVMStepIn"])
    types["InstantiatingMigratedVMStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["InstantiatingMigratedVMStepOut"])
    types["CutoverForecastIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CutoverForecastIn"]
    )
    types["CutoverForecastOut"] = t.struct(
        {
            "estimatedCutoverJobDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CutoverForecastOut"])
    types["PreparingVMDisksStepIn"] = t.struct({"_": t.string().optional()}).named(
        renames["PreparingVMDisksStepIn"]
    )
    types["PreparingVMDisksStepOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["PreparingVMDisksStepOut"])
    types["AwsSourceVmDetailsIn"] = t.struct(
        {
            "committedStorageBytes": t.string().optional(),
            "firmware": t.string().optional(),
        }
    ).named(renames["AwsSourceVmDetailsIn"])
    types["AwsSourceVmDetailsOut"] = t.struct(
        {
            "committedStorageBytes": t.string().optional(),
            "firmware": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsSourceVmDetailsOut"])
    types["UtilizationReportIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "vms": t.array(t.proxy(renames["VmUtilizationInfoIn"])).optional(),
            "timeFrame": t.string().optional(),
        }
    ).named(renames["UtilizationReportIn"])
    types["UtilizationReportOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "vms": t.array(t.proxy(renames["VmUtilizationInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "vmCount": t.integer().optional(),
            "timeFrame": t.string().optional(),
            "stateTime": t.string().optional(),
            "name": t.string().optional(),
            "frameEndTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(renames["UtilizationReportOut"])
    types["ReplicationSyncIn"] = t.struct(
        {"lastSyncTime": t.string().optional()}
    ).named(renames["ReplicationSyncIn"])
    types["ReplicationSyncOut"] = t.struct(
        {
            "lastSyncTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplicationSyncOut"])
    types["VmUtilizationMetricsIn"] = t.struct(
        {
            "diskIoRateAverageKbps": t.string().optional(),
            "cpuMaxPercent": t.integer().optional(),
            "networkThroughputMaxKbps": t.string().optional(),
            "memoryAveragePercent": t.integer().optional(),
            "networkThroughputAverageKbps": t.string().optional(),
            "diskIoRateMaxKbps": t.string().optional(),
            "memoryMaxPercent": t.integer().optional(),
            "cpuAveragePercent": t.integer().optional(),
        }
    ).named(renames["VmUtilizationMetricsIn"])
    types["VmUtilizationMetricsOut"] = t.struct(
        {
            "diskIoRateAverageKbps": t.string().optional(),
            "cpuMaxPercent": t.integer().optional(),
            "networkThroughputMaxKbps": t.string().optional(),
            "memoryAveragePercent": t.integer().optional(),
            "networkThroughputAverageKbps": t.string().optional(),
            "diskIoRateMaxKbps": t.string().optional(),
            "memoryMaxPercent": t.integer().optional(),
            "cpuAveragePercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VmUtilizationMetricsOut"])
    types["SchedulePolicyIn"] = t.struct(
        {
            "idleDuration": t.string().optional(),
            "skipOsAdaptation": t.boolean().optional(),
        }
    ).named(renames["SchedulePolicyIn"])
    types["SchedulePolicyOut"] = t.struct(
        {
            "idleDuration": t.string().optional(),
            "skipOsAdaptation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SchedulePolicyOut"])
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
    types["AwsVmDetailsIn"] = t.struct(
        {
            "diskCount": t.integer().optional(),
            "securityGroups": t.array(
                t.proxy(renames["AwsSecurityGroupIn"])
            ).optional(),
            "memoryMb": t.integer().optional(),
            "sourceId": t.string().optional(),
            "tags": t.struct({"_": t.string().optional()}).optional(),
            "committedStorageMb": t.string().optional(),
            "vmId": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceDescription": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "zone": t.string().optional(),
            "bootOption": t.string().optional(),
            "architecture": t.string().optional(),
            "vpcId": t.string().optional(),
            "instanceType": t.string().optional(),
            "virtualizationType": t.string().optional(),
            "osDescription": t.string().optional(),
        }
    ).named(renames["AwsVmDetailsIn"])
    types["AwsVmDetailsOut"] = t.struct(
        {
            "powerState": t.string().optional(),
            "diskCount": t.integer().optional(),
            "securityGroups": t.array(
                t.proxy(renames["AwsSecurityGroupOut"])
            ).optional(),
            "memoryMb": t.integer().optional(),
            "sourceId": t.string().optional(),
            "tags": t.struct({"_": t.string().optional()}).optional(),
            "committedStorageMb": t.string().optional(),
            "vmId": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceDescription": t.string().optional(),
            "cpuCount": t.integer().optional(),
            "zone": t.string().optional(),
            "bootOption": t.string().optional(),
            "architecture": t.string().optional(),
            "vpcId": t.string().optional(),
            "instanceType": t.string().optional(),
            "virtualizationType": t.string().optional(),
            "osDescription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AwsVmDetailsOut"])

    functions = {}
    functions["projectsLocationsGet"] = vmmigration.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsCreate"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsDelete"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsPatch"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsList"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsTargetProjectsGet"] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TargetProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = vmmigration.post(
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
    functions["projectsLocationsOperationsGet"] = vmmigration.post(
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
    functions["projectsLocationsOperationsList"] = vmmigration.post(
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
    functions["projectsLocationsOperationsCancel"] = vmmigration.post(
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
    functions["projectsLocationsSourcesFetchInventory"] = vmmigration.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "sourceId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesGet"] = vmmigration.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "sourceId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesPatch"] = vmmigration.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "sourceId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesList"] = vmmigration.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "sourceId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDelete"] = vmmigration.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "sourceId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesCreate"] = vmmigration.post(
        "v1/{parent}/sources",
        t.struct(
            {
                "sourceId": t.string(),
                "requestId": t.string().optional(),
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "description": t.string().optional(),
                "vmware": t.proxy(renames["VmwareSourceDetailsIn"]).optional(),
                "aws": t.proxy(renames["AwsSourceDetailsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsDelete"] = vmmigration.get(
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatacenterConnectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsGet"] = vmmigration.get(
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatacenterConnectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsCreate"] = vmmigration.get(
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatacenterConnectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesDatacenterConnectorsUpgradeAppliance"
    ] = vmmigration.get(
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatacenterConnectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesDatacenterConnectorsList"] = vmmigration.get(
        "v1/{parent}/datacenterConnectors",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListDatacenterConnectorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsGet"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "sourceVmId": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsDelete"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "sourceVmId": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsStartMigration"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "sourceVmId": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesMigratingVmsResumeMigration"
    ] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "sourceVmId": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsList"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "sourceVmId": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsPauseMigration"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "sourceVmId": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesMigratingVmsFinalizeMigration"
    ] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "sourceVmId": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCreate"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "sourceVmId": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsPatch"] = vmmigration.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "description": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "policy": t.proxy(renames["SchedulePolicyIn"]).optional(),
                "computeEngineTargetDefaults": t.proxy(
                    renames["ComputeEngineTargetDefaultsIn"]
                ).optional(),
                "sourceVmId": t.string().optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["projectsLocationsSourcesMigratingVmsCloneJobsGet"] = vmmigration.get(
        "v1/{parent}/cloneJobs",
        t.struct(
            {
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCloneJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCloneJobsCancel"] = vmmigration.get(
        "v1/{parent}/cloneJobs",
        t.struct(
            {
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCloneJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCloneJobsCreate"] = vmmigration.get(
        "v1/{parent}/cloneJobs",
        t.struct(
            {
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCloneJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesMigratingVmsCloneJobsList"] = vmmigration.get(
        "v1/{parent}/cloneJobs",
        t.struct(
            {
                "pageToken": t.string(),
                "orderBy": t.string().optional(),
                "parent": t.string(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListCloneJobsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesMigratingVmsReplicationCyclesList"
    ] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReplicationCycleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsSourcesMigratingVmsReplicationCyclesGet"
    ] = vmmigration.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ReplicationCycleOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsDelete"] = vmmigration.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UtilizationReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsList"] = vmmigration.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UtilizationReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsCreate"] = vmmigration.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UtilizationReportOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSourcesUtilizationReportsGet"] = vmmigration.get(
        "v1/{name}",
        t.struct(
            {
                "view": t.string().optional(),
                "name": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["UtilizationReportOut"]),
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
    functions["projectsLocationsGroupsPatch"] = vmmigration.get(
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
    functions["projectsLocationsGroupsRemoveGroupMigration"] = vmmigration.get(
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
    functions["projectsLocationsGroupsList"] = vmmigration.get(
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

    return Import(
        importer="vmmigration", renames=renames, types=types, functions=functions
    )
