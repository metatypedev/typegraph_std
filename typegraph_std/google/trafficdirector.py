from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_trafficdirector():
    trafficdirector = HTTPRuntime("https://trafficdirector.googleapis.com/")

    renames = {
        "ErrorResponse": "_trafficdirector_1_ErrorResponse",
        "ClustersConfigDumpIn": "_trafficdirector_2_ClustersConfigDumpIn",
        "ClustersConfigDumpOut": "_trafficdirector_3_ClustersConfigDumpOut",
        "DynamicListenerStateIn": "_trafficdirector_4_DynamicListenerStateIn",
        "DynamicListenerStateOut": "_trafficdirector_5_DynamicListenerStateOut",
        "ClientConfigIn": "_trafficdirector_6_ClientConfigIn",
        "ClientConfigOut": "_trafficdirector_7_ClientConfigOut",
        "RegexMatcherIn": "_trafficdirector_8_RegexMatcherIn",
        "RegexMatcherOut": "_trafficdirector_9_RegexMatcherOut",
        "StaticListenerIn": "_trafficdirector_10_StaticListenerIn",
        "StaticListenerOut": "_trafficdirector_11_StaticListenerOut",
        "NullMatchIn": "_trafficdirector_12_NullMatchIn",
        "NullMatchOut": "_trafficdirector_13_NullMatchOut",
        "PerXdsConfigIn": "_trafficdirector_14_PerXdsConfigIn",
        "PerXdsConfigOut": "_trafficdirector_15_PerXdsConfigOut",
        "ClientStatusRequestIn": "_trafficdirector_16_ClientStatusRequestIn",
        "ClientStatusRequestOut": "_trafficdirector_17_ClientStatusRequestOut",
        "ExtensionIn": "_trafficdirector_18_ExtensionIn",
        "ExtensionOut": "_trafficdirector_19_ExtensionOut",
        "RoutesConfigDumpIn": "_trafficdirector_20_RoutesConfigDumpIn",
        "RoutesConfigDumpOut": "_trafficdirector_21_RoutesConfigDumpOut",
        "AddressIn": "_trafficdirector_22_AddressIn",
        "AddressOut": "_trafficdirector_23_AddressOut",
        "GoogleRE2In": "_trafficdirector_24_GoogleRE2In",
        "GoogleRE2Out": "_trafficdirector_25_GoogleRE2Out",
        "ScopedRoutesConfigDumpIn": "_trafficdirector_26_ScopedRoutesConfigDumpIn",
        "ScopedRoutesConfigDumpOut": "_trafficdirector_27_ScopedRoutesConfigDumpOut",
        "DoubleRangeIn": "_trafficdirector_28_DoubleRangeIn",
        "DoubleRangeOut": "_trafficdirector_29_DoubleRangeOut",
        "ListMatcherIn": "_trafficdirector_30_ListMatcherIn",
        "ListMatcherOut": "_trafficdirector_31_ListMatcherOut",
        "ValueMatcherIn": "_trafficdirector_32_ValueMatcherIn",
        "ValueMatcherOut": "_trafficdirector_33_ValueMatcherOut",
        "StaticRouteConfigIn": "_trafficdirector_34_StaticRouteConfigIn",
        "StaticRouteConfigOut": "_trafficdirector_35_StaticRouteConfigOut",
        "DynamicRouteConfigIn": "_trafficdirector_36_DynamicRouteConfigIn",
        "DynamicRouteConfigOut": "_trafficdirector_37_DynamicRouteConfigOut",
        "LocalityIn": "_trafficdirector_38_LocalityIn",
        "LocalityOut": "_trafficdirector_39_LocalityOut",
        "NodeMatcherIn": "_trafficdirector_40_NodeMatcherIn",
        "NodeMatcherOut": "_trafficdirector_41_NodeMatcherOut",
        "SocketAddressIn": "_trafficdirector_42_SocketAddressIn",
        "SocketAddressOut": "_trafficdirector_43_SocketAddressOut",
        "SemanticVersionIn": "_trafficdirector_44_SemanticVersionIn",
        "SemanticVersionOut": "_trafficdirector_45_SemanticVersionOut",
        "StringMatcherIn": "_trafficdirector_46_StringMatcherIn",
        "StringMatcherOut": "_trafficdirector_47_StringMatcherOut",
        "PipeIn": "_trafficdirector_48_PipeIn",
        "PipeOut": "_trafficdirector_49_PipeOut",
        "DoubleMatcherIn": "_trafficdirector_50_DoubleMatcherIn",
        "DoubleMatcherOut": "_trafficdirector_51_DoubleMatcherOut",
        "UpdateFailureStateIn": "_trafficdirector_52_UpdateFailureStateIn",
        "UpdateFailureStateOut": "_trafficdirector_53_UpdateFailureStateOut",
        "DynamicClusterIn": "_trafficdirector_54_DynamicClusterIn",
        "DynamicClusterOut": "_trafficdirector_55_DynamicClusterOut",
        "PathSegmentIn": "_trafficdirector_56_PathSegmentIn",
        "PathSegmentOut": "_trafficdirector_57_PathSegmentOut",
        "DynamicListenerIn": "_trafficdirector_58_DynamicListenerIn",
        "DynamicListenerOut": "_trafficdirector_59_DynamicListenerOut",
        "StaticClusterIn": "_trafficdirector_60_StaticClusterIn",
        "StaticClusterOut": "_trafficdirector_61_StaticClusterOut",
        "ListenersConfigDumpIn": "_trafficdirector_62_ListenersConfigDumpIn",
        "ListenersConfigDumpOut": "_trafficdirector_63_ListenersConfigDumpOut",
        "BuildVersionIn": "_trafficdirector_64_BuildVersionIn",
        "BuildVersionOut": "_trafficdirector_65_BuildVersionOut",
        "StructMatcherIn": "_trafficdirector_66_StructMatcherIn",
        "StructMatcherOut": "_trafficdirector_67_StructMatcherOut",
        "InlineScopedRouteConfigsIn": "_trafficdirector_68_InlineScopedRouteConfigsIn",
        "InlineScopedRouteConfigsOut": "_trafficdirector_69_InlineScopedRouteConfigsOut",
        "NodeIn": "_trafficdirector_70_NodeIn",
        "NodeOut": "_trafficdirector_71_NodeOut",
        "DynamicScopedRouteConfigsIn": "_trafficdirector_72_DynamicScopedRouteConfigsIn",
        "DynamicScopedRouteConfigsOut": "_trafficdirector_73_DynamicScopedRouteConfigsOut",
        "ClientStatusResponseIn": "_trafficdirector_74_ClientStatusResponseIn",
        "ClientStatusResponseOut": "_trafficdirector_75_ClientStatusResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ClustersConfigDumpIn"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "dynamicActiveClusters": t.array(
                t.proxy(renames["DynamicClusterIn"])
            ).optional(),
            "staticClusters": t.array(t.proxy(renames["StaticClusterIn"])).optional(),
            "dynamicWarmingClusters": t.array(
                t.proxy(renames["DynamicClusterIn"])
            ).optional(),
        }
    ).named(renames["ClustersConfigDumpIn"])
    types["ClustersConfigDumpOut"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "dynamicActiveClusters": t.array(
                t.proxy(renames["DynamicClusterOut"])
            ).optional(),
            "staticClusters": t.array(t.proxy(renames["StaticClusterOut"])).optional(),
            "dynamicWarmingClusters": t.array(
                t.proxy(renames["DynamicClusterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClustersConfigDumpOut"])
    types["DynamicListenerStateIn"] = t.struct(
        {
            "listener": t.struct({"_": t.string().optional()}).optional(),
            "versionInfo": t.string().optional(),
            "lastUpdated": t.string().optional(),
        }
    ).named(renames["DynamicListenerStateIn"])
    types["DynamicListenerStateOut"] = t.struct(
        {
            "listener": t.struct({"_": t.string().optional()}).optional(),
            "versionInfo": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicListenerStateOut"])
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
    types["StaticListenerIn"] = t.struct(
        {
            "listener": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
        }
    ).named(renames["StaticListenerIn"])
    types["StaticListenerOut"] = t.struct(
        {
            "listener": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StaticListenerOut"])
    types["NullMatchIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NullMatchIn"]
    )
    types["NullMatchOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NullMatchOut"])
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
    types["ClientStatusRequestIn"] = t.struct(
        {"nodeMatchers": t.array(t.proxy(renames["NodeMatcherIn"])).optional()}
    ).named(renames["ClientStatusRequestIn"])
    types["ClientStatusRequestOut"] = t.struct(
        {
            "nodeMatchers": t.array(t.proxy(renames["NodeMatcherOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientStatusRequestOut"])
    types["ExtensionIn"] = t.struct(
        {
            "version": t.proxy(renames["BuildVersionIn"]).optional(),
            "disabled": t.boolean().optional(),
            "name": t.string().optional(),
            "typeDescriptor": t.string().optional(),
            "category": t.string().optional(),
        }
    ).named(renames["ExtensionIn"])
    types["ExtensionOut"] = t.struct(
        {
            "version": t.proxy(renames["BuildVersionOut"]).optional(),
            "disabled": t.boolean().optional(),
            "name": t.string().optional(),
            "typeDescriptor": t.string().optional(),
            "category": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtensionOut"])
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
    types["DoubleRangeIn"] = t.struct(
        {"end": t.number().optional(), "start": t.number().optional()}
    ).named(renames["DoubleRangeIn"])
    types["DoubleRangeOut"] = t.struct(
        {
            "end": t.number().optional(),
            "start": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DoubleRangeOut"])
    types["ListMatcherIn"] = t.struct(
        {"oneOf": t.proxy(renames["ValueMatcherIn"]).optional()}
    ).named(renames["ListMatcherIn"])
    types["ListMatcherOut"] = t.struct(
        {
            "oneOf": t.proxy(renames["ValueMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMatcherOut"])
    types["ValueMatcherIn"] = t.struct(
        {
            "presentMatch": t.boolean().optional(),
            "nullMatch": t.proxy(renames["NullMatchIn"]).optional(),
            "listMatch": t.proxy(renames["ListMatcherIn"]).optional(),
            "boolMatch": t.boolean().optional(),
            "doubleMatch": t.proxy(renames["DoubleMatcherIn"]).optional(),
            "stringMatch": t.proxy(renames["StringMatcherIn"]).optional(),
        }
    ).named(renames["ValueMatcherIn"])
    types["ValueMatcherOut"] = t.struct(
        {
            "presentMatch": t.boolean().optional(),
            "nullMatch": t.proxy(renames["NullMatchOut"]).optional(),
            "listMatch": t.proxy(renames["ListMatcherOut"]).optional(),
            "boolMatch": t.boolean().optional(),
            "doubleMatch": t.proxy(renames["DoubleMatcherOut"]).optional(),
            "stringMatch": t.proxy(renames["StringMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueMatcherOut"])
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
    types["LocalityIn"] = t.struct(
        {
            "zone": t.string().optional(),
            "subZone": t.string().optional(),
            "region": t.string().optional(),
        }
    ).named(renames["LocalityIn"])
    types["LocalityOut"] = t.struct(
        {
            "zone": t.string().optional(),
            "subZone": t.string().optional(),
            "region": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocalityOut"])
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
    types["SocketAddressIn"] = t.struct(
        {
            "namedPort": t.string().optional(),
            "ipv4Compat": t.boolean().optional(),
            "portValue": t.integer(),
            "resolverName": t.string().optional(),
            "protocol": t.string(),
            "address": t.string().optional(),
        }
    ).named(renames["SocketAddressIn"])
    types["SocketAddressOut"] = t.struct(
        {
            "namedPort": t.string().optional(),
            "ipv4Compat": t.boolean().optional(),
            "portValue": t.integer(),
            "resolverName": t.string().optional(),
            "protocol": t.string(),
            "address": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocketAddressOut"])
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
    types["StringMatcherIn"] = t.struct(
        {
            "exact": t.string().optional(),
            "safeRegex": t.proxy(renames["RegexMatcherIn"]).optional(),
            "ignoreCase": t.boolean().optional(),
            "prefix": t.string().optional(),
            "regex": t.string().optional(),
            "suffix": t.string().optional(),
        }
    ).named(renames["StringMatcherIn"])
    types["StringMatcherOut"] = t.struct(
        {
            "exact": t.string().optional(),
            "safeRegex": t.proxy(renames["RegexMatcherOut"]).optional(),
            "ignoreCase": t.boolean().optional(),
            "prefix": t.string().optional(),
            "regex": t.string().optional(),
            "suffix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringMatcherOut"])
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
    types["UpdateFailureStateIn"] = t.struct(
        {
            "lastUpdateAttempt": t.string().optional(),
            "details": t.string().optional(),
            "failedConfiguration": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["UpdateFailureStateIn"])
    types["UpdateFailureStateOut"] = t.struct(
        {
            "lastUpdateAttempt": t.string().optional(),
            "details": t.string().optional(),
            "failedConfiguration": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UpdateFailureStateOut"])
    types["DynamicClusterIn"] = t.struct(
        {
            "cluster": t.struct({"_": t.string().optional()}).optional(),
            "versionInfo": t.string().optional(),
            "lastUpdated": t.string().optional(),
        }
    ).named(renames["DynamicClusterIn"])
    types["DynamicClusterOut"] = t.struct(
        {
            "cluster": t.struct({"_": t.string().optional()}).optional(),
            "versionInfo": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicClusterOut"])
    types["PathSegmentIn"] = t.struct({"key": t.string().optional()}).named(
        renames["PathSegmentIn"]
    )
    types["PathSegmentOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathSegmentOut"])
    types["DynamicListenerIn"] = t.struct(
        {
            "drainingState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
            "errorState": t.proxy(renames["UpdateFailureStateIn"]).optional(),
            "warmingState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
            "name": t.string().optional(),
            "activeState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
        }
    ).named(renames["DynamicListenerIn"])
    types["DynamicListenerOut"] = t.struct(
        {
            "drainingState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "errorState": t.proxy(renames["UpdateFailureStateOut"]).optional(),
            "warmingState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "name": t.string().optional(),
            "activeState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicListenerOut"])
    types["StaticClusterIn"] = t.struct(
        {
            "cluster": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
        }
    ).named(renames["StaticClusterIn"])
    types["StaticClusterOut"] = t.struct(
        {
            "cluster": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StaticClusterOut"])
    types["ListenersConfigDumpIn"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "dynamicListeners": t.array(
                t.proxy(renames["DynamicListenerIn"])
            ).optional(),
            "staticListeners": t.array(t.proxy(renames["StaticListenerIn"])).optional(),
        }
    ).named(renames["ListenersConfigDumpIn"])
    types["ListenersConfigDumpOut"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "dynamicListeners": t.array(
                t.proxy(renames["DynamicListenerOut"])
            ).optional(),
            "staticListeners": t.array(
                t.proxy(renames["StaticListenerOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListenersConfigDumpOut"])
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
    types["InlineScopedRouteConfigsIn"] = t.struct(
        {
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "lastUpdated": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["InlineScopedRouteConfigsIn"])
    types["InlineScopedRouteConfigsOut"] = t.struct(
        {
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "lastUpdated": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineScopedRouteConfigsOut"])
    types["NodeIn"] = t.struct(
        {
            "listeningAddresses": t.array(t.proxy(renames["AddressIn"])).optional(),
            "extensions": t.array(t.proxy(renames["ExtensionIn"])).optional(),
            "cluster": t.string().optional(),
            "buildVersion": t.string().optional(),
            "clientFeatures": t.array(t.string()).optional(),
            "userAgentName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "userAgentBuildVersion": t.proxy(renames["BuildVersionIn"]).optional(),
            "userAgentVersion": t.string().optional(),
            "locality": t.proxy(renames["LocalityIn"]).optional(),
            "id": t.string().optional(),
        }
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "listeningAddresses": t.array(t.proxy(renames["AddressOut"])).optional(),
            "extensions": t.array(t.proxy(renames["ExtensionOut"])).optional(),
            "cluster": t.string().optional(),
            "buildVersion": t.string().optional(),
            "clientFeatures": t.array(t.string()).optional(),
            "userAgentName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "userAgentBuildVersion": t.proxy(renames["BuildVersionOut"]).optional(),
            "userAgentVersion": t.string().optional(),
            "locality": t.proxy(renames["LocalityOut"]).optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["DynamicScopedRouteConfigsIn"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "name": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
        }
    ).named(renames["DynamicScopedRouteConfigsIn"])
    types["DynamicScopedRouteConfigsOut"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "lastUpdated": t.string().optional(),
            "name": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicScopedRouteConfigsOut"])
    types["ClientStatusResponseIn"] = t.struct(
        {"config": t.array(t.proxy(renames["ClientConfigIn"])).optional()}
    ).named(renames["ClientStatusResponseIn"])
    types["ClientStatusResponseOut"] = t.struct(
        {
            "config": t.array(t.proxy(renames["ClientConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientStatusResponseOut"])

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
