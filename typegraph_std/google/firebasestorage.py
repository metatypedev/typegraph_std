from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_firebasestorage():
    firebasestorage = HTTPRuntime("https://firebasestorage.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasestorage_1_ErrorResponse",
        "EmptyIn": "_firebasestorage_2_EmptyIn",
        "EmptyOut": "_firebasestorage_3_EmptyOut",
        "ListBucketsResponseIn": "_firebasestorage_4_ListBucketsResponseIn",
        "ListBucketsResponseOut": "_firebasestorage_5_ListBucketsResponseOut",
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn": "_firebasestorage_6_GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn",
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut": "_firebasestorage_7_GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut",
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn": "_firebasestorage_8_GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn",
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut": "_firebasestorage_9_GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut",
        "RemoveFirebaseRequestIn": "_firebasestorage_10_RemoveFirebaseRequestIn",
        "RemoveFirebaseRequestOut": "_firebasestorage_11_RemoveFirebaseRequestOut",
        "BucketIn": "_firebasestorage_12_BucketIn",
        "BucketOut": "_firebasestorage_13_BucketOut",
        "AddFirebaseRequestIn": "_firebasestorage_14_AddFirebaseRequestIn",
        "AddFirebaseRequestOut": "_firebasestorage_15_AddFirebaseRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListBucketsResponseIn"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["BucketIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListBucketsResponseIn"])
    types["ListBucketsResponseOut"] = t.struct(
        {
            "buckets": t.array(t.proxy(renames["BucketOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBucketsResponseOut"])
    types[
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn"
    ] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn"
        ]
    )
    types[
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut"
    ] = t.struct(
        {
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut"
        ]
    )
    types[
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "state": t.string().optional(),
        }
    ).named(
        renames[
            "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn"
        ]
    )
    types[
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut"
        ]
    )
    types["RemoveFirebaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveFirebaseRequestIn"]
    )
    types["RemoveFirebaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveFirebaseRequestOut"])
    types["BucketIn"] = t.struct({"name": t.string().optional()}).named(
        renames["BucketIn"]
    )
    types["BucketOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOut"])
    types["AddFirebaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddFirebaseRequestIn"]
    )
    types["AddFirebaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddFirebaseRequestOut"])

    functions = {}
    functions["projectsBucketsAddFirebase"] = firebasestorage.get(
        "v1beta/{parent}/buckets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBucketsRemoveFirebase"] = firebasestorage.get(
        "v1beta/{parent}/buckets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBucketsGet"] = firebasestorage.get(
        "v1beta/{parent}/buckets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBucketsList"] = firebasestorage.get(
        "v1beta/{parent}/buckets",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListBucketsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebasestorage",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
