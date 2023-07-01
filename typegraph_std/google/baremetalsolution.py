from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_baremetalsolution():
    baremetalsolution = HTTPRuntime("https://baremetalsolution.googleapis.com/")

    renames = {
        "ErrorResponse": "_baremetalsolution_1_ErrorResponse",
        "OperationIn": "_baremetalsolution_2_OperationIn",
        "OperationOut": "_baremetalsolution_3_OperationOut",
        "NetworkAddressReservationIn": "_baremetalsolution_4_NetworkAddressReservationIn",
        "NetworkAddressReservationOut": "_baremetalsolution_5_NetworkAddressReservationOut",
        "ListVolumeSnapshotsResponseIn": "_baremetalsolution_6_ListVolumeSnapshotsResponseIn",
        "ListVolumeSnapshotsResponseOut": "_baremetalsolution_7_ListVolumeSnapshotsResponseOut",
        "NetworkUsageIn": "_baremetalsolution_8_NetworkUsageIn",
        "NetworkUsageOut": "_baremetalsolution_9_NetworkUsageOut",
        "NfsShareIn": "_baremetalsolution_10_NfsShareIn",
        "NfsShareOut": "_baremetalsolution_11_NfsShareOut",
        "SSHKeyIn": "_baremetalsolution_12_SSHKeyIn",
        "SSHKeyOut": "_baremetalsolution_13_SSHKeyOut",
        "IntakeVlanAttachmentIn": "_baremetalsolution_14_IntakeVlanAttachmentIn",
        "IntakeVlanAttachmentOut": "_baremetalsolution_15_IntakeVlanAttachmentOut",
        "ListLocationsResponseIn": "_baremetalsolution_16_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_baremetalsolution_17_ListLocationsResponseOut",
        "SnapshotReservationDetailIn": "_baremetalsolution_18_SnapshotReservationDetailIn",
        "SnapshotReservationDetailOut": "_baremetalsolution_19_SnapshotReservationDetailOut",
        "LunRangeIn": "_baremetalsolution_20_LunRangeIn",
        "LunRangeOut": "_baremetalsolution_21_LunRangeOut",
        "LocationIn": "_baremetalsolution_22_LocationIn",
        "LocationOut": "_baremetalsolution_23_LocationOut",
        "QosPolicyIn": "_baremetalsolution_24_QosPolicyIn",
        "QosPolicyOut": "_baremetalsolution_25_QosPolicyOut",
        "EmptyIn": "_baremetalsolution_26_EmptyIn",
        "EmptyOut": "_baremetalsolution_27_EmptyOut",
        "ProvisioningConfigIn": "_baremetalsolution_28_ProvisioningConfigIn",
        "ProvisioningConfigOut": "_baremetalsolution_29_ProvisioningConfigOut",
        "ListNetworksResponseIn": "_baremetalsolution_30_ListNetworksResponseIn",
        "ListNetworksResponseOut": "_baremetalsolution_31_ListNetworksResponseOut",
        "EnableInteractiveSerialConsoleRequestIn": "_baremetalsolution_32_EnableInteractiveSerialConsoleRequestIn",
        "EnableInteractiveSerialConsoleRequestOut": "_baremetalsolution_33_EnableInteractiveSerialConsoleRequestOut",
        "ResetInstanceResponseIn": "_baremetalsolution_34_ResetInstanceResponseIn",
        "ResetInstanceResponseOut": "_baremetalsolution_35_ResetInstanceResponseOut",
        "StopInstanceResponseIn": "_baremetalsolution_36_StopInstanceResponseIn",
        "StopInstanceResponseOut": "_baremetalsolution_37_StopInstanceResponseOut",
        "VRFIn": "_baremetalsolution_38_VRFIn",
        "VRFOut": "_baremetalsolution_39_VRFOut",
        "DetachLunRequestIn": "_baremetalsolution_40_DetachLunRequestIn",
        "DetachLunRequestOut": "_baremetalsolution_41_DetachLunRequestOut",
        "SubmitProvisioningConfigResponseIn": "_baremetalsolution_42_SubmitProvisioningConfigResponseIn",
        "SubmitProvisioningConfigResponseOut": "_baremetalsolution_43_SubmitProvisioningConfigResponseOut",
        "ProvisioningQuotaIn": "_baremetalsolution_44_ProvisioningQuotaIn",
        "ProvisioningQuotaOut": "_baremetalsolution_45_ProvisioningQuotaOut",
        "VlanAttachmentIn": "_baremetalsolution_46_VlanAttachmentIn",
        "VlanAttachmentOut": "_baremetalsolution_47_VlanAttachmentOut",
        "NetworkAddressIn": "_baremetalsolution_48_NetworkAddressIn",
        "NetworkAddressOut": "_baremetalsolution_49_NetworkAddressOut",
        "LogicalNetworkInterfaceIn": "_baremetalsolution_50_LogicalNetworkInterfaceIn",
        "LogicalNetworkInterfaceOut": "_baremetalsolution_51_LogicalNetworkInterfaceOut",
        "ListProvisioningQuotasResponseIn": "_baremetalsolution_52_ListProvisioningQuotasResponseIn",
        "ListProvisioningQuotasResponseOut": "_baremetalsolution_53_ListProvisioningQuotasResponseOut",
        "VolumeSnapshotIn": "_baremetalsolution_54_VolumeSnapshotIn",
        "VolumeSnapshotOut": "_baremetalsolution_55_VolumeSnapshotOut",
        "StatusIn": "_baremetalsolution_56_StatusIn",
        "StatusOut": "_baremetalsolution_57_StatusOut",
        "ListNfsSharesResponseIn": "_baremetalsolution_58_ListNfsSharesResponseIn",
        "ListNfsSharesResponseOut": "_baremetalsolution_59_ListNfsSharesResponseOut",
        "StartInstanceRequestIn": "_baremetalsolution_60_StartInstanceRequestIn",
        "StartInstanceRequestOut": "_baremetalsolution_61_StartInstanceRequestOut",
        "ListInstancesResponseIn": "_baremetalsolution_62_ListInstancesResponseIn",
        "ListInstancesResponseOut": "_baremetalsolution_63_ListInstancesResponseOut",
        "RenameVolumeRequestIn": "_baremetalsolution_64_RenameVolumeRequestIn",
        "RenameVolumeRequestOut": "_baremetalsolution_65_RenameVolumeRequestOut",
        "InstanceIn": "_baremetalsolution_66_InstanceIn",
        "InstanceOut": "_baremetalsolution_67_InstanceOut",
        "InstanceQuotaIn": "_baremetalsolution_68_InstanceQuotaIn",
        "InstanceQuotaOut": "_baremetalsolution_69_InstanceQuotaOut",
        "ResizeVolumeRequestIn": "_baremetalsolution_70_ResizeVolumeRequestIn",
        "ResizeVolumeRequestOut": "_baremetalsolution_71_ResizeVolumeRequestOut",
        "NetworkConfigIn": "_baremetalsolution_72_NetworkConfigIn",
        "NetworkConfigOut": "_baremetalsolution_73_NetworkConfigOut",
        "GoogleCloudBaremetalsolutionV2LogicalInterfaceIn": "_baremetalsolution_74_GoogleCloudBaremetalsolutionV2LogicalInterfaceIn",
        "GoogleCloudBaremetalsolutionV2LogicalInterfaceOut": "_baremetalsolution_75_GoogleCloudBaremetalsolutionV2LogicalInterfaceOut",
        "StartInstanceResponseIn": "_baremetalsolution_76_StartInstanceResponseIn",
        "StartInstanceResponseOut": "_baremetalsolution_77_StartInstanceResponseOut",
        "SubmitProvisioningConfigRequestIn": "_baremetalsolution_78_SubmitProvisioningConfigRequestIn",
        "SubmitProvisioningConfigRequestOut": "_baremetalsolution_79_SubmitProvisioningConfigRequestOut",
        "ListSSHKeysResponseIn": "_baremetalsolution_80_ListSSHKeysResponseIn",
        "ListSSHKeysResponseOut": "_baremetalsolution_81_ListSSHKeysResponseOut",
        "ResetInstanceRequestIn": "_baremetalsolution_82_ResetInstanceRequestIn",
        "ResetInstanceRequestOut": "_baremetalsolution_83_ResetInstanceRequestOut",
        "VolumeIn": "_baremetalsolution_84_VolumeIn",
        "VolumeOut": "_baremetalsolution_85_VolumeOut",
        "ListNetworkUsageResponseIn": "_baremetalsolution_86_ListNetworkUsageResponseIn",
        "ListNetworkUsageResponseOut": "_baremetalsolution_87_ListNetworkUsageResponseOut",
        "ListLunsResponseIn": "_baremetalsolution_88_ListLunsResponseIn",
        "ListLunsResponseOut": "_baremetalsolution_89_ListLunsResponseOut",
        "EvictLunRequestIn": "_baremetalsolution_90_EvictLunRequestIn",
        "EvictLunRequestOut": "_baremetalsolution_91_EvictLunRequestOut",
        "DisableInteractiveSerialConsoleRequestIn": "_baremetalsolution_92_DisableInteractiveSerialConsoleRequestIn",
        "DisableInteractiveSerialConsoleRequestOut": "_baremetalsolution_93_DisableInteractiveSerialConsoleRequestOut",
        "NetworkIn": "_baremetalsolution_94_NetworkIn",
        "NetworkOut": "_baremetalsolution_95_NetworkOut",
        "VolumeConfigIn": "_baremetalsolution_96_VolumeConfigIn",
        "VolumeConfigOut": "_baremetalsolution_97_VolumeConfigOut",
        "LunIn": "_baremetalsolution_98_LunIn",
        "LunOut": "_baremetalsolution_99_LunOut",
        "RenameNetworkRequestIn": "_baremetalsolution_100_RenameNetworkRequestIn",
        "RenameNetworkRequestOut": "_baremetalsolution_101_RenameNetworkRequestOut",
        "RenameNfsShareRequestIn": "_baremetalsolution_102_RenameNfsShareRequestIn",
        "RenameNfsShareRequestOut": "_baremetalsolution_103_RenameNfsShareRequestOut",
        "NetworkMountPointIn": "_baremetalsolution_104_NetworkMountPointIn",
        "NetworkMountPointOut": "_baremetalsolution_105_NetworkMountPointOut",
        "RenameInstanceRequestIn": "_baremetalsolution_106_RenameInstanceRequestIn",
        "RenameInstanceRequestOut": "_baremetalsolution_107_RenameInstanceRequestOut",
        "ListVolumesResponseIn": "_baremetalsolution_108_ListVolumesResponseIn",
        "ListVolumesResponseOut": "_baremetalsolution_109_ListVolumesResponseOut",
        "InstanceConfigIn": "_baremetalsolution_110_InstanceConfigIn",
        "InstanceConfigOut": "_baremetalsolution_111_InstanceConfigOut",
        "StopInstanceRequestIn": "_baremetalsolution_112_StopInstanceRequestIn",
        "StopInstanceRequestOut": "_baremetalsolution_113_StopInstanceRequestOut",
        "AllowedClientIn": "_baremetalsolution_114_AllowedClientIn",
        "AllowedClientOut": "_baremetalsolution_115_AllowedClientOut",
        "NfsExportIn": "_baremetalsolution_116_NfsExportIn",
        "NfsExportOut": "_baremetalsolution_117_NfsExportOut",
        "EvictVolumeRequestIn": "_baremetalsolution_118_EvictVolumeRequestIn",
        "EvictVolumeRequestOut": "_baremetalsolution_119_EvictVolumeRequestOut",
        "RestoreVolumeSnapshotRequestIn": "_baremetalsolution_120_RestoreVolumeSnapshotRequestIn",
        "RestoreVolumeSnapshotRequestOut": "_baremetalsolution_121_RestoreVolumeSnapshotRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["NetworkAddressReservationIn"] = t.struct(
        {
            "startAddress": t.string().optional(),
            "note": t.string().optional(),
            "endAddress": t.string().optional(),
        }
    ).named(renames["NetworkAddressReservationIn"])
    types["NetworkAddressReservationOut"] = t.struct(
        {
            "startAddress": t.string().optional(),
            "note": t.string().optional(),
            "endAddress": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressReservationOut"])
    types["ListVolumeSnapshotsResponseIn"] = t.struct(
        {
            "volumeSnapshots": t.array(t.proxy(renames["VolumeSnapshotIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVolumeSnapshotsResponseIn"])
    types["ListVolumeSnapshotsResponseOut"] = t.struct(
        {
            "volumeSnapshots": t.array(
                t.proxy(renames["VolumeSnapshotOut"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVolumeSnapshotsResponseOut"])
    types["NetworkUsageIn"] = t.struct(
        {
            "usedIps": t.array(t.string()).optional(),
            "network": t.proxy(renames["NetworkIn"]).optional(),
        }
    ).named(renames["NetworkUsageIn"])
    types["NetworkUsageOut"] = t.struct(
        {
            "usedIps": t.array(t.string()).optional(),
            "network": t.proxy(renames["NetworkOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkUsageOut"])
    types["NfsShareIn"] = t.struct(
        {
            "requestedSizeGib": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "storageType": t.string().optional(),
            "name": t.string().optional(),
            "allowedClients": t.array(t.proxy(renames["AllowedClientIn"])).optional(),
        }
    ).named(renames["NfsShareIn"])
    types["NfsShareOut"] = t.struct(
        {
            "id": t.string().optional(),
            "requestedSizeGib": t.string().optional(),
            "volume": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "storageType": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "nfsShareId": t.string().optional(),
            "allowedClients": t.array(t.proxy(renames["AllowedClientOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsShareOut"])
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
    types["SnapshotReservationDetailIn"] = t.struct(
        {
            "reservedSpaceGib": t.string().optional(),
            "reservedSpaceRemainingGib": t.string().optional(),
            "reservedSpaceUsedPercent": t.integer().optional(),
            "reservedSpacePercent": t.integer().optional(),
        }
    ).named(renames["SnapshotReservationDetailIn"])
    types["SnapshotReservationDetailOut"] = t.struct(
        {
            "reservedSpaceGib": t.string().optional(),
            "reservedSpaceRemainingGib": t.string().optional(),
            "reservedSpaceUsedPercent": t.integer().optional(),
            "reservedSpacePercent": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SnapshotReservationDetailOut"])
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
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["QosPolicyIn"] = t.struct({"bandwidthGbps": t.number().optional()}).named(
        renames["QosPolicyIn"]
    )
    types["QosPolicyOut"] = t.struct(
        {
            "bandwidthGbps": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["QosPolicyOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ProvisioningConfigIn"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceConfigIn"])).optional(),
            "email": t.string().optional(),
            "customId": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeConfigIn"])).optional(),
            "vpcScEnabled": t.boolean().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
            "location": t.string().optional(),
            "handoverServiceAccount": t.string().optional(),
            "ticketId": t.string().optional(),
        }
    ).named(renames["ProvisioningConfigIn"])
    types["ProvisioningConfigOut"] = t.struct(
        {
            "cloudConsoleUri": t.string().optional(),
            "statusMessage": t.string().optional(),
            "state": t.string().optional(),
            "instances": t.array(t.proxy(renames["InstanceConfigOut"])).optional(),
            "email": t.string().optional(),
            "customId": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeConfigOut"])).optional(),
            "updateTime": t.string().optional(),
            "vpcScEnabled": t.boolean().optional(),
            "networks": t.array(t.proxy(renames["NetworkConfigOut"])).optional(),
            "location": t.string().optional(),
            "handoverServiceAccount": t.string().optional(),
            "ticketId": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvisioningConfigOut"])
    types["ListNetworksResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkIn"])).optional(),
        }
    ).named(renames["ListNetworksResponseIn"])
    types["ListNetworksResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNetworksResponseOut"])
    types["EnableInteractiveSerialConsoleRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["EnableInteractiveSerialConsoleRequestIn"])
    types["EnableInteractiveSerialConsoleRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EnableInteractiveSerialConsoleRequestOut"])
    types["ResetInstanceResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResetInstanceResponseIn"]
    )
    types["ResetInstanceResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetInstanceResponseOut"])
    types["StopInstanceResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopInstanceResponseIn"]
    )
    types["StopInstanceResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopInstanceResponseOut"])
    types["VRFIn"] = t.struct(
        {
            "qosPolicy": t.proxy(renames["QosPolicyIn"]).optional(),
            "vlanAttachments": t.array(t.proxy(renames["VlanAttachmentIn"])).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["VRFIn"])
    types["VRFOut"] = t.struct(
        {
            "qosPolicy": t.proxy(renames["QosPolicyOut"]).optional(),
            "vlanAttachments": t.array(
                t.proxy(renames["VlanAttachmentOut"])
            ).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VRFOut"])
    types["DetachLunRequestIn"] = t.struct(
        {"lun": t.string(), "skipReboot": t.boolean().optional()}
    ).named(renames["DetachLunRequestIn"])
    types["DetachLunRequestOut"] = t.struct(
        {
            "lun": t.string(),
            "skipReboot": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DetachLunRequestOut"])
    types["SubmitProvisioningConfigResponseIn"] = t.struct(
        {"provisioningConfig": t.proxy(renames["ProvisioningConfigIn"]).optional()}
    ).named(renames["SubmitProvisioningConfigResponseIn"])
    types["SubmitProvisioningConfigResponseOut"] = t.struct(
        {
            "provisioningConfig": t.proxy(renames["ProvisioningConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitProvisioningConfigResponseOut"])
    types["ProvisioningQuotaIn"] = t.struct(
        {
            "storageGib": t.string().optional(),
            "gcpService": t.string().optional(),
            "availableCount": t.integer().optional(),
            "networkBandwidth": t.string().optional(),
            "location": t.string().optional(),
            "instanceQuota": t.proxy(renames["InstanceQuotaIn"]).optional(),
            "serverCount": t.string().optional(),
            "assetType": t.string().optional(),
        }
    ).named(renames["ProvisioningQuotaIn"])
    types["ProvisioningQuotaOut"] = t.struct(
        {
            "name": t.string().optional(),
            "storageGib": t.string().optional(),
            "gcpService": t.string().optional(),
            "availableCount": t.integer().optional(),
            "networkBandwidth": t.string().optional(),
            "location": t.string().optional(),
            "instanceQuota": t.proxy(renames["InstanceQuotaOut"]).optional(),
            "serverCount": t.string().optional(),
            "assetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProvisioningQuotaOut"])
    types["VlanAttachmentIn"] = t.struct(
        {
            "peerVlanId": t.string().optional(),
            "peerIp": t.string().optional(),
            "qosPolicy": t.proxy(renames["QosPolicyIn"]).optional(),
            "routerIp": t.string().optional(),
            "id": t.string().optional(),
            "pairingKey": t.string().optional(),
        }
    ).named(renames["VlanAttachmentIn"])
    types["VlanAttachmentOut"] = t.struct(
        {
            "peerVlanId": t.string().optional(),
            "peerIp": t.string().optional(),
            "qosPolicy": t.proxy(renames["QosPolicyOut"]).optional(),
            "routerIp": t.string().optional(),
            "id": t.string().optional(),
            "pairingKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VlanAttachmentOut"])
    types["NetworkAddressIn"] = t.struct(
        {
            "address": t.string().optional(),
            "networkId": t.string().optional(),
            "existingNetworkId": t.string().optional(),
        }
    ).named(renames["NetworkAddressIn"])
    types["NetworkAddressOut"] = t.struct(
        {
            "address": t.string().optional(),
            "networkId": t.string().optional(),
            "existingNetworkId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkAddressOut"])
    types["LogicalNetworkInterfaceIn"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "id": t.string().optional(),
            "network": t.string().optional(),
            "networkType": t.string().optional(),
            "defaultGateway": t.boolean().optional(),
        }
    ).named(renames["LogicalNetworkInterfaceIn"])
    types["LogicalNetworkInterfaceOut"] = t.struct(
        {
            "ipAddress": t.string().optional(),
            "id": t.string().optional(),
            "network": t.string().optional(),
            "networkType": t.string().optional(),
            "defaultGateway": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LogicalNetworkInterfaceOut"])
    types["ListProvisioningQuotasResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "provisioningQuotas": t.array(
                t.proxy(renames["ProvisioningQuotaIn"])
            ).optional(),
        }
    ).named(renames["ListProvisioningQuotasResponseIn"])
    types["ListProvisioningQuotasResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "provisioningQuotas": t.array(
                t.proxy(renames["ProvisioningQuotaOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProvisioningQuotasResponseOut"])
    types["VolumeSnapshotIn"] = t.struct(
        {"name": t.string().optional(), "description": t.string().optional()}
    ).named(renames["VolumeSnapshotIn"])
    types["VolumeSnapshotOut"] = t.struct(
        {
            "storageVolume": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "type": t.string().optional(),
            "id": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeSnapshotOut"])
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
    types["ListNfsSharesResponseIn"] = t.struct(
        {
            "nfsShares": t.array(t.proxy(renames["NfsShareIn"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListNfsSharesResponseIn"])
    types["ListNfsSharesResponseOut"] = t.struct(
        {
            "nfsShares": t.array(t.proxy(renames["NfsShareOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNfsSharesResponseOut"])
    types["StartInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartInstanceRequestIn"]
    )
    types["StartInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartInstanceRequestOut"])
    types["ListInstancesResponseIn"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListInstancesResponseIn"])
    types["ListInstancesResponseOut"] = t.struct(
        {
            "instances": t.array(t.proxy(renames["InstanceOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListInstancesResponseOut"])
    types["RenameVolumeRequestIn"] = t.struct({"newVolumeId": t.string()}).named(
        renames["RenameVolumeRequestIn"]
    )
    types["RenameVolumeRequestOut"] = t.struct(
        {
            "newVolumeId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameVolumeRequestOut"])
    types["InstanceIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "machineType": t.string().optional(),
            "networkTemplate": t.string().optional(),
            "pod": t.string().optional(),
            "hyperthreadingEnabled": t.boolean().optional(),
            "osImage": t.string().optional(),
            "workloadProfile": t.string().optional(),
            "logicalInterfaces": t.array(
                t.proxy(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceIn"])
            ).optional(),
            "luns": t.array(t.proxy(renames["LunIn"])).optional(),
            "name": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
        }
    ).named(renames["InstanceIn"])
    types["InstanceOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "machineType": t.string().optional(),
            "networkTemplate": t.string().optional(),
            "state": t.string().optional(),
            "pod": t.string().optional(),
            "hyperthreadingEnabled": t.boolean().optional(),
            "osImage": t.string().optional(),
            "workloadProfile": t.string().optional(),
            "interactiveSerialConsoleEnabled": t.boolean().optional(),
            "id": t.string().optional(),
            "logicalInterfaces": t.array(
                t.proxy(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceOut"])
            ).optional(),
            "luns": t.array(t.proxy(renames["LunOut"])).optional(),
            "loginInfo": t.string().optional(),
            "networks": t.array(t.proxy(renames["NetworkOut"])).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "firmwareVersion": t.string().optional(),
            "name": t.string().optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceOut"])
    types["InstanceQuotaIn"] = t.struct(
        {
            "availableMachineCount": t.integer().optional(),
            "instanceType": t.string().optional(),
            "location": t.string().optional(),
            "gcpService": t.string().optional(),
        }
    ).named(renames["InstanceQuotaIn"])
    types["InstanceQuotaOut"] = t.struct(
        {
            "name": t.string().optional(),
            "availableMachineCount": t.integer().optional(),
            "instanceType": t.string().optional(),
            "location": t.string().optional(),
            "gcpService": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceQuotaOut"])
    types["ResizeVolumeRequestIn"] = t.struct({"sizeGib": t.string().optional()}).named(
        renames["ResizeVolumeRequestIn"]
    )
    types["ResizeVolumeRequestOut"] = t.struct(
        {
            "sizeGib": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResizeVolumeRequestOut"])
    types["NetworkConfigIn"] = t.struct(
        {
            "id": t.string().optional(),
            "serviceCidr": t.string().optional(),
            "gcpService": t.string().optional(),
            "vlanSameProject": t.boolean().optional(),
            "userNote": t.string().optional(),
            "cidr": t.string().optional(),
            "jumboFramesEnabled": t.boolean().optional(),
            "vlanAttachments": t.array(
                t.proxy(renames["IntakeVlanAttachmentIn"])
            ).optional(),
            "type": t.string().optional(),
            "bandwidth": t.string().optional(),
        }
    ).named(renames["NetworkConfigIn"])
    types["NetworkConfigOut"] = t.struct(
        {
            "id": t.string().optional(),
            "serviceCidr": t.string().optional(),
            "gcpService": t.string().optional(),
            "vlanSameProject": t.boolean().optional(),
            "userNote": t.string().optional(),
            "cidr": t.string().optional(),
            "jumboFramesEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "vlanAttachments": t.array(
                t.proxy(renames["IntakeVlanAttachmentOut"])
            ).optional(),
            "type": t.string().optional(),
            "bandwidth": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkConfigOut"])
    types["GoogleCloudBaremetalsolutionV2LogicalInterfaceIn"] = t.struct(
        {
            "logicalNetworkInterfaces": t.array(
                t.proxy(renames["LogicalNetworkInterfaceIn"])
            ).optional(),
            "interfaceIndex": t.integer().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceIn"])
    types["GoogleCloudBaremetalsolutionV2LogicalInterfaceOut"] = t.struct(
        {
            "logicalNetworkInterfaces": t.array(
                t.proxy(renames["LogicalNetworkInterfaceOut"])
            ).optional(),
            "interfaceIndex": t.integer().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceOut"])
    types["StartInstanceResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StartInstanceResponseIn"]
    )
    types["StartInstanceResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StartInstanceResponseOut"])
    types["SubmitProvisioningConfigRequestIn"] = t.struct(
        {
            "provisioningConfig": t.proxy(renames["ProvisioningConfigIn"]),
            "email": t.string().optional(),
        }
    ).named(renames["SubmitProvisioningConfigRequestIn"])
    types["SubmitProvisioningConfigRequestOut"] = t.struct(
        {
            "provisioningConfig": t.proxy(renames["ProvisioningConfigOut"]),
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SubmitProvisioningConfigRequestOut"])
    types["ListSSHKeysResponseIn"] = t.struct(
        {
            "sshKeys": t.array(t.proxy(renames["SSHKeyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListSSHKeysResponseIn"])
    types["ListSSHKeysResponseOut"] = t.struct(
        {
            "sshKeys": t.array(t.proxy(renames["SSHKeyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListSSHKeysResponseOut"])
    types["ResetInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ResetInstanceRequestIn"]
    )
    types["ResetInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetInstanceRequestOut"])
    types["VolumeIn"] = t.struct(
        {
            "currentSizeGib": t.string().optional(),
            "workloadProfile": t.string().optional(),
            "remainingSpaceGib": t.string().optional(),
            "originallyRequestedSizeGib": t.string().optional(),
            "snapshotSchedulePolicy": t.string().optional(),
            "storageAggregatePool": t.string().optional(),
            "performanceTier": t.string().optional(),
            "snapshotAutoDeleteBehavior": t.string().optional(),
            "autoGrownSizeGib": t.string().optional(),
            "pod": t.string().optional(),
            "requestedSizeGib": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "storageType": t.string().optional(),
            "notes": t.string().optional(),
            "emergencySizeGib": t.string().optional(),
            "maxSizeGib": t.string().optional(),
            "state": t.string().optional(),
            "snapshotEnabled": t.boolean().optional(),
            "id": t.string().optional(),
            "snapshotReservationDetail": t.proxy(
                renames["SnapshotReservationDetailIn"]
            ).optional(),
        }
    ).named(renames["VolumeIn"])
    types["VolumeOut"] = t.struct(
        {
            "currentSizeGib": t.string().optional(),
            "workloadProfile": t.string().optional(),
            "expireTime": t.string().optional(),
            "remainingSpaceGib": t.string().optional(),
            "originallyRequestedSizeGib": t.string().optional(),
            "snapshotSchedulePolicy": t.string().optional(),
            "storageAggregatePool": t.string().optional(),
            "performanceTier": t.string().optional(),
            "snapshotAutoDeleteBehavior": t.string().optional(),
            "attached": t.boolean().optional(),
            "protocol": t.string().optional(),
            "autoGrownSizeGib": t.string().optional(),
            "bootVolume": t.boolean().optional(),
            "pod": t.string().optional(),
            "requestedSizeGib": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "storageType": t.string().optional(),
            "notes": t.string().optional(),
            "name": t.string().optional(),
            "emergencySizeGib": t.string().optional(),
            "maxSizeGib": t.string().optional(),
            "state": t.string().optional(),
            "snapshotEnabled": t.boolean().optional(),
            "instances": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "snapshotReservationDetail": t.proxy(
                renames["SnapshotReservationDetailOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeOut"])
    types["ListNetworkUsageResponseIn"] = t.struct(
        {"networks": t.array(t.proxy(renames["NetworkUsageIn"])).optional()}
    ).named(renames["ListNetworkUsageResponseIn"])
    types["ListNetworkUsageResponseOut"] = t.struct(
        {
            "networks": t.array(t.proxy(renames["NetworkUsageOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListNetworkUsageResponseOut"])
    types["ListLunsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "luns": t.array(t.proxy(renames["LunIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(renames["ListLunsResponseIn"])
    types["ListLunsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "luns": t.array(t.proxy(renames["LunOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLunsResponseOut"])
    types["EvictLunRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EvictLunRequestIn"]
    )
    types["EvictLunRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EvictLunRequestOut"])
    types["DisableInteractiveSerialConsoleRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DisableInteractiveSerialConsoleRequestIn"])
    types["DisableInteractiveSerialConsoleRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DisableInteractiveSerialConsoleRequestOut"])
    types["NetworkIn"] = t.struct(
        {
            "type": t.string().optional(),
            "vlanId": t.string().optional(),
            "cidr": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "ipAddress": t.string().optional(),
            "state": t.string().optional(),
            "reservations": t.array(
                t.proxy(renames["NetworkAddressReservationIn"])
            ).optional(),
            "servicesCidr": t.string().optional(),
            "vrf": t.proxy(renames["VRFIn"]).optional(),
            "id": t.string().optional(),
            "jumboFramesEnabled": t.boolean().optional(),
            "macAddress": t.array(t.string()).optional(),
            "mountPoints": t.array(t.proxy(renames["NetworkMountPointIn"])).optional(),
        }
    ).named(renames["NetworkIn"])
    types["NetworkOut"] = t.struct(
        {
            "type": t.string().optional(),
            "vlanId": t.string().optional(),
            "cidr": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "ipAddress": t.string().optional(),
            "state": t.string().optional(),
            "gatewayIp": t.string().optional(),
            "reservations": t.array(
                t.proxy(renames["NetworkAddressReservationOut"])
            ).optional(),
            "servicesCidr": t.string().optional(),
            "vrf": t.proxy(renames["VRFOut"]).optional(),
            "id": t.string().optional(),
            "jumboFramesEnabled": t.boolean().optional(),
            "name": t.string().optional(),
            "pod": t.string().optional(),
            "macAddress": t.array(t.string()).optional(),
            "mountPoints": t.array(t.proxy(renames["NetworkMountPointOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkOut"])
    types["VolumeConfigIn"] = t.struct(
        {
            "storageAggregatePool": t.string().optional(),
            "snapshotsEnabled": t.boolean().optional(),
            "machineIds": t.array(t.string()).optional(),
            "performanceTier": t.string().optional(),
            "nfsExports": t.array(t.proxy(renames["NfsExportIn"])).optional(),
            "gcpService": t.string().optional(),
            "lunRanges": t.array(t.proxy(renames["LunRangeIn"])).optional(),
            "type": t.string().optional(),
            "protocol": t.string().optional(),
            "userNote": t.string().optional(),
            "id": t.string().optional(),
            "sizeGb": t.integer().optional(),
        }
    ).named(renames["VolumeConfigIn"])
    types["VolumeConfigOut"] = t.struct(
        {
            "storageAggregatePool": t.string().optional(),
            "snapshotsEnabled": t.boolean().optional(),
            "machineIds": t.array(t.string()).optional(),
            "performanceTier": t.string().optional(),
            "name": t.string().optional(),
            "nfsExports": t.array(t.proxy(renames["NfsExportOut"])).optional(),
            "gcpService": t.string().optional(),
            "lunRanges": t.array(t.proxy(renames["LunRangeOut"])).optional(),
            "type": t.string().optional(),
            "protocol": t.string().optional(),
            "userNote": t.string().optional(),
            "id": t.string().optional(),
            "sizeGb": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VolumeConfigOut"])
    types["LunIn"] = t.struct(
        {
            "storageType": t.string().optional(),
            "multiprotocolType": t.string().optional(),
            "id": t.string().optional(),
            "wwid": t.string().optional(),
            "state": t.string().optional(),
            "shareable": t.boolean().optional(),
            "sizeGb": t.string().optional(),
            "bootLun": t.boolean().optional(),
            "storageVolume": t.string().optional(),
        }
    ).named(renames["LunIn"])
    types["LunOut"] = t.struct(
        {
            "storageType": t.string().optional(),
            "multiprotocolType": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "wwid": t.string().optional(),
            "state": t.string().optional(),
            "instances": t.array(t.string()).optional(),
            "shareable": t.boolean().optional(),
            "expireTime": t.string().optional(),
            "sizeGb": t.string().optional(),
            "bootLun": t.boolean().optional(),
            "storageVolume": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LunOut"])
    types["RenameNetworkRequestIn"] = t.struct({"newNetworkId": t.string()}).named(
        renames["RenameNetworkRequestIn"]
    )
    types["RenameNetworkRequestOut"] = t.struct(
        {
            "newNetworkId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameNetworkRequestOut"])
    types["RenameNfsShareRequestIn"] = t.struct({"newNfsshareId": t.string()}).named(
        renames["RenameNfsShareRequestIn"]
    )
    types["RenameNfsShareRequestOut"] = t.struct(
        {
            "newNfsshareId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameNfsShareRequestOut"])
    types["NetworkMountPointIn"] = t.struct(
        {
            "logicalInterface": t.string().optional(),
            "ipAddress": t.string().optional(),
            "defaultGateway": t.boolean().optional(),
            "instance": t.string().optional(),
        }
    ).named(renames["NetworkMountPointIn"])
    types["NetworkMountPointOut"] = t.struct(
        {
            "logicalInterface": t.string().optional(),
            "ipAddress": t.string().optional(),
            "defaultGateway": t.boolean().optional(),
            "instance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NetworkMountPointOut"])
    types["RenameInstanceRequestIn"] = t.struct({"newInstanceId": t.string()}).named(
        renames["RenameInstanceRequestIn"]
    )
    types["RenameInstanceRequestOut"] = t.struct(
        {
            "newInstanceId": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RenameInstanceRequestOut"])
    types["ListVolumesResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "volumes": t.array(t.proxy(renames["VolumeIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListVolumesResponseIn"])
    types["ListVolumesResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "volumes": t.array(t.proxy(renames["VolumeOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListVolumesResponseOut"])
    types["InstanceConfigIn"] = t.struct(
        {
            "clientNetwork": t.proxy(renames["NetworkAddressIn"]).optional(),
            "hyperthreading": t.boolean().optional(),
            "osImage": t.string().optional(),
            "accountNetworksEnabled": t.boolean().optional(),
            "networkTemplate": t.string().optional(),
            "networkConfig": t.string().optional(),
            "logicalInterfaces": t.array(
                t.proxy(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceIn"])
            ).optional(),
            "instanceType": t.string().optional(),
            "id": t.string().optional(),
            "userNote": t.string().optional(),
            "privateNetwork": t.proxy(renames["NetworkAddressIn"]).optional(),
            "sshKeyNames": t.array(t.string()).optional(),
        }
    ).named(renames["InstanceConfigIn"])
    types["InstanceConfigOut"] = t.struct(
        {
            "clientNetwork": t.proxy(renames["NetworkAddressOut"]).optional(),
            "hyperthreading": t.boolean().optional(),
            "osImage": t.string().optional(),
            "accountNetworksEnabled": t.boolean().optional(),
            "networkTemplate": t.string().optional(),
            "networkConfig": t.string().optional(),
            "logicalInterfaces": t.array(
                t.proxy(renames["GoogleCloudBaremetalsolutionV2LogicalInterfaceOut"])
            ).optional(),
            "instanceType": t.string().optional(),
            "id": t.string().optional(),
            "name": t.string().optional(),
            "userNote": t.string().optional(),
            "privateNetwork": t.proxy(renames["NetworkAddressOut"]).optional(),
            "sshKeyNames": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InstanceConfigOut"])
    types["StopInstanceRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["StopInstanceRequestIn"]
    )
    types["StopInstanceRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["StopInstanceRequestOut"])
    types["AllowedClientIn"] = t.struct(
        {
            "noRootSquash": t.boolean().optional(),
            "allowDev": t.boolean().optional(),
            "mountPermissions": t.string().optional(),
            "network": t.string().optional(),
            "allowedClientsCidr": t.string().optional(),
            "allowSuid": t.boolean().optional(),
        }
    ).named(renames["AllowedClientIn"])
    types["AllowedClientOut"] = t.struct(
        {
            "noRootSquash": t.boolean().optional(),
            "allowDev": t.boolean().optional(),
            "mountPermissions": t.string().optional(),
            "shareIp": t.string().optional(),
            "network": t.string().optional(),
            "allowedClientsCidr": t.string().optional(),
            "allowSuid": t.boolean().optional(),
            "nfsPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllowedClientOut"])
    types["NfsExportIn"] = t.struct(
        {
            "allowDev": t.boolean().optional(),
            "machineId": t.string().optional(),
            "permissions": t.string().optional(),
            "networkId": t.string().optional(),
            "cidr": t.string().optional(),
            "allowSuid": t.boolean().optional(),
            "noRootSquash": t.boolean().optional(),
        }
    ).named(renames["NfsExportIn"])
    types["NfsExportOut"] = t.struct(
        {
            "allowDev": t.boolean().optional(),
            "machineId": t.string().optional(),
            "permissions": t.string().optional(),
            "networkId": t.string().optional(),
            "cidr": t.string().optional(),
            "allowSuid": t.boolean().optional(),
            "noRootSquash": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NfsExportOut"])
    types["EvictVolumeRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["EvictVolumeRequestIn"]
    )
    types["EvictVolumeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EvictVolumeRequestOut"])
    types["RestoreVolumeSnapshotRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["RestoreVolumeSnapshotRequestIn"])
    types["RestoreVolumeSnapshotRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RestoreVolumeSnapshotRequestOut"])

    functions = {}
    functions["projectsLocationsList"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSshKeysDelete"] = baremetalsolution.post(
        "v2/{parent}/sshKeys",
        t.struct(
            {
                "sshKeyId": t.string(),
                "parent": t.string(),
                "publicKey": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SSHKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSshKeysList"] = baremetalsolution.post(
        "v2/{parent}/sshKeys",
        t.struct(
            {
                "sshKeyId": t.string(),
                "parent": t.string(),
                "publicKey": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SSHKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsSshKeysCreate"] = baremetalsolution.post(
        "v2/{parent}/sshKeys",
        t.struct(
            {
                "sshKeyId": t.string(),
                "parent": t.string(),
                "publicKey": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SSHKeyOut"]),
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
    functions["projectsLocationsNfsSharesDelete"] = baremetalsolution.post(
        "v2/{parent}/nfsShares",
        t.struct(
            {
                "parent": t.string(),
                "requestedSizeGib": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "storageType": t.string().optional(),
                "name": t.string().optional(),
                "allowedClients": t.array(
                    t.proxy(renames["AllowedClientIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesRename"] = baremetalsolution.post(
        "v2/{parent}/nfsShares",
        t.struct(
            {
                "parent": t.string(),
                "requestedSizeGib": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "storageType": t.string().optional(),
                "name": t.string().optional(),
                "allowedClients": t.array(
                    t.proxy(renames["AllowedClientIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesPatch"] = baremetalsolution.post(
        "v2/{parent}/nfsShares",
        t.struct(
            {
                "parent": t.string(),
                "requestedSizeGib": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "storageType": t.string().optional(),
                "name": t.string().optional(),
                "allowedClients": t.array(
                    t.proxy(renames["AllowedClientIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesGet"] = baremetalsolution.post(
        "v2/{parent}/nfsShares",
        t.struct(
            {
                "parent": t.string(),
                "requestedSizeGib": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "storageType": t.string().optional(),
                "name": t.string().optional(),
                "allowedClients": t.array(
                    t.proxy(renames["AllowedClientIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesList"] = baremetalsolution.post(
        "v2/{parent}/nfsShares",
        t.struct(
            {
                "parent": t.string(),
                "requestedSizeGib": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "storageType": t.string().optional(),
                "name": t.string().optional(),
                "allowedClients": t.array(
                    t.proxy(renames["AllowedClientIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNfsSharesCreate"] = baremetalsolution.post(
        "v2/{parent}/nfsShares",
        t.struct(
            {
                "parent": t.string(),
                "requestedSizeGib": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "storageType": t.string().optional(),
                "name": t.string().optional(),
                "allowedClients": t.array(
                    t.proxy(renames["AllowedClientIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksList"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NetworkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksListNetworkUsage"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NetworkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksRename"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NetworkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksPatch"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NetworkOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsNetworksGet"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["NetworkOut"]),
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
    functions["projectsLocationsVolumesResize"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesEvict"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesPatch"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesList"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesRename"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["VolumeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsVolumesGet"] = baremetalsolution.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
                "name": t.string().optional(),
                "description": t.string().optional(),
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
                "name": t.string().optional(),
                "description": t.string().optional(),
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
                "name": t.string().optional(),
                "description": t.string().optional(),
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
                "name": t.string().optional(),
                "description": t.string().optional(),
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
                "name": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VolumeSnapshotOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningConfigsSubmit"] = baremetalsolution.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "email": t.string().optional(),
                "statusMessage": t.string().optional(),
                "instances": t.array(t.proxy(renames["InstanceConfigIn"])).optional(),
                "customId": t.string().optional(),
                "volumes": t.array(t.proxy(renames["VolumeConfigIn"])).optional(),
                "vpcScEnabled": t.boolean().optional(),
                "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
                "location": t.string().optional(),
                "handoverServiceAccount": t.string().optional(),
                "ticketId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProvisioningConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningConfigsCreate"] = baremetalsolution.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "email": t.string().optional(),
                "statusMessage": t.string().optional(),
                "instances": t.array(t.proxy(renames["InstanceConfigIn"])).optional(),
                "customId": t.string().optional(),
                "volumes": t.array(t.proxy(renames["VolumeConfigIn"])).optional(),
                "vpcScEnabled": t.boolean().optional(),
                "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
                "location": t.string().optional(),
                "handoverServiceAccount": t.string().optional(),
                "ticketId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProvisioningConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningConfigsGet"] = baremetalsolution.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "email": t.string().optional(),
                "statusMessage": t.string().optional(),
                "instances": t.array(t.proxy(renames["InstanceConfigIn"])).optional(),
                "customId": t.string().optional(),
                "volumes": t.array(t.proxy(renames["VolumeConfigIn"])).optional(),
                "vpcScEnabled": t.boolean().optional(),
                "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
                "location": t.string().optional(),
                "handoverServiceAccount": t.string().optional(),
                "ticketId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProvisioningConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningConfigsPatch"] = baremetalsolution.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "email": t.string().optional(),
                "statusMessage": t.string().optional(),
                "instances": t.array(t.proxy(renames["InstanceConfigIn"])).optional(),
                "customId": t.string().optional(),
                "volumes": t.array(t.proxy(renames["VolumeConfigIn"])).optional(),
                "vpcScEnabled": t.boolean().optional(),
                "networks": t.array(t.proxy(renames["NetworkConfigIn"])).optional(),
                "location": t.string().optional(),
                "handoverServiceAccount": t.string().optional(),
                "ticketId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ProvisioningConfigOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsProvisioningQuotasList"] = baremetalsolution.get(
        "v2/{parent}/provisioningQuotas",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListProvisioningQuotasResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="baremetalsolution",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
