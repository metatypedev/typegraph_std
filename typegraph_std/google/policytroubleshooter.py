from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_policytroubleshooter() -> Import:
    policytroubleshooter = HTTPRuntime("https://policytroubleshooter.googleapis.com/")

    renames = {
        "ErrorResponse": "_policytroubleshooter_1_ErrorResponse",
        "GoogleIamV1BindingIn": "_policytroubleshooter_2_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_policytroubleshooter_3_GoogleIamV1BindingOut",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn": "_policytroubleshooter_4_GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut": "_policytroubleshooter_5_GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut",
        "GoogleRpcStatusIn": "_policytroubleshooter_6_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_policytroubleshooter_7_GoogleRpcStatusOut",
        "GoogleTypeExprIn": "_policytroubleshooter_8_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_policytroubleshooter_9_GoogleTypeExprOut",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn": "_policytroubleshooter_10_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut": "_policytroubleshooter_11_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationIn": "_policytroubleshooter_12_GoogleCloudPolicytroubleshooterV1BindingExplanationIn",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationOut": "_policytroubleshooter_13_GoogleCloudPolicytroubleshooterV1BindingExplanationOut",
        "GoogleIamV1PolicyIn": "_policytroubleshooter_14_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_policytroubleshooter_15_GoogleIamV1PolicyOut",
        "GoogleIamV1AuditLogConfigIn": "_policytroubleshooter_16_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_policytroubleshooter_17_GoogleIamV1AuditLogConfigOut",
        "GoogleIamV1AuditConfigIn": "_policytroubleshooter_18_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_policytroubleshooter_19_GoogleIamV1AuditConfigOut",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn": "_policytroubleshooter_20_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut": "_policytroubleshooter_21_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut",
        "GoogleCloudPolicytroubleshooterV1AccessTupleIn": "_policytroubleshooter_22_GoogleCloudPolicytroubleshooterV1AccessTupleIn",
        "GoogleCloudPolicytroubleshooterV1AccessTupleOut": "_policytroubleshooter_23_GoogleCloudPolicytroubleshooterV1AccessTupleOut",
        "GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn": "_policytroubleshooter_24_GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn",
        "GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut": "_policytroubleshooter_25_GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleIamV1BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingIn"])
    types["GoogleIamV1BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingOut"])
    types[
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn"
    ] = t.struct(
        {"relevance": t.string().optional(), "membership": t.string().optional()}
    ).named(
        renames[
            "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn"
        ]
    )
    types[
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut"
    ] = t.struct(
        {
            "relevance": t.string().optional(),
            "membership": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut"
        ]
    )
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn"] = t.struct(
        {
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicytroubleshooterV1AccessTupleIn"]
            ).optional()
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn"])
    types[
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut"
    ] = t.struct(
        {
            "accessTuple": t.proxy(
                renames["GoogleCloudPolicytroubleshooterV1AccessTupleOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut"]
    )
    types["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "rolePermission": t.string().optional(),
            "relevance": t.string().optional(),
            "access": t.string(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "rolePermissionRelevance": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"])
    types["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "rolePermission": t.string().optional(),
            "relevance": t.string().optional(),
            "access": t.string(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "rolePermissionRelevance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
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
    types[
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn"
    ] = t.struct(
        {
            "access": t.string().optional(),
            "explainedPolicies": t.array(
                t.proxy(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"])
            ).optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
        }
    ).named(
        renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn"]
    )
    types[
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut"
    ] = t.struct(
        {
            "access": t.string().optional(),
            "explainedPolicies": t.array(
                t.proxy(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"])
            ).optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut"]
    )
    types["GoogleCloudPolicytroubleshooterV1AccessTupleIn"] = t.struct(
        {
            "permission": t.string(),
            "fullResourceName": t.string(),
            "principal": t.string(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1AccessTupleIn"])
    types["GoogleCloudPolicytroubleshooterV1AccessTupleOut"] = t.struct(
        {
            "permission": t.string(),
            "fullResourceName": t.string(),
            "principal": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1AccessTupleOut"])
    types["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "bindingExplanations": t.array(
                t.proxy(
                    renames["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"]
                )
            ).optional(),
            "relevance": t.string().optional(),
            "access": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"])
    types["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "bindingExplanations": t.array(
                t.proxy(
                    renames["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"]
                )
            ).optional(),
            "relevance": t.string().optional(),
            "access": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"])

    functions = {}
    functions["iamTroubleshoot"] = policytroubleshooter.post(
        "v1/iam:troubleshoot",
        t.struct(
            {
                "accessTuple": t.proxy(
                    renames["GoogleCloudPolicytroubleshooterV1AccessTupleIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="policytroubleshooter",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
