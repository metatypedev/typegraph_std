from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_digitalassetlinks() -> Import:
    digitalassetlinks = HTTPRuntime("https://digitalassetlinks.googleapis.com/")

    renames = {
        "ErrorResponse": "_digitalassetlinks_1_ErrorResponse",
        "CertificateInfoIn": "_digitalassetlinks_2_CertificateInfoIn",
        "CertificateInfoOut": "_digitalassetlinks_3_CertificateInfoOut",
        "BulkCheckRequestIn": "_digitalassetlinks_4_BulkCheckRequestIn",
        "BulkCheckRequestOut": "_digitalassetlinks_5_BulkCheckRequestOut",
        "AssetIn": "_digitalassetlinks_6_AssetIn",
        "AssetOut": "_digitalassetlinks_7_AssetOut",
        "StatementIn": "_digitalassetlinks_8_StatementIn",
        "StatementOut": "_digitalassetlinks_9_StatementOut",
        "BulkCheckResponseIn": "_digitalassetlinks_10_BulkCheckResponseIn",
        "BulkCheckResponseOut": "_digitalassetlinks_11_BulkCheckResponseOut",
        "StatementTemplateIn": "_digitalassetlinks_12_StatementTemplateIn",
        "StatementTemplateOut": "_digitalassetlinks_13_StatementTemplateOut",
        "CheckResponseIn": "_digitalassetlinks_14_CheckResponseIn",
        "CheckResponseOut": "_digitalassetlinks_15_CheckResponseOut",
        "ListResponseIn": "_digitalassetlinks_16_ListResponseIn",
        "ListResponseOut": "_digitalassetlinks_17_ListResponseOut",
        "WebAssetIn": "_digitalassetlinks_18_WebAssetIn",
        "WebAssetOut": "_digitalassetlinks_19_WebAssetOut",
        "AndroidAppAssetIn": "_digitalassetlinks_20_AndroidAppAssetIn",
        "AndroidAppAssetOut": "_digitalassetlinks_21_AndroidAppAssetOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["CertificateInfoIn"] = t.struct(
        {"sha256Fingerprint": t.string().optional()}
    ).named(renames["CertificateInfoIn"])
    types["CertificateInfoOut"] = t.struct(
        {
            "sha256Fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateInfoOut"])
    types["BulkCheckRequestIn"] = t.struct(
        {
            "statements": t.array(t.proxy(renames["StatementTemplateIn"])).optional(),
            "defaultTarget": t.proxy(renames["AssetIn"]).optional(),
            "defaultSource": t.proxy(renames["AssetIn"]).optional(),
            "allowGoogleInternalDataSources": t.boolean().optional(),
            "defaultRelation": t.string().optional(),
            "skipCacheLookup": t.boolean().optional(),
        }
    ).named(renames["BulkCheckRequestIn"])
    types["BulkCheckRequestOut"] = t.struct(
        {
            "statements": t.array(t.proxy(renames["StatementTemplateOut"])).optional(),
            "defaultTarget": t.proxy(renames["AssetOut"]).optional(),
            "defaultSource": t.proxy(renames["AssetOut"]).optional(),
            "allowGoogleInternalDataSources": t.boolean().optional(),
            "defaultRelation": t.string().optional(),
            "skipCacheLookup": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkCheckRequestOut"])
    types["AssetIn"] = t.struct(
        {
            "web": t.proxy(renames["WebAssetIn"]).optional(),
            "androidApp": t.proxy(renames["AndroidAppAssetIn"]).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "web": t.proxy(renames["WebAssetOut"]).optional(),
            "androidApp": t.proxy(renames["AndroidAppAssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["StatementIn"] = t.struct(
        {
            "target": t.proxy(renames["AssetIn"]).optional(),
            "source": t.proxy(renames["AssetIn"]).optional(),
            "relation": t.string().optional(),
        }
    ).named(renames["StatementIn"])
    types["StatementOut"] = t.struct(
        {
            "target": t.proxy(renames["AssetOut"]).optional(),
            "source": t.proxy(renames["AssetOut"]).optional(),
            "relation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatementOut"])
    types["BulkCheckResponseIn"] = t.struct(
        {
            "bulkErrorCode": t.string().optional(),
            "checkResults": t.array(t.proxy(renames["CheckResponseIn"])).optional(),
        }
    ).named(renames["BulkCheckResponseIn"])
    types["BulkCheckResponseOut"] = t.struct(
        {
            "bulkErrorCode": t.string().optional(),
            "checkResults": t.array(t.proxy(renames["CheckResponseOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkCheckResponseOut"])
    types["StatementTemplateIn"] = t.struct(
        {
            "target": t.proxy(renames["AssetIn"]).optional(),
            "source": t.proxy(renames["AssetIn"]).optional(),
            "relation": t.string().optional(),
        }
    ).named(renames["StatementTemplateIn"])
    types["StatementTemplateOut"] = t.struct(
        {
            "target": t.proxy(renames["AssetOut"]).optional(),
            "source": t.proxy(renames["AssetOut"]).optional(),
            "relation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatementTemplateOut"])
    types["CheckResponseIn"] = t.struct(
        {
            "debugString": t.string().optional(),
            "maxAge": t.string().optional(),
            "linked": t.boolean().optional(),
            "errorCode": t.array(t.string()).optional(),
        }
    ).named(renames["CheckResponseIn"])
    types["CheckResponseOut"] = t.struct(
        {
            "debugString": t.string().optional(),
            "maxAge": t.string().optional(),
            "linked": t.boolean().optional(),
            "errorCode": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckResponseOut"])
    types["ListResponseIn"] = t.struct(
        {
            "maxAge": t.string().optional(),
            "errorCode": t.array(t.string()).optional(),
            "debugString": t.string().optional(),
            "statements": t.array(t.proxy(renames["StatementIn"])).optional(),
        }
    ).named(renames["ListResponseIn"])
    types["ListResponseOut"] = t.struct(
        {
            "maxAge": t.string().optional(),
            "errorCode": t.array(t.string()).optional(),
            "debugString": t.string().optional(),
            "statements": t.array(t.proxy(renames["StatementOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListResponseOut"])
    types["WebAssetIn"] = t.struct({"site": t.string().optional()}).named(
        renames["WebAssetIn"]
    )
    types["WebAssetOut"] = t.struct(
        {
            "site": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAssetOut"])
    types["AndroidAppAssetIn"] = t.struct(
        {
            "packageName": t.string().optional(),
            "certificate": t.proxy(renames["CertificateInfoIn"]).optional(),
        }
    ).named(renames["AndroidAppAssetIn"])
    types["AndroidAppAssetOut"] = t.struct(
        {
            "packageName": t.string().optional(),
            "certificate": t.proxy(renames["CertificateInfoOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AndroidAppAssetOut"])

    functions = {}
    functions["assetlinksBulkCheck"] = digitalassetlinks.get(
        "v1/assetlinks:check",
        t.struct(
            {
                "relation": t.string().optional(),
                "target.androidApp.packageName": t.string().optional(),
                "source.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "source.web.site": t.string().optional(),
                "target.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "source.androidApp.packageName": t.string().optional(),
                "target.web.site": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["assetlinksCheck"] = digitalassetlinks.get(
        "v1/assetlinks:check",
        t.struct(
            {
                "relation": t.string().optional(),
                "target.androidApp.packageName": t.string().optional(),
                "source.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "source.web.site": t.string().optional(),
                "target.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "source.androidApp.packageName": t.string().optional(),
                "target.web.site": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["statementsList"] = digitalassetlinks.get(
        "v1/statements:list",
        t.struct(
            {
                "source.androidApp.packageName": t.string().optional(),
                "source.web.site": t.string().optional(),
                "source.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "relation": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="digitalassetlinks",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
