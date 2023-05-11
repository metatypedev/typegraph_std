from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_policysimulator() -> Import:
    policysimulator = HTTPRuntime("https://policysimulator.googleapis.com/")

    renames = {
        "ErrorResponse": "_policysimulator_1_ErrorResponse",
        "GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn": "_policysimulator_2_GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn",
        "GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut": "_policysimulator_3_GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut",
        "GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn": "_policysimulator_4_GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn",
        "GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut": "_policysimulator_5_GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut",
        "GoogleIamV1AuditConfigIn": "_policysimulator_6_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_policysimulator_7_GoogleIamV1AuditConfigOut",
        "GoogleCloudPolicysimulatorV1AccessStateDiffIn": "_policysimulator_8_GoogleCloudPolicysimulatorV1AccessStateDiffIn",
        "GoogleCloudPolicysimulatorV1AccessStateDiffOut": "_policysimulator_9_GoogleCloudPolicysimulatorV1AccessStateDiffOut",
        "GoogleCloudPolicysimulatorV1ReplayConfigIn": "_policysimulator_10_GoogleCloudPolicysimulatorV1ReplayConfigIn",
        "GoogleCloudPolicysimulatorV1ReplayConfigOut": "_policysimulator_11_GoogleCloudPolicysimulatorV1ReplayConfigOut",
        "GoogleLongrunningOperationIn": "_policysimulator_12_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_policysimulator_13_GoogleLongrunningOperationOut",
        "GoogleCloudPolicysimulatorV1ExplainedAccessIn": "_policysimulator_14_GoogleCloudPolicysimulatorV1ExplainedAccessIn",
        "GoogleCloudPolicysimulatorV1ExplainedAccessOut": "_policysimulator_15_GoogleCloudPolicysimulatorV1ExplainedAccessOut",
        "GoogleIamV1BindingIn": "_policysimulator_16_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_policysimulator_17_GoogleIamV1BindingOut",
        "GoogleIamV1AuditLogConfigIn": "_policysimulator_18_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_policysimulator_19_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudPolicysimulatorV1AccessTupleIn": "_policysimulator_20_GoogleCloudPolicysimulatorV1AccessTupleIn",
        "GoogleCloudPolicysimulatorV1AccessTupleOut": "_policysimulator_21_GoogleCloudPolicysimulatorV1AccessTupleOut",
        "GoogleRpcStatusIn": "_policysimulator_22_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_policysimulator_23_GoogleRpcStatusOut",
        "GoogleCloudPolicysimulatorV1ReplayResultIn": "_policysimulator_24_GoogleCloudPolicysimulatorV1ReplayResultIn",
        "GoogleCloudPolicysimulatorV1ReplayResultOut": "_policysimulator_25_GoogleCloudPolicysimulatorV1ReplayResultOut",
        "GoogleLongrunningListOperationsResponseIn": "_policysimulator_26_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_policysimulator_27_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn": "_policysimulator_28_GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn",
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut": "_policysimulator_29_GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut",
        "GoogleCloudPolicysimulatorV1ReplayDiffIn": "_policysimulator_30_GoogleCloudPolicysimulatorV1ReplayDiffIn",
        "GoogleCloudPolicysimulatorV1ReplayDiffOut": "_policysimulator_31_GoogleCloudPolicysimulatorV1ReplayDiffOut",
        "GoogleIamV1PolicyIn": "_policysimulator_32_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_policysimulator_33_GoogleIamV1PolicyOut",
        "GoogleCloudPolicysimulatorV1ExplainedPolicyIn": "_policysimulator_34_GoogleCloudPolicysimulatorV1ExplainedPolicyIn",
        "GoogleCloudPolicysimulatorV1ExplainedPolicyOut": "_policysimulator_35_GoogleCloudPolicysimulatorV1ExplainedPolicyOut",
        "GoogleCloudPolicysimulatorV1ReplayIn": "_policysimulator_36_GoogleCloudPolicysimulatorV1ReplayIn",
        "GoogleCloudPolicysimulatorV1ReplayOut": "_policysimulator_37_GoogleCloudPolicysimulatorV1ReplayOut",
        "GoogleCloudPolicysimulatorV1BindingExplanationIn": "_policysimulator_38_GoogleCloudPolicysimulatorV1BindingExplanationIn",
        "GoogleCloudPolicysimulatorV1BindingExplanationOut": "_policysimulator_39_GoogleCloudPolicysimulatorV1BindingExplanationOut",
        "GoogleTypeExprIn": "_policysimulator_40_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_policysimulator_41_GoogleTypeExprOut",
        "GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn": "_policysimulator_42_GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn",
        "GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut": "_policysimulator_43_GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut",
        "GoogleTypeDateIn": "_policysimulator_44_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_policysimulator_45_GoogleTypeDateOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn"] = t.struct(
        {"startTime": t.string().optional()}
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn"])
    types["GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut"])
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
    types["GoogleIamV1AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigIn"])
            ).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigIn"])
    types["GoogleIamV1AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1AuditConfigOut"])
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
    types["GoogleCloudPolicysimulatorV1ReplayConfigIn"] = t.struct(
        {
            "policyOverlay": t.struct({"_": t.string().optional()}).optional(),
            "logSource": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayConfigIn"])
    types["GoogleCloudPolicysimulatorV1ReplayConfigOut"] = t.struct(
        {
            "policyOverlay": t.struct({"_": t.string().optional()}).optional(),
            "logSource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayConfigOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudPolicysimulatorV1ExplainedAccessIn"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "policies": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"])
            ).optional(),
            "accessState": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedAccessIn"])
    types["GoogleCloudPolicysimulatorV1ExplainedAccessOut"] = t.struct(
        {
            "errors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "policies": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"])
            ).optional(),
            "accessState": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedAccessOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
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
    types["GoogleCloudPolicysimulatorV1ReplayResultIn"] = t.struct(
        {
            "diff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayDiffIn"]
            ).optional(),
            "lastSeenDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessTupleIn"]
            ).optional(),
            "parent": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultIn"])
    types["GoogleCloudPolicysimulatorV1ReplayResultOut"] = t.struct(
        {
            "diff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayDiffOut"]
            ).optional(),
            "lastSeenDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessTupleOut"]
            ).optional(),
            "parent": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultOut"])
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
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"] = t.struct(
        {
            "bindingExplanations": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1BindingExplanationIn"])
            ).optional(),
            "access": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "relevance": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"])
    types["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"] = t.struct(
        {
            "bindingExplanations": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1BindingExplanationOut"])
            ).optional(),
            "access": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "relevance": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"])
    types["GoogleCloudPolicysimulatorV1ReplayIn"] = t.struct(
        {"config": t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayConfigIn"])}
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayIn"])
    types["GoogleCloudPolicysimulatorV1ReplayOut"] = t.struct(
        {
            "resultsSummary": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"]
            ).optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "config": t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayConfigOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOut"])
    types["GoogleCloudPolicysimulatorV1BindingExplanationIn"] = t.struct(
        {
            "rolePermissionRelevance": t.string().optional(),
            "access": t.string(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "relevance": t.string().optional(),
            "rolePermission": t.string().optional(),
            "role": t.string().optional(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1BindingExplanationIn"])
    types["GoogleCloudPolicysimulatorV1BindingExplanationOut"] = t.struct(
        {
            "rolePermissionRelevance": t.string().optional(),
            "access": t.string(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "relevance": t.string().optional(),
            "rolePermission": t.string().optional(),
            "role": t.string().optional(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1BindingExplanationOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn"] = t.struct(
        {
            "unchangedCount": t.integer().optional(),
            "oldestDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "logCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "differenceCount": t.integer().optional(),
            "newestDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn"])
    types["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"] = t.struct(
        {
            "unchangedCount": t.integer().optional(),
            "oldestDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "logCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "differenceCount": t.integer().optional(),
            "newestDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"])
    types["GoogleTypeDateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])

    functions = {}
    functions["operationsList"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = policysimulator.get(
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReplaysOperationsList"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReplaysOperationsGet"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsReplaysGet"] = policysimulator.post(
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
    functions["foldersLocationsReplaysCreate"] = policysimulator.post(
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
    functions["foldersLocationsReplaysOperationsList"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsReplaysOperationsGet"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersLocationsReplaysResultsList"] = policysimulator.get(
        "v1/{parent}/results",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsReplaysGet"] = policysimulator.post(
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
    functions["organizationsLocationsReplaysCreate"] = policysimulator.post(
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
    functions["organizationsLocationsReplaysOperationsGet"] = policysimulator.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsReplaysOperationsList"] = policysimulator.get(
        "v1/{name}",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsReplaysResultsList"] = policysimulator.get(
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

    return Import(
        importer="policysimulator", renames=renames, types=types, functions=functions
    )
