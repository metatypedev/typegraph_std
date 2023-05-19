from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_baremetalsolution() -> Import:
    baremetalsolution = HTTPRuntime("https://baremetalsolution.googleapis.com/")

    renames = {
        "ErrorResponse": "_baremetalsolution_1_ErrorResponse",
        "NetworkAddressReservationIn": "_baremetalsolution_2_NetworkAddressReservationIn",
        "NetworkAddressReservationOut": "_baremetalsolution_3_NetworkAddressReservationOut",
        "SnapshotReservationDetailIn": "_baremetalsolution_4_SnapshotReservationDetailIn",
        "SnapshotReservationDetailOut": "_baremetalsolution_5_SnapshotReservationDetailOut",
        "InstanceIn": "_baremetalsolution_6_InstanceIn",
        "InstanceOut": "_baremetalsolution_7_InstanceOut",
        "NetworkConfigIn": "_baremetalsolution_8_NetworkConfigIn",
        "NetworkConfigOut": "_baremetalsolution_9_NetworkConfigOut",
        "AllowedClientIn": "_baremetalsolution_10_AllowedClientIn",
        "AllowedClientOut": "_baremetalsolution_11_AllowedClientOut",
        "NetworkUsageIn": "_baremetalsolution_12_NetworkUsageIn",
        "NetworkUsageOut": "_baremetalsolution_13_NetworkUsageOut",
        "LocationIn": "_baremetalsolution_14_LocationIn",
        "LocationOut": "_baremetalsolution_15_LocationOut",
        "RenameNfsShareRequestIn": "_baremetalsolution_16_RenameNfsShareRequestIn",
        "RenameNfsShareRequestOut": "_baremetalsolution_17_RenameNfsShareRequestOut",
        "SubmitProvisioningConfigRequestIn": "_baremetalsolution_18_SubmitProvisioningConfigRequestIn",
        "SubmitProvisioningConfigRequestOut": "_baremetalsolution_19_SubmitProvisioningConfigRequestOut",
        "RenameVolumeRequestIn": "_baremetalsolution_20_RenameVolumeRequestIn",
        "RenameVolumeRequestOut": "_baremetalsolution_21_RenameVolumeRequestOut",
        "ResetInstanceRequestIn": "_baremetalsolution_22_ResetInstanceRequestIn",
        "ResetInstanceRequestOut": "_baremetalsolution_23_ResetInstanceRequestOut",
        "EmptyIn": "_baremetalsolution_24_EmptyIn",
        "EmptyOut": "_baremetalsolution_25_EmptyOut",
        "NfsExportIn": "_baremetalsolution_26_NfsExportIn",
        "NfsExportOut": "_baremetalsolution_27_NfsExportOut",
        "ServerNetworkTemplateIn": "_baremetalsolution_28_ServerNetworkTemplateIn",
        "ServerNetworkTemplateOut": "_baremetalsolution_29_ServerNetworkTemplateOut",
        "ListNetworksResponseIn": "_baremetalsolution_30_ListNetworksResponseIn",
        "ListNetworksResponseOut": "_baremetalsolution_31_ListNetworksResponseOut",
        "NetworkAddressIn": "_baremetalsolution_32_NetworkAddressIn",
        "NetworkAddressOut": "_baremetalsolution_33_NetworkAddressOut",
        "OperationIn": "_baremetalsolution_34_OperationIn",
        "OperationOut": "_baremetalsolution_35_OperationOut",
        "VolumeIn": "_baremetalsolution_36_VolumeIn",
        "VolumeOut": "_baremetalsolution_37_VolumeOut",
        "StatusIn": "_baremetalsolution_38_StatusIn",
        "StatusOut": "_baremetalsolution_39_StatusOut",
        "QosPolicyIn": "_baremetalsolution_40_QosPolicyIn",
        "QosPolicyOut": "_baremetalsolution_41_QosPolicyOut",
        "ListVolumesResponseIn": "_baremetalsolution_42_ListVolumesResponseIn",
        "ListVolumesResponseOut": "_baremetalsolution_43_ListVolumesResponseOut",
        "ListProvisioningQuotasResponseIn": "_baremetalsolution_44_ListProvisioningQuotasResponseIn",
        "ListProvisioningQuotasResponseOut": "_baremetalsolution_45_ListProvisioningQuotasResponseOut",
        "IntakeVlanAttachmentIn": "_baremetalsolution_46_IntakeVlanAttachmentIn",
        "IntakeVlanAttachmentOut": "_baremetalsolution_47_IntakeVlanAttachmentOut",
        "ListInstancesResponseIn": "_baremetalsolution_48_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_baremetalsolution_49_ListInstancesResponseOut",
        "VolumeSnapshotIn": "_baremetalsolution_50_VolumeSnapshotIn",
        "VolumeSnapshotOut": "_baremetalsolution_51_VolumeSnapshotOut",
        "LunIn": "_baremetalsolution_52_LunIn",
        "LunOut": "_baremetalsolution_53_LunOut",
        "RestoreVolumeSnapshotRequestIn": "_baremetalsolution_54_RestoreVolumeSnapshotRequestIn",
        "RestoreVolumeSnapshotRequestOut": "_baremetalsolution_55_RestoreVolumeSnapshotRequestOut",
        "NetworkIn": "_baremetalsolution_56_NetworkIn",
        "NetworkOut": "_baremetalsolution_57_NetworkOut",
        "SSHKeyIn": "_baremetalsolution_58_SSHKeyIn",
        "SSHKeyOut": "_baremetalsolution_59_SSHKeyOut",
        "InstanceQuotaIn": "_baremetalsolution_60_InstanceQuotaIn",
        "InstanceQuotaOut": "_baremetalsolution_61_InstanceQuotaOut",
        "FetchInstanceProvisioningSettingsResponseIn": "_baremetalsolution_62_FetchInstanceProvisioningSettingsResponseIn",
        "FetchInstanceProvisioningSettingsResponseOut": "_baremetalsolution_63_FetchInstanceProvisioningSettingsResponseOut",
        "StopInstanceRequestIn": "_baremetalsolution_64_StopInstanceRequestIn",
        "StopInstanceRequestOut": "_baremetalsolution_65_StopInstanceRequestOut",
        "RenameNetworkRequestIn": "_baremetalsolution_66_RenameNetworkRequestIn",
        "RenameNetworkRequestOut": "_baremetalsolution_67_RenameNetworkRequestOut",
        "ListNetworkUsageResponseIn": "_baremetalsolution_68_ListNetworkUsageResponseIn",
        "ListNetworkUsageResponseOut": "_baremetalsolution_69_ListNetworkUsageResponseOut",
        "GoogleCloudBaremetalsolutionV2LogicalInterfaceIn": "_baremetalsolution_70_GoogleCloudBaremetalsolutionV2LogicalInterfaceIn",
        "GoogleCloudBaremetalsolutionV2LogicalInterfaceOut": "_baremetalsolution_71_GoogleCloudBaremetalsolutionV2LogicalInterfaceOut",
        "InstanceConfigIn": "_baremetalsolution_72_InstanceConfigIn",
        "InstanceConfigOut": "_baremetalsolution_73_InstanceConfigOut",
        "VolumeConfigIn": "_baremetalsolution_74_VolumeConfigIn",
        "VolumeConfigOut": "_baremetalsolution_75_VolumeConfigOut",
        "EnableInteractiveSerialConsoleRequestIn": "_baremetalsolution_76_EnableInteractiveSerialConsoleRequestIn",
        "EnableInteractiveSerialConsoleRequestOut": "_baremetalsolution_77_EnableInteractiveSerialConsoleRequestOut",
        "ListNfsSharesResponseIn": "_baremetalsolution_78_ListNfsSharesResponseIn",
        "ListNfsSharesResponseOut": "_baremetalsolution_79_ListNfsSharesResponseOut",
        "ListLocationsResponseIn": "_baremetalsolution_80_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_baremetalsolution_81_ListLocationsResponseOut",
        "EvictLunRequestIn": "_baremetalsolution_82_EvictLunRequestIn",
        "EvictLunRequestOut": "_baremetalsolution_83_EvictLunRequestOut",
        "NetworkMountPointIn": "_baremetalsolution_84_NetworkMountPointIn",
        "NetworkMountPointOut": "_baremetalsolution_85_NetworkMountPointOut",
        "DetachLunRequestIn": "_baremetalsolution_86_DetachLunRequestIn",
        "DetachLunRequestOut": "_baremetalsolution_87_DetachLunRequestOut",
        "VlanAttachmentIn": "_baremetalsolution_88_VlanAttachmentIn",
        "VlanAttachmentOut": "_baremetalsolution_89_VlanAttachmentOut",
        "GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceIn": "_baremetalsolution_90_GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceIn",
        "GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceOut": "_baremetalsolution_91_GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceOut",
        "ResizeVolumeRequestIn": "_baremetalsolution_92_ResizeVolumeRequestIn",
        "ResizeVolumeRequestOut": "_baremetalsolution_93_ResizeVolumeRequestOut",
        "ProvisioningConfigIn": "_baremetalsolution_94_ProvisioningConfigIn",
        "ProvisioningConfigOut": "_baremetalsolution_95_ProvisioningConfigOut",
        "NfsShareIn": "_baremetalsolution_96_NfsShareIn",
        "NfsShareOut": "_baremetalsolution_97_NfsShareOut",
        "SubmitProvisioningConfigResponseIn": "_baremetalsolution_98_SubmitProvisioningConfigResponseIn",
        "SubmitProvisioningConfigResponseOut": "_baremetalsolution_99_SubmitProvisioningConfigResponseOut",
        "ListLunsResponseIn": "_baremetalsolution_100_ListLunsResponseIn",
        "ListLunsResponseOut": "_baremetalsolution_101_ListLunsResponseOut",
        "OSImageIn": "_baremetalsolution_102_OSImageIn",
        "OSImageOut": "_baremetalsolution_103_OSImageOut",
        "ProvisioningQuotaIn": "_baremetalsolution_104_ProvisioningQuotaIn",
        "ProvisioningQuotaOut": "_baremetalsolution_105_ProvisioningQuotaOut",
        "LogicalNetworkInterfaceIn": "_baremetalsolution_106_LogicalNetworkInterfaceIn",
        "LogicalNetworkInterfaceOut": "_baremetalsolution_107_LogicalNetworkInterfaceOut",
        "RenameInstanceRequestIn": "_baremetalsolution_108_RenameInstanceRequestIn",
        "RenameInstanceRequestOut": "_baremetalsolution_109_RenameInstanceRequestOut",
        "StartInstanceRequestIn": "_baremetalsolution_110_StartInstanceRequestIn",
        "StartInstanceRequestOut": "_baremetalsolution_111_StartInstanceRequestOut",
        "ListSSHKeysResponseIn": "_baremetalsolution_112_ListSSHKeysResponseIn",
        "ListSSHKeysResponseOut": "_baremetalsolution_113_ListSSHKeysResponseOut",
        "VRFIn": "_baremetalsolution_114_VRFIn",
        "VRFOut": "_baremetalsolution_115_VRFOut",
        "EvictVolumeRequestIn": "_baremetalsolution_116_EvictVolumeRequestIn",
        "EvictVolumeRequestOut": "_baremetalsolution_117_EvictVolumeRequestOut",
        "DisableInteractiveSerialConsoleRequestIn": "_baremetalsolution_118_DisableInteractiveSerialConsoleRequestIn",
        "DisableInteractiveSerialConsoleRequestOut": "_baremetalsolution_119_DisableInteractiveSerialConsoleRequestOut",
        "ListVolumeSnapshotsResponseIn": "_baremetalsolution_120_ListVolumeSnapshotsResponseIn",
        "ListVolumeSnapshotsResponseOut": "_baremetalsolution_121_ListVolumeSnapshotsResponseOut",
        "LunRangeIn": "_baremetalsolution_122_LunRangeIn",
        "LunRangeOut": "_baremetalsolution_123_LunRangeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["NetworkAddressReservationIn"] = t.struct(
        {
            "startAddress": t.string().optional(),
            "endAddress": t.string().optional(),
            "note": t.string().optional(),
        }
    ).named(renames["NetworkAddressReservationIn"])
    types["NetworkAddressReservationOut"] = t.struct(
        {
            "startAddress": t.string().optional(),
            "endAddress": t.string().optional(),
            "note": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressReservationOut"])
    types["SnapshotReservationDetailIn"] = t.struct(
        {
            "reservedSpaceRemainingGib": t.string().optional(),
            "reservedSpacePercent": t.integer().optional(),
            "reservedSpaceGib": t.string().optional(),
            "reservedSpaceUsedPercent": t.integer().optional(),
        }
    ).named(renames["SnapshotReservationDetailIn"])
    types["SnapshotReservationDetailOut"] = t.struct(
        {
            "reservedSpaceRemainingGib": t.string().optional(),
            "reservedSpacePercent": t.integer().optional(),
            "reservedSpaceGib": t.string().optional(),
            "reservedSpaceUsedPercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotReservationDetailOut"])
    types["InstanceIn"] = t.struct(
        {
            "machineType": t.string().optional(),
            "osImage": t.string().optional(),
            "luns": t.array(t.proxy(renames["LunIn"])).optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "networkTemplate": t.string().optional(),
            "hyperthreadingEnabled": t.boolean().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "workloadProfile": t.string().optional(),
            "logicalInterfaces": t.array(
                t.proxy(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceIn"])
            ).optional(),
            "pod": t.string().optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "firmwareVersion": t.string().optional(),
            "machineType": t.string().optional(),
            "osImage": t.string().optional(),
            "interactiveSerialConsoleEnabled": t.boolean().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "luns": t.array(t.proxy(renames["LunOut"])).optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "networkTemplate": t.string().optional(),
            "hyperthreadingEnabled": t.boolean().optional(),
            "id": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "workloadProfile": t.string().optional(),
            "loginInfo": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkOut"])).optional(),
            "logicalInterfaces": t.array(
                t.proxy(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceOut"])
            ).optional(),
            "state": t.string().optional(),
            "pod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "jumboFramesEnabled": t.boolean().optional(),
            "vlanAttachments": t.array(
                t.proxy(renames["IntakeVlanAttachmentIn"])
            ).optional(),
            "serviceCidr": t.string().optional(),
            "cidr": t.string().optional(),
            "bandwidth": t.string().optional(),
            "vlanSameProject": t.boolean().optional(),
            "gcpService": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "userNote": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "jumboFramesEnabled": t.boolean().optional(),
            "vlanAttachments": t.array(
                t.proxy(renames["IntakeVlanAttachmentOut"])
            ).optional(),
            "serviceCidr": t.string().optional(),
            "name": t.string().optional(),
            "cidr": t.string().optional(),
            "bandwidth": t.string().optional(),
            "vlanSameProject": t.boolean().optional(),
            "gcpService": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "userNote": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["AllowedClientIn"] = t.struct(
        {
            "allowedClientsCidr": t.string().optional(),
            "noRootSquash": t.boolean().optional(),
            "allowSuid": t.boolean().optional(),
            "network": t.string().optional(),
            "mountPermissions": t.string().optional(),
            "allowDev": t.boolean().optional(),
        }
    ).named(renames["AllowedClientIn"])
    types["AllowedClientOut"] = t.struct(
        {
            "shareIp": t.string().optional(),
            "nfsPath": t.string().optional(),
            "allowedClientsCidr": t.string().optional(),
            "noRootSquash": t.boolean().optional(),
            "allowSuid": t.boolean().optional(),
            "network": t.string().optional(),
            "mountPermissions": t.string().optional(),
            "allowDev": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllowedClientOut"])
    types["NetworkUsageIn"] = t.struct(
        {
            "network": t.proxy(renames["NetworkIn"]).optional(),
            "usedIps": t.array(t.string()).optional(),
        }
    ).named(renames["NetworkUsageIn"])
    types["NetworkUsageOut"] = t.struct(
        {
            "network": t.proxy(renames["NetworkOut"]).optional(),
            "usedIps": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkUsageOut"])
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["RenameNfsShareRequestIn"] = t.struct({"newNfsshareId": t.string()}).named(
        renames["RenameNfsShareRequestIn"]
    )
    types["RenameNfsShareRequestOut"] = t.struct(
        {
            "newNfsshareId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameNfsShareRequestOut"])
    types["SubmitProvisioningConfigRequestIn"] = t.struct(
        {
            "email": t.string().optional(),
            "provisioningConfig": t.proxy(renames["ProvisioningConfigIn"]),
        }
    ).named(renames["SubmitProvisioningConfigRequestIn"])
    types["SubmitProvisioningConfigRequestOut"] = t.struct(
        {
            "email": t.string().optional(),
            "provisioningConfig": t.proxy(renames["ProvisioningConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitProvisioningConfigRequestOut"])
    types["RenameVolumeRequestIn"] = t.struct({"newVolumeId": t.string()}).named(
        renames["RenameVolumeRequestIn"]
    )
    types["RenameVolumeRequestOut"] = t.struct(
        {
            "newVolumeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameVolumeRequestOut"])
    types["ResetInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResetInstanceRequestIn"]
    )
    types["ResetInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetInstanceRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["NfsExportIn"] = t.struct(
        {
            "allowSuid": t.boolean().optional(),
            "allowDev": t.boolean().optional(),
            "noRootSquash": t.boolean().optional(),
            "networkId": t.string().optional(),
            "machineId": t.string().optional(),
            "cidr": t.string().optional(),
            "permissions": t.string().optional(),
        }
    ).named(renames["NfsExportIn"])
    types["NfsExportOut"] = t.struct(
        {
            "allowSuid": t.boolean().optional(),
            "allowDev": t.boolean().optional(),
            "noRootSquash": t.boolean().optional(),
            "networkId": t.string().optional(),
            "machineId": t.string().optional(),
            "cidr": t.string().optional(),
            "permissions": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportOut"])
    types["ServerNetworkTemplateIn"] = t.struct(
        {
            "logicalInterfaces": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceIn"
                    ]
                )
            ).optional(),
            "applicableInstanceTypes": t.array(t.string()).optional(),
        }
    ).named(renames["ServerNetworkTemplateIn"])
    types["ServerNetworkTemplateOut"] = t.struct(
        {
            "name": t.string().optional(),
            "logicalInterfaces": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceOut"
                    ]
                )
            ).optional(),
            "applicableInstanceTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServerNetworkTemplateOut"])
    types["ListNetworksResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "networks": t.array(t.proxy(renames["NetworkIn"])).optional(),
        }
    ).named(renames["ListNetworksResponseIn"])
    types["ListNetworksResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "networks": t.array(t.proxy(renames["NetworkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNetworksResponseOut"])
    types["NetworkAddressIn"] = t.struct(
        {
            "existingNetworkId": t.string().optional(),
            "address": t.string().optional(),
            "networkId": t.string().optional(),
        }
    ).named(renames["NetworkAddressIn"])
    types["NetworkAddressOut"] = t.struct(
        {
            "existingNetworkId": t.string().optional(),
            "address": t.string().optional(),
            "networkId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["VolumeIn"] = t.struct(
        {
            "remainingSpaceGib": t.string().optional(),
            "performanceTier": t.string().optional(),
            "maxSizeGib": t.string().optional(),
            "snapshotSchedulePolicy": t.string().optional(),
            "requestedSizeGib": t.string().optional(),
            "state": t.string().optional(),
            "autoGrownSizeGib": t.string().optional(),
            "snapshotReservationDetail": t.proxy(
                renames["SnapshotReservationDetailIn"]
            ).optional(),
            "emergencySizeGib": t.string().optional(),
            "snapshotAutoDeleteBehavior": t.string().optional(),
            "pod": t.string().optional(),
            "snapshotEnabled": t.boolean().optional(),
            "storageType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "storageAggregatePool": t.string().optional(),
            "id": t.string().optional(),
            "originallyRequestedSizeGib": t.string().optional(),
            "currentSizeGib": t.string().optional(),
            "workloadProfile": t.string().optional(),
            "notes": t.string().optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "name": t.string().optional(),
            "attached": t.boolean().optional(),
            "protocol": t.string().optional(),
            "remainingSpaceGib": t.string().optional(),
            "performanceTier": t.string().optional(),
            "maxSizeGib": t.string().optional(),
            "snapshotSchedulePolicy": t.string().optional(),
            "requestedSizeGib": t.string().optional(),
            "state": t.string().optional(),
            "autoGrownSizeGib": t.string().optional(),
            "snapshotReservationDetail": t.proxy(
                renames["SnapshotReservationDetailOut"]
            ).optional(),
            "emergencySizeGib": t.string().optional(),
            "snapshotAutoDeleteBehavior": t.string().optional(),
            "bootVolume": t.boolean().optional(),
            "pod": t.string().optional(),
            "snapshotEnabled": t.boolean().optional(),
            "storageType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "instances": t.array(t.string()).optional(),
            "storageAggregatePool": t.string().optional(),
            "id": t.string().optional(),
            "originallyRequestedSizeGib": t.string().optional(),
            "currentSizeGib": t.string().optional(),
            "expireTime": t.string().optional(),
            "workloadProfile": t.string().optional(),
            "notes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
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
    types["QosPolicyIn"] = t.struct({"bandwidthGbps": t.number().optional()}).named(
        renames["QosPolicyIn"]
    )
    types["QosPolicyOut"] = t.struct(
        {
            "bandwidthGbps": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QosPolicyOut"])
    types["ListVolumesResponseIn"] = t.struct(
        {
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVolumesResponseIn"])
    types["ListVolumesResponseOut"] = t.struct(
        {
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVolumesResponseOut"])
    types["ListProvisioningQuotasResponseIn"] = t.struct(
        {
            "provisioningQuotas": t.array(
                t.proxy(renames["ProvisioningQuotaIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProvisioningQuotasResponseIn"])
    types["ListProvisioningQuotasResponseOut"] = t.struct(
        {
            "provisioningQuotas": t.array(
                t.proxy(renames["ProvisioningQuotaOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProvisioningQuotasResponseOut"])
    types["IntakeVlanAttachmentIn"] = t.struct(
        {"id": t.string().optional(), "pairingKey": t.string().optional()}
    ).named(renames["IntakeVlanAttachmentIn"])
    types["IntakeVlanAttachmentOut"] = t.struct(
        {
            "id": t.string().optional(),
            "pairingKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IntakeVlanAttachmentOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["VolumeSnapshotIn"] = t.struct(
        {"description": t.string().optional(), "name": t.string().optional()}
    ).named(renames["VolumeSnapshotIn"])
    types["VolumeSnapshotOut"] = t.struct(
        {
            "id": t.string().optional(),
            "storageVolume": t.string().optional(),
            "description": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeSnapshotOut"])
    types["LunIn"] = t.struct(
        {
            "storageVolume": t.string().optional(),
            "multiprotocolType": t.string().optional(),
            "state": t.string().optional(),
            "storageType": t.string().optional(),
            "id": t.string().optional(),
            "wwid": t.string().optional(),
            "bootLun": t.boolean().optional(),
            "shareable": t.boolean().optional(),
            "sizeGb": t.string().optional(),
        }
    ).named(renames["LunIn"])
    types["LunOut"] = t.struct(
        {
            "storageVolume": t.string().optional(),
            "multiprotocolType": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "instances": t.array(t.string()).optional(),
            "storageType": t.string().optional(),
            "id": t.string().optional(),
            "wwid": t.string().optional(),
            "bootLun": t.boolean().optional(),
            "shareable": t.boolean().optional(),
            "expireTime": t.string().optional(),
            "sizeGb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LunOut"])
    types["RestoreVolumeSnapshotRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestoreVolumeSnapshotRequestIn"])
    types["RestoreVolumeSnapshotRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreVolumeSnapshotRequestOut"])
    types["NetworkIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "cidr": t.string().optional(),
            "id": t.string().optional(),
            "reservations": t.array(
                t.proxy(renames["NetworkAddressReservationIn"])
            ).optional(),
            "vrf": t.proxy(renames["VRFIn"]).optional(),
            "vlanId": t.string().optional(),
            "jumboFramesEnabled": t.boolean().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mountPoints": t.array(t.proxy(renames["NetworkMountPointIn"])).optional(),
            "servicesCidr": t.string().optional(),
            "macAddress": t.array(t.string()).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["NetworkIn"])
    types["NetworkOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "cidr": t.string().optional(),
            "id": t.string().optional(),
            "reservations": t.array(
                t.proxy(renames["NetworkAddressReservationOut"])
            ).optional(),
            "name": t.string().optional(),
            "vrf": t.proxy(renames["VRFOut"]).optional(),
            "vlanId": t.string().optional(),
            "jumboFramesEnabled": t.boolean().optional(),
            "state": t.string().optional(),
            "gatewayIp": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "mountPoints": t.array(t.proxy(renames["NetworkMountPointOut"])).optional(),
            "pod": t.string().optional(),
            "servicesCidr": t.string().optional(),
            "macAddress": t.array(t.string()).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkOut"])
    types["SSHKeyIn"] = t.struct({"publicKey": t.string().optional()}).named(
        renames["SSHKeyIn"]
    )
    types["SSHKeyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "publicKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SSHKeyOut"])
    types["InstanceQuotaIn"] = t.struct(
        {
            "location": t.string().optional(),
            "gcpService": t.string().optional(),
            "instanceType": t.string().optional(),
            "availableMachineCount": t.integer().optional(),
        }
    ).named(renames["InstanceQuotaIn"])
    types["InstanceQuotaOut"] = t.struct(
        {
            "location": t.string().optional(),
            "name": t.string().optional(),
            "gcpService": t.string().optional(),
            "instanceType": t.string().optional(),
            "availableMachineCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceQuotaOut"])
    types["FetchInstanceProvisioningSettingsResponseIn"] = t.struct(
        {"images": t.array(t.proxy(renames["OSImageIn"])).optional()}
    ).named(renames["FetchInstanceProvisioningSettingsResponseIn"])
    types["FetchInstanceProvisioningSettingsResponseOut"] = t.struct(
        {
            "images": t.array(t.proxy(renames["OSImageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FetchInstanceProvisioningSettingsResponseOut"])
    types["StopInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopInstanceRequestIn"]
    )
    types["StopInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopInstanceRequestOut"])
    types["RenameNetworkRequestIn"] = t.struct({"newNetworkId": t.string()}).named(
        renames["RenameNetworkRequestIn"]
    )
    types["RenameNetworkRequestOut"] = t.struct(
        {
            "newNetworkId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameNetworkRequestOut"])
    types["ListNetworkUsageResponseIn"] = t.struct(
        {"networks": t.array(t.proxy(renames["NetworkUsageIn"])).optional()}
    ).named(renames["ListNetworkUsageResponseIn"])
    types["ListNetworkUsageResponseOut"] = t.struct(
        {
            "networks": t.array(t.proxy(renames["NetworkUsageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNetworkUsageResponseOut"])
    types["GoogleCloudBaremetalsolutionV2LogicalInterfaceIn"] = t.struct(
        {
            "interfaceIndex": t.integer().optional(),
            "name": t.string().optional(),
            "logicalNetworkInterfaces": t.array(
                t.proxy(renames["LogicalNetworkInterfaceIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceIn"])
    types["GoogleCloudBaremetalsolutionV2LogicalInterfaceOut"] = t.struct(
        {
            "interfaceIndex": t.integer().optional(),
            "name": t.string().optional(),
            "logicalNetworkInterfaces": t.array(
                t.proxy(renames["LogicalNetworkInterfaceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceOut"])
    types["InstanceConfigIn"] = t.struct(
        {
            "id": t.string().optional(),
            "networkConfig": t.string().optional(),
            "networkTemplate": t.string().optional(),
            "logicalInterfaces": t.array(
                t.proxy(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceIn"])
            ).optional(),
            "instanceType": t.string().optional(),
            "hyperthreading": t.boolean().optional(),
            "osImage": t.string().optional(),
            "userNote": t.string().optional(),
            "accountNetworksEnabled": t.boolean().optional(),
            "clientNetwork": t.proxy(renames["NetworkAddressIn"]).optional(),
            "privateNetwork": t.proxy(renames["NetworkAddressIn"]).optional(),
        }
    ).named(renames["InstanceConfigIn"])
    types["InstanceConfigOut"] = t.struct(
        {
            "id": t.string().optional(),
            "networkConfig": t.string().optional(),
            "name": t.string().optional(),
            "networkTemplate": t.string().optional(),
            "logicalInterfaces": t.array(
                t.proxy(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceOut"])
            ).optional(),
            "instanceType": t.string().optional(),
            "hyperthreading": t.boolean().optional(),
            "osImage": t.string().optional(),
            "userNote": t.string().optional(),
            "accountNetworksEnabled": t.boolean().optional(),
            "clientNetwork": t.proxy(renames["NetworkAddressOut"]).optional(),
            "privateNetwork": t.proxy(renames["NetworkAddressOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
    types["VolumeConfigIn"] = t.struct(
        {
            "userNote": t.string().optional(),
            "id": t.string().optional(),
            "machineIds": t.array(t.string()).optional(),
            "lunRanges": t.array(t.proxy(renames["LunRangeIn"])).optional(),
            "type": t.string().optional(),
            "snapshotsEnabled": t.boolean().optional(),
            "nfsExports": t.array(t.proxy(renames["NfsExportIn"])).optional(),
            "sizeGb": t.integer().optional(),
            "protocol": t.string().optional(),
            "performanceTier": t.string().optional(),
            "gcpService": t.string().optional(),
            "storageAggregatePool": t.string().optional(),
        }
    ).named(renames["VolumeConfigIn"])
    types["VolumeConfigOut"] = t.struct(
        {
            "userNote": t.string().optional(),
            "name": t.string().optional(),
            "id": t.string().optional(),
            "machineIds": t.array(t.string()).optional(),
            "lunRanges": t.array(t.proxy(renames["LunRangeOut"])).optional(),
            "type": t.string().optional(),
            "snapshotsEnabled": t.boolean().optional(),
            "nfsExports": t.array(t.proxy(renames["NfsExportOut"])).optional(),
            "sizeGb": t.integer().optional(),
            "protocol": t.string().optional(),
            "performanceTier": t.string().optional(),
            "gcpService": t.string().optional(),
            "storageAggregatePool": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeConfigOut"])
    types["EnableInteractiveSerialConsoleRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EnableInteractiveSerialConsoleRequestIn"])
    types["EnableInteractiveSerialConsoleRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableInteractiveSerialConsoleRequestOut"])
    types["ListNfsSharesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nfsShares": t.array(t.proxy(renames["NfsShareIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListNfsSharesResponseIn"])
    types["ListNfsSharesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nfsShares": t.array(t.proxy(renames["NfsShareOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNfsSharesResponseOut"])
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
    types["EvictLunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EvictLunRequestIn"]
    )
    types["EvictLunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EvictLunRequestOut"])
    types["NetworkMountPointIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "logicalInterface": t.string().optional(),
            "instance": t.string().optional(),
            "defaultGateway": t.boolean().optional(),
        }
    ).named(renames["NetworkMountPointIn"])
    types["NetworkMountPointOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "logicalInterface": t.string().optional(),
            "instance": t.string().optional(),
            "defaultGateway": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkMountPointOut"])
    types["DetachLunRequestIn"] = t.struct(
        {"skipReboot": t.boolean().optional(), "lun": t.string()}
    ).named(renames["DetachLunRequestIn"])
    types["DetachLunRequestOut"] = t.struct(
        {
            "skipReboot": t.boolean().optional(),
            "lun": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetachLunRequestOut"])
    types["VlanAttachmentIn"] = t.struct(
        {
            "qosPolicy": t.proxy(renames["QosPolicyIn"]).optional(),
            "peerIp": t.string().optional(),
            "id": t.string().optional(),
            "routerIp": t.string().optional(),
            "peerVlanId": t.string().optional(),
            "pairingKey": t.string().optional(),
        }
    ).named(renames["VlanAttachmentIn"])
    types["VlanAttachmentOut"] = t.struct(
        {
            "qosPolicy": t.proxy(renames["QosPolicyOut"]).optional(),
            "peerIp": t.string().optional(),
            "id": t.string().optional(),
            "routerIp": t.string().optional(),
            "peerVlanId": t.string().optional(),
            "pairingKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VlanAttachmentOut"])
    types[
        "GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceIn"
    ] = t.struct(
        {
            "required": t.boolean().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceIn"]
    )
    types[
        "GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceOut"
    ] = t.struct(
        {
            "required": t.boolean().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBaremetalsolutionV2ServerNetworkTemplateLogicalInterfaceOut"
        ]
    )
    types["ResizeVolumeRequestIn"] = t.struct({"sizeGib": t.string().optional()}).named(
        renames["ResizeVolumeRequestIn"]
    )
    types["ResizeVolumeRequestOut"] = t.struct(
        {
            "sizeGib": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResizeVolumeRequestOut"])
    types["ProvisioningConfigIn"] = t.struct(
        {
            "volumes": t.array(t.proxy(renames["VolumeConfigIn"])).optional(),
            "handoverServiceAccount": t.string().optional(),
            "statusMessage": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceConfigIn"])).optional(),
            "customId": t.string().optional(),
            "vpcScEnabled": t.boolean().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
            "ticketId": t.string().optional(),
            "location": t.string().optional(),
            "email": t.string().optional(),
        }
    ).named(renames["ProvisioningConfigIn"])
    types["ProvisioningConfigOut"] = t.struct(
        {
            "volumes": t.array(t.proxy(renames["VolumeConfigOut"])).optional(),
            "handoverServiceAccount": t.string().optional(),
            "statusMessage": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceConfigOut"])).optional(),
            "customId": t.string().optional(),
            "vpcScEnabled": t.boolean().optional(),
            "state": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigOut"])).optional(),
            "ticketId": t.string().optional(),
            "name": t.string().optional(),
            "cloudConsoleUri": t.string().optional(),
            "location": t.string().optional(),
            "updateTime": t.string().optional(),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvisioningConfigOut"])
    types["NfsShareIn"] = t.struct(
        {
            "name": t.string().optional(),
            "requestedSizeGib": t.string().optional(),
            "allowedClients": t.array(t.proxy(renames["AllowedClientIn"])).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "storageType": t.string().optional(),
        }
    ).named(renames["NfsShareIn"])
    types["NfsShareOut"] = t.struct(
        {
            "name": t.string().optional(),
            "requestedSizeGib": t.string().optional(),
            "state": t.string().optional(),
            "nfsShareId": t.string().optional(),
            "allowedClients": t.array(t.proxy(renames["AllowedClientOut"])).optional(),
            "volume": t.string().optional(),
            "id": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "storageType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsShareOut"])
    types["SubmitProvisioningConfigResponseIn"] = t.struct(
        {"provisioningConfig": t.proxy(renames["ProvisioningConfigIn"]).optional()}
    ).named(renames["SubmitProvisioningConfigResponseIn"])
    types["SubmitProvisioningConfigResponseOut"] = t.struct(
        {
            "provisioningConfig": t.proxy(renames["ProvisioningConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitProvisioningConfigResponseOut"])
    types["ListLunsResponseIn"] = t.struct(
        {
            "luns": t.array(t.proxy(renames["LunIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListLunsResponseIn"])
    types["ListLunsResponseOut"] = t.struct(
        {
            "luns": t.array(t.proxy(renames["LunOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLunsResponseOut"])
    types["OSImageIn"] = t.struct(
        {
            "description": t.string().optional(),
            "supportedNetworkTemplates": t.array(
                t.proxy(renames["ServerNetworkTemplateIn"])
            ).optional(),
            "code": t.string().optional(),
            "applicableInstanceTypes": t.array(t.string()).optional(),
        }
    ).named(renames["OSImageIn"])
    types["OSImageOut"] = t.struct(
        {
            "description": t.string().optional(),
            "supportedNetworkTemplates": t.array(
                t.proxy(renames["ServerNetworkTemplateOut"])
            ).optional(),
            "code": t.string().optional(),
            "applicableInstanceTypes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OSImageOut"])
    types["ProvisioningQuotaIn"] = t.struct(
        {
            "networkBandwidth": t.string().optional(),
            "assetType": t.string().optional(),
            "instanceQuota": t.proxy(renames["InstanceQuotaIn"]).optional(),
            "availableCount": t.integer().optional(),
            "gcpService": t.string().optional(),
            "location": t.string().optional(),
            "storageGib": t.string().optional(),
            "serverCount": t.string().optional(),
        }
    ).named(renames["ProvisioningQuotaIn"])
    types["ProvisioningQuotaOut"] = t.struct(
        {
            "networkBandwidth": t.string().optional(),
            "assetType": t.string().optional(),
            "name": t.string().optional(),
            "instanceQuota": t.proxy(renames["InstanceQuotaOut"]).optional(),
            "availableCount": t.integer().optional(),
            "gcpService": t.string().optional(),
            "location": t.string().optional(),
            "storageGib": t.string().optional(),
            "serverCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvisioningQuotaOut"])
    types["LogicalNetworkInterfaceIn"] = t.struct(
        {
            "network": t.string().optional(),
            "networkType": t.string().optional(),
            "ipAddress": t.string().optional(),
            "id": t.string().optional(),
            "defaultGateway": t.boolean().optional(),
        }
    ).named(renames["LogicalNetworkInterfaceIn"])
    types["LogicalNetworkInterfaceOut"] = t.struct(
        {
            "network": t.string().optional(),
            "networkType": t.string().optional(),
            "ipAddress": t.string().optional(),
            "id": t.string().optional(),
            "defaultGateway": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogicalNetworkInterfaceOut"])
    types["RenameInstanceRequestIn"] = t.struct({"newInstanceId": t.string()}).named(
        renames["RenameInstanceRequestIn"]
    )
    types["RenameInstanceRequestOut"] = t.struct(
        {
            "newInstanceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameInstanceRequestOut"])
    types["StartInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartInstanceRequestIn"]
    )
    types["StartInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartInstanceRequestOut"])
    types["ListSSHKeysResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sshKeys": t.array(t.proxy(renames["SSHKeyIn"])).optional(),
        }
    ).named(renames["ListSSHKeysResponseIn"])
    types["ListSSHKeysResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "sshKeys": t.array(t.proxy(renames["SSHKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSSHKeysResponseOut"])
    types["VRFIn"] = t.struct(
        {
            "name": t.string().optional(),
            "qosPolicy": t.proxy(renames["QosPolicyIn"]).optional(),
            "state": t.string().optional(),
            "vlanAttachments": t.array(t.proxy(renames["VlanAttachmentIn"])).optional(),
        }
    ).named(renames["VRFIn"])
    types["VRFOut"] = t.struct(
        {
            "name": t.string().optional(),
            "qosPolicy": t.proxy(renames["QosPolicyOut"]).optional(),
            "state": t.string().optional(),
            "vlanAttachments": t.array(
                t.proxy(renames["VlanAttachmentOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VRFOut"])
    types["EvictVolumeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EvictVolumeRequestIn"]
    )
    types["EvictVolumeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EvictVolumeRequestOut"])
    types["DisableInteractiveSerialConsoleRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DisableInteractiveSerialConsoleRequestIn"])
    types["DisableInteractiveSerialConsoleRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DisableInteractiveSerialConsoleRequestOut"])
    types["ListVolumeSnapshotsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "volumeSnapshots": t.array(t.proxy(renames["VolumeSnapshotIn"])).optional(),
        }
    ).named(renames["ListVolumeSnapshotsResponseIn"])
    types["ListVolumeSnapshotsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "volumeSnapshots": t.array(
                t.proxy(renames["VolumeSnapshotOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVolumeSnapshotsResponseOut"])
    types["LunRangeIn"] = t.struct(
        {"sizeGb": t.integer().optional(), "quantity": t.integer().optional()}
    ).named(renames["LunRangeIn"])
    types["LunRangeOut"] = t.struct(
        {
            "sizeGb": t.integer().optional(),
            "quantity": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LunRangeOut"])

    functions = {}
    functions["projectsLocationsGet"] = baremetalsolution.get(
        "v2/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = baremetalsolution.get(
        "v2/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningQuotasList"] = baremetalsolution.get(
        "v2/{parent}/provisioningQuotas",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProvisioningQuotasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesGet"] = baremetalsolution.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesPatch"] = baremetalsolution.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesRename"] = baremetalsolution.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesCreate"] = baremetalsolution.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesList"] = baremetalsolution.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesDelete"] = baremetalsolution.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksGet"] = baremetalsolution.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ipAddress": t.string().optional(),
                "cidr": t.string().optional(),
                "id": t.string().optional(),
                "reservations": t.array(
                    t.proxy(renames["NetworkAddressReservationIn"])
                ).optional(),
                "vrf": t.proxy(renames["VRFIn"]).optional(),
                "vlanId": t.string().optional(),
                "jumboFramesEnabled": t.boolean().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mountPoints": t.array(
                    t.proxy(renames["NetworkMountPointIn"])
                ).optional(),
                "servicesCidr": t.string().optional(),
                "macAddress": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksListNetworkUsage"] = baremetalsolution.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ipAddress": t.string().optional(),
                "cidr": t.string().optional(),
                "id": t.string().optional(),
                "reservations": t.array(
                    t.proxy(renames["NetworkAddressReservationIn"])
                ).optional(),
                "vrf": t.proxy(renames["VRFIn"]).optional(),
                "vlanId": t.string().optional(),
                "jumboFramesEnabled": t.boolean().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mountPoints": t.array(
                    t.proxy(renames["NetworkMountPointIn"])
                ).optional(),
                "servicesCidr": t.string().optional(),
                "macAddress": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksList"] = baremetalsolution.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ipAddress": t.string().optional(),
                "cidr": t.string().optional(),
                "id": t.string().optional(),
                "reservations": t.array(
                    t.proxy(renames["NetworkAddressReservationIn"])
                ).optional(),
                "vrf": t.proxy(renames["VRFIn"]).optional(),
                "vlanId": t.string().optional(),
                "jumboFramesEnabled": t.boolean().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mountPoints": t.array(
                    t.proxy(renames["NetworkMountPointIn"])
                ).optional(),
                "servicesCidr": t.string().optional(),
                "macAddress": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksRename"] = baremetalsolution.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ipAddress": t.string().optional(),
                "cidr": t.string().optional(),
                "id": t.string().optional(),
                "reservations": t.array(
                    t.proxy(renames["NetworkAddressReservationIn"])
                ).optional(),
                "vrf": t.proxy(renames["VRFIn"]).optional(),
                "vlanId": t.string().optional(),
                "jumboFramesEnabled": t.boolean().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mountPoints": t.array(
                    t.proxy(renames["NetworkMountPointIn"])
                ).optional(),
                "servicesCidr": t.string().optional(),
                "macAddress": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksPatch"] = baremetalsolution.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "ipAddress": t.string().optional(),
                "cidr": t.string().optional(),
                "id": t.string().optional(),
                "reservations": t.array(
                    t.proxy(renames["NetworkAddressReservationIn"])
                ).optional(),
                "vrf": t.proxy(renames["VRFIn"]).optional(),
                "vlanId": t.string().optional(),
                "jumboFramesEnabled": t.boolean().optional(),
                "state": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "mountPoints": t.array(
                    t.proxy(renames["NetworkMountPointIn"])
                ).optional(),
                "servicesCidr": t.string().optional(),
                "macAddress": t.array(t.string()).optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSshKeysCreate"] = baremetalsolution.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSshKeysList"] = baremetalsolution.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSshKeysDelete"] = baremetalsolution.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesResize"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newVolumeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesPatch"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newVolumeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesList"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newVolumeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesEvict"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newVolumeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesGet"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newVolumeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesRename"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newVolumeId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesLunsGet"] = baremetalsolution.post(
        "v2/{name}:evict",
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
    functions["projectsLocationsVolumesLunsList"] = baremetalsolution.post(
        "v2/{name}:evict",
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
    functions["projectsLocationsVolumesLunsEvict"] = baremetalsolution.post(
        "v2/{name}:evict",
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
        "projectsLocationsVolumesSnapshotsRestoreVolumeSnapshot"
    ] = baremetalsolution.post(
        "v2/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeSnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesSnapshotsGet"] = baremetalsolution.post(
        "v2/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeSnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesSnapshotsList"] = baremetalsolution.post(
        "v2/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeSnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesSnapshotsDelete"] = baremetalsolution.post(
        "v2/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeSnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesSnapshotsCreate"] = baremetalsolution.post(
        "v2/{parent}/snapshots",
        t.struct(
            {
                "parent": t.string(),
                "description": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeSnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesCreate"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesPatch"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesStart"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsInstancesEnableInteractiveSerialConsole"
    ] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesGet"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesStop"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesReset"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesList"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesDetachLun"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsInstancesDisableInteractiveSerialConsole"
    ] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsInstancesRename"] = baremetalsolution.post(
        "v2/{name}:rename",
        t.struct(
            {
                "name": t.string(),
                "newInstanceId": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["InstanceOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningConfigsPatch"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProvisioningConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningConfigsSubmit"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProvisioningConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningConfigsCreate"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProvisioningConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningConfigsGet"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProvisioningConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsInstanceProvisioningSettingsFetch"
    ] = baremetalsolution.get(
        "v2/{location}/instanceProvisioningSettings:fetch",
        t.struct({"location": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FetchInstanceProvisioningSettingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="baremetalsolution",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
