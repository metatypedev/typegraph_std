from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_firebasestorage() -> Import:
    firebasestorage = HTTPRuntime("https://firebasestorage.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasestorage_1_ErrorResponse",
        "AddFirebaseRequestIn": "_firebasestorage_2_AddFirebaseRequestIn",
        "AddFirebaseRequestOut": "_firebasestorage_3_AddFirebaseRequestOut",
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn": "_firebasestorage_4_GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn",
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut": "_firebasestorage_5_GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut",
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn": "_firebasestorage_6_GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn",
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut": "_firebasestorage_7_GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut",
        "BucketIn": "_firebasestorage_8_BucketIn",
        "BucketOut": "_firebasestorage_9_BucketOut",
        "EmptyIn": "_firebasestorage_10_EmptyIn",
        "EmptyOut": "_firebasestorage_11_EmptyOut",
        "ListBucketsResponseIn": "_firebasestorage_12_ListBucketsResponseIn",
        "ListBucketsResponseOut": "_firebasestorage_13_ListBucketsResponseOut",
        "RemoveFirebaseRequestIn": "_firebasestorage_14_RemoveFirebaseRequestIn",
        "RemoveFirebaseRequestOut": "_firebasestorage_15_RemoveFirebaseRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AddFirebaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["AddFirebaseRequestIn"]
    )
    types["AddFirebaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AddFirebaseRequestOut"])
    types[
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn"
    ] = t.struct(
        {
            "lastUpdateTime": t.string().optional(),
            "createTime": t.string().optional(),
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
            "lastUpdateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut"
        ]
    )
    types[
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn"
    ] = t.struct(
        {
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "state": t.string().optional(),
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
            "createTime": t.string().optional(),
            "lastUpdateTime": t.string().optional(),
            "state": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut"
        ]
    )
    types["BucketIn"] = t.struct({"name": t.string().optional()}).named(
        renames["BucketIn"]
    )
    types["BucketOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ListBucketsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "buckets": t.array(t.proxy(renames["BucketIn"])).optional(),
        }
    ).named(renames["ListBucketsResponseIn"])
    types["ListBucketsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "buckets": t.array(t.proxy(renames["BucketOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListBucketsResponseOut"])
    types["RemoveFirebaseRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["RemoveFirebaseRequestIn"]
    )
    types["RemoveFirebaseRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["RemoveFirebaseRequestOut"])

    functions = {}
    functions["projectsBucketsGet"] = firebasestorage.post(
        "v1beta/{bucket}:removeFirebase",
        t.struct(
            {
                "bucket": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBucketsAddFirebase"] = firebasestorage.post(
        "v1beta/{bucket}:removeFirebase",
        t.struct(
            {
                "bucket": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBucketsList"] = firebasestorage.post(
        "v1beta/{bucket}:removeFirebase",
        t.struct(
            {
                "bucket": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBucketsRemoveFirebase"] = firebasestorage.post(
        "v1beta/{bucket}:removeFirebase",
        t.struct(
            {
                "bucket": t.string(),
                "_": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebasestorage",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
