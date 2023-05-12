from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_domains() -> Import:
    domains = HTTPRuntime("https://domains.googleapis.com/")

    renames = {
        "ErrorResponse": "_domains_1_ErrorResponse",
        "TestIamPermissionsRequestIn": "_domains_2_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_domains_3_TestIamPermissionsRequestOut",
        "StatusIn": "_domains_4_StatusIn",
        "StatusOut": "_domains_5_StatusOut",
        "PostalAddressIn": "_domains_6_PostalAddressIn",
        "PostalAddressOut": "_domains_7_PostalAddressOut",
        "AuditConfigIn": "_domains_8_AuditConfigIn",
        "AuditConfigOut": "_domains_9_AuditConfigOut",
        "MoneyIn": "_domains_10_MoneyIn",
        "MoneyOut": "_domains_11_MoneyOut",
        "RegistrationIn": "_domains_12_RegistrationIn",
        "RegistrationOut": "_domains_13_RegistrationOut",
        "TransferDomainRequestIn": "_domains_14_TransferDomainRequestIn",
        "TransferDomainRequestOut": "_domains_15_TransferDomainRequestOut",
        "RegisterDomainRequestIn": "_domains_16_RegisterDomainRequestIn",
        "RegisterDomainRequestOut": "_domains_17_RegisterDomainRequestOut",
        "OperationIn": "_domains_18_OperationIn",
        "OperationOut": "_domains_19_OperationOut",
        "ExprIn": "_domains_20_ExprIn",
        "ExprOut": "_domains_21_ExprOut",
        "DnsSettingsIn": "_domains_22_DnsSettingsIn",
        "DnsSettingsOut": "_domains_23_DnsSettingsOut",
        "TestIamPermissionsResponseIn": "_domains_24_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_domains_25_TestIamPermissionsResponseOut",
        "AuthorizationCodeIn": "_domains_26_AuthorizationCodeIn",
        "AuthorizationCodeOut": "_domains_27_AuthorizationCodeOut",
        "ListLocationsResponseIn": "_domains_28_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_domains_29_ListLocationsResponseOut",
        "SetIamPolicyRequestIn": "_domains_30_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_domains_31_SetIamPolicyRequestOut",
        "LocationIn": "_domains_32_LocationIn",
        "LocationOut": "_domains_33_LocationOut",
        "TransferParametersIn": "_domains_34_TransferParametersIn",
        "TransferParametersOut": "_domains_35_TransferParametersOut",
        "ListRegistrationsResponseIn": "_domains_36_ListRegistrationsResponseIn",
        "ListRegistrationsResponseOut": "_domains_37_ListRegistrationsResponseOut",
        "ManagementSettingsIn": "_domains_38_ManagementSettingsIn",
        "ManagementSettingsOut": "_domains_39_ManagementSettingsOut",
        "ImportDomainRequestIn": "_domains_40_ImportDomainRequestIn",
        "ImportDomainRequestOut": "_domains_41_ImportDomainRequestOut",
        "ContactIn": "_domains_42_ContactIn",
        "ContactOut": "_domains_43_ContactOut",
        "PolicyIn": "_domains_44_PolicyIn",
        "PolicyOut": "_domains_45_PolicyOut",
        "BindingIn": "_domains_46_BindingIn",
        "BindingOut": "_domains_47_BindingOut",
        "RetrieveTransferParametersResponseIn": "_domains_48_RetrieveTransferParametersResponseIn",
        "RetrieveTransferParametersResponseOut": "_domains_49_RetrieveTransferParametersResponseOut",
        "ConfigureContactSettingsRequestIn": "_domains_50_ConfigureContactSettingsRequestIn",
        "ConfigureContactSettingsRequestOut": "_domains_51_ConfigureContactSettingsRequestOut",
        "SearchDomainsResponseIn": "_domains_52_SearchDomainsResponseIn",
        "SearchDomainsResponseOut": "_domains_53_SearchDomainsResponseOut",
        "ContactSettingsIn": "_domains_54_ContactSettingsIn",
        "ContactSettingsOut": "_domains_55_ContactSettingsOut",
        "DomainIn": "_domains_56_DomainIn",
        "DomainOut": "_domains_57_DomainOut",
        "GoogleDomainsDnsIn": "_domains_58_GoogleDomainsDnsIn",
        "GoogleDomainsDnsOut": "_domains_59_GoogleDomainsDnsOut",
        "RetrieveImportableDomainsResponseIn": "_domains_60_RetrieveImportableDomainsResponseIn",
        "RetrieveImportableDomainsResponseOut": "_domains_61_RetrieveImportableDomainsResponseOut",
        "OperationMetadataIn": "_domains_62_OperationMetadataIn",
        "OperationMetadataOut": "_domains_63_OperationMetadataOut",
        "ListOperationsResponseIn": "_domains_64_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_domains_65_ListOperationsResponseOut",
        "ExportRegistrationRequestIn": "_domains_66_ExportRegistrationRequestIn",
        "ExportRegistrationRequestOut": "_domains_67_ExportRegistrationRequestOut",
        "ResetAuthorizationCodeRequestIn": "_domains_68_ResetAuthorizationCodeRequestIn",
        "ResetAuthorizationCodeRequestOut": "_domains_69_ResetAuthorizationCodeRequestOut",
        "ConfigureDnsSettingsRequestIn": "_domains_70_ConfigureDnsSettingsRequestIn",
        "ConfigureDnsSettingsRequestOut": "_domains_71_ConfigureDnsSettingsRequestOut",
        "RetrieveRegisterParametersResponseIn": "_domains_72_RetrieveRegisterParametersResponseIn",
        "RetrieveRegisterParametersResponseOut": "_domains_73_RetrieveRegisterParametersResponseOut",
        "ConfigureManagementSettingsRequestIn": "_domains_74_ConfigureManagementSettingsRequestIn",
        "ConfigureManagementSettingsRequestOut": "_domains_75_ConfigureManagementSettingsRequestOut",
        "RegisterParametersIn": "_domains_76_RegisterParametersIn",
        "RegisterParametersOut": "_domains_77_RegisterParametersOut",
        "GlueRecordIn": "_domains_78_GlueRecordIn",
        "GlueRecordOut": "_domains_79_GlueRecordOut",
        "AuditLogConfigIn": "_domains_80_AuditLogConfigIn",
        "AuditLogConfigOut": "_domains_81_AuditLogConfigOut",
        "DsRecordIn": "_domains_82_DsRecordIn",
        "DsRecordOut": "_domains_83_DsRecordOut",
        "CustomDnsIn": "_domains_84_CustomDnsIn",
        "CustomDnsOut": "_domains_85_CustomDnsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["PostalAddressIn"] = t.struct(
        {
            "sortingCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "regionCode": t.string(),
            "organization": t.string().optional(),
            "languageCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "locality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "sortingCode": t.string().optional(),
            "postalCode": t.string().optional(),
            "sublocality": t.string().optional(),
            "regionCode": t.string(),
            "organization": t.string().optional(),
            "languageCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "locality": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "administrativeArea": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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
    types["RegistrationIn"] = t.struct(
        {
            "dnsSettings": t.proxy(renames["DnsSettingsIn"]).optional(),
            "contactSettings": t.proxy(renames["ContactSettingsIn"]),
            "domainName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "managementSettings": t.proxy(renames["ManagementSettingsIn"]).optional(),
        }
    ).named(renames["RegistrationIn"])
    types["RegistrationOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "dnsSettings": t.proxy(renames["DnsSettingsOut"]).optional(),
            "pendingContactSettings": t.proxy(renames["ContactSettingsOut"]).optional(),
            "registerFailureReason": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "issues": t.array(t.string()).optional(),
            "expireTime": t.string().optional(),
            "name": t.string().optional(),
            "contactSettings": t.proxy(renames["ContactSettingsOut"]),
            "domainName": t.string(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "transferFailureReason": t.string().optional(),
            "state": t.string().optional(),
            "managementSettings": t.proxy(renames["ManagementSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegistrationOut"])
    types["TransferDomainRequestIn"] = t.struct(
        {
            "registration": t.proxy(renames["RegistrationIn"]),
            "authorizationCode": t.proxy(renames["AuthorizationCodeIn"]).optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]),
            "validateOnly": t.boolean().optional(),
            "contactNotices": t.array(t.string()).optional(),
        }
    ).named(renames["TransferDomainRequestIn"])
    types["TransferDomainRequestOut"] = t.struct(
        {
            "registration": t.proxy(renames["RegistrationOut"]),
            "authorizationCode": t.proxy(renames["AuthorizationCodeOut"]).optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]),
            "validateOnly": t.boolean().optional(),
            "contactNotices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferDomainRequestOut"])
    types["RegisterDomainRequestIn"] = t.struct(
        {
            "yearlyPrice": t.proxy(renames["MoneyIn"]),
            "validateOnly": t.boolean().optional(),
            "registration": t.proxy(renames["RegistrationIn"]),
            "domainNotices": t.array(t.string()).optional(),
            "contactNotices": t.array(t.string()).optional(),
        }
    ).named(renames["RegisterDomainRequestIn"])
    types["RegisterDomainRequestOut"] = t.struct(
        {
            "yearlyPrice": t.proxy(renames["MoneyOut"]),
            "validateOnly": t.boolean().optional(),
            "registration": t.proxy(renames["RegistrationOut"]),
            "domainNotices": t.array(t.string()).optional(),
            "contactNotices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterDomainRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["DnsSettingsIn"] = t.struct(
        {
            "googleDomainsDns": t.proxy(renames["GoogleDomainsDnsIn"]).optional(),
            "glueRecords": t.array(t.proxy(renames["GlueRecordIn"])).optional(),
            "customDns": t.proxy(renames["CustomDnsIn"]).optional(),
        }
    ).named(renames["DnsSettingsIn"])
    types["DnsSettingsOut"] = t.struct(
        {
            "googleDomainsDns": t.proxy(renames["GoogleDomainsDnsOut"]).optional(),
            "glueRecords": t.array(t.proxy(renames["GlueRecordOut"])).optional(),
            "customDns": t.proxy(renames["CustomDnsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsSettingsOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["AuthorizationCodeIn"] = t.struct({"code": t.string().optional()}).named(
        renames["AuthorizationCodeIn"]
    )
    types["AuthorizationCodeOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationCodeOut"])
    types["ListLocationsResponseIn"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLocationsResponseIn"])
    types["ListLocationsResponseOut"] = t.struct(
        {
            "locations": t.array(t.proxy(renames["LocationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLocationsResponseOut"])
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
    types["LocationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "displayName": t.string().optional(),
            "locationId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
    types["TransferParametersIn"] = t.struct(
        {
            "supportedPrivacy": t.array(t.string()).optional(),
            "currentRegistrar": t.string().optional(),
            "nameServers": t.array(t.string()).optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "transferLockState": t.string().optional(),
            "currentRegistrarUri": t.string().optional(),
            "domainName": t.string().optional(),
        }
    ).named(renames["TransferParametersIn"])
    types["TransferParametersOut"] = t.struct(
        {
            "supportedPrivacy": t.array(t.string()).optional(),
            "currentRegistrar": t.string().optional(),
            "nameServers": t.array(t.string()).optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "transferLockState": t.string().optional(),
            "currentRegistrarUri": t.string().optional(),
            "domainName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferParametersOut"])
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
    types["ContactIn"] = t.struct(
        {
            "faxNumber": t.string().optional(),
            "postalAddress": t.proxy(renames["PostalAddressIn"]),
            "email": t.string(),
            "phoneNumber": t.string(),
        }
    ).named(renames["ContactIn"])
    types["ContactOut"] = t.struct(
        {
            "faxNumber": t.string().optional(),
            "postalAddress": t.proxy(renames["PostalAddressOut"]),
            "email": t.string(),
            "phoneNumber": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["RetrieveTransferParametersResponseIn"] = t.struct(
        {"transferParameters": t.proxy(renames["TransferParametersIn"]).optional()}
    ).named(renames["RetrieveTransferParametersResponseIn"])
    types["RetrieveTransferParametersResponseOut"] = t.struct(
        {
            "transferParameters": t.proxy(renames["TransferParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveTransferParametersResponseOut"])
    types["ConfigureContactSettingsRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "contactNotices": t.array(t.string()).optional(),
            "updateMask": t.string(),
            "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
        }
    ).named(renames["ConfigureContactSettingsRequestIn"])
    types["ConfigureContactSettingsRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "contactNotices": t.array(t.string()).optional(),
            "updateMask": t.string(),
            "contactSettings": t.proxy(renames["ContactSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigureContactSettingsRequestOut"])
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
    types["ContactSettingsIn"] = t.struct(
        {
            "registrantContact": t.proxy(renames["ContactIn"]),
            "technicalContact": t.proxy(renames["ContactIn"]),
            "adminContact": t.proxy(renames["ContactIn"]),
            "privacy": t.string(),
        }
    ).named(renames["ContactSettingsIn"])
    types["ContactSettingsOut"] = t.struct(
        {
            "registrantContact": t.proxy(renames["ContactOut"]),
            "technicalContact": t.proxy(renames["ContactOut"]),
            "adminContact": t.proxy(renames["ContactOut"]),
            "privacy": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactSettingsOut"])
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
    types["OperationMetadataIn"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "endTime": t.string().optional(),
            "createTime": t.string().optional(),
            "verb": t.string().optional(),
            "apiVersion": t.string().optional(),
            "target": t.string().optional(),
            "statusDetail": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["ExportRegistrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportRegistrationRequestIn"]
    )
    types["ExportRegistrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportRegistrationRequestOut"])
    types["ResetAuthorizationCodeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResetAuthorizationCodeRequestIn"])
    types["ResetAuthorizationCodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetAuthorizationCodeRequestOut"])
    types["ConfigureDnsSettingsRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "updateMask": t.string(),
            "dnsSettings": t.proxy(renames["DnsSettingsIn"]).optional(),
        }
    ).named(renames["ConfigureDnsSettingsRequestIn"])
    types["ConfigureDnsSettingsRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "updateMask": t.string(),
            "dnsSettings": t.proxy(renames["DnsSettingsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConfigureDnsSettingsRequestOut"])
    types["RetrieveRegisterParametersResponseIn"] = t.struct(
        {"registerParameters": t.proxy(renames["RegisterParametersIn"]).optional()}
    ).named(renames["RetrieveRegisterParametersResponseIn"])
    types["RetrieveRegisterParametersResponseOut"] = t.struct(
        {
            "registerParameters": t.proxy(renames["RegisterParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveRegisterParametersResponseOut"])
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
    types["RegisterParametersIn"] = t.struct(
        {
            "availability": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "domainNotices": t.array(t.string()).optional(),
            "domainName": t.string().optional(),
        }
    ).named(renames["RegisterParametersIn"])
    types["RegisterParametersOut"] = t.struct(
        {
            "availability": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "domainNotices": t.array(t.string()).optional(),
            "domainName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterParametersOut"])
    types["GlueRecordIn"] = t.struct(
        {
            "ipv4Addresses": t.array(t.string()).optional(),
            "ipv6Addresses": t.array(t.string()).optional(),
            "hostName": t.string(),
        }
    ).named(renames["GlueRecordIn"])
    types["GlueRecordOut"] = t.struct(
        {
            "ipv4Addresses": t.array(t.string()).optional(),
            "ipv6Addresses": t.array(t.string()).optional(),
            "hostName": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GlueRecordOut"])
    types["AuditLogConfigIn"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
        }
    ).named(renames["AuditLogConfigIn"])
    types["AuditLogConfigOut"] = t.struct(
        {
            "exemptedMembers": t.array(t.string()).optional(),
            "logType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuditLogConfigOut"])
    types["DsRecordIn"] = t.struct(
        {
            "digestType": t.string().optional(),
            "algorithm": t.string().optional(),
            "digest": t.string().optional(),
            "keyTag": t.integer().optional(),
        }
    ).named(renames["DsRecordIn"])
    types["DsRecordOut"] = t.struct(
        {
            "digestType": t.string().optional(),
            "algorithm": t.string().optional(),
            "digest": t.string().optional(),
            "keyTag": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DsRecordOut"])
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

    functions = {}
    functions["projectsLocationsGet"] = domains.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsList"] = domains.get(
        "v1/{name}/locations",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLocationsResponseOut"]),
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
    functions["projectsLocationsRegistrationsConfigureDnsSettings"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsDelete"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsPatch"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRetrieveAuthorizationCode"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsGetIamPolicy"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRetrieveImportableDomains"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsExport"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsSearchDomains"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRegistrationsRetrieveRegisterParameters"
    ] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsList"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsImport"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsConfigureContactSettings"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsTestIamPermissions"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsGet"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRegistrationsRetrieveTransferParameters"
    ] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsTransfer"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "projectsLocationsRegistrationsConfigureManagementSettings"
    ] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsResetAuthorizationCode"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRegister"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsSetIamPolicy"] = domains.post(
        "v1/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "updateMask": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="domains", renames=renames, types=Box(types), functions=Box(functions)
    )
