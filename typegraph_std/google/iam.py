from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_iam() -> Import:
    iam = HTTPRuntime("https://iam.googleapis.com/")

    renames = {
        "ErrorResponse": "_iam_1_ErrorResponse",
        "GoogleRpcStatusIn": "_iam_2_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_iam_3_GoogleRpcStatusOut",
        "GoogleIamV1BindingDeltaIn": "_iam_4_GoogleIamV1BindingDeltaIn",
        "GoogleIamV1BindingDeltaOut": "_iam_5_GoogleIamV1BindingDeltaOut",
        "GoogleIamV2ListPoliciesResponseIn": "_iam_6_GoogleIamV2ListPoliciesResponseIn",
        "GoogleIamV2ListPoliciesResponseOut": "_iam_7_GoogleIamV2ListPoliciesResponseOut",
        "GoogleIamV1LoggingAuditDataIn": "_iam_8_GoogleIamV1LoggingAuditDataIn",
        "GoogleIamV1LoggingAuditDataOut": "_iam_9_GoogleIamV1LoggingAuditDataOut",
        "GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn": "_iam_10_GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn",
        "GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut": "_iam_11_GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut",
        "GoogleIamV2PolicyIn": "_iam_12_GoogleIamV2PolicyIn",
        "GoogleIamV2PolicyOut": "_iam_13_GoogleIamV2PolicyOut",
        "GoogleLongrunningOperationIn": "_iam_14_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_iam_15_GoogleLongrunningOperationOut",
        "GoogleIamAdminV1AuditDataPermissionDeltaIn": "_iam_16_GoogleIamAdminV1AuditDataPermissionDeltaIn",
        "GoogleIamAdminV1AuditDataPermissionDeltaOut": "_iam_17_GoogleIamAdminV1AuditDataPermissionDeltaOut",
        "GoogleIamAdminV1AuditDataIn": "_iam_18_GoogleIamAdminV1AuditDataIn",
        "GoogleIamAdminV1AuditDataOut": "_iam_19_GoogleIamAdminV1AuditDataOut",
        "GoogleIamV1PolicyDeltaIn": "_iam_20_GoogleIamV1PolicyDeltaIn",
        "GoogleIamV1PolicyDeltaOut": "_iam_21_GoogleIamV1PolicyDeltaOut",
        "GoogleIamV2DenyRuleIn": "_iam_22_GoogleIamV2DenyRuleIn",
        "GoogleIamV2DenyRuleOut": "_iam_23_GoogleIamV2DenyRuleOut",
        "GoogleIamV2PolicyRuleIn": "_iam_24_GoogleIamV2PolicyRuleIn",
        "GoogleIamV2PolicyRuleOut": "_iam_25_GoogleIamV2PolicyRuleOut",
        "GoogleTypeExprIn": "_iam_26_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_iam_27_GoogleTypeExprOut",
        "GoogleIamV2PolicyOperationMetadataIn": "_iam_28_GoogleIamV2PolicyOperationMetadataIn",
        "GoogleIamV2PolicyOperationMetadataOut": "_iam_29_GoogleIamV2PolicyOperationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GoogleIamV1BindingDeltaIn"] = t.struct(
        {
            "action": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "member": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleIamV1BindingDeltaIn"])
    types["GoogleIamV1BindingDeltaOut"] = t.struct(
        {
            "action": t.string().optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "member": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingDeltaOut"])
    types["GoogleIamV2ListPoliciesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "policies": t.array(t.proxy(renames["GoogleIamV2PolicyIn"])).optional(),
        }
    ).named(renames["GoogleIamV2ListPoliciesResponseIn"])
    types["GoogleIamV2ListPoliciesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "policies": t.array(t.proxy(renames["GoogleIamV2PolicyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2ListPoliciesResponseOut"])
    types["GoogleIamV1LoggingAuditDataIn"] = t.struct(
        {"policyDelta": t.proxy(renames["GoogleIamV1PolicyDeltaIn"]).optional()}
    ).named(renames["GoogleIamV1LoggingAuditDataIn"])
    types["GoogleIamV1LoggingAuditDataOut"] = t.struct(
        {
            "policyDelta": t.proxy(renames["GoogleIamV1PolicyDeltaOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1LoggingAuditDataOut"])
    types["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn"])
    types["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut"])
    types["GoogleIamV2PolicyIn"] = t.struct(
        {
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleIamV2PolicyRuleIn"])).optional(),
        }
    ).named(renames["GoogleIamV2PolicyIn"])
    types["GoogleIamV2PolicyOut"] = t.struct(
        {
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "kind": t.string().optional(),
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleIamV2PolicyRuleOut"])).optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyOut"])
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["GoogleIamV2DenyRuleIn"] = t.struct(
        {
            "exceptionPrincipals": t.array(t.string()).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleIn"])
    types["GoogleIamV2DenyRuleOut"] = t.struct(
        {
            "exceptionPrincipals": t.array(t.string()).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "denialCondition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleOut"])
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
    types["GoogleIamV2PolicyOperationMetadataIn"] = t.struct(
        {"createTime": t.string().optional()}
    ).named(renames["GoogleIamV2PolicyOperationMetadataIn"])
    types["GoogleIamV2PolicyOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyOperationMetadataOut"])

    functions = {}
    functions["policiesUpdate"] = iam.post(
        "v2/{parent}",
        t.struct(
            {
                "policyId": t.string().optional(),
                "parent": t.string(),
                "uid": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
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
                "uid": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleLongrunningOperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["policiesDelete"] = iam.post(
        "v2/{parent}",
        t.struct(
            {
                "policyId": t.string().optional(),
                "parent": t.string(),
                "uid": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
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
                "uid": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
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
                "uid": t.string().optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "name": t.string().optional(),
                "rules": t.array(
                    t.proxy(renames["GoogleIamV2PolicyRuleIn"])
                ).optional(),
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

    return Import(importer="iam", renames=renames, types=types, functions=functions)
