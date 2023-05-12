from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_kmsinventory() -> Import:
    kmsinventory = HTTPRuntime("https://kmsinventory.googleapis.com/")

    renames = {
        "ErrorResponse": "_kmsinventory_1_ErrorResponse",
        "GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn": "_kmsinventory_2_GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn",
        "GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut": "_kmsinventory_3_GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut",
        "GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn": "_kmsinventory_4_GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn",
        "GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut": "_kmsinventory_5_GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut",
        "GoogleCloudKmsV1CryptoKeyVersionIn": "_kmsinventory_6_GoogleCloudKmsV1CryptoKeyVersionIn",
        "GoogleCloudKmsV1CryptoKeyVersionOut": "_kmsinventory_7_GoogleCloudKmsV1CryptoKeyVersionOut",
        "GoogleCloudKmsV1ExternalProtectionLevelOptionsIn": "_kmsinventory_8_GoogleCloudKmsV1ExternalProtectionLevelOptionsIn",
        "GoogleCloudKmsV1ExternalProtectionLevelOptionsOut": "_kmsinventory_9_GoogleCloudKmsV1ExternalProtectionLevelOptionsOut",
        "GoogleCloudKmsV1KeyOperationAttestationIn": "_kmsinventory_10_GoogleCloudKmsV1KeyOperationAttestationIn",
        "GoogleCloudKmsV1KeyOperationAttestationOut": "_kmsinventory_11_GoogleCloudKmsV1KeyOperationAttestationOut",
        "GoogleCloudKmsV1CryptoKeyIn": "_kmsinventory_12_GoogleCloudKmsV1CryptoKeyIn",
        "GoogleCloudKmsV1CryptoKeyOut": "_kmsinventory_13_GoogleCloudKmsV1CryptoKeyOut",
        "GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn": "_kmsinventory_14_GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn",
        "GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut": "_kmsinventory_15_GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut",
        "GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn": "_kmsinventory_16_GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn",
        "GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut": "_kmsinventory_17_GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut",
        "GoogleCloudKmsInventoryV1ProtectedResourceIn": "_kmsinventory_18_GoogleCloudKmsInventoryV1ProtectedResourceIn",
        "GoogleCloudKmsInventoryV1ProtectedResourceOut": "_kmsinventory_19_GoogleCloudKmsInventoryV1ProtectedResourceOut",
        "GoogleCloudKmsV1CryptoKeyVersionTemplateIn": "_kmsinventory_20_GoogleCloudKmsV1CryptoKeyVersionTemplateIn",
        "GoogleCloudKmsV1CryptoKeyVersionTemplateOut": "_kmsinventory_21_GoogleCloudKmsV1CryptoKeyVersionTemplateOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn"] = t.struct(
        {
            "protectedResources": t.array(
                t.proxy(renames["GoogleCloudKmsInventoryV1ProtectedResourceIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn"])
    types["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut"] = t.struct(
        {
            "protectedResources": t.array(
                t.proxy(renames["GoogleCloudKmsInventoryV1ProtectedResourceOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut"])
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
            "importTime": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "name": t.string().optional(),
            "destroyTime": t.string().optional(),
            "reimportEligible": t.boolean().optional(),
            "generateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "importJob": t.string().optional(),
            "state": t.string().optional(),
            "destroyEventTime": t.string().optional(),
            "externalProtectionLevelOptions": t.proxy(
                renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsOut"]
            ).optional(),
            "generationFailureReason": t.string().optional(),
            "algorithm": t.string().optional(),
            "importFailureReason": t.string().optional(),
            "externalDestructionFailureReason": t.string().optional(),
            "attestation": t.proxy(
                renames["GoogleCloudKmsV1KeyOperationAttestationOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionOut"])
    types["GoogleCloudKmsV1ExternalProtectionLevelOptionsIn"] = t.struct(
        {
            "externalKeyUri": t.string().optional(),
            "ekmConnectionKeyPath": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsIn"])
    types["GoogleCloudKmsV1ExternalProtectionLevelOptionsOut"] = t.struct(
        {
            "externalKeyUri": t.string().optional(),
            "ekmConnectionKeyPath": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsOut"])
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
    types["GoogleCloudKmsV1CryptoKeyIn"] = t.struct(
        {
            "versionTemplate": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionTemplateIn"]
            ).optional(),
            "importOnly": t.boolean().optional(),
            "purpose": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nextRotationTime": t.string().optional(),
            "cryptoKeyBackend": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyIn"])
    types["GoogleCloudKmsV1CryptoKeyOut"] = t.struct(
        {
            "versionTemplate": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionTemplateOut"]
            ).optional(),
            "importOnly": t.boolean().optional(),
            "primary": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionOut"]
            ).optional(),
            "purpose": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nextRotationTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "cryptoKeyBackend": t.string().optional(),
            "rotationPeriod": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyOut"])
    types["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn"] = t.struct(
        {
            "locations": t.struct({"_": t.string().optional()}).optional(),
            "cloudProducts": t.struct({"_": t.string().optional()}).optional(),
            "resourceTypes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "projectCount": t.integer().optional(),
            "resourceCount": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn"])
    types["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut"] = t.struct(
        {
            "locations": t.struct({"_": t.string().optional()}).optional(),
            "cloudProducts": t.struct({"_": t.string().optional()}).optional(),
            "resourceTypes": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "projectCount": t.integer().optional(),
            "resourceCount": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut"])
    types["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn"] = t.struct(
        {
            "googleCardCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
            "caviumCerts": t.array(t.string()).optional(),
        }
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn"])
    types["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut"] = t.struct(
        {
            "googleCardCerts": t.array(t.string()).optional(),
            "googlePartitionCerts": t.array(t.string()).optional(),
            "caviumCerts": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut"])
    types["GoogleCloudKmsInventoryV1ProtectedResourceIn"] = t.struct(
        {
            "cloudProduct": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "cryptoKeyVersion": t.string().optional(),
            "location": t.string().optional(),
            "cryptoKeyVersions": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourceIn"])
    types["GoogleCloudKmsInventoryV1ProtectedResourceOut"] = t.struct(
        {
            "cloudProduct": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "cryptoKeyVersion": t.string().optional(),
            "location": t.string().optional(),
            "cryptoKeyVersions": t.array(t.string()).optional(),
            "project": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourceOut"])
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

    functions = {}
    functions["organizationsProtectedResourcesSearch"] = kmsinventory.get(
        "v1/{scope}/protectedResources:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "cryptoKey": t.string(),
                "scope": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(
            renames["GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut"]
        ),
        auth_token_field="auth",
        content_type="application/json",
    )
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

    return Import(
        importer="kmsinventory",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
