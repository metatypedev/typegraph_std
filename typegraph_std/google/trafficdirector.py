from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_trafficdirector() -> Import:
    trafficdirector = HTTPRuntime("https://trafficdirector.googleapis.com/")

    renames = {
        "ErrorResponse": "_trafficdirector_1_ErrorResponse",
        "GoogleRE2In": "_trafficdirector_2_GoogleRE2In",
        "GoogleRE2Out": "_trafficdirector_3_GoogleRE2Out",
        "PipeIn": "_trafficdirector_4_PipeIn",
        "PipeOut": "_trafficdirector_5_PipeOut",
        "StaticListenerIn": "_trafficdirector_6_StaticListenerIn",
        "StaticListenerOut": "_trafficdirector_7_StaticListenerOut",
        "RegexMatcherIn": "_trafficdirector_8_RegexMatcherIn",
        "RegexMatcherOut": "_trafficdirector_9_RegexMatcherOut",
        "DynamicRouteConfigIn": "_trafficdirector_10_DynamicRouteConfigIn",
        "DynamicRouteConfigOut": "_trafficdirector_11_DynamicRouteConfigOut",
        "NodeIn": "_trafficdirector_12_NodeIn",
        "NodeOut": "_trafficdirector_13_NodeOut",
        "DynamicListenerStateIn": "_trafficdirector_14_DynamicListenerStateIn",
        "DynamicListenerStateOut": "_trafficdirector_15_DynamicListenerStateOut",
        "BuildVersionIn": "_trafficdirector_16_BuildVersionIn",
        "BuildVersionOut": "_trafficdirector_17_BuildVersionOut",
        "SemanticVersionIn": "_trafficdirector_18_SemanticVersionIn",
        "SemanticVersionOut": "_trafficdirector_19_SemanticVersionOut",
        "StaticClusterIn": "_trafficdirector_20_StaticClusterIn",
        "StaticClusterOut": "_trafficdirector_21_StaticClusterOut",
        "ListMatcherIn": "_trafficdirector_22_ListMatcherIn",
        "ListMatcherOut": "_trafficdirector_23_ListMatcherOut",
        "ExtensionIn": "_trafficdirector_24_ExtensionIn",
        "ExtensionOut": "_trafficdirector_25_ExtensionOut",
        "SocketAddressIn": "_trafficdirector_26_SocketAddressIn",
        "SocketAddressOut": "_trafficdirector_27_SocketAddressOut",
        "ClientStatusResponseIn": "_trafficdirector_28_ClientStatusResponseIn",
        "ClientStatusResponseOut": "_trafficdirector_29_ClientStatusResponseOut",
        "RoutesConfigDumpIn": "_trafficdirector_30_RoutesConfigDumpIn",
        "RoutesConfigDumpOut": "_trafficdirector_31_RoutesConfigDumpOut",
        "ClientConfigIn": "_trafficdirector_32_ClientConfigIn",
        "ClientConfigOut": "_trafficdirector_33_ClientConfigOut",
        "NodeMatcherIn": "_trafficdirector_34_NodeMatcherIn",
        "NodeMatcherOut": "_trafficdirector_35_NodeMatcherOut",
        "PerXdsConfigIn": "_trafficdirector_36_PerXdsConfigIn",
        "PerXdsConfigOut": "_trafficdirector_37_PerXdsConfigOut",
        "DynamicListenerIn": "_trafficdirector_38_DynamicListenerIn",
        "DynamicListenerOut": "_trafficdirector_39_DynamicListenerOut",
        "StructMatcherIn": "_trafficdirector_40_StructMatcherIn",
        "StructMatcherOut": "_trafficdirector_41_StructMatcherOut",
        "StaticRouteConfigIn": "_trafficdirector_42_StaticRouteConfigIn",
        "StaticRouteConfigOut": "_trafficdirector_43_StaticRouteConfigOut",
        "ValueMatcherIn": "_trafficdirector_44_ValueMatcherIn",
        "ValueMatcherOut": "_trafficdirector_45_ValueMatcherOut",
        "ListenersConfigDumpIn": "_trafficdirector_46_ListenersConfigDumpIn",
        "ListenersConfigDumpOut": "_trafficdirector_47_ListenersConfigDumpOut",
        "UpdateFailureStateIn": "_trafficdirector_48_UpdateFailureStateIn",
        "UpdateFailureStateOut": "_trafficdirector_49_UpdateFailureStateOut",
        "ScopedRoutesConfigDumpIn": "_trafficdirector_50_ScopedRoutesConfigDumpIn",
        "ScopedRoutesConfigDumpOut": "_trafficdirector_51_ScopedRoutesConfigDumpOut",
        "DynamicClusterIn": "_trafficdirector_52_DynamicClusterIn",
        "DynamicClusterOut": "_trafficdirector_53_DynamicClusterOut",
        "AddressIn": "_trafficdirector_54_AddressIn",
        "AddressOut": "_trafficdirector_55_AddressOut",
        "PathSegmentIn": "_trafficdirector_56_PathSegmentIn",
        "PathSegmentOut": "_trafficdirector_57_PathSegmentOut",
        "LocalityIn": "_trafficdirector_58_LocalityIn",
        "LocalityOut": "_trafficdirector_59_LocalityOut",
        "DoubleMatcherIn": "_trafficdirector_60_DoubleMatcherIn",
        "DoubleMatcherOut": "_trafficdirector_61_DoubleMatcherOut",
        "DynamicScopedRouteConfigsIn": "_trafficdirector_62_DynamicScopedRouteConfigsIn",
        "DynamicScopedRouteConfigsOut": "_trafficdirector_63_DynamicScopedRouteConfigsOut",
        "ClientStatusRequestIn": "_trafficdirector_64_ClientStatusRequestIn",
        "ClientStatusRequestOut": "_trafficdirector_65_ClientStatusRequestOut",
        "NullMatchIn": "_trafficdirector_66_NullMatchIn",
        "NullMatchOut": "_trafficdirector_67_NullMatchOut",
        "ClustersConfigDumpIn": "_trafficdirector_68_ClustersConfigDumpIn",
        "ClustersConfigDumpOut": "_trafficdirector_69_ClustersConfigDumpOut",
        "DoubleRangeIn": "_trafficdirector_70_DoubleRangeIn",
        "DoubleRangeOut": "_trafficdirector_71_DoubleRangeOut",
        "StringMatcherIn": "_trafficdirector_72_StringMatcherIn",
        "StringMatcherOut": "_trafficdirector_73_StringMatcherOut",
        "InlineScopedRouteConfigsIn": "_trafficdirector_74_InlineScopedRouteConfigsIn",
        "InlineScopedRouteConfigsOut": "_trafficdirector_75_InlineScopedRouteConfigsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleRE2In"] = t.struct({"maxProgramSize": t.integer().optional()}).named(
        renames["GoogleRE2In"]
    )
    types["GoogleRE2Out"] = t.struct(
        {
            "maxProgramSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRE2Out"])
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
    types["DynamicRouteConfigIn"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
            "versionInfo": t.string().optional(),
        }
    ).named(renames["DynamicRouteConfigIn"])
    types["DynamicRouteConfigOut"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
            "versionInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicRouteConfigOut"])
    types["NodeIn"] = t.struct(
        {
            "locality": t.proxy(renames["LocalityIn"]).optional(),
            "listeningAddresses": t.array(t.proxy(renames["AddressIn"])).optional(),
            "extensions": t.array(t.proxy(renames["ExtensionIn"])).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "userAgentVersion": t.string().optional(),
            "userAgentBuildVersion": t.proxy(renames["BuildVersionIn"]).optional(),
            "userAgentName": t.string().optional(),
            "clientFeatures": t.array(t.string()).optional(),
            "cluster": t.string().optional(),
            "buildVersion": t.string().optional(),
        }
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "locality": t.proxy(renames["LocalityOut"]).optional(),
            "listeningAddresses": t.array(t.proxy(renames["AddressOut"])).optional(),
            "extensions": t.array(t.proxy(renames["ExtensionOut"])).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "userAgentVersion": t.string().optional(),
            "userAgentBuildVersion": t.proxy(renames["BuildVersionOut"]).optional(),
            "userAgentName": t.string().optional(),
            "clientFeatures": t.array(t.string()).optional(),
            "cluster": t.string().optional(),
            "buildVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
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
    types["SemanticVersionIn"] = t.struct(
        {"patch": t.integer(), "majorNumber": t.integer(), "minorNumber": t.integer()}
    ).named(renames["SemanticVersionIn"])
    types["SemanticVersionOut"] = t.struct(
        {
            "patch": t.integer(),
            "majorNumber": t.integer(),
            "minorNumber": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SemanticVersionOut"])
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
    types["ListMatcherIn"] = t.struct(
        {"oneOf": t.proxy(renames["ValueMatcherIn"]).optional()}
    ).named(renames["ListMatcherIn"])
    types["ListMatcherOut"] = t.struct(
        {
            "oneOf": t.proxy(renames["ValueMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMatcherOut"])
    types["ExtensionIn"] = t.struct(
        {
            "name": t.string().optional(),
            "category": t.string().optional(),
            "disabled": t.boolean().optional(),
            "typeDescriptor": t.string().optional(),
            "version": t.proxy(renames["BuildVersionIn"]).optional(),
        }
    ).named(renames["ExtensionIn"])
    types["ExtensionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "category": t.string().optional(),
            "disabled": t.boolean().optional(),
            "typeDescriptor": t.string().optional(),
            "version": t.proxy(renames["BuildVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtensionOut"])
    types["SocketAddressIn"] = t.struct(
        {
            "protocol": t.string(),
            "ipv4Compat": t.boolean().optional(),
            "namedPort": t.string().optional(),
            "resolverName": t.string().optional(),
            "portValue": t.integer(),
            "address": t.string().optional(),
        }
    ).named(renames["SocketAddressIn"])
    types["SocketAddressOut"] = t.struct(
        {
            "protocol": t.string(),
            "ipv4Compat": t.boolean().optional(),
            "namedPort": t.string().optional(),
            "resolverName": t.string().optional(),
            "portValue": t.integer(),
            "address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocketAddressOut"])
    types["ClientStatusResponseIn"] = t.struct(
        {"config": t.array(t.proxy(renames["ClientConfigIn"])).optional()}
    ).named(renames["ClientStatusResponseIn"])
    types["ClientStatusResponseOut"] = t.struct(
        {
            "config": t.array(t.proxy(renames["ClientConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientStatusResponseOut"])
    types["RoutesConfigDumpIn"] = t.struct(
        {
            "dynamicRouteConfigs": t.array(
                t.proxy(renames["DynamicRouteConfigIn"])
            ).optional(),
            "staticRouteConfigs": t.array(
                t.proxy(renames["StaticRouteConfigIn"])
            ).optional(),
        }
    ).named(renames["RoutesConfigDumpIn"])
    types["RoutesConfigDumpOut"] = t.struct(
        {
            "dynamicRouteConfigs": t.array(
                t.proxy(renames["DynamicRouteConfigOut"])
            ).optional(),
            "staticRouteConfigs": t.array(
                t.proxy(renames["StaticRouteConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RoutesConfigDumpOut"])
    types["ClientConfigIn"] = t.struct(
        {
            "xdsConfig": t.array(t.proxy(renames["PerXdsConfigIn"])),
            "node": t.proxy(renames["NodeIn"]).optional(),
        }
    ).named(renames["ClientConfigIn"])
    types["ClientConfigOut"] = t.struct(
        {
            "xdsConfig": t.array(t.proxy(renames["PerXdsConfigOut"])),
            "node": t.proxy(renames["NodeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientConfigOut"])
    types["NodeMatcherIn"] = t.struct(
        {
            "nodeMetadatas": t.array(t.proxy(renames["StructMatcherIn"])).optional(),
            "nodeId": t.proxy(renames["StringMatcherIn"]).optional(),
        }
    ).named(renames["NodeMatcherIn"])
    types["NodeMatcherOut"] = t.struct(
        {
            "nodeMetadatas": t.array(t.proxy(renames["StructMatcherOut"])).optional(),
            "nodeId": t.proxy(renames["StringMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeMatcherOut"])
    types["PerXdsConfigIn"] = t.struct(
        {
            "listenerConfig": t.proxy(renames["ListenersConfigDumpIn"]),
            "routeConfig": t.proxy(renames["RoutesConfigDumpIn"]),
            "status": t.string(),
            "clusterConfig": t.proxy(renames["ClustersConfigDumpIn"]),
            "scopedRouteConfig": t.proxy(renames["ScopedRoutesConfigDumpIn"]),
        }
    ).named(renames["PerXdsConfigIn"])
    types["PerXdsConfigOut"] = t.struct(
        {
            "listenerConfig": t.proxy(renames["ListenersConfigDumpOut"]),
            "routeConfig": t.proxy(renames["RoutesConfigDumpOut"]),
            "status": t.string(),
            "clusterConfig": t.proxy(renames["ClustersConfigDumpOut"]),
            "scopedRouteConfig": t.proxy(renames["ScopedRoutesConfigDumpOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerXdsConfigOut"])
    types["DynamicListenerIn"] = t.struct(
        {
            "name": t.string().optional(),
            "drainingState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
            "errorState": t.proxy(renames["UpdateFailureStateIn"]).optional(),
            "warmingState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
            "activeState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
        }
    ).named(renames["DynamicListenerIn"])
    types["DynamicListenerOut"] = t.struct(
        {
            "name": t.string().optional(),
            "drainingState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "errorState": t.proxy(renames["UpdateFailureStateOut"]).optional(),
            "warmingState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "activeState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicListenerOut"])
    types["StructMatcherIn"] = t.struct(
        {
            "value": t.proxy(renames["ValueMatcherIn"]).optional(),
            "path": t.array(t.proxy(renames["PathSegmentIn"])).optional(),
        }
    ).named(renames["StructMatcherIn"])
    types["StructMatcherOut"] = t.struct(
        {
            "value": t.proxy(renames["ValueMatcherOut"]).optional(),
            "path": t.array(t.proxy(renames["PathSegmentOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StructMatcherOut"])
    types["StaticRouteConfigIn"] = t.struct(
        {
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
        }
    ).named(renames["StaticRouteConfigIn"])
    types["StaticRouteConfigOut"] = t.struct(
        {
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StaticRouteConfigOut"])
    types["ValueMatcherIn"] = t.struct(
        {
            "nullMatch": t.proxy(renames["NullMatchIn"]).optional(),
            "presentMatch": t.boolean().optional(),
            "stringMatch": t.proxy(renames["StringMatcherIn"]).optional(),
            "listMatch": t.proxy(renames["ListMatcherIn"]).optional(),
            "boolMatch": t.boolean().optional(),
            "doubleMatch": t.proxy(renames["DoubleMatcherIn"]).optional(),
        }
    ).named(renames["ValueMatcherIn"])
    types["ValueMatcherOut"] = t.struct(
        {
            "nullMatch": t.proxy(renames["NullMatchOut"]).optional(),
            "presentMatch": t.boolean().optional(),
            "stringMatch": t.proxy(renames["StringMatcherOut"]).optional(),
            "listMatch": t.proxy(renames["ListMatcherOut"]).optional(),
            "boolMatch": t.boolean().optional(),
            "doubleMatch": t.proxy(renames["DoubleMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueMatcherOut"])
    types["ListenersConfigDumpIn"] = t.struct(
        {
            "dynamicListeners": t.array(
                t.proxy(renames["DynamicListenerIn"])
            ).optional(),
            "versionInfo": t.string().optional(),
            "staticListeners": t.array(t.proxy(renames["StaticListenerIn"])).optional(),
        }
    ).named(renames["ListenersConfigDumpIn"])
    types["ListenersConfigDumpOut"] = t.struct(
        {
            "dynamicListeners": t.array(
                t.proxy(renames["DynamicListenerOut"])
            ).optional(),
            "versionInfo": t.string().optional(),
            "staticListeners": t.array(
                t.proxy(renames["StaticListenerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenersConfigDumpOut"])
    types["UpdateFailureStateIn"] = t.struct(
        {
            "lastUpdateAttempt": t.string().optional(),
            "failedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "details": t.string().optional(),
        }
    ).named(renames["UpdateFailureStateIn"])
    types["UpdateFailureStateOut"] = t.struct(
        {
            "lastUpdateAttempt": t.string().optional(),
            "failedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "details": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateFailureStateOut"])
    types["ScopedRoutesConfigDumpIn"] = t.struct(
        {
            "dynamicScopedRouteConfigs": t.array(
                t.proxy(renames["DynamicScopedRouteConfigsIn"])
            ).optional(),
            "inlineScopedRouteConfigs": t.array(
                t.proxy(renames["InlineScopedRouteConfigsIn"])
            ).optional(),
        }
    ).named(renames["ScopedRoutesConfigDumpIn"])
    types["ScopedRoutesConfigDumpOut"] = t.struct(
        {
            "dynamicScopedRouteConfigs": t.array(
                t.proxy(renames["DynamicScopedRouteConfigsOut"])
            ).optional(),
            "inlineScopedRouteConfigs": t.array(
                t.proxy(renames["InlineScopedRouteConfigsOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ScopedRoutesConfigDumpOut"])
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
    types["PathSegmentIn"] = t.struct({"key": t.string().optional()}).named(
        renames["PathSegmentIn"]
    )
    types["PathSegmentOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathSegmentOut"])
    types["LocalityIn"] = t.struct(
        {
            "region": t.string().optional(),
            "zone": t.string().optional(),
            "subZone": t.string().optional(),
        }
    ).named(renames["LocalityIn"])
    types["LocalityOut"] = t.struct(
        {
            "region": t.string().optional(),
            "zone": t.string().optional(),
            "subZone": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalityOut"])
    types["DoubleMatcherIn"] = t.struct(
        {
            "range": t.proxy(renames["DoubleRangeIn"]).optional(),
            "exact": t.number().optional(),
        }
    ).named(renames["DoubleMatcherIn"])
    types["DoubleMatcherOut"] = t.struct(
        {
            "range": t.proxy(renames["DoubleRangeOut"]).optional(),
            "exact": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleMatcherOut"])
    types["DynamicScopedRouteConfigsIn"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "versionInfo": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["DynamicScopedRouteConfigsIn"])
    types["DynamicScopedRouteConfigsOut"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "versionInfo": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicScopedRouteConfigsOut"])
    types["ClientStatusRequestIn"] = t.struct(
        {"nodeMatchers": t.array(t.proxy(renames["NodeMatcherIn"])).optional()}
    ).named(renames["ClientStatusRequestIn"])
    types["ClientStatusRequestOut"] = t.struct(
        {
            "nodeMatchers": t.array(t.proxy(renames["NodeMatcherOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientStatusRequestOut"])
    types["NullMatchIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NullMatchIn"]
    )
    types["NullMatchOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NullMatchOut"])
    types["ClustersConfigDumpIn"] = t.struct(
        {
            "staticClusters": t.array(t.proxy(renames["StaticClusterIn"])).optional(),
            "versionInfo": t.string().optional(),
            "dynamicActiveClusters": t.array(
                t.proxy(renames["DynamicClusterIn"])
            ).optional(),
            "dynamicWarmingClusters": t.array(
                t.proxy(renames["DynamicClusterIn"])
            ).optional(),
        }
    ).named(renames["ClustersConfigDumpIn"])
    types["ClustersConfigDumpOut"] = t.struct(
        {
            "staticClusters": t.array(t.proxy(renames["StaticClusterOut"])).optional(),
            "versionInfo": t.string().optional(),
            "dynamicActiveClusters": t.array(
                t.proxy(renames["DynamicClusterOut"])
            ).optional(),
            "dynamicWarmingClusters": t.array(
                t.proxy(renames["DynamicClusterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClustersConfigDumpOut"])
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
    types["StringMatcherIn"] = t.struct(
        {
            "safeRegex": t.proxy(renames["RegexMatcherIn"]).optional(),
            "prefix": t.string().optional(),
            "suffix": t.string().optional(),
            "ignoreCase": t.boolean().optional(),
            "exact": t.string().optional(),
            "regex": t.string().optional(),
        }
    ).named(renames["StringMatcherIn"])
    types["StringMatcherOut"] = t.struct(
        {
            "safeRegex": t.proxy(renames["RegexMatcherOut"]).optional(),
            "prefix": t.string().optional(),
            "suffix": t.string().optional(),
            "ignoreCase": t.boolean().optional(),
            "exact": t.string().optional(),
            "regex": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringMatcherOut"])
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
        importer="trafficdirector",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
