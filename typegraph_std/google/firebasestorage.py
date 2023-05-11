from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_firebasestorage() -> Import:
    firebasestorage = HTTPRuntime("https://firebasestorage.googleapis.com/")

    renames = {
        "ErrorResponse": "_firebasestorage_1_ErrorResponse",
        "EmptyIn": "_firebasestorage_2_EmptyIn",
        "EmptyOut": "_firebasestorage_3_EmptyOut",
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn": "_firebasestorage_4_GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn",
        "GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut": "_firebasestorage_5_GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut",
        "RemoveFirebaseRequestIn": "_firebasestorage_6_RemoveFirebaseRequestIn",
        "RemoveFirebaseRequestOut": "_firebasestorage_7_RemoveFirebaseRequestOut",
        "BucketIn": "_firebasestorage_8_BucketIn",
        "BucketOut": "_firebasestorage_9_BucketOut",
        "AddFirebaseRequestIn": "_firebasestorage_10_AddFirebaseRequestIn",
        "AddFirebaseRequestOut": "_firebasestorage_11_AddFirebaseRequestOut",
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn": "_firebasestorage_12_GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn",
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut": "_firebasestorage_13_GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut",
        "ListBucketsResponseIn": "_firebasestorage_14_ListBucketsResponseIn",
        "ListBucketsResponseOut": "_firebasestorage_15_ListBucketsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types[
        "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn"
    ] = t.struct(
        {
            "lastUpdateTime": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
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
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut"
        ]
    )
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

    functions = {}
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
        importer="firebasestorage", renames=renames, types=types, functions=functions
    )
