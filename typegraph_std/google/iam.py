from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_iam() -> Import:
    iam = HTTPRuntime("https://iam.googleapis.com/")

    renames = {
        "ErrorResponse": "_iam_1_ErrorResponse",
        "GoogleLongrunningOperationIn": "_iam_2_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_iam_3_GoogleLongrunningOperationOut",
        "GoogleIamV1LoggingAuditDataIn": "_iam_4_GoogleIamV1LoggingAuditDataIn",
        "GoogleIamV1LoggingAuditDataOut": "_iam_5_GoogleIamV1LoggingAuditDataOut",
        "GoogleRpcStatusIn": "_iam_6_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_iam_7_GoogleRpcStatusOut",
        "GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn": "_iam_8_GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn",
        "GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut": "_iam_9_GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut",
        "GoogleIamAdminV1AuditDataIn": "_iam_10_GoogleIamAdminV1AuditDataIn",
        "GoogleIamAdminV1AuditDataOut": "_iam_11_GoogleIamAdminV1AuditDataOut",
        "GoogleIamV2PolicyOperationMetadataIn": "_iam_12_GoogleIamV2PolicyOperationMetadataIn",
        "GoogleIamV2PolicyOperationMetadataOut": "_iam_13_GoogleIamV2PolicyOperationMetadataOut",
        "GoogleIamAdminV1AuditDataPermissionDeltaIn": "_iam_14_GoogleIamAdminV1AuditDataPermissionDeltaIn",
        "GoogleIamAdminV1AuditDataPermissionDeltaOut": "_iam_15_GoogleIamAdminV1AuditDataPermissionDeltaOut",
        "GoogleIamV2PolicyRuleIn": "_iam_16_GoogleIamV2PolicyRuleIn",
        "GoogleIamV2PolicyRuleOut": "_iam_17_GoogleIamV2PolicyRuleOut",
        "GoogleTypeExprIn": "_iam_18_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_iam_19_GoogleTypeExprOut",
        "GoogleIamV2DenyRuleIn": "_iam_20_GoogleIamV2DenyRuleIn",
        "GoogleIamV2DenyRuleOut": "_iam_21_GoogleIamV2DenyRuleOut",
        "GoogleIamV1BindingDeltaIn": "_iam_22_GoogleIamV1BindingDeltaIn",
        "GoogleIamV1BindingDeltaOut": "_iam_23_GoogleIamV1BindingDeltaOut",
        "GoogleIamV2PolicyIn": "_iam_24_GoogleIamV2PolicyIn",
        "GoogleIamV2PolicyOut": "_iam_25_GoogleIamV2PolicyOut",
        "GoogleIamV1PolicyDeltaIn": "_iam_26_GoogleIamV1PolicyDeltaIn",
        "GoogleIamV1PolicyDeltaOut": "_iam_27_GoogleIamV1PolicyDeltaOut",
        "GoogleIamV2ListPoliciesResponseIn": "_iam_28_GoogleIamV2ListPoliciesResponseIn",
        "GoogleIamV2ListPoliciesResponseOut": "_iam_29_GoogleIamV2ListPoliciesResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
    types["GoogleIamV1LoggingAuditDataIn"] = t.struct(
        {"policyDelta": t.proxy(renames["GoogleIamV1PolicyDeltaIn"]).optional()}
    ).named(renames["GoogleIamV1LoggingAuditDataIn"])
    types["GoogleIamV1LoggingAuditDataOut"] = t.struct(
        {
            "policyDelta": t.proxy(renames["GoogleIamV1PolicyDeltaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1LoggingAuditDataOut"])
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
    types["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn"])
    types["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut"])
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
    types["GoogleIamV2PolicyOperationMetadataIn"] = t.struct(
        {"createTime": t.string().optional()}
    ).named(renames["GoogleIamV2PolicyOperationMetadataIn"])
    types["GoogleIamV2PolicyOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyOperationMetadataOut"])
    types["GoogleIamAdminV1AuditDataPermissionDeltaIn"] = t.struct(
        {
            "addedPermissions": t.array(t.string()).optional(),
            "removedPermissions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamAdminV1AuditDataPermissionDeltaIn"])
    types["GoogleIamAdminV1AuditDataPermissionDeltaOut"] = t.struct(
        {
            "addedPermissions": t.array(t.string()).optional(),
            "removedPermissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamAdminV1AuditDataPermissionDeltaOut"])
    types["GoogleIamV2PolicyRuleIn"] = t.struct(
        {
            "denyRule": t.proxy(renames["GoogleIamV2DenyRuleIn"]).optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleIamV2PolicyRuleIn"])
    types["GoogleIamV2PolicyRuleOut"] = t.struct(
        {
            "denyRule": t.proxy(renames["GoogleIamV2DenyRuleOut"]).optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyRuleOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleIamV2DenyRuleIn"] = t.struct(
        {
            "deniedPrincipals": t.array(t.string()).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleIn"])
    types["GoogleIamV2DenyRuleOut"] = t.struct(
        {
            "deniedPrincipals": t.array(t.string()).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleOut"])
    types["GoogleIamV1BindingDeltaIn"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "member": t.string().optional(),
            "action": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleIamV1BindingDeltaIn"])
    types["GoogleIamV1BindingDeltaOut"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "member": t.string().optional(),
            "action": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingDeltaOut"])
    types["GoogleIamV2PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleIamV2PolicyRuleIn"])).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["GoogleIamV2PolicyIn"])
    types["GoogleIamV2PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "deleteTime": t.string().optional(),
            "createTime": t.string().optional(),
            "kind": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleIamV2PolicyRuleOut"])).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyOut"])
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
    functions["policiesDelete"] = iam.post(
        "v2/{parent}",
        t.struct(
            {
                "policyId": t.string().optional(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "uid": t.string().optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesGet"] = iam.post(
        "v2/{parent}",
        t.struct(
            {
                "policyId": t.string().optional(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "uid": t.string().optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesUpdate"] = iam.post(
        "v2/{parent}",
        t.struct(
            {
                "policyId": t.string().optional(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "uid": t.string().optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesListPolicies"] = iam.post(
        "v2/{parent}",
        t.struct(
            {
                "policyId": t.string().optional(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "uid": t.string().optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesCreatePolicy"] = iam.post(
        "v2/{parent}",
        t.struct(
            {
                "policyId": t.string().optional(),
                "parent": t.string(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "uid": t.string().optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
                "displayName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
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
