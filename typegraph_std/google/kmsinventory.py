from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_kmsinventory() -> Import:
    kmsinventory = HTTPRuntime("https://kmsinventory.googleapis.com/")

    renames = {
        "ErrorResponse": "_kmsinventory_1_ErrorResponse",
        "GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn": "_kmsinventory_2_GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn",
        "GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut": "_kmsinventory_3_GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut",
        "GoogleCloudKmsV1CryptoKeyVersionTemplateIn": "_kmsinventory_4_GoogleCloudKmsV1CryptoKeyVersionTemplateIn",
        "GoogleCloudKmsV1CryptoKeyVersionTemplateOut": "_kmsinventory_5_GoogleCloudKmsV1CryptoKeyVersionTemplateOut",
        "GoogleCloudKmsV1KeyOperationAttestationIn": "_kmsinventory_6_GoogleCloudKmsV1KeyOperationAttestationIn",
        "GoogleCloudKmsV1KeyOperationAttestationOut": "_kmsinventory_7_GoogleCloudKmsV1KeyOperationAttestationOut",
        "GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn": "_kmsinventory_8_GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn",
        "GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut": "_kmsinventory_9_GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut",
        "GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn": "_kmsinventory_10_GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn",
        "GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut": "_kmsinventory_11_GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut",
        "GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn": "_kmsinventory_12_GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn",
        "GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut": "_kmsinventory_13_GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut",
        "GoogleCloudKmsInventoryV1ProtectedResourceIn": "_kmsinventory_14_GoogleCloudKmsInventoryV1ProtectedResourceIn",
        "GoogleCloudKmsInventoryV1ProtectedResourceOut": "_kmsinventory_15_GoogleCloudKmsInventoryV1ProtectedResourceOut",
        "GoogleCloudKmsV1CryptoKeyIn": "_kmsinventory_16_GoogleCloudKmsV1CryptoKeyIn",
        "GoogleCloudKmsV1CryptoKeyOut": "_kmsinventory_17_GoogleCloudKmsV1CryptoKeyOut",
        "GoogleCloudKmsV1ExternalProtectionLevelOptionsIn": "_kmsinventory_18_GoogleCloudKmsV1ExternalProtectionLevelOptionsIn",
        "GoogleCloudKmsV1ExternalProtectionLevelOptionsOut": "_kmsinventory_19_GoogleCloudKmsV1ExternalProtectionLevelOptionsOut",
        "GoogleCloudKmsV1CryptoKeyVersionIn": "_kmsinventory_20_GoogleCloudKmsV1CryptoKeyVersionIn",
        "GoogleCloudKmsV1CryptoKeyVersionOut": "_kmsinventory_21_GoogleCloudKmsV1CryptoKeyVersionOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cryptoKeys": t.array(
                t.proxy(renames["GoogleCloudKmsV1CryptoKeyIn"])
            ).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn"])
    types["GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "cryptoKeys": t.array(
                t.proxy(renames["GoogleCloudKmsV1CryptoKeyOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut"])
    types["GoogleCloudKmsV1CryptoKeyVersionTemplateIn"] = t.struct(
        {"algorithm": t.string(), "protectionLevel": t.string().optional()}
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionTemplateIn"])
    types["GoogleCloudKmsV1CryptoKeyVersionTemplateOut"] = t.struct(
        {
            "algorithm": t.string(),
            "protectionLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionTemplateOut"])
    types["GoogleCloudKmsV1KeyOperationAttestationIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationIn"])
    types["GoogleCloudKmsV1KeyOperationAttestationOut"] = t.struct(
        {
            "certChains": t.proxy(
                renames["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut"]
            ).optional(),
            "format": t.string().optional(),
            "content": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationOut"])
    types["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn"] = t.struct(
        {
            "resourceTypes": t.struct({"_": t.string().optional()}).optional(),
            "projectCount": t.integer().optional(),
            "resourceCount": t.string().optional(),
            "locations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "cloudProducts": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn"])
    types["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut"] = t.struct(
        {
            "resourceTypes": t.struct({"_": t.string().optional()}).optional(),
            "projectCount": t.integer().optional(),
            "resourceCount": t.string().optional(),
            "locations": t.struct({"_": t.string().optional()}).optional(),
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
    types["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn"] = t.struct(
        {
            "caviumCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
            "googleCardCerts": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn"])
    types["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut"] = t.struct(
        {
            "caviumCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
            "googleCardCerts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut"])
    types["GoogleCloudKmsInventoryV1ProtectedResourceIn"] = t.struct(
        {
            "location": t.string().optional(),
            "projectId": t.string().optional(),
            "cloudProduct": t.string().optional(),
            "project": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cryptoKeyVersion": t.string().optional(),
            "cryptoKeyVersions": t.array(t.string()).optional(),
            "resourceType": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourceIn"])
    types["GoogleCloudKmsInventoryV1ProtectedResourceOut"] = t.struct(
        {
            "location": t.string().optional(),
            "projectId": t.string().optional(),
            "cloudProduct": t.string().optional(),
            "project": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cryptoKeyVersion": t.string().optional(),
            "cryptoKeyVersions": t.array(t.string()).optional(),
            "resourceType": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourceOut"])
    types["GoogleCloudKmsV1CryptoKeyIn"] = t.struct(
        {
            "rotationPeriod": t.string().optional(),
            "versionTemplate": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionTemplateIn"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "purpose": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "nextRotationTime": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
            "cryptoKeyBackend": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyIn"])
    types["GoogleCloudKmsV1CryptoKeyOut"] = t.struct(
        {
            "rotationPeriod": t.string().optional(),
            "primary": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionOut"]
            ).optional(),
            "versionTemplate": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionTemplateOut"]
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "purpose": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "nextRotationTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
            "cryptoKeyBackend": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyOut"])
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
    types["GoogleCloudKmsV1CryptoKeyVersionIn"] = t.struct(
        {
            "externalProtectionLevelOptions": t.proxy(
                renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsIn"]
            ).optional(),
            "state": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionIn"])
    types["GoogleCloudKmsV1CryptoKeyVersionOut"] = t.struct(
        {
            "generateTime": t.string().optional(),
            "externalDestructionFailureReason": t.string().optional(),
            "externalProtectionLevelOptions": t.proxy(
                renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsOut"]
            ).optional(),
            "reimportEligible": t.boolean().optional(),
            "name": t.string().optional(),
            "algorithm": t.string().optional(),
            "destroyEventTime": t.string().optional(),
            "importJob": t.string().optional(),
            "generationFailureReason": t.string().optional(),
            "destroyTime": t.string().optional(),
            "state": t.string().optional(),
            "attestation": t.proxy(
                renames["GoogleCloudKmsV1KeyOperationAttestationOut"]
            ).optional(),
            "importTime": t.string().optional(),
            "importFailureReason": t.string().optional(),
            "createTime": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionOut"])

    functions = {}
    functions["organizationsProtectedResourcesSearch"] = kmsinventory.get(
        "v1/{scope}/protectedResources:search",
        t.struct(
            {
                "scope": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "cryptoKey": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut"]
        ),
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
    functions["projectsCryptoKeysList"] = kmsinventory.get(
        "v1/{parent}/cryptoKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="kmsinventory",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
