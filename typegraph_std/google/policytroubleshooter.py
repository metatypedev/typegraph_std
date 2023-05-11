from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_policytroubleshooter() -> Import:
    policytroubleshooter = HTTPRuntime("https://policytroubleshooter.googleapis.com/")

    renames = {
        "ErrorResponse": "_policytroubleshooter_1_ErrorResponse",
        "GoogleIamV1BindingIn": "_policytroubleshooter_2_GoogleIamV1BindingIn",
        "GoogleIamV1BindingOut": "_policytroubleshooter_3_GoogleIamV1BindingOut",
        "GoogleIamV1PolicyIn": "_policytroubleshooter_4_GoogleIamV1PolicyIn",
        "GoogleIamV1PolicyOut": "_policytroubleshooter_5_GoogleIamV1PolicyOut",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationIn": "_policytroubleshooter_6_GoogleCloudPolicytroubleshooterV1BindingExplanationIn",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationOut": "_policytroubleshooter_7_GoogleCloudPolicytroubleshooterV1BindingExplanationOut",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn": "_policytroubleshooter_8_GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn",
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut": "_policytroubleshooter_9_GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut",
        "GoogleRpcStatusIn": "_policytroubleshooter_10_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_policytroubleshooter_11_GoogleRpcStatusOut",
        "GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn": "_policytroubleshooter_12_GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn",
        "GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut": "_policytroubleshooter_13_GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn": "_policytroubleshooter_14_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut": "_policytroubleshooter_15_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut",
        "GoogleCloudPolicytroubleshooterV1AccessTupleIn": "_policytroubleshooter_16_GoogleCloudPolicytroubleshooterV1AccessTupleIn",
        "GoogleCloudPolicytroubleshooterV1AccessTupleOut": "_policytroubleshooter_17_GoogleCloudPolicytroubleshooterV1AccessTupleOut",
        "GoogleTypeExprIn": "_policytroubleshooter_18_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_policytroubleshooter_19_GoogleTypeExprOut",
        "GoogleIamV1AuditConfigIn": "_policytroubleshooter_20_GoogleIamV1AuditConfigIn",
        "GoogleIamV1AuditConfigOut": "_policytroubleshooter_21_GoogleIamV1AuditConfigOut",
        "GoogleIamV1AuditLogConfigIn": "_policytroubleshooter_22_GoogleIamV1AuditLogConfigIn",
        "GoogleIamV1AuditLogConfigOut": "_policytroubleshooter_23_GoogleIamV1AuditLogConfigOut",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn": "_policytroubleshooter_24_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestIn",
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut": "_policytroubleshooter_25_GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"] = t.struct(
        {
            "role": t.string().optional(),
            "rolePermission": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "rolePermissionRelevance": t.string().optional(),
            "access": t.string(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "relevance": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"])
    types["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"] = t.struct(
        {
            "role": t.string().optional(),
            "rolePermission": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "rolePermissionRelevance": t.string().optional(),
            "access": t.string(),
            "memberships": t.struct({"_": t.string().optional()}).optional(),
            "relevance": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"])
    types[
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn"
    ] = t.struct(
        {"membership": t.string().optional(), "relevance": t.string().optional()}
    ).named(
        renames[
            "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipIn"
        ]
    )
    types[
        "GoogleCloudPolicytroubleshooterV1BindingExplanationAnnotatedMembershipOut"
    ] = t.struct(
        {
            "membership": t.string().optional(),
            "relevance": t.string().optional(),
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
    types["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"] = t.struct(
        {
            "relevance": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyIn"]).optional(),
            "fullResourceName": t.string().optional(),
            "bindingExplanations": t.array(
                t.proxy(
                    renames["GoogleCloudPolicytroubleshooterV1BindingExplanationIn"]
                )
            ).optional(),
            "access": t.string().optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"])
    types["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"] = t.struct(
        {
            "relevance": t.string().optional(),
            "policy": t.proxy(renames["GoogleIamV1PolicyOut"]).optional(),
            "fullResourceName": t.string().optional(),
            "bindingExplanations": t.array(
                t.proxy(
                    renames["GoogleCloudPolicytroubleshooterV1BindingExplanationOut"]
                )
            ).optional(),
            "access": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"])
    types[
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn"
    ] = t.struct(
        {
            "explainedPolicies": t.array(
                t.proxy(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyIn"])
            ).optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusIn"])).optional(),
            "access": t.string().optional(),
        }
    ).named(
        renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseIn"]
    )
    types[
        "GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut"
    ] = t.struct(
        {
            "explainedPolicies": t.array(
                t.proxy(renames["GoogleCloudPolicytroubleshooterV1ExplainedPolicyOut"])
            ).optional(),
            "errors": t.array(t.proxy(renames["GoogleRpcStatusOut"])).optional(),
            "access": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames["GoogleCloudPolicytroubleshooterV1TroubleshootIamPolicyResponseOut"]
    )
    types["GoogleCloudPolicytroubleshooterV1AccessTupleIn"] = t.struct(
        {
            "principal": t.string(),
            "fullResourceName": t.string(),
            "permission": t.string(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1AccessTupleIn"])
    types["GoogleCloudPolicytroubleshooterV1AccessTupleOut"] = t.struct(
        {
            "principal": t.string(),
            "fullResourceName": t.string(),
            "permission": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudPolicytroubleshooterV1AccessTupleOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
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
        types=types,
        functions=functions,
    )
