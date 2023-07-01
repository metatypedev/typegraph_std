from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_checks():
    checks = HTTPRuntime("https://checks.googleapis.com/")

    renames = {
        "ErrorResponse": "_checks_1_ErrorResponse",
        "DateIn": "_checks_2_DateIn",
        "DateOut": "_checks_3_DateOut",
        "PolicyDataTypeAnnotationIn": "_checks_4_PolicyDataTypeAnnotationIn",
        "PolicyDataTypeAnnotationOut": "_checks_5_PolicyDataTypeAnnotationOut",
        "PolicyPurposeOfUseAnnotationIn": "_checks_6_PolicyPurposeOfUseAnnotationIn",
        "PolicyPurposeOfUseAnnotationOut": "_checks_7_PolicyPurposeOfUseAnnotationOut",
        "AnalyzePrivacyPolicyRequestIn": "_checks_8_AnalyzePrivacyPolicyRequestIn",
        "AnalyzePrivacyPolicyRequestOut": "_checks_9_AnalyzePrivacyPolicyRequestOut",
        "OperationIn": "_checks_10_OperationIn",
        "OperationOut": "_checks_11_OperationOut",
        "PolicySectionAnnotationIn": "_checks_12_PolicySectionAnnotationIn",
        "PolicySectionAnnotationOut": "_checks_13_PolicySectionAnnotationOut",
        "StatusIn": "_checks_14_StatusIn",
        "StatusOut": "_checks_15_StatusOut",
        "AnalyzePrivacyPolicyResponseIn": "_checks_16_AnalyzePrivacyPolicyResponseIn",
        "AnalyzePrivacyPolicyResponseOut": "_checks_17_AnalyzePrivacyPolicyResponseOut",
        "LastUpdatedDateIn": "_checks_18_LastUpdatedDateIn",
        "LastUpdatedDateOut": "_checks_19_LastUpdatedDateOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DateIn"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
        }
    ).named(renames["DateIn"])
    types["DateOut"] = t.struct(
        {
            "year": t.integer().optional(),
            "day": t.integer().optional(),
            "month": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DateOut"])
    types["PolicyDataTypeAnnotationIn"] = t.struct(
        {
            "startOffset": t.string().optional(),
            "score": t.number().optional(),
            "textContent": t.string().optional(),
            "dataType": t.string().optional(),
            "endOffset": t.string().optional(),
        }
    ).named(renames["PolicyDataTypeAnnotationIn"])
    types["PolicyDataTypeAnnotationOut"] = t.struct(
        {
            "startOffset": t.string().optional(),
            "score": t.number().optional(),
            "textContent": t.string().optional(),
            "dataType": t.string().optional(),
            "endOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyDataTypeAnnotationOut"])
    types["PolicyPurposeOfUseAnnotationIn"] = t.struct(
        {
            "startOffset": t.string().optional(),
            "score": t.number().optional(),
            "textContent": t.string().optional(),
            "endOffset": t.string().optional(),
            "purposeOfUse": t.string().optional(),
        }
    ).named(renames["PolicyPurposeOfUseAnnotationIn"])
    types["PolicyPurposeOfUseAnnotationOut"] = t.struct(
        {
            "startOffset": t.string().optional(),
            "score": t.number().optional(),
            "textContent": t.string().optional(),
            "endOffset": t.string().optional(),
            "purposeOfUse": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyPurposeOfUseAnnotationOut"])
    types["AnalyzePrivacyPolicyRequestIn"] = t.struct(
        {
            "privacyPolicyUri": t.string().optional(),
            "privacyPolicyPageContent": t.string().optional(),
        }
    ).named(renames["AnalyzePrivacyPolicyRequestIn"])
    types["AnalyzePrivacyPolicyRequestOut"] = t.struct(
        {
            "privacyPolicyUri": t.string().optional(),
            "privacyPolicyPageContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePrivacyPolicyRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["PolicySectionAnnotationIn"] = t.struct(
        {
            "sectionType": t.string().optional(),
            "score": t.number().optional(),
            "startOffset": t.string().optional(),
            "endOffset": t.string().optional(),
            "textContent": t.string().optional(),
        }
    ).named(renames["PolicySectionAnnotationIn"])
    types["PolicySectionAnnotationOut"] = t.struct(
        {
            "sectionType": t.string().optional(),
            "score": t.number().optional(),
            "startOffset": t.string().optional(),
            "endOffset": t.string().optional(),
            "textContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicySectionAnnotationOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AnalyzePrivacyPolicyResponseIn"] = t.struct(
        {
            "sectionAnnotations": t.array(
                t.proxy(renames["PolicySectionAnnotationIn"])
            ).optional(),
            "lastUpdatedDateInfo": t.proxy(renames["LastUpdatedDateIn"]).optional(),
            "dataTypeAnnotations": t.array(
                t.proxy(renames["PolicyDataTypeAnnotationIn"])
            ).optional(),
            "dataPurposeAnnotations": t.array(
                t.proxy(renames["PolicyPurposeOfUseAnnotationIn"])
            ).optional(),
            "htmlContent": t.string().optional(),
        }
    ).named(renames["AnalyzePrivacyPolicyResponseIn"])
    types["AnalyzePrivacyPolicyResponseOut"] = t.struct(
        {
            "sectionAnnotations": t.array(
                t.proxy(renames["PolicySectionAnnotationOut"])
            ).optional(),
            "lastUpdatedDateInfo": t.proxy(renames["LastUpdatedDateOut"]).optional(),
            "dataTypeAnnotations": t.array(
                t.proxy(renames["PolicyDataTypeAnnotationOut"])
            ).optional(),
            "dataPurposeAnnotations": t.array(
                t.proxy(renames["PolicyPurposeOfUseAnnotationOut"])
            ).optional(),
            "htmlContent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzePrivacyPolicyResponseOut"])
    types["LastUpdatedDateIn"] = t.struct(
        {
            "startOffset": t.string().optional(),
            "lastUpdatedDate": t.proxy(renames["DateIn"]).optional(),
            "textContent": t.string().optional(),
            "endOffset": t.string().optional(),
        }
    ).named(renames["LastUpdatedDateIn"])
    types["LastUpdatedDateOut"] = t.struct(
        {
            "startOffset": t.string().optional(),
            "lastUpdatedDate": t.proxy(renames["DateOut"]).optional(),
            "textContent": t.string().optional(),
            "endOffset": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LastUpdatedDateOut"])

    functions = {}
    functions["privacypolicyAnalyze"] = checks.post(
        "v1alpha/privacypolicy:analyze",
        t.struct(
            {
                "privacyPolicyUri": t.string().optional(),
                "privacyPolicyPageContent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["AnalyzePrivacyPolicyResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accountsAppsOperationsGet"] = checks.get(
        "v1alpha/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="checks", renames=renames, types=Box(types), functions=Box(functions)
    )
