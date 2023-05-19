from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_servicecontrol() -> Import:
    servicecontrol = HTTPRuntime("https://servicecontrol.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicecontrol_1_ErrorResponse",
        "StatusIn": "_servicecontrol_2_StatusIn",
        "StatusOut": "_servicecontrol_3_StatusOut",
        "PeerIn": "_servicecontrol_4_PeerIn",
        "PeerOut": "_servicecontrol_5_PeerOut",
        "AuthIn": "_servicecontrol_6_AuthIn",
        "AuthOut": "_servicecontrol_7_AuthOut",
        "AttributeContextIn": "_servicecontrol_8_AttributeContextIn",
        "AttributeContextOut": "_servicecontrol_9_AttributeContextOut",
        "ServiceAccountDelegationInfoIn": "_servicecontrol_10_ServiceAccountDelegationInfoIn",
        "ServiceAccountDelegationInfoOut": "_servicecontrol_11_ServiceAccountDelegationInfoOut",
        "ReportResponseIn": "_servicecontrol_12_ReportResponseIn",
        "ReportResponseOut": "_servicecontrol_13_ReportResponseOut",
        "AuthorizationInfoIn": "_servicecontrol_14_AuthorizationInfoIn",
        "AuthorizationInfoOut": "_servicecontrol_15_AuthorizationInfoOut",
        "ThirdPartyPrincipalIn": "_servicecontrol_16_ThirdPartyPrincipalIn",
        "ThirdPartyPrincipalOut": "_servicecontrol_17_ThirdPartyPrincipalOut",
        "ResourceIn": "_servicecontrol_18_ResourceIn",
        "ResourceOut": "_servicecontrol_19_ResourceOut",
        "ResourceLocationIn": "_servicecontrol_20_ResourceLocationIn",
        "ResourceLocationOut": "_servicecontrol_21_ResourceLocationOut",
        "V2LogEntrySourceLocationIn": "_servicecontrol_22_V2LogEntrySourceLocationIn",
        "V2LogEntrySourceLocationOut": "_servicecontrol_23_V2LogEntrySourceLocationOut",
        "FirstPartyPrincipalIn": "_servicecontrol_24_FirstPartyPrincipalIn",
        "FirstPartyPrincipalOut": "_servicecontrol_25_FirstPartyPrincipalOut",
        "RequestIn": "_servicecontrol_26_RequestIn",
        "RequestOut": "_servicecontrol_27_RequestOut",
        "CheckResponseIn": "_servicecontrol_28_CheckResponseIn",
        "CheckResponseOut": "_servicecontrol_29_CheckResponseOut",
        "ReportRequestIn": "_servicecontrol_30_ReportRequestIn",
        "ReportRequestOut": "_servicecontrol_31_ReportRequestOut",
        "AuthenticationInfoIn": "_servicecontrol_32_AuthenticationInfoIn",
        "AuthenticationInfoOut": "_servicecontrol_33_AuthenticationInfoOut",
        "ResponseIn": "_servicecontrol_34_ResponseIn",
        "ResponseOut": "_servicecontrol_35_ResponseOut",
        "V2LogEntryOperationIn": "_servicecontrol_36_V2LogEntryOperationIn",
        "V2LogEntryOperationOut": "_servicecontrol_37_V2LogEntryOperationOut",
        "RequestMetadataIn": "_servicecontrol_38_RequestMetadataIn",
        "RequestMetadataOut": "_servicecontrol_39_RequestMetadataOut",
        "CheckRequestIn": "_servicecontrol_40_CheckRequestIn",
        "CheckRequestOut": "_servicecontrol_41_CheckRequestOut",
        "OrgPolicyViolationInfoIn": "_servicecontrol_42_OrgPolicyViolationInfoIn",
        "OrgPolicyViolationInfoOut": "_servicecontrol_43_OrgPolicyViolationInfoOut",
        "V2HttpRequestIn": "_servicecontrol_44_V2HttpRequestIn",
        "V2HttpRequestOut": "_servicecontrol_45_V2HttpRequestOut",
        "ResourceInfoIn": "_servicecontrol_46_ResourceInfoIn",
        "ResourceInfoOut": "_servicecontrol_47_ResourceInfoOut",
        "ApiIn": "_servicecontrol_48_ApiIn",
        "ApiOut": "_servicecontrol_49_ApiOut",
        "SpanContextIn": "_servicecontrol_50_SpanContextIn",
        "SpanContextOut": "_servicecontrol_51_SpanContextOut",
        "ViolationInfoIn": "_servicecontrol_52_ViolationInfoIn",
        "ViolationInfoOut": "_servicecontrol_53_ViolationInfoOut",
        "AuditLogIn": "_servicecontrol_54_AuditLogIn",
        "AuditLogOut": "_servicecontrol_55_AuditLogOut",
        "PolicyViolationInfoIn": "_servicecontrol_56_PolicyViolationInfoIn",
        "PolicyViolationInfoOut": "_servicecontrol_57_PolicyViolationInfoOut",
        "V2LogEntryIn": "_servicecontrol_58_V2LogEntryIn",
        "V2LogEntryOut": "_servicecontrol_59_V2LogEntryOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["PeerIn"] = t.struct(
        {
            "ip": t.string().optional(),
            "regionCode": t.string().optional(),
            "port": t.string().optional(),
            "principal": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["PeerIn"])
    types["PeerOut"] = t.struct(
        {
            "ip": t.string().optional(),
            "regionCode": t.string().optional(),
            "port": t.string().optional(),
            "principal": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeerOut"])
    types["AuthIn"] = t.struct(
        {
            "claims": t.struct({"_": t.string().optional()}).optional(),
            "presenter": t.string().optional(),
            "accessLevels": t.array(t.string()).optional(),
            "principal": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
        }
    ).named(renames["AuthIn"])
    types["AuthOut"] = t.struct(
        {
            "claims": t.struct({"_": t.string().optional()}).optional(),
            "presenter": t.string().optional(),
            "accessLevels": t.array(t.string()).optional(),
            "principal": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthOut"])
    types["AttributeContextIn"] = t.struct(
        {
            "request": t.proxy(renames["RequestIn"]).optional(),
            "api": t.proxy(renames["ApiIn"]).optional(),
            "response": t.proxy(renames["ResponseIn"]).optional(),
            "source": t.proxy(renames["PeerIn"]).optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "origin": t.proxy(renames["PeerIn"]).optional(),
            "destination": t.proxy(renames["PeerIn"]).optional(),
        }
    ).named(renames["AttributeContextIn"])
    types["AttributeContextOut"] = t.struct(
        {
            "request": t.proxy(renames["RequestOut"]).optional(),
            "api": t.proxy(renames["ApiOut"]).optional(),
            "response": t.proxy(renames["ResponseOut"]).optional(),
            "source": t.proxy(renames["PeerOut"]).optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "origin": t.proxy(renames["PeerOut"]).optional(),
            "destination": t.proxy(renames["PeerOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeContextOut"])
    types["ServiceAccountDelegationInfoIn"] = t.struct(
        {
            "thirdPartyPrincipal": t.proxy(renames["ThirdPartyPrincipalIn"]).optional(),
            "firstPartyPrincipal": t.proxy(renames["FirstPartyPrincipalIn"]).optional(),
            "principalSubject": t.string().optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoIn"])
    types["ServiceAccountDelegationInfoOut"] = t.struct(
        {
            "thirdPartyPrincipal": t.proxy(
                renames["ThirdPartyPrincipalOut"]
            ).optional(),
            "firstPartyPrincipal": t.proxy(
                renames["FirstPartyPrincipalOut"]
            ).optional(),
            "principalSubject": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoOut"])
    types["ReportResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportResponseIn"]
    )
    types["ReportResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportResponseOut"])
    types["AuthorizationInfoIn"] = t.struct(
        {
            "permission": t.string().optional(),
            "resource": t.string().optional(),
            "granted": t.boolean().optional(),
            "resourceAttributes": t.proxy(renames["ResourceIn"]).optional(),
        }
    ).named(renames["AuthorizationInfoIn"])
    types["AuthorizationInfoOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "resource": t.string().optional(),
            "granted": t.boolean().optional(),
            "resourceAttributes": t.proxy(renames["ResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationInfoOut"])
    types["ThirdPartyPrincipalIn"] = t.struct(
        {"thirdPartyClaims": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ThirdPartyPrincipalIn"])
    types["ThirdPartyPrincipalOut"] = t.struct(
        {
            "thirdPartyClaims": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyPrincipalOut"])
    types["ResourceIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "uid": t.string().optional(),
            "location": t.string().optional(),
            "type": t.string().optional(),
            "updateTime": t.string().optional(),
            "service": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "uid": t.string().optional(),
            "location": t.string().optional(),
            "type": t.string().optional(),
            "updateTime": t.string().optional(),
            "service": t.string().optional(),
            "etag": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["ResourceLocationIn"] = t.struct(
        {
            "originalLocations": t.array(t.string()).optional(),
            "currentLocations": t.array(t.string()).optional(),
        }
    ).named(renames["ResourceLocationIn"])
    types["ResourceLocationOut"] = t.struct(
        {
            "originalLocations": t.array(t.string()).optional(),
            "currentLocations": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceLocationOut"])
    types["V2LogEntrySourceLocationIn"] = t.struct(
        {
            "line": t.string().optional(),
            "function": t.string().optional(),
            "file": t.string().optional(),
        }
    ).named(renames["V2LogEntrySourceLocationIn"])
    types["V2LogEntrySourceLocationOut"] = t.struct(
        {
            "line": t.string().optional(),
            "function": t.string().optional(),
            "file": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntrySourceLocationOut"])
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
    types["RequestIn"] = t.struct(
        {
            "size": t.string().optional(),
            "id": t.string().optional(),
            "scheme": t.string().optional(),
            "host": t.string().optional(),
            "auth": t.proxy(renames["AuthIn"]).optional(),
            "query": t.string().optional(),
            "protocol": t.string().optional(),
            "reason": t.string().optional(),
            "time": t.string().optional(),
            "path": t.string().optional(),
            "method": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "size": t.string().optional(),
            "id": t.string().optional(),
            "scheme": t.string().optional(),
            "host": t.string().optional(),
            "auth": t.proxy(renames["AuthOut"]).optional(),
            "query": t.string().optional(),
            "protocol": t.string().optional(),
            "reason": t.string().optional(),
            "time": t.string().optional(),
            "path": t.string().optional(),
            "method": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["CheckResponseIn"] = t.struct(
        {
            "status": t.proxy(renames["StatusIn"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["CheckResponseIn"])
    types["CheckResponseOut"] = t.struct(
        {
            "status": t.proxy(renames["StatusOut"]).optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckResponseOut"])
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
    types["AuthenticationInfoIn"] = t.struct(
        {
            "principalSubject": t.string().optional(),
            "principalEmail": t.string().optional(),
            "serviceAccountKeyName": t.string().optional(),
            "authoritySelector": t.string().optional(),
            "thirdPartyPrincipal": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoIn"])
            ).optional(),
        }
    ).named(renames["AuthenticationInfoIn"])
    types["AuthenticationInfoOut"] = t.struct(
        {
            "principalSubject": t.string().optional(),
            "principalEmail": t.string().optional(),
            "serviceAccountKeyName": t.string().optional(),
            "authoritySelector": t.string().optional(),
            "thirdPartyPrincipal": t.struct({"_": t.string().optional()}).optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationInfoOut"])
    types["ResponseIn"] = t.struct(
        {
            "time": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "backendLatency": t.string().optional(),
            "code": t.string().optional(),
            "size": t.string().optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "time": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "backendLatency": t.string().optional(),
            "code": t.string().optional(),
            "size": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["V2LogEntryOperationIn"] = t.struct(
        {
            "last": t.boolean().optional(),
            "producer": t.string().optional(),
            "id": t.string().optional(),
            "first": t.boolean().optional(),
        }
    ).named(renames["V2LogEntryOperationIn"])
    types["V2LogEntryOperationOut"] = t.struct(
        {
            "last": t.boolean().optional(),
            "producer": t.string().optional(),
            "id": t.string().optional(),
            "first": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntryOperationOut"])
    types["RequestMetadataIn"] = t.struct(
        {
            "callerNetwork": t.string().optional(),
            "callerIp": t.string().optional(),
            "requestAttributes": t.proxy(renames["RequestIn"]).optional(),
            "destinationAttributes": t.proxy(renames["PeerIn"]).optional(),
            "callerSuppliedUserAgent": t.string().optional(),
        }
    ).named(renames["RequestMetadataIn"])
    types["RequestMetadataOut"] = t.struct(
        {
            "callerNetwork": t.string().optional(),
            "callerIp": t.string().optional(),
            "requestAttributes": t.proxy(renames["RequestOut"]).optional(),
            "destinationAttributes": t.proxy(renames["PeerOut"]).optional(),
            "callerSuppliedUserAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestMetadataOut"])
    types["CheckRequestIn"] = t.struct(
        {
            "serviceConfigId": t.string().optional(),
            "attributes": t.proxy(renames["AttributeContextIn"]).optional(),
            "flags": t.string().optional(),
            "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
        }
    ).named(renames["CheckRequestIn"])
    types["CheckRequestOut"] = t.struct(
        {
            "serviceConfigId": t.string().optional(),
            "attributes": t.proxy(renames["AttributeContextOut"]).optional(),
            "flags": t.string().optional(),
            "resources": t.array(t.proxy(renames["ResourceInfoOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckRequestOut"])
    types["OrgPolicyViolationInfoIn"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "violationInfo": t.array(t.proxy(renames["ViolationInfoIn"])).optional(),
            "resourceTags": t.struct({"_": t.string().optional()}).optional(),
            "resourceType": t.string().optional(),
        }
    ).named(renames["OrgPolicyViolationInfoIn"])
    types["OrgPolicyViolationInfoOut"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "violationInfo": t.array(t.proxy(renames["ViolationInfoOut"])).optional(),
            "resourceTags": t.struct({"_": t.string().optional()}).optional(),
            "resourceType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgPolicyViolationInfoOut"])
    types["V2HttpRequestIn"] = t.struct(
        {
            "serverIp": t.string().optional(),
            "cacheFillBytes": t.string().optional(),
            "responseSize": t.string().optional(),
            "protocol": t.string().optional(),
            "remoteIp": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "userAgent": t.string().optional(),
            "requestUrl": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "referer": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "status": t.integer().optional(),
            "requestSize": t.string().optional(),
            "latency": t.string().optional(),
            "requestMethod": t.string().optional(),
        }
    ).named(renames["V2HttpRequestIn"])
    types["V2HttpRequestOut"] = t.struct(
        {
            "serverIp": t.string().optional(),
            "cacheFillBytes": t.string().optional(),
            "responseSize": t.string().optional(),
            "protocol": t.string().optional(),
            "remoteIp": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "userAgent": t.string().optional(),
            "requestUrl": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "referer": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "status": t.integer().optional(),
            "requestSize": t.string().optional(),
            "latency": t.string().optional(),
            "requestMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2HttpRequestOut"])
    types["ResourceInfoIn"] = t.struct(
        {
            "permission": t.string().optional(),
            "container": t.string().optional(),
            "location": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["ResourceInfoIn"])
    types["ResourceInfoOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "container": t.string().optional(),
            "location": t.string().optional(),
            "name": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceInfoOut"])
    types["ApiIn"] = t.struct(
        {
            "service": t.string().optional(),
            "operation": t.string().optional(),
            "protocol": t.string().optional(),
            "version": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "service": t.string().optional(),
            "operation": t.string().optional(),
            "protocol": t.string().optional(),
            "version": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["SpanContextIn"] = t.struct({"spanName": t.string().optional()}).named(
        renames["SpanContextIn"]
    )
    types["SpanContextOut"] = t.struct(
        {
            "spanName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanContextOut"])
    types["ViolationInfoIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "policyType": t.string().optional(),
            "constraint": t.string().optional(),
            "checkedValue": t.string().optional(),
        }
    ).named(renames["ViolationInfoIn"])
    types["ViolationInfoOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "policyType": t.string().optional(),
            "constraint": t.string().optional(),
            "checkedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolationInfoOut"])
    types["AuditLogIn"] = t.struct(
        {
            "methodName": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceLocation": t.proxy(renames["ResourceLocationIn"]).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "resourceOriginalState": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "numResponseItems": t.string().optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataIn"]).optional(),
            "serviceData": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "policyViolationInfo": t.proxy(renames["PolicyViolationInfoIn"]).optional(),
            "serviceName": t.string().optional(),
            "authorizationInfo": t.array(
                t.proxy(renames["AuthorizationInfoIn"])
            ).optional(),
            "authenticationInfo": t.proxy(renames["AuthenticationInfoIn"]).optional(),
        }
    ).named(renames["AuditLogIn"])
    types["AuditLogOut"] = t.struct(
        {
            "methodName": t.string().optional(),
            "resourceName": t.string().optional(),
            "resourceLocation": t.proxy(renames["ResourceLocationOut"]).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "resourceOriginalState": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "numResponseItems": t.string().optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataOut"]).optional(),
            "serviceData": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "policyViolationInfo": t.proxy(
                renames["PolicyViolationInfoOut"]
            ).optional(),
            "serviceName": t.string().optional(),
            "authorizationInfo": t.array(
                t.proxy(renames["AuthorizationInfoOut"])
            ).optional(),
            "authenticationInfo": t.proxy(renames["AuthenticationInfoOut"]).optional(),
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
    types["V2LogEntryIn"] = t.struct(
        {
            "structPayload": t.struct({"_": t.string().optional()}).optional(),
            "sourceLocation": t.proxy(renames["V2LogEntrySourceLocationIn"]).optional(),
            "httpRequest": t.proxy(renames["V2HttpRequestIn"]).optional(),
            "severity": t.string().optional(),
            "timestamp": t.string().optional(),
            "insertId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operation": t.proxy(renames["V2LogEntryOperationIn"]).optional(),
            "monitoredResourceLabels": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "name": t.string(),
            "textPayload": t.string().optional(),
            "trace": t.string().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["V2LogEntryIn"])
    types["V2LogEntryOut"] = t.struct(
        {
            "structPayload": t.struct({"_": t.string().optional()}).optional(),
            "sourceLocation": t.proxy(
                renames["V2LogEntrySourceLocationOut"]
            ).optional(),
            "httpRequest": t.proxy(renames["V2HttpRequestOut"]).optional(),
            "severity": t.string().optional(),
            "timestamp": t.string().optional(),
            "insertId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "operation": t.proxy(renames["V2LogEntryOperationOut"]).optional(),
            "monitoredResourceLabels": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "name": t.string(),
            "textPayload": t.string().optional(),
            "trace": t.string().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntryOut"])

    functions = {}
    functions["servicesReport"] = servicecontrol.post(
        "v2/services/{serviceName}:check",
        t.struct(
            {
                "serviceName": t.string().optional(),
                "serviceConfigId": t.string().optional(),
                "attributes": t.proxy(renames["AttributeContextIn"]).optional(),
                "flags": t.string().optional(),
                "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
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
                "serviceConfigId": t.string().optional(),
                "attributes": t.proxy(renames["AttributeContextIn"]).optional(),
                "flags": t.string().optional(),
                "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
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
