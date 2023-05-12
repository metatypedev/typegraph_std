from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_accesscontextmanager() -> Import:
    accesscontextmanager = HTTPRuntime("https://accesscontextmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_accesscontextmanager_1_ErrorResponse",
        "ListAccessLevelsResponseIn": "_accesscontextmanager_2_ListAccessLevelsResponseIn",
        "ListAccessLevelsResponseOut": "_accesscontextmanager_3_ListAccessLevelsResponseOut",
        "GetIamPolicyRequestIn": "_accesscontextmanager_4_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_accesscontextmanager_5_GetIamPolicyRequestOut",
        "ListServicePerimetersResponseIn": "_accesscontextmanager_6_ListServicePerimetersResponseIn",
        "ListServicePerimetersResponseOut": "_accesscontextmanager_7_ListServicePerimetersResponseOut",
        "ExprIn": "_accesscontextmanager_8_ExprIn",
        "ExprOut": "_accesscontextmanager_9_ExprOut",
        "MethodSelectorIn": "_accesscontextmanager_10_MethodSelectorIn",
        "MethodSelectorOut": "_accesscontextmanager_11_MethodSelectorOut",
        "OsConstraintIn": "_accesscontextmanager_12_OsConstraintIn",
        "OsConstraintOut": "_accesscontextmanager_13_OsConstraintOut",
        "PolicyIn": "_accesscontextmanager_14_PolicyIn",
        "PolicyOut": "_accesscontextmanager_15_PolicyOut",
        "ListAuthorizedOrgsDescsResponseIn": "_accesscontextmanager_16_ListAuthorizedOrgsDescsResponseIn",
        "ListAuthorizedOrgsDescsResponseOut": "_accesscontextmanager_17_ListAuthorizedOrgsDescsResponseOut",
        "CommitServicePerimetersResponseIn": "_accesscontextmanager_18_CommitServicePerimetersResponseIn",
        "CommitServicePerimetersResponseOut": "_accesscontextmanager_19_CommitServicePerimetersResponseOut",
        "ListOperationsResponseIn": "_accesscontextmanager_20_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_accesscontextmanager_21_ListOperationsResponseOut",
        "CustomLevelIn": "_accesscontextmanager_22_CustomLevelIn",
        "CustomLevelOut": "_accesscontextmanager_23_CustomLevelOut",
        "AccessLevelIn": "_accesscontextmanager_24_AccessLevelIn",
        "AccessLevelOut": "_accesscontextmanager_25_AccessLevelOut",
        "AccessPolicyIn": "_accesscontextmanager_26_AccessPolicyIn",
        "AccessPolicyOut": "_accesscontextmanager_27_AccessPolicyOut",
        "ConditionIn": "_accesscontextmanager_28_ConditionIn",
        "ConditionOut": "_accesscontextmanager_29_ConditionOut",
        "IngressSourceIn": "_accesscontextmanager_30_IngressSourceIn",
        "IngressSourceOut": "_accesscontextmanager_31_IngressSourceOut",
        "ReplaceServicePerimetersRequestIn": "_accesscontextmanager_32_ReplaceServicePerimetersRequestIn",
        "ReplaceServicePerimetersRequestOut": "_accesscontextmanager_33_ReplaceServicePerimetersRequestOut",
        "TestIamPermissionsRequestIn": "_accesscontextmanager_34_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_accesscontextmanager_35_TestIamPermissionsRequestOut",
        "IngressFromIn": "_accesscontextmanager_36_IngressFromIn",
        "IngressFromOut": "_accesscontextmanager_37_IngressFromOut",
        "TestIamPermissionsResponseIn": "_accesscontextmanager_38_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_accesscontextmanager_39_TestIamPermissionsResponseOut",
        "CancelOperationRequestIn": "_accesscontextmanager_40_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_accesscontextmanager_41_CancelOperationRequestOut",
        "GetPolicyOptionsIn": "_accesscontextmanager_42_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_accesscontextmanager_43_GetPolicyOptionsOut",
        "EmptyIn": "_accesscontextmanager_44_EmptyIn",
        "EmptyOut": "_accesscontextmanager_45_EmptyOut",
        "AccessContextManagerOperationMetadataIn": "_accesscontextmanager_46_AccessContextManagerOperationMetadataIn",
        "AccessContextManagerOperationMetadataOut": "_accesscontextmanager_47_AccessContextManagerOperationMetadataOut",
        "EgressFromIn": "_accesscontextmanager_48_EgressFromIn",
        "EgressFromOut": "_accesscontextmanager_49_EgressFromOut",
        "IngressPolicyIn": "_accesscontextmanager_50_IngressPolicyIn",
        "IngressPolicyOut": "_accesscontextmanager_51_IngressPolicyOut",
        "DevicePolicyIn": "_accesscontextmanager_52_DevicePolicyIn",
        "DevicePolicyOut": "_accesscontextmanager_53_DevicePolicyOut",
        "AuditLogConfigIn": "_accesscontextmanager_54_AuditLogConfigIn",
        "AuditLogConfigOut": "_accesscontextmanager_55_AuditLogConfigOut",
        "StatusIn": "_accesscontextmanager_56_StatusIn",
        "StatusOut": "_accesscontextmanager_57_StatusOut",
        "SetIamPolicyRequestIn": "_accesscontextmanager_58_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_accesscontextmanager_59_SetIamPolicyRequestOut",
        "ReplaceAccessLevelsRequestIn": "_accesscontextmanager_60_ReplaceAccessLevelsRequestIn",
        "ReplaceAccessLevelsRequestOut": "_accesscontextmanager_61_ReplaceAccessLevelsRequestOut",
        "ApiOperationIn": "_accesscontextmanager_62_ApiOperationIn",
        "ApiOperationOut": "_accesscontextmanager_63_ApiOperationOut",
        "ListAccessPoliciesResponseIn": "_accesscontextmanager_64_ListAccessPoliciesResponseIn",
        "ListAccessPoliciesResponseOut": "_accesscontextmanager_65_ListAccessPoliciesResponseOut",
        "EgressPolicyIn": "_accesscontextmanager_66_EgressPolicyIn",
        "EgressPolicyOut": "_accesscontextmanager_67_EgressPolicyOut",
        "BasicLevelIn": "_accesscontextmanager_68_BasicLevelIn",
        "BasicLevelOut": "_accesscontextmanager_69_BasicLevelOut",
        "ListGcpUserAccessBindingsResponseIn": "_accesscontextmanager_70_ListGcpUserAccessBindingsResponseIn",
        "ListGcpUserAccessBindingsResponseOut": "_accesscontextmanager_71_ListGcpUserAccessBindingsResponseOut",
        "BindingIn": "_accesscontextmanager_72_BindingIn",
        "BindingOut": "_accesscontextmanager_73_BindingOut",
        "AuditConfigIn": "_accesscontextmanager_74_AuditConfigIn",
        "AuditConfigOut": "_accesscontextmanager_75_AuditConfigOut",
        "ReplaceServicePerimetersResponseIn": "_accesscontextmanager_76_ReplaceServicePerimetersResponseIn",
        "ReplaceServicePerimetersResponseOut": "_accesscontextmanager_77_ReplaceServicePerimetersResponseOut",
        "ReplaceAccessLevelsResponseIn": "_accesscontextmanager_78_ReplaceAccessLevelsResponseIn",
        "ReplaceAccessLevelsResponseOut": "_accesscontextmanager_79_ReplaceAccessLevelsResponseOut",
        "EgressToIn": "_accesscontextmanager_80_EgressToIn",
        "EgressToOut": "_accesscontextmanager_81_EgressToOut",
        "VpcAccessibleServicesIn": "_accesscontextmanager_82_VpcAccessibleServicesIn",
        "VpcAccessibleServicesOut": "_accesscontextmanager_83_VpcAccessibleServicesOut",
        "OperationIn": "_accesscontextmanager_84_OperationIn",
        "OperationOut": "_accesscontextmanager_85_OperationOut",
        "ServicePerimeterIn": "_accesscontextmanager_86_ServicePerimeterIn",
        "ServicePerimeterOut": "_accesscontextmanager_87_ServicePerimeterOut",
        "CommitServicePerimetersRequestIn": "_accesscontextmanager_88_CommitServicePerimetersRequestIn",
        "CommitServicePerimetersRequestOut": "_accesscontextmanager_89_CommitServicePerimetersRequestOut",
        "IngressToIn": "_accesscontextmanager_90_IngressToIn",
        "IngressToOut": "_accesscontextmanager_91_IngressToOut",
        "AuthorizedOrgsDescIn": "_accesscontextmanager_92_AuthorizedOrgsDescIn",
        "AuthorizedOrgsDescOut": "_accesscontextmanager_93_AuthorizedOrgsDescOut",
        "GcpUserAccessBindingIn": "_accesscontextmanager_94_GcpUserAccessBindingIn",
        "GcpUserAccessBindingOut": "_accesscontextmanager_95_GcpUserAccessBindingOut",
        "GcpUserAccessBindingOperationMetadataIn": "_accesscontextmanager_96_GcpUserAccessBindingOperationMetadataIn",
        "GcpUserAccessBindingOperationMetadataOut": "_accesscontextmanager_97_GcpUserAccessBindingOperationMetadataOut",
        "ServicePerimeterConfigIn": "_accesscontextmanager_98_ServicePerimeterConfigIn",
        "ServicePerimeterConfigOut": "_accesscontextmanager_99_ServicePerimeterConfigOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["ListServicePerimetersResponseIn"] = t.struct(
        {
            "servicePerimeters": t.array(
                t.proxy(renames["ServicePerimeterIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListServicePerimetersResponseIn"])
    types["ListServicePerimetersResponseOut"] = t.struct(
        {
            "servicePerimeters": t.array(
                t.proxy(renames["ServicePerimeterOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListServicePerimetersResponseOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "location": t.string().optional(),
            "expression": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["MethodSelectorIn"] = t.struct(
        {"method": t.string().optional(), "permission": t.string().optional()}
    ).named(renames["MethodSelectorIn"])
    types["MethodSelectorOut"] = t.struct(
        {
            "method": t.string().optional(),
            "permission": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MethodSelectorOut"])
    types["OsConstraintIn"] = t.struct(
        {
            "osType": t.string(),
            "minimumVersion": t.string().optional(),
            "requireVerifiedChromeOs": t.boolean().optional(),
        }
    ).named(renames["OsConstraintIn"])
    types["OsConstraintOut"] = t.struct(
        {
            "osType": t.string(),
            "minimumVersion": t.string().optional(),
            "requireVerifiedChromeOs": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsConstraintOut"])
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["ListAuthorizedOrgsDescsResponseIn"] = t.struct(
        {
            "authorizedOrgsDescs": t.array(
                t.proxy(renames["AuthorizedOrgsDescIn"])
            ).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAuthorizedOrgsDescsResponseIn"])
    types["ListAuthorizedOrgsDescsResponseOut"] = t.struct(
        {
            "authorizedOrgsDescs": t.array(
                t.proxy(renames["AuthorizedOrgsDescOut"])
            ).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAuthorizedOrgsDescsResponseOut"])
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
    types["CustomLevelIn"] = t.struct({"expr": t.proxy(renames["ExprIn"])}).named(
        renames["CustomLevelIn"]
    )
    types["CustomLevelOut"] = t.struct(
        {
            "expr": t.proxy(renames["ExprOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomLevelOut"])
    types["AccessLevelIn"] = t.struct(
        {
            "basic": t.proxy(renames["BasicLevelIn"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "custom": t.proxy(renames["CustomLevelIn"]).optional(),
        }
    ).named(renames["AccessLevelIn"])
    types["AccessLevelOut"] = t.struct(
        {
            "basic": t.proxy(renames["BasicLevelOut"]).optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "custom": t.proxy(renames["CustomLevelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessLevelOut"])
    types["AccessPolicyIn"] = t.struct(
        {
            "parent": t.string(),
            "name": t.string().optional(),
            "title": t.string(),
            "scopes": t.array(t.string()).optional(),
            "etag": t.string().optional(),
        }
    ).named(renames["AccessPolicyIn"])
    types["AccessPolicyOut"] = t.struct(
        {
            "parent": t.string(),
            "name": t.string().optional(),
            "title": t.string(),
            "scopes": t.array(t.string()).optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessPolicyOut"])
    types["ConditionIn"] = t.struct(
        {
            "devicePolicy": t.proxy(renames["DevicePolicyIn"]).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "members": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "regions": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "devicePolicy": t.proxy(renames["DevicePolicyOut"]).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "members": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "regions": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["IngressSourceIn"] = t.struct(
        {"accessLevel": t.string().optional(), "resource": t.string().optional()}
    ).named(renames["IngressSourceIn"])
    types["IngressSourceOut"] = t.struct(
        {
            "accessLevel": t.string().optional(),
            "resource": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngressSourceOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["IngressFromIn"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["IngressSourceIn"])).optional(),
            "identityType": t.string().optional(),
            "identities": t.array(t.string()).optional(),
        }
    ).named(renames["IngressFromIn"])
    types["IngressFromOut"] = t.struct(
        {
            "sources": t.array(t.proxy(renames["IngressSourceOut"])).optional(),
            "identityType": t.string().optional(),
            "identities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngressFromOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["AccessContextManagerOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AccessContextManagerOperationMetadataIn"])
    types["AccessContextManagerOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AccessContextManagerOperationMetadataOut"])
    types["EgressFromIn"] = t.struct(
        {
            "identityType": t.string().optional(),
            "identities": t.array(t.string()).optional(),
        }
    ).named(renames["EgressFromIn"])
    types["EgressFromOut"] = t.struct(
        {
            "identityType": t.string().optional(),
            "identities": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EgressFromOut"])
    types["IngressPolicyIn"] = t.struct(
        {
            "ingressTo": t.proxy(renames["IngressToIn"]).optional(),
            "ingressFrom": t.proxy(renames["IngressFromIn"]).optional(),
        }
    ).named(renames["IngressPolicyIn"])
    types["IngressPolicyOut"] = t.struct(
        {
            "ingressTo": t.proxy(renames["IngressToOut"]).optional(),
            "ingressFrom": t.proxy(renames["IngressFromOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngressPolicyOut"])
    types["DevicePolicyIn"] = t.struct(
        {
            "requireScreenlock": t.boolean().optional(),
            "osConstraints": t.array(t.proxy(renames["OsConstraintIn"])).optional(),
            "requireCorpOwned": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireAdminApproval": t.boolean().optional(),
        }
    ).named(renames["DevicePolicyIn"])
    types["DevicePolicyOut"] = t.struct(
        {
            "requireScreenlock": t.boolean().optional(),
            "osConstraints": t.array(t.proxy(renames["OsConstraintOut"])).optional(),
            "requireCorpOwned": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicePolicyOut"])
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
    types["ReplaceAccessLevelsRequestIn"] = t.struct(
        {
            "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])),
            "etag": t.string().optional(),
        }
    ).named(renames["ReplaceAccessLevelsRequestIn"])
    types["ReplaceAccessLevelsRequestOut"] = t.struct(
        {
            "accessLevels": t.array(t.proxy(renames["AccessLevelOut"])),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAccessLevelsRequestOut"])
    types["ApiOperationIn"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "methodSelectors": t.array(t.proxy(renames["MethodSelectorIn"])).optional(),
        }
    ).named(renames["ApiOperationIn"])
    types["ApiOperationOut"] = t.struct(
        {
            "serviceName": t.string().optional(),
            "methodSelectors": t.array(
                t.proxy(renames["MethodSelectorOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ApiOperationOut"])
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
    types["ListGcpUserAccessBindingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gcpUserAccessBindings": t.array(
                t.proxy(renames["GcpUserAccessBindingIn"])
            ).optional(),
        }
    ).named(renames["ListGcpUserAccessBindingsResponseIn"])
    types["ListGcpUserAccessBindingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "gcpUserAccessBindings": t.array(
                t.proxy(renames["GcpUserAccessBindingOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListGcpUserAccessBindingsResponseOut"])
    types["BindingIn"] = t.struct(
        {
            "condition": t.proxy(renames["ExprIn"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "members": t.array(t.string()).optional(),
            "role": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
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
    types["ReplaceAccessLevelsResponseIn"] = t.struct(
        {"accessLevels": t.array(t.proxy(renames["AccessLevelIn"])).optional()}
    ).named(renames["ReplaceAccessLevelsResponseIn"])
    types["ReplaceAccessLevelsResponseOut"] = t.struct(
        {
            "accessLevels": t.array(t.proxy(renames["AccessLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAccessLevelsResponseOut"])
    types["EgressToIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["ApiOperationIn"])).optional(),
            "externalResources": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
        }
    ).named(renames["EgressToIn"])
    types["EgressToOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["ApiOperationOut"])).optional(),
            "externalResources": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EgressToOut"])
    types["VpcAccessibleServicesIn"] = t.struct(
        {
            "enableRestriction": t.boolean().optional(),
            "allowedServices": t.array(t.string()).optional(),
        }
    ).named(renames["VpcAccessibleServicesIn"])
    types["VpcAccessibleServicesOut"] = t.struct(
        {
            "enableRestriction": t.boolean().optional(),
            "allowedServices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["VpcAccessibleServicesOut"])
    types["OperationIn"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["ServicePerimeterIn"] = t.struct(
        {
            "description": t.string().optional(),
            "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "perimeterType": t.string().optional(),
            "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ServicePerimeterIn"])
    types["ServicePerimeterOut"] = t.struct(
        {
            "description": t.string().optional(),
            "spec": t.proxy(renames["ServicePerimeterConfigOut"]).optional(),
            "useExplicitDryRunSpec": t.boolean().optional(),
            "perimeterType": t.string().optional(),
            "status": t.proxy(renames["ServicePerimeterConfigOut"]).optional(),
            "name": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicePerimeterOut"])
    types["CommitServicePerimetersRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["CommitServicePerimetersRequestIn"])
    types["CommitServicePerimetersRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitServicePerimetersRequestOut"])
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
            "assetType": t.string().optional(),
            "authorizationType": t.string().optional(),
            "orgs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "authorizationDirection": t.string().optional(),
        }
    ).named(renames["AuthorizedOrgsDescIn"])
    types["AuthorizedOrgsDescOut"] = t.struct(
        {
            "assetType": t.string().optional(),
            "authorizationType": t.string().optional(),
            "orgs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "authorizationDirection": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedOrgsDescOut"])
    types["GcpUserAccessBindingIn"] = t.struct(
        {
            "accessLevels": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "groupKey": t.string(),
            "dryRunAccessLevels": t.array(t.string()).optional(),
        }
    ).named(renames["GcpUserAccessBindingIn"])
    types["GcpUserAccessBindingOut"] = t.struct(
        {
            "accessLevels": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "groupKey": t.string(),
            "dryRunAccessLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcpUserAccessBindingOut"])
    types["GcpUserAccessBindingOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GcpUserAccessBindingOperationMetadataIn"])
    types["GcpUserAccessBindingOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcpUserAccessBindingOperationMetadataOut"])
    types["ServicePerimeterConfigIn"] = t.struct(
        {
            "vpcAccessibleServices": t.proxy(
                renames["VpcAccessibleServicesIn"]
            ).optional(),
            "egressPolicies": t.array(t.proxy(renames["EgressPolicyIn"])).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "ingressPolicies": t.array(t.proxy(renames["IngressPolicyIn"])).optional(),
        }
    ).named(renames["ServicePerimeterConfigIn"])
    types["ServicePerimeterConfigOut"] = t.struct(
        {
            "vpcAccessibleServices": t.proxy(
                renames["VpcAccessibleServicesOut"]
            ).optional(),
            "egressPolicies": t.array(t.proxy(renames["EgressPolicyOut"])).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "ingressPolicies": t.array(t.proxy(renames["IngressPolicyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicePerimeterConfigOut"])

    functions = {}
    functions["organizationsGcpUserAccessBindingsList"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "accessLevels": t.array(t.string()).optional(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsDelete"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "accessLevels": t.array(t.string()).optional(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsGet"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "accessLevels": t.array(t.string()).optional(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsCreate"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "accessLevels": t.array(t.string()).optional(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsPatch"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "updateMask": t.string(),
                "name": t.string().optional(),
                "accessLevels": t.array(t.string()).optional(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
    functions["accessPoliciesAuthorizedOrgsDescsList"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizedOrgsDescOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsDelete"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizedOrgsDescOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsCreate"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizedOrgsDescOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsPatch"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizedOrgsDescOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsGet"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AuthorizedOrgsDescOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsDelete"] = accesscontextmanager.get(
        "v1/{parent}/accessLevels",
        t.struct(
            {
                "accessLevelFormat": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessLevelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsCreate"] = accesscontextmanager.get(
        "v1/{parent}/accessLevels",
        t.struct(
            {
                "accessLevelFormat": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessLevelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsGet"] = accesscontextmanager.get(
        "v1/{parent}/accessLevels",
        t.struct(
            {
                "accessLevelFormat": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessLevelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsReplaceAll"] = accesscontextmanager.get(
        "v1/{parent}/accessLevels",
        t.struct(
            {
                "accessLevelFormat": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessLevelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsPatch"] = accesscontextmanager.get(
        "v1/{parent}/accessLevels",
        t.struct(
            {
                "accessLevelFormat": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessLevelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accessPoliciesAccessLevelsTestIamPermissions"
    ] = accesscontextmanager.get(
        "v1/{parent}/accessLevels",
        t.struct(
            {
                "accessLevelFormat": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessLevelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsList"] = accesscontextmanager.get(
        "v1/{parent}/accessLevels",
        t.struct(
            {
                "accessLevelFormat": t.string().optional(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessLevelsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accessPoliciesServicePerimetersReplaceAll"
    ] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersList"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersPatch"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersCreate"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accessPoliciesServicePerimetersTestIamPermissions"
    ] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersCommit"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersGet"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersDelete"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
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
