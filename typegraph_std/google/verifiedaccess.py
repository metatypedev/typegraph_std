from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_verifiedaccess():
    verifiedaccess = HTTPRuntime("https://verifiedaccess.googleapis.com/")

    renames = {
        "ErrorResponse": "_verifiedaccess_1_ErrorResponse",
        "CrowdStrikeAgentIn": "_verifiedaccess_2_CrowdStrikeAgentIn",
        "CrowdStrikeAgentOut": "_verifiedaccess_3_CrowdStrikeAgentOut",
        "DeviceSignalsIn": "_verifiedaccess_4_DeviceSignalsIn",
        "DeviceSignalsOut": "_verifiedaccess_5_DeviceSignalsOut",
        "EmptyIn": "_verifiedaccess_6_EmptyIn",
        "EmptyOut": "_verifiedaccess_7_EmptyOut",
        "VerifyChallengeResponseResultIn": "_verifiedaccess_8_VerifyChallengeResponseResultIn",
        "VerifyChallengeResponseResultOut": "_verifiedaccess_9_VerifyChallengeResponseResultOut",
        "ChallengeIn": "_verifiedaccess_10_ChallengeIn",
        "ChallengeOut": "_verifiedaccess_11_ChallengeOut",
        "VerifyChallengeResponseRequestIn": "_verifiedaccess_12_VerifyChallengeResponseRequestIn",
        "VerifyChallengeResponseRequestOut": "_verifiedaccess_13_VerifyChallengeResponseRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
            "screenLockSecured": t.string().optional(),
            "windowsMachineDomain": t.string().optional(),
            "browserVersion": t.string().optional(),
            "operatingSystem": t.string().optional(),
            "deviceModel": t.string().optional(),
            "windowsUserDomain": t.string().optional(),
            "diskEncryption": t.string().optional(),
            "meid": t.array(t.string()).optional(),
            "serialNumber": t.string().optional(),
            "chromeRemoteDesktopAppBlocked": t.boolean().optional(),
            "safeBrowsingProtectionLevel": t.string().optional(),
            "thirdPartyBlockingEnabled": t.boolean().optional(),
            "macAddresses": t.array(t.string()).optional(),
            "osVersion": t.string().optional(),
            "osFirewall": t.string().optional(),
            "crowdStrikeAgent": t.proxy(renames["CrowdStrikeAgentIn"]).optional(),
            "trigger": t.string().optional(),
            "systemDnsServers": t.array(t.string()).optional(),
            "secureBootMode": t.string().optional(),
            "deviceManufacturer": t.string().optional(),
            "builtInDnsClientEnabled": t.boolean().optional(),
            "deviceAffiliationIds": t.array(t.string()).optional(),
            "hostname": t.string().optional(),
            "realtimeUrlCheckMode": t.string().optional(),
            "imei": t.array(t.string()).optional(),
            "siteIsolationEnabled": t.boolean().optional(),
            "deviceEnrollmentDomain": t.string().optional(),
            "displayName": t.string().optional(),
            "profileAffiliationIds": t.array(t.string()).optional(),
            "passwordProtectionWarningTrigger": t.string().optional(),
            "allowScreenLock": t.boolean().optional(),
        }
    ).named(renames["DeviceSignalsIn"])
    types["DeviceSignalsOut"] = t.struct(
        {
            "screenLockSecured": t.string().optional(),
            "windowsMachineDomain": t.string().optional(),
            "browserVersion": t.string().optional(),
            "operatingSystem": t.string().optional(),
            "deviceModel": t.string().optional(),
            "windowsUserDomain": t.string().optional(),
            "diskEncryption": t.string().optional(),
            "meid": t.array(t.string()).optional(),
            "serialNumber": t.string().optional(),
            "chromeRemoteDesktopAppBlocked": t.boolean().optional(),
            "safeBrowsingProtectionLevel": t.string().optional(),
            "thirdPartyBlockingEnabled": t.boolean().optional(),
            "macAddresses": t.array(t.string()).optional(),
            "osVersion": t.string().optional(),
            "osFirewall": t.string().optional(),
            "crowdStrikeAgent": t.proxy(renames["CrowdStrikeAgentOut"]).optional(),
            "trigger": t.string().optional(),
            "systemDnsServers": t.array(t.string()).optional(),
            "secureBootMode": t.string().optional(),
            "deviceManufacturer": t.string().optional(),
            "builtInDnsClientEnabled": t.boolean().optional(),
            "deviceAffiliationIds": t.array(t.string()).optional(),
            "hostname": t.string().optional(),
            "realtimeUrlCheckMode": t.string().optional(),
            "imei": t.array(t.string()).optional(),
            "siteIsolationEnabled": t.boolean().optional(),
            "deviceEnrollmentDomain": t.string().optional(),
            "displayName": t.string().optional(),
            "profileAffiliationIds": t.array(t.string()).optional(),
            "passwordProtectionWarningTrigger": t.string().optional(),
            "allowScreenLock": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSignalsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["VerifyChallengeResponseResultIn"] = t.struct(
        {
            "virtualDeviceId": t.string().optional(),
            "virtualProfileId": t.string().optional(),
            "signedPublicKeyAndChallenge": t.string().optional(),
            "customerId": t.string().optional(),
            "deviceSignals": t.proxy(renames["DeviceSignalsIn"]).optional(),
            "keyTrustLevel": t.string().optional(),
            "profileCustomerId": t.string().optional(),
            "profileKeyTrustLevel": t.string().optional(),
            "deviceSignal": t.string().optional(),
            "devicePermanentId": t.string().optional(),
        }
    ).named(renames["VerifyChallengeResponseResultIn"])
    types["VerifyChallengeResponseResultOut"] = t.struct(
        {
            "virtualDeviceId": t.string().optional(),
            "virtualProfileId": t.string().optional(),
            "signedPublicKeyAndChallenge": t.string().optional(),
            "customerId": t.string().optional(),
            "deviceSignals": t.proxy(renames["DeviceSignalsOut"]).optional(),
            "keyTrustLevel": t.string().optional(),
            "profileCustomerId": t.string().optional(),
            "profileKeyTrustLevel": t.string().optional(),
            "deviceSignal": t.string().optional(),
            "devicePermanentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyChallengeResponseResultOut"])
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

    functions = {}
    functions["challengeVerify"] = verifiedaccess.post(
        "v2/challenge:generate",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ChallengeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["challengeGenerate"] = verifiedaccess.post(
        "v2/challenge:generate",
        t.struct({"_": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["ChallengeOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="verifiedaccess",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
