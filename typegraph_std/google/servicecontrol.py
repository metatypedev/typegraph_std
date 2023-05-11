from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_servicecontrol() -> Import:
    servicecontrol = HTTPRuntime("https://servicecontrol.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicecontrol_1_ErrorResponse",
        "ResponseIn": "_servicecontrol_2_ResponseIn",
        "ResponseOut": "_servicecontrol_3_ResponseOut",
        "AuthorizationInfoIn": "_servicecontrol_4_AuthorizationInfoIn",
        "AuthorizationInfoOut": "_servicecontrol_5_AuthorizationInfoOut",
        "ServiceAccountDelegationInfoIn": "_servicecontrol_6_ServiceAccountDelegationInfoIn",
        "ServiceAccountDelegationInfoOut": "_servicecontrol_7_ServiceAccountDelegationInfoOut",
        "ApiIn": "_servicecontrol_8_ApiIn",
        "ApiOut": "_servicecontrol_9_ApiOut",
        "AttributeContextIn": "_servicecontrol_10_AttributeContextIn",
        "AttributeContextOut": "_servicecontrol_11_AttributeContextOut",
        "ResourceInfoIn": "_servicecontrol_12_ResourceInfoIn",
        "ResourceInfoOut": "_servicecontrol_13_ResourceInfoOut",
        "ViolationInfoIn": "_servicecontrol_14_ViolationInfoIn",
        "ViolationInfoOut": "_servicecontrol_15_ViolationInfoOut",
        "ResourceLocationIn": "_servicecontrol_16_ResourceLocationIn",
        "ResourceLocationOut": "_servicecontrol_17_ResourceLocationOut",
        "AuthIn": "_servicecontrol_18_AuthIn",
        "AuthOut": "_servicecontrol_19_AuthOut",
        "ResourceIn": "_servicecontrol_20_ResourceIn",
        "ResourceOut": "_servicecontrol_21_ResourceOut",
        "ReportResponseIn": "_servicecontrol_22_ReportResponseIn",
        "ReportResponseOut": "_servicecontrol_23_ReportResponseOut",
        "V2LogEntryIn": "_servicecontrol_24_V2LogEntryIn",
        "V2LogEntryOut": "_servicecontrol_25_V2LogEntryOut",
        "CheckRequestIn": "_servicecontrol_26_CheckRequestIn",
        "CheckRequestOut": "_servicecontrol_27_CheckRequestOut",
        "SpanContextIn": "_servicecontrol_28_SpanContextIn",
        "SpanContextOut": "_servicecontrol_29_SpanContextOut",
        "FirstPartyPrincipalIn": "_servicecontrol_30_FirstPartyPrincipalIn",
        "FirstPartyPrincipalOut": "_servicecontrol_31_FirstPartyPrincipalOut",
        "V2LogEntryOperationIn": "_servicecontrol_32_V2LogEntryOperationIn",
        "V2LogEntryOperationOut": "_servicecontrol_33_V2LogEntryOperationOut",
        "OrgPolicyViolationInfoIn": "_servicecontrol_34_OrgPolicyViolationInfoIn",
        "OrgPolicyViolationInfoOut": "_servicecontrol_35_OrgPolicyViolationInfoOut",
        "CheckResponseIn": "_servicecontrol_36_CheckResponseIn",
        "CheckResponseOut": "_servicecontrol_37_CheckResponseOut",
        "StatusIn": "_servicecontrol_38_StatusIn",
        "StatusOut": "_servicecontrol_39_StatusOut",
        "AuthenticationInfoIn": "_servicecontrol_40_AuthenticationInfoIn",
        "AuthenticationInfoOut": "_servicecontrol_41_AuthenticationInfoOut",
        "PeerIn": "_servicecontrol_42_PeerIn",
        "PeerOut": "_servicecontrol_43_PeerOut",
        "ThirdPartyPrincipalIn": "_servicecontrol_44_ThirdPartyPrincipalIn",
        "ThirdPartyPrincipalOut": "_servicecontrol_45_ThirdPartyPrincipalOut",
        "AuditLogIn": "_servicecontrol_46_AuditLogIn",
        "AuditLogOut": "_servicecontrol_47_AuditLogOut",
        "PolicyViolationInfoIn": "_servicecontrol_48_PolicyViolationInfoIn",
        "PolicyViolationInfoOut": "_servicecontrol_49_PolicyViolationInfoOut",
        "V2LogEntrySourceLocationIn": "_servicecontrol_50_V2LogEntrySourceLocationIn",
        "V2LogEntrySourceLocationOut": "_servicecontrol_51_V2LogEntrySourceLocationOut",
        "V2HttpRequestIn": "_servicecontrol_52_V2HttpRequestIn",
        "V2HttpRequestOut": "_servicecontrol_53_V2HttpRequestOut",
        "RequestIn": "_servicecontrol_54_RequestIn",
        "RequestOut": "_servicecontrol_55_RequestOut",
        "RequestMetadataIn": "_servicecontrol_56_RequestMetadataIn",
        "RequestMetadataOut": "_servicecontrol_57_RequestMetadataOut",
        "ReportRequestIn": "_servicecontrol_58_ReportRequestIn",
        "ReportRequestOut": "_servicecontrol_59_ReportRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ResponseIn"] = t.struct(
        {
            "size": t.string().optional(),
            "backendLatency": t.string().optional(),
            "code": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "time": t.string().optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "size": t.string().optional(),
            "backendLatency": t.string().optional(),
            "code": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "time": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["AuthorizationInfoIn"] = t.struct(
        {
            "resource": t.string().optional(),
            "permission": t.string().optional(),
            "granted": t.boolean().optional(),
            "resourceAttributes": t.proxy(renames["ResourceIn"]).optional(),
        }
    ).named(renames["AuthorizationInfoIn"])
    types["AuthorizationInfoOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "permission": t.string().optional(),
            "granted": t.boolean().optional(),
            "resourceAttributes": t.proxy(renames["ResourceOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationInfoOut"])
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
    types["ApiIn"] = t.struct(
        {
            "protocol": t.string().optional(),
            "operation": t.string().optional(),
            "version": t.string().optional(),
            "service": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "protocol": t.string().optional(),
            "operation": t.string().optional(),
            "version": t.string().optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["AttributeContextIn"] = t.struct(
        {
            "origin": t.proxy(renames["PeerIn"]).optional(),
            "source": t.proxy(renames["PeerIn"]).optional(),
            "request": t.proxy(renames["RequestIn"]).optional(),
            "destination": t.proxy(renames["PeerIn"]).optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "response": t.proxy(renames["ResponseIn"]).optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "api": t.proxy(renames["ApiIn"]).optional(),
        }
    ).named(renames["AttributeContextIn"])
    types["AttributeContextOut"] = t.struct(
        {
            "origin": t.proxy(renames["PeerOut"]).optional(),
            "source": t.proxy(renames["PeerOut"]).optional(),
            "request": t.proxy(renames["RequestOut"]).optional(),
            "destination": t.proxy(renames["PeerOut"]).optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "response": t.proxy(renames["ResponseOut"]).optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "api": t.proxy(renames["ApiOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeContextOut"])
    types["ResourceInfoIn"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "container": t.string().optional(),
            "location": t.string().optional(),
            "permission": t.string().optional(),
        }
    ).named(renames["ResourceInfoIn"])
    types["ResourceInfoOut"] = t.struct(
        {
            "name": t.string().optional(),
            "type": t.string().optional(),
            "container": t.string().optional(),
            "location": t.string().optional(),
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceInfoOut"])
    types["ViolationInfoIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "constraint": t.string().optional(),
            "policyType": t.string().optional(),
            "checkedValue": t.string().optional(),
        }
    ).named(renames["ViolationInfoIn"])
    types["ViolationInfoOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "constraint": t.string().optional(),
            "policyType": t.string().optional(),
            "checkedValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolationInfoOut"])
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
    types["AuthIn"] = t.struct(
        {
            "principal": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
            "claims": t.struct({"_": t.string().optional()}).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "presenter": t.string().optional(),
        }
    ).named(renames["AuthIn"])
    types["AuthOut"] = t.struct(
        {
            "principal": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
            "claims": t.struct({"_": t.string().optional()}).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "presenter": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthOut"])
    types["ResourceIn"] = t.struct(
        {
            "service": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "deleteTime": t.string().optional(),
            "uid": t.string().optional(),
            "etag": t.string().optional(),
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "service": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "deleteTime": t.string().optional(),
            "uid": t.string().optional(),
            "etag": t.string().optional(),
            "type": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
    types["ReportResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportResponseIn"]
    )
    types["ReportResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportResponseOut"])
    types["V2LogEntryIn"] = t.struct(
        {
            "structPayload": t.struct({"_": t.string().optional()}).optional(),
            "trace": t.string().optional(),
            "severity": t.string().optional(),
            "operation": t.proxy(renames["V2LogEntryOperationIn"]).optional(),
            "name": t.string(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "monitoredResourceLabels": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sourceLocation": t.proxy(renames["V2LogEntrySourceLocationIn"]).optional(),
            "timestamp": t.string().optional(),
            "httpRequest": t.proxy(renames["V2HttpRequestIn"]).optional(),
            "textPayload": t.string().optional(),
            "insertId": t.string().optional(),
        }
    ).named(renames["V2LogEntryIn"])
    types["V2LogEntryOut"] = t.struct(
        {
            "structPayload": t.struct({"_": t.string().optional()}).optional(),
            "trace": t.string().optional(),
            "severity": t.string().optional(),
            "operation": t.proxy(renames["V2LogEntryOperationOut"]).optional(),
            "name": t.string(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "monitoredResourceLabels": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sourceLocation": t.proxy(
                renames["V2LogEntrySourceLocationOut"]
            ).optional(),
            "timestamp": t.string().optional(),
            "httpRequest": t.proxy(renames["V2HttpRequestOut"]).optional(),
            "textPayload": t.string().optional(),
            "insertId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntryOut"])
    types["CheckRequestIn"] = t.struct(
        {
            "flags": t.string().optional(),
            "serviceConfigId": t.string().optional(),
            "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
            "attributes": t.proxy(renames["AttributeContextIn"]).optional(),
        }
    ).named(renames["CheckRequestIn"])
    types["CheckRequestOut"] = t.struct(
        {
            "flags": t.string().optional(),
            "serviceConfigId": t.string().optional(),
            "resources": t.array(t.proxy(renames["ResourceInfoOut"])).optional(),
            "attributes": t.proxy(renames["AttributeContextOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckRequestOut"])
    types["SpanContextIn"] = t.struct({"spanName": t.string().optional()}).named(
        renames["SpanContextIn"]
    )
    types["SpanContextOut"] = t.struct(
        {
            "spanName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanContextOut"])
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
    types["V2LogEntryOperationIn"] = t.struct(
        {
            "id": t.string().optional(),
            "first": t.boolean().optional(),
            "producer": t.string().optional(),
            "last": t.boolean().optional(),
        }
    ).named(renames["V2LogEntryOperationIn"])
    types["V2LogEntryOperationOut"] = t.struct(
        {
            "id": t.string().optional(),
            "first": t.boolean().optional(),
            "producer": t.string().optional(),
            "last": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntryOperationOut"])
    types["OrgPolicyViolationInfoIn"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "violationInfo": t.array(t.proxy(renames["ViolationInfoIn"])).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "resourceTags": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OrgPolicyViolationInfoIn"])
    types["OrgPolicyViolationInfoOut"] = t.struct(
        {
            "resourceType": t.string().optional(),
            "violationInfo": t.array(t.proxy(renames["ViolationInfoOut"])).optional(),
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "resourceTags": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgPolicyViolationInfoOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AuthenticationInfoIn"] = t.struct(
        {
            "serviceAccountKeyName": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoIn"])
            ).optional(),
            "authoritySelector": t.string().optional(),
            "principalSubject": t.string().optional(),
            "thirdPartyPrincipal": t.struct({"_": t.string().optional()}).optional(),
            "principalEmail": t.string().optional(),
        }
    ).named(renames["AuthenticationInfoIn"])
    types["AuthenticationInfoOut"] = t.struct(
        {
            "serviceAccountKeyName": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoOut"])
            ).optional(),
            "authoritySelector": t.string().optional(),
            "principalSubject": t.string().optional(),
            "thirdPartyPrincipal": t.struct({"_": t.string().optional()}).optional(),
            "principalEmail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationInfoOut"])
    types["PeerIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "port": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "principal": t.string().optional(),
            "ip": t.string().optional(),
        }
    ).named(renames["PeerIn"])
    types["PeerOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "port": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "principal": t.string().optional(),
            "ip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeerOut"])
    types["ThirdPartyPrincipalIn"] = t.struct(
        {"thirdPartyClaims": t.struct({"_": t.string().optional()}).optional()}
    ).named(renames["ThirdPartyPrincipalIn"])
    types["ThirdPartyPrincipalOut"] = t.struct(
        {
            "thirdPartyClaims": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ThirdPartyPrincipalOut"])
    types["AuditLogIn"] = t.struct(
        {
            "policyViolationInfo": t.proxy(renames["PolicyViolationInfoIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "authenticationInfo": t.proxy(renames["AuthenticationInfoIn"]).optional(),
            "serviceName": t.string().optional(),
            "methodName": t.string().optional(),
            "resourceOriginalState": t.struct({"_": t.string().optional()}).optional(),
            "authorizationInfo": t.array(
                t.proxy(renames["AuthorizationInfoIn"])
            ).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "resourceName": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataIn"]).optional(),
            "numResponseItems": t.string().optional(),
            "resourceLocation": t.proxy(renames["ResourceLocationIn"]).optional(),
            "serviceData": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AuditLogIn"])
    types["AuditLogOut"] = t.struct(
        {
            "policyViolationInfo": t.proxy(
                renames["PolicyViolationInfoOut"]
            ).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "authenticationInfo": t.proxy(renames["AuthenticationInfoOut"]).optional(),
            "serviceName": t.string().optional(),
            "methodName": t.string().optional(),
            "resourceOriginalState": t.struct({"_": t.string().optional()}).optional(),
            "authorizationInfo": t.array(
                t.proxy(renames["AuthorizationInfoOut"])
            ).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "resourceName": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataOut"]).optional(),
            "numResponseItems": t.string().optional(),
            "resourceLocation": t.proxy(renames["ResourceLocationOut"]).optional(),
            "serviceData": t.struct({"_": t.string().optional()}).optional(),
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
    types["V2HttpRequestIn"] = t.struct(
        {
            "cacheFillBytes": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "referer": t.string().optional(),
            "protocol": t.string().optional(),
            "latency": t.string().optional(),
            "requestUrl": t.string().optional(),
            "serverIp": t.string().optional(),
            "requestSize": t.string().optional(),
            "remoteIp": t.string().optional(),
            "responseSize": t.string().optional(),
            "status": t.integer().optional(),
            "requestMethod": t.string().optional(),
            "userAgent": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "cacheHit": t.boolean().optional(),
        }
    ).named(renames["V2HttpRequestIn"])
    types["V2HttpRequestOut"] = t.struct(
        {
            "cacheFillBytes": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "referer": t.string().optional(),
            "protocol": t.string().optional(),
            "latency": t.string().optional(),
            "requestUrl": t.string().optional(),
            "serverIp": t.string().optional(),
            "requestSize": t.string().optional(),
            "remoteIp": t.string().optional(),
            "responseSize": t.string().optional(),
            "status": t.integer().optional(),
            "requestMethod": t.string().optional(),
            "userAgent": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "cacheHit": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2HttpRequestOut"])
    types["RequestIn"] = t.struct(
        {
            "size": t.string().optional(),
            "host": t.string().optional(),
            "time": t.string().optional(),
            "scheme": t.string().optional(),
            "path": t.string().optional(),
            "protocol": t.string().optional(),
            "id": t.string().optional(),
            "method": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "reason": t.string().optional(),
            "query": t.string().optional(),
            "auth": t.proxy(renames["AuthIn"]).optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "size": t.string().optional(),
            "host": t.string().optional(),
            "time": t.string().optional(),
            "scheme": t.string().optional(),
            "path": t.string().optional(),
            "protocol": t.string().optional(),
            "id": t.string().optional(),
            "method": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "reason": t.string().optional(),
            "query": t.string().optional(),
            "auth": t.proxy(renames["AuthOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["RequestMetadataIn"] = t.struct(
        {
            "requestAttributes": t.proxy(renames["RequestIn"]).optional(),
            "callerIp": t.string().optional(),
            "destinationAttributes": t.proxy(renames["PeerIn"]).optional(),
            "callerNetwork": t.string().optional(),
            "callerSuppliedUserAgent": t.string().optional(),
        }
    ).named(renames["RequestMetadataIn"])
    types["RequestMetadataOut"] = t.struct(
        {
            "requestAttributes": t.proxy(renames["RequestOut"]).optional(),
            "callerIp": t.string().optional(),
            "destinationAttributes": t.proxy(renames["PeerOut"]).optional(),
            "callerNetwork": t.string().optional(),
            "callerSuppliedUserAgent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestMetadataOut"])
    types["ReportRequestIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["AttributeContextIn"])).optional(),
            "serviceConfigId": t.string().optional(),
        }
    ).named(renames["ReportRequestIn"])
    types["ReportRequestOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["AttributeContextOut"])).optional(),
            "serviceConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReportRequestOut"])

    functions = {}
    functions["servicesReport"] = servicecontrol.post(
        "v2/services/{serviceName}:check",
        t.struct(
            {
                "serviceName": t.string().optional(),
                "flags": t.string().optional(),
                "serviceConfigId": t.string().optional(),
                "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
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
                "serviceConfigId": t.string().optional(),
                "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
                "attributes": t.proxy(renames["AttributeContextIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["CheckResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="servicecontrol", renames=renames, types=types, functions=functions
    )
