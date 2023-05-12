from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_binaryauthorization() -> Import:
    binaryauthorization = HTTPRuntime("https://binaryauthorization.googleapis.com/")

    renames = {
        "ErrorResponse": "_binaryauthorization_1_ErrorResponse",
        "JwtIn": "_binaryauthorization_2_JwtIn",
        "JwtOut": "_binaryauthorization_3_JwtOut",
        "ListAttestorsResponseIn": "_binaryauthorization_4_ListAttestorsResponseIn",
        "ListAttestorsResponseOut": "_binaryauthorization_5_ListAttestorsResponseOut",
        "PkixPublicKeyIn": "_binaryauthorization_6_PkixPublicKeyIn",
        "PkixPublicKeyOut": "_binaryauthorization_7_PkixPublicKeyOut",
        "BindingIn": "_binaryauthorization_8_BindingIn",
        "BindingOut": "_binaryauthorization_9_BindingOut",
        "TestIamPermissionsResponseIn": "_binaryauthorization_10_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_binaryauthorization_11_TestIamPermissionsResponseOut",
        "PolicyIn": "_binaryauthorization_12_PolicyIn",
        "PolicyOut": "_binaryauthorization_13_PolicyOut",
        "EmptyIn": "_binaryauthorization_14_EmptyIn",
        "EmptyOut": "_binaryauthorization_15_EmptyOut",
        "IamPolicyIn": "_binaryauthorization_16_IamPolicyIn",
        "IamPolicyOut": "_binaryauthorization_17_IamPolicyOut",
        "TestIamPermissionsRequestIn": "_binaryauthorization_18_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_binaryauthorization_19_TestIamPermissionsRequestOut",
        "SetIamPolicyRequestIn": "_binaryauthorization_20_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_binaryauthorization_21_SetIamPolicyRequestOut",
        "UserOwnedGrafeasNoteIn": "_binaryauthorization_22_UserOwnedGrafeasNoteIn",
        "UserOwnedGrafeasNoteOut": "_binaryauthorization_23_UserOwnedGrafeasNoteOut",
        "ExprIn": "_binaryauthorization_24_ExprIn",
        "ExprOut": "_binaryauthorization_25_ExprOut",
        "ValidateAttestationOccurrenceResponseIn": "_binaryauthorization_26_ValidateAttestationOccurrenceResponseIn",
        "ValidateAttestationOccurrenceResponseOut": "_binaryauthorization_27_ValidateAttestationOccurrenceResponseOut",
        "AdmissionWhitelistPatternIn": "_binaryauthorization_28_AdmissionWhitelistPatternIn",
        "AdmissionWhitelistPatternOut": "_binaryauthorization_29_AdmissionWhitelistPatternOut",
        "AdmissionRuleIn": "_binaryauthorization_30_AdmissionRuleIn",
        "AdmissionRuleOut": "_binaryauthorization_31_AdmissionRuleOut",
        "ValidateAttestationOccurrenceRequestIn": "_binaryauthorization_32_ValidateAttestationOccurrenceRequestIn",
        "ValidateAttestationOccurrenceRequestOut": "_binaryauthorization_33_ValidateAttestationOccurrenceRequestOut",
        "AttestorIn": "_binaryauthorization_34_AttestorIn",
        "AttestorOut": "_binaryauthorization_35_AttestorOut",
        "SignatureIn": "_binaryauthorization_36_SignatureIn",
        "SignatureOut": "_binaryauthorization_37_SignatureOut",
        "AttestationOccurrenceIn": "_binaryauthorization_38_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_binaryauthorization_39_AttestationOccurrenceOut",
        "AttestorPublicKeyIn": "_binaryauthorization_40_AttestorPublicKeyIn",
        "AttestorPublicKeyOut": "_binaryauthorization_41_AttestorPublicKeyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
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
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["PolicyIn"] = t.struct(
        {
            "kubernetesServiceAccountAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "clusterAdmissionRules": t.struct({"_": t.string().optional()}).optional(),
            "globalPolicyEvaluationMode": t.string().optional(),
            "description": t.string().optional(),
            "admissionWhitelistPatterns": t.array(
                t.proxy(renames["AdmissionWhitelistPatternIn"])
            ).optional(),
            "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
            "istioServiceIdentityAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "etag": t.string().optional(),
            "kubernetesNamespaceAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "kubernetesServiceAccountAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "clusterAdmissionRules": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "globalPolicyEvaluationMode": t.string().optional(),
            "description": t.string().optional(),
            "admissionWhitelistPatterns": t.array(
                t.proxy(renames["AdmissionWhitelistPatternOut"])
            ).optional(),
            "defaultAdmissionRule": t.proxy(renames["AdmissionRuleOut"]),
            "updateTime": t.string().optional(),
            "istioServiceIdentityAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "etag": t.string().optional(),
            "kubernetesNamespaceAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["IamPolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["IamPolicyIn"])
    types["IamPolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IamPolicyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["IamPolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["IamPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["UserOwnedGrafeasNoteIn"] = t.struct(
        {
            "publicKeys": t.array(t.proxy(renames["AttestorPublicKeyIn"])).optional(),
            "noteReference": t.string(),
        }
    ).named(renames["UserOwnedGrafeasNoteIn"])
    types["UserOwnedGrafeasNoteOut"] = t.struct(
        {
            "delegationServiceAccountEmail": t.string().optional(),
            "publicKeys": t.array(t.proxy(renames["AttestorPublicKeyOut"])).optional(),
            "noteReference": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOwnedGrafeasNoteOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["AdmissionWhitelistPatternIn"] = t.struct(
        {"namePattern": t.string().optional()}
    ).named(renames["AdmissionWhitelistPatternIn"])
    types["AdmissionWhitelistPatternOut"] = t.struct(
        {
            "namePattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdmissionWhitelistPatternOut"])
    types["AdmissionRuleIn"] = t.struct(
        {
            "requireAttestationsBy": t.array(t.string()).optional(),
            "evaluationMode": t.string(),
            "enforcementMode": t.string(),
        }
    ).named(renames["AdmissionRuleIn"])
    types["AdmissionRuleOut"] = t.struct(
        {
            "requireAttestationsBy": t.array(t.string()).optional(),
            "evaluationMode": t.string(),
            "enforcementMode": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdmissionRuleOut"])
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
    types["AttestorIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "userOwnedGrafeasNote": t.proxy(
                renames["UserOwnedGrafeasNoteIn"]
            ).optional(),
        }
    ).named(renames["AttestorIn"])
    types["AttestorOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "userOwnedGrafeasNote": t.proxy(
                renames["UserOwnedGrafeasNoteOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestorOut"])
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
    types["AttestationOccurrenceIn"] = t.struct(
        {
            "serializedPayload": t.string(),
            "signatures": t.array(t.proxy(renames["SignatureIn"])).optional(),
            "jwts": t.array(t.proxy(renames["JwtIn"])).optional(),
        }
    ).named(renames["AttestationOccurrenceIn"])
    types["AttestationOccurrenceOut"] = t.struct(
        {
            "serializedPayload": t.string(),
            "signatures": t.array(t.proxy(renames["SignatureOut"])).optional(),
            "jwts": t.array(t.proxy(renames["JwtOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationOccurrenceOut"])
    types["AttestorPublicKeyIn"] = t.struct(
        {
            "asciiArmoredPgpPublicKey": t.string().optional(),
            "id": t.string().optional(),
            "comment": t.string().optional(),
            "pkixPublicKey": t.proxy(renames["PkixPublicKeyIn"]).optional(),
        }
    ).named(renames["AttestorPublicKeyIn"])
    types["AttestorPublicKeyOut"] = t.struct(
        {
            "asciiArmoredPgpPublicKey": t.string().optional(),
            "id": t.string().optional(),
            "comment": t.string().optional(),
            "pkixPublicKey": t.proxy(renames["PkixPublicKeyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestorPublicKeyOut"])

    functions = {}
    functions["systempolicyGetPolicy"] = binaryauthorization.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUpdatePolicy"] = binaryauthorization.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetPolicy"] = binaryauthorization.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
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
    functions["projectsAttestorsTestIamPermissions"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
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
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
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
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
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
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
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
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
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
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
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
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
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
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
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
                "etag": t.string().optional(),
                "description": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
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
