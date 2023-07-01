from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_iam():
    iam = HTTPRuntime("https://iam.googleapis.com/")

    renames = {
        "ErrorResponse": "_iam_1_ErrorResponse",
        "GoogleIamV2PolicyIn": "_iam_2_GoogleIamV2PolicyIn",
        "GoogleIamV2PolicyOut": "_iam_3_GoogleIamV2PolicyOut",
        "GoogleIamV2PolicyOperationMetadataIn": "_iam_4_GoogleIamV2PolicyOperationMetadataIn",
        "GoogleIamV2PolicyOperationMetadataOut": "_iam_5_GoogleIamV2PolicyOperationMetadataOut",
        "GoogleRpcStatusIn": "_iam_6_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_iam_7_GoogleRpcStatusOut",
        "GoogleIamV1BindingDeltaIn": "_iam_8_GoogleIamV1BindingDeltaIn",
        "GoogleIamV1BindingDeltaOut": "_iam_9_GoogleIamV1BindingDeltaOut",
        "GoogleIamV2DenyRuleIn": "_iam_10_GoogleIamV2DenyRuleIn",
        "GoogleIamV2DenyRuleOut": "_iam_11_GoogleIamV2DenyRuleOut",
        "GoogleTypeExprIn": "_iam_12_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_iam_13_GoogleTypeExprOut",
        "GoogleIamAdminV1AuditDataIn": "_iam_14_GoogleIamAdminV1AuditDataIn",
        "GoogleIamAdminV1AuditDataOut": "_iam_15_GoogleIamAdminV1AuditDataOut",
        "GoogleIamV1LoggingAuditDataIn": "_iam_16_GoogleIamV1LoggingAuditDataIn",
        "GoogleIamV1LoggingAuditDataOut": "_iam_17_GoogleIamV1LoggingAuditDataOut",
        "GoogleIamV2PolicyRuleIn": "_iam_18_GoogleIamV2PolicyRuleIn",
        "GoogleIamV2PolicyRuleOut": "_iam_19_GoogleIamV2PolicyRuleOut",
        "GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn": "_iam_20_GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn",
        "GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut": "_iam_21_GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut",
        "GoogleIamV1PolicyDeltaIn": "_iam_22_GoogleIamV1PolicyDeltaIn",
        "GoogleIamV1PolicyDeltaOut": "_iam_23_GoogleIamV1PolicyDeltaOut",
        "GoogleIamAdminV1AuditDataPermissionDeltaIn": "_iam_24_GoogleIamAdminV1AuditDataPermissionDeltaIn",
        "GoogleIamAdminV1AuditDataPermissionDeltaOut": "_iam_25_GoogleIamAdminV1AuditDataPermissionDeltaOut",
        "GoogleLongrunningOperationIn": "_iam_26_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_iam_27_GoogleLongrunningOperationOut",
        "GoogleIamV2ListPoliciesResponseIn": "_iam_28_GoogleIamV2ListPoliciesResponseIn",
        "GoogleIamV2ListPoliciesResponseOut": "_iam_29_GoogleIamV2ListPoliciesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleIamV2PolicyIn"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["GoogleIamV2PolicyRuleIn"])).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["GoogleIamV2PolicyIn"])
    types["GoogleIamV2PolicyOut"] = t.struct(
        {
            "rules": t.array(t.proxy(renames["GoogleIamV2PolicyRuleOut"])).optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "deleteTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyOut"])
    types["GoogleIamV2PolicyOperationMetadataIn"] = t.struct(
        {"createTime": t.string().optional()}
    ).named(renames["GoogleIamV2PolicyOperationMetadataIn"])
    types["GoogleIamV2PolicyOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyOperationMetadataOut"])
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
    types["GoogleIamV1BindingDeltaIn"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "role": t.string().optional(),
            "member": t.string().optional(),
            "action": t.string().optional(),
        }
    ).named(renames["GoogleIamV1BindingDeltaIn"])
    types["GoogleIamV1BindingDeltaOut"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "role": t.string().optional(),
            "member": t.string().optional(),
            "action": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingDeltaOut"])
    types["GoogleIamV2DenyRuleIn"] = t.struct(
        {
            "denialCondition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleIn"])
    types["GoogleIamV2DenyRuleOut"] = t.struct(
        {
            "denialCondition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleOut"])
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
    types["GoogleIamAdminV1AuditDataIn"] = t.struct(
        {
            "permissionDelta": t.proxy(
                renames["GoogleIamAdminV1AuditDataPermissionDeltaIn"]
            ).optional()
        }
    ).named(renames["GoogleIamAdminV1AuditDataIn"])
    types["GoogleIamAdminV1AuditDataOut"] = t.struct(
        {
            "permissionDelta": t.proxy(
                renames["GoogleIamAdminV1AuditDataPermissionDeltaOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamAdminV1AuditDataOut"])
    types["GoogleIamV1LoggingAuditDataIn"] = t.struct(
        {"policyDelta": t.proxy(renames["GoogleIamV1PolicyDeltaIn"]).optional()}
    ).named(renames["GoogleIamV1LoggingAuditDataIn"])
    types["GoogleIamV1LoggingAuditDataOut"] = t.struct(
        {
            "policyDelta": t.proxy(renames["GoogleIamV1PolicyDeltaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1LoggingAuditDataOut"])
    types["GoogleIamV2PolicyRuleIn"] = t.struct(
        {
            "description": t.string().optional(),
            "denyRule": t.proxy(renames["GoogleIamV2DenyRuleIn"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyRuleIn"])
    types["GoogleIamV2PolicyRuleOut"] = t.struct(
        {
            "description": t.string().optional(),
            "denyRule": t.proxy(renames["GoogleIamV2DenyRuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyRuleOut"])
    types["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn"])
    types["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut"])
    types["GoogleIamV1PolicyDeltaIn"] = t.struct(
        {
            "bindingDeltas": t.array(
                t.proxy(renames["GoogleIamV1BindingDeltaIn"])
            ).optional()
        }
    ).named(renames["GoogleIamV1PolicyDeltaIn"])
    types["GoogleIamV1PolicyDeltaOut"] = t.struct(
        {
            "bindingDeltas": t.array(
                t.proxy(renames["GoogleIamV1BindingDeltaOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1PolicyDeltaOut"])
    types["GoogleIamAdminV1AuditDataPermissionDeltaIn"] = t.struct(
        {
            "removedPermissions": t.array(t.string()).optional(),
            "addedPermissions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamAdminV1AuditDataPermissionDeltaIn"])
    types["GoogleIamAdminV1AuditDataPermissionDeltaOut"] = t.struct(
        {
            "removedPermissions": t.array(t.string()).optional(),
            "addedPermissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamAdminV1AuditDataPermissionDeltaOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleIamV2ListPoliciesResponseIn"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["GoogleIamV2PolicyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleIamV2ListPoliciesResponseIn"])
    types["GoogleIamV2ListPoliciesResponseOut"] = t.struct(
        {
            "policies": t.array(t.proxy(renames["GoogleIamV2PolicyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2ListPoliciesResponseOut"])

    functions = {}
    functions["policiesListPolicies"] = iam.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleIamV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesCreatePolicy"] = iam.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleIamV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesDelete"] = iam.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleIamV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesUpdate"] = iam.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleIamV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesGet"] = iam.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleIamV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesOperationsGet"] = iam.get(
        "v2/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="iam", renames=renames, types=Box(types), functions=Box(functions)
    )
