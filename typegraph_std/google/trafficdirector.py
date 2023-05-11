from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_trafficdirector() -> Import:
    trafficdirector = HTTPRuntime("https://trafficdirector.googleapis.com/")

    renames = {
        "ErrorResponse": "_trafficdirector_1_ErrorResponse",
        "SocketAddressIn": "_trafficdirector_2_SocketAddressIn",
        "SocketAddressOut": "_trafficdirector_3_SocketAddressOut",
        "ClientConfigIn": "_trafficdirector_4_ClientConfigIn",
        "ClientConfigOut": "_trafficdirector_5_ClientConfigOut",
        "UpdateFailureStateIn": "_trafficdirector_6_UpdateFailureStateIn",
        "UpdateFailureStateOut": "_trafficdirector_7_UpdateFailureStateOut",
        "ListMatcherIn": "_trafficdirector_8_ListMatcherIn",
        "ListMatcherOut": "_trafficdirector_9_ListMatcherOut",
        "StructMatcherIn": "_trafficdirector_10_StructMatcherIn",
        "StructMatcherOut": "_trafficdirector_11_StructMatcherOut",
        "StaticRouteConfigIn": "_trafficdirector_12_StaticRouteConfigIn",
        "StaticRouteConfigOut": "_trafficdirector_13_StaticRouteConfigOut",
        "SemanticVersionIn": "_trafficdirector_14_SemanticVersionIn",
        "SemanticVersionOut": "_trafficdirector_15_SemanticVersionOut",
        "LocalityIn": "_trafficdirector_16_LocalityIn",
        "LocalityOut": "_trafficdirector_17_LocalityOut",
        "DoubleMatcherIn": "_trafficdirector_18_DoubleMatcherIn",
        "DoubleMatcherOut": "_trafficdirector_19_DoubleMatcherOut",
        "DynamicScopedRouteConfigsIn": "_trafficdirector_20_DynamicScopedRouteConfigsIn",
        "DynamicScopedRouteConfigsOut": "_trafficdirector_21_DynamicScopedRouteConfigsOut",
        "PipeIn": "_trafficdirector_22_PipeIn",
        "PipeOut": "_trafficdirector_23_PipeOut",
        "DynamicClusterIn": "_trafficdirector_24_DynamicClusterIn",
        "DynamicClusterOut": "_trafficdirector_25_DynamicClusterOut",
        "InlineScopedRouteConfigsIn": "_trafficdirector_26_InlineScopedRouteConfigsIn",
        "InlineScopedRouteConfigsOut": "_trafficdirector_27_InlineScopedRouteConfigsOut",
        "DynamicListenerStateIn": "_trafficdirector_28_DynamicListenerStateIn",
        "DynamicListenerStateOut": "_trafficdirector_29_DynamicListenerStateOut",
        "RoutesConfigDumpIn": "_trafficdirector_30_RoutesConfigDumpIn",
        "RoutesConfigDumpOut": "_trafficdirector_31_RoutesConfigDumpOut",
        "PathSegmentIn": "_trafficdirector_32_PathSegmentIn",
        "PathSegmentOut": "_trafficdirector_33_PathSegmentOut",
        "ExtensionIn": "_trafficdirector_34_ExtensionIn",
        "ExtensionOut": "_trafficdirector_35_ExtensionOut",
        "DoubleRangeIn": "_trafficdirector_36_DoubleRangeIn",
        "DoubleRangeOut": "_trafficdirector_37_DoubleRangeOut",
        "ClientStatusRequestIn": "_trafficdirector_38_ClientStatusRequestIn",
        "ClientStatusRequestOut": "_trafficdirector_39_ClientStatusRequestOut",
        "StaticClusterIn": "_trafficdirector_40_StaticClusterIn",
        "StaticClusterOut": "_trafficdirector_41_StaticClusterOut",
        "ClientStatusResponseIn": "_trafficdirector_42_ClientStatusResponseIn",
        "ClientStatusResponseOut": "_trafficdirector_43_ClientStatusResponseOut",
        "ListenersConfigDumpIn": "_trafficdirector_44_ListenersConfigDumpIn",
        "ListenersConfigDumpOut": "_trafficdirector_45_ListenersConfigDumpOut",
        "NullMatchIn": "_trafficdirector_46_NullMatchIn",
        "NullMatchOut": "_trafficdirector_47_NullMatchOut",
        "NodeMatcherIn": "_trafficdirector_48_NodeMatcherIn",
        "NodeMatcherOut": "_trafficdirector_49_NodeMatcherOut",
        "BuildVersionIn": "_trafficdirector_50_BuildVersionIn",
        "BuildVersionOut": "_trafficdirector_51_BuildVersionOut",
        "DynamicListenerIn": "_trafficdirector_52_DynamicListenerIn",
        "DynamicListenerOut": "_trafficdirector_53_DynamicListenerOut",
        "StaticListenerIn": "_trafficdirector_54_StaticListenerIn",
        "StaticListenerOut": "_trafficdirector_55_StaticListenerOut",
        "NodeIn": "_trafficdirector_56_NodeIn",
        "NodeOut": "_trafficdirector_57_NodeOut",
        "AddressIn": "_trafficdirector_58_AddressIn",
        "AddressOut": "_trafficdirector_59_AddressOut",
        "GoogleRE2In": "_trafficdirector_60_GoogleRE2In",
        "GoogleRE2Out": "_trafficdirector_61_GoogleRE2Out",
        "PerXdsConfigIn": "_trafficdirector_62_PerXdsConfigIn",
        "PerXdsConfigOut": "_trafficdirector_63_PerXdsConfigOut",
        "DynamicRouteConfigIn": "_trafficdirector_64_DynamicRouteConfigIn",
        "DynamicRouteConfigOut": "_trafficdirector_65_DynamicRouteConfigOut",
        "ClustersConfigDumpIn": "_trafficdirector_66_ClustersConfigDumpIn",
        "ClustersConfigDumpOut": "_trafficdirector_67_ClustersConfigDumpOut",
        "ValueMatcherIn": "_trafficdirector_68_ValueMatcherIn",
        "ValueMatcherOut": "_trafficdirector_69_ValueMatcherOut",
        "RegexMatcherIn": "_trafficdirector_70_RegexMatcherIn",
        "RegexMatcherOut": "_trafficdirector_71_RegexMatcherOut",
        "ScopedRoutesConfigDumpIn": "_trafficdirector_72_ScopedRoutesConfigDumpIn",
        "ScopedRoutesConfigDumpOut": "_trafficdirector_73_ScopedRoutesConfigDumpOut",
        "StringMatcherIn": "_trafficdirector_74_StringMatcherIn",
        "StringMatcherOut": "_trafficdirector_75_StringMatcherOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SocketAddressIn"] = t.struct(
        {
            "address": t.string().optional(),
            "resolverName": t.string().optional(),
            "ipv4Compat": t.boolean().optional(),
            "portValue": t.integer(),
            "protocol": t.string(),
            "namedPort": t.string().optional(),
        }
    ).named(renames["SocketAddressIn"])
    types["SocketAddressOut"] = t.struct(
        {
            "address": t.string().optional(),
            "resolverName": t.string().optional(),
            "ipv4Compat": t.boolean().optional(),
            "portValue": t.integer(),
            "protocol": t.string(),
            "namedPort": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocketAddressOut"])
    types["ClientConfigIn"] = t.struct(
        {
            "node": t.proxy(renames["NodeIn"]).optional(),
            "xdsConfig": t.array(t.proxy(renames["PerXdsConfigIn"])),
        }
    ).named(renames["ClientConfigIn"])
    types["ClientConfigOut"] = t.struct(
        {
            "node": t.proxy(renames["NodeOut"]).optional(),
            "xdsConfig": t.array(t.proxy(renames["PerXdsConfigOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientConfigOut"])
    types["UpdateFailureStateIn"] = t.struct(
        {
            "details": t.string().optional(),
            "lastUpdateAttempt": t.string().optional(),
            "failedConfiguration": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["UpdateFailureStateIn"])
    types["UpdateFailureStateOut"] = t.struct(
        {
            "details": t.string().optional(),
            "lastUpdateAttempt": t.string().optional(),
            "failedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateFailureStateOut"])
    types["ListMatcherIn"] = t.struct(
        {"oneOf": t.proxy(renames["ValueMatcherIn"]).optional()}
    ).named(renames["ListMatcherIn"])
    types["ListMatcherOut"] = t.struct(
        {
            "oneOf": t.proxy(renames["ValueMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMatcherOut"])
    types["StructMatcherIn"] = t.struct(
        {
            "path": t.array(t.proxy(renames["PathSegmentIn"])).optional(),
            "value": t.proxy(renames["ValueMatcherIn"]).optional(),
        }
    ).named(renames["StructMatcherIn"])
    types["StructMatcherOut"] = t.struct(
        {
            "path": t.array(t.proxy(renames["PathSegmentOut"])).optional(),
            "value": t.proxy(renames["ValueMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructMatcherOut"])
    types["StaticRouteConfigIn"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StaticRouteConfigIn"])
    types["StaticRouteConfigOut"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StaticRouteConfigOut"])
    types["SemanticVersionIn"] = t.struct(
        {"majorNumber": t.integer(), "patch": t.integer(), "minorNumber": t.integer()}
    ).named(renames["SemanticVersionIn"])
    types["SemanticVersionOut"] = t.struct(
        {
            "majorNumber": t.integer(),
            "patch": t.integer(),
            "minorNumber": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SemanticVersionOut"])
    types["LocalityIn"] = t.struct(
        {
            "region": t.string().optional(),
            "subZone": t.string().optional(),
            "zone": t.string().optional(),
        }
    ).named(renames["LocalityIn"])
    types["LocalityOut"] = t.struct(
        {
            "region": t.string().optional(),
            "subZone": t.string().optional(),
            "zone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalityOut"])
    types["DoubleMatcherIn"] = t.struct(
        {
            "exact": t.number().optional(),
            "range": t.proxy(renames["DoubleRangeIn"]).optional(),
        }
    ).named(renames["DoubleMatcherIn"])
    types["DoubleMatcherOut"] = t.struct(
        {
            "exact": t.number().optional(),
            "range": t.proxy(renames["DoubleRangeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleMatcherOut"])
    types["DynamicScopedRouteConfigsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "versionInfo": t.string().optional(),
        }
    ).named(renames["DynamicScopedRouteConfigsIn"])
    types["DynamicScopedRouteConfigsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "versionInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicScopedRouteConfigsOut"])
    types["PipeIn"] = t.struct(
        {"path": t.string().optional(), "mode": t.integer().optional()}
    ).named(renames["PipeIn"])
    types["PipeOut"] = t.struct(
        {
            "path": t.string().optional(),
            "mode": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipeOut"])
    types["DynamicClusterIn"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "cluster": t.struct({"_": t.string().optional()}).optional(),
            "versionInfo": t.string().optional(),
        }
    ).named(renames["DynamicClusterIn"])
    types["DynamicClusterOut"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "cluster": t.struct({"_": t.string().optional()}).optional(),
            "versionInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicClusterOut"])
    types["InlineScopedRouteConfigsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
        }
    ).named(renames["InlineScopedRouteConfigsIn"])
    types["InlineScopedRouteConfigsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineScopedRouteConfigsOut"])
    types["DynamicListenerStateIn"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "listener": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
        }
    ).named(renames["DynamicListenerStateIn"])
    types["DynamicListenerStateOut"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "listener": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicListenerStateOut"])
    types["RoutesConfigDumpIn"] = t.struct(
        {
            "staticRouteConfigs": t.array(
                t.proxy(renames["StaticRouteConfigIn"])
            ).optional(),
            "dynamicRouteConfigs": t.array(
                t.proxy(renames["DynamicRouteConfigIn"])
            ).optional(),
        }
    ).named(renames["RoutesConfigDumpIn"])
    types["RoutesConfigDumpOut"] = t.struct(
        {
            "staticRouteConfigs": t.array(
                t.proxy(renames["StaticRouteConfigOut"])
            ).optional(),
            "dynamicRouteConfigs": t.array(
                t.proxy(renames["DynamicRouteConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoutesConfigDumpOut"])
    types["PathSegmentIn"] = t.struct({"key": t.string().optional()}).named(
        renames["PathSegmentIn"]
    )
    types["PathSegmentOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathSegmentOut"])
    types["ExtensionIn"] = t.struct(
        {
            "category": t.string().optional(),
            "name": t.string().optional(),
            "typeDescriptor": t.string().optional(),
            "disabled": t.boolean().optional(),
            "version": t.proxy(renames["BuildVersionIn"]).optional(),
        }
    ).named(renames["ExtensionIn"])
    types["ExtensionOut"] = t.struct(
        {
            "category": t.string().optional(),
            "name": t.string().optional(),
            "typeDescriptor": t.string().optional(),
            "disabled": t.boolean().optional(),
            "version": t.proxy(renames["BuildVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtensionOut"])
    types["DoubleRangeIn"] = t.struct(
        {"start": t.number().optional(), "end": t.number().optional()}
    ).named(renames["DoubleRangeIn"])
    types["DoubleRangeOut"] = t.struct(
        {
            "start": t.number().optional(),
            "end": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleRangeOut"])
    types["ClientStatusRequestIn"] = t.struct(
        {"nodeMatchers": t.array(t.proxy(renames["NodeMatcherIn"])).optional()}
    ).named(renames["ClientStatusRequestIn"])
    types["ClientStatusRequestOut"] = t.struct(
        {
            "nodeMatchers": t.array(t.proxy(renames["NodeMatcherOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientStatusRequestOut"])
    types["StaticClusterIn"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "cluster": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StaticClusterIn"])
    types["StaticClusterOut"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "cluster": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StaticClusterOut"])
    types["ClientStatusResponseIn"] = t.struct(
        {"config": t.array(t.proxy(renames["ClientConfigIn"])).optional()}
    ).named(renames["ClientStatusResponseIn"])
    types["ClientStatusResponseOut"] = t.struct(
        {
            "config": t.array(t.proxy(renames["ClientConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientStatusResponseOut"])
    types["ListenersConfigDumpIn"] = t.struct(
        {
            "staticListeners": t.array(t.proxy(renames["StaticListenerIn"])).optional(),
            "versionInfo": t.string().optional(),
            "dynamicListeners": t.array(
                t.proxy(renames["DynamicListenerIn"])
            ).optional(),
        }
    ).named(renames["ListenersConfigDumpIn"])
    types["ListenersConfigDumpOut"] = t.struct(
        {
            "staticListeners": t.array(
                t.proxy(renames["StaticListenerOut"])
            ).optional(),
            "versionInfo": t.string().optional(),
            "dynamicListeners": t.array(
                t.proxy(renames["DynamicListenerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenersConfigDumpOut"])
    types["NullMatchIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NullMatchIn"]
    )
    types["NullMatchOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NullMatchOut"])
    types["NodeMatcherIn"] = t.struct(
        {
            "nodeId": t.proxy(renames["StringMatcherIn"]).optional(),
            "nodeMetadatas": t.array(t.proxy(renames["StructMatcherIn"])).optional(),
        }
    ).named(renames["NodeMatcherIn"])
    types["NodeMatcherOut"] = t.struct(
        {
            "nodeId": t.proxy(renames["StringMatcherOut"]).optional(),
            "nodeMetadatas": t.array(t.proxy(renames["StructMatcherOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeMatcherOut"])
    types["BuildVersionIn"] = t.struct(
        {
            "version": t.proxy(renames["SemanticVersionIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["BuildVersionIn"])
    types["BuildVersionOut"] = t.struct(
        {
            "version": t.proxy(renames["SemanticVersionOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildVersionOut"])
    types["DynamicListenerIn"] = t.struct(
        {
            "drainingState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
            "name": t.string().optional(),
            "errorState": t.proxy(renames["UpdateFailureStateIn"]).optional(),
            "activeState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
            "warmingState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
        }
    ).named(renames["DynamicListenerIn"])
    types["DynamicListenerOut"] = t.struct(
        {
            "drainingState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "name": t.string().optional(),
            "errorState": t.proxy(renames["UpdateFailureStateOut"]).optional(),
            "activeState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "warmingState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicListenerOut"])
    types["StaticListenerIn"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "listener": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["StaticListenerIn"])
    types["StaticListenerOut"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "listener": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StaticListenerOut"])
    types["NodeIn"] = t.struct(
        {
            "buildVersion": t.string().optional(),
            "locality": t.proxy(renames["LocalityIn"]).optional(),
            "listeningAddresses": t.array(t.proxy(renames["AddressIn"])).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "userAgentVersion": t.string().optional(),
            "userAgentBuildVersion": t.proxy(renames["BuildVersionIn"]).optional(),
            "clientFeatures": t.array(t.string()).optional(),
            "extensions": t.array(t.proxy(renames["ExtensionIn"])).optional(),
            "cluster": t.string().optional(),
            "userAgentName": t.string().optional(),
        }
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "buildVersion": t.string().optional(),
            "locality": t.proxy(renames["LocalityOut"]).optional(),
            "listeningAddresses": t.array(t.proxy(renames["AddressOut"])).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "userAgentVersion": t.string().optional(),
            "userAgentBuildVersion": t.proxy(renames["BuildVersionOut"]).optional(),
            "clientFeatures": t.array(t.string()).optional(),
            "extensions": t.array(t.proxy(renames["ExtensionOut"])).optional(),
            "cluster": t.string().optional(),
            "userAgentName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["AddressIn"] = t.struct(
        {
            "socketAddress": t.proxy(renames["SocketAddressIn"]),
            "pipe": t.proxy(renames["PipeIn"]),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "socketAddress": t.proxy(renames["SocketAddressOut"]),
            "pipe": t.proxy(renames["PipeOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["GoogleRE2In"] = t.struct({"maxProgramSize": t.integer().optional()}).named(
        renames["GoogleRE2In"]
    )
    types["GoogleRE2Out"] = t.struct(
        {
            "maxProgramSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRE2Out"])
    types["PerXdsConfigIn"] = t.struct(
        {
            "status": t.string(),
            "listenerConfig": t.proxy(renames["ListenersConfigDumpIn"]),
            "clusterConfig": t.proxy(renames["ClustersConfigDumpIn"]),
            "scopedRouteConfig": t.proxy(renames["ScopedRoutesConfigDumpIn"]),
            "routeConfig": t.proxy(renames["RoutesConfigDumpIn"]),
        }
    ).named(renames["PerXdsConfigIn"])
    types["PerXdsConfigOut"] = t.struct(
        {
            "status": t.string(),
            "listenerConfig": t.proxy(renames["ListenersConfigDumpOut"]),
            "clusterConfig": t.proxy(renames["ClustersConfigDumpOut"]),
            "scopedRouteConfig": t.proxy(renames["ScopedRoutesConfigDumpOut"]),
            "routeConfig": t.proxy(renames["RoutesConfigDumpOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerXdsConfigOut"])
    types["DynamicRouteConfigIn"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["DynamicRouteConfigIn"])
    types["DynamicRouteConfigOut"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicRouteConfigOut"])
    types["ClustersConfigDumpIn"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "staticClusters": t.array(t.proxy(renames["StaticClusterIn"])).optional(),
            "dynamicWarmingClusters": t.array(
                t.proxy(renames["DynamicClusterIn"])
            ).optional(),
            "dynamicActiveClusters": t.array(
                t.proxy(renames["DynamicClusterIn"])
            ).optional(),
        }
    ).named(renames["ClustersConfigDumpIn"])
    types["ClustersConfigDumpOut"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "staticClusters": t.array(t.proxy(renames["StaticClusterOut"])).optional(),
            "dynamicWarmingClusters": t.array(
                t.proxy(renames["DynamicClusterOut"])
            ).optional(),
            "dynamicActiveClusters": t.array(
                t.proxy(renames["DynamicClusterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClustersConfigDumpOut"])
    types["ValueMatcherIn"] = t.struct(
        {
            "doubleMatch": t.proxy(renames["DoubleMatcherIn"]).optional(),
            "stringMatch": t.proxy(renames["StringMatcherIn"]).optional(),
            "nullMatch": t.proxy(renames["NullMatchIn"]).optional(),
            "boolMatch": t.boolean().optional(),
            "presentMatch": t.boolean().optional(),
            "listMatch": t.proxy(renames["ListMatcherIn"]).optional(),
        }
    ).named(renames["ValueMatcherIn"])
    types["ValueMatcherOut"] = t.struct(
        {
            "doubleMatch": t.proxy(renames["DoubleMatcherOut"]).optional(),
            "stringMatch": t.proxy(renames["StringMatcherOut"]).optional(),
            "nullMatch": t.proxy(renames["NullMatchOut"]).optional(),
            "boolMatch": t.boolean().optional(),
            "presentMatch": t.boolean().optional(),
            "listMatch": t.proxy(renames["ListMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueMatcherOut"])
    types["RegexMatcherIn"] = t.struct(
        {
            "googleRe2": t.proxy(renames["GoogleRE2In"]).optional(),
            "regex": t.string().optional(),
        }
    ).named(renames["RegexMatcherIn"])
    types["RegexMatcherOut"] = t.struct(
        {
            "googleRe2": t.proxy(renames["GoogleRE2Out"]).optional(),
            "regex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegexMatcherOut"])
    types["ScopedRoutesConfigDumpIn"] = t.struct(
        {
            "inlineScopedRouteConfigs": t.array(
                t.proxy(renames["InlineScopedRouteConfigsIn"])
            ).optional(),
            "dynamicScopedRouteConfigs": t.array(
                t.proxy(renames["DynamicScopedRouteConfigsIn"])
            ).optional(),
        }
    ).named(renames["ScopedRoutesConfigDumpIn"])
    types["ScopedRoutesConfigDumpOut"] = t.struct(
        {
            "inlineScopedRouteConfigs": t.array(
                t.proxy(renames["InlineScopedRouteConfigsOut"])
            ).optional(),
            "dynamicScopedRouteConfigs": t.array(
                t.proxy(renames["DynamicScopedRouteConfigsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopedRoutesConfigDumpOut"])
    types["StringMatcherIn"] = t.struct(
        {
            "safeRegex": t.proxy(renames["RegexMatcherIn"]).optional(),
            "ignoreCase": t.boolean().optional(),
            "prefix": t.string().optional(),
            "regex": t.string().optional(),
            "suffix": t.string().optional(),
            "exact": t.string().optional(),
        }
    ).named(renames["StringMatcherIn"])
    types["StringMatcherOut"] = t.struct(
        {
            "safeRegex": t.proxy(renames["RegexMatcherOut"]).optional(),
            "ignoreCase": t.boolean().optional(),
            "prefix": t.string().optional(),
            "regex": t.string().optional(),
            "suffix": t.string().optional(),
            "exact": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringMatcherOut"])

    functions = {}
    functions["discoveryClient_status"] = trafficdirector.post(
        "v2/discovery:client_status",
        t.struct(
            {
                "nodeMatchers": t.array(t.proxy(renames["NodeMatcherIn"])).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClientStatusResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="trafficdirector", renames=renames, types=types, functions=functions
    )
