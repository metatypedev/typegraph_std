from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_domains() -> Import:
    domains = HTTPRuntime("https://domains.googleapis.com/")

    renames = {
        "ErrorResponse": "_domains_1_ErrorResponse",
        "GoogleDomainsDnsIn": "_domains_2_GoogleDomainsDnsIn",
        "GoogleDomainsDnsOut": "_domains_3_GoogleDomainsDnsOut",
        "SearchDomainsResponseIn": "_domains_4_SearchDomainsResponseIn",
        "SearchDomainsResponseOut": "_domains_5_SearchDomainsResponseOut",
        "TransferDomainRequestIn": "_domains_6_TransferDomainRequestIn",
        "TransferDomainRequestOut": "_domains_7_TransferDomainRequestOut",
        "ConfigureManagementSettingsRequestIn": "_domains_8_ConfigureManagementSettingsRequestIn",
        "ConfigureManagementSettingsRequestOut": "_domains_9_ConfigureManagementSettingsRequestOut",
        "GlueRecordIn": "_domains_10_GlueRecordIn",
        "GlueRecordOut": "_domains_11_GlueRecordOut",
        "TransferParametersIn": "_domains_12_TransferParametersIn",
        "TransferParametersOut": "_domains_13_TransferParametersOut",
        "ContactIn": "_domains_14_ContactIn",
        "ContactOut": "_domains_15_ContactOut",
        "ResetAuthorizationCodeRequestIn": "_domains_16_ResetAuthorizationCodeRequestIn",
        "ResetAuthorizationCodeRequestOut": "_domains_17_ResetAuthorizationCodeRequestOut",
        "ListLocationsResponseIn": "_domains_18_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_domains_19_ListLocationsResponseOut",
        "BindingIn": "_domains_20_BindingIn",
        "BindingOut": "_domains_21_BindingOut",
        "ConfigureContactSettingsRequestIn": "_domains_22_ConfigureContactSettingsRequestIn",
        "ConfigureContactSettingsRequestOut": "_domains_23_ConfigureContactSettingsRequestOut",
        "TestIamPermissionsRequestIn": "_domains_24_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_domains_25_TestIamPermissionsRequestOut",
        "MoneyIn": "_domains_26_MoneyIn",
        "MoneyOut": "_domains_27_MoneyOut",
        "DomainIn": "_domains_28_DomainIn",
        "DomainOut": "_domains_29_DomainOut",
        "TestIamPermissionsResponseIn": "_domains_30_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_domains_31_TestIamPermissionsResponseOut",
        "ListRegistrationsResponseIn": "_domains_32_ListRegistrationsResponseIn",
        "ListRegistrationsResponseOut": "_domains_33_ListRegistrationsResponseOut",
        "StatusIn": "_domains_34_StatusIn",
        "StatusOut": "_domains_35_StatusOut",
        "DsRecordIn": "_domains_36_DsRecordIn",
        "DsRecordOut": "_domains_37_DsRecordOut",
        "RetrieveImportableDomainsResponseIn": "_domains_38_RetrieveImportableDomainsResponseIn",
        "RetrieveImportableDomainsResponseOut": "_domains_39_RetrieveImportableDomainsResponseOut",
        "ImportDomainRequestIn": "_domains_40_ImportDomainRequestIn",
        "ImportDomainRequestOut": "_domains_41_ImportDomainRequestOut",
        "DnsSettingsIn": "_domains_42_DnsSettingsIn",
        "DnsSettingsOut": "_domains_43_DnsSettingsOut",
        "AuthorizationCodeIn": "_domains_44_AuthorizationCodeIn",
        "AuthorizationCodeOut": "_domains_45_AuthorizationCodeOut",
        "ContactSettingsIn": "_domains_46_ContactSettingsIn",
        "ContactSettingsOut": "_domains_47_ContactSettingsOut",
        "PostalAddressIn": "_domains_48_PostalAddressIn",
        "PostalAddressOut": "_domains_49_PostalAddressOut",
        "ConfigureDnsSettingsRequestIn": "_domains_50_ConfigureDnsSettingsRequestIn",
        "ConfigureDnsSettingsRequestOut": "_domains_51_ConfigureDnsSettingsRequestOut",
        "PolicyIn": "_domains_52_PolicyIn",
        "PolicyOut": "_domains_53_PolicyOut",
        "AuditLogConfigIn": "_domains_54_AuditLogConfigIn",
        "AuditLogConfigOut": "_domains_55_AuditLogConfigOut",
        "OperationIn": "_domains_56_OperationIn",
        "OperationOut": "_domains_57_OperationOut",
        "LocationIn": "_domains_58_LocationIn",
        "LocationOut": "_domains_59_LocationOut",
        "ListOperationsResponseIn": "_domains_60_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_domains_61_ListOperationsResponseOut",
        "SetIamPolicyRequestIn": "_domains_62_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_domains_63_SetIamPolicyRequestOut",
        "RetrieveRegisterParametersResponseIn": "_domains_64_RetrieveRegisterParametersResponseIn",
        "RetrieveRegisterParametersResponseOut": "_domains_65_RetrieveRegisterParametersResponseOut",
        "OperationMetadataIn": "_domains_66_OperationMetadataIn",
        "OperationMetadataOut": "_domains_67_OperationMetadataOut",
        "ExprIn": "_domains_68_ExprIn",
        "ExprOut": "_domains_69_ExprOut",
        "RegisterDomainRequestIn": "_domains_70_RegisterDomainRequestIn",
        "RegisterDomainRequestOut": "_domains_71_RegisterDomainRequestOut",
        "ExportRegistrationRequestIn": "_domains_72_ExportRegistrationRequestIn",
        "ExportRegistrationRequestOut": "_domains_73_ExportRegistrationRequestOut",
        "CustomDnsIn": "_domains_74_CustomDnsIn",
        "CustomDnsOut": "_domains_75_CustomDnsOut",
        "ManagementSettingsIn": "_domains_76_ManagementSettingsIn",
        "ManagementSettingsOut": "_domains_77_ManagementSettingsOut",
        "RegistrationIn": "_domains_78_RegistrationIn",
        "RegistrationOut": "_domains_79_RegistrationOut",
        "RetrieveTransferParametersResponseIn": "_domains_80_RetrieveTransferParametersResponseIn",
        "RetrieveTransferParametersResponseOut": "_domains_81_RetrieveTransferParametersResponseOut",
        "RegisterParametersIn": "_domains_82_RegisterParametersIn",
        "RegisterParametersOut": "_domains_83_RegisterParametersOut",
        "AuditConfigIn": "_domains_84_AuditConfigIn",
        "AuditConfigOut": "_domains_85_AuditConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["GoogleDomainsDnsIn"] = t.struct({"dsState": t.string()}).named(
        renames["GoogleDomainsDnsIn"]
    )
    types["GoogleDomainsDnsOut"] = t.struct(
        {
            "nameServers": t.array(t.string()).optional(),
            "dsState": t.string(),
            "dsRecords": t.array(t.proxy(renames["DsRecordOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GoogleDomainsDnsOut"])
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
    types["TransferDomainRequestIn"] = t.struct(
        {
            "yearlyPrice": t.proxy(renames["MoneyIn"]),
            "authorizationCode": t.proxy(renames["AuthorizationCodeIn"]).optional(),
            "registration": t.proxy(renames["RegistrationIn"]),
            "validateOnly": t.boolean().optional(),
            "contactNotices": t.array(t.string()).optional(),
        }
    ).named(renames["TransferDomainRequestIn"])
    types["TransferDomainRequestOut"] = t.struct(
        {
            "yearlyPrice": t.proxy(renames["MoneyOut"]),
            "authorizationCode": t.proxy(renames["AuthorizationCodeOut"]).optional(),
            "registration": t.proxy(renames["RegistrationOut"]),
            "validateOnly": t.boolean().optional(),
            "contactNotices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferDomainRequestOut"])
    types["ConfigureManagementSettingsRequestIn"] = t.struct(
        {
            "updateMask": t.string(),
            "managementSettings": t.proxy(renames["ManagementSettingsIn"]).optional(),
        }
    ).named(renames["ConfigureManagementSettingsRequestIn"])
    types["ConfigureManagementSettingsRequestOut"] = t.struct(
        {
            "updateMask": t.string(),
            "managementSettings": t.proxy(renames["ManagementSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigureManagementSettingsRequestOut"])
    types["GlueRecordIn"] = t.struct(
        {
            "ipv6Addresses": t.array(t.string()).optional(),
            "ipv4Addresses": t.array(t.string()).optional(),
            "hostName": t.string(),
        }
    ).named(renames["GlueRecordIn"])
    types["GlueRecordOut"] = t.struct(
        {
            "ipv6Addresses": t.array(t.string()).optional(),
            "ipv4Addresses": t.array(t.string()).optional(),
            "hostName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlueRecordOut"])
    types["TransferParametersIn"] = t.struct(
        {
            "transferLockState": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "currentRegistrar": t.string().optional(),
            "currentRegistrarUri": t.string().optional(),
            "domainName": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "nameServers": t.array(t.string()).optional(),
        }
    ).named(renames["TransferParametersIn"])
    types["TransferParametersOut"] = t.struct(
        {
            "transferLockState": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "currentRegistrar": t.string().optional(),
            "currentRegistrarUri": t.string().optional(),
            "domainName": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "nameServers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferParametersOut"])
    types["ContactIn"] = t.struct(
        {
            "email": t.string(),
            "faxNumber": t.string().optional(),
            "phoneNumber": t.string(),
            "postalAddress": t.proxy(renames["PostalAddressIn"]),
        }
    ).named(renames["ContactIn"])
    types["ContactOut"] = t.struct(
        {
            "email": t.string(),
            "faxNumber": t.string().optional(),
            "phoneNumber": t.string(),
            "postalAddress": t.proxy(renames["PostalAddressOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactOut"])
    types["ResetAuthorizationCodeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResetAuthorizationCodeRequestIn"])
    types["ResetAuthorizationCodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetAuthorizationCodeRequestOut"])
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
    types["BindingIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["ConfigureContactSettingsRequestIn"] = t.struct(
        {
            "contactNotices": t.array(t.string()).optional(),
            "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
            "validateOnly": t.boolean().optional(),
            "updateMask": t.string(),
        }
    ).named(renames["ConfigureContactSettingsRequestIn"])
    types["ConfigureContactSettingsRequestOut"] = t.struct(
        {
            "contactNotices": t.array(t.string()).optional(),
            "contactSettings": t.proxy(renames["ContactSettingsOut"]).optional(),
            "validateOnly": t.boolean().optional(),
            "updateMask": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigureContactSettingsRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["MoneyIn"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
        }
    ).named(renames["MoneyIn"])
    types["MoneyOut"] = t.struct(
        {
            "nanos": t.integer().optional(),
            "currencyCode": t.string().optional(),
            "units": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoneyOut"])
    types["DomainIn"] = t.struct(
        {
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "resourceState": t.string().optional(),
            "domainName": t.string().optional(),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "resourceState": t.string().optional(),
            "domainName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["DsRecordIn"] = t.struct(
        {
            "digestType": t.string().optional(),
            "keyTag": t.integer().optional(),
            "digest": t.string().optional(),
            "algorithm": t.string().optional(),
        }
    ).named(renames["DsRecordIn"])
    types["DsRecordOut"] = t.struct(
        {
            "digestType": t.string().optional(),
            "keyTag": t.integer().optional(),
            "digest": t.string().optional(),
            "algorithm": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DsRecordOut"])
    types["RetrieveImportableDomainsResponseIn"] = t.struct(
        {
            "domains": t.array(t.proxy(renames["DomainIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["RetrieveImportableDomainsResponseIn"])
    types["RetrieveImportableDomainsResponseOut"] = t.struct(
        {
            "domains": t.array(t.proxy(renames["DomainOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveImportableDomainsResponseOut"])
    types["ImportDomainRequestIn"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "domainName": t.string(),
        }
    ).named(renames["ImportDomainRequestIn"])
    types["ImportDomainRequestOut"] = t.struct(
        {
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "domainName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ImportDomainRequestOut"])
    types["DnsSettingsIn"] = t.struct(
        {
            "customDns": t.proxy(renames["CustomDnsIn"]).optional(),
            "googleDomainsDns": t.proxy(renames["GoogleDomainsDnsIn"]).optional(),
            "glueRecords": t.array(t.proxy(renames["GlueRecordIn"])).optional(),
        }
    ).named(renames["DnsSettingsIn"])
    types["DnsSettingsOut"] = t.struct(
        {
            "customDns": t.proxy(renames["CustomDnsOut"]).optional(),
            "googleDomainsDns": t.proxy(renames["GoogleDomainsDnsOut"]).optional(),
            "glueRecords": t.array(t.proxy(renames["GlueRecordOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsSettingsOut"])
    types["AuthorizationCodeIn"] = t.struct({"code": t.string().optional()}).named(
        renames["AuthorizationCodeIn"]
    )
    types["AuthorizationCodeOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationCodeOut"])
    types["ContactSettingsIn"] = t.struct(
        {
            "registrantContact": t.proxy(renames["ContactIn"]),
            "technicalContact": t.proxy(renames["ContactIn"]),
            "privacy": t.string(),
            "adminContact": t.proxy(renames["ContactIn"]),
        }
    ).named(renames["ContactSettingsIn"])
    types["ContactSettingsOut"] = t.struct(
        {
            "registrantContact": t.proxy(renames["ContactOut"]),
            "technicalContact": t.proxy(renames["ContactOut"]),
            "privacy": t.string(),
            "adminContact": t.proxy(renames["ContactOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactSettingsOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "recipients": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "regionCode": t.string(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
            "revision": t.integer().optional(),
            "languageCode": t.string().optional(),
            "sortingCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "postalCode": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "recipients": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "regionCode": t.string(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
            "revision": t.integer().optional(),
            "languageCode": t.string().optional(),
            "sortingCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "postalCode": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["LocationIn"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "locationId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["ListOperationsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationIn"])).optional(),
        }
    ).named(renames["ListOperationsResponseIn"])
    types["ListOperationsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "operations": t.array(t.proxy(renames["OperationOut"])).optional(),
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
    types["RetrieveRegisterParametersResponseIn"] = t.struct(
        {"registerParameters": t.proxy(renames["RegisterParametersIn"]).optional()}
    ).named(renames["RetrieveRegisterParametersResponseIn"])
    types["RetrieveRegisterParametersResponseOut"] = t.struct(
        {
            "registerParameters": t.proxy(renames["RegisterParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveRegisterParametersResponseOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "verb": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
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
    types["ExportRegistrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportRegistrationRequestIn"]
    )
    types["ExportRegistrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportRegistrationRequestOut"])
    types["CustomDnsIn"] = t.struct(
        {
            "nameServers": t.array(t.string()),
            "dsRecords": t.array(t.proxy(renames["DsRecordIn"])).optional(),
        }
    ).named(renames["CustomDnsIn"])
    types["CustomDnsOut"] = t.struct(
        {
            "nameServers": t.array(t.string()),
            "dsRecords": t.array(t.proxy(renames["DsRecordOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomDnsOut"])
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
    types["RegistrationIn"] = t.struct(
        {
            "managementSettings": t.proxy(renames["ManagementSettingsIn"]).optional(),
            "contactSettings": t.proxy(renames["ContactSettingsIn"]),
            "domainName": t.string(),
            "dnsSettings": t.proxy(renames["DnsSettingsIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RegistrationIn"])
    types["RegistrationOut"] = t.struct(
        {
            "managementSettings": t.proxy(renames["ManagementSettingsOut"]).optional(),
            "createTime": t.string().optional(),
            "contactSettings": t.proxy(renames["ContactSettingsOut"]),
            "domainName": t.string(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "dnsSettings": t.proxy(renames["DnsSettingsOut"]).optional(),
            "issues": t.array(t.string()).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "pendingContactSettings": t.proxy(renames["ContactSettingsOut"]).optional(),
            "transferFailureReason": t.string().optional(),
            "registerFailureReason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegistrationOut"])
    types["RetrieveTransferParametersResponseIn"] = t.struct(
        {"transferParameters": t.proxy(renames["TransferParametersIn"]).optional()}
    ).named(renames["RetrieveTransferParametersResponseIn"])
    types["RetrieveTransferParametersResponseOut"] = t.struct(
        {
            "transferParameters": t.proxy(renames["TransferParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveTransferParametersResponseOut"])
    types["RegisterParametersIn"] = t.struct(
        {
            "domainName": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "domainNotices": t.array(t.string()).optional(),
            "availability": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
        }
    ).named(renames["RegisterParametersIn"])
    types["RegisterParametersOut"] = t.struct(
        {
            "domainName": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "domainNotices": t.array(t.string()).optional(),
            "availability": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterParametersOut"])
    types["AuditConfigIn"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(t.proxy(renames["AuditLogConfigIn"])).optional(),
        }
    ).named(renames["AuditConfigIn"])
    types["AuditConfigOut"] = t.struct(
        {
            "service": t.string().optional(),
            "auditLogConfigs": t.array(
                t.proxy(renames["AuditLogConfigOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditConfigOut"])

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
    functions["projectsLocationsRegistrationsTestIamPermissions"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRegister"] = domains.post(
        "v1/{parent}/registrations:import",
        t.struct(
            {
                "parent": t.string(),
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
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
                "labels": t.struct({"_": t.string().optional()}).optional(),
                "domainName": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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

    return Import(
        importer="domains", renames=renames, types=Box(types), functions=Box(functions)
    )
