from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_verifiedaccess() -> Import:
    verifiedaccess = HTTPRuntime("https://verifiedaccess.googleapis.com/")

    renames = {
        "ErrorResponse": "_verifiedaccess_1_ErrorResponse",
        "ChallengeIn": "_verifiedaccess_2_ChallengeIn",
        "ChallengeOut": "_verifiedaccess_3_ChallengeOut",
        "VerifyChallengeResponseResultIn": "_verifiedaccess_4_VerifyChallengeResponseResultIn",
        "VerifyChallengeResponseResultOut": "_verifiedaccess_5_VerifyChallengeResponseResultOut",
        "EmptyIn": "_verifiedaccess_6_EmptyIn",
        "EmptyOut": "_verifiedaccess_7_EmptyOut",
        "CrowdStrikeAgentIn": "_verifiedaccess_8_CrowdStrikeAgentIn",
        "CrowdStrikeAgentOut": "_verifiedaccess_9_CrowdStrikeAgentOut",
        "DeviceSignalsIn": "_verifiedaccess_10_DeviceSignalsIn",
        "DeviceSignalsOut": "_verifiedaccess_11_DeviceSignalsOut",
        "VerifyChallengeResponseRequestIn": "_verifiedaccess_12_VerifyChallengeResponseRequestIn",
        "VerifyChallengeResponseRequestOut": "_verifiedaccess_13_VerifyChallengeResponseRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ChallengeIn"] = t.struct({"challenge": t.string().optional()}).named(
        renames["ChallengeIn"]
    )
    types["ChallengeOut"] = t.struct(
        {
            "challenge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChallengeOut"])
    types["VerifyChallengeResponseResultIn"] = t.struct(
        {
            "signedPublicKeyAndChallenge": t.string().optional(),
            "deviceSignals": t.proxy(renames["DeviceSignalsIn"]).optional(),
            "deviceSignal": t.string().optional(),
            "customerId": t.string().optional(),
            "keyTrustLevel": t.string().optional(),
            "devicePermanentId": t.string().optional(),
            "virtualDeviceId": t.string().optional(),
        }
    ).named(renames["VerifyChallengeResponseResultIn"])
    types["VerifyChallengeResponseResultOut"] = t.struct(
        {
            "signedPublicKeyAndChallenge": t.string().optional(),
            "deviceSignals": t.proxy(renames["DeviceSignalsOut"]).optional(),
            "deviceSignal": t.string().optional(),
            "customerId": t.string().optional(),
            "keyTrustLevel": t.string().optional(),
            "devicePermanentId": t.string().optional(),
            "virtualDeviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyChallengeResponseResultOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["CrowdStrikeAgentIn"] = t.struct(
        {"customerId": t.string().optional(), "agentId": t.string().optional()}
    ).named(renames["CrowdStrikeAgentIn"])
    types["CrowdStrikeAgentOut"] = t.struct(
        {
            "customerId": t.string().optional(),
            "agentId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CrowdStrikeAgentOut"])
    types["DeviceSignalsIn"] = t.struct(
        {
            "realtimeUrlCheckMode": t.string().optional(),
            "imei": t.array(t.string()).optional(),
            "deviceAffiliationIds": t.array(t.string()).optional(),
            "systemDnsServers": t.array(t.string()).optional(),
            "crowdStrikeAgent": t.proxy(renames["CrowdStrikeAgentIn"]).optional(),
            "deviceManufacturer": t.string().optional(),
            "diskEncryption": t.string().optional(),
            "osFirewall": t.string().optional(),
            "displayName": t.string().optional(),
            "passwordProtectionWarningTrigger": t.string().optional(),
            "chromeRemoteDesktopAppBlocked": t.boolean().optional(),
            "secureBootMode": t.string().optional(),
            "operatingSystem": t.string().optional(),
            "browserVersion": t.string().optional(),
            "thirdPartyBlockingEnabled": t.boolean().optional(),
            "windowsUserDomain": t.string().optional(),
            "deviceEnrollmentDomain": t.string().optional(),
            "profileAffiliationIds": t.array(t.string()).optional(),
            "builtInDnsClientEnabled": t.boolean().optional(),
            "deviceModel": t.string().optional(),
            "allowScreenLock": t.boolean().optional(),
            "windowsMachineDomain": t.string().optional(),
            "meid": t.array(t.string()).optional(),
            "siteIsolationEnabled": t.boolean().optional(),
            "safeBrowsingProtectionLevel": t.string().optional(),
            "osVersion": t.string().optional(),
            "hostname": t.string().optional(),
            "macAddresses": t.array(t.string()).optional(),
            "screenLockSecured": t.string().optional(),
            "serialNumber": t.string().optional(),
        }
    ).named(renames["DeviceSignalsIn"])
    types["DeviceSignalsOut"] = t.struct(
        {
            "realtimeUrlCheckMode": t.string().optional(),
            "imei": t.array(t.string()).optional(),
            "deviceAffiliationIds": t.array(t.string()).optional(),
            "systemDnsServers": t.array(t.string()).optional(),
            "crowdStrikeAgent": t.proxy(renames["CrowdStrikeAgentOut"]).optional(),
            "deviceManufacturer": t.string().optional(),
            "diskEncryption": t.string().optional(),
            "osFirewall": t.string().optional(),
            "displayName": t.string().optional(),
            "passwordProtectionWarningTrigger": t.string().optional(),
            "chromeRemoteDesktopAppBlocked": t.boolean().optional(),
            "secureBootMode": t.string().optional(),
            "operatingSystem": t.string().optional(),
            "browserVersion": t.string().optional(),
            "thirdPartyBlockingEnabled": t.boolean().optional(),
            "windowsUserDomain": t.string().optional(),
            "deviceEnrollmentDomain": t.string().optional(),
            "profileAffiliationIds": t.array(t.string()).optional(),
            "builtInDnsClientEnabled": t.boolean().optional(),
            "deviceModel": t.string().optional(),
            "allowScreenLock": t.boolean().optional(),
            "windowsMachineDomain": t.string().optional(),
            "meid": t.array(t.string()).optional(),
            "siteIsolationEnabled": t.boolean().optional(),
            "safeBrowsingProtectionLevel": t.string().optional(),
            "osVersion": t.string().optional(),
            "hostname": t.string().optional(),
            "macAddresses": t.array(t.string()).optional(),
            "screenLockSecured": t.string().optional(),
            "serialNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSignalsOut"])
    types["VerifyChallengeResponseRequestIn"] = t.struct(
        {"expectedIdentity": t.string().optional(), "challengeResponse": t.string()}
    ).named(renames["VerifyChallengeResponseRequestIn"])
    types["VerifyChallengeResponseRequestOut"] = t.struct(
        {
            "expectedIdentity": t.string().optional(),
            "challengeResponse": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyChallengeResponseRequestOut"])

    functions = {}
    functions["challengeGenerate"] = verifiedaccess.post(
        "v2/challenge:verify",
        t.struct(
            {
                "expectedIdentity": t.string().optional(),
                "challengeResponse": t.string(),
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
                "expectedIdentity": t.string().optional(),
                "challengeResponse": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["VerifyChallengeResponseResultOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="verifiedaccess",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
