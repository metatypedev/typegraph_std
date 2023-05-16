from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_firebasestorage() -> Import:
    firebasestorage = HTTPRuntime("https://firebasestorage.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasestorage_1_ErrorResponse",
        "AddFirebaseRequestIn": "_firebasestorage_2_AddFirebaseRequestIn",
        "AddFirebaseRequestOut": "_firebasestorage_3_AddFirebaseRequestOut",
        "ListBucketsResponseIn": "_firebasestorage_4_ListBucketsResponseIn",
        "ListBucketsResponseOut": "_firebasestorage_5_ListBucketsResponseOut",
        "EmptyIn": "_firebasestorage_6_EmptyIn",
        "EmptyOut": "_firebasestorage_7_EmptyOut",
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn": "_firebasestorage_8_GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn",
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut": "_firebasestorage_9_GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut",
        "RemoveFirebaseRequestIn": "_firebasestorage_10_RemoveFirebaseRequestIn",
        "RemoveFirebaseRequestOut": "_firebasestorage_11_RemoveFirebaseRequestOut",
        "BucketIn": "_firebasestorage_12_BucketIn",
        "BucketOut": "_firebasestorage_13_BucketOut",
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn": "_firebasestorage_14_GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn",
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut": "_firebasestorage_15_GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut",
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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

    functions = {}
    functions["projectsBucketsRemoveFirebase"] = firebasestorage.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBucketsList"] = firebasestorage.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBucketsAddFirebase"] = firebasestorage.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsBucketsGet"] = firebasestorage.get(
        "v1beta/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="firebasestorage",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
