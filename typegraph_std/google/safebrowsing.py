from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_safebrowsing() -> Import:
    safebrowsing = HTTPRuntime("https://safebrowsing.googleapis.com/")

    renames = {
        "ErrorResponse": "_safebrowsing_1_ErrorResponse",
        "GoogleProtobufEmptyIn": "_safebrowsing_2_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_safebrowsing_3_GoogleProtobufEmptyOut",
        "GoogleSecuritySafebrowsingV4ThreatMatchIn": "_safebrowsing_4_GoogleSecuritySafebrowsingV4ThreatMatchIn",
        "GoogleSecuritySafebrowsingV4ThreatMatchOut": "_safebrowsing_5_GoogleSecuritySafebrowsingV4ThreatMatchOut",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsIn": "_safebrowsing_6_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsIn",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsOut": "_safebrowsing_7_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsOut",
        "GoogleSecuritySafebrowsingV4ThreatHitIn": "_safebrowsing_8_GoogleSecuritySafebrowsingV4ThreatHitIn",
        "GoogleSecuritySafebrowsingV4ThreatHitOut": "_safebrowsing_9_GoogleSecuritySafebrowsingV4ThreatHitOut",
        "GoogleSecuritySafebrowsingV4ThreatInfoIn": "_safebrowsing_10_GoogleSecuritySafebrowsingV4ThreatInfoIn",
        "GoogleSecuritySafebrowsingV4ThreatInfoOut": "_safebrowsing_11_GoogleSecuritySafebrowsingV4ThreatInfoOut",
        "GoogleSecuritySafebrowsingV4FindFullHashesRequestIn": "_safebrowsing_12_GoogleSecuritySafebrowsingV4FindFullHashesRequestIn",
        "GoogleSecuritySafebrowsingV4FindFullHashesRequestOut": "_safebrowsing_13_GoogleSecuritySafebrowsingV4FindFullHashesRequestOut",
        "GoogleSecuritySafebrowsingV4FindFullHashesResponseIn": "_safebrowsing_14_GoogleSecuritySafebrowsingV4FindFullHashesResponseIn",
        "GoogleSecuritySafebrowsingV4FindFullHashesResponseOut": "_safebrowsing_15_GoogleSecuritySafebrowsingV4FindFullHashesResponseOut",
        "GoogleSecuritySafebrowsingV4ChecksumIn": "_safebrowsing_16_GoogleSecuritySafebrowsingV4ChecksumIn",
        "GoogleSecuritySafebrowsingV4ChecksumOut": "_safebrowsing_17_GoogleSecuritySafebrowsingV4ChecksumOut",
        "GoogleSecuritySafebrowsingV4FindThreatMatchesRequestIn": "_safebrowsing_18_GoogleSecuritySafebrowsingV4FindThreatMatchesRequestIn",
        "GoogleSecuritySafebrowsingV4FindThreatMatchesRequestOut": "_safebrowsing_19_GoogleSecuritySafebrowsingV4FindThreatMatchesRequestOut",
        "GoogleSecuritySafebrowsingV4FindThreatMatchesResponseIn": "_safebrowsing_20_GoogleSecuritySafebrowsingV4FindThreatMatchesResponseIn",
        "GoogleSecuritySafebrowsingV4FindThreatMatchesResponseOut": "_safebrowsing_21_GoogleSecuritySafebrowsingV4FindThreatMatchesResponseOut",
        "GoogleSecuritySafebrowsingV4ThreatHitThreatSourceIn": "_safebrowsing_22_GoogleSecuritySafebrowsingV4ThreatHitThreatSourceIn",
        "GoogleSecuritySafebrowsingV4ThreatHitThreatSourceOut": "_safebrowsing_23_GoogleSecuritySafebrowsingV4ThreatHitThreatSourceOut",
        "GoogleSecuritySafebrowsingV4ClientInfoIn": "_safebrowsing_24_GoogleSecuritySafebrowsingV4ClientInfoIn",
        "GoogleSecuritySafebrowsingV4ClientInfoOut": "_safebrowsing_25_GoogleSecuritySafebrowsingV4ClientInfoOut",
        "GoogleSecuritySafebrowsingV4RawHashesIn": "_safebrowsing_26_GoogleSecuritySafebrowsingV4RawHashesIn",
        "GoogleSecuritySafebrowsingV4RawHashesOut": "_safebrowsing_27_GoogleSecuritySafebrowsingV4RawHashesOut",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestIn": "_safebrowsing_28_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestIn",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestOut": "_safebrowsing_29_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestOut",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseIn": "_safebrowsing_30_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseIn",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseOut": "_safebrowsing_31_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseOut",
        "GoogleSecuritySafebrowsingV4RawIndicesIn": "_safebrowsing_32_GoogleSecuritySafebrowsingV4RawIndicesIn",
        "GoogleSecuritySafebrowsingV4RawIndicesOut": "_safebrowsing_33_GoogleSecuritySafebrowsingV4RawIndicesOut",
        "GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryIn": "_safebrowsing_34_GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryIn",
        "GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryOut": "_safebrowsing_35_GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryOut",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseIn": "_safebrowsing_36_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseIn",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseOut": "_safebrowsing_37_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseOut",
        "GoogleSecuritySafebrowsingV4ThreatEntryMetadataIn": "_safebrowsing_38_GoogleSecuritySafebrowsingV4ThreatEntryMetadataIn",
        "GoogleSecuritySafebrowsingV4ThreatEntryMetadataOut": "_safebrowsing_39_GoogleSecuritySafebrowsingV4ThreatEntryMetadataOut",
        "GoogleSecuritySafebrowsingV4ListThreatListsResponseIn": "_safebrowsing_40_GoogleSecuritySafebrowsingV4ListThreatListsResponseIn",
        "GoogleSecuritySafebrowsingV4ListThreatListsResponseOut": "_safebrowsing_41_GoogleSecuritySafebrowsingV4ListThreatListsResponseOut",
        "GoogleSecuritySafebrowsingV4ThreatListDescriptorIn": "_safebrowsing_42_GoogleSecuritySafebrowsingV4ThreatListDescriptorIn",
        "GoogleSecuritySafebrowsingV4ThreatListDescriptorOut": "_safebrowsing_43_GoogleSecuritySafebrowsingV4ThreatListDescriptorOut",
        "GoogleSecuritySafebrowsingV4ThreatEntryIn": "_safebrowsing_44_GoogleSecuritySafebrowsingV4ThreatEntryIn",
        "GoogleSecuritySafebrowsingV4ThreatEntryOut": "_safebrowsing_45_GoogleSecuritySafebrowsingV4ThreatEntryOut",
        "GoogleSecuritySafebrowsingV4ThreatHitUserInfoIn": "_safebrowsing_46_GoogleSecuritySafebrowsingV4ThreatHitUserInfoIn",
        "GoogleSecuritySafebrowsingV4ThreatHitUserInfoOut": "_safebrowsing_47_GoogleSecuritySafebrowsingV4ThreatHitUserInfoOut",
        "GoogleSecuritySafebrowsingV4ThreatEntrySetIn": "_safebrowsing_48_GoogleSecuritySafebrowsingV4ThreatEntrySetIn",
        "GoogleSecuritySafebrowsingV4ThreatEntrySetOut": "_safebrowsing_49_GoogleSecuritySafebrowsingV4ThreatEntrySetOut",
        "GoogleSecuritySafebrowsingV4RiceDeltaEncodingIn": "_safebrowsing_50_GoogleSecuritySafebrowsingV4RiceDeltaEncodingIn",
        "GoogleSecuritySafebrowsingV4RiceDeltaEncodingOut": "_safebrowsing_51_GoogleSecuritySafebrowsingV4RiceDeltaEncodingOut",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestIn": "_safebrowsing_52_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestIn",
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestOut": "_safebrowsing_53_GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleSecuritySafebrowsingV4ThreatMatchIn"] = t.struct(
        {
            "platformType": t.string().optional(),
            "threat": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatEntryIn"]
            ).optional(),
            "cacheDuration": t.string().optional(),
            "threatEntryType": t.string().optional(),
            "threatType": t.string().optional(),
            "threatEntryMetadata": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatEntryMetadataIn"]
            ).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatMatchIn"])
    types["GoogleSecuritySafebrowsingV4ThreatMatchOut"] = t.struct(
        {
            "platformType": t.string().optional(),
            "threat": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatEntryOut"]
            ).optional(),
            "cacheDuration": t.string().optional(),
            "threatEntryType": t.string().optional(),
            "threatType": t.string().optional(),
            "threatEntryMetadata": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatEntryMetadataOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatMatchOut"])
    types[
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsIn"
    ] = t.struct(
        {
            "language": t.string().optional(),
            "maxUpdateEntries": t.integer().optional(),
            "maxDatabaseEntries": t.integer().optional(),
            "deviceLocation": t.string().optional(),
            "region": t.string().optional(),
            "supportedCompressions": t.array(t.string()).optional(),
        }
    ).named(
        renames[
            "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsIn"
        ]
    )
    types[
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsOut"
    ] = t.struct(
        {
            "language": t.string().optional(),
            "maxUpdateEntries": t.integer().optional(),
            "maxDatabaseEntries": t.integer().optional(),
            "deviceLocation": t.string().optional(),
            "region": t.string().optional(),
            "supportedCompressions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsOut"
        ]
    )
    types["GoogleSecuritySafebrowsingV4ThreatHitIn"] = t.struct(
        {
            "platformType": t.string().optional(),
            "resources": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatHitThreatSourceIn"])
            ).optional(),
            "clientInfo": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
            ).optional(),
            "userInfo": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatHitUserInfoIn"]
            ).optional(),
            "threatType": t.string().optional(),
            "entry": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatEntryIn"]
            ).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatHitIn"])
    types["GoogleSecuritySafebrowsingV4ThreatHitOut"] = t.struct(
        {
            "platformType": t.string().optional(),
            "resources": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatHitThreatSourceOut"])
            ).optional(),
            "clientInfo": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoOut"]
            ).optional(),
            "userInfo": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatHitUserInfoOut"]
            ).optional(),
            "threatType": t.string().optional(),
            "entry": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatEntryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatHitOut"])
    types["GoogleSecuritySafebrowsingV4ThreatInfoIn"] = t.struct(
        {
            "platformTypes": t.array(t.string()).optional(),
            "threatEntryTypes": t.array(t.string()).optional(),
            "threatTypes": t.array(t.string()).optional(),
            "threatEntries": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatEntryIn"])
            ).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatInfoIn"])
    types["GoogleSecuritySafebrowsingV4ThreatInfoOut"] = t.struct(
        {
            "platformTypes": t.array(t.string()).optional(),
            "threatEntryTypes": t.array(t.string()).optional(),
            "threatTypes": t.array(t.string()).optional(),
            "threatEntries": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatEntryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatInfoOut"])
    types["GoogleSecuritySafebrowsingV4FindFullHashesRequestIn"] = t.struct(
        {
            "threatInfo": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatInfoIn"]
            ).optional(),
            "clientStates": t.array(t.string()).optional(),
            "apiClient": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
            ).optional(),
            "client": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FindFullHashesRequestIn"])
    types["GoogleSecuritySafebrowsingV4FindFullHashesRequestOut"] = t.struct(
        {
            "threatInfo": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatInfoOut"]
            ).optional(),
            "clientStates": t.array(t.string()).optional(),
            "apiClient": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoOut"]
            ).optional(),
            "client": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FindFullHashesRequestOut"])
    types["GoogleSecuritySafebrowsingV4FindFullHashesResponseIn"] = t.struct(
        {
            "negativeCacheDuration": t.string().optional(),
            "matches": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatMatchIn"])
            ).optional(),
            "minimumWaitDuration": t.string().optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FindFullHashesResponseIn"])
    types["GoogleSecuritySafebrowsingV4FindFullHashesResponseOut"] = t.struct(
        {
            "negativeCacheDuration": t.string().optional(),
            "matches": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatMatchOut"])
            ).optional(),
            "minimumWaitDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FindFullHashesResponseOut"])
    types["GoogleSecuritySafebrowsingV4ChecksumIn"] = t.struct(
        {"sha256": t.string().optional()}
    ).named(renames["GoogleSecuritySafebrowsingV4ChecksumIn"])
    types["GoogleSecuritySafebrowsingV4ChecksumOut"] = t.struct(
        {
            "sha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ChecksumOut"])
    types["GoogleSecuritySafebrowsingV4FindThreatMatchesRequestIn"] = t.struct(
        {
            "client": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
            ).optional(),
            "threatInfo": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatInfoIn"]
            ).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FindThreatMatchesRequestIn"])
    types["GoogleSecuritySafebrowsingV4FindThreatMatchesRequestOut"] = t.struct(
        {
            "client": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoOut"]
            ).optional(),
            "threatInfo": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ThreatInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FindThreatMatchesRequestOut"])
    types["GoogleSecuritySafebrowsingV4FindThreatMatchesResponseIn"] = t.struct(
        {
            "matches": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatMatchIn"])
            ).optional()
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FindThreatMatchesResponseIn"])
    types["GoogleSecuritySafebrowsingV4FindThreatMatchesResponseOut"] = t.struct(
        {
            "matches": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatMatchOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FindThreatMatchesResponseOut"])
    types["GoogleSecuritySafebrowsingV4ThreatHitThreatSourceIn"] = t.struct(
        {
            "url": t.string().optional(),
            "referrer": t.string().optional(),
            "type": t.string().optional(),
            "remoteIp": t.string().optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatHitThreatSourceIn"])
    types["GoogleSecuritySafebrowsingV4ThreatHitThreatSourceOut"] = t.struct(
        {
            "url": t.string().optional(),
            "referrer": t.string().optional(),
            "type": t.string().optional(),
            "remoteIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatHitThreatSourceOut"])
    types["GoogleSecuritySafebrowsingV4ClientInfoIn"] = t.struct(
        {"clientId": t.string().optional(), "clientVersion": t.string().optional()}
    ).named(renames["GoogleSecuritySafebrowsingV4ClientInfoIn"])
    types["GoogleSecuritySafebrowsingV4ClientInfoOut"] = t.struct(
        {
            "clientId": t.string().optional(),
            "clientVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ClientInfoOut"])
    types["GoogleSecuritySafebrowsingV4RawHashesIn"] = t.struct(
        {"rawHashes": t.string().optional(), "prefixSize": t.integer().optional()}
    ).named(renames["GoogleSecuritySafebrowsingV4RawHashesIn"])
    types["GoogleSecuritySafebrowsingV4RawHashesOut"] = t.struct(
        {
            "rawHashes": t.string().optional(),
            "prefixSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4RawHashesOut"])
    types[
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestIn"
    ] = t.struct(
        {
            "constraints": t.proxy(
                renames[
                    "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsIn"
                ]
            ).optional(),
            "platformType": t.string().optional(),
            "state": t.string().optional(),
            "threatType": t.string().optional(),
            "threatEntryType": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestIn"
        ]
    )
    types[
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestOut"
    ] = t.struct(
        {
            "constraints": t.proxy(
                renames[
                    "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestConstraintsOut"
                ]
            ).optional(),
            "platformType": t.string().optional(),
            "state": t.string().optional(),
            "threatType": t.string().optional(),
            "threatEntryType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestOut"
        ]
    )
    types["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseIn"] = t.struct(
        {
            "minimumWaitDuration": t.string().optional(),
            "listUpdateResponses": t.array(
                t.proxy(
                    renames[
                        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseIn"])
    types["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseOut"] = t.struct(
        {
            "minimumWaitDuration": t.string().optional(),
            "listUpdateResponses": t.array(
                t.proxy(
                    renames[
                        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseOut"])
    types["GoogleSecuritySafebrowsingV4RawIndicesIn"] = t.struct(
        {"indices": t.array(t.integer()).optional()}
    ).named(renames["GoogleSecuritySafebrowsingV4RawIndicesIn"])
    types["GoogleSecuritySafebrowsingV4RawIndicesOut"] = t.struct(
        {
            "indices": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4RawIndicesOut"])
    types["GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryIn"] = t.struct(
        {"key": t.string().optional(), "value": t.string().optional()}
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryIn"])
    types["GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryOut"] = t.struct(
        {
            "key": t.string().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryOut"])
    types[
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseIn"
    ] = t.struct(
        {
            "threatEntryType": t.string().optional(),
            "newClientState": t.string().optional(),
            "removals": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatEntrySetIn"])
            ).optional(),
            "threatType": t.string().optional(),
            "additions": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatEntrySetIn"])
            ).optional(),
            "platformType": t.string().optional(),
            "checksum": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ChecksumIn"]
            ).optional(),
            "responseType": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseIn"
        ]
    )
    types[
        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseOut"
    ] = t.struct(
        {
            "threatEntryType": t.string().optional(),
            "newClientState": t.string().optional(),
            "removals": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatEntrySetOut"])
            ).optional(),
            "threatType": t.string().optional(),
            "additions": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatEntrySetOut"])
            ).optional(),
            "platformType": t.string().optional(),
            "checksum": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ChecksumOut"]
            ).optional(),
            "responseType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseListUpdateResponseOut"
        ]
    )
    types["GoogleSecuritySafebrowsingV4ThreatEntryMetadataIn"] = t.struct(
        {
            "entries": t.array(
                t.proxy(
                    renames[
                        "GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryIn"
                    ]
                )
            ).optional()
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatEntryMetadataIn"])
    types["GoogleSecuritySafebrowsingV4ThreatEntryMetadataOut"] = t.struct(
        {
            "entries": t.array(
                t.proxy(
                    renames[
                        "GoogleSecuritySafebrowsingV4ThreatEntryMetadataMetadataEntryOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatEntryMetadataOut"])
    types["GoogleSecuritySafebrowsingV4ListThreatListsResponseIn"] = t.struct(
        {
            "threatLists": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatListDescriptorIn"])
            ).optional()
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ListThreatListsResponseIn"])
    types["GoogleSecuritySafebrowsingV4ListThreatListsResponseOut"] = t.struct(
        {
            "threatLists": t.array(
                t.proxy(renames["GoogleSecuritySafebrowsingV4ThreatListDescriptorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ListThreatListsResponseOut"])
    types["GoogleSecuritySafebrowsingV4ThreatListDescriptorIn"] = t.struct(
        {
            "threatEntryType": t.string().optional(),
            "platformType": t.string().optional(),
            "threatType": t.string().optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatListDescriptorIn"])
    types["GoogleSecuritySafebrowsingV4ThreatListDescriptorOut"] = t.struct(
        {
            "threatEntryType": t.string().optional(),
            "platformType": t.string().optional(),
            "threatType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatListDescriptorOut"])
    types["GoogleSecuritySafebrowsingV4ThreatEntryIn"] = t.struct(
        {
            "hash": t.string().optional(),
            "digest": t.string().optional(),
            "url": t.string().optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatEntryIn"])
    types["GoogleSecuritySafebrowsingV4ThreatEntryOut"] = t.struct(
        {
            "hash": t.string().optional(),
            "digest": t.string().optional(),
            "url": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatEntryOut"])
    types["GoogleSecuritySafebrowsingV4ThreatHitUserInfoIn"] = t.struct(
        {"regionCode": t.string().optional(), "userId": t.string().optional()}
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatHitUserInfoIn"])
    types["GoogleSecuritySafebrowsingV4ThreatHitUserInfoOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatHitUserInfoOut"])
    types["GoogleSecuritySafebrowsingV4ThreatEntrySetIn"] = t.struct(
        {
            "compressionType": t.string().optional(),
            "riceIndices": t.proxy(
                renames["GoogleSecuritySafebrowsingV4RiceDeltaEncodingIn"]
            ).optional(),
            "rawIndices": t.proxy(
                renames["GoogleSecuritySafebrowsingV4RawIndicesIn"]
            ).optional(),
            "rawHashes": t.proxy(
                renames["GoogleSecuritySafebrowsingV4RawHashesIn"]
            ).optional(),
            "riceHashes": t.proxy(
                renames["GoogleSecuritySafebrowsingV4RiceDeltaEncodingIn"]
            ).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatEntrySetIn"])
    types["GoogleSecuritySafebrowsingV4ThreatEntrySetOut"] = t.struct(
        {
            "compressionType": t.string().optional(),
            "riceIndices": t.proxy(
                renames["GoogleSecuritySafebrowsingV4RiceDeltaEncodingOut"]
            ).optional(),
            "rawIndices": t.proxy(
                renames["GoogleSecuritySafebrowsingV4RawIndicesOut"]
            ).optional(),
            "rawHashes": t.proxy(
                renames["GoogleSecuritySafebrowsingV4RawHashesOut"]
            ).optional(),
            "riceHashes": t.proxy(
                renames["GoogleSecuritySafebrowsingV4RiceDeltaEncodingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4ThreatEntrySetOut"])
    types["GoogleSecuritySafebrowsingV4RiceDeltaEncodingIn"] = t.struct(
        {
            "riceParameter": t.integer().optional(),
            "encodedData": t.string().optional(),
            "firstValue": t.string().optional(),
            "numEntries": t.integer().optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4RiceDeltaEncodingIn"])
    types["GoogleSecuritySafebrowsingV4RiceDeltaEncodingOut"] = t.struct(
        {
            "riceParameter": t.integer().optional(),
            "encodedData": t.string().optional(),
            "firstValue": t.string().optional(),
            "numEntries": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4RiceDeltaEncodingOut"])
    types["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestIn"] = t.struct(
        {
            "client": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
            ).optional(),
            "listUpdateRequests": t.array(
                t.proxy(
                    renames[
                        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestIn"
                    ]
                )
            ).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestIn"])
    types["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestOut"] = t.struct(
        {
            "client": t.proxy(
                renames["GoogleSecuritySafebrowsingV4ClientInfoOut"]
            ).optional(),
            "listUpdateRequests": t.array(
                t.proxy(
                    renames[
                        "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestOut"
                    ]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestOut"])

    functions = {}
    functions["fullHashesFind"] = safebrowsing.post(
        "v4/fullHashes:find",
        t.struct(
            {
                "threatInfo": t.proxy(
                    renames["GoogleSecuritySafebrowsingV4ThreatInfoIn"]
                ).optional(),
                "clientStates": t.array(t.string()).optional(),
                "apiClient": t.proxy(
                    renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
                ).optional(),
                "client": t.proxy(
                    renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleSecuritySafebrowsingV4FindFullHashesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["encodedUpdatesGet"] = safebrowsing.get(
        "v4/encodedUpdates/{encodedRequest}",
        t.struct(
            {
                "encodedRequest": t.string().optional(),
                "clientVersion": t.string().optional(),
                "clientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["encodedFullHashesGet"] = safebrowsing.get(
        "v4/encodedFullHashes/{encodedRequest}",
        t.struct(
            {
                "clientVersion": t.string().optional(),
                "encodedRequest": t.string().optional(),
                "clientId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleSecuritySafebrowsingV4FindFullHashesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["threatHitsCreate"] = safebrowsing.post(
        "v4/threatHits",
        t.struct(
            {
                "platformType": t.string().optional(),
                "resources": t.array(
                    t.proxy(
                        renames["GoogleSecuritySafebrowsingV4ThreatHitThreatSourceIn"]
                    )
                ).optional(),
                "clientInfo": t.proxy(
                    renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
                ).optional(),
                "userInfo": t.proxy(
                    renames["GoogleSecuritySafebrowsingV4ThreatHitUserInfoIn"]
                ).optional(),
                "threatType": t.string().optional(),
                "entry": t.proxy(
                    renames["GoogleSecuritySafebrowsingV4ThreatEntryIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["threatListUpdatesFetch"] = safebrowsing.post(
        "v4/threatListUpdates:fetch",
        t.struct(
            {
                "client": t.proxy(
                    renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
                ).optional(),
                "listUpdateRequests": t.array(
                    t.proxy(
                        renames[
                            "GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequestListUpdateRequestIn"
                        ]
                    )
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["threatMatchesFind"] = safebrowsing.post(
        "v4/threatMatches:find",
        t.struct(
            {
                "client": t.proxy(
                    renames["GoogleSecuritySafebrowsingV4ClientInfoIn"]
                ).optional(),
                "threatInfo": t.proxy(
                    renames["GoogleSecuritySafebrowsingV4ThreatInfoIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleSecuritySafebrowsingV4FindThreatMatchesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["threatListsList"] = safebrowsing.get(
        "v4/threatLists",
        t.struct({"auth": t.string().optional()}),
        t.proxy(renames["GoogleSecuritySafebrowsingV4ListThreatListsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="safebrowsing",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
