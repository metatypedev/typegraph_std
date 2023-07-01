from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_kmsinventory():
    kmsinventory = HTTPRuntime("https://kmsinventory.googleapis.com/")

    renames = {
        "ErrorResponse": "_kmsinventory_1_ErrorResponse",
        "GoogleCloudKmsV1ExternalProtectionLevelOptionsIn": "_kmsinventory_2_GoogleCloudKmsV1ExternalProtectionLevelOptionsIn",
        "GoogleCloudKmsV1ExternalProtectionLevelOptionsOut": "_kmsinventory_3_GoogleCloudKmsV1ExternalProtectionLevelOptionsOut",
        "GoogleCloudKmsV1CryptoKeyVersionTemplateIn": "_kmsinventory_4_GoogleCloudKmsV1CryptoKeyVersionTemplateIn",
        "GoogleCloudKmsV1CryptoKeyVersionTemplateOut": "_kmsinventory_5_GoogleCloudKmsV1CryptoKeyVersionTemplateOut",
        "GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn": "_kmsinventory_6_GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn",
        "GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut": "_kmsinventory_7_GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut",
        "GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn": "_kmsinventory_8_GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn",
        "GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut": "_kmsinventory_9_GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut",
        "GoogleCloudKmsV1CryptoKeyVersionIn": "_kmsinventory_10_GoogleCloudKmsV1CryptoKeyVersionIn",
        "GoogleCloudKmsV1CryptoKeyVersionOut": "_kmsinventory_11_GoogleCloudKmsV1CryptoKeyVersionOut",
        "GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn": "_kmsinventory_12_GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn",
        "GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut": "_kmsinventory_13_GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut",
        "GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn": "_kmsinventory_14_GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn",
        "GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut": "_kmsinventory_15_GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut",
        "GoogleCloudKmsInventoryV1ProtectedResourceIn": "_kmsinventory_16_GoogleCloudKmsInventoryV1ProtectedResourceIn",
        "GoogleCloudKmsInventoryV1ProtectedResourceOut": "_kmsinventory_17_GoogleCloudKmsInventoryV1ProtectedResourceOut",
        "GoogleCloudKmsV1KeyOperationAttestationIn": "_kmsinventory_18_GoogleCloudKmsV1KeyOperationAttestationIn",
        "GoogleCloudKmsV1KeyOperationAttestationOut": "_kmsinventory_19_GoogleCloudKmsV1KeyOperationAttestationOut",
        "GoogleCloudKmsV1CryptoKeyIn": "_kmsinventory_20_GoogleCloudKmsV1CryptoKeyIn",
        "GoogleCloudKmsV1CryptoKeyOut": "_kmsinventory_21_GoogleCloudKmsV1CryptoKeyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudKmsV1ExternalProtectionLevelOptionsIn"] = t.struct(
        {
            "ekmConnectionKeyPath": t.string().optional(),
            "externalKeyUri": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsIn"])
    types["GoogleCloudKmsV1ExternalProtectionLevelOptionsOut"] = t.struct(
        {
            "ekmConnectionKeyPath": t.string().optional(),
            "externalKeyUri": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsOut"])
    types["GoogleCloudKmsV1CryptoKeyVersionTemplateIn"] = t.struct(
        {"protectionLevel": t.string().optional(), "algorithm": t.string()}
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionTemplateIn"])
    types["GoogleCloudKmsV1CryptoKeyVersionTemplateOut"] = t.struct(
        {
            "protectionLevel": t.string().optional(),
            "algorithm": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionTemplateOut"])
    types["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn"] = t.struct(
        {
            "locations": t.struct({"_": t.string().optional()}).optional(),
            "projectCount": t.integer().optional(),
            "resourceTypes": t.struct({"_": t.string().optional()}).optional(),
            "resourceCount": t.string().optional(),
            "name": t.string().optional(),
            "cloudProducts": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn"])
    types["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut"] = t.struct(
        {
            "locations": t.struct({"_": t.string().optional()}).optional(),
            "projectCount": t.integer().optional(),
            "resourceTypes": t.struct({"_": t.string().optional()}).optional(),
            "resourceCount": t.string().optional(),
            "name": t.string().optional(),
            "cloudProducts": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut"])
    types["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "protectedResources": t.array(
                t.proxy(renames["GoogleCloudKmsInventoryV1ProtectedResourceIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn"])
    types["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "protectedResources": t.array(
                t.proxy(renames["GoogleCloudKmsInventoryV1ProtectedResourceOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut"])
    types["GoogleCloudKmsV1CryptoKeyVersionIn"] = t.struct(
        {
            "state": t.string().optional(),
            "externalProtectionLevelOptions": t.proxy(
                renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsIn"]
            ).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionIn"])
    types["GoogleCloudKmsV1CryptoKeyVersionOut"] = t.struct(
        {
            "name": t.string().optional(),
            "attestation": t.proxy(
                renames["GoogleCloudKmsV1KeyOperationAttestationOut"]
            ).optional(),
            "reimportEligible": t.boolean().optional(),
            "generationFailureReason": t.string().optional(),
            "generateTime": t.string().optional(),
            "importTime": t.string().optional(),
            "createTime": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "state": t.string().optional(),
            "destroyEventTime": t.string().optional(),
            "destroyTime": t.string().optional(),
            "externalDestructionFailureReason": t.string().optional(),
            "importFailureReason": t.string().optional(),
            "algorithm": t.string().optional(),
            "externalProtectionLevelOptions": t.proxy(
                renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsOut"]
            ).optional(),
            "importJob": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionOut"])
    types["GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn"] = t.struct(
        {
            "cryptoKeys": t.array(
                t.proxy(renames["GoogleCloudKmsV1CryptoKeyIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn"])
    types["GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut"] = t.struct(
        {
            "cryptoKeys": t.array(
                t.proxy(renames["GoogleCloudKmsV1CryptoKeyOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut"])
    types["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn"] = t.struct(
        {
            "googleCardCerts": t.array(t.string()).optional(),
            "caviumCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn"])
    types["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut"] = t.struct(
        {
            "googleCardCerts": t.array(t.string()).optional(),
            "caviumCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut"])
    types["GoogleCloudKmsInventoryV1ProtectedResourceIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "cloudProduct": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "cryptoKeyVersions": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "cryptoKeyVersion": t.string().optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourceIn"])
    types["GoogleCloudKmsInventoryV1ProtectedResourceOut"] = t.struct(
        {
            "projectId": t.string().optional(),
            "cloudProduct": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "location": t.string().optional(),
            "cryptoKeyVersions": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "name": t.string().optional(),
            "cryptoKeyVersion": t.string().optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourceOut"])
    types["GoogleCloudKmsV1KeyOperationAttestationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationIn"])
    types["GoogleCloudKmsV1KeyOperationAttestationOut"] = t.struct(
        {
            "content": t.string().optional(),
            "format": t.string().optional(),
            "certChains": t.proxy(
                renames["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationOut"])
    types["GoogleCloudKmsV1CryptoKeyIn"] = t.struct(
        {
            "cryptoKeyBackend": t.string().optional(),
            "nextRotationTime": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "versionTemplate": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionTemplateIn"]
            ).optional(),
            "purpose": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destroyScheduledDuration": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyIn"])
    types["GoogleCloudKmsV1CryptoKeyOut"] = t.struct(
        {
            "cryptoKeyBackend": t.string().optional(),
            "primary": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionOut"]
            ).optional(),
            "nextRotationTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "versionTemplate": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionTemplateOut"]
            ).optional(),
            "purpose": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "destroyScheduledDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyOut"])

    functions = {}
    functions["projectsCryptoKeysList"] = kmsinventory.get(
        "v1/{parent}/cryptoKeys",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsKeyRingsCryptoKeysGetProtectedResourcesSummary"
    ] = kmsinventory.get(
        "v1/{name}/protectedResourcesSummary",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsProtectedResourcesSearch"] = kmsinventory.get(
        "v1/{scope}/protectedResources:search",
        t.struct(
            {
                "scope": t.string(),
                "cryptoKey": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="kmsinventory",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
