from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_binaryauthorization() -> Import:
    binaryauthorization = HTTPRuntime("https://binaryauthorization.googleapis.com/")

    renames = {
        "ErrorResponse": "_binaryauthorization_1_ErrorResponse",
        "SignatureIn": "_binaryauthorization_2_SignatureIn",
        "SignatureOut": "_binaryauthorization_3_SignatureOut",
        "AttestorIn": "_binaryauthorization_4_AttestorIn",
        "AttestorOut": "_binaryauthorization_5_AttestorOut",
        "PolicyIn": "_binaryauthorization_6_PolicyIn",
        "PolicyOut": "_binaryauthorization_7_PolicyOut",
        "ListAttestorsResponseIn": "_binaryauthorization_8_ListAttestorsResponseIn",
        "ListAttestorsResponseOut": "_binaryauthorization_9_ListAttestorsResponseOut",
        "SetIamPolicyRequestIn": "_binaryauthorization_10_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_binaryauthorization_11_SetIamPolicyRequestOut",
        "ValidateAttestationOccurrenceRequestIn": "_binaryauthorization_12_ValidateAttestationOccurrenceRequestIn",
        "ValidateAttestationOccurrenceRequestOut": "_binaryauthorization_13_ValidateAttestationOccurrenceRequestOut",
        "TestIamPermissionsResponseIn": "_binaryauthorization_14_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_binaryauthorization_15_TestIamPermissionsResponseOut",
        "UserOwnedGrafeasNoteIn": "_binaryauthorization_16_UserOwnedGrafeasNoteIn",
        "UserOwnedGrafeasNoteOut": "_binaryauthorization_17_UserOwnedGrafeasNoteOut",
        "ValidateAttestationOccurrenceResponseIn": "_binaryauthorization_18_ValidateAttestationOccurrenceResponseIn",
        "ValidateAttestationOccurrenceResponseOut": "_binaryauthorization_19_ValidateAttestationOccurrenceResponseOut",
        "EmptyIn": "_binaryauthorization_20_EmptyIn",
        "EmptyOut": "_binaryauthorization_21_EmptyOut",
        "TestIamPermissionsRequestIn": "_binaryauthorization_22_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_binaryauthorization_23_TestIamPermissionsRequestOut",
        "AdmissionRuleIn": "_binaryauthorization_24_AdmissionRuleIn",
        "AdmissionRuleOut": "_binaryauthorization_25_AdmissionRuleOut",
        "ExprIn": "_binaryauthorization_26_ExprIn",
        "ExprOut": "_binaryauthorization_27_ExprOut",
        "IamPolicyIn": "_binaryauthorization_28_IamPolicyIn",
        "IamPolicyOut": "_binaryauthorization_29_IamPolicyOut",
        "AdmissionWhitelistPatternIn": "_binaryauthorization_30_AdmissionWhitelistPatternIn",
        "AdmissionWhitelistPatternOut": "_binaryauthorization_31_AdmissionWhitelistPatternOut",
        "JwtIn": "_binaryauthorization_32_JwtIn",
        "JwtOut": "_binaryauthorization_33_JwtOut",
        "PkixPublicKeyIn": "_binaryauthorization_34_PkixPublicKeyIn",
        "PkixPublicKeyOut": "_binaryauthorization_35_PkixPublicKeyOut",
        "AttestorPublicKeyIn": "_binaryauthorization_36_AttestorPublicKeyIn",
        "AttestorPublicKeyOut": "_binaryauthorization_37_AttestorPublicKeyOut",
        "BindingIn": "_binaryauthorization_38_BindingIn",
        "BindingOut": "_binaryauthorization_39_BindingOut",
        "AttestationOccurrenceIn": "_binaryauthorization_40_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_binaryauthorization_41_AttestationOccurrenceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["AttestorIn"] = t.struct(
        {
            "name": t.string(),
            "userOwnedGrafeasNote": t.proxy(
                renames["UserOwnedGrafeasNoteIn"]
            ).optional(),
            "description": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["AttestorIn"])
    types["AttestorOut"] = t.struct(
        {
            "name": t.string(),
            "userOwnedGrafeasNote": t.proxy(
                renames["UserOwnedGrafeasNoteOut"]
            ).optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestorOut"])
    types["PolicyIn"] = t.struct(
        {
            "istioServiceIdentityAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "admissionWhitelistPatterns": t.array(
                t.proxy(renames["AdmissionWhitelistPatternIn"])
            ).optional(),
            "kubernetesNamespaceAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "etag": t.string().optional(),
            "clusterAdmissionRules": t.struct({"_": t.string().optional()}).optional(),
            "kubernetesServiceAccountAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
            "globalPolicyEvaluationMode": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "istioServiceIdentityAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "admissionWhitelistPatterns": t.array(
                t.proxy(renames["AdmissionWhitelistPatternOut"])
            ).optional(),
            "updateTime": t.string().optional(),
            "kubernetesNamespaceAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "etag": t.string().optional(),
            "clusterAdmissionRules": t.struct({"_": t.string().optional()}).optional(),
            "kubernetesServiceAccountAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "defaultAdmissionRule": t.proxy(renames["AdmissionRuleOut"]),
            "globalPolicyEvaluationMode": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["IamPolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["IamPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["ValidateAttestationOccurrenceRequestIn"] = t.struct(
        {
            "occurrenceNote": t.string(),
            "occurrenceResourceUri": t.string(),
            "attestation": t.proxy(renames["AttestationOccurrenceIn"]),
        }
    ).named(renames["ValidateAttestationOccurrenceRequestIn"])
    types["ValidateAttestationOccurrenceRequestOut"] = t.struct(
        {
            "occurrenceNote": t.string(),
            "occurrenceResourceUri": t.string(),
            "attestation": t.proxy(renames["AttestationOccurrenceOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateAttestationOccurrenceRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["ValidateAttestationOccurrenceResponseIn"] = t.struct(
        {"denialReason": t.string().optional(), "result": t.string().optional()}
    ).named(renames["ValidateAttestationOccurrenceResponseIn"])
    types["ValidateAttestationOccurrenceResponseOut"] = t.struct(
        {
            "denialReason": t.string().optional(),
            "result": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ValidateAttestationOccurrenceResponseOut"])
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
    types["AdmissionRuleIn"] = t.struct(
        {
            "requireAttestationsBy": t.array(t.string()).optional(),
            "enforcementMode": t.string(),
            "evaluationMode": t.string(),
        }
    ).named(renames["AdmissionRuleIn"])
    types["AdmissionRuleOut"] = t.struct(
        {
            "requireAttestationsBy": t.array(t.string()).optional(),
            "enforcementMode": t.string(),
            "evaluationMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdmissionRuleOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
    types["PkixPublicKeyIn"] = t.struct(
        {
            "signatureAlgorithm": t.string().optional(),
            "publicKeyPem": t.string().optional(),
        }
    ).named(renames["PkixPublicKeyIn"])
    types["PkixPublicKeyOut"] = t.struct(
        {
            "signatureAlgorithm": t.string().optional(),
            "publicKeyPem": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PkixPublicKeyOut"])
    types["AttestorPublicKeyIn"] = t.struct(
        {
            "pkixPublicKey": t.proxy(renames["PkixPublicKeyIn"]).optional(),
            "id": t.string().optional(),
            "asciiArmoredPgpPublicKey": t.string().optional(),
            "comment": t.string().optional(),
        }
    ).named(renames["AttestorPublicKeyIn"])
    types["AttestorPublicKeyOut"] = t.struct(
        {
            "pkixPublicKey": t.proxy(renames["PkixPublicKeyOut"]).optional(),
            "id": t.string().optional(),
            "asciiArmoredPgpPublicKey": t.string().optional(),
            "comment": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestorPublicKeyOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["AttestationOccurrenceIn"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["SignatureIn"])).optional(),
            "serializedPayload": t.string(),
            "jwts": t.array(t.proxy(renames["JwtIn"])).optional(),
        }
    ).named(renames["AttestationOccurrenceIn"])
    types["AttestationOccurrenceOut"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["SignatureOut"])).optional(),
            "serializedPayload": t.string(),
            "jwts": t.array(t.proxy(renames["JwtOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationOccurrenceOut"])

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
                "istioServiceIdentityAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "admissionWhitelistPatterns": t.array(
                    t.proxy(renames["AdmissionWhitelistPatternIn"])
                ).optional(),
                "kubernetesNamespaceAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "clusterAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "kubernetesServiceAccountAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
                "globalPolicyEvaluationMode": t.string().optional(),
                "description": t.string().optional(),
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
                "istioServiceIdentityAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "admissionWhitelistPatterns": t.array(
                    t.proxy(renames["AdmissionWhitelistPatternIn"])
                ).optional(),
                "kubernetesNamespaceAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "clusterAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "kubernetesServiceAccountAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
                "globalPolicyEvaluationMode": t.string().optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPolicyGetIamPolicy"] = binaryauthorization.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPolicySetIamPolicy"] = binaryauthorization.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPolicyTestIamPermissions"] = binaryauthorization.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsAttestorsValidateAttestationOccurrence"
    ] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsDelete"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsGet"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsCreate"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsSetIamPolicy"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsList"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsGetIamPolicy"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsTestIamPermissions"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsUpdate"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="binaryauthorization",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
