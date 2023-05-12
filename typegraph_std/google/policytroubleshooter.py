from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_policytroubleshooter() -> Import:
    policytroubleshooter = HTTPRuntime("https://policytroubleshooter.googleapis.com/")

    renames = {
        "ErrorResponse": "_policytroubleshooter_1_ErrorResponse",
        "GoogleTypeExprIn": "_policytroubleshooter_2_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_policytroubleshooter_3_GoogleTypeExprOut",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationIn": "_policytroubleshooter_4_GoogleCloudPolicytroubleshooterV1BindingExplanationIn",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationOut": "_policytroubleshooter_5_GoogleCloudPolicytroubleshooterV1BindingExplanationOut",
        "GoogleIamV1AuditLogConfigIn": "_policytroubleshooter_6_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_policytroubleshooter_7_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn": "_policytroubleshooter_8_GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut": "_policytroubleshooter_9_GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn": "_policytroubleshooter_10_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut": "_policytroubleshooter_11_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut",
        "GoogleIamV1PolicyIn": "_policytroubleshooter_12_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_policytroubleshooter_13_GoogleIamV1PolicyOut",
        "GoogleRpcStatusIn": "_policytroubleshooter_14_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_policytroubleshooter_15_GoogleRpcStatusOut",
        "GoogleIamV1BindingIn": "_policytroubleshooter_16_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_policytroubleshooter_17_GoogleIamV1BindingOut",
        "GoogleCloudPolicytroubleshooterV1AccessTupleIn": "_policytroubleshooter_18_GoogleCloudPolicytroubleshooterV1AccessTupleIn",
        "GoogleCloudPolicytroubleshooterV1AccessTupleOut": "_policytroubleshooter_19_GoogleCloudPolicytroubleshooterV1AccessTupleOut",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn": "_policytroubleshooter_20_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut": "_policytroubleshooter_21_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut",
        "GoogleIamV1AuditConfigIn": "_policytroubleshooter_22_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_policytroubleshooter_23_GoogleIamV1AuditConfigOut",
        "GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn": "_policytroubleshooter_24_GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn",
        "GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut": "_policytroubleshooter_25_GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"] = t.struct(
        {
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "rolePermissionRelevance": t.string().optional(),
            "relevance": t.string().optional(),
            "access": t.string(),
            "rolePermission": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"])
    types["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"] = t.struct(
        {
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "rolePermissionRelevance": t.string().optional(),
            "relevance": t.string().optional(),
            "access": t.string(),
            "rolePermission": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"])
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
    types[
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn"
    ] = t.struct(
        {
            "access": t.string().optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "explainedPolicies": t.array(
                t.proxy(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"])
            ).optional(),
        }
    ).named(
        renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn"]
    )
    types[
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut"
    ] = t.struct(
        {
            "access": t.string().optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "explainedPolicies": t.array(
                t.proxy(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut"]
    )
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
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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
    types["GoogleCloudPolicytroubleshooterV1AccessTupleIn"] = t.struct(
        {
            "principal": t.string(),
            "permission": t.string(),
            "fullResourceName": t.string(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1AccessTupleIn"])
    types["GoogleCloudPolicytroubleshooterV1AccessTupleOut"] = t.struct(
        {
            "principal": t.string(),
            "permission": t.string(),
            "fullResourceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1AccessTupleOut"])
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
    types["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "bindingExplanations": t.array(
                t.proxy(
                    renames["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"]
                )
            ).optional(),
            "access": t.string().optional(),
            "relevance": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"])
    types["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"] = t.struct(
        {
            "fullResourceName": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "bindingExplanations": t.array(
                t.proxy(
                    renames["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"]
                )
            ).optional(),
            "access": t.string().optional(),
            "relevance": t.string().optional(),
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
