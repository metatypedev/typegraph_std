from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_domains():
    domains = HTTPRuntime("https://domains.googleapis.com/")

    renames = {
        "ErrorResponse": "_domains_1_ErrorResponse",
        "TransferDomainRequestIn": "_domains_2_TransferDomainRequestIn",
        "TransferDomainRequestOut": "_domains_3_TransferDomainRequestOut",
        "RetrieveImportableDomainsResponseIn": "_domains_4_RetrieveImportableDomainsResponseIn",
        "RetrieveImportableDomainsResponseOut": "_domains_5_RetrieveImportableDomainsResponseOut",
        "ManagementSettingsIn": "_domains_6_ManagementSettingsIn",
        "ManagementSettingsOut": "_domains_7_ManagementSettingsOut",
        "ConfigureDnsSettingsRequestIn": "_domains_8_ConfigureDnsSettingsRequestIn",
        "ConfigureDnsSettingsRequestOut": "_domains_9_ConfigureDnsSettingsRequestOut",
        "ConfigureContactSettingsRequestIn": "_domains_10_ConfigureContactSettingsRequestIn",
        "ConfigureContactSettingsRequestOut": "_domains_11_ConfigureContactSettingsRequestOut",
        "StatusIn": "_domains_12_StatusIn",
        "StatusOut": "_domains_13_StatusOut",
        "RegistrationIn": "_domains_14_RegistrationIn",
        "RegistrationOut": "_domains_15_RegistrationOut",
        "LocationIn": "_domains_16_LocationIn",
        "LocationOut": "_domains_17_LocationOut",
        "BindingIn": "_domains_18_BindingIn",
        "BindingOut": "_domains_19_BindingOut",
        "ConfigureManagementSettingsRequestIn": "_domains_20_ConfigureManagementSettingsRequestIn",
        "ConfigureManagementSettingsRequestOut": "_domains_21_ConfigureManagementSettingsRequestOut",
        "RetrieveRegisterParametersResponseIn": "_domains_22_RetrieveRegisterParametersResponseIn",
        "RetrieveRegisterParametersResponseOut": "_domains_23_RetrieveRegisterParametersResponseOut",
        "ListRegistrationsResponseIn": "_domains_24_ListRegistrationsResponseIn",
        "ListRegistrationsResponseOut": "_domains_25_ListRegistrationsResponseOut",
        "RegisterDomainRequestIn": "_domains_26_RegisterDomainRequestIn",
        "RegisterDomainRequestOut": "_domains_27_RegisterDomainRequestOut",
        "SearchDomainsResponseIn": "_domains_28_SearchDomainsResponseIn",
        "SearchDomainsResponseOut": "_domains_29_SearchDomainsResponseOut",
        "AuditConfigIn": "_domains_30_AuditConfigIn",
        "AuditConfigOut": "_domains_31_AuditConfigOut",
        "ExportRegistrationRequestIn": "_domains_32_ExportRegistrationRequestIn",
        "ExportRegistrationRequestOut": "_domains_33_ExportRegistrationRequestOut",
        "OperationMetadataIn": "_domains_34_OperationMetadataIn",
        "OperationMetadataOut": "_domains_35_OperationMetadataOut",
        "OperationIn": "_domains_36_OperationIn",
        "OperationOut": "_domains_37_OperationOut",
        "DnsSettingsIn": "_domains_38_DnsSettingsIn",
        "DnsSettingsOut": "_domains_39_DnsSettingsOut",
        "ContactIn": "_domains_40_ContactIn",
        "ContactOut": "_domains_41_ContactOut",
        "AuthorizationCodeIn": "_domains_42_AuthorizationCodeIn",
        "AuthorizationCodeOut": "_domains_43_AuthorizationCodeOut",
        "TestIamPermissionsRequestIn": "_domains_44_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_domains_45_TestIamPermissionsRequestOut",
        "TestIamPermissionsResponseIn": "_domains_46_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_domains_47_TestIamPermissionsResponseOut",
        "RegisterParametersIn": "_domains_48_RegisterParametersIn",
        "RegisterParametersOut": "_domains_49_RegisterParametersOut",
        "AuditLogConfigIn": "_domains_50_AuditLogConfigIn",
        "AuditLogConfigOut": "_domains_51_AuditLogConfigOut",
        "ImportDomainRequestIn": "_domains_52_ImportDomainRequestIn",
        "ImportDomainRequestOut": "_domains_53_ImportDomainRequestOut",
        "ListOperationsResponseIn": "_domains_54_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_domains_55_ListOperationsResponseOut",
        "SetIamPolicyRequestIn": "_domains_56_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_domains_57_SetIamPolicyRequestOut",
        "TransferParametersIn": "_domains_58_TransferParametersIn",
        "TransferParametersOut": "_domains_59_TransferParametersOut",
        "ExprIn": "_domains_60_ExprIn",
        "ExprOut": "_domains_61_ExprOut",
        "ContactSettingsIn": "_domains_62_ContactSettingsIn",
        "ContactSettingsOut": "_domains_63_ContactSettingsOut",
        "GlueRecordIn": "_domains_64_GlueRecordIn",
        "GlueRecordOut": "_domains_65_GlueRecordOut",
        "DomainIn": "_domains_66_DomainIn",
        "DomainOut": "_domains_67_DomainOut",
        "GoogleDomainsDnsIn": "_domains_68_GoogleDomainsDnsIn",
        "GoogleDomainsDnsOut": "_domains_69_GoogleDomainsDnsOut",
        "DsRecordIn": "_domains_70_DsRecordIn",
        "DsRecordOut": "_domains_71_DsRecordOut",
        "PostalAddressIn": "_domains_72_PostalAddressIn",
        "PostalAddressOut": "_domains_73_PostalAddressOut",
        "ListLocationsResponseIn": "_domains_74_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_domains_75_ListLocationsResponseOut",
        "RetrieveTransferParametersResponseIn": "_domains_76_RetrieveTransferParametersResponseIn",
        "RetrieveTransferParametersResponseOut": "_domains_77_RetrieveTransferParametersResponseOut",
        "MoneyIn": "_domains_78_MoneyIn",
        "MoneyOut": "_domains_79_MoneyOut",
        "CustomDnsIn": "_domains_80_CustomDnsIn",
        "CustomDnsOut": "_domains_81_CustomDnsOut",
        "PolicyIn": "_domains_82_PolicyIn",
        "PolicyOut": "_domains_83_PolicyOut",
        "ResetAuthorizationCodeRequestIn": "_domains_84_ResetAuthorizationCodeRequestIn",
        "ResetAuthorizationCodeRequestOut": "_domains_85_ResetAuthorizationCodeRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TransferDomainRequestIn"] = t.struct(
        {
            "registration": t.proxy(renames["RegistrationIn"]),
            "yearlyPrice": t.proxy(renames["MoneyIn"]),
            "validateOnly": t.boolean().optional(),
            "contactNotices": t.array(t.string()).optional(),
            "authorizationCode": t.proxy(renames["AuthorizationCodeIn"]).optional(),
        }
    ).named(renames["TransferDomainRequestIn"])
    types["TransferDomainRequestOut"] = t.struct(
        {
            "registration": t.proxy(renames["RegistrationOut"]),
            "yearlyPrice": t.proxy(renames["MoneyOut"]),
            "validateOnly": t.boolean().optional(),
            "contactNotices": t.array(t.string()).optional(),
            "authorizationCode": t.proxy(renames["AuthorizationCodeOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferDomainRequestOut"])
    types["RetrieveImportableDomainsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "domains": t.array(t.proxy(renames["DomainIn"])).optional(),
        }
    ).named(renames["RetrieveImportableDomainsResponseIn"])
    types["RetrieveImportableDomainsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "domains": t.array(t.proxy(renames["DomainOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveImportableDomainsResponseOut"])
    types["ManagementSettingsIn"] = t.struct(
        {"transferLockState": t.string().optional()}
    ).named(renames["ManagementSettingsIn"])
    types["ManagementSettingsOut"] = t.struct(
        {
            "transferLockState": t.string().optional(),
            "renewalMethod": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ManagementSettingsOut"])
    types["ConfigureDnsSettingsRequestIn"] = t.struct(
        {
            "updateMask": t.string(),
            "validateOnly": t.boolean().optional(),
            "dnsSettings": t.proxy(renames["DnsSettingsIn"]).optional(),
        }
    ).named(renames["ConfigureDnsSettingsRequestIn"])
    types["ConfigureDnsSettingsRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "validateOnly": t.boolean().optional(),
            "dnsSettings": t.proxy(renames["DnsSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigureDnsSettingsRequestOut"])
    types["ConfigureContactSettingsRequestIn"] = t.struct(
        {
            "contactNotices": t.array(t.string()).optional(),
            "validateOnly": t.boolean().optional(),
            "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
            "updateMask": t.string(),
        }
    ).named(renames["ConfigureContactSettingsRequestIn"])
    types["ConfigureContactSettingsRequestOut"] = t.struct(
        {
            "contactNotices": t.array(t.string()).optional(),
            "validateOnly": t.boolean().optional(),
            "contactSettings": t.proxy(renames["ContactSettingsOut"]).optional(),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigureContactSettingsRequestOut"])
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
    types["RegistrationIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "domainName": t.string(),
            "managementSettings": t.proxy(renames["ManagementSettingsIn"]).optional(),
            "contactSettings": t.proxy(renames["ContactSettingsIn"]),
            "dnsSettings": t.proxy(renames["DnsSettingsIn"]).optional(),
        }
    ).named(renames["RegistrationIn"])
    types["RegistrationOut"] = t.struct(
        {
            "pendingContactSettings": t.proxy(renames["ContactSettingsOut"]).optional(),
            "issues": t.array(t.string()).optional(),
            "state": t.string().optional(),
            "registerFailureReason": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "domainName": t.string(),
            "managementSettings": t.proxy(renames["ManagementSettingsOut"]).optional(),
            "contactSettings": t.proxy(renames["ContactSettingsOut"]),
            "expireTime": t.string().optional(),
            "createTime": t.string().optional(),
            "transferFailureReason": t.string().optional(),
            "name": t.string().optional(),
            "dnsSettings": t.proxy(renames["DnsSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegistrationOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ConfigureManagementSettingsRequestIn"] = t.struct(
        {
            "managementSettings": t.proxy(renames["ManagementSettingsIn"]).optional(),
            "updateMask": t.string(),
        }
    ).named(renames["ConfigureManagementSettingsRequestIn"])
    types["ConfigureManagementSettingsRequestOut"] = t.struct(
        {
            "managementSettings": t.proxy(renames["ManagementSettingsOut"]).optional(),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigureManagementSettingsRequestOut"])
    types["RetrieveRegisterParametersResponseIn"] = t.struct(
        {"registerParameters": t.proxy(renames["RegisterParametersIn"]).optional()}
    ).named(renames["RetrieveRegisterParametersResponseIn"])
    types["RetrieveRegisterParametersResponseOut"] = t.struct(
        {
            "registerParameters": t.proxy(renames["RegisterParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveRegisterParametersResponseOut"])
    types["ListRegistrationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "registrations": t.array(t.proxy(renames["RegistrationIn"])).optional(),
        }
    ).named(renames["ListRegistrationsResponseIn"])
    types["ListRegistrationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "registrations": t.array(t.proxy(renames["RegistrationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRegistrationsResponseOut"])
    types["RegisterDomainRequestIn"] = t.struct(
        {
            "yearlyPrice": t.proxy(renames["MoneyIn"]),
            "contactNotices": t.array(t.string()).optional(),
            "domainNotices": t.array(t.string()).optional(),
            "registration": t.proxy(renames["RegistrationIn"]),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["RegisterDomainRequestIn"])
    types["RegisterDomainRequestOut"] = t.struct(
        {
            "yearlyPrice": t.proxy(renames["MoneyOut"]),
            "contactNotices": t.array(t.string()).optional(),
            "domainNotices": t.array(t.string()).optional(),
            "registration": t.proxy(renames["RegistrationOut"]),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterDomainRequestOut"])
    types["SearchDomainsResponseIn"] = t.struct(
        {
            "registerParameters": t.array(
                t.proxy(renames["RegisterParametersIn"])
            ).optional()
        }
    ).named(renames["SearchDomainsResponseIn"])
    types["SearchDomainsResponseOut"] = t.struct(
        {
            "registerParameters": t.array(
                t.proxy(renames["RegisterParametersOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchDomainsResponseOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
            "service": t.string().optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "service": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])
    types["ExportRegistrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportRegistrationRequestIn"]
    )
    types["ExportRegistrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportRegistrationRequestOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "verb": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["DnsSettingsIn"] = t.struct(
        {
            "customDns": t.proxy(renames["CustomDnsIn"]).optional(),
            "glueRecords": t.array(t.proxy(renames["GlueRecordIn"])).optional(),
            "googleDomainsDns": t.proxy(renames["GoogleDomainsDnsIn"]).optional(),
        }
    ).named(renames["DnsSettingsIn"])
    types["DnsSettingsOut"] = t.struct(
        {
            "customDns": t.proxy(renames["CustomDnsOut"]).optional(),
            "glueRecords": t.array(t.proxy(renames["GlueRecordOut"])).optional(),
            "googleDomainsDns": t.proxy(renames["GoogleDomainsDnsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsSettingsOut"])
    types["ContactIn"] = t.struct(
        {
            "email": t.string(),
            "faxNumber": t.string().optional(),
            "postalAddress": t.proxy(renames["PostalAddressIn"]),
            "phoneNumber": t.string(),
        }
    ).named(renames["ContactIn"])
    types["ContactOut"] = t.struct(
        {
            "email": t.string(),
            "faxNumber": t.string().optional(),
            "postalAddress": t.proxy(renames["PostalAddressOut"]),
            "phoneNumber": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactOut"])
    types["AuthorizationCodeIn"] = t.struct({"code": t.string().optional()}).named(
        renames["AuthorizationCodeIn"]
    )
    types["AuthorizationCodeOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationCodeOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["RegisterParametersIn"] = t.struct(
        {
            "domainName": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "availability": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "domainNotices": t.array(t.string()).optional(),
        }
    ).named(renames["RegisterParametersIn"])
    types["RegisterParametersOut"] = t.struct(
        {
            "domainName": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "availability": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "domainNotices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterParametersOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "logType": t.string().optional(),
            "exemptedMembers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["ImportDomainRequestIn"] = t.struct(
        {
            "domainName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ImportDomainRequestIn"])
    types["ImportDomainRequestOut"] = t.struct(
        {
            "domainName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDomainRequestOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListOperationsResponseOut"])
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyIn"]).optional(),
            "updateMask": t.string().optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "updateMask": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
    types["TransferParametersIn"] = t.struct(
        {
            "domainName": t.string().optional(),
            "currentRegistrarUri": t.string().optional(),
            "transferLockState": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "currentRegistrar": t.string().optional(),
            "nameServers": t.array(t.string()).optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
        }
    ).named(renames["TransferParametersIn"])
    types["TransferParametersOut"] = t.struct(
        {
            "domainName": t.string().optional(),
            "currentRegistrarUri": t.string().optional(),
            "transferLockState": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "currentRegistrar": t.string().optional(),
            "nameServers": t.array(t.string()).optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferParametersOut"])
    types["ExprIn"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "description": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["ContactSettingsIn"] = t.struct(
        {
            "privacy": t.string(),
            "technicalContact": t.proxy(renames["ContactIn"]),
            "adminContact": t.proxy(renames["ContactIn"]),
            "registrantContact": t.proxy(renames["ContactIn"]),
        }
    ).named(renames["ContactSettingsIn"])
    types["ContactSettingsOut"] = t.struct(
        {
            "privacy": t.string(),
            "technicalContact": t.proxy(renames["ContactOut"]),
            "adminContact": t.proxy(renames["ContactOut"]),
            "registrantContact": t.proxy(renames["ContactOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactSettingsOut"])
    types["GlueRecordIn"] = t.struct(
        {
            "ipv4Addresses": t.array(t.string()).optional(),
            "hostName": t.string(),
            "ipv6Addresses": t.array(t.string()).optional(),
        }
    ).named(renames["GlueRecordIn"])
    types["GlueRecordOut"] = t.struct(
        {
            "ipv4Addresses": t.array(t.string()).optional(),
            "hostName": t.string(),
            "ipv6Addresses": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlueRecordOut"])
    types["DomainIn"] = t.struct(
        {
            "domainName": t.string().optional(),
            "resourceState": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "domainName": t.string().optional(),
            "resourceState": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
    types["GoogleDomainsDnsIn"] = t.struct({"dsState": t.string()}).named(
        renames["GoogleDomainsDnsIn"]
    )
    types["GoogleDomainsDnsOut"] = t.struct(
        {
            "nameServers": t.array(t.string()).optional(),
            "dsRecords": t.array(t.proxy(renames["DsRecordOut"])).optional(),
            "dsState": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDomainsDnsOut"])
    types["DsRecordIn"] = t.struct(
        {
            "digestType": t.string().optional(),
            "digest": t.string().optional(),
            "algorithm": t.string().optional(),
            "keyTag": t.integer().optional(),
        }
    ).named(renames["DsRecordIn"])
    types["DsRecordOut"] = t.struct(
        {
            "digestType": t.string().optional(),
            "digest": t.string().optional(),
            "algorithm": t.string().optional(),
            "keyTag": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DsRecordOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "regionCode": t.string(),
            "languageCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "revision": t.integer().optional(),
            "locality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "sortingCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "organization": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "regionCode": t.string(),
            "languageCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "sublocality": t.string().optional(),
            "revision": t.integer().optional(),
            "locality": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "sortingCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "organization": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
    types["RetrieveTransferParametersResponseIn"] = t.struct(
        {"transferParameters": t.proxy(renames["TransferParametersIn"]).optional()}
    ).named(renames["RetrieveTransferParametersResponseIn"])
    types["RetrieveTransferParametersResponseOut"] = t.struct(
        {
            "transferParameters": t.proxy(renames["TransferParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveTransferParametersResponseOut"])
    types["MoneyIn"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "nanos": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["CustomDnsIn"] = t.struct(
        {
            "dsRecords": t.array(t.proxy(renames["DsRecordIn"])).optional(),
            "nameServers": t.array(t.string()),
        }
    ).named(renames["CustomDnsIn"])
    types["CustomDnsOut"] = t.struct(
        {
            "dsRecords": t.array(t.proxy(renames["DsRecordOut"])).optional(),
            "nameServers": t.array(t.string()),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDnsOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ResetAuthorizationCodeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResetAuthorizationCodeRequestIn"])
    types["ResetAuthorizationCodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetAuthorizationCodeRequestOut"])

    functions = {}
    functions["projectsLocationsList"] = domains.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsGet"] = domains.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["LocationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = domains.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = domains.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRegister"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsConfigureContactSettings"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsSetIamPolicy"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsList"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRetrieveImportableDomains"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRegistrationsConfigureManagementSettings"
    ] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsDelete"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsExport"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsTransfer"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsConfigureDnsSettings"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRetrieveAuthorizationCode"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsResetAuthorizationCode"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRegistrationsRetrieveRegisterParameters"
    ] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsTestIamPermissions"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsPatch"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsSearchDomains"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsGetIamPolicy"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsGet"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRegistrationsRetrieveTransferParameters"
    ] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsImport"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "domainName": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="domains", renames=renames, types=Box(types), functions=Box(functions)
    )
