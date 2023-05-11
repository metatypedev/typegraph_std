from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_kmsinventory() -> Import:
    kmsinventory = HTTPRuntime("https://kmsinventory.googleapis.com/")

    renames = {
        "ErrorResponse": "_kmsinventory_1_ErrorResponse",
        "GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn": "_kmsinventory_2_GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseIn",
        "GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut": "_kmsinventory_3_GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseOut",
        "GoogleCloudKmsV1KeyOperationAttestationIn": "_kmsinventory_4_GoogleCloudKmsV1KeyOperationAttestationIn",
        "GoogleCloudKmsV1KeyOperationAttestationOut": "_kmsinventory_5_GoogleCloudKmsV1KeyOperationAttestationOut",
        "GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn": "_kmsinventory_6_GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn",
        "GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut": "_kmsinventory_7_GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut",
        "GoogleCloudKmsV1CryptoKeyVersionIn": "_kmsinventory_8_GoogleCloudKmsV1CryptoKeyVersionIn",
        "GoogleCloudKmsV1CryptoKeyVersionOut": "_kmsinventory_9_GoogleCloudKmsV1CryptoKeyVersionOut",
        "GoogleCloudKmsV1CryptoKeyVersionTemplateIn": "_kmsinventory_10_GoogleCloudKmsV1CryptoKeyVersionTemplateIn",
        "GoogleCloudKmsV1CryptoKeyVersionTemplateOut": "_kmsinventory_11_GoogleCloudKmsV1CryptoKeyVersionTemplateOut",
        "GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn": "_kmsinventory_12_GoogleCloudKmsV1KeyOperationAttestationCertificateChainsIn",
        "GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut": "_kmsinventory_13_GoogleCloudKmsV1KeyOperationAttestationCertificateChainsOut",
        "GoogleCloudKmsV1ExternalProtectionLevelOptionsIn": "_kmsinventory_14_GoogleCloudKmsV1ExternalProtectionLevelOptionsIn",
        "GoogleCloudKmsV1ExternalProtectionLevelOptionsOut": "_kmsinventory_15_GoogleCloudKmsV1ExternalProtectionLevelOptionsOut",
        "GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn": "_kmsinventory_16_GoogleCloudKmsInventoryV1ListCryptoKeysResponseIn",
        "GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut": "_kmsinventory_17_GoogleCloudKmsInventoryV1ListCryptoKeysResponseOut",
        "GoogleCloudKmsInventoryV1ProtectedResourceIn": "_kmsinventory_18_GoogleCloudKmsInventoryV1ProtectedResourceIn",
        "GoogleCloudKmsInventoryV1ProtectedResourceOut": "_kmsinventory_19_GoogleCloudKmsInventoryV1ProtectedResourceOut",
        "GoogleCloudKmsV1CryptoKeyIn": "_kmsinventory_20_GoogleCloudKmsV1CryptoKeyIn",
        "GoogleCloudKmsV1CryptoKeyOut": "_kmsinventory_21_GoogleCloudKmsV1CryptoKeyOut",
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
            "name": t.string().optional(),
            "resourceCount": t.string().optional(),
            "resourceTypes": t.struct({"_": t.string().optional()}).optional(),
            "cloudProducts": t.struct({"_": t.string().optional()}).optional(),
            "locations": t.struct({"_": t.string().optional()}).optional(),
            "projectCount": t.integer().optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryIn"])
    types["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut"] = t.struct(
        {
            "name": t.string().optional(),
            "resourceCount": t.string().optional(),
            "resourceTypes": t.struct({"_": t.string().optional()}).optional(),
            "cloudProducts": t.struct({"_": t.string().optional()}).optional(),
            "locations": t.struct({"_": t.string().optional()}).optional(),
            "projectCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourcesSummaryOut"])
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
            "destroyEventTime": t.string().optional(),
            "externalDestructionFailureReason": t.string().optional(),
            "importJob": t.string().optional(),
            "importTime": t.string().optional(),
            "algorithm": t.string().optional(),
            "destroyTime": t.string().optional(),
            "generateTime": t.string().optional(),
            "generationFailureReason": t.string().optional(),
            "protectionLevel": t.string().optional(),
            "externalProtectionLevelOptions": t.proxy(
                renames["GoogleCloudKmsV1ExternalProtectionLevelOptionsOut"]
            ).optional(),
            "state": t.string().optional(),
            "importFailureReason": t.string().optional(),
            "attestation": t.proxy(
                renames["GoogleCloudKmsV1KeyOperationAttestationOut"]
            ).optional(),
            "reimportEligible": t.boolean().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyVersionOut"])
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
    types["GoogleCloudKmsInventoryV1ProtectedResourceIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "cloudProduct": t.string().optional(),
            "cryptoKeyVersions": t.array(t.string()).optional(),
            "cryptoKeyVersion": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "location": t.string().optional(),
            "project": t.string().optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourceIn"])
    types["GoogleCloudKmsInventoryV1ProtectedResourceOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "createTime": t.string().optional(),
            "cloudProduct": t.string().optional(),
            "cryptoKeyVersions": t.array(t.string()).optional(),
            "cryptoKeyVersion": t.string().optional(),
            "name": t.string().optional(),
            "projectId": t.string().optional(),
            "location": t.string().optional(),
            "project": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsInventoryV1ProtectedResourceOut"])
    types["GoogleCloudKmsV1CryptoKeyIn"] = t.struct(
        {
            "rotationPeriod": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nextRotationTime": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
            "versionTemplate": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionTemplateIn"]
            ).optional(),
            "cryptoKeyBackend": t.string().optional(),
            "purpose": t.string().optional(),
            "importOnly": t.boolean().optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyIn"])
    types["GoogleCloudKmsV1CryptoKeyOut"] = t.struct(
        {
            "rotationPeriod": t.string().optional(),
            "primary": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionOut"]
            ).optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "nextRotationTime": t.string().optional(),
            "destroyScheduledDuration": t.string().optional(),
            "versionTemplate": t.proxy(
                renames["GoogleCloudKmsV1CryptoKeyVersionTemplateOut"]
            ).optional(),
            "name": t.string().optional(),
            "cryptoKeyBackend": t.string().optional(),
            "purpose": t.string().optional(),
            "importOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleCloudKmsV1CryptoKeyOut"])

    functions = {}
    functions["organizationsProtectedResourcesSearch"] = kmsinventory.get(
        "v1/{scope}/protectedResources:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "scope": t.string(),
                "cryptoKey": t.string(),
                "pageToken": t.string().optional(),
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
        importer="kmsinventory", renames=renames, types=types, functions=functions
    )
