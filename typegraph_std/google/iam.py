from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_iam() -> Import:
    iam = HTTPRuntime("https://iam.googleapis.com/")

    renames = {
        "ErrorResponse": "_iam_1_ErrorResponse",
        "GoogleIamV2DenyRuleIn": "_iam_2_GoogleIamV2DenyRuleIn",
        "GoogleIamV2DenyRuleOut": "_iam_3_GoogleIamV2DenyRuleOut",
        "GoogleIamAdminV1AuditDataPermissionDeltaIn": "_iam_4_GoogleIamAdminV1AuditDataPermissionDeltaIn",
        "GoogleIamAdminV1AuditDataPermissionDeltaOut": "_iam_5_GoogleIamAdminV1AuditDataPermissionDeltaOut",
        "GoogleIamAdminV1AuditDataIn": "_iam_6_GoogleIamAdminV1AuditDataIn",
        "GoogleIamAdminV1AuditDataOut": "_iam_7_GoogleIamAdminV1AuditDataOut",
        "GoogleIamV1LoggingAuditDataIn": "_iam_8_GoogleIamV1LoggingAuditDataIn",
        "GoogleIamV1LoggingAuditDataOut": "_iam_9_GoogleIamV1LoggingAuditDataOut",
        "GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn": "_iam_10_GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn",
        "GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut": "_iam_11_GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut",
        "GoogleIamV2PolicyRuleIn": "_iam_12_GoogleIamV2PolicyRuleIn",
        "GoogleIamV2PolicyRuleOut": "_iam_13_GoogleIamV2PolicyRuleOut",
        "GoogleLongrunningOperationIn": "_iam_14_GoogleLongrunningOperationIn",
        "GoogleLongrunningOperationOut": "_iam_15_GoogleLongrunningOperationOut",
        "GoogleTypeExprIn": "_iam_16_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_iam_17_GoogleTypeExprOut",
        "GoogleIamV1BindingDeltaIn": "_iam_18_GoogleIamV1BindingDeltaIn",
        "GoogleIamV1BindingDeltaOut": "_iam_19_GoogleIamV1BindingDeltaOut",
        "GoogleIamV2PolicyOperationMetadataIn": "_iam_20_GoogleIamV2PolicyOperationMetadataIn",
        "GoogleIamV2PolicyOperationMetadataOut": "_iam_21_GoogleIamV2PolicyOperationMetadataOut",
        "GoogleIamV2ListPoliciesResponseIn": "_iam_22_GoogleIamV2ListPoliciesResponseIn",
        "GoogleIamV2ListPoliciesResponseOut": "_iam_23_GoogleIamV2ListPoliciesResponseOut",
        "GoogleIamV2PolicyIn": "_iam_24_GoogleIamV2PolicyIn",
        "GoogleIamV2PolicyOut": "_iam_25_GoogleIamV2PolicyOut",
        "GoogleRpcStatusIn": "_iam_26_GoogleRpcStatusIn",
        "GoogleRpcStatusOut": "_iam_27_GoogleRpcStatusOut",
        "GoogleIamV1PolicyDeltaIn": "_iam_28_GoogleIamV1PolicyDeltaIn",
        "GoogleIamV1PolicyDeltaOut": "_iam_29_GoogleIamV1PolicyDeltaOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleIamV2DenyRuleIn"] = t.struct(
        {
            "denialCondition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleIn"])
    types["GoogleIamV2DenyRuleOut"] = t.struct(
        {
            "denialCondition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "exceptionPrincipals": t.array(t.string()).optional(),
            "exceptionPermissions": t.array(t.string()).optional(),
            "deniedPrincipals": t.array(t.string()).optional(),
            "deniedPermissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2DenyRuleOut"])
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
    types["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataIn"])
    types["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleIamV1betaWorkloadIdentityPoolOperationMetadataOut"])
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
    types["GoogleLongrunningOperationIn"] = t.struct(
        {
            "error": t.proxy(renames["GoogleRpcStatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationIn"])
    types["GoogleLongrunningOperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleLongrunningOperationOut"])
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
    types["GoogleIamV1BindingDeltaIn"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "action": t.string().optional(),
            "member": t.string().optional(),
            "role": t.string().optional(),
        }
    ).named(renames["GoogleIamV1BindingDeltaIn"])
    types["GoogleIamV1BindingDeltaOut"] = t.struct(
        {
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "action": t.string().optional(),
            "member": t.string().optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV1BindingDeltaOut"])
    types["GoogleIamV2PolicyOperationMetadataIn"] = t.struct(
        {"createTime": t.string().optional()}
    ).named(renames["GoogleIamV2PolicyOperationMetadataIn"])
    types["GoogleIamV2PolicyOperationMetadataOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyOperationMetadataOut"])
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
    types["GoogleIamV2PolicyIn"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleIamV2PolicyRuleIn"])).optional(),
        }
    ).named(renames["GoogleIamV2PolicyIn"])
    types["GoogleIamV2PolicyOut"] = t.struct(
        {
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "deleteTime": t.string().optional(),
            "kind": t.string().optional(),
            "updateTime": t.string().optional(),
            "uid": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "rules": t.array(t.proxy(renames["GoogleIamV2PolicyRuleOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleIamV2PolicyOut"])
    types["GoogleRpcStatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["GoogleRpcStatusIn"])
    types["GoogleRpcStatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleRpcStatusOut"])
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

    functions = {}
    functions["policiesGet"] = iam.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "uid": t.string().optional(),
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
    functions["policiesDelete"] = iam.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "uid": t.string().optional(),
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
    functions["policiesListPolicies"] = iam.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "uid": t.string().optional(),
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
    functions["policiesCreatePolicy"] = iam.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "uid": t.string().optional(),
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
    functions["policiesUpdate"] = iam.put(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "annotations": t.struct({"_": t.string().optional()}).optional(),
                "displayName": t.string().optional(),
                "etag": t.string().optional(),
                "uid": t.string().optional(),
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

    return Import(
        importer="iam", renames=renames, types=Box(types), functions=Box(functions)
    )
