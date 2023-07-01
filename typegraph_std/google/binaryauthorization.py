from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_binaryauthorization():
    binaryauthorization = HTTPRuntime("https://binaryauthorization.googleapis.com/")

    renames = {
        "ErrorResponse": "_binaryauthorization_1_ErrorResponse",
        "SetIamPolicyRequestIn": "_binaryauthorization_2_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_binaryauthorization_3_SetIamPolicyRequestOut",
        "JwtIn": "_binaryauthorization_4_JwtIn",
        "JwtOut": "_binaryauthorization_5_JwtOut",
        "SignatureIn": "_binaryauthorization_6_SignatureIn",
        "SignatureOut": "_binaryauthorization_7_SignatureOut",
        "AttestorPublicKeyIn": "_binaryauthorization_8_AttestorPublicKeyIn",
        "AttestorPublicKeyOut": "_binaryauthorization_9_AttestorPublicKeyOut",
        "EmptyIn": "_binaryauthorization_10_EmptyIn",
        "EmptyOut": "_binaryauthorization_11_EmptyOut",
        "BindingIn": "_binaryauthorization_12_BindingIn",
        "BindingOut": "_binaryauthorization_13_BindingOut",
        "PolicyIn": "_binaryauthorization_14_PolicyIn",
        "PolicyOut": "_binaryauthorization_15_PolicyOut",
        "TestIamPermissionsRequestIn": "_binaryauthorization_16_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_binaryauthorization_17_TestIamPermissionsRequestOut",
        "AttestationOccurrenceIn": "_binaryauthorization_18_AttestationOccurrenceIn",
        "AttestationOccurrenceOut": "_binaryauthorization_19_AttestationOccurrenceOut",
        "AdmissionWhitelistPatternIn": "_binaryauthorization_20_AdmissionWhitelistPatternIn",
        "AdmissionWhitelistPatternOut": "_binaryauthorization_21_AdmissionWhitelistPatternOut",
        "ExprIn": "_binaryauthorization_22_ExprIn",
        "ExprOut": "_binaryauthorization_23_ExprOut",
        "ValidateAttestationOccurrenceRequestIn": "_binaryauthorization_24_ValidateAttestationOccurrenceRequestIn",
        "ValidateAttestationOccurrenceRequestOut": "_binaryauthorization_25_ValidateAttestationOccurrenceRequestOut",
        "AdmissionRuleIn": "_binaryauthorization_26_AdmissionRuleIn",
        "AdmissionRuleOut": "_binaryauthorization_27_AdmissionRuleOut",
        "TestIamPermissionsResponseIn": "_binaryauthorization_28_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_binaryauthorization_29_TestIamPermissionsResponseOut",
        "AttestorIn": "_binaryauthorization_30_AttestorIn",
        "AttestorOut": "_binaryauthorization_31_AttestorOut",
        "PkixPublicKeyIn": "_binaryauthorization_32_PkixPublicKeyIn",
        "PkixPublicKeyOut": "_binaryauthorization_33_PkixPublicKeyOut",
        "ListAttestorsResponseIn": "_binaryauthorization_34_ListAttestorsResponseIn",
        "ListAttestorsResponseOut": "_binaryauthorization_35_ListAttestorsResponseOut",
        "UserOwnedGrafeasNoteIn": "_binaryauthorization_36_UserOwnedGrafeasNoteIn",
        "UserOwnedGrafeasNoteOut": "_binaryauthorization_37_UserOwnedGrafeasNoteOut",
        "ValidateAttestationOccurrenceResponseIn": "_binaryauthorization_38_ValidateAttestationOccurrenceResponseIn",
        "ValidateAttestationOccurrenceResponseOut": "_binaryauthorization_39_ValidateAttestationOccurrenceResponseOut",
        "IamPolicyIn": "_binaryauthorization_40_IamPolicyIn",
        "IamPolicyOut": "_binaryauthorization_41_IamPolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {"policy": t.proxy(renames["IamPolicyIn"]).optional()}
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["IamPolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["JwtIn"] = t.struct({"compactJwt": t.string().optional()}).named(
        renames["JwtIn"]
    )
    types["JwtOut"] = t.struct(
        {
            "compactJwt": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["JwtOut"])
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
    types["AttestorPublicKeyIn"] = t.struct(
        {
            "pkixPublicKey": t.proxy(renames["PkixPublicKeyIn"]).optional(),
            "id": t.string().optional(),
            "comment": t.string().optional(),
            "asciiArmoredPgpPublicKey": t.string().optional(),
        }
    ).named(renames["AttestorPublicKeyIn"])
    types["AttestorPublicKeyOut"] = t.struct(
        {
            "pkixPublicKey": t.proxy(renames["PkixPublicKeyOut"]).optional(),
            "id": t.string().optional(),
            "comment": t.string().optional(),
            "asciiArmoredPgpPublicKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestorPublicKeyOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["PolicyIn"] = t.struct(
        {
            "admissionWhitelistPatterns": t.array(
                t.proxy(renames["AdmissionWhitelistPatternIn"])
            ).optional(),
            "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
            "istioServiceIdentityAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "globalPolicyEvaluationMode": t.string().optional(),
            "description": t.string().optional(),
            "kubernetesNamespaceAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "etag": t.string().optional(),
            "clusterAdmissionRules": t.struct({"_": t.string().optional()}).optional(),
            "kubernetesServiceAccountAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "admissionWhitelistPatterns": t.array(
                t.proxy(renames["AdmissionWhitelistPatternOut"])
            ).optional(),
            "defaultAdmissionRule": t.proxy(renames["AdmissionRuleOut"]),
            "istioServiceIdentityAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "globalPolicyEvaluationMode": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "kubernetesNamespaceAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "etag": t.string().optional(),
            "clusterAdmissionRules": t.struct({"_": t.string().optional()}).optional(),
            "kubernetesServiceAccountAdmissionRules": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["AttestationOccurrenceIn"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["SignatureIn"])).optional(),
            "jwts": t.array(t.proxy(renames["JwtIn"])).optional(),
            "serializedPayload": t.string(),
        }
    ).named(renames["AttestationOccurrenceIn"])
    types["AttestationOccurrenceOut"] = t.struct(
        {
            "signatures": t.array(t.proxy(renames["SignatureOut"])).optional(),
            "jwts": t.array(t.proxy(renames["JwtOut"])).optional(),
            "serializedPayload": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestationOccurrenceOut"])
    types["AdmissionWhitelistPatternIn"] = t.struct(
        {"namePattern": t.string().optional()}
    ).named(renames["AdmissionWhitelistPatternIn"])
    types["AdmissionWhitelistPatternOut"] = t.struct(
        {
            "namePattern": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AdmissionWhitelistPatternOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["AttestorIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "userOwnedGrafeasNote": t.proxy(
                renames["UserOwnedGrafeasNoteIn"]
            ).optional(),
            "name": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["AttestorIn"])
    types["AttestorOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "userOwnedGrafeasNote": t.proxy(
                renames["UserOwnedGrafeasNoteOut"]
            ).optional(),
            "updateTime": t.string().optional(),
            "name": t.string(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttestorOut"])
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
    types["UserOwnedGrafeasNoteIn"] = t.struct(
        {
            "noteReference": t.string(),
            "publicKeys": t.array(t.proxy(renames["AttestorPublicKeyIn"])).optional(),
        }
    ).named(renames["UserOwnedGrafeasNoteIn"])
    types["UserOwnedGrafeasNoteOut"] = t.struct(
        {
            "delegationServiceAccountEmail": t.string().optional(),
            "noteReference": t.string(),
            "publicKeys": t.array(t.proxy(renames["AttestorPublicKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["UserOwnedGrafeasNoteOut"])
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

    functions = {}
    functions["projectsGetPolicy"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "admissionWhitelistPatterns": t.array(
                    t.proxy(renames["AdmissionWhitelistPatternIn"])
                ).optional(),
                "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
                "istioServiceIdentityAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "globalPolicyEvaluationMode": t.string().optional(),
                "description": t.string().optional(),
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
                "defaultAdmissionRule": t.proxy(renames["AdmissionRuleIn"]),
                "istioServiceIdentityAdmissionRules": t.struct(
                    {"_": t.string().optional()}
                ).optional(),
                "globalPolicyEvaluationMode": t.string().optional(),
                "description": t.string().optional(),
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
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsAttestorsCreate"] = binaryauthorization.put(
        "v1/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
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
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
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
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
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
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
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
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
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
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
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
                "etag": t.string().optional(),
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
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
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
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
                "userOwnedGrafeasNote": t.proxy(
                    renames["UserOwnedGrafeasNoteIn"]
                ).optional(),
                "description": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AttestorOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPolicyGetIamPolicy"] = binaryauthorization.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["IamPolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IamPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPolicyTestIamPermissions"] = binaryauthorization.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["IamPolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IamPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPolicySetIamPolicy"] = binaryauthorization.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["IamPolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["IamPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["systempolicyGetPolicy"] = binaryauthorization.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="binaryauthorization",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
