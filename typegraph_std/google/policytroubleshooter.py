from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_policytroubleshooter():
    policytroubleshooter = HTTPRuntime("https://policytroubleshooter.googleapis.com/")

    renames = {
        "ErrorResponse": "_policytroubleshooter_1_ErrorResponse",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn": "_policytroubleshooter_2_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut": "_policytroubleshooter_3_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn": "_policytroubleshooter_4_GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut": "_policytroubleshooter_5_GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut",
        "GoogleIamV1BindingIn": "_policytroubleshooter_6_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_policytroubleshooter_7_GoogleIamV1BindingOut",
        "GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn": "_policytroubleshooter_8_GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn",
        "GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut": "_policytroubleshooter_9_GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut",
        "GoogleIamV1AuditLogConfigIn": "_policytroubleshooter_10_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_policytroubleshooter_11_GoogleIamV1AuditLogConfigOut",
        "GoogleTypeExprIn": "_policytroubleshooter_12_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_policytroubleshooter_13_GoogleTypeExprOut",
        "GoogleIamV1PolicyIn": "_policytroubleshooter_14_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_policytroubleshooter_15_GoogleIamV1PolicyOut",
        "GoogleIamV1AuditConfigIn": "_policytroubleshooter_16_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_policytroubleshooter_17_GoogleIamV1AuditConfigOut",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn": "_policytroubleshooter_18_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut": "_policytroubleshooter_19_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationIn": "_policytroubleshooter_20_GoogleCloudPolicytroubleshooterV1BindingExplanationIn",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationOut": "_policytroubleshooter_21_GoogleCloudPolicytroubleshooterV1BindingExplanationOut",
        "GoogleCloudPolicytroubleshooterV1AccessTupleIn": "_policytroubleshooter_22_GoogleCloudPolicytroubleshooterV1AccessTupleIn",
        "GoogleCloudPolicytroubleshooterV1AccessTupleOut": "_policytroubleshooter_23_GoogleCloudPolicytroubleshooterV1AccessTupleOut",
        "GoogleRpcStatusIn": "_policytroubleshooter_24_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_policytroubleshooter_25_GoogleRpcStatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"] = t.struct(
        {
            "bindingExplanations": t.array(
                t.proxy(
                    renames["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"]
                )
            ).optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "relevance": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "access": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"])
    types["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"] = t.struct(
        {
            "bindingExplanations": t.array(
                t.proxy(
                    renames["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"]
                )
            ).optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "relevance": t.string().optional(),
            "fullResourceName": t.string().optional(),
            "access": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"])
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
    types["GoogleTypeExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleIamV1PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigIn"])
            ).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingIn"])).optional(),
        }
    ).named(renames["GoogleIamV1PolicyIn"])
    types["GoogleIamV1PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(
                t.proxy(renames["GoogleIamV1AuditConfigOut"])
            ).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["GoogleIamV1BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyOut"])
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
    types[
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn"
    ] = t.struct(
        {
            "errors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "access": t.string().optional(),
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
            "errors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "access": t.string().optional(),
            "explainedPolicies": t.array(
                t.proxy(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut"]
    )
    types["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"] = t.struct(
        {
            "access": t.string(),
            "rolePermissionRelevance": t.string().optional(),
            "role": t.string().optional(),
            "relevance": t.string().optional(),
            "rolePermission": t.string().optional(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"])
    types["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"] = t.struct(
        {
            "access": t.string(),
            "rolePermissionRelevance": t.string().optional(),
            "role": t.string().optional(),
            "relevance": t.string().optional(),
            "rolePermission": t.string().optional(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"])
    types["GoogleCloudPolicytroubleshooterV1AccessTupleIn"] = t.struct(
        {
            "permission": t.string(),
            "principal": t.string(),
            "fullResourceName": t.string(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1AccessTupleIn"])
    types["GoogleCloudPolicytroubleshooterV1AccessTupleOut"] = t.struct(
        {
            "permission": t.string(),
            "principal": t.string(),
            "fullResourceName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1AccessTupleOut"])
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
