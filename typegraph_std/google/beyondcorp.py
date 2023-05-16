from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_beyondcorp() -> Import:
    beyondcorp = HTTPRuntime("https://beyondcorp.googleapis.com/")

    renames = {
        "ErrorResponse": "_beyondcorp_1_ErrorResponse",
        "GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn": "_beyondcorp_2_GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut": "_beyondcorp_3_GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn": "_beyondcorp_4_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut": "_beyondcorp_5_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn": "_beyondcorp_6_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut": "_beyondcorp_7_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut",
        "GoogleLongrunningListOperationsResponseIn": "_beyondcorp_8_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_beyondcorp_9_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn": "_beyondcorp_10_GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut": "_beyondcorp_11_GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn": "_beyondcorp_12_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut": "_beyondcorp_13_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn": "_beyondcorp_14_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut": "_beyondcorp_15_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn": "_beyondcorp_16_GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut": "_beyondcorp_17_GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_beyondcorp_18_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_beyondcorp_19_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn": "_beyondcorp_20_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut": "_beyondcorp_21_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut",
        "GoogleIamV1AuditLogConfigIn": "_beyondcorp_22_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_beyondcorp_23_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn": "_beyondcorp_24_GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut": "_beyondcorp_25_GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn": "_beyondcorp_26_CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut": "_beyondcorp_27_CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn": "_beyondcorp_28_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut": "_beyondcorp_29_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut",
        "GoogleCloudLocationLocationIn": "_beyondcorp_30_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_beyondcorp_31_GoogleCloudLocationLocationOut",
        "GoogleIamV1BindingIn": "_beyondcorp_32_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_beyondcorp_33_GoogleIamV1BindingOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn": "_beyondcorp_34_GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut": "_beyondcorp_35_GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn": "_beyondcorp_36_GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut": "_beyondcorp_37_GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut",
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn": "_beyondcorp_38_GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut": "_beyondcorp_39_GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut",
        "GoogleIamV1PolicyIn": "_beyondcorp_40_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_beyondcorp_41_GoogleIamV1PolicyOut",
        "Tunnelv1ProtoTunnelerInfoIn": "_beyondcorp_42_Tunnelv1ProtoTunnelerInfoIn",
        "Tunnelv1ProtoTunnelerInfoOut": "_beyondcorp_43_Tunnelv1ProtoTunnelerInfoOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn": "_beyondcorp_44_GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut": "_beyondcorp_45_GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut",
        "CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn": "_beyondcorp_46_CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn",
        "CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut": "_beyondcorp_47_CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn": "_beyondcorp_48_GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut": "_beyondcorp_49_GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn": "_beyondcorp_50_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut": "_beyondcorp_51_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut",
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn": "_beyondcorp_52_GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut": "_beyondcorp_53_GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut",
        "GoogleRpcStatusIn": "_beyondcorp_54_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_beyondcorp_55_GoogleRpcStatusOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn": "_beyondcorp_56_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut": "_beyondcorp_57_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn": "_beyondcorp_58_CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut": "_beyondcorp_59_CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut",
        "AppGatewayOperationMetadataIn": "_beyondcorp_60_AppGatewayOperationMetadataIn",
        "AppGatewayOperationMetadataOut": "_beyondcorp_61_AppGatewayOperationMetadataOut",
        "GoogleCloudLocationListLocationsResponseIn": "_beyondcorp_62_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_beyondcorp_63_GoogleCloudLocationListLocationsResponseOut",
        "AllocatedConnectionIn": "_beyondcorp_64_AllocatedConnectionIn",
        "AllocatedConnectionOut": "_beyondcorp_65_AllocatedConnectionOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn": "_beyondcorp_66_GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut": "_beyondcorp_67_GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn": "_beyondcorp_68_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut": "_beyondcorp_69_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut",
        "GoogleIamV1AuditConfigIn": "_beyondcorp_70_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_beyondcorp_71_GoogleIamV1AuditConfigOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn": "_beyondcorp_72_GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut": "_beyondcorp_73_GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn": "_beyondcorp_74_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut": "_beyondcorp_75_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut",
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn": "_beyondcorp_76_GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn",
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut": "_beyondcorp_77_GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn": "_beyondcorp_78_GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut": "_beyondcorp_79_GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut",
        "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataIn": "_beyondcorp_80_GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut": "_beyondcorp_81_GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut",
        "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataIn": "_beyondcorp_82_GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataIn",
        "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut": "_beyondcorp_83_GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut",
        "Tunnelv1ProtoTunnelerErrorIn": "_beyondcorp_84_Tunnelv1ProtoTunnelerErrorIn",
        "Tunnelv1ProtoTunnelerErrorOut": "_beyondcorp_85_Tunnelv1ProtoTunnelerErrorOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn": "_beyondcorp_86_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut": "_beyondcorp_87_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn": "_beyondcorp_88_CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut": "_beyondcorp_89_CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut",
        "GoogleLongrunningCancelOperationRequestIn": "_beyondcorp_90_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_beyondcorp_91_GoogleLongrunningCancelOperationRequestOut",
        "ListAppGatewaysResponseIn": "_beyondcorp_92_ListAppGatewaysResponseIn",
        "ListAppGatewaysResponseOut": "_beyondcorp_93_ListAppGatewaysResponseOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_beyondcorp_94_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_beyondcorp_95_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn": "_beyondcorp_96_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut": "_beyondcorp_97_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_beyondcorp_98_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_beyondcorp_99_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn": "_beyondcorp_100_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut": "_beyondcorp_101_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn": "_beyondcorp_102_GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut": "_beyondcorp_103_GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut",
        "EmptyIn": "_beyondcorp_104_EmptyIn",
        "EmptyOut": "_beyondcorp_105_EmptyOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn": "_beyondcorp_106_GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut": "_beyondcorp_107_GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut",
        "GoogleLongrunningOperationIn": "_beyondcorp_108_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_beyondcorp_109_GoogleLongrunningOperationOut",
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn": "_beyondcorp_110_GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut": "_beyondcorp_111_GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut",
        "AppGatewayIn": "_beyondcorp_112_AppGatewayIn",
        "AppGatewayOut": "_beyondcorp_113_AppGatewayOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn": "_beyondcorp_114_GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut": "_beyondcorp_115_GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut",
        "GoogleTypeExprIn": "_beyondcorp_116_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_beyondcorp_117_GoogleTypeExprOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn": "_beyondcorp_118_GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut": "_beyondcorp_119_GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn"] = t.struct(
        {
            "expectedConfigVersion": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut"] = t.struct(
        {
            "expectedConfigVersion": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn"
    ] = t.struct(
        {
            "recentMigVms": t.array(t.string()).optional(),
            "appConnection": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"]
            ).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut"
    ] = t.struct(
        {
            "recentMigVms": t.array(t.string()).optional(),
            "appConnection": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
    ] = t.struct({"host": t.string(), "port": t.integer()}).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut"
    ] = t.struct(
        {
            "host": t.string(),
            "port": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut"
        ]
    )
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn"] = t.struct(
        {
            "pubsubNotification": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut"] = t.struct(
        {
            "pubsubNotification": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"] = t.struct(
        {
            "type": t.string(),
            "name": t.string(),
            "gateway": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "connectors": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "applicationEndpoint": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                ]
            ),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"] = t.struct(
        {
            "type": t.string(),
            "name": t.string(),
            "gateway": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"]
            ).optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "connectors": t.array(t.string()).optional(),
            "displayName": t.string().optional(),
            "applicationEndpoint": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "appConnections": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "appConnections": t.array(
                t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut"]
    )
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut"
    ] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut"]
    )
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut"])
    types["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"] = t.struct(
        {
            "interface": t.string().optional(),
            "name": t.string().optional(),
            "port": t.integer().optional(),
            "project": t.string().optional(),
            "selfLink": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"])
    types["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"] = t.struct(
        {
            "interface": t.string().optional(),
            "name": t.string().optional(),
            "port": t.integer().optional(),
            "project": t.string().optional(),
            "selfLink": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn"
    ] = t.struct(
        {
            "notificationConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn"]
            ).optional(),
            "instanceConfig": t.struct({"_": t.string().optional()}).optional(),
            "imageConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn"]
            ).optional(),
            "sequenceNumber": t.string(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut"
    ] = t.struct(
        {
            "notificationConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut"]
            ).optional(),
            "instanceConfig": t.struct({"_": t.string().optional()}).optional(),
            "imageConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut"]
            ).optional(),
            "sequenceNumber": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut"]
    )
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types[
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut"
    ] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut"
    ] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut"
    ] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut"
        ]
    )
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["Tunnelv1ProtoTunnelerInfoIn"] = t.struct(
        {
            "totalRetryCount": t.integer().optional(),
            "backoffRetryCount": t.integer().optional(),
            "id": t.string().optional(),
            "latestRetryTime": t.string().optional(),
            "latestErr": t.proxy(renames["Tunnelv1ProtoTunnelerErrorIn"]).optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerInfoIn"])
    types["Tunnelv1ProtoTunnelerInfoOut"] = t.struct(
        {
            "totalRetryCount": t.integer().optional(),
            "backoffRetryCount": t.integer().optional(),
            "id": t.string().optional(),
            "latestRetryTime": t.string().optional(),
            "latestErr": t.proxy(renames["Tunnelv1ProtoTunnelerErrorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerInfoOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"] = t.struct(
        {
            "time": t.string().optional(),
            "sub": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"])
            ).optional(),
            "status": t.string().optional(),
            "id": t.string(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"] = t.struct(
        {
            "time": t.string().optional(),
            "sub": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"])
            ).optional(),
            "status": t.string().optional(),
            "id": t.string(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"])
    types["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn"])
    types["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn"
    ] = t.struct(
        {
            "expectedConfigVersion": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "currentConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut"
    ] = t.struct(
        {
            "expectedConfigVersion": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "currentConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "appConnectionDetails": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn"
                    ]
                )
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut"
    ] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "appConnectionDetails": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut"
                    ]
                )
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut"]
    )
    types[
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut"
    ] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut"]
    )
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"] = t.struct(
        {"type": t.string(), "appGateway": t.string()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"] = t.struct(
        {
            "type": t.string(),
            "ingressPort": t.integer().optional(),
            "l7psc": t.string().optional(),
            "uri": t.string().optional(),
            "appGateway": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"])
    types[
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn"]
    )
    types[
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut"]
    )
    types["AppGatewayOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppGatewayOperationMetadataIn"])
    types["AppGatewayOperationMetadataOut"] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppGatewayOperationMetadataOut"])
    types["GoogleCloudLocationListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseIn"])
    types["GoogleCloudLocationListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseOut"])
    types["AllocatedConnectionIn"] = t.struct(
        {"pscUri": t.string(), "ingressPort": t.integer()}
    ).named(renames["AllocatedConnectionIn"])
    types["AllocatedConnectionOut"] = t.struct(
        {
            "pscUri": t.string(),
            "ingressPort": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllocatedConnectionOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut"
        ]
    )
    types["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "principalInfo": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                ]
            ),
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "principalInfo": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut"
                ]
            ),
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut"])
    types["GoogleIamV1AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigIn"])
            ).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigIn"])
    types["GoogleIamV1AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn"] = t.struct(
        {"stableImage": t.string().optional(), "targetImage": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut"] = t.struct(
        {
            "stableImage": t.string().optional(),
            "targetImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn"
    ] = t.struct({"pubsubSubscription": t.string().optional()}).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut"
    ] = t.struct(
        {
            "pubsubSubscription": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut"]
    )
    types["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn"] = t.struct(
        {
            "errorMsg": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "currentConfigVersion": t.string().optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut"] = t.struct(
        {
            "errorMsg": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "currentConfigVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut"])
    types[
        "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut"
    ] = t.struct(
        {
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut"
        ]
    )
    types["Tunnelv1ProtoTunnelerErrorIn"] = t.struct(
        {"err": t.string().optional(), "retryable": t.boolean().optional()}
    ).named(renames["Tunnelv1ProtoTunnelerErrorIn"])
    types["Tunnelv1ProtoTunnelerErrorOut"] = t.struct(
        {
            "err": t.string().optional(),
            "retryable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerErrorOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn"
    ] = t.struct({"email": t.string().optional()}).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut"
    ] = t.struct(
        {
            "email": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut"
        ]
    )
    types[
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn"
    ] = t.struct(
        {
            "project": t.string().optional(),
            "name": t.string().optional(),
            "applicationName": t.string().optional(),
            "tunnelsPerGateway": t.integer().optional(),
            "applicationEndpoint": t.string().optional(),
            "gateway": t.array(
                t.proxy(
                    renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"]
                )
            ).optional(),
            "userPort": t.integer().optional(),
        }
    ).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn"]
    )
    types[
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut"
    ] = t.struct(
        {
            "project": t.string().optional(),
            "name": t.string().optional(),
            "applicationName": t.string().optional(),
            "tunnelsPerGateway": t.integer().optional(),
            "applicationEndpoint": t.string().optional(),
            "gateway": t.array(
                t.proxy(
                    renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"]
                )
            ).optional(),
            "userPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut"]
    )
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["ListAppGatewaysResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "appGateways": t.array(t.proxy(renames["AppGatewayIn"])).optional(),
        }
    ).named(renames["ListAppGatewaysResponseIn"])
    types["ListAppGatewaysResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "appGateways": t.array(t.proxy(renames["AppGatewayOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAppGatewaysResponseOut"])
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut"
        ]
    )
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"] = t.struct(
        {
            "serviceAccount": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn"
                ]
            ).optional()
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut"
    ] = t.struct(
        {
            "serviceAccount": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut"]
    )
    types["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn"] = t.struct(
        {
            "requestId": t.string().optional(),
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
            ),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut"] = t.struct(
        {
            "requestId": t.string().optional(),
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"]
            ),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types[
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn"
        ]
    )
    types[
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut"
        ]
    )
    types["AppGatewayIn"] = t.struct(
        {
            "name": t.string(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hostType": t.string(),
        }
    ).named(renames["AppGatewayIn"])
    types["AppGatewayOut"] = t.struct(
        {
            "name": t.string(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "uri": t.string().optional(),
            "allocatedConnections": t.array(
                t.proxy(renames["AllocatedConnectionOut"])
            ).optional(),
            "uid": t.string().optional(),
            "type": t.string(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "hostType": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppGatewayOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "appConnectors": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut"
    ] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "appConnectors": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut"]
    )
    types["GoogleTypeExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn"
    ] = t.struct(
        {
            "instanceConfig": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn"
                ]
            ).optional()
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
    ] = t.struct(
        {
            "instanceConfig": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut"
                ]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"]
    )

    functions = {}
    functions["projectsLocationsList"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudLocationLocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudLocationLocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsTestIamPermissions"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsDelete"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsPatch"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsList"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsResolve"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsCreate"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsGetIamPolicy"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsSetIamPolicy"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsGet"] = beyondcorp.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientGatewaysTestIamPermissions"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientGatewaysGetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientGatewaysSetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysGet"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysCreate"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysList"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysDelete"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysGetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysSetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysTestIamPermissions"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = beyondcorp.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = beyondcorp.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = beyondcorp.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = beyondcorp.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientConnectorServicesSetIamPolicy"] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsClientConnectorServicesTestIamPermissions"
    ] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientConnectorServicesGetIamPolicy"] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsReportStatus"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsDelete"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsSetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsList"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsPatch"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsGet"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsGetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsCreate"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsResolveInstanceConfig"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsTestIamPermissions"] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsGlobalTenantsTestIamPermissions"] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsGlobalTenantsSetIamPolicy"] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsGlobalTenantsGetIamPolicy"] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsGlobalTenantsProxyConfigsGetIamPolicy"
    ] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsGlobalTenantsProxyConfigsSetIamPolicy"
    ] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsGlobalTenantsProxyConfigsTestIamPermissions"
    ] = beyondcorp.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="beyondcorp",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
