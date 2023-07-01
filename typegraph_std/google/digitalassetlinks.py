from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_digitalassetlinks():
    digitalassetlinks = HTTPRuntime("https://digitalassetlinks.googleapis.com/")

    renames = {
        "ErrorResponse": "_digitalassetlinks_1_ErrorResponse",
        "BulkCheckRequestIn": "_digitalassetlinks_2_BulkCheckRequestIn",
        "BulkCheckRequestOut": "_digitalassetlinks_3_BulkCheckRequestOut",
        "AndroidAppAssetIn": "_digitalassetlinks_4_AndroidAppAssetIn",
        "AndroidAppAssetOut": "_digitalassetlinks_5_AndroidAppAssetOut",
        "CertificateInfoIn": "_digitalassetlinks_6_CertificateInfoIn",
        "CertificateInfoOut": "_digitalassetlinks_7_CertificateInfoOut",
        "CheckResponseIn": "_digitalassetlinks_8_CheckResponseIn",
        "CheckResponseOut": "_digitalassetlinks_9_CheckResponseOut",
        "ListResponseIn": "_digitalassetlinks_10_ListResponseIn",
        "ListResponseOut": "_digitalassetlinks_11_ListResponseOut",
        "StatementIn": "_digitalassetlinks_12_StatementIn",
        "StatementOut": "_digitalassetlinks_13_StatementOut",
        "BulkCheckResponseIn": "_digitalassetlinks_14_BulkCheckResponseIn",
        "BulkCheckResponseOut": "_digitalassetlinks_15_BulkCheckResponseOut",
        "AssetIn": "_digitalassetlinks_16_AssetIn",
        "AssetOut": "_digitalassetlinks_17_AssetOut",
        "WebAssetIn": "_digitalassetlinks_18_WebAssetIn",
        "WebAssetOut": "_digitalassetlinks_19_WebAssetOut",
        "StatementTemplateIn": "_digitalassetlinks_20_StatementTemplateIn",
        "StatementTemplateOut": "_digitalassetlinks_21_StatementTemplateOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BulkCheckRequestIn"] = t.struct(
        {
            "statements": t.array(t.proxy(renames["StatementTemplateIn"])).optional(),
            "defaultSource": t.proxy(renames["AssetIn"]).optional(),
            "allowGoogleInternalDataSources": t.boolean().optional(),
            "defaultRelation": t.string().optional(),
            "defaultTarget": t.proxy(renames["AssetIn"]).optional(),
            "skipCacheLookup": t.boolean().optional(),
        }
    ).named(renames["BulkCheckRequestIn"])
    types["BulkCheckRequestOut"] = t.struct(
        {
            "statements": t.array(t.proxy(renames["StatementTemplateOut"])).optional(),
            "defaultSource": t.proxy(renames["AssetOut"]).optional(),
            "allowGoogleInternalDataSources": t.boolean().optional(),
            "defaultRelation": t.string().optional(),
            "defaultTarget": t.proxy(renames["AssetOut"]).optional(),
            "skipCacheLookup": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BulkCheckRequestOut"])
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
    types["CertificateInfoIn"] = t.struct(
        {"sha256Fingerprint": t.string().optional()}
    ).named(renames["CertificateInfoIn"])
    types["CertificateInfoOut"] = t.struct(
        {
            "sha256Fingerprint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CertificateInfoOut"])
    types["CheckResponseIn"] = t.struct(
        {
            "errorCode": t.array(t.string()).optional(),
            "linked": t.boolean().optional(),
            "debugString": t.string().optional(),
            "maxAge": t.string().optional(),
        }
    ).named(renames["CheckResponseIn"])
    types["CheckResponseOut"] = t.struct(
        {
            "errorCode": t.array(t.string()).optional(),
            "linked": t.boolean().optional(),
            "debugString": t.string().optional(),
            "maxAge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckResponseOut"])
    types["ListResponseIn"] = t.struct(
        {
            "maxAge": t.string().optional(),
            "statements": t.array(t.proxy(renames["StatementIn"])).optional(),
            "errorCode": t.array(t.string()).optional(),
            "debugString": t.string().optional(),
        }
    ).named(renames["ListResponseIn"])
    types["ListResponseOut"] = t.struct(
        {
            "maxAge": t.string().optional(),
            "statements": t.array(t.proxy(renames["StatementOut"])).optional(),
            "errorCode": t.array(t.string()).optional(),
            "debugString": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListResponseOut"])
    types["StatementIn"] = t.struct(
        {
            "source": t.proxy(renames["AssetIn"]).optional(),
            "relation": t.string().optional(),
            "target": t.proxy(renames["AssetIn"]).optional(),
        }
    ).named(renames["StatementIn"])
    types["StatementOut"] = t.struct(
        {
            "source": t.proxy(renames["AssetOut"]).optional(),
            "relation": t.string().optional(),
            "target": t.proxy(renames["AssetOut"]).optional(),
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
    types["AssetIn"] = t.struct(
        {
            "androidApp": t.proxy(renames["AndroidAppAssetIn"]).optional(),
            "web": t.proxy(renames["WebAssetIn"]).optional(),
        }
    ).named(renames["AssetIn"])
    types["AssetOut"] = t.struct(
        {
            "androidApp": t.proxy(renames["AndroidAppAssetOut"]).optional(),
            "web": t.proxy(renames["WebAssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AssetOut"])
    types["WebAssetIn"] = t.struct({"site": t.string().optional()}).named(
        renames["WebAssetIn"]
    )
    types["WebAssetOut"] = t.struct(
        {
            "site": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["WebAssetOut"])
    types["StatementTemplateIn"] = t.struct(
        {
            "target": t.proxy(renames["AssetIn"]).optional(),
            "relation": t.string().optional(),
            "source": t.proxy(renames["AssetIn"]).optional(),
        }
    ).named(renames["StatementTemplateIn"])
    types["StatementTemplateOut"] = t.struct(
        {
            "target": t.proxy(renames["AssetOut"]).optional(),
            "relation": t.string().optional(),
            "source": t.proxy(renames["AssetOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatementTemplateOut"])

    functions = {}
    functions["statementsList"] = digitalassetlinks.get(
        "v1/statements:list",
        t.struct(
            {
                "source.web.site": t.string().optional(),
                "relation": t.string().optional(),
                "source.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "source.androidApp.packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["assetlinksBulkCheck"] = digitalassetlinks.get(
        "v1/assetlinks:check",
        t.struct(
            {
                "relation": t.string().optional(),
                "target.web.site": t.string().optional(),
                "source.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "source.web.site": t.string().optional(),
                "target.androidApp.packageName": t.string().optional(),
                "target.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "source.androidApp.packageName": t.string().optional(),
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
                "target.web.site": t.string().optional(),
                "source.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "source.web.site": t.string().optional(),
                "target.androidApp.packageName": t.string().optional(),
                "target.androidApp.certificate.sha256Fingerprint": t.string().optional(),
                "source.androidApp.packageName": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="digitalassetlinks",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
