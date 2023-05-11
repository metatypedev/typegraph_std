from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_verifiedaccess() -> Import:
    verifiedaccess = HTTPRuntime("https://verifiedaccess.googleapis.com/")

    renames = {
        "ErrorResponse": "_verifiedaccess_1_ErrorResponse",
        "EmptyIn": "_verifiedaccess_2_EmptyIn",
        "EmptyOut": "_verifiedaccess_3_EmptyOut",
        "CrowdStrikeAgentIn": "_verifiedaccess_4_CrowdStrikeAgentIn",
        "CrowdStrikeAgentOut": "_verifiedaccess_5_CrowdStrikeAgentOut",
        "DeviceSignalsIn": "_verifiedaccess_6_DeviceSignalsIn",
        "DeviceSignalsOut": "_verifiedaccess_7_DeviceSignalsOut",
        "ChallengeIn": "_verifiedaccess_8_ChallengeIn",
        "ChallengeOut": "_verifiedaccess_9_ChallengeOut",
        "VerifyChallengeResponseRequestIn": "_verifiedaccess_10_VerifyChallengeResponseRequestIn",
        "VerifyChallengeResponseRequestOut": "_verifiedaccess_11_VerifyChallengeResponseRequestOut",
        "VerifyChallengeResponseResultIn": "_verifiedaccess_12_VerifyChallengeResponseResultIn",
        "VerifyChallengeResponseResultOut": "_verifiedaccess_13_VerifyChallengeResponseResultOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CrowdStrikeAgentIn"] = t.struct(
        {"agentId": t.string().optional(), "customerId": t.string().optional()}
    ).named(renames["CrowdStrikeAgentIn"])
    types["CrowdStrikeAgentOut"] = t.struct(
        {
            "agentId": t.string().optional(),
            "customerId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrowdStrikeAgentOut"])
    types["DeviceSignalsIn"] = t.struct(
        {
            "crowdStrikeAgent": t.proxy(renames["CrowdStrikeAgentIn"]).optional(),
            "safeBrowsingProtectionLevel": t.string().optional(),
            "systemDnsServers": t.array(t.string()).optional(),
            "osVersion": t.string().optional(),
            "allowScreenLock": t.boolean().optional(),
            "deviceModel": t.string().optional(),
            "builtInDnsClientEnabled": t.boolean().optional(),
            "browserVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "deviceManufacturer": t.string().optional(),
            "realtimeUrlCheckMode": t.string().optional(),
            "hostname": t.string().optional(),
            "screenLockSecured": t.string().optional(),
            "serialNumber": t.string().optional(),
            "meid": t.array(t.string()).optional(),
            "imei": t.array(t.string()).optional(),
            "profileAffiliationIds": t.array(t.string()).optional(),
            "thirdPartyBlockingEnabled": t.boolean().optional(),
            "passwordProtectionWarningTrigger": t.string().optional(),
            "macAddresses": t.array(t.string()).optional(),
            "operatingSystem": t.string().optional(),
            "windowsMachineDomain": t.string().optional(),
            "deviceEnrollmentDomain": t.string().optional(),
            "siteIsolationEnabled": t.boolean().optional(),
            "osFirewall": t.string().optional(),
            "windowsUserDomain": t.string().optional(),
            "secureBootMode": t.string().optional(),
            "diskEncryption": t.string().optional(),
            "deviceAffiliationIds": t.array(t.string()).optional(),
            "chromeRemoteDesktopAppBlocked": t.boolean().optional(),
        }
    ).named(renames["DeviceSignalsIn"])
    types["DeviceSignalsOut"] = t.struct(
        {
            "crowdStrikeAgent": t.proxy(renames["CrowdStrikeAgentOut"]).optional(),
            "safeBrowsingProtectionLevel": t.string().optional(),
            "systemDnsServers": t.array(t.string()).optional(),
            "osVersion": t.string().optional(),
            "allowScreenLock": t.boolean().optional(),
            "deviceModel": t.string().optional(),
            "builtInDnsClientEnabled": t.boolean().optional(),
            "browserVersion": t.string().optional(),
            "displayName": t.string().optional(),
            "deviceManufacturer": t.string().optional(),
            "realtimeUrlCheckMode": t.string().optional(),
            "hostname": t.string().optional(),
            "screenLockSecured": t.string().optional(),
            "serialNumber": t.string().optional(),
            "meid": t.array(t.string()).optional(),
            "imei": t.array(t.string()).optional(),
            "profileAffiliationIds": t.array(t.string()).optional(),
            "thirdPartyBlockingEnabled": t.boolean().optional(),
            "passwordProtectionWarningTrigger": t.string().optional(),
            "macAddresses": t.array(t.string()).optional(),
            "operatingSystem": t.string().optional(),
            "windowsMachineDomain": t.string().optional(),
            "deviceEnrollmentDomain": t.string().optional(),
            "siteIsolationEnabled": t.boolean().optional(),
            "osFirewall": t.string().optional(),
            "windowsUserDomain": t.string().optional(),
            "secureBootMode": t.string().optional(),
            "diskEncryption": t.string().optional(),
            "deviceAffiliationIds": t.array(t.string()).optional(),
            "chromeRemoteDesktopAppBlocked": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSignalsOut"])
    types["ChallengeIn"] = t.struct({"challenge": t.string().optional()}).named(
        renames["ChallengeIn"]
    )
    types["ChallengeOut"] = t.struct(
        {
            "challenge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChallengeOut"])
    types["VerifyChallengeResponseRequestIn"] = t.struct(
        {"challengeResponse": t.string(), "expectedIdentity": t.string().optional()}
    ).named(renames["VerifyChallengeResponseRequestIn"])
    types["VerifyChallengeResponseRequestOut"] = t.struct(
        {
            "challengeResponse": t.string(),
            "expectedIdentity": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyChallengeResponseRequestOut"])
    types["VerifyChallengeResponseResultIn"] = t.struct(
        {
            "devicePermanentId": t.string().optional(),
            "customerId": t.string().optional(),
            "keyTrustLevel": t.string().optional(),
            "virtualDeviceId": t.string().optional(),
            "signedPublicKeyAndChallenge": t.string().optional(),
            "deviceSignals": t.proxy(renames["DeviceSignalsIn"]).optional(),
            "deviceSignal": t.string().optional(),
        }
    ).named(renames["VerifyChallengeResponseResultIn"])
    types["VerifyChallengeResponseResultOut"] = t.struct(
        {
            "devicePermanentId": t.string().optional(),
            "customerId": t.string().optional(),
            "keyTrustLevel": t.string().optional(),
            "virtualDeviceId": t.string().optional(),
            "signedPublicKeyAndChallenge": t.string().optional(),
            "deviceSignals": t.proxy(renames["DeviceSignalsOut"]).optional(),
            "deviceSignal": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyChallengeResponseResultOut"])

    functions = {}
    functions["challengeGenerate"] = verifiedaccess.post(
        "v2/challenge:verify",
        t.struct(
            {
                "challengeResponse": t.string(),
                "expectedIdentity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VerifyChallengeResponseResultOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["challengeVerify"] = verifiedaccess.post(
        "v2/challenge:verify",
        t.struct(
            {
                "challengeResponse": t.string(),
                "expectedIdentity": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VerifyChallengeResponseResultOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="verifiedaccess", renames=renames, types=types, functions=functions
    )
