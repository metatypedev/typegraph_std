from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_policysimulator():
    policysimulator = HTTPRuntime("https://policysimulator.googleapis.com/")

    renames = {
        "ErrorResponse": "_policysimulator_1_ErrorResponse",
        "GoogleIamV1BindingIn": "_policysimulator_2_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_policysimulator_3_GoogleIamV1BindingOut",
        "GoogleCloudPolicysimulatorV1ReplayResultIn": "_policysimulator_4_GoogleCloudPolicysimulatorV1ReplayResultIn",
        "GoogleCloudPolicysimulatorV1ReplayResultOut": "_policysimulator_5_GoogleCloudPolicysimulatorV1ReplayResultOut",
        "GoogleCloudPolicysimulatorV1BindingExplanationIn": "_policysimulator_6_GoogleCloudPolicysimulatorV1BindingExplanationIn",
        "GoogleCloudPolicysimulatorV1BindingExplanationOut": "_policysimulator_7_GoogleCloudPolicysimulatorV1BindingExplanationOut",
        "GoogleCloudPolicysimulatorV1ReplayIn": "_policysimulator_8_GoogleCloudPolicysimulatorV1ReplayIn",
        "GoogleCloudPolicysimulatorV1ReplayOut": "_policysimulator_9_GoogleCloudPolicysimulatorV1ReplayOut",
        "GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn": "_policysimulator_10_GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn",
        "GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut": "_policysimulator_11_GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut",
        "GoogleIamV1PolicyIn": "_policysimulator_12_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_policysimulator_13_GoogleIamV1PolicyOut",
        "GoogleCloudPolicysimulatorV1AccessTupleIn": "_policysimulator_14_GoogleCloudPolicysimulatorV1AccessTupleIn",
        "GoogleCloudPolicysimulatorV1AccessTupleOut": "_policysimulator_15_GoogleCloudPolicysimulatorV1AccessTupleOut",
        "GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn": "_policysimulator_16_GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn",
        "GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut": "_policysimulator_17_GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut",
        "GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn": "_policysimulator_18_GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn",
        "GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut": "_policysimulator_19_GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut",
        "GoogleCloudPolicysimulatorV1ExplainedPolicyIn": "_policysimulator_20_GoogleCloudPolicysimulatorV1ExplainedPolicyIn",
        "GoogleCloudPolicysimulatorV1ExplainedPolicyOut": "_policysimulator_21_GoogleCloudPolicysimulatorV1ExplainedPolicyOut",
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn": "_policysimulator_22_GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn",
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut": "_policysimulator_23_GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut",
        "GoogleCloudPolicysimulatorV1AccessStateDiffIn": "_policysimulator_24_GoogleCloudPolicysimulatorV1AccessStateDiffIn",
        "GoogleCloudPolicysimulatorV1AccessStateDiffOut": "_policysimulator_25_GoogleCloudPolicysimulatorV1AccessStateDiffOut",
        "GoogleLongrunningListOperationsResponseIn": "_policysimulator_26_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_policysimulator_27_GoogleLongrunningListOperationsResponseOut",
        "GoogleIamV1AuditConfigIn": "_policysimulator_28_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_policysimulator_29_GoogleIamV1AuditConfigOut",
        "GoogleIamV1AuditLogConfigIn": "_policysimulator_30_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_policysimulator_31_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudPolicysimulatorV1ReplayDiffIn": "_policysimulator_32_GoogleCloudPolicysimulatorV1ReplayDiffIn",
        "GoogleCloudPolicysimulatorV1ReplayDiffOut": "_policysimulator_33_GoogleCloudPolicysimulatorV1ReplayDiffOut",
        "GoogleTypeDateIn": "_policysimulator_34_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_policysimulator_35_GoogleTypeDateOut",
        "GoogleCloudPolicysimulatorV1ExplainedAccessIn": "_policysimulator_36_GoogleCloudPolicysimulatorV1ExplainedAccessIn",
        "GoogleCloudPolicysimulatorV1ExplainedAccessOut": "_policysimulator_37_GoogleCloudPolicysimulatorV1ExplainedAccessOut",
        "GoogleLongrunningOperationIn": "_policysimulator_38_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_policysimulator_39_GoogleLongrunningOperationOut",
        "GoogleRpcStatusIn": "_policysimulator_40_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_policysimulator_41_GoogleRpcStatusOut",
        "GoogleTypeExprIn": "_policysimulator_42_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_policysimulator_43_GoogleTypeExprOut",
        "GoogleCloudPolicysimulatorV1ReplayConfigIn": "_policysimulator_44_GoogleCloudPolicysimulatorV1ReplayConfigIn",
        "GoogleCloudPolicysimulatorV1ReplayConfigOut": "_policysimulator_45_GoogleCloudPolicysimulatorV1ReplayConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleCloudPolicysimulatorV1ReplayResultIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessTupleIn"]
            ).optional(),
            "parent": t.string().optional(),
            "diff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayDiffIn"]
            ).optional(),
            "name": t.string().optional(),
            "lastSeenDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultIn"])
    types["GoogleCloudPolicysimulatorV1ReplayResultOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessTupleOut"]
            ).optional(),
            "parent": t.string().optional(),
            "diff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayDiffOut"]
            ).optional(),
            "name": t.string().optional(),
            "lastSeenDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultOut"])
    types["GoogleCloudPolicysimulatorV1BindingExplanationIn"] = t.struct(
        {
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "rolePermission": t.string().optional(),
            "access": t.string(),
            "rolePermissionRelevance": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "relevance": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1BindingExplanationIn"])
    types["GoogleCloudPolicysimulatorV1BindingExplanationOut"] = t.struct(
        {
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "rolePermission": t.string().optional(),
            "access": t.string(),
            "rolePermissionRelevance": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "relevance": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1BindingExplanationOut"])
    types["GoogleCloudPolicysimulatorV1ReplayIn"] = t.struct(
        {"config": t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayConfigIn"])}
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayIn"])
    types["GoogleCloudPolicysimulatorV1ReplayOut"] = t.struct(
        {
            "state": t.string().optional(),
            "config": t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayConfigOut"]),
            "resultsSummary": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"]
            ).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOut"])
    types["GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn"] = t.struct(
        {
            "replayResults": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayResultIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn"])
    types["GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut"] = t.struct(
        {
            "replayResults": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayResultOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudPolicysimulatorV1AccessTupleIn"] = t.struct(
        {
            "fullResourceName": t.string(),
            "permission": t.string(),
            "principal": t.string(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessTupleIn"])
    types["GoogleCloudPolicysimulatorV1AccessTupleOut"] = t.struct(
        {
            "fullResourceName": t.string(),
            "permission": t.string(),
            "principal": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessTupleOut"])
    types["GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn"] = t.struct(
        {"startTime": t.string().optional()}
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn"])
    types["GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut"])
    types["GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn"] = t.struct(
        {
            "differenceCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "unchangedCount": t.integer().optional(),
            "logCount": t.integer().optional(),
            "newestDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "oldestDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn"])
    types["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"] = t.struct(
        {
            "differenceCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "unchangedCount": t.integer().optional(),
            "logCount": t.integer().optional(),
            "newestDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "oldestDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"])
    types["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"] = t.struct(
        {
            "relevance": t.string().optional(),
            "bindingExplanations": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1BindingExplanationIn"])
            ).optional(),
            "access": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"])
    types["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"] = t.struct(
        {
            "relevance": t.string().optional(),
            "bindingExplanations": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1BindingExplanationOut"])
            ).optional(),
            "access": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"])
    types[
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn"
    ] = t.struct(
        {"relevance": t.string().optional(), "membership": t.string().optional()}
    ).named(
        renames["GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn"]
    )
    types[
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut"
    ] = t.struct(
        {
            "relevance": t.string().optional(),
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut"]
    )
    types["GoogleCloudPolicysimulatorV1AccessStateDiffIn"] = t.struct(
        {
            "accessChange": t.string().optional(),
            "baseline": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessIn"]
            ).optional(),
            "simulated": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessStateDiffIn"])
    types["GoogleCloudPolicysimulatorV1AccessStateDiffOut"] = t.struct(
        {
            "accessChange": t.string().optional(),
            "baseline": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessOut"]
            ).optional(),
            "simulated": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessStateDiffOut"])
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
    types["GoogleIamV1AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigIn"])
    types["GoogleIamV1AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditLogConfigOut"])
    types["GoogleCloudPolicysimulatorV1ReplayDiffIn"] = t.struct(
        {
            "accessDiff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessStateDiffIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayDiffIn"])
    types["GoogleCloudPolicysimulatorV1ReplayDiffOut"] = t.struct(
        {
            "accessDiff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessStateDiffOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayDiffOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "day": t.integer().optional(),
            "year": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
    types["GoogleCloudPolicysimulatorV1ExplainedAccessIn"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"])
            ).optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "accessState": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedAccessIn"])
    types["GoogleCloudPolicysimulatorV1ExplainedAccessOut"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"])
            ).optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "accessState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedAccessOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["GoogleTypeExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudPolicysimulatorV1ReplayConfigIn"] = t.struct(
        {
            "logSource": t.string().optional(),
            "policyOverlay": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayConfigIn"])
    types["GoogleCloudPolicysimulatorV1ReplayConfigOut"] = t.struct(
        {
            "logSource": t.string().optional(),
            "policyOverlay": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayConfigOut"])

    functions = {}
    functions["operationsGet"] = policysimulator.get(
        "v1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = policysimulator.get(
        "v1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsReplaysCreate"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsReplaysGet"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsReplaysOperationsGet"] = policysimulator.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsReplaysOperationsList"] = policysimulator.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsReplaysResultsList"] = policysimulator.get(
        "v1/{parent}/results",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsReplaysCreate"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsReplaysGet"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsReplaysResultsList"] = policysimulator.get(
        "v1/{parent}/results",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsReplaysOperationsList"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsReplaysOperationsGet"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReplaysGet"] = policysimulator.post(
        "v1/{parent}/replays",
        t.struct(
            {
                "parent": t.string(),
                "config": t.proxy(
                    renames["GoogleCloudPolicysimulatorV1ReplayConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReplaysCreate"] = policysimulator.post(
        "v1/{parent}/replays",
        t.struct(
            {
                "parent": t.string(),
                "config": t.proxy(
                    renames["GoogleCloudPolicysimulatorV1ReplayConfigIn"]
                ),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReplaysResultsList"] = policysimulator.get(
        "v1/{parent}/results",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReplaysOperationsGet"] = policysimulator.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReplaysOperationsList"] = policysimulator.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="policysimulator",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
