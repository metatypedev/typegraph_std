from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_policysimulator() -> Import:
    policysimulator = HTTPRuntime("https://policysimulator.googleapis.com/")

    renames = {
        "ErrorResponse": "_policysimulator_1_ErrorResponse",
        "GoogleRpcStatusIn": "_policysimulator_2_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_policysimulator_3_GoogleRpcStatusOut",
        "GoogleLongrunningListOperationsResponseIn": "_policysimulator_4_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_policysimulator_5_GoogleLongrunningListOperationsResponseOut",
        "GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn": "_policysimulator_6_GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn",
        "GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut": "_policysimulator_7_GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut",
        "GoogleCloudPolicysimulatorV1ReplayConfigIn": "_policysimulator_8_GoogleCloudPolicysimulatorV1ReplayConfigIn",
        "GoogleCloudPolicysimulatorV1ReplayConfigOut": "_policysimulator_9_GoogleCloudPolicysimulatorV1ReplayConfigOut",
        "GoogleLongrunningOperationIn": "_policysimulator_10_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_policysimulator_11_GoogleLongrunningOperationOut",
        "GoogleTypeExprIn": "_policysimulator_12_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_policysimulator_13_GoogleTypeExprOut",
        "GoogleIamV1PolicyIn": "_policysimulator_14_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_policysimulator_15_GoogleIamV1PolicyOut",
        "GoogleCloudPolicysimulatorV1AccessTupleIn": "_policysimulator_16_GoogleCloudPolicysimulatorV1AccessTupleIn",
        "GoogleCloudPolicysimulatorV1AccessTupleOut": "_policysimulator_17_GoogleCloudPolicysimulatorV1AccessTupleOut",
        "GoogleIamV1BindingIn": "_policysimulator_18_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_policysimulator_19_GoogleIamV1BindingOut",
        "GoogleCloudPolicysimulatorV1AccessStateDiffIn": "_policysimulator_20_GoogleCloudPolicysimulatorV1AccessStateDiffIn",
        "GoogleCloudPolicysimulatorV1AccessStateDiffOut": "_policysimulator_21_GoogleCloudPolicysimulatorV1AccessStateDiffOut",
        "GoogleCloudPolicysimulatorV1ExplainedAccessIn": "_policysimulator_22_GoogleCloudPolicysimulatorV1ExplainedAccessIn",
        "GoogleCloudPolicysimulatorV1ExplainedAccessOut": "_policysimulator_23_GoogleCloudPolicysimulatorV1ExplainedAccessOut",
        "GoogleCloudPolicysimulatorV1BindingExplanationIn": "_policysimulator_24_GoogleCloudPolicysimulatorV1BindingExplanationIn",
        "GoogleCloudPolicysimulatorV1BindingExplanationOut": "_policysimulator_25_GoogleCloudPolicysimulatorV1BindingExplanationOut",
        "GoogleIamV1AuditConfigIn": "_policysimulator_26_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_policysimulator_27_GoogleIamV1AuditConfigOut",
        "GoogleCloudPolicysimulatorV1ReplayResultIn": "_policysimulator_28_GoogleCloudPolicysimulatorV1ReplayResultIn",
        "GoogleCloudPolicysimulatorV1ReplayResultOut": "_policysimulator_29_GoogleCloudPolicysimulatorV1ReplayResultOut",
        "GoogleCloudPolicysimulatorV1ReplayDiffIn": "_policysimulator_30_GoogleCloudPolicysimulatorV1ReplayDiffIn",
        "GoogleCloudPolicysimulatorV1ReplayDiffOut": "_policysimulator_31_GoogleCloudPolicysimulatorV1ReplayDiffOut",
        "GoogleCloudPolicysimulatorV1ExplainedPolicyIn": "_policysimulator_32_GoogleCloudPolicysimulatorV1ExplainedPolicyIn",
        "GoogleCloudPolicysimulatorV1ExplainedPolicyOut": "_policysimulator_33_GoogleCloudPolicysimulatorV1ExplainedPolicyOut",
        "GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn": "_policysimulator_34_GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn",
        "GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut": "_policysimulator_35_GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut",
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn": "_policysimulator_36_GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn",
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut": "_policysimulator_37_GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut",
        "GoogleTypeDateIn": "_policysimulator_38_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_policysimulator_39_GoogleTypeDateOut",
        "GoogleIamV1AuditLogConfigIn": "_policysimulator_40_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_policysimulator_41_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudPolicysimulatorV1ReplayIn": "_policysimulator_42_GoogleCloudPolicysimulatorV1ReplayIn",
        "GoogleCloudPolicysimulatorV1ReplayOut": "_policysimulator_43_GoogleCloudPolicysimulatorV1ReplayOut",
        "GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn": "_policysimulator_44_GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn",
        "GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut": "_policysimulator_45_GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn"] = t.struct(
        {"startTime": t.string().optional()}
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn"])
    types["GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudPolicysimulatorV1AccessTupleIn"] = t.struct(
        {
            "principal": t.string(),
            "fullResourceName": t.string(),
            "permission": t.string(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessTupleIn"])
    types["GoogleCloudPolicysimulatorV1AccessTupleOut"] = t.struct(
        {
            "principal": t.string(),
            "fullResourceName": t.string(),
            "permission": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessTupleOut"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types["GoogleCloudPolicysimulatorV1AccessStateDiffIn"] = t.struct(
        {
            "baseline": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessIn"]
            ).optional(),
            "accessChange": t.string().optional(),
            "simulated": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessStateDiffIn"])
    types["GoogleCloudPolicysimulatorV1AccessStateDiffOut"] = t.struct(
        {
            "baseline": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessOut"]
            ).optional(),
            "accessChange": t.string().optional(),
            "simulated": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessStateDiffOut"])
    types["GoogleCloudPolicysimulatorV1ExplainedAccessIn"] = t.struct(
        {
            "accessState": t.string().optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "policies": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedAccessIn"])
    types["GoogleCloudPolicysimulatorV1ExplainedAccessOut"] = t.struct(
        {
            "accessState": t.string().optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "policies": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedAccessOut"])
    types["GoogleCloudPolicysimulatorV1BindingExplanationIn"] = t.struct(
        {
            "access": t.string(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "role": t.string().optional(),
            "relevance": t.string().optional(),
            "rolePermission": t.string().optional(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "rolePermissionRelevance": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1BindingExplanationIn"])
    types["GoogleCloudPolicysimulatorV1BindingExplanationOut"] = t.struct(
        {
            "access": t.string(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "role": t.string().optional(),
            "relevance": t.string().optional(),
            "rolePermission": t.string().optional(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "rolePermissionRelevance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1BindingExplanationOut"])
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
    types["GoogleCloudPolicysimulatorV1ReplayResultIn"] = t.struct(
        {
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessTupleIn"]
            ).optional(),
            "lastSeenDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "name": t.string().optional(),
            "diff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayDiffIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultIn"])
    types["GoogleCloudPolicysimulatorV1ReplayResultOut"] = t.struct(
        {
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessTupleOut"]
            ).optional(),
            "lastSeenDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "name": t.string().optional(),
            "diff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayDiffOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultOut"])
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
    types["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "access": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "relevance": t.string().optional(),
            "bindingExplanations": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1BindingExplanationIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"])
    types["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "access": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "relevance": t.string().optional(),
            "bindingExplanations": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1BindingExplanationOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"])
    types["GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn"] = t.struct(
        {
            "differenceCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "oldestDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "unchangedCount": t.integer().optional(),
            "newestDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "logCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn"])
    types["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"] = t.struct(
        {
            "differenceCount": t.integer().optional(),
            "errorCount": t.integer().optional(),
            "oldestDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "unchangedCount": t.integer().optional(),
            "newestDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "logCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"])
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
    types["GoogleTypeDateIn"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
        }
    ).named(renames["GoogleTypeDateIn"])
    types["GoogleTypeDateOut"] = t.struct(
        {
            "month": t.integer().optional(),
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeDateOut"])
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
    types["GoogleCloudPolicysimulatorV1ReplayIn"] = t.struct(
        {"config": t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayConfigIn"])}
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayIn"])
    types["GoogleCloudPolicysimulatorV1ReplayOut"] = t.struct(
        {
            "resultsSummary": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"]
            ).optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "config": t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayConfigOut"]),
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

    functions = {}
    functions["projectsLocationsReplaysCreate"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsReplaysGet"] = policysimulator.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayOut"]),
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
    functions["foldersLocationsReplaysResultsList"] = policysimulator.get(
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
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsLocationsReplaysOperationsGet"] = policysimulator.get(
        "v1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
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
