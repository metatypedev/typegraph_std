from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_beyondcorp() -> Import:
    beyondcorp = HTTPRuntime("https://beyondcorp.googleapis.com/")

    renames = {
        "ErrorResponse": "_beyondcorp_1_ErrorResponse",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn": "_beyondcorp_2_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut": "_beyondcorp_3_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn": "_beyondcorp_4_GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut": "_beyondcorp_5_GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn": "_beyondcorp_6_GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut": "_beyondcorp_7_GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn": "_beyondcorp_8_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut": "_beyondcorp_9_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut",
        "GoogleIamV1SetIamPolicyRequestIn": "_beyondcorp_10_GoogleIamV1SetIamPolicyRequestIn",
        "GoogleIamV1SetIamPolicyRequestOut": "_beyondcorp_11_GoogleIamV1SetIamPolicyRequestOut",
        "ListAppGatewaysResponseIn": "_beyondcorp_12_ListAppGatewaysResponseIn",
        "ListAppGatewaysResponseOut": "_beyondcorp_13_ListAppGatewaysResponseOut",
        "Tunnelv1ProtoTunnelerErrorIn": "_beyondcorp_14_Tunnelv1ProtoTunnelerErrorIn",
        "Tunnelv1ProtoTunnelerErrorOut": "_beyondcorp_15_Tunnelv1ProtoTunnelerErrorOut",
        "GoogleIamV1TestIamPermissionsResponseIn": "_beyondcorp_16_GoogleIamV1TestIamPermissionsResponseIn",
        "GoogleIamV1TestIamPermissionsResponseOut": "_beyondcorp_17_GoogleIamV1TestIamPermissionsResponseOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn": "_beyondcorp_18_CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut": "_beyondcorp_19_CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut",
        "GoogleRpcStatusIn": "_beyondcorp_20_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_beyondcorp_21_GoogleRpcStatusOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn": "_beyondcorp_22_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut": "_beyondcorp_23_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn": "_beyondcorp_24_GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut": "_beyondcorp_25_GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponseOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn": "_beyondcorp_26_GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut": "_beyondcorp_27_GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn": "_beyondcorp_28_GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut": "_beyondcorp_29_GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut",
        "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataIn": "_beyondcorp_30_GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut": "_beyondcorp_31_GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut",
        "Tunnelv1ProtoTunnelerInfoIn": "_beyondcorp_32_Tunnelv1ProtoTunnelerInfoIn",
        "Tunnelv1ProtoTunnelerInfoOut": "_beyondcorp_33_Tunnelv1ProtoTunnelerInfoOut",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn": "_beyondcorp_34_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut": "_beyondcorp_35_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn": "_beyondcorp_36_CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut": "_beyondcorp_37_CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut",
        "AppGatewayIn": "_beyondcorp_38_AppGatewayIn",
        "AppGatewayOut": "_beyondcorp_39_AppGatewayOut",
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn": "_beyondcorp_40_GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut": "_beyondcorp_41_GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut",
        "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataIn": "_beyondcorp_42_GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataIn",
        "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut": "_beyondcorp_43_GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn": "_beyondcorp_44_GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut": "_beyondcorp_45_GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut",
        "GoogleLongrunningOperationIn": "_beyondcorp_46_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_beyondcorp_47_GoogleLongrunningOperationOut",
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn": "_beyondcorp_48_GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataIn",
        "GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut": "_beyondcorp_49_GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn": "_beyondcorp_50_GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut": "_beyondcorp_51_GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn": "_beyondcorp_52_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut": "_beyondcorp_53_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut",
        "CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn": "_beyondcorp_54_CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn",
        "CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut": "_beyondcorp_55_CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn": "_beyondcorp_56_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut": "_beyondcorp_57_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn": "_beyondcorp_58_GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut": "_beyondcorp_59_GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponseOut",
        "AllocatedConnectionIn": "_beyondcorp_60_AllocatedConnectionIn",
        "AllocatedConnectionOut": "_beyondcorp_61_AllocatedConnectionOut",
        "AppGatewayOperationMetadataIn": "_beyondcorp_62_AppGatewayOperationMetadataIn",
        "AppGatewayOperationMetadataOut": "_beyondcorp_63_AppGatewayOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn": "_beyondcorp_64_GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut": "_beyondcorp_65_GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn": "_beyondcorp_66_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut": "_beyondcorp_67_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn": "_beyondcorp_68_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut": "_beyondcorp_69_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut",
        "GoogleIamV1PolicyIn": "_beyondcorp_70_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_beyondcorp_71_GoogleIamV1PolicyOut",
        "GoogleLongrunningListOperationsResponseIn": "_beyondcorp_72_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_beyondcorp_73_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn": "_beyondcorp_74_GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn",
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut": "_beyondcorp_75_GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn": "_beyondcorp_76_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut": "_beyondcorp_77_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut",
        "GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn": "_beyondcorp_78_GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut": "_beyondcorp_79_GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut",
        "GoogleTypeExprIn": "_beyondcorp_80_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_beyondcorp_81_GoogleTypeExprOut",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn": "_beyondcorp_82_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn",
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut": "_beyondcorp_83_GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut",
        "GoogleIamV1AuditConfigIn": "_beyondcorp_84_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_beyondcorp_85_GoogleIamV1AuditConfigOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn": "_beyondcorp_86_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut": "_beyondcorp_87_GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn": "_beyondcorp_88_CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn",
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut": "_beyondcorp_89_CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut",
        "GoogleIamV1AuditLogConfigIn": "_beyondcorp_90_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_beyondcorp_91_GoogleIamV1AuditLogConfigOut",
        "EmptyIn": "_beyondcorp_92_EmptyIn",
        "EmptyOut": "_beyondcorp_93_EmptyOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn": "_beyondcorp_94_GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut": "_beyondcorp_95_GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut",
        "GoogleIamV1TestIamPermissionsRequestIn": "_beyondcorp_96_GoogleIamV1TestIamPermissionsRequestIn",
        "GoogleIamV1TestIamPermissionsRequestOut": "_beyondcorp_97_GoogleIamV1TestIamPermissionsRequestOut",
        "GoogleLongrunningCancelOperationRequestIn": "_beyondcorp_98_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_beyondcorp_99_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudLocationListLocationsResponseIn": "_beyondcorp_100_GoogleCloudLocationListLocationsResponseIn",
        "GoogleCloudLocationListLocationsResponseOut": "_beyondcorp_101_GoogleCloudLocationListLocationsResponseOut",
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn": "_beyondcorp_102_GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut": "_beyondcorp_103_GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut",
        "GoogleIamV1BindingIn": "_beyondcorp_104_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_beyondcorp_105_GoogleIamV1BindingOut",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn": "_beyondcorp_106_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountIn",
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut": "_beyondcorp_107_GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccountOut",
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn": "_beyondcorp_108_GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataIn",
        "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut": "_beyondcorp_109_GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut",
        "GoogleCloudLocationLocationIn": "_beyondcorp_110_GoogleCloudLocationLocationIn",
        "GoogleCloudLocationLocationOut": "_beyondcorp_111_GoogleCloudLocationLocationOut",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn": "_beyondcorp_112_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigIn",
        "GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut": "_beyondcorp_113_GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfigOut",
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn": "_beyondcorp_114_GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn",
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut": "_beyondcorp_115_GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut",
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn": "_beyondcorp_116_GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataIn",
        "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut": "_beyondcorp_117_GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut",
        "GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn": "_beyondcorp_118_GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn",
        "GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut": "_beyondcorp_119_GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn"] = t.struct(
        {
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "principalInfo": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                ]
            ),
            "name": t.string(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut"] = t.struct(
        {
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "principalInfo": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoOut"
                ]
            ),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOut"])
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
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadataOut"
        ]
    )
    types["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetailsOut"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"] = t.struct(
        {"appGateway": t.string(), "type": t.string()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"] = t.struct(
        {
            "appGateway": t.string(),
            "type": t.string(),
            "uri": t.string().optional(),
            "l7psc": t.string().optional(),
            "ingressPort": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"])
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
    types["GoogleIamV1TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsResponseIn"])
    types["GoogleIamV1TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsResponseOut"])
    types["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "selfLink": t.string().optional(),
            "interface": t.string().optional(),
            "port": t.integer().optional(),
        }
    ).named(renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"])
    types["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "selfLink": t.string().optional(),
            "interface": t.string().optional(),
            "port": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn"
    ] = t.struct(
        {
            "imageConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigIn"]
            ).optional(),
            "sequenceNumber": t.string(),
            "instanceConfig": t.struct({"_": t.string().optional()}).optional(),
            "notificationConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigIn"]
            ).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut"
    ] = t.struct(
        {
            "imageConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ImageConfigOut"]
            ).optional(),
            "sequenceNumber": t.string(),
            "instanceConfig": t.struct({"_": t.string().optional()}).optional(),
            "notificationConfig": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfigOut"]
    )
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
    types["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"] = t.struct(
        {
            "status": t.string().optional(),
            "time": t.string().optional(),
            "id": t.string(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "sub": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"] = t.struct(
        {
            "status": t.string().optional(),
            "time": t.string().optional(),
            "id": t.string(),
            "resource": t.struct({"_": t.string().optional()}).optional(),
            "sub": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetailsOut"])
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
            "requestedCancellation": t.boolean().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadataOut"
        ]
    )
    types["Tunnelv1ProtoTunnelerInfoIn"] = t.struct(
        {
            "totalRetryCount": t.integer().optional(),
            "id": t.string().optional(),
            "latestRetryTime": t.string().optional(),
            "backoffRetryCount": t.integer().optional(),
            "latestErr": t.proxy(renames["Tunnelv1ProtoTunnelerErrorIn"]).optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerInfoIn"])
    types["Tunnelv1ProtoTunnelerInfoOut"] = t.struct(
        {
            "totalRetryCount": t.integer().optional(),
            "id": t.string().optional(),
            "latestRetryTime": t.string().optional(),
            "backoffRetryCount": t.integer().optional(),
            "latestErr": t.proxy(renames["Tunnelv1ProtoTunnelerErrorOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["Tunnelv1ProtoTunnelerInfoOut"])
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
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn"
    ] = t.struct(
        {
            "applicationName": t.string().optional(),
            "applicationEndpoint": t.string().optional(),
            "tunnelsPerGateway": t.integer().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "userPort": t.integer().optional(),
            "gateway": t.array(
                t.proxy(
                    renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayIn"]
                )
            ).optional(),
        }
    ).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigIn"]
    )
    types[
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut"
    ] = t.struct(
        {
            "applicationName": t.string().optional(),
            "applicationEndpoint": t.string().optional(),
            "tunnelsPerGateway": t.integer().optional(),
            "name": t.string().optional(),
            "project": t.string().optional(),
            "userPort": t.integer().optional(),
            "gateway": t.array(
                t.proxy(
                    renames["CloudSecurityZerotrustApplinkAppConnectorProtoGatewayOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfigOut"]
    )
    types["AppGatewayIn"] = t.struct(
        {
            "type": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hostType": t.string(),
            "displayName": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["AppGatewayIn"])
    types["AppGatewayOut"] = t.struct(
        {
            "state": t.string().optional(),
            "type": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "hostType": t.string(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "allocatedConnections": t.array(
                t.proxy(renames["AllocatedConnectionOut"])
            ).optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string(),
            "uri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppGatewayOut"])
    types[
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut"
    ] = t.struct(
        {
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadataOut"]
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
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadataOut"
        ]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn"
    ] = t.struct(
        {
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "errorMsg": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut"
    ] = t.struct(
        {
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "errorMsg": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetailsOut"]
    )
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadataOut"]
    )
    types["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn"] = t.struct(
        {
            "errorMsg": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "expectedConfigVersion": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsIn"])
    types["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut"] = t.struct(
        {
            "errorMsg": t.string().optional(),
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "expectedConfigVersion": t.string().optional(),
            "currentConfigVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetailsOut"])
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut"
    ] = t.struct(
        {
            "requestedCancellation": t.boolean().optional(),
            "statusMessage": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadataOut"
        ]
    )
    types["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsIn"])
    types["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetailsOut"])
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
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadataOut"]
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
    types["AppGatewayOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AppGatewayOperationMetadataIn"])
    types["AppGatewayOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AppGatewayOperationMetadataOut"])
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
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn"
    ] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "appConnectionDetails": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsIn"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseIn"]
    )
    types[
        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut"
    ] = t.struct(
        {
            "unreachable": t.array(t.string()).optional(),
            "appConnectionDetails": t.array(
                t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetailsOut"
                    ]
                )
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseOut"]
    )
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
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
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataIn"]
    )
    types[
        "GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut"
    ] = t.struct(
        {
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadataOut"]
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
    types["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetailsOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"] = t.struct(
        {
            "connectors": t.array(t.string()).optional(),
            "name": t.string(),
            "displayName": t.string().optional(),
            "type": t.string(),
            "applicationEndpoint": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointIn"
                ]
            ),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gateway": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"])
    types["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "connectors": t.array(t.string()).optional(),
            "name": t.string(),
            "displayName": t.string().optional(),
            "type": t.string(),
            "applicationEndpoint": t.proxy(
                renames[
                    "GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpointOut"
                ]
            ),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "gateway": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGatewayOut"]
            ).optional(),
            "state": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOut"])
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
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn"
    ] = t.struct({"_": t.string().optional()}).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsIn"]
    )
    types[
        "CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut"
    ] = t.struct({"error": t.proxy(renames["ErrorResponse"]).optional()}).named(
        renames["CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetailsOut"]
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn"] = t.struct(
        {
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
            ),
            "requestId": t.string().optional(),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut"] = t.struct(
        {
            "resourceInfo": t.proxy(
                renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoOut"]
            ),
            "requestId": t.string().optional(),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequestOut"])
    types["GoogleIamV1TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["GoogleIamV1TestIamPermissionsRequestIn"])
    types["GoogleIamV1TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1TestIamPermissionsRequestOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
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
            "requestedCancellation": t.boolean().optional(),
            "apiVersion": t.string().optional(),
            "statusMessage": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadataOut"
        ]
    )
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
            "requestedCancellation": t.boolean().optional(),
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "endTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "createTime": t.string().optional(),
            "statusMessage": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadataOut"
        ]
    )
    types["GoogleCloudLocationLocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["GoogleCloudLocationLocationIn"])
    types["GoogleCloudLocationLocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudLocationLocationOut"])
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
        "GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseIn"
    ] = t.struct(
        {
            "appConnections": t.array(
                t.proxy(renames["GoogleCloudBeyondcorpAppconnectionsV1AppConnectionIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
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
            "nextPageToken": t.string().optional(),
            "unreachable": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponseOut"]
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
            "statusMessage": t.string().optional(),
            "requestedCancellation": t.boolean().optional(),
            "createTime": t.string().optional(),
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadataOut"
        ]
    )
    types["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn"] = t.struct(
        {
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsIn"])
    types["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut"] = t.struct(
        {
            "extendedStatus": t.struct({"_": t.string().optional()}).optional(),
            "currentConfigVersion": t.string().optional(),
            "expectedConfigVersion": t.string().optional(),
            "errorMsg": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetailsOut"])

    functions = {}
    functions["organizationsLocationsGlobalTenantsGetIamPolicy"] = beyondcorp.post(
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
    functions["organizationsLocationsGlobalTenantsSetIamPolicy"] = beyondcorp.post(
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
        "organizationsLocationsGlobalTenantsTestIamPermissions"
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
    functions[
        "organizationsLocationsGlobalTenantsProxyConfigsSetIamPolicy"
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
    functions[
        "organizationsLocationsGlobalTenantsProxyConfigsGetIamPolicy"
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
    functions["projectsLocationsAppConnectorsTestIamPermissions"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsCreate"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsReportStatus"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsDelete"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsSetIamPolicy"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsGet"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsResolveInstanceConfig"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsList"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsGetIamPolicy"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectorsPatch"] = beyondcorp.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "validateOnly": t.boolean().optional(),
                "name": t.string(),
                "requestId": t.string().optional(),
                "resourceInfo": t.proxy(
                    renames["GoogleCloudBeyondcorpAppconnectorsV1ResourceInfoIn"]
                ).optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "principalInfo": t.proxy(
                    renames[
                        "GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoIn"
                    ]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsDelete"] = beyondcorp.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = beyondcorp.get(
        "v1/{name}/operations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysTestIamPermissions"] = beyondcorp.get(
        "v1/{parent}/appGateways",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppGatewaysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppGatewaysGetIamPolicy"] = beyondcorp.get(
        "v1/{parent}/appGateways",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
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
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "parent": t.string(),
                "orderBy": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAppGatewaysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsAppConnectionsCreate"] = beyondcorp.post(
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
    functions["projectsLocationsAppConnectionsDelete"] = beyondcorp.post(
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
    functions["projectsLocationsAppConnectionsGetIamPolicy"] = beyondcorp.post(
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
    functions["projectsLocationsAppConnectionsGet"] = beyondcorp.post(
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
    functions["projectsLocationsAppConnectionsPatch"] = beyondcorp.post(
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
    functions["projectsLocationsAppConnectionsResolve"] = beyondcorp.post(
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
    functions["projectsLocationsAppConnectionsTestIamPermissions"] = beyondcorp.post(
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
    functions["projectsLocationsAppConnectionsList"] = beyondcorp.post(
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
    functions["projectsLocationsAppConnectionsSetIamPolicy"] = beyondcorp.post(
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
        importer="beyondcorp",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
