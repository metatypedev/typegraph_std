from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_policysimulator() -> Import:
    policysimulator = HTTPRuntime("https://policysimulator.googleapis.com/")

    renames = {
        "ErrorResponse": "_policysimulator_1_ErrorResponse",
        "GoogleCloudPolicysimulatorV1ReplayConfigIn": "_policysimulator_2_GoogleCloudPolicysimulatorV1ReplayConfigIn",
        "GoogleCloudPolicysimulatorV1ReplayConfigOut": "_policysimulator_3_GoogleCloudPolicysimulatorV1ReplayConfigOut",
        "GoogleIamV1AuditConfigIn": "_policysimulator_4_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_policysimulator_5_GoogleIamV1AuditConfigOut",
        "GoogleIamV1PolicyIn": "_policysimulator_6_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_policysimulator_7_GoogleIamV1PolicyOut",
        "GoogleCloudPolicysimulatorV1ReplayIn": "_policysimulator_8_GoogleCloudPolicysimulatorV1ReplayIn",
        "GoogleCloudPolicysimulatorV1ReplayOut": "_policysimulator_9_GoogleCloudPolicysimulatorV1ReplayOut",
        "GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn": "_policysimulator_10_GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn",
        "GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut": "_policysimulator_11_GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut",
        "GoogleTypeDateIn": "_policysimulator_12_GoogleTypeDateIn",
        "GoogleTypeDateOut": "_policysimulator_13_GoogleTypeDateOut",
        "GoogleCloudPolicysimulatorV1ExplainedPolicyIn": "_policysimulator_14_GoogleCloudPolicysimulatorV1ExplainedPolicyIn",
        "GoogleCloudPolicysimulatorV1ExplainedPolicyOut": "_policysimulator_15_GoogleCloudPolicysimulatorV1ExplainedPolicyOut",
        "GoogleTypeExprIn": "_policysimulator_16_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_policysimulator_17_GoogleTypeExprOut",
        "GoogleIamV1AuditLogConfigIn": "_policysimulator_18_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_policysimulator_19_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudPolicysimulatorV1BindingExplanationIn": "_policysimulator_20_GoogleCloudPolicysimulatorV1BindingExplanationIn",
        "GoogleCloudPolicysimulatorV1BindingExplanationOut": "_policysimulator_21_GoogleCloudPolicysimulatorV1BindingExplanationOut",
        "GoogleCloudPolicysimulatorV1ExplainedAccessIn": "_policysimulator_22_GoogleCloudPolicysimulatorV1ExplainedAccessIn",
        "GoogleCloudPolicysimulatorV1ExplainedAccessOut": "_policysimulator_23_GoogleCloudPolicysimulatorV1ExplainedAccessOut",
        "GoogleLongrunningOperationIn": "_policysimulator_24_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_policysimulator_25_GoogleLongrunningOperationOut",
        "GoogleCloudPolicysimulatorV1ReplayResultIn": "_policysimulator_26_GoogleCloudPolicysimulatorV1ReplayResultIn",
        "GoogleCloudPolicysimulatorV1ReplayResultOut": "_policysimulator_27_GoogleCloudPolicysimulatorV1ReplayResultOut",
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn": "_policysimulator_28_GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn",
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut": "_policysimulator_29_GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut",
        "GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn": "_policysimulator_30_GoogleCloudPolicysimulatorV1ListReplayResultsResponseIn",
        "GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut": "_policysimulator_31_GoogleCloudPolicysimulatorV1ListReplayResultsResponseOut",
        "GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn": "_policysimulator_32_GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn",
        "GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut": "_policysimulator_33_GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut",
        "GoogleCloudPolicysimulatorV1AccessTupleIn": "_policysimulator_34_GoogleCloudPolicysimulatorV1AccessTupleIn",
        "GoogleCloudPolicysimulatorV1AccessTupleOut": "_policysimulator_35_GoogleCloudPolicysimulatorV1AccessTupleOut",
        "GoogleCloudPolicysimulatorV1AccessStateDiffIn": "_policysimulator_36_GoogleCloudPolicysimulatorV1AccessStateDiffIn",
        "GoogleCloudPolicysimulatorV1AccessStateDiffOut": "_policysimulator_37_GoogleCloudPolicysimulatorV1AccessStateDiffOut",
        "GoogleLongrunningListOperationsResponseIn": "_policysimulator_38_GoogleLongrunningListOperationsResponseIn",
        "GoogleLongrunningListOperationsResponseOut": "_policysimulator_39_GoogleLongrunningListOperationsResponseOut",
        "GoogleIamV1BindingIn": "_policysimulator_40_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_policysimulator_41_GoogleIamV1BindingOut",
        "GoogleRpcStatusIn": "_policysimulator_42_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_policysimulator_43_GoogleRpcStatusOut",
        "GoogleCloudPolicysimulatorV1ReplayDiffIn": "_policysimulator_44_GoogleCloudPolicysimulatorV1ReplayDiffIn",
        "GoogleCloudPolicysimulatorV1ReplayDiffOut": "_policysimulator_45_GoogleCloudPolicysimulatorV1ReplayDiffOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
    types["GoogleCloudPolicysimulatorV1ReplayIn"] = t.struct(
        {"config": t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayConfigIn"])}
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayIn"])
    types["GoogleCloudPolicysimulatorV1ReplayOut"] = t.struct(
        {
            "config": t.proxy(renames["GoogleCloudPolicysimulatorV1ReplayConfigOut"]),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "resultsSummary": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOut"])
    types["GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn"] = t.struct(
        {
            "unchangedCount": t.integer().optional(),
            "differenceCount": t.integer().optional(),
            "oldestDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "logCount": t.integer().optional(),
            "newestDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "errorCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultsSummaryIn"])
    types["GoogleCloudPolicysimulatorV1ReplayResultsSummaryOut"] = t.struct(
        {
            "unchangedCount": t.integer().optional(),
            "differenceCount": t.integer().optional(),
            "oldestDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "logCount": t.integer().optional(),
            "newestDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "errorCount": t.integer().optional(),
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
    types["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"] = t.struct(
        {
            "bindingExplanations": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1BindingExplanationIn"])
            ).optional(),
            "fullResourceName": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "relevance": t.string().optional(),
            "access": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyIn"])
    types["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"] = t.struct(
        {
            "bindingExplanations": t.array(
                t.proxy(renames["GoogleCloudPolicysimulatorV1BindingExplanationOut"])
            ).optional(),
            "fullResourceName": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "relevance": t.string().optional(),
            "access": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ExplainedPolicyOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
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
    types["GoogleCloudPolicysimulatorV1BindingExplanationIn"] = t.struct(
        {
            "rolePermission": t.string().optional(),
            "role": t.string().optional(),
            "rolePermissionRelevance": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "access": t.string(),
            "relevance": t.string().optional(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1BindingExplanationIn"])
    types["GoogleCloudPolicysimulatorV1BindingExplanationOut"] = t.struct(
        {
            "rolePermission": t.string().optional(),
            "role": t.string().optional(),
            "rolePermissionRelevance": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "access": t.string(),
            "relevance": t.string().optional(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1BindingExplanationOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleCloudPolicysimulatorV1ReplayResultIn"] = t.struct(
        {
            "diff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayDiffIn"]
            ).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "lastSeenDate": t.proxy(renames["GoogleTypeDateIn"]).optional(),
            "name": t.string().optional(),
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessTupleIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultIn"])
    types["GoogleCloudPolicysimulatorV1ReplayResultOut"] = t.struct(
        {
            "diff": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ReplayDiffOut"]
            ).optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "lastSeenDate": t.proxy(renames["GoogleTypeDateOut"]).optional(),
            "name": t.string().optional(),
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicysimulatorV1AccessTupleOut"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayResultOut"])
    types[
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn"
    ] = t.struct(
        {"membership": t.string().optional(), "relevance": t.string().optional()}
    ).named(
        renames["GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipIn"]
    )
    types[
        "GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut"
    ] = t.struct(
        {
            "membership": t.string().optional(),
            "relevance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPolicysimulatorV1BindingExplanationAnnotatedMembershipOut"]
    )
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
    types["GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn"] = t.struct(
        {"startTime": t.string().optional()}
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOperationMetadataIn"])
    types["GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut"] = t.struct(
        {
            "startTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1ReplayOperationMetadataOut"])
    types["GoogleCloudPolicysimulatorV1AccessTupleIn"] = t.struct(
        {
            "principal": t.string(),
            "permission": t.string(),
            "fullResourceName": t.string(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessTupleIn"])
    types["GoogleCloudPolicysimulatorV1AccessTupleOut"] = t.struct(
        {
            "principal": t.string(),
            "permission": t.string(),
            "fullResourceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessTupleOut"])
    types["GoogleCloudPolicysimulatorV1AccessStateDiffIn"] = t.struct(
        {
            "accessChange": t.string().optional(),
            "simulated": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessIn"]
            ).optional(),
            "baseline": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudPolicysimulatorV1AccessStateDiffIn"])
    types["GoogleCloudPolicysimulatorV1AccessStateDiffOut"] = t.struct(
        {
            "accessChange": t.string().optional(),
            "simulated": t.proxy(
                renames["GoogleCloudPolicysimulatorV1ExplainedAccessOut"]
            ).optional(),
            "baseline": t.proxy(
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

    functions = {}
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
    functions["projectsLocationsReplaysOperationsGet"] = policysimulator.get(
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
    functions["projectsLocationsReplaysOperationsList"] = policysimulator.get(
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
                "parent": t.string(),
                "pageSize": t.integer().optional(),
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
    functions["foldersLocationsReplaysOperationsList"] = policysimulator.get(
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

    return Import(
        importer="policysimulator",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
