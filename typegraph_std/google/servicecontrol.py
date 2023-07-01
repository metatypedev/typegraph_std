from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_servicecontrol():
    servicecontrol = HTTPRuntime("https://servicecontrol.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicecontrol_1_ErrorResponse",
        "OrgPolicyViolationInfoIn": "_servicecontrol_2_OrgPolicyViolationInfoIn",
        "OrgPolicyViolationInfoOut": "_servicecontrol_3_OrgPolicyViolationInfoOut",
        "ReportResponseIn": "_servicecontrol_4_ReportResponseIn",
        "ReportResponseOut": "_servicecontrol_5_ReportResponseOut",
        "CheckRequestIn": "_servicecontrol_6_CheckRequestIn",
        "CheckRequestOut": "_servicecontrol_7_CheckRequestOut",
        "RequestMetadataIn": "_servicecontrol_8_RequestMetadataIn",
        "RequestMetadataOut": "_servicecontrol_9_RequestMetadataOut",
        "CheckResponseIn": "_servicecontrol_10_CheckResponseIn",
        "CheckResponseOut": "_servicecontrol_11_CheckResponseOut",
        "RequestIn": "_servicecontrol_12_RequestIn",
        "RequestOut": "_servicecontrol_13_RequestOut",
        "ServiceAccountDelegationInfoIn": "_servicecontrol_14_ServiceAccountDelegationInfoIn",
        "ServiceAccountDelegationInfoOut": "_servicecontrol_15_ServiceAccountDelegationInfoOut",
        "AuthorizationInfoIn": "_servicecontrol_16_AuthorizationInfoIn",
        "AuthorizationInfoOut": "_servicecontrol_17_AuthorizationInfoOut",
        "AuditLogIn": "_servicecontrol_18_AuditLogIn",
        "AuditLogOut": "_servicecontrol_19_AuditLogOut",
        "PolicyViolationInfoIn": "_servicecontrol_20_PolicyViolationInfoIn",
        "PolicyViolationInfoOut": "_servicecontrol_21_PolicyViolationInfoOut",
        "AuthIn": "_servicecontrol_22_AuthIn",
        "AuthOut": "_servicecontrol_23_AuthOut",
        "ResourceInfoIn": "_servicecontrol_24_ResourceInfoIn",
        "ResourceInfoOut": "_servicecontrol_25_ResourceInfoOut",
        "FirstPartyPrincipalIn": "_servicecontrol_26_FirstPartyPrincipalIn",
        "FirstPartyPrincipalOut": "_servicecontrol_27_FirstPartyPrincipalOut",
        "ThirdPartyPrincipalIn": "_servicecontrol_28_ThirdPartyPrincipalIn",
        "ThirdPartyPrincipalOut": "_servicecontrol_29_ThirdPartyPrincipalOut",
        "ReportRequestIn": "_servicecontrol_30_ReportRequestIn",
        "ReportRequestOut": "_servicecontrol_31_ReportRequestOut",
        "PeerIn": "_servicecontrol_32_PeerIn",
        "PeerOut": "_servicecontrol_33_PeerOut",
        "ViolationInfoIn": "_servicecontrol_34_ViolationInfoIn",
        "ViolationInfoOut": "_servicecontrol_35_ViolationInfoOut",
        "SpanContextIn": "_servicecontrol_36_SpanContextIn",
        "SpanContextOut": "_servicecontrol_37_SpanContextOut",
        "AuthenticationInfoIn": "_servicecontrol_38_AuthenticationInfoIn",
        "AuthenticationInfoOut": "_servicecontrol_39_AuthenticationInfoOut",
        "StatusIn": "_servicecontrol_40_StatusIn",
        "StatusOut": "_servicecontrol_41_StatusOut",
        "AttributeContextIn": "_servicecontrol_42_AttributeContextIn",
        "AttributeContextOut": "_servicecontrol_43_AttributeContextOut",
        "ApiIn": "_servicecontrol_44_ApiIn",
        "ApiOut": "_servicecontrol_45_ApiOut",
        "V2LogEntryIn": "_servicecontrol_46_V2LogEntryIn",
        "V2LogEntryOut": "_servicecontrol_47_V2LogEntryOut",
        "V2LogEntrySourceLocationIn": "_servicecontrol_48_V2LogEntrySourceLocationIn",
        "V2LogEntrySourceLocationOut": "_servicecontrol_49_V2LogEntrySourceLocationOut",
        "V2LogEntryOperationIn": "_servicecontrol_50_V2LogEntryOperationIn",
        "V2LogEntryOperationOut": "_servicecontrol_51_V2LogEntryOperationOut",
        "ResponseIn": "_servicecontrol_52_ResponseIn",
        "ResponseOut": "_servicecontrol_53_ResponseOut",
        "V2HttpRequestIn": "_servicecontrol_54_V2HttpRequestIn",
        "V2HttpRequestOut": "_servicecontrol_55_V2HttpRequestOut",
        "ResourceLocationIn": "_servicecontrol_56_ResourceLocationIn",
        "ResourceLocationOut": "_servicecontrol_57_ResourceLocationOut",
        "ResourceIn": "_servicecontrol_58_ResourceIn",
        "ResourceOut": "_servicecontrol_59_ResourceOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["OrgPolicyViolationInfoIn"] = t.struct(
        {
            "violationInfo": t.array(t.proxy(renames["ViolationInfoIn"])).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "resourceTags": t.struct({"_": t.string().optional()}).optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["OrgPolicyViolationInfoIn"])
    types["OrgPolicyViolationInfoOut"] = t.struct(
        {
            "violationInfo": t.array(t.proxy(renames["ViolationInfoOut"])).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "resourceTags": t.struct({"_": t.string().optional()}).optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgPolicyViolationInfoOut"])
    types["ReportResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportResponseIn"]
    )
    types["ReportResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportResponseOut"])
    types["CheckRequestIn"] = t.struct(
        {
            "flags": t.string().optional(),
            "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
            "serviceConfigId": t.string().optional(),
            "attributes": t.proxy(renames["AttributeContextIn"]).optional(),
        }
    ).named(renames["CheckRequestIn"])
    types["CheckRequestOut"] = t.struct(
        {
            "flags": t.string().optional(),
            "resources": t.array(t.proxy(renames["ResourceInfoOut"])).optional(),
            "serviceConfigId": t.string().optional(),
            "attributes": t.proxy(renames["AttributeContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckRequestOut"])
    types["RequestMetadataIn"] = t.struct(
        {
            "requestAttributes": t.proxy(renames["RequestIn"]).optional(),
            "callerNetwork": t.string().optional(),
            "callerSuppliedUserAgent": t.string().optional(),
            "destinationAttributes": t.proxy(renames["PeerIn"]).optional(),
            "callerIp": t.string().optional(),
        }
    ).named(renames["RequestMetadataIn"])
    types["RequestMetadataOut"] = t.struct(
        {
            "requestAttributes": t.proxy(renames["RequestOut"]).optional(),
            "callerNetwork": t.string().optional(),
            "callerSuppliedUserAgent": t.string().optional(),
            "destinationAttributes": t.proxy(renames["PeerOut"]).optional(),
            "callerIp": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestMetadataOut"])
    types["CheckResponseIn"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["CheckResponseIn"])
    types["CheckResponseOut"] = t.struct(
        {
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckResponseOut"])
    types["RequestIn"] = t.struct(
        {
            "scheme": t.string().optional(),
            "query": t.string().optional(),
            "method": t.string().optional(),
            "host": t.string().optional(),
            "reason": t.string().optional(),
            "path": t.string().optional(),
            "time": t.string().optional(),
            "protocol": t.string().optional(),
            "auth": t.proxy(renames["AuthIn"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "size": t.string().optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "scheme": t.string().optional(),
            "query": t.string().optional(),
            "method": t.string().optional(),
            "host": t.string().optional(),
            "reason": t.string().optional(),
            "path": t.string().optional(),
            "time": t.string().optional(),
            "protocol": t.string().optional(),
            "auth": t.proxy(renames["AuthOut"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "size": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["ServiceAccountDelegationInfoIn"] = t.struct(
        {
            "firstPartyPrincipal": t.proxy(renames["FirstPartyPrincipalIn"]).optional(),
            "thirdPartyPrincipal": t.proxy(renames["ThirdPartyPrincipalIn"]).optional(),
            "principalSubject": t.string().optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoIn"])
    types["ServiceAccountDelegationInfoOut"] = t.struct(
        {
            "firstPartyPrincipal": t.proxy(
                renames["FirstPartyPrincipalOut"]
            ).optional(),
            "thirdPartyPrincipal": t.proxy(
                renames["ThirdPartyPrincipalOut"]
            ).optional(),
            "principalSubject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoOut"])
    types["AuthorizationInfoIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "permission": t.string().optional(),
            "resourceAttributes": t.proxy(renames["ResourceIn"]).optional(),
            "granted": t.boolean().optional(),
        }
    ).named(renames["AuthorizationInfoIn"])
    types["AuthorizationInfoOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "permission": t.string().optional(),
            "resourceAttributes": t.proxy(renames["ResourceOut"]).optional(),
            "granted": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationInfoOut"])
    types["AuditLogIn"] = t.struct(
        {
            "policyViolationInfo": t.proxy(renames["PolicyViolationInfoIn"]).optional(),
            "serviceName": t.string().optional(),
            "numResponseItems": t.string().optional(),
            "resourceLocation": t.proxy(renames["ResourceLocationIn"]).optional(),
            "authorizationInfo": t.array(
                t.proxy(renames["AuthorizationInfoIn"])
            ).optional(),
            "methodName": t.string().optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataIn"]).optional(),
            "serviceData": t.struct({"_": t.string().optional()}).optional(),
            "authenticationInfo": t.proxy(renames["AuthenticationInfoIn"]).optional(),
            "resourceOriginalState": t.struct({"_": t.string().optional()}).optional(),
            "resourceName": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AuditLogIn"])
    types["AuditLogOut"] = t.struct(
        {
            "policyViolationInfo": t.proxy(
                renames["PolicyViolationInfoOut"]
            ).optional(),
            "serviceName": t.string().optional(),
            "numResponseItems": t.string().optional(),
            "resourceLocation": t.proxy(renames["ResourceLocationOut"]).optional(),
            "authorizationInfo": t.array(
                t.proxy(renames["AuthorizationInfoOut"])
            ).optional(),
            "methodName": t.string().optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataOut"]).optional(),
            "serviceData": t.struct({"_": t.string().optional()}).optional(),
            "authenticationInfo": t.proxy(renames["AuthenticationInfoOut"]).optional(),
            "resourceOriginalState": t.struct({"_": t.string().optional()}).optional(),
            "resourceName": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogOut"])
    types["PolicyViolationInfoIn"] = t.struct(
        {
            "orgPolicyViolationInfo": t.proxy(
                renames["OrgPolicyViolationInfoIn"]
            ).optional()
        }
    ).named(renames["PolicyViolationInfoIn"])
    types["PolicyViolationInfoOut"] = t.struct(
        {
            "orgPolicyViolationInfo": t.proxy(
                renames["OrgPolicyViolationInfoOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyViolationInfoOut"])
    types["AuthIn"] = t.struct(
        {
            "accessLevels": t.array(t.string()).optional(),
            "audiences": t.array(t.string()).optional(),
            "principal": t.string().optional(),
            "presenter": t.string().optional(),
            "claims": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AuthIn"])
    types["AuthOut"] = t.struct(
        {
            "accessLevels": t.array(t.string()).optional(),
            "audiences": t.array(t.string()).optional(),
            "principal": t.string().optional(),
            "presenter": t.string().optional(),
            "claims": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthOut"])
    types["ResourceInfoIn"] = t.struct(
        {
            "location": t.string().optional(),
            "type": t.string().optional(),
            "permission": t.string().optional(),
            "name": t.string().optional(),
            "container": t.string().optional(),
        }
    ).named(renames["ResourceInfoIn"])
    types["ResourceInfoOut"] = t.struct(
        {
            "location": t.string().optional(),
            "type": t.string().optional(),
            "permission": t.string().optional(),
            "name": t.string().optional(),
            "container": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceInfoOut"])
    types["FirstPartyPrincipalIn"] = t.struct(
        {
            "principalEmail": t.string().optional(),
            "serviceMetadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["FirstPartyPrincipalIn"])
    types["FirstPartyPrincipalOut"] = t.struct(
        {
            "principalEmail": t.string().optional(),
            "serviceMetadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FirstPartyPrincipalOut"])
    types["ThirdPartyPrincipalIn"] = t.struct(
        {"thirdPartyClaims": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ThirdPartyPrincipalIn"])
    types["ThirdPartyPrincipalOut"] = t.struct(
        {
            "thirdPartyClaims": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyPrincipalOut"])
    types["ReportRequestIn"] = t.struct(
        {
            "serviceConfigId": t.string().optional(),
            "operations": t.array(t.proxy(renames["AttributeContextIn"])).optional(),
        }
    ).named(renames["ReportRequestIn"])
    types["ReportRequestOut"] = t.struct(
        {
            "serviceConfigId": t.string().optional(),
            "operations": t.array(t.proxy(renames["AttributeContextOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRequestOut"])
    types["PeerIn"] = t.struct(
        {
            "ip": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "principal": t.string().optional(),
            "port": t.string().optional(),
            "regionCode": t.string().optional(),
        }
    ).named(renames["PeerIn"])
    types["PeerOut"] = t.struct(
        {
            "ip": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "principal": t.string().optional(),
            "port": t.string().optional(),
            "regionCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeerOut"])
    types["ViolationInfoIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "checkedValue": t.string().optional(),
            "policyType": t.string().optional(),
            "constraint": t.string().optional(),
        }
    ).named(renames["ViolationInfoIn"])
    types["ViolationInfoOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "checkedValue": t.string().optional(),
            "policyType": t.string().optional(),
            "constraint": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolationInfoOut"])
    types["SpanContextIn"] = t.struct({"spanName": t.string().optional()}).named(
        renames["SpanContextIn"]
    )
    types["SpanContextOut"] = t.struct(
        {
            "spanName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanContextOut"])
    types["AuthenticationInfoIn"] = t.struct(
        {
            "principalEmail": t.string().optional(),
            "thirdPartyPrincipal": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountKeyName": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoIn"])
            ).optional(),
            "authoritySelector": t.string().optional(),
            "principalSubject": t.string().optional(),
        }
    ).named(renames["AuthenticationInfoIn"])
    types["AuthenticationInfoOut"] = t.struct(
        {
            "principalEmail": t.string().optional(),
            "thirdPartyPrincipal": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountKeyName": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoOut"])
            ).optional(),
            "authoritySelector": t.string().optional(),
            "principalSubject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationInfoOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AttributeContextIn"] = t.struct(
        {
            "request": t.proxy(renames["RequestIn"]).optional(),
            "origin": t.proxy(renames["PeerIn"]).optional(),
            "destination": t.proxy(renames["PeerIn"]).optional(),
            "api": t.proxy(renames["ApiIn"]).optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "response": t.proxy(renames["ResponseIn"]).optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "source": t.proxy(renames["PeerIn"]).optional(),
        }
    ).named(renames["AttributeContextIn"])
    types["AttributeContextOut"] = t.struct(
        {
            "request": t.proxy(renames["RequestOut"]).optional(),
            "origin": t.proxy(renames["PeerOut"]).optional(),
            "destination": t.proxy(renames["PeerOut"]).optional(),
            "api": t.proxy(renames["ApiOut"]).optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "response": t.proxy(renames["ResponseOut"]).optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "source": t.proxy(renames["PeerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeContextOut"])
    types["ApiIn"] = t.struct(
        {
            "protocol": t.string().optional(),
            "service": t.string().optional(),
            "version": t.string().optional(),
            "operation": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "protocol": t.string().optional(),
            "service": t.string().optional(),
            "version": t.string().optional(),
            "operation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["V2LogEntryIn"] = t.struct(
        {
            "operation": t.proxy(renames["V2LogEntryOperationIn"]).optional(),
            "sourceLocation": t.proxy(renames["V2LogEntrySourceLocationIn"]).optional(),
            "severity": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "httpRequest": t.proxy(renames["V2HttpRequestIn"]).optional(),
            "monitoredResourceLabels": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "trace": t.string().optional(),
            "structPayload": t.struct({"_": t.string().optional()}).optional(),
            "timestamp": t.string().optional(),
            "textPayload": t.string().optional(),
            "insertId": t.string().optional(),
        }
    ).named(renames["V2LogEntryIn"])
    types["V2LogEntryOut"] = t.struct(
        {
            "operation": t.proxy(renames["V2LogEntryOperationOut"]).optional(),
            "sourceLocation": t.proxy(
                renames["V2LogEntrySourceLocationOut"]
            ).optional(),
            "severity": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "httpRequest": t.proxy(renames["V2HttpRequestOut"]).optional(),
            "monitoredResourceLabels": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "trace": t.string().optional(),
            "structPayload": t.struct({"_": t.string().optional()}).optional(),
            "timestamp": t.string().optional(),
            "textPayload": t.string().optional(),
            "insertId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntryOut"])
    types["V2LogEntrySourceLocationIn"] = t.struct(
        {
            "file": t.string().optional(),
            "line": t.string().optional(),
            "function": t.string().optional(),
        }
    ).named(renames["V2LogEntrySourceLocationIn"])
    types["V2LogEntrySourceLocationOut"] = t.struct(
        {
            "file": t.string().optional(),
            "line": t.string().optional(),
            "function": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntrySourceLocationOut"])
    types["V2LogEntryOperationIn"] = t.struct(
        {
            "last": t.boolean().optional(),
            "producer": t.string().optional(),
            "first": t.boolean().optional(),
            "id": t.string().optional(),
        }
    ).named(renames["V2LogEntryOperationIn"])
    types["V2LogEntryOperationOut"] = t.struct(
        {
            "last": t.boolean().optional(),
            "producer": t.string().optional(),
            "first": t.boolean().optional(),
            "id": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntryOperationOut"])
    types["ResponseIn"] = t.struct(
        {
            "size": t.string().optional(),
            "time": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "code": t.string().optional(),
            "backendLatency": t.string().optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "size": t.string().optional(),
            "time": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "code": t.string().optional(),
            "backendLatency": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["V2HttpRequestIn"] = t.struct(
        {
            "status": t.integer().optional(),
            "protocol": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "cacheFillBytes": t.string().optional(),
            "requestUrl": t.string().optional(),
            "userAgent": t.string().optional(),
            "remoteIp": t.string().optional(),
            "requestSize": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "serverIp": t.string().optional(),
            "referer": t.string().optional(),
            "responseSize": t.string().optional(),
            "latency": t.string().optional(),
            "requestMethod": t.string().optional(),
        }
    ).named(renames["V2HttpRequestIn"])
    types["V2HttpRequestOut"] = t.struct(
        {
            "status": t.integer().optional(),
            "protocol": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "cacheFillBytes": t.string().optional(),
            "requestUrl": t.string().optional(),
            "userAgent": t.string().optional(),
            "remoteIp": t.string().optional(),
            "requestSize": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "serverIp": t.string().optional(),
            "referer": t.string().optional(),
            "responseSize": t.string().optional(),
            "latency": t.string().optional(),
            "requestMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2HttpRequestOut"])
    types["ResourceLocationIn"] = t.struct(
        {
            "currentLocations": t.array(t.string()).optional(),
            "originalLocations": t.array(t.string()).optional(),
        }
    ).named(renames["ResourceLocationIn"])
    types["ResourceLocationOut"] = t.struct(
        {
            "currentLocations": t.array(t.string()).optional(),
            "originalLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLocationOut"])
    types["ResourceIn"] = t.struct(
        {
            "location": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "service": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "location": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "uid": t.string().optional(),
            "service": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])

    functions = {}
    functions["servicesReport"] = servicecontrol.post(
        "v2/services/{serviceName}:check",
        t.struct(
            {
                "serviceName": t.string().optional(),
                "flags": t.string().optional(),
                "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
                "serviceConfigId": t.string().optional(),
                "attributes": t.proxy(renames["AttributeContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesCheck"] = servicecontrol.post(
        "v2/services/{serviceName}:check",
        t.struct(
            {
                "serviceName": t.string().optional(),
                "flags": t.string().optional(),
                "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
                "serviceConfigId": t.string().optional(),
                "attributes": t.proxy(renames["AttributeContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="servicecontrol",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
