from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_accesscontextmanager():
    accesscontextmanager = HTTPRuntime("https://accesscontextmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_accesscontextmanager_1_ErrorResponse",
        "MethodSelectorIn": "_accesscontextmanager_2_MethodSelectorIn",
        "MethodSelectorOut": "_accesscontextmanager_3_MethodSelectorOut",
        "AuditLogConfigIn": "_accesscontextmanager_4_AuditLogConfigIn",
        "AuditLogConfigOut": "_accesscontextmanager_5_AuditLogConfigOut",
        "OsConstraintIn": "_accesscontextmanager_6_OsConstraintIn",
        "OsConstraintOut": "_accesscontextmanager_7_OsConstraintOut",
        "IngressFromIn": "_accesscontextmanager_8_IngressFromIn",
        "IngressFromOut": "_accesscontextmanager_9_IngressFromOut",
        "ListAuthorizedOrgsDescsResponseIn": "_accesscontextmanager_10_ListAuthorizedOrgsDescsResponseIn",
        "ListAuthorizedOrgsDescsResponseOut": "_accesscontextmanager_11_ListAuthorizedOrgsDescsResponseOut",
        "ListOperationsResponseIn": "_accesscontextmanager_12_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_accesscontextmanager_13_ListOperationsResponseOut",
        "CommitServicePerimetersRequestIn": "_accesscontextmanager_14_CommitServicePerimetersRequestIn",
        "CommitServicePerimetersRequestOut": "_accesscontextmanager_15_CommitServicePerimetersRequestOut",
        "AuditConfigIn": "_accesscontextmanager_16_AuditConfigIn",
        "AuditConfigOut": "_accesscontextmanager_17_AuditConfigOut",
        "AccessPolicyIn": "_accesscontextmanager_18_AccessPolicyIn",
        "AccessPolicyOut": "_accesscontextmanager_19_AccessPolicyOut",
        "AccessLevelIn": "_accesscontextmanager_20_AccessLevelIn",
        "AccessLevelOut": "_accesscontextmanager_21_AccessLevelOut",
        "GetIamPolicyRequestIn": "_accesscontextmanager_22_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_accesscontextmanager_23_GetIamPolicyRequestOut",
        "IngressPolicyIn": "_accesscontextmanager_24_IngressPolicyIn",
        "IngressPolicyOut": "_accesscontextmanager_25_IngressPolicyOut",
        "CommitServicePerimetersResponseIn": "_accesscontextmanager_26_CommitServicePerimetersResponseIn",
        "CommitServicePerimetersResponseOut": "_accesscontextmanager_27_CommitServicePerimetersResponseOut",
        "TestIamPermissionsResponseIn": "_accesscontextmanager_28_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_accesscontextmanager_29_TestIamPermissionsResponseOut",
        "ListGcpUserAccessBindingsResponseIn": "_accesscontextmanager_30_ListGcpUserAccessBindingsResponseIn",
        "ListGcpUserAccessBindingsResponseOut": "_accesscontextmanager_31_ListGcpUserAccessBindingsResponseOut",
        "OperationIn": "_accesscontextmanager_32_OperationIn",
        "OperationOut": "_accesscontextmanager_33_OperationOut",
        "EgressPolicyIn": "_accesscontextmanager_34_EgressPolicyIn",
        "EgressPolicyOut": "_accesscontextmanager_35_EgressPolicyOut",
        "ReplaceServicePerimetersRequestIn": "_accesscontextmanager_36_ReplaceServicePerimetersRequestIn",
        "ReplaceServicePerimetersRequestOut": "_accesscontextmanager_37_ReplaceServicePerimetersRequestOut",
        "BindingIn": "_accesscontextmanager_38_BindingIn",
        "BindingOut": "_accesscontextmanager_39_BindingOut",
        "DevicePolicyIn": "_accesscontextmanager_40_DevicePolicyIn",
        "DevicePolicyOut": "_accesscontextmanager_41_DevicePolicyOut",
        "ReplaceAccessLevelsRequestIn": "_accesscontextmanager_42_ReplaceAccessLevelsRequestIn",
        "ReplaceAccessLevelsRequestOut": "_accesscontextmanager_43_ReplaceAccessLevelsRequestOut",
        "StatusIn": "_accesscontextmanager_44_StatusIn",
        "StatusOut": "_accesscontextmanager_45_StatusOut",
        "TestIamPermissionsRequestIn": "_accesscontextmanager_46_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_accesscontextmanager_47_TestIamPermissionsRequestOut",
        "GcpUserAccessBindingIn": "_accesscontextmanager_48_GcpUserAccessBindingIn",
        "GcpUserAccessBindingOut": "_accesscontextmanager_49_GcpUserAccessBindingOut",
        "GcpUserAccessBindingOperationMetadataIn": "_accesscontextmanager_50_GcpUserAccessBindingOperationMetadataIn",
        "GcpUserAccessBindingOperationMetadataOut": "_accesscontextmanager_51_GcpUserAccessBindingOperationMetadataOut",
        "EgressToIn": "_accesscontextmanager_52_EgressToIn",
        "EgressToOut": "_accesscontextmanager_53_EgressToOut",
        "CustomLevelIn": "_accesscontextmanager_54_CustomLevelIn",
        "CustomLevelOut": "_accesscontextmanager_55_CustomLevelOut",
        "PolicyIn": "_accesscontextmanager_56_PolicyIn",
        "PolicyOut": "_accesscontextmanager_57_PolicyOut",
        "VpcAccessibleServicesIn": "_accesscontextmanager_58_VpcAccessibleServicesIn",
        "VpcAccessibleServicesOut": "_accesscontextmanager_59_VpcAccessibleServicesOut",
        "ApiOperationIn": "_accesscontextmanager_60_ApiOperationIn",
        "ApiOperationOut": "_accesscontextmanager_61_ApiOperationOut",
        "AccessContextManagerOperationMetadataIn": "_accesscontextmanager_62_AccessContextManagerOperationMetadataIn",
        "AccessContextManagerOperationMetadataOut": "_accesscontextmanager_63_AccessContextManagerOperationMetadataOut",
        "ExprIn": "_accesscontextmanager_64_ExprIn",
        "ExprOut": "_accesscontextmanager_65_ExprOut",
        "CancelOperationRequestIn": "_accesscontextmanager_66_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_accesscontextmanager_67_CancelOperationRequestOut",
        "EmptyIn": "_accesscontextmanager_68_EmptyIn",
        "EmptyOut": "_accesscontextmanager_69_EmptyOut",
        "GetPolicyOptionsIn": "_accesscontextmanager_70_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_accesscontextmanager_71_GetPolicyOptionsOut",
        "ReplaceServicePerimetersResponseIn": "_accesscontextmanager_72_ReplaceServicePerimetersResponseIn",
        "ReplaceServicePerimetersResponseOut": "_accesscontextmanager_73_ReplaceServicePerimetersResponseOut",
        "ServicePerimeterConfigIn": "_accesscontextmanager_74_ServicePerimeterConfigIn",
        "ServicePerimeterConfigOut": "_accesscontextmanager_75_ServicePerimeterConfigOut",
        "SetIamPolicyRequestIn": "_accesscontextmanager_76_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_accesscontextmanager_77_SetIamPolicyRequestOut",
        "ConditionIn": "_accesscontextmanager_78_ConditionIn",
        "ConditionOut": "_accesscontextmanager_79_ConditionOut",
        "ReplaceAccessLevelsResponseIn": "_accesscontextmanager_80_ReplaceAccessLevelsResponseIn",
        "ReplaceAccessLevelsResponseOut": "_accesscontextmanager_81_ReplaceAccessLevelsResponseOut",
        "IngressSourceIn": "_accesscontextmanager_82_IngressSourceIn",
        "IngressSourceOut": "_accesscontextmanager_83_IngressSourceOut",
        "ServicePerimeterIn": "_accesscontextmanager_84_ServicePerimeterIn",
        "ServicePerimeterOut": "_accesscontextmanager_85_ServicePerimeterOut",
        "ListServicePerimetersResponseIn": "_accesscontextmanager_86_ListServicePerimetersResponseIn",
        "ListServicePerimetersResponseOut": "_accesscontextmanager_87_ListServicePerimetersResponseOut",
        "ListAccessPoliciesResponseIn": "_accesscontextmanager_88_ListAccessPoliciesResponseIn",
        "ListAccessPoliciesResponseOut": "_accesscontextmanager_89_ListAccessPoliciesResponseOut",
        "EgressFromIn": "_accesscontextmanager_90_EgressFromIn",
        "EgressFromOut": "_accesscontextmanager_91_EgressFromOut",
        "IngressToIn": "_accesscontextmanager_92_IngressToIn",
        "IngressToOut": "_accesscontextmanager_93_IngressToOut",
        "AuthorizedOrgsDescIn": "_accesscontextmanager_94_AuthorizedOrgsDescIn",
        "AuthorizedOrgsDescOut": "_accesscontextmanager_95_AuthorizedOrgsDescOut",
        "ListAccessLevelsResponseIn": "_accesscontextmanager_96_ListAccessLevelsResponseIn",
        "ListAccessLevelsResponseOut": "_accesscontextmanager_97_ListAccessLevelsResponseOut",
        "BasicLevelIn": "_accesscontextmanager_98_BasicLevelIn",
        "BasicLevelOut": "_accesscontextmanager_99_BasicLevelOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["MethodSelectorIn"] = t.struct(
        {"permission": t.string().optional(), "method": t.string().optional()}
    ).named(renames["MethodSelectorIn"])
    types["MethodSelectorOut"] = t.struct(
        {
            "permission": t.string().optional(),
            "method": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodSelectorOut"])
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
    types["OsConstraintIn"] = t.struct(
        {
            "minimumVersion": t.string().optional(),
            "osType": t.string(),
            "requireVerifiedChromeOs": t.boolean().optional(),
        }
    ).named(renames["OsConstraintIn"])
    types["OsConstraintOut"] = t.struct(
        {
            "minimumVersion": t.string().optional(),
            "osType": t.string(),
            "requireVerifiedChromeOs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsConstraintOut"])
    types["IngressFromIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["IngressSourceIn"])).optional(),
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
        }
    ).named(renames["IngressFromIn"])
    types["IngressFromOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["IngressSourceOut"])).optional(),
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngressFromOut"])
    types["ListAuthorizedOrgsDescsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "authorizedOrgsDescs": t.array(
                t.proxy(renames["AuthorizedOrgsDescIn"])
            ).optional(),
        }
    ).named(renames["ListAuthorizedOrgsDescsResponseIn"])
    types["ListAuthorizedOrgsDescsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "authorizedOrgsDescs": t.array(
                t.proxy(renames["AuthorizedOrgsDescOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAuthorizedOrgsDescsResponseOut"])
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
    types["CommitServicePerimetersRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["CommitServicePerimetersRequestIn"])
    types["CommitServicePerimetersRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitServicePerimetersRequestOut"])
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
    types["AccessPolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "title": t.string(),
            "parent": t.string(),
        }
    ).named(renames["AccessPolicyIn"])
    types["AccessPolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "scopes": t.array(t.string()).optional(),
            "title": t.string(),
            "parent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessPolicyOut"])
    types["AccessLevelIn"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "custom": t.proxy(renames["CustomLevelIn"]).optional(),
            "basic": t.proxy(renames["BasicLevelIn"]).optional(),
        }
    ).named(renames["AccessLevelIn"])
    types["AccessLevelOut"] = t.struct(
        {
            "name": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "custom": t.proxy(renames["CustomLevelOut"]).optional(),
            "basic": t.proxy(renames["BasicLevelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessLevelOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["IngressPolicyIn"] = t.struct(
        {
            "ingressFrom": t.proxy(renames["IngressFromIn"]).optional(),
            "ingressTo": t.proxy(renames["IngressToIn"]).optional(),
        }
    ).named(renames["IngressPolicyIn"])
    types["IngressPolicyOut"] = t.struct(
        {
            "ingressFrom": t.proxy(renames["IngressFromOut"]).optional(),
            "ingressTo": t.proxy(renames["IngressToOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngressPolicyOut"])
    types["CommitServicePerimetersResponseIn"] = t.struct(
        {
            "servicePerimeters": t.array(
                t.proxy(renames["ServicePerimeterIn"])
            ).optional()
        }
    ).named(renames["CommitServicePerimetersResponseIn"])
    types["CommitServicePerimetersResponseOut"] = t.struct(
        {
            "servicePerimeters": t.array(
                t.proxy(renames["ServicePerimeterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitServicePerimetersResponseOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ListGcpUserAccessBindingsResponseIn"] = t.struct(
        {
            "gcpUserAccessBindings": t.array(
                t.proxy(renames["GcpUserAccessBindingIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListGcpUserAccessBindingsResponseIn"])
    types["ListGcpUserAccessBindingsResponseOut"] = t.struct(
        {
            "gcpUserAccessBindings": t.array(
                t.proxy(renames["GcpUserAccessBindingOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGcpUserAccessBindingsResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
        }
    ).named(renames["OperationOut"])
    types["EgressPolicyIn"] = t.struct(
        {
            "egressFrom": t.proxy(renames["EgressFromIn"]).optional(),
            "egressTo": t.proxy(renames["EgressToIn"]).optional(),
        }
    ).named(renames["EgressPolicyIn"])
    types["EgressPolicyOut"] = t.struct(
        {
            "egressFrom": t.proxy(renames["EgressFromOut"]).optional(),
            "egressTo": t.proxy(renames["EgressToOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EgressPolicyOut"])
    types["ReplaceServicePerimetersRequestIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "servicePerimeters": t.array(t.proxy(renames["ServicePerimeterIn"])),
        }
    ).named(renames["ReplaceServicePerimetersRequestIn"])
    types["ReplaceServicePerimetersRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "servicePerimeters": t.array(t.proxy(renames["ServicePerimeterOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceServicePerimetersRequestOut"])
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
    types["DevicePolicyIn"] = t.struct(
        {
            "requireCorpOwned": t.boolean().optional(),
            "requireScreenlock": t.boolean().optional(),
            "requireAdminApproval": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "osConstraints": t.array(t.proxy(renames["OsConstraintIn"])).optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
        }
    ).named(renames["DevicePolicyIn"])
    types["DevicePolicyOut"] = t.struct(
        {
            "requireCorpOwned": t.boolean().optional(),
            "requireScreenlock": t.boolean().optional(),
            "requireAdminApproval": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "osConstraints": t.array(t.proxy(renames["OsConstraintOut"])).optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicePolicyOut"])
    types["ReplaceAccessLevelsRequestIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])),
        }
    ).named(renames["ReplaceAccessLevelsRequestIn"])
    types["ReplaceAccessLevelsRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "accessLevels": t.array(t.proxy(renames["AccessLevelOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAccessLevelsRequestOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["GcpUserAccessBindingIn"] = t.struct(
        {
            "dryRunAccessLevels": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "accessLevels": t.array(t.string()).optional(),
            "groupKey": t.string(),
        }
    ).named(renames["GcpUserAccessBindingIn"])
    types["GcpUserAccessBindingOut"] = t.struct(
        {
            "dryRunAccessLevels": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "accessLevels": t.array(t.string()).optional(),
            "groupKey": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcpUserAccessBindingOut"])
    types["GcpUserAccessBindingOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GcpUserAccessBindingOperationMetadataIn"])
    types["GcpUserAccessBindingOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcpUserAccessBindingOperationMetadataOut"])
    types["EgressToIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["ApiOperationIn"])).optional(),
            "resources": t.array(t.string()).optional(),
            "externalResources": t.array(t.string()).optional(),
        }
    ).named(renames["EgressToIn"])
    types["EgressToOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["ApiOperationOut"])).optional(),
            "resources": t.array(t.string()).optional(),
            "externalResources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EgressToOut"])
    types["CustomLevelIn"] = t.struct({"expr": t.proxy(renames["ExprIn"])}).named(
        renames["CustomLevelIn"]
    )
    types["CustomLevelOut"] = t.struct(
        {
            "expr": t.proxy(renames["ExprOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomLevelOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["VpcAccessibleServicesIn"] = t.struct(
        {
            "allowedServices": t.array(t.string()).optional(),
            "enableRestriction": t.boolean().optional(),
        }
    ).named(renames["VpcAccessibleServicesIn"])
    types["VpcAccessibleServicesOut"] = t.struct(
        {
            "allowedServices": t.array(t.string()).optional(),
            "enableRestriction": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcAccessibleServicesOut"])
    types["ApiOperationIn"] = t.struct(
        {
            "methodSelectors": t.array(t.proxy(renames["MethodSelectorIn"])).optional(),
            "serviceName": t.string().optional(),
        }
    ).named(renames["ApiOperationIn"])
    types["ApiOperationOut"] = t.struct(
        {
            "methodSelectors": t.array(
                t.proxy(renames["MethodSelectorOut"])
            ).optional(),
            "serviceName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOperationOut"])
    types["AccessContextManagerOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AccessContextManagerOperationMetadataIn"])
    types["AccessContextManagerOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AccessContextManagerOperationMetadataOut"])
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["ReplaceServicePerimetersResponseIn"] = t.struct(
        {
            "servicePerimeters": t.array(
                t.proxy(renames["ServicePerimeterIn"])
            ).optional()
        }
    ).named(renames["ReplaceServicePerimetersResponseIn"])
    types["ReplaceServicePerimetersResponseOut"] = t.struct(
        {
            "servicePerimeters": t.array(
                t.proxy(renames["ServicePerimeterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceServicePerimetersResponseOut"])
    types["ServicePerimeterConfigIn"] = t.struct(
        {
            "accessLevels": t.array(t.string()).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "ingressPolicies": t.array(t.proxy(renames["IngressPolicyIn"])).optional(),
            "egressPolicies": t.array(t.proxy(renames["EgressPolicyIn"])).optional(),
            "resources": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["VpcAccessibleServicesIn"]
            ).optional(),
        }
    ).named(renames["ServicePerimeterConfigIn"])
    types["ServicePerimeterConfigOut"] = t.struct(
        {
            "accessLevels": t.array(t.string()).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "ingressPolicies": t.array(t.proxy(renames["IngressPolicyOut"])).optional(),
            "egressPolicies": t.array(t.proxy(renames["EgressPolicyOut"])).optional(),
            "resources": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["VpcAccessibleServicesOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicePerimeterConfigOut"])
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
    types["ConditionIn"] = t.struct(
        {
            "regions": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(renames["DevicePolicyIn"]).optional(),
            "members": t.array(t.string()).optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "regions": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(renames["DevicePolicyOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["ReplaceAccessLevelsResponseIn"] = t.struct(
        {"accessLevels": t.array(t.proxy(renames["AccessLevelIn"])).optional()}
    ).named(renames["ReplaceAccessLevelsResponseIn"])
    types["ReplaceAccessLevelsResponseOut"] = t.struct(
        {
            "accessLevels": t.array(t.proxy(renames["AccessLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAccessLevelsResponseOut"])
    types["IngressSourceIn"] = t.struct(
        {"resource": t.string().optional(), "accessLevel": t.string().optional()}
    ).named(renames["IngressSourceIn"])
    types["IngressSourceOut"] = t.struct(
        {
            "resource": t.string().optional(),
            "accessLevel": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngressSourceOut"])
    types["ServicePerimeterIn"] = t.struct(
        {
            "perimeterType": t.string().optional(),
            "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "description": t.string().optional(),
            "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
        }
    ).named(renames["ServicePerimeterIn"])
    types["ServicePerimeterOut"] = t.struct(
        {
            "perimeterType": t.string().optional(),
            "status": t.proxy(renames["ServicePerimeterConfigOut"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "description": t.string().optional(),
            "spec": t.proxy(renames["ServicePerimeterConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicePerimeterOut"])
    types["ListServicePerimetersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "servicePerimeters": t.array(
                t.proxy(renames["ServicePerimeterIn"])
            ).optional(),
        }
    ).named(renames["ListServicePerimetersResponseIn"])
    types["ListServicePerimetersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "servicePerimeters": t.array(
                t.proxy(renames["ServicePerimeterOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicePerimetersResponseOut"])
    types["ListAccessPoliciesResponseIn"] = t.struct(
        {
            "accessPolicies": t.array(t.proxy(renames["AccessPolicyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAccessPoliciesResponseIn"])
    types["ListAccessPoliciesResponseOut"] = t.struct(
        {
            "accessPolicies": t.array(t.proxy(renames["AccessPolicyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccessPoliciesResponseOut"])
    types["EgressFromIn"] = t.struct(
        {
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
        }
    ).named(renames["EgressFromIn"])
    types["EgressFromOut"] = t.struct(
        {
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EgressFromOut"])
    types["IngressToIn"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "operations": t.array(t.proxy(renames["ApiOperationIn"])).optional(),
        }
    ).named(renames["IngressToIn"])
    types["IngressToOut"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "operations": t.array(t.proxy(renames["ApiOperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngressToOut"])
    types["AuthorizedOrgsDescIn"] = t.struct(
        {
            "orgs": t.array(t.string()).optional(),
            "authorizationDirection": t.string().optional(),
            "name": t.string().optional(),
            "authorizationType": t.string().optional(),
            "assetType": t.string().optional(),
        }
    ).named(renames["AuthorizedOrgsDescIn"])
    types["AuthorizedOrgsDescOut"] = t.struct(
        {
            "orgs": t.array(t.string()).optional(),
            "authorizationDirection": t.string().optional(),
            "name": t.string().optional(),
            "authorizationType": t.string().optional(),
            "assetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedOrgsDescOut"])
    types["ListAccessLevelsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])).optional(),
        }
    ).named(renames["ListAccessLevelsResponseIn"])
    types["ListAccessLevelsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "accessLevels": t.array(t.proxy(renames["AccessLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccessLevelsResponseOut"])
    types["BasicLevelIn"] = t.struct(
        {
            "conditions": t.array(t.proxy(renames["ConditionIn"])),
            "combiningFunction": t.string().optional(),
        }
    ).named(renames["BasicLevelIn"])
    types["BasicLevelOut"] = t.struct(
        {
            "conditions": t.array(t.proxy(renames["ConditionOut"])),
            "combiningFunction": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicLevelOut"])

    functions = {}
    functions["organizationsGcpUserAccessBindingsGet"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsList"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsPatch"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsCreate"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsDelete"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "name": t.string().optional(),
                "filter": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesCreate"] = accesscontextmanager.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesList"] = accesscontextmanager.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesGet"] = accesscontextmanager.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesPatch"] = accesscontextmanager.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesDelete"] = accesscontextmanager.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesTestIamPermissions"] = accesscontextmanager.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesSetIamPolicy"] = accesscontextmanager.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesGetIamPolicy"] = accesscontextmanager.post(
        "v1/{resource}:getIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "options": t.proxy(renames["GetPolicyOptionsIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsDelete"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "orgs": t.array(t.string()).optional(),
                "authorizationDirection": t.string().optional(),
                "authorizationType": t.string().optional(),
                "assetType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsList"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "orgs": t.array(t.string()).optional(),
                "authorizationDirection": t.string().optional(),
                "authorizationType": t.string().optional(),
                "assetType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsCreate"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "orgs": t.array(t.string()).optional(),
                "authorizationDirection": t.string().optional(),
                "authorizationType": t.string().optional(),
                "assetType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsGet"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "orgs": t.array(t.string()).optional(),
                "authorizationDirection": t.string().optional(),
                "authorizationType": t.string().optional(),
                "assetType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsPatch"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "orgs": t.array(t.string()).optional(),
                "authorizationDirection": t.string().optional(),
                "authorizationType": t.string().optional(),
                "assetType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accessPoliciesServicePerimetersTestIamPermissions"
    ] = accesscontextmanager.get(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicePerimetersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersCreate"] = accesscontextmanager.get(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicePerimetersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersDelete"] = accesscontextmanager.get(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicePerimetersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersReplaceAll"] = accesscontextmanager.get(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicePerimetersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersCommit"] = accesscontextmanager.get(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicePerimetersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersPatch"] = accesscontextmanager.get(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicePerimetersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersGet"] = accesscontextmanager.get(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicePerimetersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersList"] = accesscontextmanager.get(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListServicePerimetersResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsReplaceAll"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "title": t.string().optional(),
                "custom": t.proxy(renames["CustomLevelIn"]).optional(),
                "basic": t.proxy(renames["BasicLevelIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsGet"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "title": t.string().optional(),
                "custom": t.proxy(renames["CustomLevelIn"]).optional(),
                "basic": t.proxy(renames["BasicLevelIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsCreate"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "title": t.string().optional(),
                "custom": t.proxy(renames["CustomLevelIn"]).optional(),
                "basic": t.proxy(renames["BasicLevelIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accessPoliciesAccessLevelsTestIamPermissions"
    ] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "title": t.string().optional(),
                "custom": t.proxy(renames["CustomLevelIn"]).optional(),
                "basic": t.proxy(renames["BasicLevelIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsList"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "title": t.string().optional(),
                "custom": t.proxy(renames["CustomLevelIn"]).optional(),
                "basic": t.proxy(renames["BasicLevelIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsDelete"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "title": t.string().optional(),
                "custom": t.proxy(renames["CustomLevelIn"]).optional(),
                "basic": t.proxy(renames["BasicLevelIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsPatch"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "description": t.string().optional(),
                "title": t.string().optional(),
                "custom": t.proxy(renames["CustomLevelIn"]).optional(),
                "basic": t.proxy(renames["BasicLevelIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="accesscontextmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
