from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_orgpolicy() -> Import:
    orgpolicy = HTTPRuntime("https://orgpolicy.googleapis.com/")

    renames = {
        "ErrorResponse": "_orgpolicy_1_ErrorResponse",
        "GoogleCloudOrgpolicyV2PolicyIn": "_orgpolicy_2_GoogleCloudOrgpolicyV2PolicyIn",
        "GoogleCloudOrgpolicyV2PolicyOut": "_orgpolicy_3_GoogleCloudOrgpolicyV2PolicyOut",
        "GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn": "_orgpolicy_4_GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn",
        "GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut": "_orgpolicy_5_GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut",
        "GoogleCloudOrgpolicyV2PolicySpecIn": "_orgpolicy_6_GoogleCloudOrgpolicyV2PolicySpecIn",
        "GoogleCloudOrgpolicyV2PolicySpecOut": "_orgpolicy_7_GoogleCloudOrgpolicyV2PolicySpecOut",
        "GoogleCloudOrgpolicyV2ListCustomConstraintsResponseIn": "_orgpolicy_8_GoogleCloudOrgpolicyV2ListCustomConstraintsResponseIn",
        "GoogleCloudOrgpolicyV2ListCustomConstraintsResponseOut": "_orgpolicy_9_GoogleCloudOrgpolicyV2ListCustomConstraintsResponseOut",
        "GoogleCloudOrgpolicyV2ListPoliciesResponseIn": "_orgpolicy_10_GoogleCloudOrgpolicyV2ListPoliciesResponseIn",
        "GoogleCloudOrgpolicyV2ListPoliciesResponseOut": "_orgpolicy_11_GoogleCloudOrgpolicyV2ListPoliciesResponseOut",
        "GoogleProtobufEmptyIn": "_orgpolicy_12_GoogleProtobufEmptyIn",
        "GoogleProtobufEmptyOut": "_orgpolicy_13_GoogleProtobufEmptyOut",
        "GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn": "_orgpolicy_14_GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn",
        "GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut": "_orgpolicy_15_GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut",
        "GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn": "_orgpolicy_16_GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn",
        "GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut": "_orgpolicy_17_GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut",
        "GoogleCloudOrgpolicyV2AlternatePolicySpecIn": "_orgpolicy_18_GoogleCloudOrgpolicyV2AlternatePolicySpecIn",
        "GoogleCloudOrgpolicyV2AlternatePolicySpecOut": "_orgpolicy_19_GoogleCloudOrgpolicyV2AlternatePolicySpecOut",
        "GoogleCloudOrgpolicyV2ConstraintIn": "_orgpolicy_20_GoogleCloudOrgpolicyV2ConstraintIn",
        "GoogleCloudOrgpolicyV2ConstraintOut": "_orgpolicy_21_GoogleCloudOrgpolicyV2ConstraintOut",
        "GoogleCloudOrgpolicyV2CustomConstraintIn": "_orgpolicy_22_GoogleCloudOrgpolicyV2CustomConstraintIn",
        "GoogleCloudOrgpolicyV2CustomConstraintOut": "_orgpolicy_23_GoogleCloudOrgpolicyV2CustomConstraintOut",
        "GoogleCloudOrgpolicyV2ConstraintListConstraintIn": "_orgpolicy_24_GoogleCloudOrgpolicyV2ConstraintListConstraintIn",
        "GoogleCloudOrgpolicyV2ConstraintListConstraintOut": "_orgpolicy_25_GoogleCloudOrgpolicyV2ConstraintListConstraintOut",
        "GoogleTypeExprIn": "_orgpolicy_26_GoogleTypeExprIn",
        "GoogleTypeExprOut": "_orgpolicy_27_GoogleTypeExprOut",
        "GoogleCloudOrgpolicyV2ListConstraintsResponseIn": "_orgpolicy_28_GoogleCloudOrgpolicyV2ListConstraintsResponseIn",
        "GoogleCloudOrgpolicyV2ListConstraintsResponseOut": "_orgpolicy_29_GoogleCloudOrgpolicyV2ListConstraintsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudOrgpolicyV2PolicyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "spec": t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecIn"]).optional(),
            "dryRunSpec": t.proxy(
                renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
            ).optional(),
            "alternate": t.proxy(
                renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicyIn"])
    types["GoogleCloudOrgpolicyV2PolicyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "spec": t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecOut"]).optional(),
            "dryRunSpec": t.proxy(
                renames["GoogleCloudOrgpolicyV2PolicySpecOut"]
            ).optional(),
            "alternate": t.proxy(
                renames["GoogleCloudOrgpolicyV2AlternatePolicySpecOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicyOut"])
    types["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn"])
    types["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut"])
    types["GoogleCloudOrgpolicyV2PolicySpecIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn"])
            ).optional(),
            "inheritFromParent": t.boolean().optional(),
            "reset": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecIn"])
    types["GoogleCloudOrgpolicyV2PolicySpecOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "rules": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut"])
            ).optional(),
            "inheritFromParent": t.boolean().optional(),
            "reset": t.boolean().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecOut"])
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
    types["GoogleProtobufEmptyIn"] = t.struct({"_": t.string().optional()}).named(
        renames["GoogleProtobufEmptyIn"]
    )
    types["GoogleProtobufEmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GoogleProtobufEmptyOut"])
    types["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn"] = t.struct(
        {
            "denyAll": t.boolean().optional(),
            "enforce": t.boolean().optional(),
            "values": t.proxy(
                renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn"]
            ).optional(),
            "condition": t.proxy(renames["GoogleTypeExprIn"]).optional(),
            "allowAll": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleIn"])
    types["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut"] = t.struct(
        {
            "denyAll": t.boolean().optional(),
            "enforce": t.boolean().optional(),
            "values": t.proxy(
                renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut"]
            ).optional(),
            "condition": t.proxy(renames["GoogleTypeExprOut"]).optional(),
            "allowAll": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleOut"])
    types["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn"] = t.struct(
        {
            "allowedValues": t.array(t.string()).optional(),
            "deniedValues": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesIn"])
    types["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut"] = t.struct(
        {
            "allowedValues": t.array(t.string()).optional(),
            "deniedValues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValuesOut"])
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
    types["GoogleCloudOrgpolicyV2ConstraintIn"] = t.struct(
        {
            "booleanConstraint": t.proxy(
                renames["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintIn"]
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "supportsDryRun": t.boolean().optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudOrgpolicyV2ConstraintListConstraintIn"]
            ).optional(),
            "constraintDefault": t.string().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintIn"])
    types["GoogleCloudOrgpolicyV2ConstraintOut"] = t.struct(
        {
            "booleanConstraint": t.proxy(
                renames["GoogleCloudOrgpolicyV2ConstraintBooleanConstraintOut"]
            ).optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "supportsDryRun": t.boolean().optional(),
            "listConstraint": t.proxy(
                renames["GoogleCloudOrgpolicyV2ConstraintListConstraintOut"]
            ).optional(),
            "constraintDefault": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintOut"])
    types["GoogleCloudOrgpolicyV2CustomConstraintIn"] = t.struct(
        {
            "name": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "actionType": t.string().optional(),
            "displayName": t.string().optional(),
            "condition": t.string().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2CustomConstraintIn"])
    types["GoogleCloudOrgpolicyV2CustomConstraintOut"] = t.struct(
        {
            "name": t.string().optional(),
            "methodTypes": t.array(t.string()).optional(),
            "description": t.string().optional(),
            "resourceTypes": t.array(t.string()).optional(),
            "actionType": t.string().optional(),
            "displayName": t.string().optional(),
            "condition": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2CustomConstraintOut"])
    types["GoogleCloudOrgpolicyV2ConstraintListConstraintIn"] = t.struct(
        {"supportsIn": t.boolean().optional(), "supportsUnder": t.boolean().optional()}
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintListConstraintIn"])
    types["GoogleCloudOrgpolicyV2ConstraintListConstraintOut"] = t.struct(
        {
            "supportsIn": t.boolean().optional(),
            "supportsUnder": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ConstraintListConstraintOut"])
    types["GoogleTypeExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["GoogleTypeExprIn"])
    types["GoogleTypeExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleTypeExprOut"])
    types["GoogleCloudOrgpolicyV2ListConstraintsResponseIn"] = t.struct(
        {
            "constraints": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2ConstraintIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ListConstraintsResponseIn"])
    types["GoogleCloudOrgpolicyV2ListConstraintsResponseOut"] = t.struct(
        {
            "constraints": t.array(
                t.proxy(renames["GoogleCloudOrgpolicyV2ConstraintOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudOrgpolicyV2ListConstraintsResponseOut"])

    functions = {}
    functions["organizationsPoliciesPatch"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesDelete"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesCreate"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesList"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesGetEffectivePolicy"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsPoliciesGet"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsConstraintsList"] = orgpolicy.get(
        "v2/{parent}/constraints",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2ListConstraintsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsDelete"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2CustomConstraintOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsPatch"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2CustomConstraintOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsCreate"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2CustomConstraintOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsList"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2CustomConstraintOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsCustomConstraintsGet"] = orgpolicy.get(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudOrgpolicyV2CustomConstraintOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsConstraintsList"] = orgpolicy.get(
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
    functions["projectsPoliciesPatch"] = orgpolicy.post(
        "v2/{parent}/policies",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesGet"] = orgpolicy.post(
        "v2/{parent}/policies",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesGetEffectivePolicy"] = orgpolicy.post(
        "v2/{parent}/policies",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesList"] = orgpolicy.post(
        "v2/{parent}/policies",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesDelete"] = orgpolicy.post(
        "v2/{parent}/policies",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPoliciesCreate"] = orgpolicy.post(
        "v2/{parent}/policies",
        t.struct(
            {
                "parent": t.string(),
                "name": t.string().optional(),
                "spec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "dryRunSpec": t.proxy(
                    renames["GoogleCloudOrgpolicyV2PolicySpecIn"]
                ).optional(),
                "alternate": t.proxy(
                    renames["GoogleCloudOrgpolicyV2AlternatePolicySpecIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesCreate"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesGetEffectivePolicy"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesPatch"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesGet"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesList"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPoliciesDelete"] = orgpolicy.delete(
        "v2/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleProtobufEmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersConstraintsList"] = orgpolicy.get(
        "v2/{parent}/constraints",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudOrgpolicyV2ListConstraintsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="orgpolicy", renames=renames, types=types, functions=functions
    )
