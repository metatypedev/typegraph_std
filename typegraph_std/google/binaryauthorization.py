from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_binaryauthorization() -> Import:
    binaryauthorization = HTTPRuntime("https://binaryauthorization.googleapis.com/")

    renames = {
        "ErrorResponse": "_binaryauthorization_1_ErrorResponse",
        "ExprIn": "_binaryauthorization_2_ExprIn",
        "ExprOut": "_binaryauthorization_3_ExprOut",
        "PolicyIn": "_binaryauthorization_4_PolicyIn",
        "PolicyOut": "_binaryauthorization_5_PolicyOut",
        "AdmissionRuleIn": "_binaryauthorization_6_AdmissionRuleIn",
        "AdmissionRuleOut": "_binaryauthorization_7_AdmissionRuleOut",
        "ListAttestorsResponseIn": "_binaryauthorization_8_ListAttestorsResponseIn",
        "ListAttestorsResponseOut": "_binaryauthorization_9_ListAttestorsResponseOut",
        "SignatureIn": "_binaryauthorization_10_SignatureIn",
        "SignatureOut": "_binaryauthorization_11_SignatureOut",
        "EmptyIn": "_binaryauthorization_12_EmptyIn",
        "EmptyOut": "_binaryauthorization_13_EmptyOut",
        "TestIamPermissionsRequestIn": "_binaryauthorization_14_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_binaryauthorization_15_TestIamPermissionsRequestOut",
        "BindingIn": "_binaryauthorization_16_BindingIn",
        "BindingOut": "_binaryauthorization_17_BindingOut",
        "AttestorIn": "_binaryauthorization_18_AttestorIn",
        "AttestorOut": "_binaryauthorization_19_AttestorOut",
        "ValidateAttestationOccurrenceResponseIn": "_binaryauthorization_20_ValidateAttestationOccurrenceResponseIn",
        "ValidateAttestationOccurrenceResponseOut": "_binaryauthorization_21_ValidateAttestationOccurrenceResponseOut",
        "TestIamPermissionsResponseIn": "_binaryauthorization_22_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_binaryauthorization_23_TestIamPermissionsResponseOut",
        "AttestationOccurrenceIn": "_binaryauthorization_24_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_binaryauthorization_25_AttestationOccurrenceOut",
        "JwtIn": "_binaryauthorization_26_JwtIn",
        "JwtOut": "_binaryauthorization_27_JwtOut",
        "AttestorPublicKeyIn": "_binaryauthorization_28_AttestorPublicKeyIn",
        "AttestorPublicKeyOut": "_binaryauthorization_29_AttestorPublicKeyOut",
        "ValidateAttestationOccurrenceRequestIn": "_binaryauthorization_30_ValidateAttestationOccurrenceRequestIn",
        "ValidateAttestationOccurrenceRequestOut": "_binaryauthorization_31_ValidateAttestationOccurrenceRequestOut",
        "SetIamPolicyRequestIn": "_binaryauthorization_32_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_binaryauthorization_33_SetIamPolicyRequestOut",
        "IamPolicyIn": "_binaryauthorization_34_IamPolicyIn",
        "IamPolicyOut": "_binaryauthorization_35_IamPolicyOut",
        "AdmissionWhitelistPatternIn": "_binaryauthorization_36_AdmissionWhitelistPatternIn",
        "AdmissionWhitelistPatternOut": "_binaryauthorization_37_AdmissionWhitelistPatternOut",
        "PkixPublicKeyIn": "_binaryauthorization_38_PkixPublicKeyIn",
        "PkixPublicKeyOut": "_binaryauthorization_39_PkixPublicKeyOut",
        "UserOwnedGrafeasNoteIn": "_binaryauthorization_40_UserOwnedGrafeasNoteIn",
        "UserOwnedGrafeasNoteOut": "_binaryauthorization_41_UserOwnedGrafeasNoteOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["PolicyIn"] = t.struct(
        {
            "admissionWhitelistPatterns": t.array(
                t.proxy(renames["AdmissionWhitelistPatternIn"])
            ).optional(),
            "kubernetesServiceAccountAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "clusterAdmissionRules": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "istioServiceIdentityAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "globalPolicyEvaluationMode": t.string().optional(),
            "etag": t.string().optional(),
            "kubernetesNamespaceAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "admissionWhitelistPatterns": t.array(
                t.proxy(renames["AdmissionWhitelistPatternOut"])
            ).optional(),
            "kubernetesServiceAccountAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "clusterAdmissionRules": t.struct({"_": t.string().optional()}).optional(),
            "description": t.string().optional(),
            "istioServiceIdentityAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "globalPolicyEvaluationMode": t.string().optional(),
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "kubernetesNamespaceAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "defaultAdmissionRule": t.proxy(renames["AdmissionRuleOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["AdmissionRuleIn"] = t.struct(
        {
            "enforcementMode": t.string(),
            "evaluationMode": t.string(),
            "requireAttestationsBy": t.array(t.string()).optional(),
        }
    ).named(renames["AdmissionRuleIn"])
    types["AdmissionRuleOut"] = t.struct(
        {
            "enforcementMode": t.string(),
            "evaluationMode": t.string(),
            "requireAttestationsBy": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdmissionRuleOut"])
    types["ListAttestorsResponseIn"] = t.struct(
        {
            "attestors": t.array(t.proxy(renames["AttestorIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAttestorsResponseIn"])
    types["ListAttestorsResponseOut"] = t.struct(
        {
            "attestors": t.array(t.proxy(renames["AttestorOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAttestorsResponseOut"])
    types["SignatureIn"] = t.struct(
        {"publicKeyId": t.string().optional(), "signature": t.string().optional()}
    ).named(renames["SignatureIn"])
    types["SignatureOut"] = t.struct(
        {
            "publicKeyId": t.string().optional(),
            "signature": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SignatureOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["AttestorIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "userOwnedGrafeasNote": t.proxy(
                renames["UserOwnedGrafeasNoteIn"]
            ).optional(),
            "description": t.string().optional(),
            "name": t.string(),
        }
    ).named(renames["AttestorIn"])
    types["AttestorOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "userOwnedGrafeasNote": t.proxy(
                renames["UserOwnedGrafeasNoteOut"]
            ).optional(),
            "description": t.string().optional(),
            "name": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestorOut"])
    types["ValidateAttestationOccurrenceResponseIn"] = t.struct(
        {"result": t.string().optional(), "denialReason": t.string().optional()}
    ).named(renames["ValidateAttestationOccurrenceResponseIn"])
    types["ValidateAttestationOccurrenceResponseOut"] = t.struct(
        {
            "result": t.string().optional(),
            "denialReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateAttestationOccurrenceResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["AttestationOccurrenceIn"] = t.struct(
        {
            "serializedPayload": t.string(),
            "jwts": t.array(t.proxy(renames["JwtIn"])).optional(),
            "signatures": t.array(t.proxy(renames["SignatureIn"])).optional(),
        }
    ).named(renames["AttestationOccurrenceIn"])
    types["AttestationOccurrenceOut"] = t.struct(
        {
            "serializedPayload": t.string(),
            "jwts": t.array(t.proxy(renames["JwtOut"])).optional(),
            "signatures": t.array(t.proxy(renames["SignatureOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationOccurrenceOut"])
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
    types["AttestorPublicKeyIn"] = t.struct(
        {
            "id": t.string().optional(),
            "asciiArmoredPgpPublicKey": t.string().optional(),
            "pkixPublicKey": t.proxy(renames["PkixPublicKeyIn"]).optional(),
            "comment": t.string().optional(),
        }
    ).named(renames["AttestorPublicKeyIn"])
    types["AttestorPublicKeyOut"] = t.struct(
        {
            "id": t.string().optional(),
            "asciiArmoredPgpPublicKey": t.string().optional(),
            "pkixPublicKey": t.proxy(renames["PkixPublicKeyOut"]).optional(),
            "comment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestorPublicKeyOut"])
    types["ValidateAttestationOccurrenceRequestIn"] = t.struct(
        {
            "occurrenceResourceUri": t.string(),
            "occurrenceNote": t.string(),
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]),
        }
    ).named(renames["ValidateAttestationOccurrenceRequestIn"])
    types["ValidateAttestationOccurrenceRequestOut"] = t.struct(
        {
            "occurrenceResourceUri": t.string(),
            "occurrenceNote": t.string(),
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateAttestationOccurrenceRequestOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["IamPolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["IamPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["IamPolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["IamPolicyIn"])
    types["IamPolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyOut"])
    types["AdmissionWhitelistPatternIn"] = t.struct(
        {"namePattern": t.string().optional()}
    ).named(renames["AdmissionWhitelistPatternIn"])
    types["AdmissionWhitelistPatternOut"] = t.struct(
        {
            "namePattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdmissionWhitelistPatternOut"])
    types["PkixPublicKeyIn"] = t.struct(
        {
            "publicKeyPem": t.string().optional(),
            "signatureAlgorithm": t.string().optional(),
        }
    ).named(renames["PkixPublicKeyIn"])
    types["PkixPublicKeyOut"] = t.struct(
        {
            "publicKeyPem": t.string().optional(),
            "signatureAlgorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PkixPublicKeyOut"])
    types["UserOwnedGrafeasNoteIn"] = t.struct(
        {
            "noteReference": t.string(),
            "publicKeys": t.array(t.proxy(renames["AttestorPublicKeyIn"])).optional(),
        }
    ).named(renames["UserOwnedGrafeasNoteIn"])
    types["UserOwnedGrafeasNoteOut"] = t.struct(
        {
            "noteReference": t.string(),
            "delegationServiceAccountEmail": t.string().optional(),
            "publicKeys": t.array(t.proxy(renames["AttestorPublicKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOwnedGrafeasNoteOut"])

    functions = {}
    functions["systempolicyGetPolicy"] = binaryauthorization.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetPolicy"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "admissionWhitelistPatterns": t.array(
                    t.proxy(renames["AdmissionWhitelistPatternIn"])
                ).optional(),
                "kubernetesServiceAccountAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "clusterAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "description": t.string().optional(),
                "istioServiceIdentityAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "globalPolicyEvaluationMode": t.string().optional(),
                "etag": t.string().optional(),
                "kubernetesNamespaceAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdatePolicy"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "admissionWhitelistPatterns": t.array(
                    t.proxy(renames["AdmissionWhitelistPatternIn"])
                ).optional(),
                "kubernetesServiceAccountAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "clusterAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "description": t.string().optional(),
                "istioServiceIdentityAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "globalPolicyEvaluationMode": t.string().optional(),
                "etag": t.string().optional(),
                "kubernetesNamespaceAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPolicyTestIamPermissions"] = binaryauthorization.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IamPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPolicySetIamPolicy"] = binaryauthorization.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IamPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPolicyGetIamPolicy"] = binaryauthorization.get(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "options.requestedPolicyVersion": t.integer().optional(),
                "resource": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IamPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsSetIamPolicy"] = binaryauthorization.get(
        "v1/{parent}/attestors",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttestorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsUpdate"] = binaryauthorization.get(
        "v1/{parent}/attestors",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttestorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsTestIamPermissions"] = binaryauthorization.get(
        "v1/{parent}/attestors",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttestorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsGetIamPolicy"] = binaryauthorization.get(
        "v1/{parent}/attestors",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttestorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsCreate"] = binaryauthorization.get(
        "v1/{parent}/attestors",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttestorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsGet"] = binaryauthorization.get(
        "v1/{parent}/attestors",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttestorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsAttestorsValidateAttestationOccurrence"
    ] = binaryauthorization.get(
        "v1/{parent}/attestors",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttestorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsDelete"] = binaryauthorization.get(
        "v1/{parent}/attestors",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttestorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsList"] = binaryauthorization.get(
        "v1/{parent}/attestors",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAttestorsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="binaryauthorization",
        renames=renames,
        types=types,
        functions=functions,
    )
