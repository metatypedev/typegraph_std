from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_licensing():
    licensing = HTTPRuntime("https://licensing.googleapis.com/")

    renames = {
        "ErrorResponse": "_licensing_1_ErrorResponse",
        "LicenseAssignmentListIn": "_licensing_2_LicenseAssignmentListIn",
        "LicenseAssignmentListOut": "_licensing_3_LicenseAssignmentListOut",
        "LicenseAssignmentIn": "_licensing_4_LicenseAssignmentIn",
        "LicenseAssignmentOut": "_licensing_5_LicenseAssignmentOut",
        "LicenseAssignmentInsertIn": "_licensing_6_LicenseAssignmentInsertIn",
        "LicenseAssignmentInsertOut": "_licensing_7_LicenseAssignmentInsertOut",
        "EmptyIn": "_licensing_8_EmptyIn",
        "EmptyOut": "_licensing_9_EmptyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LicenseAssignmentListIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["LicenseAssignmentIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["LicenseAssignmentListIn"])
    types["LicenseAssignmentListOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "etag": t.string().optional(),
            "items": t.array(t.proxy(renames["LicenseAssignmentOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LicenseAssignmentListOut"])
    types["LicenseAssignmentIn"] = t.struct(
        {
            "userId": t.string().optional(),
            "etags": t.string().optional(),
            "skuId": t.string().optional(),
            "selfLink": t.string().optional(),
            "productName": t.string().optional(),
            "skuName": t.string().optional(),
            "kind": t.string().optional(),
            "productId": t.string().optional(),
        }
    ).named(renames["LicenseAssignmentIn"])
    types["LicenseAssignmentOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "etags": t.string().optional(),
            "skuId": t.string().optional(),
            "selfLink": t.string().optional(),
            "productName": t.string().optional(),
            "skuName": t.string().optional(),
            "kind": t.string().optional(),
            "productId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LicenseAssignmentOut"])
    types["LicenseAssignmentInsertIn"] = t.struct(
        {"userId": t.string().optional()}
    ).named(renames["LicenseAssignmentInsertIn"])
    types["LicenseAssignmentInsertOut"] = t.struct(
        {
            "userId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LicenseAssignmentInsertOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])

    functions = {}
    functions["licenseAssignmentsDelete"] = licensing.get(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/users",
        t.struct(
            {
                "customerId": t.string().optional(),
                "skuId": t.string().optional(),
                "productId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsGet"] = licensing.get(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/users",
        t.struct(
            {
                "customerId": t.string().optional(),
                "skuId": t.string().optional(),
                "productId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsInsert"] = licensing.get(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/users",
        t.struct(
            {
                "customerId": t.string().optional(),
                "skuId": t.string().optional(),
                "productId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsUpdate"] = licensing.get(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/users",
        t.struct(
            {
                "customerId": t.string().optional(),
                "skuId": t.string().optional(),
                "productId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsListForProduct"] = licensing.get(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/users",
        t.struct(
            {
                "customerId": t.string().optional(),
                "skuId": t.string().optional(),
                "productId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsPatch"] = licensing.get(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/users",
        t.struct(
            {
                "customerId": t.string().optional(),
                "skuId": t.string().optional(),
                "productId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsListForProductAndSku"] = licensing.get(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/users",
        t.struct(
            {
                "customerId": t.string().optional(),
                "skuId": t.string().optional(),
                "productId": t.string().optional(),
                "pageToken": t.string().optional(),
                "maxResults": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentListOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="licensing",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
