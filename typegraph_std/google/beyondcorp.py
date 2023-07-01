from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_beyondcorp():
    beyondcorp = HTTPRuntime("https://beyondcorp.googleapis.com/")

    renames = {
        "ErrorResponse": "_beyondcorp_1_ErrorResponse",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn": "_beyondcorp_2_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut": "_beyondcorp_3_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut",
        "GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn": "_beyondcorp_4_GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut": "_beyondcorp_5_GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn": "_beyondcorp_6_GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut": "_beyondcorp_7_GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut",
        "GoogleTypeExprIn": "_beyondcorp_8_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_beyondcorp_9_GoogleTypeExprOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn": "_beyondcorp_10_GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut": "_beyondcorp_11_GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn": "_beyondcorp_12_CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut": "_beyondcorp_13_CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut",
        "AppGatewayIn": "_beyondcorp_14_AppGatewayIn",
        "AppGatewayOut": "_beyondcorp_15_AppGatewayOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn": "_beyondcorp_16_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut": "_beyondcorp_17_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut",
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn": "_beyondcorp_18_GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut": "_beyondcorp_19_GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn": "_beyondcorp_20_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut": "_beyondcorp_21_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn": "_beyondcorp_22_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut": "_beyondcorp_23_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut",
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn": "_beyondcorp_24_GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut": "_beyondcorp_25_GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut",
        "Tunnelv1ProtoTunnelerInfoIn": "_beyondcorp_26_Tunnelv1ProtoTunnelerInfoIn",
        "Tunnelv1ProtoTunnelerInfoOut": "_beyondcorp_27_Tunnelv1ProtoTunnelerInfoOut",
        "GoogleLongrunningListOperationsResponseIn": "_beyondcorp_28_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_beyondcorp_29_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn": "_beyondcorp_30_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut": "_beyondcorp_31_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut",
        "GoogleCloudLocationListLocationsResponseIn": "_beyondcorp_32_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_beyondcorp_33_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn": "_beyondcorp_34_GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut": "_beyondcorp_35_GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut",
        "GoogleIamV1AuditConfigIn": "_beyondcorp_36_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_beyondcorp_37_GoogleIamV1AuditConfigOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn": "_beyondcorp_38_CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut": "_beyondcorp_39_CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut",
        "GoogleIamV1PolicyIn": "_beyondcorp_40_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_beyondcorp_41_GoogleIamV1PolicyOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn": "_beyondcorp_42_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut": "_beyondcorp_43_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn": "_beyondcorp_44_GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut": "_beyondcorp_45_GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_beyondcorp_46_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_beyondcorp_47_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn": "_beyondcorp_48_GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut": "_beyondcorp_49_GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn": "_beyondcorp_50_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut": "_beyondcorp_51_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn": "_beyondcorp_52_CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut": "_beyondcorp_53_CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut",
        "GoogleRpcStatusIn": "_beyondcorp_54_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_beyondcorp_55_GoogleRpcStatusOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_beyondcorp_56_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_beyondcorp_57_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn": "_beyondcorp_58_GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut": "_beyondcorp_59_GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn": "_beyondcorp_60_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut": "_beyondcorp_61_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut",
        "Tunnelv1ProtoTunnelerErrorIn": "_beyondcorp_62_Tunnelv1ProtoTunnelerErrorIn",
        "Tunnelv1ProtoTunnelerErrorOut": "_beyondcorp_63_Tunnelv1ProtoTunnelerErrorOut",
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn": "_beyondcorp_64_GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn",
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut": "_beyondcorp_65_GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn": "_beyondcorp_66_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut": "_beyondcorp_67_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut",
        "GoogleLongrunningCancelOperationRequestIn": "_beyondcorp_68_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_beyondcorp_69_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn": "_beyondcorp_70_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut": "_beyondcorp_71_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut",
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn": "_beyondcorp_72_GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut": "_beyondcorp_73_GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn": "_beyondcorp_74_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut": "_beyondcorp_75_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut",
        "AppGatewayOperationMetadataIn": "_beyondcorp_76_AppGatewayOperationMetadataIn",
        "AppGatewayOperationMetadataOut": "_beyondcorp_77_AppGatewayOperationMetadataOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn": "_beyondcorp_78_GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut": "_beyondcorp_79_GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut",
        "GoogleLongrunningOperationIn": "_beyondcorp_80_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_beyondcorp_81_GoogleLongrunningOperationOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn": "_beyondcorp_82_GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut": "_beyondcorp_83_GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn": "_beyondcorp_84_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut": "_beyondcorp_85_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut",
        "AllocatedConnectionIn": "_beyondcorp_86_AllocatedConnectionIn",
        "AllocatedConnectionOut": "_beyondcorp_87_AllocatedConnectionOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_beyondcorp_88_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_beyondcorp_89_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleIamV1AuditLogConfigIn": "_beyondcorp_90_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_beyondcorp_91_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn": "_beyondcorp_92_GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut": "_beyondcorp_93_GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut",
        "GoogleIamV1BindingIn": "_beyondcorp_94_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_beyondcorp_95_GoogleIamV1BindingOut",
        "EmptyIn": "_beyondcorp_96_EmptyIn",
        "EmptyOut": "_beyondcorp_97_EmptyOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn": "_beyondcorp_98_GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut": "_beyondcorp_99_GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn": "_beyondcorp_100_GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut": "_beyondcorp_101_GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn": "_beyondcorp_102_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut": "_beyondcorp_103_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut",
        "GoogleCloudLocationLocationIn": "_beyondcorp_104_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_beyondcorp_105_GoogleCloudLocationLocationOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn": "_beyondcorp_106_GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut": "_beyondcorp_107_GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut",
        "CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn": "_beyondcorp_108_CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn",
        "CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut": "_beyondcorp_109_CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn": "_beyondcorp_110_GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut": "_beyondcorp_111_GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn": "_beyondcorp_112_GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut": "_beyondcorp_113_GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut",
        "ListAppGatewaysResponseIn": "_beyondcorp_114_ListAppGatewaysResponseIn",
        "ListAppGatewaysResponseOut": "_beyondcorp_115_ListAppGatewaysResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string(),
            "principalInfo": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                ]
            ),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string(),
            "principalInfo": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut"
                ]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn"
    ] = t.struct(
        {
            "appConnections": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"])
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut"
    ] = t.struct(
        {
            "appConnections": t.array(
                t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]
                )
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut"]
    )
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
    types["AppGatewayIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string(),
            "type": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hostType": t.string(),
        }
    ).named(renames["AppGatewayIn"])
    types["AppGatewayOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "uri": t.string().optional(),
            "name": t.string(),
            "state": t.string().optional(),
            "type": t.string(),
            "uid": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "hostType": t.string(),
            "allocatedConnections": t.array(
                t.proxy(renames["AllocatedConnectionOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppGatewayOut"])
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
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut"
        ]
    )
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
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut"
        ]
    )
    types["Tunnelv1ProtoTunnelerInfoIn"] = t.struct(
        {
            "backoffRetryCount": t.integer().optional(),
            "id": t.string().optional(),
            "latestErr": t.proxy(renames["Tunnelv1ProtoTunnelerErrorIn"]).optional(),
            "totalRetryCount": t.integer().optional(),
            "latestRetryTime": t.string().optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerInfoIn"])
    types["Tunnelv1ProtoTunnelerInfoOut"] = t.struct(
        {
            "backoffRetryCount": t.integer().optional(),
            "id": t.string().optional(),
            "latestErr": t.proxy(renames["Tunnelv1ProtoTunnelerErrorOut"]).optional(),
            "totalRetryCount": t.integer().optional(),
            "latestRetryTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerInfoOut"])
    types["GoogleLongrunningListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseIn"])
    types["GoogleLongrunningListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(
                t.proxy(renames["GoogleLongrunningOperationOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningListOperationsResponseOut"])
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
    types["GoogleCloudLocationListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseIn"])
    types["GoogleCloudLocationListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(
                t.proxy(renames["GoogleCloudLocationLocationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationListLocationsResponseOut"])
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
    types[
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn"
    ] = t.struct(
        {
            "gateway": t.array(
                t.proxy(
                    renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"]
                )
            ).optional(),
            "name": t.string().optional(),
            "applicationName": t.string().optional(),
            "userPort": t.integer().optional(),
            "tunnelsPerGateway": t.integer().optional(),
            "project": t.string().optional(),
            "applicationEndpoint": t.string().optional(),
        }
    ).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn"]
    )
    types[
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut"
    ] = t.struct(
        {
            "gateway": t.array(
                t.proxy(
                    renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"]
                )
            ).optional(),
            "name": t.string().optional(),
            "applicationName": t.string().optional(),
            "userPort": t.integer().optional(),
            "tunnelsPerGateway": t.integer().optional(),
            "project": t.string().optional(),
            "applicationEndpoint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut"]
    )
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
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
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut"
    ] = t.struct(
        {
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut"]
    )
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"] = t.struct(
        {
            "status": t.string().optional(),
            "sub": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"])
            ).optional(),
            "id": t.string(),
            "time": t.string().optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"] = t.struct(
        {
            "status": t.string().optional(),
            "sub": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"])
            ).optional(),
            "id": t.string(),
            "time": t.string().optional(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut"
    ] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut"]
    )
    types["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"] = t.struct(
        {
            "interface": t.string().optional(),
            "name": t.string().optional(),
            "port": t.integer().optional(),
            "project": t.string().optional(),
            "zone": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"])
    types["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"] = t.struct(
        {
            "interface": t.string().optional(),
            "name": t.string().optional(),
            "port": t.integer().optional(),
            "project": t.string().optional(),
            "zone": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "requestId": t.string().optional(),
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
            ),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "requestId": t.string().optional(),
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"]
            ),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut"])
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
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut"
    ] = t.struct(
        {
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut"
        ]
    )
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn"
    ] = t.struct(
        {
            "appConnection": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"]
            ).optional(),
            "recentMigVms": t.array(t.string()).optional(),
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
            "appConnection": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"]
            ).optional(),
            "recentMigVms": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut"
        ]
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
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut"
        ]
    )
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"] = t.struct(
        {
            "type": t.string(),
            "gateway": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"]
            ).optional(),
            "connectors": t.array(t.string()).optional(),
            "applicationEndpoint": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                ]
            ),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"] = t.struct(
        {
            "state": t.string().optional(),
            "type": t.string(),
            "gateway": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"]
            ).optional(),
            "uid": t.string().optional(),
            "connectors": t.array(t.string()).optional(),
            "applicationEndpoint": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut"
                ]
            ),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"])
    types["AppGatewayOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppGatewayOperationMetadataIn"])
    types["AppGatewayOperationMetadataOut"] = t.struct(
        {
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppGatewayOperationMetadataOut"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut"
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
    types["AllocatedConnectionIn"] = t.struct(
        {"ingressPort": t.integer(), "pscUri": t.string()}
    ).named(renames["AllocatedConnectionIn"])
    types["AllocatedConnectionOut"] = t.struct(
        {
            "ingressPort": t.integer(),
            "pscUri": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AllocatedConnectionOut"])
    types["GoogleIamV1SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestIn"])
    types["GoogleIamV1SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1SetIamPolicyRequestOut"])
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
    types[
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut"]
    )
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn"] = t.struct(
        {
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut"] = t.struct(
        {
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn"] = t.struct(
        {"targetImage": t.string().optional(), "stableImage": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut"] = t.struct(
        {
            "targetImage": t.string().optional(),
            "stableImage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"] = t.struct(
        {"type": t.string(), "appGateway": t.string()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"] = t.struct(
        {
            "l7psc": t.string().optional(),
            "ingressPort": t.integer().optional(),
            "uri": t.string().optional(),
            "type": t.string(),
            "appGateway": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"])
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn"
    ] = t.struct(
        {
            "expectedConfigVersion": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "errorMsg": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
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
            "errorMsg": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut"]
    )
    types["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn"])
    types["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn"] = t.struct(
        {
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut"] = t.struct(
        {
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut"])
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
    types["ListAppGatewaysResponseIn"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "appGateways": t.array(t.proxy(renames["AppGatewayIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAppGatewaysResponseIn"])
    types["ListAppGatewaysResponseOut"] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "appGateways": t.array(t.proxy(renames["AppGatewayOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAppGatewaysResponseOut"])

    functions = {}
    functions["organizationsLocationsOperationsList"] = beyondcorp.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsCancel"] = beyondcorp.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsGet"] = beyondcorp.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsOperationsDelete"] = beyondcorp.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = beyondcorp.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudLocationListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = beyondcorp.get(
        "v1/{name}/locations",
        t.struct(
            {
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudLocationListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsCreate"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsResolve"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsList"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsDelete"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsGetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsTestIamPermissions"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsPatch"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsGet"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsSetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = beyondcorp.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = beyondcorp.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsCancel"] = beyondcorp.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = beyondcorp.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientGatewaysSetIamPolicy"] = beyondcorp.get(
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
    functions["projectsLocationsClientGatewaysTestIamPermissions"] = beyondcorp.get(
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
    functions["projectsLocationsClientGatewaysGetIamPolicy"] = beyondcorp.get(
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
    ] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientConnectorServicesGetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientConnectorServicesSetIamPolicy"] = beyondcorp.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysGetIamPolicy"] = beyondcorp.get(
        "v1/{parent}/appGateways",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppGatewaysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysSetIamPolicy"] = beyondcorp.get(
        "v1/{parent}/appGateways",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppGatewaysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysTestIamPermissions"] = beyondcorp.get(
        "v1/{parent}/appGateways",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppGatewaysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysGet"] = beyondcorp.get(
        "v1/{parent}/appGateways",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppGatewaysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysCreate"] = beyondcorp.get(
        "v1/{parent}/appGateways",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppGatewaysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysDelete"] = beyondcorp.get(
        "v1/{parent}/appGateways",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppGatewaysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysList"] = beyondcorp.get(
        "v1/{parent}/appGateways",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppGatewaysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsReportStatus"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsPatch"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsGet"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsGetIamPolicy"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsTestIamPermissions"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsSetIamPolicy"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsCreate"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsDelete"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsList"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsResolveInstanceConfig"] = beyondcorp.get(
        "v1/{appConnector}:resolveInstanceConfig",
        t.struct({"appConnector": t.string(), "auth": t.string().optional()}),
        t.proxy(
            renames[
                "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut"
            ]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="beyondcorp",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
