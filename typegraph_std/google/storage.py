from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_storage() -> Import:
    storage = HTTPRuntime("https://storage.googleapis.com/")

    renames = {
        "ErrorResponse": "_storage_1_ErrorResponse",
        "BucketIn": "_storage_2_BucketIn",
        "BucketOut": "_storage_3_BucketOut",
        "BucketAccessControlIn": "_storage_4_BucketAccessControlIn",
        "BucketAccessControlOut": "_storage_5_BucketAccessControlOut",
        "BucketAccessControlsIn": "_storage_6_BucketAccessControlsIn",
        "BucketAccessControlsOut": "_storage_7_BucketAccessControlsOut",
        "BucketsIn": "_storage_8_BucketsIn",
        "BucketsOut": "_storage_9_BucketsOut",
        "ChannelIn": "_storage_10_ChannelIn",
        "ChannelOut": "_storage_11_ChannelOut",
        "ComposeRequestIn": "_storage_12_ComposeRequestIn",
        "ComposeRequestOut": "_storage_13_ComposeRequestOut",
        "ExprIn": "_storage_14_ExprIn",
        "ExprOut": "_storage_15_ExprOut",
        "HmacKeyIn": "_storage_16_HmacKeyIn",
        "HmacKeyOut": "_storage_17_HmacKeyOut",
        "HmacKeyMetadataIn": "_storage_18_HmacKeyMetadataIn",
        "HmacKeyMetadataOut": "_storage_19_HmacKeyMetadataOut",
        "HmacKeysMetadataIn": "_storage_20_HmacKeysMetadataIn",
        "HmacKeysMetadataOut": "_storage_21_HmacKeysMetadataOut",
        "NotificationIn": "_storage_22_NotificationIn",
        "NotificationOut": "_storage_23_NotificationOut",
        "NotificationsIn": "_storage_24_NotificationsIn",
        "NotificationsOut": "_storage_25_NotificationsOut",
        "ObjectIn": "_storage_26_ObjectIn",
        "ObjectOut": "_storage_27_ObjectOut",
        "ObjectAccessControlIn": "_storage_28_ObjectAccessControlIn",
        "ObjectAccessControlOut": "_storage_29_ObjectAccessControlOut",
        "ObjectAccessControlsIn": "_storage_30_ObjectAccessControlsIn",
        "ObjectAccessControlsOut": "_storage_31_ObjectAccessControlsOut",
        "ObjectsIn": "_storage_32_ObjectsIn",
        "ObjectsOut": "_storage_33_ObjectsOut",
        "PolicyIn": "_storage_34_PolicyIn",
        "PolicyOut": "_storage_35_PolicyOut",
        "RewriteResponseIn": "_storage_36_RewriteResponseIn",
        "RewriteResponseOut": "_storage_37_RewriteResponseOut",
        "ServiceAccountIn": "_storage_38_ServiceAccountIn",
        "ServiceAccountOut": "_storage_39_ServiceAccountOut",
        "TestIamPermissionsResponseIn": "_storage_40_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_storage_41_TestIamPermissionsResponseOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BucketIn"] = t.struct(
        {
            "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
            "billing": t.struct({"requesterPays": t.boolean().optional()}).optional(),
            "cors": t.array(
                t.struct(
                    {
                        "maxAgeSeconds": t.integer().optional(),
                        "method": t.array(t.string()).optional(),
                        "origin": t.array(t.string()).optional(),
                        "responseHeader": t.array(t.string()).optional(),
                    }
                )
            ).optional(),
            "customPlacementConfig": t.struct(
                {"dataLocations": t.array(t.string()).optional()}
            ).optional(),
            "defaultEventBasedHold": t.boolean().optional(),
            "defaultObjectAcl": t.array(
                t.proxy(renames["ObjectAccessControlIn"])
            ).optional(),
            "encryption": t.struct(
                {"defaultKmsKeyName": t.string().optional()}
            ).optional(),
            "etag": t.string().optional(),
            "iamConfiguration": t.struct(
                {
                    "bucketPolicyOnly": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "lockedTime": t.string().optional(),
                        }
                    ).optional(),
                    "uniformBucketLevelAccess": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "lockedTime": t.string().optional(),
                        }
                    ).optional(),
                    "publicAccessPrevention": t.string().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "lifecycle": t.struct(
                {
                    "rule": t.array(
                        t.struct(
                            {
                                "action": t.struct(
                                    {
                                        "storageClass": t.string().optional(),
                                        "type": t.string().optional(),
                                    }
                                ).optional(),
                                "condition": t.struct(
                                    {
                                        "age": t.integer().optional(),
                                        "createdBefore": t.string().optional(),
                                        "customTimeBefore": t.string().optional(),
                                        "daysSinceCustomTime": t.integer().optional(),
                                        "daysSinceNoncurrentTime": t.integer().optional(),
                                        "isLive": t.boolean().optional(),
                                        "matchesPattern": t.string().optional(),
                                        "matchesPrefix": t.array(t.string()).optional(),
                                        "matchesSuffix": t.array(t.string()).optional(),
                                        "matchesStorageClass": t.array(
                                            t.string()
                                        ).optional(),
                                        "noncurrentTimeBefore": t.string().optional(),
                                        "numNewerVersions": t.integer().optional(),
                                    }
                                ).optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "autoclass": t.struct(
                {"enabled": t.boolean().optional(), "toggleTime": t.string().optional()}
            ).optional(),
            "location": t.string().optional(),
            "locationType": t.string().optional(),
            "logging": t.struct(
                {
                    "logBucket": t.string().optional(),
                    "logObjectPrefix": t.string().optional(),
                }
            ).optional(),
            "metageneration": t.string().optional(),
            "name": t.string().optional(),
            "owner": t.struct(
                {"entity": t.string().optional(), "entityId": t.string().optional()}
            ).optional(),
            "projectNumber": t.string().optional(),
            "retentionPolicy": t.struct(
                {
                    "effectiveTime": t.string().optional(),
                    "isLocked": t.boolean().optional(),
                    "retentionPeriod": t.string().optional(),
                }
            ).optional(),
            "rpo": t.string().optional(),
            "selfLink": t.string().optional(),
            "storageClass": t.string().optional(),
            "timeCreated": t.string().optional(),
            "updated": t.string().optional(),
            "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
            "website": t.struct(
                {
                    "mainPageSuffix": t.string().optional(),
                    "notFoundPage": t.string().optional(),
                }
            ).optional(),
            "satisfiesPZS": t.boolean().optional(),
        }
    ).named(renames["BucketIn"])
    types["BucketOut"] = t.struct(
        {
            "acl": t.array(t.proxy(renames["BucketAccessControlOut"])).optional(),
            "billing": t.struct({"requesterPays": t.boolean().optional()}).optional(),
            "cors": t.array(
                t.struct(
                    {
                        "maxAgeSeconds": t.integer().optional(),
                        "method": t.array(t.string()).optional(),
                        "origin": t.array(t.string()).optional(),
                        "responseHeader": t.array(t.string()).optional(),
                    }
                )
            ).optional(),
            "customPlacementConfig": t.struct(
                {"dataLocations": t.array(t.string()).optional()}
            ).optional(),
            "defaultEventBasedHold": t.boolean().optional(),
            "defaultObjectAcl": t.array(
                t.proxy(renames["ObjectAccessControlOut"])
            ).optional(),
            "encryption": t.struct(
                {"defaultKmsKeyName": t.string().optional()}
            ).optional(),
            "etag": t.string().optional(),
            "iamConfiguration": t.struct(
                {
                    "bucketPolicyOnly": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "lockedTime": t.string().optional(),
                        }
                    ).optional(),
                    "uniformBucketLevelAccess": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "lockedTime": t.string().optional(),
                        }
                    ).optional(),
                    "publicAccessPrevention": t.string().optional(),
                }
            ).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "lifecycle": t.struct(
                {
                    "rule": t.array(
                        t.struct(
                            {
                                "action": t.struct(
                                    {
                                        "storageClass": t.string().optional(),
                                        "type": t.string().optional(),
                                    }
                                ).optional(),
                                "condition": t.struct(
                                    {
                                        "age": t.integer().optional(),
                                        "createdBefore": t.string().optional(),
                                        "customTimeBefore": t.string().optional(),
                                        "daysSinceCustomTime": t.integer().optional(),
                                        "daysSinceNoncurrentTime": t.integer().optional(),
                                        "isLive": t.boolean().optional(),
                                        "matchesPattern": t.string().optional(),
                                        "matchesPrefix": t.array(t.string()).optional(),
                                        "matchesSuffix": t.array(t.string()).optional(),
                                        "matchesStorageClass": t.array(
                                            t.string()
                                        ).optional(),
                                        "noncurrentTimeBefore": t.string().optional(),
                                        "numNewerVersions": t.integer().optional(),
                                    }
                                ).optional(),
                            }
                        )
                    ).optional()
                }
            ).optional(),
            "autoclass": t.struct(
                {"enabled": t.boolean().optional(), "toggleTime": t.string().optional()}
            ).optional(),
            "location": t.string().optional(),
            "locationType": t.string().optional(),
            "logging": t.struct(
                {
                    "logBucket": t.string().optional(),
                    "logObjectPrefix": t.string().optional(),
                }
            ).optional(),
            "metageneration": t.string().optional(),
            "name": t.string().optional(),
            "owner": t.struct(
                {"entity": t.string().optional(), "entityId": t.string().optional()}
            ).optional(),
            "projectNumber": t.string().optional(),
            "retentionPolicy": t.struct(
                {
                    "effectiveTime": t.string().optional(),
                    "isLocked": t.boolean().optional(),
                    "retentionPeriod": t.string().optional(),
                }
            ).optional(),
            "rpo": t.string().optional(),
            "selfLink": t.string().optional(),
            "storageClass": t.string().optional(),
            "timeCreated": t.string().optional(),
            "updated": t.string().optional(),
            "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
            "website": t.struct(
                {
                    "mainPageSuffix": t.string().optional(),
                    "notFoundPage": t.string().optional(),
                }
            ).optional(),
            "satisfiesPZS": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketOut"])
    types["BucketAccessControlIn"] = t.struct(
        {
            "bucket": t.string().optional(),
            "domain": t.string().optional(),
            "email": t.string().optional(),
            "entity": t.string().optional(),
            "entityId": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "projectTeam": t.struct(
                {"projectNumber": t.string().optional(), "team": t.string().optional()}
            ).optional(),
            "role": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["BucketAccessControlIn"])
    types["BucketAccessControlOut"] = t.struct(
        {
            "bucket": t.string().optional(),
            "domain": t.string().optional(),
            "email": t.string().optional(),
            "entity": t.string().optional(),
            "entityId": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "projectTeam": t.struct(
                {"projectNumber": t.string().optional(), "team": t.string().optional()}
            ).optional(),
            "role": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketAccessControlOut"])
    types["BucketAccessControlsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["BucketAccessControlsIn"])
    types["BucketAccessControlsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BucketAccessControlOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketAccessControlsOut"])
    types["BucketsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BucketIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["BucketsIn"])
    types["BucketsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["BucketOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BucketsOut"])
    types["ChannelIn"] = t.struct(
        {
            "address": t.string().optional(),
            "expiration": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.boolean().optional(),
            "resourceId": t.string().optional(),
            "resourceUri": t.string().optional(),
            "token": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ChannelIn"])
    types["ChannelOut"] = t.struct(
        {
            "address": t.string().optional(),
            "expiration": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "params": t.struct({"_": t.string().optional()}).optional(),
            "payload": t.boolean().optional(),
            "resourceId": t.string().optional(),
            "resourceUri": t.string().optional(),
            "token": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChannelOut"])
    types["ComposeRequestIn"] = t.struct(
        {
            "destination": t.proxy(renames["ObjectIn"]).optional(),
            "kind": t.string().optional(),
            "sourceObjects": t.array(
                t.struct(
                    {
                        "generation": t.string().optional(),
                        "name": t.string().optional(),
                        "objectPreconditions": t.struct(
                            {"ifGenerationMatch": t.string().optional()}
                        ).optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["ComposeRequestIn"])
    types["ComposeRequestOut"] = t.struct(
        {
            "destination": t.proxy(renames["ObjectOut"]).optional(),
            "kind": t.string().optional(),
            "sourceObjects": t.array(
                t.struct(
                    {
                        "generation": t.string().optional(),
                        "name": t.string().optional(),
                        "objectPreconditions": t.struct(
                            {"ifGenerationMatch": t.string().optional()}
                        ).optional(),
                    }
                )
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ComposeRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["HmacKeyIn"] = t.struct(
        {
            "kind": t.string().optional(),
            "metadata": t.proxy(renames["HmacKeyMetadataIn"]).optional(),
            "secret": t.string().optional(),
        }
    ).named(renames["HmacKeyIn"])
    types["HmacKeyOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "metadata": t.proxy(renames["HmacKeyMetadataOut"]).optional(),
            "secret": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HmacKeyOut"])
    types["HmacKeyMetadataIn"] = t.struct(
        {
            "accessId": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "projectId": t.string().optional(),
            "selfLink": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "state": t.string().optional(),
            "timeCreated": t.string().optional(),
            "updated": t.string().optional(),
        }
    ).named(renames["HmacKeyMetadataIn"])
    types["HmacKeyMetadataOut"] = t.struct(
        {
            "accessId": t.string().optional(),
            "etag": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "projectId": t.string().optional(),
            "selfLink": t.string().optional(),
            "serviceAccountEmail": t.string().optional(),
            "state": t.string().optional(),
            "timeCreated": t.string().optional(),
            "updated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HmacKeyMetadataOut"])
    types["HmacKeysMetadataIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["HmacKeyMetadataIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["HmacKeysMetadataIn"])
    types["HmacKeysMetadataOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["HmacKeyMetadataOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["HmacKeysMetadataOut"])
    types["NotificationIn"] = t.struct(
        {
            "custom_attributes": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "event_types": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "object_name_prefix": t.string().optional(),
            "payload_format": t.string().optional(),
            "selfLink": t.string().optional(),
            "topic": t.string().optional(),
        }
    ).named(renames["NotificationIn"])
    types["NotificationOut"] = t.struct(
        {
            "custom_attributes": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "event_types": t.array(t.string()).optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "object_name_prefix": t.string().optional(),
            "payload_format": t.string().optional(),
            "selfLink": t.string().optional(),
            "topic": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationOut"])
    types["NotificationsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["NotificationIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["NotificationsIn"])
    types["NotificationsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["NotificationOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["NotificationsOut"])
    types["ObjectIn"] = t.struct(
        {
            "acl": t.array(t.proxy(renames["ObjectAccessControlIn"])).optional(),
            "bucket": t.string().optional(),
            "cacheControl": t.string().optional(),
            "componentCount": t.integer().optional(),
            "contentDisposition": t.string().optional(),
            "contentEncoding": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "contentType": t.string().optional(),
            "crc32c": t.string().optional(),
            "customTime": t.string().optional(),
            "customerEncryption": t.struct(
                {
                    "encryptionAlgorithm": t.string().optional(),
                    "keySha256": t.string().optional(),
                }
            ).optional(),
            "etag": t.string().optional(),
            "eventBasedHold": t.boolean().optional(),
            "generation": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "md5Hash": t.string().optional(),
            "mediaLink": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "metageneration": t.string().optional(),
            "name": t.string().optional(),
            "owner": t.struct(
                {"entity": t.string().optional(), "entityId": t.string().optional()}
            ).optional(),
            "retentionExpirationTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "size": t.string().optional(),
            "storageClass": t.string().optional(),
            "temporaryHold": t.boolean().optional(),
            "timeCreated": t.string().optional(),
            "timeDeleted": t.string().optional(),
            "timeStorageClassUpdated": t.string().optional(),
            "updated": t.string().optional(),
        }
    ).named(renames["ObjectIn"])
    types["ObjectOut"] = t.struct(
        {
            "acl": t.array(t.proxy(renames["ObjectAccessControlOut"])).optional(),
            "bucket": t.string().optional(),
            "cacheControl": t.string().optional(),
            "componentCount": t.integer().optional(),
            "contentDisposition": t.string().optional(),
            "contentEncoding": t.string().optional(),
            "contentLanguage": t.string().optional(),
            "contentType": t.string().optional(),
            "crc32c": t.string().optional(),
            "customTime": t.string().optional(),
            "customerEncryption": t.struct(
                {
                    "encryptionAlgorithm": t.string().optional(),
                    "keySha256": t.string().optional(),
                }
            ).optional(),
            "etag": t.string().optional(),
            "eventBasedHold": t.boolean().optional(),
            "generation": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "kmsKeyName": t.string().optional(),
            "md5Hash": t.string().optional(),
            "mediaLink": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "metageneration": t.string().optional(),
            "name": t.string().optional(),
            "owner": t.struct(
                {"entity": t.string().optional(), "entityId": t.string().optional()}
            ).optional(),
            "retentionExpirationTime": t.string().optional(),
            "selfLink": t.string().optional(),
            "size": t.string().optional(),
            "storageClass": t.string().optional(),
            "temporaryHold": t.boolean().optional(),
            "timeCreated": t.string().optional(),
            "timeDeleted": t.string().optional(),
            "timeStorageClassUpdated": t.string().optional(),
            "updated": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectOut"])
    types["ObjectAccessControlIn"] = t.struct(
        {
            "bucket": t.string().optional(),
            "domain": t.string().optional(),
            "email": t.string().optional(),
            "entity": t.string().optional(),
            "entityId": t.string().optional(),
            "etag": t.string().optional(),
            "generation": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "object": t.string().optional(),
            "projectTeam": t.struct(
                {"projectNumber": t.string().optional(), "team": t.string().optional()}
            ).optional(),
            "role": t.string().optional(),
            "selfLink": t.string().optional(),
        }
    ).named(renames["ObjectAccessControlIn"])
    types["ObjectAccessControlOut"] = t.struct(
        {
            "bucket": t.string().optional(),
            "domain": t.string().optional(),
            "email": t.string().optional(),
            "entity": t.string().optional(),
            "entityId": t.string().optional(),
            "etag": t.string().optional(),
            "generation": t.string().optional(),
            "id": t.string().optional(),
            "kind": t.string().optional(),
            "object": t.string().optional(),
            "projectTeam": t.struct(
                {"projectNumber": t.string().optional(), "team": t.string().optional()}
            ).optional(),
            "role": t.string().optional(),
            "selfLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectAccessControlOut"])
    types["ObjectAccessControlsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ObjectAccessControlIn"])).optional(),
            "kind": t.string().optional(),
        }
    ).named(renames["ObjectAccessControlsIn"])
    types["ObjectAccessControlsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ObjectAccessControlOut"])).optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectAccessControlsOut"])
    types["ObjectsIn"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ObjectIn"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "prefixes": t.array(t.string()).optional(),
        }
    ).named(renames["ObjectsIn"])
    types["ObjectsOut"] = t.struct(
        {
            "items": t.array(t.proxy(renames["ObjectOut"])).optional(),
            "kind": t.string().optional(),
            "nextPageToken": t.string().optional(),
            "prefixes": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ObjectsOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(
                t.struct(
                    {
                        "condition": t.proxy(renames["ExprIn"]).optional(),
                        "members": t.array(t.string()).optional(),
                        "role": t.string().optional(),
                    }
                )
            ).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "resourceId": t.string().optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(
                t.struct(
                    {
                        "condition": t.proxy(renames["ExprOut"]).optional(),
                        "members": t.array(t.string()).optional(),
                        "role": t.string().optional(),
                    }
                )
            ).optional(),
            "etag": t.string().optional(),
            "kind": t.string().optional(),
            "resourceId": t.string().optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["RewriteResponseIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "kind": t.string().optional(),
            "objectSize": t.string().optional(),
            "resource": t.proxy(renames["ObjectIn"]).optional(),
            "rewriteToken": t.string().optional(),
            "totalBytesRewritten": t.string().optional(),
        }
    ).named(renames["RewriteResponseIn"])
    types["RewriteResponseOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "kind": t.string().optional(),
            "objectSize": t.string().optional(),
            "resource": t.proxy(renames["ObjectOut"]).optional(),
            "rewriteToken": t.string().optional(),
            "totalBytesRewritten": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RewriteResponseOut"])
    types["ServiceAccountIn"] = t.struct(
        {"email_address": t.string().optional(), "kind": t.string().optional()}
    ).named(renames["ServiceAccountIn"])
    types["ServiceAccountOut"] = t.struct(
        {
            "email_address": t.string().optional(),
            "kind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"kind": t.string().optional(), "permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "kind": t.string().optional(),
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])

    functions = {}
    functions["bucketAccessControlsDelete"] = storage.put(
        "b/{bucket}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketAccessControlsGet"] = storage.put(
        "b/{bucket}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketAccessControlsInsert"] = storage.put(
        "b/{bucket}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketAccessControlsList"] = storage.put(
        "b/{bucket}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketAccessControlsPatch"] = storage.put(
        "b/{bucket}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketAccessControlsUpdate"] = storage.put(
        "b/{bucket}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsDelete"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsGet"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsGetIamPolicy"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsInsert"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsList"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsLockRetentionPolicy"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsPatch"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsSetIamPolicy"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsTestIamPermissions"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["bucketsUpdate"] = storage.put(
        "b/{bucket}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "ifMetagenerationMatch": t.string().optional(),
                "ifMetagenerationNotMatch": t.string().optional(),
                "predefinedAcl": t.string().optional(),
                "predefinedDefaultObjectAcl": t.string().optional(),
                "projection": t.string().optional(),
                "userProject": t.string().optional(),
                "acl": t.array(t.proxy(renames["BucketAccessControlIn"])).optional(),
                "billing": t.struct(
                    {"requesterPays": t.boolean().optional()}
                ).optional(),
                "cors": t.array(
                    t.struct(
                        {
                            "maxAgeSeconds": t.integer().optional(),
                            "method": t.array(t.string()).optional(),
                            "origin": t.array(t.string()).optional(),
                            "responseHeader": t.array(t.string()).optional(),
                        }
                    )
                ).optional(),
                "customPlacementConfig": t.struct(
                    {"dataLocations": t.array(t.string()).optional()}
                ).optional(),
                "defaultEventBasedHold": t.boolean().optional(),
                "defaultObjectAcl": t.array(
                    t.proxy(renames["ObjectAccessControlIn"])
                ).optional(),
                "encryption": t.struct(
                    {"defaultKmsKeyName": t.string().optional()}
                ).optional(),
                "etag": t.string().optional(),
                "iamConfiguration": t.struct(
                    {
                        "bucketPolicyOnly": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "uniformBucketLevelAccess": t.struct(
                            {
                                "enabled": t.boolean().optional(),
                                "lockedTime": t.string().optional(),
                            }
                        ).optional(),
                        "publicAccessPrevention": t.string().optional(),
                    }
                ).optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "lifecycle": t.struct(
                    {
                        "rule": t.array(
                            t.struct(
                                {
                                    "action": t.struct(
                                        {
                                            "storageClass": t.string().optional(),
                                            "type": t.string().optional(),
                                        }
                                    ).optional(),
                                    "condition": t.struct(
                                        {
                                            "age": t.integer().optional(),
                                            "createdBefore": t.string().optional(),
                                            "customTimeBefore": t.string().optional(),
                                            "daysSinceCustomTime": t.integer().optional(),
                                            "daysSinceNoncurrentTime": t.integer().optional(),
                                            "isLive": t.boolean().optional(),
                                            "matchesPattern": t.string().optional(),
                                            "matchesPrefix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesSuffix": t.array(
                                                t.string()
                                            ).optional(),
                                            "matchesStorageClass": t.array(
                                                t.string()
                                            ).optional(),
                                            "noncurrentTimeBefore": t.string().optional(),
                                            "numNewerVersions": t.integer().optional(),
                                        }
                                    ).optional(),
                                }
                            )
                        ).optional()
                    }
                ).optional(),
                "autoclass": t.struct(
                    {
                        "enabled": t.boolean().optional(),
                        "toggleTime": t.string().optional(),
                    }
                ).optional(),
                "location": t.string().optional(),
                "locationType": t.string().optional(),
                "logging": t.struct(
                    {
                        "logBucket": t.string().optional(),
                        "logObjectPrefix": t.string().optional(),
                    }
                ).optional(),
                "metageneration": t.string().optional(),
                "name": t.string().optional(),
                "owner": t.struct(
                    {"entity": t.string().optional(), "entityId": t.string().optional()}
                ).optional(),
                "projectNumber": t.string().optional(),
                "retentionPolicy": t.struct(
                    {
                        "effectiveTime": t.string().optional(),
                        "isLocked": t.boolean().optional(),
                        "retentionPeriod": t.string().optional(),
                    }
                ).optional(),
                "rpo": t.string().optional(),
                "selfLink": t.string().optional(),
                "storageClass": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "versioning": t.struct({"enabled": t.boolean().optional()}).optional(),
                "website": t.struct(
                    {
                        "mainPageSuffix": t.string().optional(),
                        "notFoundPage": t.string().optional(),
                    }
                ).optional(),
                "satisfiesPZS": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["BucketOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["channelsStop"] = storage.post(
        "channels/stop",
        t.struct(
            {
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.struct({"_": t.string().optional()}),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["defaultObjectAccessControlsDelete"] = storage.put(
        "b/{bucket}/defaultObjectAcl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "generation": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "object": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["defaultObjectAccessControlsGet"] = storage.put(
        "b/{bucket}/defaultObjectAcl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "generation": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "object": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["defaultObjectAccessControlsInsert"] = storage.put(
        "b/{bucket}/defaultObjectAcl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "generation": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "object": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["defaultObjectAccessControlsList"] = storage.put(
        "b/{bucket}/defaultObjectAcl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "generation": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "object": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["defaultObjectAccessControlsPatch"] = storage.put(
        "b/{bucket}/defaultObjectAcl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "generation": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "object": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["defaultObjectAccessControlsUpdate"] = storage.put(
        "b/{bucket}/defaultObjectAcl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "generation": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "object": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notificationsDelete"] = storage.get(
        "b/{bucket}/notificationConfigs",
        t.struct(
            {
                "bucket": t.string().optional(),
                "userProject": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notificationsGet"] = storage.get(
        "b/{bucket}/notificationConfigs",
        t.struct(
            {
                "bucket": t.string().optional(),
                "userProject": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notificationsInsert"] = storage.get(
        "b/{bucket}/notificationConfigs",
        t.struct(
            {
                "bucket": t.string().optional(),
                "userProject": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["notificationsList"] = storage.get(
        "b/{bucket}/notificationConfigs",
        t.struct(
            {
                "bucket": t.string().optional(),
                "userProject": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["NotificationsOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectAccessControlsDelete"] = storage.put(
        "b/{bucket}/o/{object}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "generation": t.string().optional(),
                "object": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectAccessControlsGet"] = storage.put(
        "b/{bucket}/o/{object}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "generation": t.string().optional(),
                "object": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectAccessControlsInsert"] = storage.put(
        "b/{bucket}/o/{object}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "generation": t.string().optional(),
                "object": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectAccessControlsList"] = storage.put(
        "b/{bucket}/o/{object}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "generation": t.string().optional(),
                "object": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectAccessControlsPatch"] = storage.put(
        "b/{bucket}/o/{object}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "generation": t.string().optional(),
                "object": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectAccessControlsUpdate"] = storage.put(
        "b/{bucket}/o/{object}/acl/{entity}",
        t.struct(
            {
                "bucket": t.string().optional(),
                "entity": t.string().optional(),
                "generation": t.string().optional(),
                "object": t.string().optional(),
                "userProject": t.string().optional(),
                "domain": t.string().optional(),
                "email": t.string().optional(),
                "entityId": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "projectTeam": t.struct(
                    {
                        "projectNumber": t.string().optional(),
                        "team": t.string().optional(),
                    }
                ).optional(),
                "role": t.string().optional(),
                "selfLink": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ObjectAccessControlOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsCompose"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsCopy"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsDelete"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsGet"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsGetIamPolicy"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsInsert"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsList"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsPatch"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsRewrite"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsSetIamPolicy"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsTestIamPermissions"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsUpdate"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["objectsWatchAll"] = storage.post(
        "b/{bucket}/o/watch",
        t.struct(
            {
                "bucket": t.string().optional(),
                "delimiter": t.string().optional(),
                "endOffset": t.string().optional(),
                "includeTrailingDelimiter": t.boolean().optional(),
                "maxResults": t.integer().optional(),
                "pageToken": t.string().optional(),
                "prefix": t.string().optional(),
                "projection": t.string().optional(),
                "startOffset": t.string().optional(),
                "userProject": t.string().optional(),
                "versions": t.boolean().optional(),
                "address": t.string().optional(),
                "expiration": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "params": t.struct({"_": t.string().optional()}).optional(),
                "payload": t.boolean().optional(),
                "resourceId": t.string().optional(),
                "resourceUri": t.string().optional(),
                "token": t.string().optional(),
                "type": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ChannelOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHmacKeysCreate"] = storage.put(
        "projects/{projectId}/hmacKeys/{accessId}",
        t.struct(
            {
                "accessId": t.string().optional(),
                "projectId": t.string().optional(),
                "userProject": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "serviceAccountEmail": t.string().optional(),
                "state": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HmacKeyMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHmacKeysDelete"] = storage.put(
        "projects/{projectId}/hmacKeys/{accessId}",
        t.struct(
            {
                "accessId": t.string().optional(),
                "projectId": t.string().optional(),
                "userProject": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "serviceAccountEmail": t.string().optional(),
                "state": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HmacKeyMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHmacKeysGet"] = storage.put(
        "projects/{projectId}/hmacKeys/{accessId}",
        t.struct(
            {
                "accessId": t.string().optional(),
                "projectId": t.string().optional(),
                "userProject": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "serviceAccountEmail": t.string().optional(),
                "state": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HmacKeyMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHmacKeysList"] = storage.put(
        "projects/{projectId}/hmacKeys/{accessId}",
        t.struct(
            {
                "accessId": t.string().optional(),
                "projectId": t.string().optional(),
                "userProject": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "serviceAccountEmail": t.string().optional(),
                "state": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HmacKeyMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsHmacKeysUpdate"] = storage.put(
        "projects/{projectId}/hmacKeys/{accessId}",
        t.struct(
            {
                "accessId": t.string().optional(),
                "projectId": t.string().optional(),
                "userProject": t.string().optional(),
                "etag": t.string().optional(),
                "id": t.string().optional(),
                "kind": t.string().optional(),
                "selfLink": t.string().optional(),
                "serviceAccountEmail": t.string().optional(),
                "state": t.string().optional(),
                "timeCreated": t.string().optional(),
                "updated": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["HmacKeyMetadataOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsServiceAccountGet"] = storage.get(
        "projects/{projectId}/serviceAccount",
        t.struct(
            {
                "projectId": t.string().optional(),
                "userProject": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ServiceAccountOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="storage", renames=renames, types=Box(types), functions=Box(functions)
    )
