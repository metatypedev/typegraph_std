from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_webrisk() -> Import:
    webrisk = HTTPRuntime("https://webrisk.googleapis.com/")

    renames = {
        "ErrorResponse": "_webrisk_1_ErrorResponse",
        "GoogleCloudWebriskV1ComputeThreatListDiffResponseIn": "_webrisk_2_GoogleCloudWebriskV1ComputeThreatListDiffResponseIn",
        "GoogleCloudWebriskV1ComputeThreatListDiffResponseOut": "_webrisk_3_GoogleCloudWebriskV1ComputeThreatListDiffResponseOut",
        "GoogleCloudWebriskV1SubmissionIn": "_webrisk_4_GoogleCloudWebriskV1SubmissionIn",
        "GoogleCloudWebriskV1SubmissionOut": "_webrisk_5_GoogleCloudWebriskV1SubmissionOut",
        "GoogleRpcStatusIn": "_webrisk_6_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_webrisk_7_GoogleRpcStatusOut",
        "GoogleLongrunningOperationIn": "_webrisk_8_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_webrisk_9_GoogleLongrunningOperationOut",
        "GoogleCloudWebriskV1SearchUrisResponseIn": "_webrisk_10_GoogleCloudWebriskV1SearchUrisResponseIn",
        "GoogleCloudWebriskV1SearchUrisResponseOut": "_webrisk_11_GoogleCloudWebriskV1SearchUrisResponseOut",
        "GoogleCloudWebriskV1SearchHashesResponseThreatHashIn": "_webrisk_12_GoogleCloudWebriskV1SearchHashesResponseThreatHashIn",
        "GoogleCloudWebriskV1SearchHashesResponseThreatHashOut": "_webrisk_13_GoogleCloudWebriskV1SearchHashesResponseThreatHashOut",
        "GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn": "_webrisk_14_GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn",
        "GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut": "_webrisk_15_GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut",
        "GoogleCloudWebriskV1ThreatEntryRemovalsIn": "_webrisk_16_GoogleCloudWebriskV1ThreatEntryRemovalsIn",
        "GoogleCloudWebriskV1ThreatEntryRemovalsOut": "_webrisk_17_GoogleCloudWebriskV1ThreatEntryRemovalsOut",
        "GoogleCloudWebriskV1ThreatEntryAdditionsIn": "_webrisk_18_GoogleCloudWebriskV1ThreatEntryAdditionsIn",
        "GoogleCloudWebriskV1ThreatEntryAdditionsOut": "_webrisk_19_GoogleCloudWebriskV1ThreatEntryAdditionsOut",
        "GoogleCloudWebriskV1RawHashesIn": "_webrisk_20_GoogleCloudWebriskV1RawHashesIn",
        "GoogleCloudWebriskV1RawHashesOut": "_webrisk_21_GoogleCloudWebriskV1RawHashesOut",
        "GoogleCloudWebriskV1RawIndicesIn": "_webrisk_22_GoogleCloudWebriskV1RawIndicesIn",
        "GoogleCloudWebriskV1RawIndicesOut": "_webrisk_23_GoogleCloudWebriskV1RawIndicesOut",
        "GoogleCloudWebriskV1SearchHashesResponseIn": "_webrisk_24_GoogleCloudWebriskV1SearchHashesResponseIn",
        "GoogleCloudWebriskV1SearchHashesResponseOut": "_webrisk_25_GoogleCloudWebriskV1SearchHashesResponseOut",
        "GoogleProtobufEmptyIn": "_webrisk_26_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_webrisk_27_GoogleProtobufEmptyOut",
        "GoogleCloudWebriskV1RiceDeltaEncodingIn": "_webrisk_28_GoogleCloudWebriskV1RiceDeltaEncodingIn",
        "GoogleCloudWebriskV1RiceDeltaEncodingOut": "_webrisk_29_GoogleCloudWebriskV1RiceDeltaEncodingOut",
        "GoogleLongrunningCancelOperationRequestIn": "_webrisk_30_GoogleLongrunningCancelOperationRequestIn",
        "GoogleLongrunningCancelOperationRequestOut": "_webrisk_31_GoogleLongrunningCancelOperationRequestOut",
        "GoogleCloudWebriskV1SearchUrisResponseThreatUriIn": "_webrisk_32_GoogleCloudWebriskV1SearchUrisResponseThreatUriIn",
        "GoogleCloudWebriskV1SearchUrisResponseThreatUriOut": "_webrisk_33_GoogleCloudWebriskV1SearchUrisResponseThreatUriOut",
        "GoogleLongrunningListOperationsResponseIn": "_webrisk_34_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_webrisk_35_GoogleLongrunningListOperationsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudWebriskV1ComputeThreatListDiffResponseIn"] = t.struct(
        {
            "checksum": t.proxy(
                renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn"]
            ).optional(),
            "removals": t.proxy(
                renames["GoogleCloudWebriskV1ThreatEntryRemovalsIn"]
            ).optional(),
            "recommendedNextDiff": t.string().optional(),
            "responseType": t.string().optional(),
            "additions": t.proxy(
                renames["GoogleCloudWebriskV1ThreatEntryAdditionsIn"]
            ).optional(),
            "newVersionToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseIn"])
    types["GoogleCloudWebriskV1ComputeThreatListDiffResponseOut"] = t.struct(
        {
            "checksum": t.proxy(
                renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut"]
            ).optional(),
            "removals": t.proxy(
                renames["GoogleCloudWebriskV1ThreatEntryRemovalsOut"]
            ).optional(),
            "recommendedNextDiff": t.string().optional(),
            "responseType": t.string().optional(),
            "additions": t.proxy(
                renames["GoogleCloudWebriskV1ThreatEntryAdditionsOut"]
            ).optional(),
            "newVersionToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseOut"])
    types["GoogleCloudWebriskV1SubmissionIn"] = t.struct({"uri": t.string()}).named(
        renames["GoogleCloudWebriskV1SubmissionIn"]
    )
    types["GoogleCloudWebriskV1SubmissionOut"] = t.struct(
        {"uri": t.string(), "error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudWebriskV1SubmissionOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["GoogleCloudWebriskV1SearchHashesResponseThreatHashIn"] = t.struct(
        {
            "threatTypes": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "hash": t.string().optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchHashesResponseThreatHashIn"])
    types["GoogleCloudWebriskV1SearchHashesResponseThreatHashOut"] = t.struct(
        {
            "threatTypes": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "hash": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchHashesResponseThreatHashOut"])
    types["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn"] = t.struct(
        {"sha256": t.string().optional()}
    ).named(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumIn"])
    types["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut"] = t.struct(
        {
            "sha256": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksumOut"])
    types["GoogleCloudWebriskV1ThreatEntryRemovalsIn"] = t.struct(
        {
            "rawIndices": t.proxy(
                renames["GoogleCloudWebriskV1RawIndicesIn"]
            ).optional(),
            "riceIndices": t.proxy(
                renames["GoogleCloudWebriskV1RiceDeltaEncodingIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ThreatEntryRemovalsIn"])
    types["GoogleCloudWebriskV1ThreatEntryRemovalsOut"] = t.struct(
        {
            "rawIndices": t.proxy(
                renames["GoogleCloudWebriskV1RawIndicesOut"]
            ).optional(),
            "riceIndices": t.proxy(
                renames["GoogleCloudWebriskV1RiceDeltaEncodingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ThreatEntryRemovalsOut"])
    types["GoogleCloudWebriskV1ThreatEntryAdditionsIn"] = t.struct(
        {
            "rawHashes": t.array(
                t.proxy(renames["GoogleCloudWebriskV1RawHashesIn"])
            ).optional(),
            "riceHashes": t.proxy(
                renames["GoogleCloudWebriskV1RiceDeltaEncodingIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ThreatEntryAdditionsIn"])
    types["GoogleCloudWebriskV1ThreatEntryAdditionsOut"] = t.struct(
        {
            "rawHashes": t.array(
                t.proxy(renames["GoogleCloudWebriskV1RawHashesOut"])
            ).optional(),
            "riceHashes": t.proxy(
                renames["GoogleCloudWebriskV1RiceDeltaEncodingOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1ThreatEntryAdditionsOut"])
    types["GoogleCloudWebriskV1RawHashesIn"] = t.struct(
        {"prefixSize": t.integer().optional(), "rawHashes": t.string().optional()}
    ).named(renames["GoogleCloudWebriskV1RawHashesIn"])
    types["GoogleCloudWebriskV1RawHashesOut"] = t.struct(
        {
            "prefixSize": t.integer().optional(),
            "rawHashes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1RawHashesOut"])
    types["GoogleCloudWebriskV1RawIndicesIn"] = t.struct(
        {"indices": t.array(t.integer()).optional()}
    ).named(renames["GoogleCloudWebriskV1RawIndicesIn"])
    types["GoogleCloudWebriskV1RawIndicesOut"] = t.struct(
        {
            "indices": t.array(t.integer()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1RawIndicesOut"])
    types["GoogleCloudWebriskV1SearchHashesResponseIn"] = t.struct(
        {
            "threats": t.array(
                t.proxy(renames["GoogleCloudWebriskV1SearchHashesResponseThreatHashIn"])
            ).optional(),
            "negativeExpireTime": t.string().optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchHashesResponseIn"])
    types["GoogleCloudWebriskV1SearchHashesResponseOut"] = t.struct(
        {
            "threats": t.array(
                t.proxy(
                    renames["GoogleCloudWebriskV1SearchHashesResponseThreatHashOut"]
                )
            ).optional(),
            "negativeExpireTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchHashesResponseOut"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudWebriskV1RiceDeltaEncodingIn"] = t.struct(
        {
            "entryCount": t.integer().optional(),
            "encodedData": t.string().optional(),
            "riceParameter": t.integer().optional(),
            "firstValue": t.string().optional(),
        }
    ).named(renames["GoogleCloudWebriskV1RiceDeltaEncodingIn"])
    types["GoogleCloudWebriskV1RiceDeltaEncodingOut"] = t.struct(
        {
            "entryCount": t.integer().optional(),
            "encodedData": t.string().optional(),
            "riceParameter": t.integer().optional(),
            "firstValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1RiceDeltaEncodingOut"])
    types["GoogleLongrunningCancelOperationRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestIn"])
    types["GoogleLongrunningCancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleLongrunningCancelOperationRequestOut"])
    types["GoogleCloudWebriskV1SearchUrisResponseThreatUriIn"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "threatTypes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchUrisResponseThreatUriIn"])
    types["GoogleCloudWebriskV1SearchUrisResponseThreatUriOut"] = t.struct(
        {
            "expireTime": t.string().optional(),
            "threatTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudWebriskV1SearchUrisResponseThreatUriOut"])
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

    functions = {}
    functions["urisSearch"] = webrisk.get(
        "v1/uris:search",
        t.struct(
            {
                "threatTypes": t.string(),
                "uri": t.string(),
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
                "hashPrefix": t.string().optional(),
                "threatTypes": t.string(),
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
                "constraints.maxDiffEntries": t.integer().optional(),
                "versionToken": t.string().optional(),
                "threatType": t.string(),
                "constraints.supportedCompressions": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudWebriskV1ComputeThreatListDiffResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="webrisk", renames=renames, types=Box(types), functions=Box(functions)
    )
