from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_webrisk() -> Import:
    webrisk = HTTPRuntime("https://webrisk.googleapis.com/")

    renames = {
        "ErrorResponse": "_webrisk_1_ErrorResponse",
        "GoogleCloudWebriskV1SearchHashesResponseIn": "_webrisk_2_GoogleCloudWebriskV1SearchHashesResponseIn",
        "GoogleCloudWebriskV1SearchHashesResponseOut": "_webrisk_3_GoogleCloudWebriskV1SearchHashesResponseOut",
        "GoogleCloudWebriskV1RiceDeltaEncodingIn": "_webrisk_4_GoogleCloudWebriskV1RiceDeltaEncodingIn",
        "GoogleCloudWebriskV1RiceDeltaEncodingOut": "_webrisk_5_GoogleCloudWebriskV1RiceDeltaEncodingOut",
        "GoogleCloudWebriskV1SearchHashesResponseThreatHashIn": "_webrisk_6_GoogleCloudWebriskV1SearchHashesResponseThreatHashIn",
        "GoogleCloudWebriskV1SearchHashesResponseThreatHashOut": "_webrisk_7_GoogleCloudWebriskV1SearchHashesResponseThreatHashOut",
        "GoogleCloudWebriskV1ThreatEntryRemovalsIn": "_webrisk_8_GoogleCloudWebriskV1ThreatEntryRemovalsIn",
        "GoogleCloudWebriskV1ThreatEntryRemovalsOut": "_webrisk_9_GoogleCloudWebriskV1ThreatEntryRemovalsOut",
        "GoogleLongrunningCancelOperationRequestIn": "_webrisk_10_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_webrisk_11_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudWebriskV1SubmissionIn": "_webrisk_12_GoogleCloudWebriskV1SubmissionIn",
        "GoogleCloudWebriskV1SubmissionOut": "_webrisk_13_GoogleCloudWebriskV1SubmissionOut",
        "GoogleLongrunningListOperationsResponseIn": "_webrisk_14_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_webrisk_15_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudWebriskV1RawIndicesIn": "_webrisk_16_GoogleCloudWebriskV1RawIndicesIn",
        "GoogleCloudWebriskV1RawIndicesOut": "_webrisk_17_GoogleCloudWebriskV1RawIndicesOut",
        "GoogleCloudWebriskV1RawHashesIn": "_webrisk_18_GoogleCloudWebriskV1RawHashesIn",
        "GoogleCloudWebriskV1RawHashesOut": "_webrisk_19_GoogleCloudWebriskV1RawHashesOut",
        "GoogleCloudWebriskV1SearchUrisResponseThreatUriIn": "_webrisk_20_GoogleCloudWebriskV1SearchUrisResponseThreatUriIn",
        "GoogleCloudWebriskV1SearchUrisResponseThreatUriOut": "_webrisk_21_GoogleCloudWebriskV1SearchUrisResponseThreatUriOut",
        "GoogleCloudWebriskV1ComputeThreatListDiffResponseIn": "_webrisk_22_GoogleCloudWebriskV1ComputeThreatListDiffResponseIn",
        "GoogleCloudWebriskV1ComputeThreatListDiffResponseOut": "_webrisk_23_GoogleCloudWebriskV1ComputeThreatListDiffResponseOut",
        "GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn": "_webrisk_24_GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn",
        "GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut": "_webrisk_25_GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut",
        "GoogleCloudWebriskV1SearchUrisResponseIn": "_webrisk_26_GoogleCloudWebriskV1SearchUrisResponseIn",
        "GoogleCloudWebriskV1SearchUrisResponseOut": "_webrisk_27_GoogleCloudWebriskV1SearchUrisResponseOut",
        "GoogleLongrunningOperationIn": "_webrisk_28_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_webrisk_29_GoogleLongrunningOperationOut",
        "GoogleProtobufEmptyIn": "_webrisk_30_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_webrisk_31_GoogleProtobufEmptyOut",
        "GoogleCloudWebriskV1ThreatEntryAdditionsIn": "_webrisk_32_GoogleCloudWebriskV1ThreatEntryAdditionsIn",
        "GoogleCloudWebriskV1ThreatEntryAdditionsOut": "_webrisk_33_GoogleCloudWebriskV1ThreatEntryAdditionsOut",
        "GoogleRpcStatusIn": "_webrisk_34_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_webrisk_35_GoogleRpcStatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudWebriskV1SearchHashesResponseIn"] = t.struct(
        {
            "negativeExpireTime": t.string().optional(),
            "threats": t.array(
                t.proxy(renames["GoogleCloudWebriskV1SearchHashesResponseThreatHashIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchHashesResponseIn"])
    types["GoogleCloudWebriskV1SearchHashesResponseOut"] = t.struct(
        {
            "negativeExpireTime": t.string().optional(),
            "threats": t.array(
                t.proxy(
                    renames["GoogleCloudWebriskV1SearchHashesResponseThreatHashOut"]
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchHashesResponseOut"])
    types["GoogleCloudWebriskV1RiceDeltaEncodingIn"] = t.struct(
        {
            "encodedData": t.string().optional(),
            "entryCount": t.integer().optional(),
            "riceParameter": t.integer().optional(),
            "firstValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudWebriskV1RiceDeltaEncodingIn"])
    types["GoogleCloudWebriskV1RiceDeltaEncodingOut"] = t.struct(
        {
            "encodedData": t.string().optional(),
            "entryCount": t.integer().optional(),
            "riceParameter": t.integer().optional(),
            "firstValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1RiceDeltaEncodingOut"])
    types["GoogleCloudWebriskV1SearchHashesResponseThreatHashIn"] = t.struct(
        {
            "hash": t.string().optional(),
            "threatTypes": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchHashesResponseThreatHashIn"])
    types["GoogleCloudWebriskV1SearchHashesResponseThreatHashOut"] = t.struct(
        {
            "hash": t.string().optional(),
            "threatTypes": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchHashesResponseThreatHashOut"])
    types["GoogleCloudWebriskV1ThreatEntryRemovalsIn"] = t.struct(
        {
            "riceIndices": t.proxy(
                renames["GoogleCloudWebriskV1RiceDeltaEncodingIn"]
            ).optional(),
            "rawIndices": t.proxy(
                renames["GoogleCloudWebriskV1RawIndicesIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ThreatEntryRemovalsIn"])
    types["GoogleCloudWebriskV1ThreatEntryRemovalsOut"] = t.struct(
        {
            "riceIndices": t.proxy(
                renames["GoogleCloudWebriskV1RiceDeltaEncodingOut"]
            ).optional(),
            "rawIndices": t.proxy(
                renames["GoogleCloudWebriskV1RawIndicesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ThreatEntryRemovalsOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleCloudWebriskV1SubmissionIn"] = t.struct({"uri": t.string()}).named(
        renames["GoogleCloudWebriskV1SubmissionIn"]
    )
    types["GoogleCloudWebriskV1SubmissionOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudWebriskV1SubmissionOut"])
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
    types["GoogleCloudWebriskV1RawIndicesIn"] = t.struct(
        {"indices": t.array(t.integer()).optional()}
    ).named(renames["GoogleCloudWebriskV1RawIndicesIn"])
    types["GoogleCloudWebriskV1RawIndicesOut"] = t.struct(
        {
            "indices": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1RawIndicesOut"])
    types["GoogleCloudWebriskV1RawHashesIn"] = t.struct(
        {"rawHashes": t.string().optional(), "prefixSize": t.integer().optional()}
    ).named(renames["GoogleCloudWebriskV1RawHashesIn"])
    types["GoogleCloudWebriskV1RawHashesOut"] = t.struct(
        {
            "rawHashes": t.string().optional(),
            "prefixSize": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1RawHashesOut"])
    types["GoogleCloudWebriskV1SearchUrisResponseThreatUriIn"] = t.struct(
        {
            "threatTypes": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchUrisResponseThreatUriIn"])
    types["GoogleCloudWebriskV1SearchUrisResponseThreatUriOut"] = t.struct(
        {
            "threatTypes": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchUrisResponseThreatUriOut"])
    types["GoogleCloudWebriskV1ComputeThreatListDiffResponseIn"] = t.struct(
        {
            "responseType": t.string().optional(),
            "newVersionToken": t.string().optional(),
            "checksum": t.proxy(
                renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn"]
            ).optional(),
            "removals": t.proxy(
                renames["GoogleCloudWebriskV1ThreatEntryRemovalsIn"]
            ).optional(),
            "recommendedNextDiff": t.string().optional(),
            "additions": t.proxy(
                renames["GoogleCloudWebriskV1ThreatEntryAdditionsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseIn"])
    types["GoogleCloudWebriskV1ComputeThreatListDiffResponseOut"] = t.struct(
        {
            "responseType": t.string().optional(),
            "newVersionToken": t.string().optional(),
            "checksum": t.proxy(
                renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut"]
            ).optional(),
            "removals": t.proxy(
                renames["GoogleCloudWebriskV1ThreatEntryRemovalsOut"]
            ).optional(),
            "recommendedNextDiff": t.string().optional(),
            "additions": t.proxy(
                renames["GoogleCloudWebriskV1ThreatEntryAdditionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseOut"])
    types["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn"] = t.struct(
        {"sha256": t.string().optional()}
    ).named(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn"])
    types["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut"] = t.struct(
        {
            "sha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut"])
    types["GoogleCloudWebriskV1SearchUrisResponseIn"] = t.struct(
        {
            "threat": t.proxy(
                renames["GoogleCloudWebriskV1SearchUrisResponseThreatUriIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudWebriskV1SearchUrisResponseIn"])
    types["GoogleCloudWebriskV1SearchUrisResponseOut"] = t.struct(
        {
            "threat": t.proxy(
                renames["GoogleCloudWebriskV1SearchUrisResponseThreatUriOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchUrisResponseOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudWebriskV1ThreatEntryAdditionsIn"] = t.struct(
        {
            "riceHashes": t.proxy(
                renames["GoogleCloudWebriskV1RiceDeltaEncodingIn"]
            ).optional(),
            "rawHashes": t.array(
                t.proxy(renames["GoogleCloudWebriskV1RawHashesIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ThreatEntryAdditionsIn"])
    types["GoogleCloudWebriskV1ThreatEntryAdditionsOut"] = t.struct(
        {
            "riceHashes": t.proxy(
                renames["GoogleCloudWebriskV1RiceDeltaEncodingOut"]
            ).optional(),
            "rawHashes": t.array(
                t.proxy(renames["GoogleCloudWebriskV1RawHashesOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ThreatEntryAdditionsOut"])
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

    functions = {}
    functions["urisSearch"] = webrisk.get(
        "v1/uris:search",
        t.struct(
            {
                "uri": t.string(),
                "threatTypes": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudWebriskV1SearchUrisResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["hashesSearch"] = webrisk.get(
        "v1/hashes:search",
        t.struct(
            {
                "threatTypes": t.string(),
                "hashPrefix": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudWebriskV1SearchHashesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSubmissionsCreate"] = webrisk.post(
        "v1/{parent}/submissions",
        t.struct(
            {"parent": t.string(), "uri": t.string(), "auth": t.string().optional()}
        ),
        t.proxy(renames["GoogleCloudWebriskV1SubmissionOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsDelete"] = webrisk.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsGet"] = webrisk.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsList"] = webrisk.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsOperationsCancel"] = webrisk.post(
        "v1/{name}:cancel",
        t.struct(
            {
                "name": t.string().optional(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["threatListsComputeDiff"] = webrisk.get(
        "v1/threatLists:computeDiff",
        t.struct(
            {
                "constraints.maxDatabaseEntries": t.integer().optional(),
                "constraints.supportedCompressions": t.string().optional(),
                "versionToken": t.string().optional(),
                "constraints.maxDiffEntries": t.integer().optional(),
                "threatType": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="webrisk", renames=renames, types=types, functions=functions)
