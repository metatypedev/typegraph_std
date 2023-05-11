from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_domains() -> Import:
    domains = HTTPRuntime("https://domains.googleapis.com/")

    renames = {
        "ErrorResponse": "_domains_1_ErrorResponse",
        "ContactSettingsIn": "_domains_2_ContactSettingsIn",
        "ContactSettingsOut": "_domains_3_ContactSettingsOut",
        "ResetAuthorizationCodeRequestIn": "_domains_4_ResetAuthorizationCodeRequestIn",
        "ResetAuthorizationCodeRequestOut": "_domains_5_ResetAuthorizationCodeRequestOut",
        "AuthorizationCodeIn": "_domains_6_AuthorizationCodeIn",
        "AuthorizationCodeOut": "_domains_7_AuthorizationCodeOut",
        "RegistrationIn": "_domains_8_RegistrationIn",
        "RegistrationOut": "_domains_9_RegistrationOut",
        "DomainIn": "_domains_10_DomainIn",
        "DomainOut": "_domains_11_DomainOut",
        "ConfigureDnsSettingsRequestIn": "_domains_12_ConfigureDnsSettingsRequestIn",
        "ConfigureDnsSettingsRequestOut": "_domains_13_ConfigureDnsSettingsRequestOut",
        "ListRegistrationsResponseIn": "_domains_14_ListRegistrationsResponseIn",
        "ListRegistrationsResponseOut": "_domains_15_ListRegistrationsResponseOut",
        "ListLocationsResponseIn": "_domains_16_ListLocationsResponseIn",
        "ListLocationsResponseOut": "_domains_17_ListLocationsResponseOut",
        "SearchDomainsResponseIn": "_domains_18_SearchDomainsResponseIn",
        "SearchDomainsResponseOut": "_domains_19_SearchDomainsResponseOut",
        "ExportRegistrationRequestIn": "_domains_20_ExportRegistrationRequestIn",
        "ExportRegistrationRequestOut": "_domains_21_ExportRegistrationRequestOut",
        "MoneyIn": "_domains_22_MoneyIn",
        "MoneyOut": "_domains_23_MoneyOut",
        "TransferDomainRequestIn": "_domains_24_TransferDomainRequestIn",
        "TransferDomainRequestOut": "_domains_25_TransferDomainRequestOut",
        "PostalAddressIn": "_domains_26_PostalAddressIn",
        "PostalAddressOut": "_domains_27_PostalAddressOut",
        "AuditConfigIn": "_domains_28_AuditConfigIn",
        "AuditConfigOut": "_domains_29_AuditConfigOut",
        "GlueRecordIn": "_domains_30_GlueRecordIn",
        "GlueRecordOut": "_domains_31_GlueRecordOut",
        "RegisterParametersIn": "_domains_32_RegisterParametersIn",
        "RegisterParametersOut": "_domains_33_RegisterParametersOut",
        "ImportDomainRequestIn": "_domains_34_ImportDomainRequestIn",
        "ImportDomainRequestOut": "_domains_35_ImportDomainRequestOut",
        "RetrieveRegisterParametersResponseIn": "_domains_36_RetrieveRegisterParametersResponseIn",
        "RetrieveRegisterParametersResponseOut": "_domains_37_RetrieveRegisterParametersResponseOut",
        "TestIamPermissionsResponseIn": "_domains_38_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_domains_39_TestIamPermissionsResponseOut",
        "ConfigureManagementSettingsRequestIn": "_domains_40_ConfigureManagementSettingsRequestIn",
        "ConfigureManagementSettingsRequestOut": "_domains_41_ConfigureManagementSettingsRequestOut",
        "CustomDnsIn": "_domains_42_CustomDnsIn",
        "CustomDnsOut": "_domains_43_CustomDnsOut",
        "TestIamPermissionsRequestIn": "_domains_44_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_domains_45_TestIamPermissionsRequestOut",
        "GoogleDomainsDnsIn": "_domains_46_GoogleDomainsDnsIn",
        "GoogleDomainsDnsOut": "_domains_47_GoogleDomainsDnsOut",
        "RegisterDomainRequestIn": "_domains_48_RegisterDomainRequestIn",
        "RegisterDomainRequestOut": "_domains_49_RegisterDomainRequestOut",
        "PolicyIn": "_domains_50_PolicyIn",
        "PolicyOut": "_domains_51_PolicyOut",
        "DsRecordIn": "_domains_52_DsRecordIn",
        "DsRecordOut": "_domains_53_DsRecordOut",
        "DnsSettingsIn": "_domains_54_DnsSettingsIn",
        "DnsSettingsOut": "_domains_55_DnsSettingsOut",
        "RetrieveTransferParametersResponseIn": "_domains_56_RetrieveTransferParametersResponseIn",
        "RetrieveTransferParametersResponseOut": "_domains_57_RetrieveTransferParametersResponseOut",
        "ListOperationsResponseIn": "_domains_58_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_domains_59_ListOperationsResponseOut",
        "StatusIn": "_domains_60_StatusIn",
        "StatusOut": "_domains_61_StatusOut",
        "BindingIn": "_domains_62_BindingIn",
        "BindingOut": "_domains_63_BindingOut",
        "ConfigureContactSettingsRequestIn": "_domains_64_ConfigureContactSettingsRequestIn",
        "ConfigureContactSettingsRequestOut": "_domains_65_ConfigureContactSettingsRequestOut",
        "SetIamPolicyRequestIn": "_domains_66_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_domains_67_SetIamPolicyRequestOut",
        "AuditLogConfigIn": "_domains_68_AuditLogConfigIn",
        "AuditLogConfigOut": "_domains_69_AuditLogConfigOut",
        "OperationIn": "_domains_70_OperationIn",
        "OperationOut": "_domains_71_OperationOut",
        "OperationMetadataIn": "_domains_72_OperationMetadataIn",
        "OperationMetadataOut": "_domains_73_OperationMetadataOut",
        "ExprIn": "_domains_74_ExprIn",
        "ExprOut": "_domains_75_ExprOut",
        "RetrieveImportableDomainsResponseIn": "_domains_76_RetrieveImportableDomainsResponseIn",
        "RetrieveImportableDomainsResponseOut": "_domains_77_RetrieveImportableDomainsResponseOut",
        "TransferParametersIn": "_domains_78_TransferParametersIn",
        "TransferParametersOut": "_domains_79_TransferParametersOut",
        "ContactIn": "_domains_80_ContactIn",
        "ContactOut": "_domains_81_ContactOut",
        "LocationIn": "_domains_82_LocationIn",
        "LocationOut": "_domains_83_LocationOut",
        "ManagementSettingsIn": "_domains_84_ManagementSettingsIn",
        "ManagementSettingsOut": "_domains_85_ManagementSettingsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["ContactSettingsIn"] = t.struct(
        {
            "adminContact": t.proxy(renames["ContactIn"]),
            "privacy": t.string(),
            "technicalContact": t.proxy(renames["ContactIn"]),
            "registrantContact": t.proxy(renames["ContactIn"]),
        }
    ).named(renames["ContactSettingsIn"])
    types["ContactSettingsOut"] = t.struct(
        {
            "adminContact": t.proxy(renames["ContactOut"]),
            "privacy": t.string(),
            "technicalContact": t.proxy(renames["ContactOut"]),
            "registrantContact": t.proxy(renames["ContactOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ContactSettingsOut"])
    types["ResetAuthorizationCodeRequestIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["ResetAuthorizationCodeRequestIn"])
    types["ResetAuthorizationCodeRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ResetAuthorizationCodeRequestOut"])
    types["AuthorizationCodeIn"] = t.struct({"code": t.string().optional()}).named(
        renames["AuthorizationCodeIn"]
    )
    types["AuthorizationCodeOut"] = t.struct(
        {
            "code": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizationCodeOut"])
    types["RegistrationIn"] = t.struct(
        {
            "contactSettings": t.proxy(renames["ContactSettingsIn"]),
            "dnsSettings": t.proxy(renames["DnsSettingsIn"]).optional(),
            "domainName": t.string(),
            "managementSettings": t.proxy(renames["ManagementSettingsIn"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["RegistrationIn"])
    types["RegistrationOut"] = t.struct(
        {
            "contactSettings": t.proxy(renames["ContactSettingsOut"]),
            "state": t.string().optional(),
            "expireTime": t.string().optional(),
            "dnsSettings": t.proxy(renames["DnsSettingsOut"]).optional(),
            "pendingContactSettings": t.proxy(renames["ContactSettingsOut"]).optional(),
            "domainName": t.string(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "registerFailureReason": t.string().optional(),
            "transferFailureReason": t.string().optional(),
            "createTime": t.string().optional(),
            "managementSettings": t.proxy(renames["ManagementSettingsOut"]).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "issues": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegistrationOut"])
    types["DomainIn"] = t.struct(
        {
            "resourceState": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "domainName": t.string().optional(),
        }
    ).named(renames["DomainIn"])
    types["DomainOut"] = t.struct(
        {
            "resourceState": t.string().optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "domainName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DomainOut"])
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
    types["ListRegistrationsResponseIn"] = t.struct(
        {
            "registrations": t.array(t.proxy(renames["RegistrationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListRegistrationsResponseIn"])
    types["ListRegistrationsResponseOut"] = t.struct(
        {
            "registrations": t.array(t.proxy(renames["RegistrationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListRegistrationsResponseOut"])
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
    types["ExportRegistrationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["ExportRegistrationRequestIn"]
    )
    types["ExportRegistrationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["ExportRegistrationRequestOut"])
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
    types["TransferDomainRequestIn"] = t.struct(
        {
            "authorizationCode": t.proxy(renames["AuthorizationCodeIn"]).optional(),
            "contactNotices": t.array(t.string()).optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]),
            "registration": t.proxy(renames["RegistrationIn"]),
            "validateOnly": t.boolean().optional(),
        }
    ).named(renames["TransferDomainRequestIn"])
    types["TransferDomainRequestOut"] = t.struct(
        {
            "authorizationCode": t.proxy(renames["AuthorizationCodeOut"]).optional(),
            "contactNotices": t.array(t.string()).optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]),
            "registration": t.proxy(renames["RegistrationOut"]),
            "validateOnly": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferDomainRequestOut"])
    types["PostalAddressIn"] = t.struct(
        {
            "sortingCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "languageCode": t.string().optional(),
            "regionCode": t.string(),
            "postalCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
        }
    ).named(renames["PostalAddressIn"])
    types["PostalAddressOut"] = t.struct(
        {
            "sortingCode": t.string().optional(),
            "recipients": t.array(t.string()).optional(),
            "organization": t.string().optional(),
            "administrativeArea": t.string().optional(),
            "languageCode": t.string().optional(),
            "regionCode": t.string(),
            "postalCode": t.string().optional(),
            "addressLines": t.array(t.string()).optional(),
            "revision": t.integer().optional(),
            "locality": t.string().optional(),
            "sublocality": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PostalAddressOut"])
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
    types["RegisterParametersIn"] = t.struct(
        {
            "supportedPrivacy": t.array(t.string()).optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "availability": t.string().optional(),
            "domainNotices": t.array(t.string()).optional(),
            "domainName": t.string().optional(),
        }
    ).named(renames["RegisterParametersIn"])
    types["RegisterParametersOut"] = t.struct(
        {
            "supportedPrivacy": t.array(t.string()).optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "availability": t.string().optional(),
            "domainNotices": t.array(t.string()).optional(),
            "domainName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterParametersOut"])
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
    types["RetrieveRegisterParametersResponseIn"] = t.struct(
        {"registerParameters": t.proxy(renames["RegisterParametersIn"]).optional()}
    ).named(renames["RetrieveRegisterParametersResponseIn"])
    types["RetrieveRegisterParametersResponseOut"] = t.struct(
        {
            "registerParameters": t.proxy(renames["RegisterParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveRegisterParametersResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["RegisterDomainRequestIn"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "domainNotices": t.array(t.string()).optional(),
            "contactNotices": t.array(t.string()).optional(),
            "registration": t.proxy(renames["RegistrationIn"]),
            "yearlyPrice": t.proxy(renames["MoneyIn"]),
        }
    ).named(renames["RegisterDomainRequestIn"])
    types["RegisterDomainRequestOut"] = t.struct(
        {
            "validateOnly": t.boolean().optional(),
            "domainNotices": t.array(t.string()).optional(),
            "contactNotices": t.array(t.string()).optional(),
            "registration": t.proxy(renames["RegistrationOut"]),
            "yearlyPrice": t.proxy(renames["MoneyOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RegisterDomainRequestOut"])
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
    types["DsRecordIn"] = t.struct(
        {
            "digest": t.string().optional(),
            "algorithm": t.string().optional(),
            "keyTag": t.integer().optional(),
            "digestType": t.string().optional(),
        }
    ).named(renames["DsRecordIn"])
    types["DsRecordOut"] = t.struct(
        {
            "digest": t.string().optional(),
            "algorithm": t.string().optional(),
            "keyTag": t.integer().optional(),
            "digestType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DsRecordOut"])
    types["DnsSettingsIn"] = t.struct(
        {
            "googleDomainsDns": t.proxy(renames["GoogleDomainsDnsIn"]).optional(),
            "customDns": t.proxy(renames["CustomDnsIn"]).optional(),
            "glueRecords": t.array(t.proxy(renames["GlueRecordIn"])).optional(),
        }
    ).named(renames["DnsSettingsIn"])
    types["DnsSettingsOut"] = t.struct(
        {
            "googleDomainsDns": t.proxy(renames["GoogleDomainsDnsOut"]).optional(),
            "customDns": t.proxy(renames["CustomDnsOut"]).optional(),
            "glueRecords": t.array(t.proxy(renames["GlueRecordOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DnsSettingsOut"])
    types["RetrieveTransferParametersResponseIn"] = t.struct(
        {"transferParameters": t.proxy(renames["TransferParametersIn"]).optional()}
    ).named(renames["RetrieveTransferParametersResponseIn"])
    types["RetrieveTransferParametersResponseOut"] = t.struct(
        {
            "transferParameters": t.proxy(renames["TransferParametersOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["RetrieveTransferParametersResponseOut"])
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
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["SetIamPolicyRequestIn"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyIn"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestIn"])
    types["SetIamPolicyRequestOut"] = t.struct(
        {
            "updateMask": t.string().optional(),
            "policy": t.proxy(renames["PolicyOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SetIamPolicyRequestOut"])
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
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
    types["OperationMetadataIn"] = t.struct(
        {
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
        }
    ).named(renames["OperationMetadataIn"])
    types["OperationMetadataOut"] = t.struct(
        {
            "verb": t.string().optional(),
            "target": t.string().optional(),
            "createTime": t.string().optional(),
            "apiVersion": t.string().optional(),
            "statusDetail": t.string().optional(),
            "endTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationMetadataOut"])
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
    types["TransferParametersIn"] = t.struct(
        {
            "transferLockState": t.string().optional(),
            "currentRegistrar": t.string().optional(),
            "currentRegistrarUri": t.string().optional(),
            "domainName": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "yearlyPrice": t.proxy(renames["MoneyIn"]).optional(),
            "nameServers": t.array(t.string()).optional(),
        }
    ).named(renames["TransferParametersIn"])
    types["TransferParametersOut"] = t.struct(
        {
            "transferLockState": t.string().optional(),
            "currentRegistrar": t.string().optional(),
            "currentRegistrarUri": t.string().optional(),
            "domainName": t.string().optional(),
            "supportedPrivacy": t.array(t.string()).optional(),
            "yearlyPrice": t.proxy(renames["MoneyOut"]).optional(),
            "nameServers": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TransferParametersOut"])
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
    types["LocationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LocationIn"])
    types["LocationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "locationId": t.string().optional(),
            "displayName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LocationOut"])
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
    functions["projectsLocationsRegistrationsPatch"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRetrieveAuthorizationCode"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRegister"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsDelete"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsExport"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsGetIamPolicy"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
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
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsSearchDomains"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsImport"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsSetIamPolicy"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsTransfer"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsTestIamPermissions"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsGet"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
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
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
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
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsList"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsResetAuthorizationCode"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsConfigureDnsSettings"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsRetrieveImportableDomains"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsRegistrationsConfigureContactSettings"] = domains.post(
        "v1/{registration}:configureContactSettings",
        t.struct(
            {
                "registration": t.string(),
                "validateOnly": t.boolean().optional(),
                "contactNotices": t.array(t.string()).optional(),
                "updateMask": t.string(),
                "contactSettings": t.proxy(renames["ContactSettingsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsGet"] = domains.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsLocationsOperationsList"] = domains.get(
        "v1/{name}/operations",
        t.struct(
            {
                "filter": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(importer="domains", renames=renames, types=types, functions=functions)
