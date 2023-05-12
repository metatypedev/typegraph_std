from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_servicecontrol() -> Import:
    servicecontrol = HTTPRuntime("https://servicecontrol.googleapis.com/")

    renames = {
        "ErrorResponse": "_servicecontrol_1_ErrorResponse",
        "AuthorizationInfoIn": "_servicecontrol_2_AuthorizationInfoIn",
        "AuthorizationInfoOut": "_servicecontrol_3_AuthorizationInfoOut",
        "ResourceLocationIn": "_servicecontrol_4_ResourceLocationIn",
        "ResourceLocationOut": "_servicecontrol_5_ResourceLocationOut",
        "ServiceAccountDelegationInfoIn": "_servicecontrol_6_ServiceAccountDelegationInfoIn",
        "ServiceAccountDelegationInfoOut": "_servicecontrol_7_ServiceAccountDelegationInfoOut",
        "OrgPolicyViolationInfoIn": "_servicecontrol_8_OrgPolicyViolationInfoIn",
        "OrgPolicyViolationInfoOut": "_servicecontrol_9_OrgPolicyViolationInfoOut",
        "AuditLogIn": "_servicecontrol_10_AuditLogIn",
        "AuditLogOut": "_servicecontrol_11_AuditLogOut",
        "RequestIn": "_servicecontrol_12_RequestIn",
        "RequestOut": "_servicecontrol_13_RequestOut",
        "V2LogEntryOperationIn": "_servicecontrol_14_V2LogEntryOperationIn",
        "V2LogEntryOperationOut": "_servicecontrol_15_V2LogEntryOperationOut",
        "ViolationInfoIn": "_servicecontrol_16_ViolationInfoIn",
        "ViolationInfoOut": "_servicecontrol_17_ViolationInfoOut",
        "AuthIn": "_servicecontrol_18_AuthIn",
        "AuthOut": "_servicecontrol_19_AuthOut",
        "PolicyViolationInfoIn": "_servicecontrol_20_PolicyViolationInfoIn",
        "PolicyViolationInfoOut": "_servicecontrol_21_PolicyViolationInfoOut",
        "V2HttpRequestIn": "_servicecontrol_22_V2HttpRequestIn",
        "V2HttpRequestOut": "_servicecontrol_23_V2HttpRequestOut",
        "V2LogEntrySourceLocationIn": "_servicecontrol_24_V2LogEntrySourceLocationIn",
        "V2LogEntrySourceLocationOut": "_servicecontrol_25_V2LogEntrySourceLocationOut",
        "CheckResponseIn": "_servicecontrol_26_CheckResponseIn",
        "CheckResponseOut": "_servicecontrol_27_CheckResponseOut",
        "RequestMetadataIn": "_servicecontrol_28_RequestMetadataIn",
        "RequestMetadataOut": "_servicecontrol_29_RequestMetadataOut",
        "ApiIn": "_servicecontrol_30_ApiIn",
        "ApiOut": "_servicecontrol_31_ApiOut",
        "AttributeContextIn": "_servicecontrol_32_AttributeContextIn",
        "AttributeContextOut": "_servicecontrol_33_AttributeContextOut",
        "ResponseIn": "_servicecontrol_34_ResponseIn",
        "ResponseOut": "_servicecontrol_35_ResponseOut",
        "StatusIn": "_servicecontrol_36_StatusIn",
        "StatusOut": "_servicecontrol_37_StatusOut",
        "FirstPartyPrincipalIn": "_servicecontrol_38_FirstPartyPrincipalIn",
        "FirstPartyPrincipalOut": "_servicecontrol_39_FirstPartyPrincipalOut",
        "ThirdPartyPrincipalIn": "_servicecontrol_40_ThirdPartyPrincipalIn",
        "ThirdPartyPrincipalOut": "_servicecontrol_41_ThirdPartyPrincipalOut",
        "V2LogEntryIn": "_servicecontrol_42_V2LogEntryIn",
        "V2LogEntryOut": "_servicecontrol_43_V2LogEntryOut",
        "ReportResponseIn": "_servicecontrol_44_ReportResponseIn",
        "ReportResponseOut": "_servicecontrol_45_ReportResponseOut",
        "AuthenticationInfoIn": "_servicecontrol_46_AuthenticationInfoIn",
        "AuthenticationInfoOut": "_servicecontrol_47_AuthenticationInfoOut",
        "ResourceInfoIn": "_servicecontrol_48_ResourceInfoIn",
        "ResourceInfoOut": "_servicecontrol_49_ResourceInfoOut",
        "ResourceIn": "_servicecontrol_50_ResourceIn",
        "ResourceOut": "_servicecontrol_51_ResourceOut",
        "ReportRequestIn": "_servicecontrol_52_ReportRequestIn",
        "ReportRequestOut": "_servicecontrol_53_ReportRequestOut",
        "SpanContextIn": "_servicecontrol_54_SpanContextIn",
        "SpanContextOut": "_servicecontrol_55_SpanContextOut",
        "PeerIn": "_servicecontrol_56_PeerIn",
        "PeerOut": "_servicecontrol_57_PeerOut",
        "CheckRequestIn": "_servicecontrol_58_CheckRequestIn",
        "CheckRequestOut": "_servicecontrol_59_CheckRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["ServiceAccountDelegationInfoIn"] = t.struct(
        {
            "principalSubject": t.string().optional(),
            "firstPartyPrincipal": t.proxy(renames["FirstPartyPrincipalIn"]).optional(),
            "thirdPartyPrincipal": t.proxy(renames["ThirdPartyPrincipalIn"]).optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoIn"])
    types["ServiceAccountDelegationInfoOut"] = t.struct(
        {
            "principalSubject": t.string().optional(),
            "firstPartyPrincipal": t.proxy(
                renames["FirstPartyPrincipalOut"]
            ).optional(),
            "thirdPartyPrincipal": t.proxy(
                renames["ThirdPartyPrincipalOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServiceAccountDelegationInfoOut"])
    types["OrgPolicyViolationInfoIn"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "resourceType": t.string().optional(),
            "violationInfo": t.array(t.proxy(renames["ViolationInfoIn"])).optional(),
            "resourceTags": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OrgPolicyViolationInfoIn"])
    types["OrgPolicyViolationInfoOut"] = t.struct(
        {
            "payload": t.struct({"_": t.string().optional()}).optional(),
            "resourceType": t.string().optional(),
            "violationInfo": t.array(t.proxy(renames["ViolationInfoOut"])).optional(),
            "resourceTags": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrgPolicyViolationInfoOut"])
    types["AuditLogIn"] = t.struct(
        {
            "serviceData": t.struct({"_": t.string().optional()}).optional(),
            "resourceName": t.string().optional(),
            "numResponseItems": t.string().optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "authenticationInfo": t.proxy(renames["AuthenticationInfoIn"]).optional(),
            "resourceLocation": t.proxy(renames["ResourceLocationIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "policyViolationInfo": t.proxy(renames["PolicyViolationInfoIn"]).optional(),
            "authorizationInfo": t.array(
                t.proxy(renames["AuthorizationInfoIn"])
            ).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "serviceName": t.string().optional(),
            "resourceOriginalState": t.struct({"_": t.string().optional()}).optional(),
            "methodName": t.string().optional(),
        }
    ).named(renames["AuditLogIn"])
    types["AuditLogOut"] = t.struct(
        {
            "serviceData": t.struct({"_": t.string().optional()}).optional(),
            "resourceName": t.string().optional(),
            "numResponseItems": t.string().optional(),
            "requestMetadata": t.proxy(renames["RequestMetadataOut"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "authenticationInfo": t.proxy(renames["AuthenticationInfoOut"]).optional(),
            "resourceLocation": t.proxy(renames["ResourceLocationOut"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "policyViolationInfo": t.proxy(
                renames["PolicyViolationInfoOut"]
            ).optional(),
            "authorizationInfo": t.array(
                t.proxy(renames["AuthorizationInfoOut"])
            ).optional(),
            "request": t.struct({"_": t.string().optional()}).optional(),
            "serviceName": t.string().optional(),
            "resourceOriginalState": t.struct({"_": t.string().optional()}).optional(),
            "methodName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogOut"])
    types["RequestIn"] = t.struct(
        {
            "path": t.string().optional(),
            "method": t.string().optional(),
            "time": t.string().optional(),
            "query": t.string().optional(),
            "protocol": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "size": t.string().optional(),
            "host": t.string().optional(),
            "scheme": t.string().optional(),
            "auth": t.proxy(renames["AuthIn"]).optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["RequestIn"])
    types["RequestOut"] = t.struct(
        {
            "path": t.string().optional(),
            "method": t.string().optional(),
            "time": t.string().optional(),
            "query": t.string().optional(),
            "protocol": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "id": t.string().optional(),
            "size": t.string().optional(),
            "host": t.string().optional(),
            "scheme": t.string().optional(),
            "auth": t.proxy(renames["AuthOut"]).optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestOut"])
    types["V2LogEntryOperationIn"] = t.struct(
        {
            "last": t.boolean().optional(),
            "id": t.string().optional(),
            "producer": t.string().optional(),
            "first": t.boolean().optional(),
        }
    ).named(renames["V2LogEntryOperationIn"])
    types["V2LogEntryOperationOut"] = t.struct(
        {
            "last": t.boolean().optional(),
            "id": t.string().optional(),
            "producer": t.string().optional(),
            "first": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntryOperationOut"])
    types["ViolationInfoIn"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "constraint": t.string().optional(),
            "checkedValue": t.string().optional(),
            "policyType": t.string().optional(),
        }
    ).named(renames["ViolationInfoIn"])
    types["ViolationInfoOut"] = t.struct(
        {
            "errorMessage": t.string().optional(),
            "constraint": t.string().optional(),
            "checkedValue": t.string().optional(),
            "policyType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ViolationInfoOut"])
    types["AuthIn"] = t.struct(
        {
            "principal": t.string().optional(),
            "accessLevels": t.array(t.string()).optional(),
            "presenter": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
            "claims": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AuthIn"])
    types["AuthOut"] = t.struct(
        {
            "principal": t.string().optional(),
            "accessLevels": t.array(t.string()).optional(),
            "presenter": t.string().optional(),
            "audiences": t.array(t.string()).optional(),
            "claims": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthOut"])
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
    types["V2HttpRequestIn"] = t.struct(
        {
            "requestSize": t.string().optional(),
            "requestMethod": t.string().optional(),
            "protocol": t.string().optional(),
            "latency": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "status": t.integer().optional(),
            "userAgent": t.string().optional(),
            "requestUrl": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "responseSize": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "cacheFillBytes": t.string().optional(),
            "serverIp": t.string().optional(),
            "remoteIp": t.string().optional(),
            "referer": t.string().optional(),
        }
    ).named(renames["V2HttpRequestIn"])
    types["V2HttpRequestOut"] = t.struct(
        {
            "requestSize": t.string().optional(),
            "requestMethod": t.string().optional(),
            "protocol": t.string().optional(),
            "latency": t.string().optional(),
            "cacheValidatedWithOriginServer": t.boolean().optional(),
            "status": t.integer().optional(),
            "userAgent": t.string().optional(),
            "requestUrl": t.string().optional(),
            "cacheLookup": t.boolean().optional(),
            "responseSize": t.string().optional(),
            "cacheHit": t.boolean().optional(),
            "cacheFillBytes": t.string().optional(),
            "serverIp": t.string().optional(),
            "remoteIp": t.string().optional(),
            "referer": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2HttpRequestOut"])
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
    types["RequestMetadataIn"] = t.struct(
        {
            "destinationAttributes": t.proxy(renames["PeerIn"]).optional(),
            "callerNetwork": t.string().optional(),
            "callerIp": t.string().optional(),
            "callerSuppliedUserAgent": t.string().optional(),
            "requestAttributes": t.proxy(renames["RequestIn"]).optional(),
        }
    ).named(renames["RequestMetadataIn"])
    types["RequestMetadataOut"] = t.struct(
        {
            "destinationAttributes": t.proxy(renames["PeerOut"]).optional(),
            "callerNetwork": t.string().optional(),
            "callerIp": t.string().optional(),
            "callerSuppliedUserAgent": t.string().optional(),
            "requestAttributes": t.proxy(renames["RequestOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RequestMetadataOut"])
    types["ApiIn"] = t.struct(
        {
            "protocol": t.string().optional(),
            "version": t.string().optional(),
            "service": t.string().optional(),
            "operation": t.string().optional(),
        }
    ).named(renames["ApiIn"])
    types["ApiOut"] = t.struct(
        {
            "protocol": t.string().optional(),
            "version": t.string().optional(),
            "service": t.string().optional(),
            "operation": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOut"])
    types["AttributeContextIn"] = t.struct(
        {
            "request": t.proxy(renames["RequestIn"]).optional(),
            "response": t.proxy(renames["ResponseIn"]).optional(),
            "origin": t.proxy(renames["PeerIn"]).optional(),
            "source": t.proxy(renames["PeerIn"]).optional(),
            "resource": t.proxy(renames["ResourceIn"]).optional(),
            "api": t.proxy(renames["ApiIn"]).optional(),
            "destination": t.proxy(renames["PeerIn"]).optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["AttributeContextIn"])
    types["AttributeContextOut"] = t.struct(
        {
            "request": t.proxy(renames["RequestOut"]).optional(),
            "response": t.proxy(renames["ResponseOut"]).optional(),
            "origin": t.proxy(renames["PeerOut"]).optional(),
            "source": t.proxy(renames["PeerOut"]).optional(),
            "resource": t.proxy(renames["ResourceOut"]).optional(),
            "api": t.proxy(renames["ApiOut"]).optional(),
            "destination": t.proxy(renames["PeerOut"]).optional(),
            "extensions": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeContextOut"])
    types["ResponseIn"] = t.struct(
        {
            "size": t.string().optional(),
            "backendLatency": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "time": t.string().optional(),
            "code": t.string().optional(),
        }
    ).named(renames["ResponseIn"])
    types["ResponseOut"] = t.struct(
        {
            "size": t.string().optional(),
            "backendLatency": t.string().optional(),
            "headers": t.struct({"_": t.string().optional()}).optional(),
            "time": t.string().optional(),
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResponseOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["FirstPartyPrincipalIn"] = t.struct(
        {
            "serviceMetadata": t.struct({"_": t.string().optional()}).optional(),
            "principalEmail": t.string().optional(),
        }
    ).named(renames["FirstPartyPrincipalIn"])
    types["FirstPartyPrincipalOut"] = t.struct(
        {
            "serviceMetadata": t.struct({"_": t.string().optional()}).optional(),
            "principalEmail": t.string().optional(),
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
    types["V2LogEntryIn"] = t.struct(
        {
            "insertId": t.string().optional(),
            "httpRequest": t.proxy(renames["V2HttpRequestIn"]).optional(),
            "name": t.string(),
            "trace": t.string().optional(),
            "monitoredResourceLabels": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "timestamp": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sourceLocation": t.proxy(renames["V2LogEntrySourceLocationIn"]).optional(),
            "severity": t.string().optional(),
            "textPayload": t.string().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "structPayload": t.struct({"_": t.string().optional()}).optional(),
            "operation": t.proxy(renames["V2LogEntryOperationIn"]).optional(),
        }
    ).named(renames["V2LogEntryIn"])
    types["V2LogEntryOut"] = t.struct(
        {
            "insertId": t.string().optional(),
            "httpRequest": t.proxy(renames["V2HttpRequestOut"]).optional(),
            "name": t.string(),
            "trace": t.string().optional(),
            "monitoredResourceLabels": t.struct(
                {"_": t.string().optional()}
            ).optional(),
            "timestamp": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "sourceLocation": t.proxy(
                renames["V2LogEntrySourceLocationOut"]
            ).optional(),
            "severity": t.string().optional(),
            "textPayload": t.string().optional(),
            "protoPayload": t.struct({"_": t.string().optional()}).optional(),
            "structPayload": t.struct({"_": t.string().optional()}).optional(),
            "operation": t.proxy(renames["V2LogEntryOperationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2LogEntryOut"])
    types["ReportResponseIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ReportResponseIn"]
    )
    types["ReportResponseOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ReportResponseOut"])
    types["AuthenticationInfoIn"] = t.struct(
        {
            "serviceAccountKeyName": t.string().optional(),
            "principalEmail": t.string().optional(),
            "authoritySelector": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoIn"])
            ).optional(),
            "principalSubject": t.string().optional(),
            "thirdPartyPrincipal": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AuthenticationInfoIn"])
    types["AuthenticationInfoOut"] = t.struct(
        {
            "serviceAccountKeyName": t.string().optional(),
            "principalEmail": t.string().optional(),
            "authoritySelector": t.string().optional(),
            "serviceAccountDelegationInfo": t.array(
                t.proxy(renames["ServiceAccountDelegationInfoOut"])
            ).optional(),
            "principalSubject": t.string().optional(),
            "thirdPartyPrincipal": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthenticationInfoOut"])
    types["ResourceInfoIn"] = t.struct(
        {
            "location": t.string().optional(),
            "permission": t.string().optional(),
            "type": t.string().optional(),
            "container": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ResourceInfoIn"])
    types["ResourceInfoOut"] = t.struct(
        {
            "location": t.string().optional(),
            "permission": t.string().optional(),
            "type": t.string().optional(),
            "container": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceInfoOut"])
    types["ResourceIn"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "service": t.string().optional(),
            "location": t.string().optional(),
            "deleteTime": t.string().optional(),
        }
    ).named(renames["ResourceIn"])
    types["ResourceOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "annotations": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "etag": t.string().optional(),
            "uid": t.string().optional(),
            "displayName": t.string().optional(),
            "type": t.string().optional(),
            "service": t.string().optional(),
            "location": t.string().optional(),
            "deleteTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ResourceOut"])
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
    types["SpanContextIn"] = t.struct({"spanName": t.string().optional()}).named(
        renames["SpanContextIn"]
    )
    types["SpanContextOut"] = t.struct(
        {
            "spanName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanContextOut"])
    types["PeerIn"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "port": t.string().optional(),
            "principal": t.string().optional(),
            "ip": t.string().optional(),
        }
    ).named(renames["PeerIn"])
    types["PeerOut"] = t.struct(
        {
            "regionCode": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "port": t.string().optional(),
            "principal": t.string().optional(),
            "ip": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PeerOut"])
    types["CheckRequestIn"] = t.struct(
        {
            "flags": t.string().optional(),
            "attributes": t.proxy(renames["AttributeContextIn"]).optional(),
            "resources": t.array(t.proxy(renames["ResourceInfoIn"])).optional(),
            "serviceConfigId": t.string().optional(),
        }
    ).named(renames["CheckRequestIn"])
    types["CheckRequestOut"] = t.struct(
        {
            "flags": t.string().optional(),
            "attributes": t.proxy(renames["AttributeContextOut"]).optional(),
            "resources": t.array(t.proxy(renames["ResourceInfoOut"])).optional(),
            "serviceConfigId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CheckRequestOut"])

    functions = {}
    functions["servicesCheck"] = servicecontrol.post(
        "v2/services/{serviceName}:report",
        t.struct(
            {
                "serviceName": t.string().optional(),
                "operations": t.array(
                    t.proxy(renames["AttributeContextIn"])
                ).optional(),
                "serviceConfigId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["servicesReport"] = servicecontrol.post(
        "v2/services/{serviceName}:report",
        t.struct(
            {
                "serviceName": t.string().optional(),
                "operations": t.array(
                    t.proxy(renames["AttributeContextIn"])
                ).optional(),
                "serviceConfigId": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ReportResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="servicecontrol",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
