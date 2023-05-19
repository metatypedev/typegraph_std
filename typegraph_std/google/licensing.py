from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_licensing() -> Import:
    licensing = HTTPRuntime("https://licensing.googleapis.com/")

    renames = {
        "ErrorResponse": "_licensing_1_ErrorResponse",
        "LicenseAssignmentListIn": "_licensing_2_LicenseAssignmentListIn",
        "LicenseAssignmentListOut": "_licensing_3_LicenseAssignmentListOut",
        "EmptyIn": "_licensing_4_EmptyIn",
        "EmptyOut": "_licensing_5_EmptyOut",
        "LicenseAssignmentIn": "_licensing_6_LicenseAssignmentIn",
        "LicenseAssignmentOut": "_licensing_7_LicenseAssignmentOut",
        "LicenseAssignmentInsertIn": "_licensing_8_LicenseAssignmentInsertIn",
        "LicenseAssignmentInsertOut": "_licensing_9_LicenseAssignmentInsertOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["LicenseAssignmentListIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["LicenseAssignmentIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["LicenseAssignmentListIn"])
    types["LicenseAssignmentListOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["LicenseAssignmentOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LicenseAssignmentListOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LicenseAssignmentIn"] = t.struct(
        {
            "productId": t.string().optional(),
            "skuName": t.string().optional(),
            "productName": t.string().optional(),
            "userId": t.string().optional(),
            "kind": t.string().optional(),
            "skuId": t.string().optional(),
            "selfLink": t.string().optional(),
            "etags": t.string().optional(),
        }
    ).named(renames["LicenseAssignmentIn"])
    types["LicenseAssignmentOut"] = t.struct(
        {
            "productId": t.string().optional(),
            "skuName": t.string().optional(),
            "productName": t.string().optional(),
            "userId": t.string().optional(),
            "kind": t.string().optional(),
            "skuId": t.string().optional(),
            "selfLink": t.string().optional(),
            "etags": t.string().optional(),
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

    functions = {}
    functions["licenseAssignmentsInsert"] = licensing.put(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "userId": t.string().optional(),
                "skuId": t.string().optional(),
                "skuName": t.string().optional(),
                "productName": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "etags": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsDelete"] = licensing.put(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "userId": t.string().optional(),
                "skuId": t.string().optional(),
                "skuName": t.string().optional(),
                "productName": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "etags": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsListForProductAndSku"] = licensing.put(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "userId": t.string().optional(),
                "skuId": t.string().optional(),
                "skuName": t.string().optional(),
                "productName": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "etags": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsListForProduct"] = licensing.put(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "userId": t.string().optional(),
                "skuId": t.string().optional(),
                "skuName": t.string().optional(),
                "productName": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "etags": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsPatch"] = licensing.put(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "userId": t.string().optional(),
                "skuId": t.string().optional(),
                "skuName": t.string().optional(),
                "productName": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "etags": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsGet"] = licensing.put(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "userId": t.string().optional(),
                "skuId": t.string().optional(),
                "skuName": t.string().optional(),
                "productName": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "etags": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["licenseAssignmentsUpdate"] = licensing.put(
        "apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId}",
        t.struct(
            {
                "productId": t.string().optional(),
                "userId": t.string().optional(),
                "skuId": t.string().optional(),
                "skuName": t.string().optional(),
                "productName": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "etags": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LicenseAssignmentOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="licensing",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
