from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_beyondcorp() -> Import:
    beyondcorp = HTTPRuntime("https://beyondcorp.googleapis.com/")

    renames = {
        "ErrorResponse": "_beyondcorp_1_ErrorResponse",
        "GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn": "_beyondcorp_2_GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut": "_beyondcorp_3_GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn": "_beyondcorp_4_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut": "_beyondcorp_5_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut",
        "GoogleLongrunningListOperationsResponseIn": "_beyondcorp_6_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_beyondcorp_7_GoogleLongrunningListOperationsResponseOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn": "_beyondcorp_8_CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut": "_beyondcorp_9_CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut",
        "CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn": "_beyondcorp_10_CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn",
        "CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut": "_beyondcorp_11_CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn": "_beyondcorp_12_GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut": "_beyondcorp_13_GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn": "_beyondcorp_14_GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut": "_beyondcorp_15_GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut",
        "EmptyIn": "_beyondcorp_16_EmptyIn",
        "EmptyOut": "_beyondcorp_17_EmptyOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn": "_beyondcorp_18_GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut": "_beyondcorp_19_GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn": "_beyondcorp_20_GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut": "_beyondcorp_21_GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut",
        "Tunnelv1ProtoTunnelerInfoIn": "_beyondcorp_22_Tunnelv1ProtoTunnelerInfoIn",
        "Tunnelv1ProtoTunnelerInfoOut": "_beyondcorp_23_Tunnelv1ProtoTunnelerInfoOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn": "_beyondcorp_24_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut": "_beyondcorp_25_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_beyondcorp_26_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_beyondcorp_27_GoogleIamV1TestIamPermissionsRequestOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn": "_beyondcorp_28_CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut": "_beyondcorp_29_CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn": "_beyondcorp_30_GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut": "_beyondcorp_31_GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut",
        "GoogleIamV1AuditConfigIn": "_beyondcorp_32_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_beyondcorp_33_GoogleIamV1AuditConfigOut",
        "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataIn": "_beyondcorp_34_GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataIn",
        "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut": "_beyondcorp_35_GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_beyondcorp_36_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_beyondcorp_37_GoogleIamV1TestIamPermissionsResponseOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn": "_beyondcorp_38_GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut": "_beyondcorp_39_GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut",
        "GoogleTypeExprIn": "_beyondcorp_40_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_beyondcorp_41_GoogleTypeExprOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn": "_beyondcorp_42_GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut": "_beyondcorp_43_GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn": "_beyondcorp_44_GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut": "_beyondcorp_45_GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut",
        "Tunnelv1ProtoTunnelerErrorIn": "_beyondcorp_46_Tunnelv1ProtoTunnelerErrorIn",
        "Tunnelv1ProtoTunnelerErrorOut": "_beyondcorp_47_Tunnelv1ProtoTunnelerErrorOut",
        "ListAppGatewaysResponseIn": "_beyondcorp_48_ListAppGatewaysResponseIn",
        "ListAppGatewaysResponseOut": "_beyondcorp_49_ListAppGatewaysResponseOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn": "_beyondcorp_50_CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut": "_beyondcorp_51_CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn": "_beyondcorp_52_GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut": "_beyondcorp_53_GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn": "_beyondcorp_54_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut": "_beyondcorp_55_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn": "_beyondcorp_56_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut": "_beyondcorp_57_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut",
        "GoogleLongrunningOperationIn": "_beyondcorp_58_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_beyondcorp_59_GoogleLongrunningOperationOut",
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn": "_beyondcorp_60_GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut": "_beyondcorp_61_GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn": "_beyondcorp_62_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut": "_beyondcorp_63_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut",
        "GoogleCloudLocationListLocationsResponseIn": "_beyondcorp_64_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_beyondcorp_65_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn": "_beyondcorp_66_GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut": "_beyondcorp_67_GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut",
        "AppGatewayOperationMetadataIn": "_beyondcorp_68_AppGatewayOperationMetadataIn",
        "AppGatewayOperationMetadataOut": "_beyondcorp_69_AppGatewayOperationMetadataOut",
        "GoogleIamV1PolicyIn": "_beyondcorp_70_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_beyondcorp_71_GoogleIamV1PolicyOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn": "_beyondcorp_72_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut": "_beyondcorp_73_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut",
        "GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn": "_beyondcorp_74_GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut": "_beyondcorp_75_GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut",
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn": "_beyondcorp_76_GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn",
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut": "_beyondcorp_77_GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut",
        "GoogleLongrunningCancelOperationRequestIn": "_beyondcorp_78_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_beyondcorp_79_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn": "_beyondcorp_80_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut": "_beyondcorp_81_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut",
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn": "_beyondcorp_82_GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut": "_beyondcorp_83_GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn": "_beyondcorp_84_GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut": "_beyondcorp_85_GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_beyondcorp_86_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_beyondcorp_87_GoogleIamV1SetIamPolicyRequestOut",
        "GoogleIamV1BindingIn": "_beyondcorp_88_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_beyondcorp_89_GoogleIamV1BindingOut",
        "GoogleCloudLocationLocationIn": "_beyondcorp_90_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_beyondcorp_91_GoogleCloudLocationLocationOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn": "_beyondcorp_92_GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut": "_beyondcorp_93_GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn": "_beyondcorp_94_GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut": "_beyondcorp_95_GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn": "_beyondcorp_96_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut": "_beyondcorp_97_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut",
        "GoogleRpcStatusIn": "_beyondcorp_98_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_beyondcorp_99_GoogleRpcStatusOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn": "_beyondcorp_100_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut": "_beyondcorp_101_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn": "_beyondcorp_102_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut": "_beyondcorp_103_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut",
        "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataIn": "_beyondcorp_104_GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut": "_beyondcorp_105_GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut",
        "GoogleIamV1AuditLogConfigIn": "_beyondcorp_106_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_beyondcorp_107_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn": "_beyondcorp_108_GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut": "_beyondcorp_109_GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn": "_beyondcorp_110_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut": "_beyondcorp_111_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut",
        "AllocatedConnectionIn": "_beyondcorp_112_AllocatedConnectionIn",
        "AllocatedConnectionOut": "_beyondcorp_113_AllocatedConnectionOut",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn": "_beyondcorp_114_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut": "_beyondcorp_115_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn": "_beyondcorp_116_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut": "_beyondcorp_117_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut",
        "AppGatewayIn": "_beyondcorp_118_AppGatewayIn",
        "AppGatewayOut": "_beyondcorp_119_AppGatewayOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn"] = t.struct(
        {
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "expectedConfigVersion": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut"] = t.struct(
        {
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "expectedConfigVersion": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn"
    ] = t.struct(
        {
            "appConnectionDetails": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn"
                    ]
                )
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut"
    ] = t.struct(
        {
            "appConnectionDetails": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut"
                    ]
                )
            ).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut"]
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
            "errorMsg": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut"
    ] = t.struct(
        {
            "errorMsg": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut"]
    )
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut"])
    types[
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut"
    ] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut"]
    )
    types["Tunnelv1ProtoTunnelerInfoIn"] = t.struct(
        {
            "latestErr": t.proxy(renames["Tunnelv1ProtoTunnelerErrorIn"]).optional(),
            "id": t.string().optional(),
            "latestRetryTime": t.string().optional(),
            "backoffRetryCount": t.integer().optional(),
            "totalRetryCount": t.integer().optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerInfoIn"])
    types["Tunnelv1ProtoTunnelerInfoOut"] = t.struct(
        {
            "latestErr": t.proxy(renames["Tunnelv1ProtoTunnelerErrorOut"]).optional(),
            "id": t.string().optional(),
            "latestRetryTime": t.string().optional(),
            "backoffRetryCount": t.integer().optional(),
            "totalRetryCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerInfoOut"])
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
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut"
        ]
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
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn"
    ] = t.struct(
        {
            "tunnelsPerGateway": t.integer().optional(),
            "applicationEndpoint": t.string().optional(),
            "applicationName": t.string().optional(),
            "gateway": t.array(
                t.proxy(
                    renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"]
                )
            ).optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "userPort": t.integer().optional(),
        }
    ).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn"]
    )
    types[
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut"
    ] = t.struct(
        {
            "tunnelsPerGateway": t.integer().optional(),
            "applicationEndpoint": t.string().optional(),
            "applicationName": t.string().optional(),
            "gateway": t.array(
                t.proxy(
                    renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"]
                )
            ).optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "userPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut"]
    )
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
    types["GoogleIamV1AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigIn"])
    types["GoogleIamV1AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigOut"])
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
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut"
        ]
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
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut"
        ]
    )
    types["GoogleTypeExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn"
    ] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
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
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
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
    types["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut"])
    types["Tunnelv1ProtoTunnelerErrorIn"] = t.struct(
        {"retryable": t.boolean().optional(), "err": t.string().optional()}
    ).named(renames["Tunnelv1ProtoTunnelerErrorIn"])
    types["Tunnelv1ProtoTunnelerErrorOut"] = t.struct(
        {
            "retryable": t.boolean().optional(),
            "err": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerErrorOut"])
    types["ListAppGatewaysResponseIn"] = t.struct(
        {
            "appGateways": t.array(t.proxy(renames["AppGatewayIn"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAppGatewaysResponseIn"])
    types["ListAppGatewaysResponseOut"] = t.struct(
        {
            "appGateways": t.array(t.proxy(renames["AppGatewayOut"])).optional(),
            "unreachable": t.array(t.string()).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAppGatewaysResponseOut"])
    types["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"] = t.struct(
        {
            "port": t.integer().optional(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "interface": t.string().optional(),
            "project": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"])
    types["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"] = t.struct(
        {
            "port": t.integer().optional(),
            "name": t.string().optional(),
            "zone": t.string().optional(),
            "interface": t.string().optional(),
            "project": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"])
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
    types["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn"] = t.struct(
        {
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
            ).optional(),
            "principalInfo": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                ]
            ),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "principalInfo": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut"
                ]
            ),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "state": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut"
        ]
    )
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
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut"]
    )
    types["AppGatewayOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppGatewayOperationMetadataIn"])
    types["AppGatewayOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppGatewayOperationMetadataOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
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
    types["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut"])
    types[
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut"]
    )
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
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
            "apiVersion": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut"
        ]
    )
    types["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn"] = t.struct(
        {
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut"] = t.struct(
        {
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut"])
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
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"] = t.struct(
        {
            "sub": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"])
            ).optional(),
            "id": t.string(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "time": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"] = t.struct(
        {
            "sub": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"])
            ).optional(),
            "id": t.string(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "time": t.string().optional(),
            "status": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"])
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
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "connectors": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "type": t.string(),
            "applicationEndpoint": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                ]
            ),
            "gateway": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "uid": t.string().optional(),
            "connectors": t.array(t.string()).optional(),
            "updateTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "type": t.string(),
            "state": t.string().optional(),
            "applicationEndpoint": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut"
                ]
            ),
            "gateway": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut"
    ] = t.struct(
        {
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut"]
    )
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
            "target": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut"
        ]
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
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn"
    ] = t.struct(
        {
            "notificationConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn"]
            ).optional(),
            "imageConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn"]
            ).optional(),
            "sequenceNumber": t.string(),
            "instanceConfig": t.struct({"_": t.string().optional()}).optional(),
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
            "imageConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut"]
            ).optional(),
            "sequenceNumber": t.string(),
            "instanceConfig": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut"]
    )
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
    types["AppGatewayIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "hostType": t.string(),
            "name": t.string(),
            "type": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AppGatewayIn"])
    types["AppGatewayOut"] = t.struct(
        {
            "allocatedConnections": t.array(
                t.proxy(renames["AllocatedConnectionOut"])
            ).optional(),
            "uid": t.string().optional(),
            "updateTime": t.string().optional(),
            "state": t.string().optional(),
            "uri": t.string().optional(),
            "displayName": t.string().optional(),
            "hostType": t.string(),
            "name": t.string(),
            "createTime": t.string().optional(),
            "type": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppGatewayOut"])

    functions = {}
    functions["projectsLocationsGet"] = beyondcorp.get(
        "v1/{name}/locations",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudLocationListLocationsResponseOut"]),
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
    functions[
        "projectsLocationsClientConnectorServicesTestIamPermissions"
    ] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientConnectorServicesSetIamPolicy"] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsClientGatewaysSetIamPolicy"] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = beyondcorp.post(
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
    functions["projectsLocationsOperationsGet"] = beyondcorp.post(
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
    functions["projectsLocationsOperationsDelete"] = beyondcorp.post(
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
    functions["projectsLocationsOperationsCancel"] = beyondcorp.post(
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
    functions["projectsLocationsAppConnectionsCreate"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "displayName": t.string().optional(),
                "connectors": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string(),
                "applicationEndpoint": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                    ]
                ),
                "gateway": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsGet"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "displayName": t.string().optional(),
                "connectors": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string(),
                "applicationEndpoint": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                    ]
                ),
                "gateway": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsTestIamPermissions"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "displayName": t.string().optional(),
                "connectors": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string(),
                "applicationEndpoint": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                    ]
                ),
                "gateway": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsResolve"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "displayName": t.string().optional(),
                "connectors": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string(),
                "applicationEndpoint": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                    ]
                ),
                "gateway": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsDelete"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "displayName": t.string().optional(),
                "connectors": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string(),
                "applicationEndpoint": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                    ]
                ),
                "gateway": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsSetIamPolicy"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "displayName": t.string().optional(),
                "connectors": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string(),
                "applicationEndpoint": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                    ]
                ),
                "gateway": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsList"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "displayName": t.string().optional(),
                "connectors": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string(),
                "applicationEndpoint": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                    ]
                ),
                "gateway": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsGetIamPolicy"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "displayName": t.string().optional(),
                "connectors": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string(),
                "applicationEndpoint": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                    ]
                ),
                "gateway": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsPatch"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "requestId": t.string().optional(),
                "updateMask": t.string(),
                "allowMissing": t.boolean().optional(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "displayName": t.string().optional(),
                "connectors": t.array(t.string()).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "type": t.string(),
                "applicationEndpoint": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                    ]
                ),
                "gateway": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"
                    ]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsGlobalTenantsTestIamPermissions"] = beyondcorp.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
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
                "resource": t.string().optional(),
                "options.requestedPolicyVersion": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleIamV1PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "organizationsLocationsGlobalTenantsProxyConfigsTestIamPermissions"
    ] = beyondcorp.post(
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
    functions[
        "organizationsLocationsGlobalTenantsProxyConfigsGetIamPolicy"
    ] = beyondcorp.post(
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
    functions[
        "organizationsLocationsGlobalTenantsProxyConfigsSetIamPolicy"
    ] = beyondcorp.post(
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

    return Import(
        importer="beyondcorp", renames=renames, types=types, functions=functions
    )
