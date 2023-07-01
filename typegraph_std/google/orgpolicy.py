from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_orgpolicy():
    orgpolicy = HTTPRuntime("https://orgpolicy.googleapis.com/")

    renames = {
        "ErrorResponse": "_orgpolicy_1_ErrorResponse",
        "GoogleProtobufEmptyIn": "_orgpolicy_2_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_orgpolicy_3_GoogleProtobufEmptyOut",
        "GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn": "_orgpolicy_4_GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn",
        "GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut": "_orgpolicy_5_GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut",
        "GoogleCloudOrgpolicyV2PolicyIn": "_orgpolicy_6_GoogleCloudOrgpolicyV2PolicyIn",
        "GoogleCloudOrgpolicyV2PolicyOut": "_orgpolicy_7_GoogleCloudOrgpolicyV2PolicyOut",
        "GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn": "_orgpolicy_8_GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn",
        "GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut": "_orgpolicy_9_GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut",
        "GoogleCloudOrgpolicyV2ListCustomConstraintsResponseIn": "_orgpolicy_10_GoogleCloudOrgpolicyV2ListCustomConstraintsResponseIn",
        "GoogleCloudOrgpolicyV2ListCustomConstraintsResponseOut": "_orgpolicy_11_GoogleCloudOrgpolicyV2ListCustomConstraintsResponseOut",
        "GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn": "_orgpolicy_12_GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn",
        "GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut": "_orgpolicy_13_GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut",
        "GoogleCloudOrgpolicyV2ListConstraintsResponseIn": "_orgpolicy_14_GoogleCloudOrgpolicyV2ListConstraintsResponseIn",
        "GoogleCloudOrgpolicyV2ListConstraintsResponseOut": "_orgpolicy_15_GoogleCloudOrgpolicyV2ListConstraintsResponseOut",
        "GoogleTypeExprIn": "_orgpolicy_16_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_orgpolicy_17_GoogleTypeExprOut",
        "GoogleCloudOrgpolicyV2ConstraintIn": "_orgpolicy_18_GoogleCloudOrgpolicyV2ConstraintIn",
        "GoogleCloudOrgpolicyV2ConstraintOut": "_orgpolicy_19_GoogleCloudOrgpolicyV2ConstraintOut",
        "GoogleCloudOrgpolicyV2PolicySpecIn": "_orgpolicy_20_GoogleCloudOrgpolicyV2PolicySpecIn",
        "GoogleCloudOrgpolicyV2PolicySpecOut": "_orgpolicy_21_GoogleCloudOrgpolicyV2PolicySpecOut",
        "GoogleCloudOrgpolicyV2AlternatePolicySpecIn": "_orgpolicy_22_GoogleCloudOrgpolicyV2AlternatePolicySpecIn",
        "GoogleCloudOrgpolicyV2AlternatePolicySpecOut": "_orgpolicy_23_GoogleCloudOrgpolicyV2AlternatePolicySpecOut",
        "GoogleCloudOrgpolicyV2ListPoliciesResponseIn": "_orgpolicy_24_GoogleCloudOrgpolicyV2ListPoliciesResponseIn",
        "GoogleCloudOrgpolicyV2ListPoliciesResponseOut": "_orgpolicy_25_GoogleCloudOrgpolicyV2ListPoliciesResponseOut",
        "GoogleCloudOrgpolicyV2ConstraintListConstraintIn": "_orgpolicy_26_GoogleCloudOrgpolicyV2ConstraintListConstraintIn",
        "GoogleCloudOrgpolicyV2ConstraintListConstraintOut": "_orgpolicy_27_GoogleCloudOrgpolicyV2ConstraintListConstraintOut",
        "GoogleCloudOrgpolicyV2CustomConstraintIn": "_orgpolicy_28_GoogleCloudOrgpolicyV2CustomConstraintIn",
        "GoogleCloudOrgpolicyV2CustomConstraintOut": "_orgpolicy_29_GoogleCloudOrgpolicyV2CustomConstraintOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn"])
    types["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut"])
    types["GoogleCloudOrgpolicyV2PolicyIn"] = t.struct(
        {
            "alternate": t.proxy(
                renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
            ).optional(),
            "name": t.string().optional(),
            "dryRunSpec": t.proxy(
                renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
            ).optional(),
            "spec": t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecIn"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicyIn"])
    types["GoogleCloudOrgpolicyV2PolicyOut"] = t.struct(
        {
            "alternate": t.proxy(
                renames["GoogleCloudOrgpolicyV2AlternatePolicySpecOut"]
            ).optional(),
            "name": t.string().optional(),
            "dryRunSpec": t.proxy(
                renames["GoogleCloudOrgpolicyV2PolicySpecOut"]
            ).optional(),
            "spec": t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicyOut"])
    types["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn"] = t.struct(
        {
            "enforce": t.boolean().optional(),
            "denyAll": t.boolean().optional(),
            "allowAll": t.boolean().optional(),
            "values": t.proxy(
                renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn"]
            ).optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn"])
    types["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut"] = t.struct(
        {
            "enforce": t.boolean().optional(),
            "denyAll": t.boolean().optional(),
            "allowAll": t.boolean().optional(),
            "values": t.proxy(
                renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut"]
            ).optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut"])
    types["GoogleCloudOrgpolicyV2ListCustomConstraintsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customConstraints": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2CustomConstraintIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ListCustomConstraintsResponseIn"])
    types["GoogleCloudOrgpolicyV2ListCustomConstraintsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "customConstraints": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2CustomConstraintOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ListCustomConstraintsResponseOut"])
    types["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn"] = t.struct(
        {
            "deniedValues": t.array(t.string()).optional(),
            "allowedValues": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn"])
    types["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut"] = t.struct(
        {
            "deniedValues": t.array(t.string()).optional(),
            "allowedValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut"])
    types["GoogleCloudOrgpolicyV2ListConstraintsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "constraints": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2ConstraintIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ListConstraintsResponseIn"])
    types["GoogleCloudOrgpolicyV2ListConstraintsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "constraints": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2ConstraintOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ListConstraintsResponseOut"])
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
    types["GoogleCloudOrgpolicyV2ConstraintIn"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudOrgpolicyV2ConstraintListConstraintIn"]
            ).optional(),
            "constraintDefault": t.string().optional(),
            "supportsDryRun": t.boolean().optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintIn"])
    types["GoogleCloudOrgpolicyV2ConstraintOut"] = t.struct(
        {
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "description": t.string().optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudOrgpolicyV2ConstraintListConstraintOut"]
            ).optional(),
            "constraintDefault": t.string().optional(),
            "supportsDryRun": t.boolean().optional(),
            "booleanConstraint": t.proxy(
                renames["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintOut"])
    types["GoogleCloudOrgpolicyV2PolicySpecIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn"])
            ).optional(),
            "reset": t.boolean().optional(),
            "inheritFromParent": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecIn"])
    types["GoogleCloudOrgpolicyV2PolicySpecOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut"])
            ).optional(),
            "reset": t.boolean().optional(),
            "inheritFromParent": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecOut"])
    types["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"] = t.struct(
        {
            "spec": t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecIn"]).optional(),
            "launch": t.string().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"])
    types["GoogleCloudOrgpolicyV2AlternatePolicySpecOut"] = t.struct(
        {
            "spec": t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecOut"]).optional(),
            "launch": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2AlternatePolicySpecOut"])
    types["GoogleCloudOrgpolicyV2ListPoliciesResponseIn"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2PolicyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ListPoliciesResponseIn"])
    types["GoogleCloudOrgpolicyV2ListPoliciesResponseOut"] = t.struct(
        {
            "policies": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ListPoliciesResponseOut"])
    types["GoogleCloudOrgpolicyV2ConstraintListConstraintIn"] = t.struct(
        {"supportsUnder": t.boolean().optional(), "supportsIn": t.boolean().optional()}
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintListConstraintIn"])
    types["GoogleCloudOrgpolicyV2ConstraintListConstraintOut"] = t.struct(
        {
            "supportsUnder": t.boolean().optional(),
            "supportsIn": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintListConstraintOut"])
    types["GoogleCloudOrgpolicyV2CustomConstraintIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "condition": t.string().optional(),
            "description": t.string().optional(),
            "actionType": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2CustomConstraintIn"])
    types["GoogleCloudOrgpolicyV2CustomConstraintOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "condition": t.string().optional(),
            "description": t.string().optional(),
            "actionType": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2CustomConstraintOut"])

    functions = {}
    functions["projectsPoliciesDelete"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesCreate"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesGetEffectivePolicy"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesList"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesGet"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesPatch"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsConstraintsList"] = orgpolicy.get(
        "v2/{parent}/constraints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2ListConstraintsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesCreate"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesGet"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesPatch"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesGetEffectivePolicy"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesList"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesDelete"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsPatch"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsCreate"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsList"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsGet"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsDelete"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsConstraintsList"] = orgpolicy.get(
        "v2/{parent}/constraints",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2ListConstraintsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesGetEffectivePolicy"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesCreate"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesList"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesGet"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesDelete"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesPatch"] = orgpolicy.patch(
        "v2/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string().optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersConstraintsList"] = orgpolicy.get(
        "v2/{parent}/constraints",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2ListConstraintsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="orgpolicy",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
