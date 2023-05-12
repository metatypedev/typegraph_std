from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_verifiedaccess() -> Import:
    verifiedaccess = HTTPRuntime("https://verifiedaccess.googleapis.com/")

    renames = {
        "ErrorResponse": "_verifiedaccess_1_ErrorResponse",
        "VerifyChallengeResponseResultIn": "_verifiedaccess_2_VerifyChallengeResponseResultIn",
        "VerifyChallengeResponseResultOut": "_verifiedaccess_3_VerifyChallengeResponseResultOut",
        "DeviceSignalsIn": "_verifiedaccess_4_DeviceSignalsIn",
        "DeviceSignalsOut": "_verifiedaccess_5_DeviceSignalsOut",
        "EmptyIn": "_verifiedaccess_6_EmptyIn",
        "EmptyOut": "_verifiedaccess_7_EmptyOut",
        "CrowdStrikeAgentIn": "_verifiedaccess_8_CrowdStrikeAgentIn",
        "CrowdStrikeAgentOut": "_verifiedaccess_9_CrowdStrikeAgentOut",
        "VerifyChallengeResponseRequestIn": "_verifiedaccess_10_VerifyChallengeResponseRequestIn",
        "VerifyChallengeResponseRequestOut": "_verifiedaccess_11_VerifyChallengeResponseRequestOut",
        "ChallengeIn": "_verifiedaccess_12_ChallengeIn",
        "ChallengeOut": "_verifiedaccess_13_ChallengeOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["VerifyChallengeResponseResultIn"] = t.struct(
        {
            "deviceSignals": t.proxy(renames["DeviceSignalsIn"]).optional(),
            "signedPublicKeyAndChallenge": t.string().optional(),
            "customerId": t.string().optional(),
            "keyTrustLevel": t.string().optional(),
            "devicePermanentId": t.string().optional(),
            "deviceSignal": t.string().optional(),
            "virtualDeviceId": t.string().optional(),
        }
    ).named(renames["VerifyChallengeResponseResultIn"])
    types["VerifyChallengeResponseResultOut"] = t.struct(
        {
            "deviceSignals": t.proxy(renames["DeviceSignalsOut"]).optional(),
            "signedPublicKeyAndChallenge": t.string().optional(),
            "customerId": t.string().optional(),
            "keyTrustLevel": t.string().optional(),
            "devicePermanentId": t.string().optional(),
            "deviceSignal": t.string().optional(),
            "virtualDeviceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VerifyChallengeResponseResultOut"])
    types["DeviceSignalsIn"] = t.struct(
        {
            "deviceModel": t.string().optional(),
            "displayName": t.string().optional(),
            "realtimeUrlCheckMode": t.string().optional(),
            "windowsMachineDomain": t.string().optional(),
            "hostname": t.string().optional(),
            "systemDnsServers": t.array(t.string()).optional(),
            "osFirewall": t.string().optional(),
            "crowdStrikeAgent": t.proxy(renames["CrowdStrikeAgentIn"]).optional(),
            "meid": t.array(t.string()).optional(),
            "deviceManufacturer": t.string().optional(),
            "screenLockSecured": t.string().optional(),
            "secureBootMode": t.string().optional(),
            "deviceAffiliationIds": t.array(t.string()).optional(),
            "windowsUserDomain": t.string().optional(),
            "safeBrowsingProtectionLevel": t.string().optional(),
            "macAddresses": t.array(t.string()).optional(),
            "profileAffiliationIds": t.array(t.string()).optional(),
            "passwordProtectionWarningTrigger": t.string().optional(),
            "thirdPartyBlockingEnabled": t.boolean().optional(),
            "allowScreenLock": t.boolean().optional(),
            "siteIsolationEnabled": t.boolean().optional(),
            "operatingSystem": t.string().optional(),
            "chromeRemoteDesktopAppBlocked": t.boolean().optional(),
            "serialNumber": t.string().optional(),
            "browserVersion": t.string().optional(),
            "builtInDnsClientEnabled": t.boolean().optional(),
            "diskEncryption": t.string().optional(),
            "deviceEnrollmentDomain": t.string().optional(),
            "imei": t.array(t.string()).optional(),
            "osVersion": t.string().optional(),
        }
    ).named(renames["DeviceSignalsIn"])
    types["DeviceSignalsOut"] = t.struct(
        {
            "deviceModel": t.string().optional(),
            "displayName": t.string().optional(),
            "realtimeUrlCheckMode": t.string().optional(),
            "windowsMachineDomain": t.string().optional(),
            "hostname": t.string().optional(),
            "systemDnsServers": t.array(t.string()).optional(),
            "osFirewall": t.string().optional(),
            "crowdStrikeAgent": t.proxy(renames["CrowdStrikeAgentOut"]).optional(),
            "meid": t.array(t.string()).optional(),
            "deviceManufacturer": t.string().optional(),
            "screenLockSecured": t.string().optional(),
            "secureBootMode": t.string().optional(),
            "deviceAffiliationIds": t.array(t.string()).optional(),
            "windowsUserDomain": t.string().optional(),
            "safeBrowsingProtectionLevel": t.string().optional(),
            "macAddresses": t.array(t.string()).optional(),
            "profileAffiliationIds": t.array(t.string()).optional(),
            "passwordProtectionWarningTrigger": t.string().optional(),
            "thirdPartyBlockingEnabled": t.boolean().optional(),
            "allowScreenLock": t.boolean().optional(),
            "siteIsolationEnabled": t.boolean().optional(),
            "operatingSystem": t.string().optional(),
            "chromeRemoteDesktopAppBlocked": t.boolean().optional(),
            "serialNumber": t.string().optional(),
            "browserVersion": t.string().optional(),
            "builtInDnsClientEnabled": t.boolean().optional(),
            "diskEncryption": t.string().optional(),
            "deviceEnrollmentDomain": t.string().optional(),
            "imei": t.array(t.string()).optional(),
            "osVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DeviceSignalsOut"])
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
    types["ChallengeIn"] = t.struct({"challenge": t.string().optional()}).named(
        renames["ChallengeIn"]
    )
    types["ChallengeOut"] = t.struct(
        {
            "challenge": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ChallengeOut"])

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
        importer="verifiedaccess",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
