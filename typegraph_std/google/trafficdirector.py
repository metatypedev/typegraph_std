from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_trafficdirector() -> Import:
    trafficdirector = HTTPRuntime("https://trafficdirector.googleapis.com/")

    renames = {
        "ErrorResponse": "_trafficdirector_1_ErrorResponse",
        "DynamicRouteConfigIn": "_trafficdirector_2_DynamicRouteConfigIn",
        "DynamicRouteConfigOut": "_trafficdirector_3_DynamicRouteConfigOut",
        "ScopedRoutesConfigDumpIn": "_trafficdirector_4_ScopedRoutesConfigDumpIn",
        "ScopedRoutesConfigDumpOut": "_trafficdirector_5_ScopedRoutesConfigDumpOut",
        "ListMatcherIn": "_trafficdirector_6_ListMatcherIn",
        "ListMatcherOut": "_trafficdirector_7_ListMatcherOut",
        "GoogleRE2In": "_trafficdirector_8_GoogleRE2In",
        "GoogleRE2Out": "_trafficdirector_9_GoogleRE2Out",
        "PipeIn": "_trafficdirector_10_PipeIn",
        "PipeOut": "_trafficdirector_11_PipeOut",
        "SocketAddressIn": "_trafficdirector_12_SocketAddressIn",
        "SocketAddressOut": "_trafficdirector_13_SocketAddressOut",
        "ClientStatusRequestIn": "_trafficdirector_14_ClientStatusRequestIn",
        "ClientStatusRequestOut": "_trafficdirector_15_ClientStatusRequestOut",
        "StringMatcherIn": "_trafficdirector_16_StringMatcherIn",
        "StringMatcherOut": "_trafficdirector_17_StringMatcherOut",
        "StaticRouteConfigIn": "_trafficdirector_18_StaticRouteConfigIn",
        "StaticRouteConfigOut": "_trafficdirector_19_StaticRouteConfigOut",
        "NodeIn": "_trafficdirector_20_NodeIn",
        "NodeOut": "_trafficdirector_21_NodeOut",
        "ClustersConfigDumpIn": "_trafficdirector_22_ClustersConfigDumpIn",
        "ClustersConfigDumpOut": "_trafficdirector_23_ClustersConfigDumpOut",
        "NullMatchIn": "_trafficdirector_24_NullMatchIn",
        "NullMatchOut": "_trafficdirector_25_NullMatchOut",
        "RoutesConfigDumpIn": "_trafficdirector_26_RoutesConfigDumpIn",
        "RoutesConfigDumpOut": "_trafficdirector_27_RoutesConfigDumpOut",
        "DynamicScopedRouteConfigsIn": "_trafficdirector_28_DynamicScopedRouteConfigsIn",
        "DynamicScopedRouteConfigsOut": "_trafficdirector_29_DynamicScopedRouteConfigsOut",
        "DynamicListenerIn": "_trafficdirector_30_DynamicListenerIn",
        "DynamicListenerOut": "_trafficdirector_31_DynamicListenerOut",
        "PathSegmentIn": "_trafficdirector_32_PathSegmentIn",
        "PathSegmentOut": "_trafficdirector_33_PathSegmentOut",
        "ListenersConfigDumpIn": "_trafficdirector_34_ListenersConfigDumpIn",
        "ListenersConfigDumpOut": "_trafficdirector_35_ListenersConfigDumpOut",
        "DynamicClusterIn": "_trafficdirector_36_DynamicClusterIn",
        "DynamicClusterOut": "_trafficdirector_37_DynamicClusterOut",
        "ClientStatusResponseIn": "_trafficdirector_38_ClientStatusResponseIn",
        "ClientStatusResponseOut": "_trafficdirector_39_ClientStatusResponseOut",
        "UpdateFailureStateIn": "_trafficdirector_40_UpdateFailureStateIn",
        "UpdateFailureStateOut": "_trafficdirector_41_UpdateFailureStateOut",
        "SemanticVersionIn": "_trafficdirector_42_SemanticVersionIn",
        "SemanticVersionOut": "_trafficdirector_43_SemanticVersionOut",
        "NodeMatcherIn": "_trafficdirector_44_NodeMatcherIn",
        "NodeMatcherOut": "_trafficdirector_45_NodeMatcherOut",
        "LocalityIn": "_trafficdirector_46_LocalityIn",
        "LocalityOut": "_trafficdirector_47_LocalityOut",
        "StaticClusterIn": "_trafficdirector_48_StaticClusterIn",
        "StaticClusterOut": "_trafficdirector_49_StaticClusterOut",
        "ValueMatcherIn": "_trafficdirector_50_ValueMatcherIn",
        "ValueMatcherOut": "_trafficdirector_51_ValueMatcherOut",
        "ClientConfigIn": "_trafficdirector_52_ClientConfigIn",
        "ClientConfigOut": "_trafficdirector_53_ClientConfigOut",
        "StructMatcherIn": "_trafficdirector_54_StructMatcherIn",
        "StructMatcherOut": "_trafficdirector_55_StructMatcherOut",
        "StaticListenerIn": "_trafficdirector_56_StaticListenerIn",
        "StaticListenerOut": "_trafficdirector_57_StaticListenerOut",
        "DoubleMatcherIn": "_trafficdirector_58_DoubleMatcherIn",
        "DoubleMatcherOut": "_trafficdirector_59_DoubleMatcherOut",
        "DynamicListenerStateIn": "_trafficdirector_60_DynamicListenerStateIn",
        "DynamicListenerStateOut": "_trafficdirector_61_DynamicListenerStateOut",
        "BuildVersionIn": "_trafficdirector_62_BuildVersionIn",
        "BuildVersionOut": "_trafficdirector_63_BuildVersionOut",
        "ExtensionIn": "_trafficdirector_64_ExtensionIn",
        "ExtensionOut": "_trafficdirector_65_ExtensionOut",
        "AddressIn": "_trafficdirector_66_AddressIn",
        "AddressOut": "_trafficdirector_67_AddressOut",
        "InlineScopedRouteConfigsIn": "_trafficdirector_68_InlineScopedRouteConfigsIn",
        "InlineScopedRouteConfigsOut": "_trafficdirector_69_InlineScopedRouteConfigsOut",
        "DoubleRangeIn": "_trafficdirector_70_DoubleRangeIn",
        "DoubleRangeOut": "_trafficdirector_71_DoubleRangeOut",
        "PerXdsConfigIn": "_trafficdirector_72_PerXdsConfigIn",
        "PerXdsConfigOut": "_trafficdirector_73_PerXdsConfigOut",
        "RegexMatcherIn": "_trafficdirector_74_RegexMatcherIn",
        "RegexMatcherOut": "_trafficdirector_75_RegexMatcherOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DynamicRouteConfigIn"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
        }
    ).named(renames["DynamicRouteConfigIn"])
    types["DynamicRouteConfigOut"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "routeConfig": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicRouteConfigOut"])
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
    types["ListMatcherIn"] = t.struct(
        {"oneOf": t.proxy(renames["ValueMatcherIn"]).optional()}
    ).named(renames["ListMatcherIn"])
    types["ListMatcherOut"] = t.struct(
        {
            "oneOf": t.proxy(renames["ValueMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListMatcherOut"])
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
        {"mode": t.integer().optional(), "path": t.string().optional()}
    ).named(renames["PipeIn"])
    types["PipeOut"] = t.struct(
        {
            "mode": t.integer().optional(),
            "path": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PipeOut"])
    types["SocketAddressIn"] = t.struct(
        {
            "address": t.string().optional(),
            "namedPort": t.string().optional(),
            "resolverName": t.string().optional(),
            "ipv4Compat": t.boolean().optional(),
            "protocol": t.string(),
            "portValue": t.integer(),
        }
    ).named(renames["SocketAddressIn"])
    types["SocketAddressOut"] = t.struct(
        {
            "address": t.string().optional(),
            "namedPort": t.string().optional(),
            "resolverName": t.string().optional(),
            "ipv4Compat": t.boolean().optional(),
            "protocol": t.string(),
            "portValue": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SocketAddressOut"])
    types["ClientStatusRequestIn"] = t.struct(
        {"nodeMatchers": t.array(t.proxy(renames["NodeMatcherIn"])).optional()}
    ).named(renames["ClientStatusRequestIn"])
    types["ClientStatusRequestOut"] = t.struct(
        {
            "nodeMatchers": t.array(t.proxy(renames["NodeMatcherOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientStatusRequestOut"])
    types["StringMatcherIn"] = t.struct(
        {
            "ignoreCase": t.boolean().optional(),
            "exact": t.string().optional(),
            "safeRegex": t.proxy(renames["RegexMatcherIn"]).optional(),
            "prefix": t.string().optional(),
            "regex": t.string().optional(),
            "suffix": t.string().optional(),
        }
    ).named(renames["StringMatcherIn"])
    types["StringMatcherOut"] = t.struct(
        {
            "ignoreCase": t.boolean().optional(),
            "exact": t.string().optional(),
            "safeRegex": t.proxy(renames["RegexMatcherOut"]).optional(),
            "prefix": t.string().optional(),
            "regex": t.string().optional(),
            "suffix": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StringMatcherOut"])
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
    types["NodeIn"] = t.struct(
        {
            "buildVersion": t.string().optional(),
            "clientFeatures": t.array(t.string()).optional(),
            "userAgentVersion": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locality": t.proxy(renames["LocalityIn"]).optional(),
            "extensions": t.array(t.proxy(renames["ExtensionIn"])).optional(),
            "listeningAddresses": t.array(t.proxy(renames["AddressIn"])).optional(),
            "cluster": t.string().optional(),
            "userAgentName": t.string().optional(),
            "id": t.string().optional(),
            "userAgentBuildVersion": t.proxy(renames["BuildVersionIn"]).optional(),
        }
    ).named(renames["NodeIn"])
    types["NodeOut"] = t.struct(
        {
            "buildVersion": t.string().optional(),
            "clientFeatures": t.array(t.string()).optional(),
            "userAgentVersion": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "locality": t.proxy(renames["LocalityOut"]).optional(),
            "extensions": t.array(t.proxy(renames["ExtensionOut"])).optional(),
            "listeningAddresses": t.array(t.proxy(renames["AddressOut"])).optional(),
            "cluster": t.string().optional(),
            "userAgentName": t.string().optional(),
            "id": t.string().optional(),
            "userAgentBuildVersion": t.proxy(renames["BuildVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NodeOut"])
    types["ClustersConfigDumpIn"] = t.struct(
        {
            "dynamicWarmingClusters": t.array(
                t.proxy(renames["DynamicClusterIn"])
            ).optional(),
            "staticClusters": t.array(t.proxy(renames["StaticClusterIn"])).optional(),
            "versionInfo": t.string().optional(),
            "dynamicActiveClusters": t.array(
                t.proxy(renames["DynamicClusterIn"])
            ).optional(),
        }
    ).named(renames["ClustersConfigDumpIn"])
    types["ClustersConfigDumpOut"] = t.struct(
        {
            "dynamicWarmingClusters": t.array(
                t.proxy(renames["DynamicClusterOut"])
            ).optional(),
            "staticClusters": t.array(t.proxy(renames["StaticClusterOut"])).optional(),
            "versionInfo": t.string().optional(),
            "dynamicActiveClusters": t.array(
                t.proxy(renames["DynamicClusterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClustersConfigDumpOut"])
    types["NullMatchIn"] = t.struct({"_": t.string().optional()}).named(
        renames["NullMatchIn"]
    )
    types["NullMatchOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["NullMatchOut"])
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
    types["DynamicScopedRouteConfigsIn"] = t.struct(
        {
            "name": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "lastUpdated": t.string().optional(),
            "versionInfo": t.string().optional(),
        }
    ).named(renames["DynamicScopedRouteConfigsIn"])
    types["DynamicScopedRouteConfigsOut"] = t.struct(
        {
            "name": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "lastUpdated": t.string().optional(),
            "versionInfo": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicScopedRouteConfigsOut"])
    types["DynamicListenerIn"] = t.struct(
        {
            "errorState": t.proxy(renames["UpdateFailureStateIn"]).optional(),
            "name": t.string().optional(),
            "drainingState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
            "warmingState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
            "activeState": t.proxy(renames["DynamicListenerStateIn"]).optional(),
        }
    ).named(renames["DynamicListenerIn"])
    types["DynamicListenerOut"] = t.struct(
        {
            "errorState": t.proxy(renames["UpdateFailureStateOut"]).optional(),
            "name": t.string().optional(),
            "drainingState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "warmingState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "activeState": t.proxy(renames["DynamicListenerStateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicListenerOut"])
    types["PathSegmentIn"] = t.struct({"key": t.string().optional()}).named(
        renames["PathSegmentIn"]
    )
    types["PathSegmentOut"] = t.struct(
        {
            "key": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PathSegmentOut"])
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
    types["DynamicClusterIn"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "cluster": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
        }
    ).named(renames["DynamicClusterIn"])
    types["DynamicClusterOut"] = t.struct(
        {
            "versionInfo": t.string().optional(),
            "cluster": t.struct({"_": t.string().optional()}).optional(),
            "lastUpdated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DynamicClusterOut"])
    types["ClientStatusResponseIn"] = t.struct(
        {"config": t.array(t.proxy(renames["ClientConfigIn"])).optional()}
    ).named(renames["ClientStatusResponseIn"])
    types["ClientStatusResponseOut"] = t.struct(
        {
            "config": t.array(t.proxy(renames["ClientConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClientStatusResponseOut"])
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
    types["SemanticVersionIn"] = t.struct(
        {"majorNumber": t.integer(), "minorNumber": t.integer(), "patch": t.integer()}
    ).named(renames["SemanticVersionIn"])
    types["SemanticVersionOut"] = t.struct(
        {
            "majorNumber": t.integer(),
            "minorNumber": t.integer(),
            "patch": t.integer(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SemanticVersionOut"])
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
    types["ValueMatcherIn"] = t.struct(
        {
            "presentMatch": t.boolean().optional(),
            "boolMatch": t.boolean().optional(),
            "listMatch": t.proxy(renames["ListMatcherIn"]).optional(),
            "doubleMatch": t.proxy(renames["DoubleMatcherIn"]).optional(),
            "nullMatch": t.proxy(renames["NullMatchIn"]).optional(),
            "stringMatch": t.proxy(renames["StringMatcherIn"]).optional(),
        }
    ).named(renames["ValueMatcherIn"])
    types["ValueMatcherOut"] = t.struct(
        {
            "presentMatch": t.boolean().optional(),
            "boolMatch": t.boolean().optional(),
            "listMatch": t.proxy(renames["ListMatcherOut"]).optional(),
            "doubleMatch": t.proxy(renames["DoubleMatcherOut"]).optional(),
            "nullMatch": t.proxy(renames["NullMatchOut"]).optional(),
            "stringMatch": t.proxy(renames["StringMatcherOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValueMatcherOut"])
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
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "version": t.proxy(renames["SemanticVersionIn"]).optional(),
        }
    ).named(renames["BuildVersionIn"])
    types["BuildVersionOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "version": t.proxy(renames["SemanticVersionOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BuildVersionOut"])
    types["ExtensionIn"] = t.struct(
        {
            "version": t.proxy(renames["BuildVersionIn"]).optional(),
            "typeDescriptor": t.string().optional(),
            "disabled": t.boolean().optional(),
            "category": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ExtensionIn"])
    types["ExtensionOut"] = t.struct(
        {
            "version": t.proxy(renames["BuildVersionOut"]).optional(),
            "typeDescriptor": t.string().optional(),
            "disabled": t.boolean().optional(),
            "category": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExtensionOut"])
    types["AddressIn"] = t.struct(
        {
            "pipe": t.proxy(renames["PipeIn"]),
            "socketAddress": t.proxy(renames["SocketAddressIn"]),
        }
    ).named(renames["AddressIn"])
    types["AddressOut"] = t.struct(
        {
            "pipe": t.proxy(renames["PipeOut"]),
            "socketAddress": t.proxy(renames["SocketAddressOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AddressOut"])
    types["InlineScopedRouteConfigsIn"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "name": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
        }
    ).named(renames["InlineScopedRouteConfigsIn"])
    types["InlineScopedRouteConfigsOut"] = t.struct(
        {
            "lastUpdated": t.string().optional(),
            "name": t.string().optional(),
            "scopedRouteConfigs": t.array(
                t.struct({"_": t.string().optional()})
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["InlineScopedRouteConfigsOut"])
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
    types["PerXdsConfigIn"] = t.struct(
        {
            "scopedRouteConfig": t.proxy(renames["ScopedRoutesConfigDumpIn"]),
            "routeConfig": t.proxy(renames["RoutesConfigDumpIn"]),
            "listenerConfig": t.proxy(renames["ListenersConfigDumpIn"]),
            "clusterConfig": t.proxy(renames["ClustersConfigDumpIn"]),
            "status": t.string(),
        }
    ).named(renames["PerXdsConfigIn"])
    types["PerXdsConfigOut"] = t.struct(
        {
            "scopedRouteConfig": t.proxy(renames["ScopedRoutesConfigDumpOut"]),
            "routeConfig": t.proxy(renames["RoutesConfigDumpOut"]),
            "listenerConfig": t.proxy(renames["ListenersConfigDumpOut"]),
            "clusterConfig": t.proxy(renames["ClustersConfigDumpOut"]),
            "status": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PerXdsConfigOut"])
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
