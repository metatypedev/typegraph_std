from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_accesscontextmanager() -> Import:
    accesscontextmanager = HTTPRuntime("https://accesscontextmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_accesscontextmanager_1_ErrorResponse",
        "ListGcpUserAccessBindingsResponseIn": "_accesscontextmanager_2_ListGcpUserAccessBindingsResponseIn",
        "ListGcpUserAccessBindingsResponseOut": "_accesscontextmanager_3_ListGcpUserAccessBindingsResponseOut",
        "GetIamPolicyRequestIn": "_accesscontextmanager_4_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_accesscontextmanager_5_GetIamPolicyRequestOut",
        "OperationIn": "_accesscontextmanager_6_OperationIn",
        "OperationOut": "_accesscontextmanager_7_OperationOut",
        "BasicLevelIn": "_accesscontextmanager_8_BasicLevelIn",
        "BasicLevelOut": "_accesscontextmanager_9_BasicLevelOut",
        "IngressPolicyIn": "_accesscontextmanager_10_IngressPolicyIn",
        "IngressPolicyOut": "_accesscontextmanager_11_IngressPolicyOut",
        "TestIamPermissionsResponseIn": "_accesscontextmanager_12_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_accesscontextmanager_13_TestIamPermissionsResponseOut",
        "EgressToIn": "_accesscontextmanager_14_EgressToIn",
        "EgressToOut": "_accesscontextmanager_15_EgressToOut",
        "ListAccessLevelsResponseIn": "_accesscontextmanager_16_ListAccessLevelsResponseIn",
        "ListAccessLevelsResponseOut": "_accesscontextmanager_17_ListAccessLevelsResponseOut",
        "ListOperationsResponseIn": "_accesscontextmanager_18_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_accesscontextmanager_19_ListOperationsResponseOut",
        "IngressFromIn": "_accesscontextmanager_20_IngressFromIn",
        "IngressFromOut": "_accesscontextmanager_21_IngressFromOut",
        "ReplaceServicePerimetersRequestIn": "_accesscontextmanager_22_ReplaceServicePerimetersRequestIn",
        "ReplaceServicePerimetersRequestOut": "_accesscontextmanager_23_ReplaceServicePerimetersRequestOut",
        "ConditionIn": "_accesscontextmanager_24_ConditionIn",
        "ConditionOut": "_accesscontextmanager_25_ConditionOut",
        "ServicePerimeterConfigIn": "_accesscontextmanager_26_ServicePerimeterConfigIn",
        "ServicePerimeterConfigOut": "_accesscontextmanager_27_ServicePerimeterConfigOut",
        "GetPolicyOptionsIn": "_accesscontextmanager_28_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_accesscontextmanager_29_GetPolicyOptionsOut",
        "DevicePolicyIn": "_accesscontextmanager_30_DevicePolicyIn",
        "DevicePolicyOut": "_accesscontextmanager_31_DevicePolicyOut",
        "CancelOperationRequestIn": "_accesscontextmanager_32_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_accesscontextmanager_33_CancelOperationRequestOut",
        "EgressPolicyIn": "_accesscontextmanager_34_EgressPolicyIn",
        "EgressPolicyOut": "_accesscontextmanager_35_EgressPolicyOut",
        "BindingIn": "_accesscontextmanager_36_BindingIn",
        "BindingOut": "_accesscontextmanager_37_BindingOut",
        "IngressToIn": "_accesscontextmanager_38_IngressToIn",
        "IngressToOut": "_accesscontextmanager_39_IngressToOut",
        "ApiOperationIn": "_accesscontextmanager_40_ApiOperationIn",
        "ApiOperationOut": "_accesscontextmanager_41_ApiOperationOut",
        "CommitServicePerimetersResponseIn": "_accesscontextmanager_42_CommitServicePerimetersResponseIn",
        "CommitServicePerimetersResponseOut": "_accesscontextmanager_43_CommitServicePerimetersResponseOut",
        "AuthorizedOrgsDescIn": "_accesscontextmanager_44_AuthorizedOrgsDescIn",
        "AuthorizedOrgsDescOut": "_accesscontextmanager_45_AuthorizedOrgsDescOut",
        "OsConstraintIn": "_accesscontextmanager_46_OsConstraintIn",
        "OsConstraintOut": "_accesscontextmanager_47_OsConstraintOut",
        "EgressFromIn": "_accesscontextmanager_48_EgressFromIn",
        "EgressFromOut": "_accesscontextmanager_49_EgressFromOut",
        "CommitServicePerimetersRequestIn": "_accesscontextmanager_50_CommitServicePerimetersRequestIn",
        "CommitServicePerimetersRequestOut": "_accesscontextmanager_51_CommitServicePerimetersRequestOut",
        "TestIamPermissionsRequestIn": "_accesscontextmanager_52_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_accesscontextmanager_53_TestIamPermissionsRequestOut",
        "EmptyIn": "_accesscontextmanager_54_EmptyIn",
        "EmptyOut": "_accesscontextmanager_55_EmptyOut",
        "ReplaceServicePerimetersResponseIn": "_accesscontextmanager_56_ReplaceServicePerimetersResponseIn",
        "ReplaceServicePerimetersResponseOut": "_accesscontextmanager_57_ReplaceServicePerimetersResponseOut",
        "StatusIn": "_accesscontextmanager_58_StatusIn",
        "StatusOut": "_accesscontextmanager_59_StatusOut",
        "ReplaceAccessLevelsResponseIn": "_accesscontextmanager_60_ReplaceAccessLevelsResponseIn",
        "ReplaceAccessLevelsResponseOut": "_accesscontextmanager_61_ReplaceAccessLevelsResponseOut",
        "ReplaceAccessLevelsRequestIn": "_accesscontextmanager_62_ReplaceAccessLevelsRequestIn",
        "ReplaceAccessLevelsRequestOut": "_accesscontextmanager_63_ReplaceAccessLevelsRequestOut",
        "SetIamPolicyRequestIn": "_accesscontextmanager_64_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_accesscontextmanager_65_SetIamPolicyRequestOut",
        "ListServicePerimetersResponseIn": "_accesscontextmanager_66_ListServicePerimetersResponseIn",
        "ListServicePerimetersResponseOut": "_accesscontextmanager_67_ListServicePerimetersResponseOut",
        "ListAuthorizedOrgsDescsResponseIn": "_accesscontextmanager_68_ListAuthorizedOrgsDescsResponseIn",
        "ListAuthorizedOrgsDescsResponseOut": "_accesscontextmanager_69_ListAuthorizedOrgsDescsResponseOut",
        "ExprIn": "_accesscontextmanager_70_ExprIn",
        "ExprOut": "_accesscontextmanager_71_ExprOut",
        "PolicyIn": "_accesscontextmanager_72_PolicyIn",
        "PolicyOut": "_accesscontextmanager_73_PolicyOut",
        "VpcAccessibleServicesIn": "_accesscontextmanager_74_VpcAccessibleServicesIn",
        "VpcAccessibleServicesOut": "_accesscontextmanager_75_VpcAccessibleServicesOut",
        "IngressSourceIn": "_accesscontextmanager_76_IngressSourceIn",
        "IngressSourceOut": "_accesscontextmanager_77_IngressSourceOut",
        "GcpUserAccessBindingOperationMetadataIn": "_accesscontextmanager_78_GcpUserAccessBindingOperationMetadataIn",
        "GcpUserAccessBindingOperationMetadataOut": "_accesscontextmanager_79_GcpUserAccessBindingOperationMetadataOut",
        "ListAccessPoliciesResponseIn": "_accesscontextmanager_80_ListAccessPoliciesResponseIn",
        "ListAccessPoliciesResponseOut": "_accesscontextmanager_81_ListAccessPoliciesResponseOut",
        "GcpUserAccessBindingIn": "_accesscontextmanager_82_GcpUserAccessBindingIn",
        "GcpUserAccessBindingOut": "_accesscontextmanager_83_GcpUserAccessBindingOut",
        "AccessContextManagerOperationMetadataIn": "_accesscontextmanager_84_AccessContextManagerOperationMetadataIn",
        "AccessContextManagerOperationMetadataOut": "_accesscontextmanager_85_AccessContextManagerOperationMetadataOut",
        "CustomLevelIn": "_accesscontextmanager_86_CustomLevelIn",
        "CustomLevelOut": "_accesscontextmanager_87_CustomLevelOut",
        "ServicePerimeterIn": "_accesscontextmanager_88_ServicePerimeterIn",
        "ServicePerimeterOut": "_accesscontextmanager_89_ServicePerimeterOut",
        "AuditLogConfigIn": "_accesscontextmanager_90_AuditLogConfigIn",
        "AuditLogConfigOut": "_accesscontextmanager_91_AuditLogConfigOut",
        "MethodSelectorIn": "_accesscontextmanager_92_MethodSelectorIn",
        "MethodSelectorOut": "_accesscontextmanager_93_MethodSelectorOut",
        "AccessLevelIn": "_accesscontextmanager_94_AccessLevelIn",
        "AccessLevelOut": "_accesscontextmanager_95_AccessLevelOut",
        "AuditConfigIn": "_accesscontextmanager_96_AuditConfigIn",
        "AuditConfigOut": "_accesscontextmanager_97_AuditConfigOut",
        "AccessPolicyIn": "_accesscontextmanager_98_AccessPolicyIn",
        "AccessPolicyOut": "_accesscontextmanager_99_AccessPolicyOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["BasicLevelIn"] = t.struct(
        {
            "combiningFunction": t.string().optional(),
            "conditions": t.array(t.proxy(renames["ConditionIn"])),
        }
    ).named(renames["BasicLevelIn"])
    types["BasicLevelOut"] = t.struct(
        {
            "combiningFunction": t.string().optional(),
            "conditions": t.array(t.proxy(renames["ConditionOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BasicLevelOut"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["EgressToIn"] = t.struct(
        {
            "externalResources": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "operations": t.array(t.proxy(renames["ApiOperationIn"])).optional(),
        }
    ).named(renames["EgressToIn"])
    types["EgressToOut"] = t.struct(
        {
            "externalResources": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "operations": t.array(t.proxy(renames["ApiOperationOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EgressToOut"])
    types["ListAccessLevelsResponseIn"] = t.struct(
        {
            "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListAccessLevelsResponseIn"])
    types["ListAccessLevelsResponseOut"] = t.struct(
        {
            "accessLevels": t.array(t.proxy(renames["AccessLevelOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListAccessLevelsResponseOut"])
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
    types["IngressFromIn"] = t.struct(
        {
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
            "sources": t.array(t.proxy(renames["IngressSourceIn"])).optional(),
        }
    ).named(renames["IngressFromIn"])
    types["IngressFromOut"] = t.struct(
        {
            "identities": t.array(t.string()).optional(),
            "identityType": t.string().optional(),
            "sources": t.array(t.proxy(renames["IngressSourceOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngressFromOut"])
    types["ReplaceServicePerimetersRequestIn"] = t.struct(
        {
            "servicePerimeters": t.array(t.proxy(renames["ServicePerimeterIn"])),
            "etag": t.string().optional(),
        }
    ).named(renames["ReplaceServicePerimetersRequestIn"])
    types["ReplaceServicePerimetersRequestOut"] = t.struct(
        {
            "servicePerimeters": t.array(t.proxy(renames["ServicePerimeterOut"])),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceServicePerimetersRequestOut"])
    types["ConditionIn"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "devicePolicy": t.proxy(renames["DevicePolicyIn"]).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "members": t.array(t.string()).optional(),
            "negate": t.boolean().optional(),
            "devicePolicy": t.proxy(renames["DevicePolicyOut"]).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "regions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
    types["ServicePerimeterConfigIn"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["VpcAccessibleServicesIn"]
            ).optional(),
            "egressPolicies": t.array(t.proxy(renames["EgressPolicyIn"])).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "ingressPolicies": t.array(t.proxy(renames["IngressPolicyIn"])).optional(),
            "restrictedServices": t.array(t.string()).optional(),
        }
    ).named(renames["ServicePerimeterConfigIn"])
    types["ServicePerimeterConfigOut"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["VpcAccessibleServicesOut"]
            ).optional(),
            "egressPolicies": t.array(t.proxy(renames["EgressPolicyOut"])).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "ingressPolicies": t.array(t.proxy(renames["IngressPolicyOut"])).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicePerimeterConfigOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["DevicePolicyIn"] = t.struct(
        {
            "requireAdminApproval": t.boolean().optional(),
            "requireScreenlock": t.boolean().optional(),
            "osConstraints": t.array(t.proxy(renames["OsConstraintIn"])).optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
        }
    ).named(renames["DevicePolicyIn"])
    types["DevicePolicyOut"] = t.struct(
        {
            "requireAdminApproval": t.boolean().optional(),
            "requireScreenlock": t.boolean().optional(),
            "osConstraints": t.array(t.proxy(renames["OsConstraintOut"])).optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicePolicyOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])
    types["EgressPolicyIn"] = t.struct(
        {
            "egressTo": t.proxy(renames["EgressToIn"]).optional(),
            "egressFrom": t.proxy(renames["EgressFromIn"]).optional(),
        }
    ).named(renames["EgressPolicyIn"])
    types["EgressPolicyOut"] = t.struct(
        {
            "egressTo": t.proxy(renames["EgressToOut"]).optional(),
            "egressFrom": t.proxy(renames["EgressFromOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EgressPolicyOut"])
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
    types["IngressToIn"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["ApiOperationIn"])).optional(),
            "resources": t.array(t.string()).optional(),
        }
    ).named(renames["IngressToIn"])
    types["IngressToOut"] = t.struct(
        {
            "operations": t.array(t.proxy(renames["ApiOperationOut"])).optional(),
            "resources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["IngressToOut"])
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
    types["AuthorizedOrgsDescIn"] = t.struct(
        {
            "orgs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "authorizationType": t.string().optional(),
            "assetType": t.string().optional(),
            "authorizationDirection": t.string().optional(),
        }
    ).named(renames["AuthorizedOrgsDescIn"])
    types["AuthorizedOrgsDescOut"] = t.struct(
        {
            "orgs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "authorizationType": t.string().optional(),
            "assetType": t.string().optional(),
            "authorizationDirection": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedOrgsDescOut"])
    types["OsConstraintIn"] = t.struct(
        {
            "requireVerifiedChromeOs": t.boolean().optional(),
            "osType": t.string(),
            "minimumVersion": t.string().optional(),
        }
    ).named(renames["OsConstraintIn"])
    types["OsConstraintOut"] = t.struct(
        {
            "requireVerifiedChromeOs": t.boolean().optional(),
            "osType": t.string(),
            "minimumVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OsConstraintOut"])
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
    types["CommitServicePerimetersRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["CommitServicePerimetersRequestIn"])
    types["CommitServicePerimetersRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitServicePerimetersRequestOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ReplaceAccessLevelsResponseIn"] = t.struct(
        {"accessLevels": t.array(t.proxy(renames["AccessLevelIn"])).optional()}
    ).named(renames["ReplaceAccessLevelsResponseIn"])
    types["ReplaceAccessLevelsResponseOut"] = t.struct(
        {
            "accessLevels": t.array(t.proxy(renames["AccessLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAccessLevelsResponseOut"])
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
    types["ExprIn"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "location": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "etag": t.string().optional(),
            "version": t.integer().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
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
    types["GcpUserAccessBindingOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GcpUserAccessBindingOperationMetadataIn"])
    types["GcpUserAccessBindingOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcpUserAccessBindingOperationMetadataOut"])
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
    types["GcpUserAccessBindingIn"] = t.struct(
        {
            "dryRunAccessLevels": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "groupKey": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["GcpUserAccessBindingIn"])
    types["GcpUserAccessBindingOut"] = t.struct(
        {
            "dryRunAccessLevels": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "groupKey": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcpUserAccessBindingOut"])
    types["AccessContextManagerOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AccessContextManagerOperationMetadataIn"])
    types["AccessContextManagerOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AccessContextManagerOperationMetadataOut"])
    types["CustomLevelIn"] = t.struct({"expr": t.proxy(renames["ExprIn"])}).named(
        renames["CustomLevelIn"]
    )
    types["CustomLevelOut"] = t.struct(
        {
            "expr": t.proxy(renames["ExprOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomLevelOut"])
    types["ServicePerimeterIn"] = t.struct(
        {
            "useExplicitDryRunSpec": t.boolean().optional(),
            "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
            "perimeterType": t.string().optional(),
            "description": t.string().optional(),
            "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["ServicePerimeterIn"])
    types["ServicePerimeterOut"] = t.struct(
        {
            "useExplicitDryRunSpec": t.boolean().optional(),
            "status": t.proxy(renames["ServicePerimeterConfigOut"]).optional(),
            "perimeterType": t.string().optional(),
            "description": t.string().optional(),
            "spec": t.proxy(renames["ServicePerimeterConfigOut"]).optional(),
            "title": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicePerimeterOut"])
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
    types["AccessLevelIn"] = t.struct(
        {
            "title": t.string().optional(),
            "custom": t.proxy(renames["CustomLevelIn"]).optional(),
            "basic": t.proxy(renames["BasicLevelIn"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AccessLevelIn"])
    types["AccessLevelOut"] = t.struct(
        {
            "title": t.string().optional(),
            "custom": t.proxy(renames["CustomLevelOut"]).optional(),
            "basic": t.proxy(renames["BasicLevelOut"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessLevelOut"])
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
    types["AccessPolicyIn"] = t.struct(
        {
            "parent": t.string(),
            "scopes": t.array(t.string()).optional(),
            "title": t.string(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["AccessPolicyIn"])
    types["AccessPolicyOut"] = t.struct(
        {
            "parent": t.string(),
            "scopes": t.array(t.string()).optional(),
            "title": t.string(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessPolicyOut"])

    functions = {}
    functions["accessPoliciesList"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccessPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesPatch"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccessPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesGetIamPolicy"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccessPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesTestIamPermissions"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccessPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesCreate"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccessPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesSetIamPolicy"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccessPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesDelete"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccessPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesGet"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["AccessPolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsCreate"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsGet"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsPatch"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsList"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAuthorizedOrgsDescsDelete"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsGet"] = accesscontextmanager.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsDelete"] = accesscontextmanager.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsCreate"] = accesscontextmanager.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsReplaceAll"] = accesscontextmanager.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsPatch"] = accesscontextmanager.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsList"] = accesscontextmanager.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accessPoliciesAccessLevelsTestIamPermissions"
    ] = accesscontextmanager.post(
        "v1/{resource}:testIamPermissions",
        t.struct(
            {
                "resource": t.string().optional(),
                "permissions": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["TestIamPermissionsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersCommit"] = accesscontextmanager.post(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "parent": t.string(),
                "useExplicitDryRunSpec": t.boolean().optional(),
                "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "perimeterType": t.string().optional(),
                "description": t.string().optional(),
                "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "title": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersReplaceAll"] = accesscontextmanager.post(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "parent": t.string(),
                "useExplicitDryRunSpec": t.boolean().optional(),
                "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "perimeterType": t.string().optional(),
                "description": t.string().optional(),
                "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "title": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersGet"] = accesscontextmanager.post(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "parent": t.string(),
                "useExplicitDryRunSpec": t.boolean().optional(),
                "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "perimeterType": t.string().optional(),
                "description": t.string().optional(),
                "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "title": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersList"] = accesscontextmanager.post(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "parent": t.string(),
                "useExplicitDryRunSpec": t.boolean().optional(),
                "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "perimeterType": t.string().optional(),
                "description": t.string().optional(),
                "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "title": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accessPoliciesServicePerimetersTestIamPermissions"
    ] = accesscontextmanager.post(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "parent": t.string(),
                "useExplicitDryRunSpec": t.boolean().optional(),
                "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "perimeterType": t.string().optional(),
                "description": t.string().optional(),
                "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "title": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersDelete"] = accesscontextmanager.post(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "parent": t.string(),
                "useExplicitDryRunSpec": t.boolean().optional(),
                "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "perimeterType": t.string().optional(),
                "description": t.string().optional(),
                "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "title": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersPatch"] = accesscontextmanager.post(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "parent": t.string(),
                "useExplicitDryRunSpec": t.boolean().optional(),
                "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "perimeterType": t.string().optional(),
                "description": t.string().optional(),
                "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "title": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersCreate"] = accesscontextmanager.post(
        "v1/{parent}/servicePerimeters",
        t.struct(
            {
                "parent": t.string(),
                "useExplicitDryRunSpec": t.boolean().optional(),
                "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "perimeterType": t.string().optional(),
                "description": t.string().optional(),
                "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
                "title": t.string().optional(),
                "name": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct(
            {
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "filter": t.string().optional(),
                "name": t.string().optional(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListOperationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsGet"] = accesscontextmanager.get(
        "v1/{parent}/gcpUserAccessBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGcpUserAccessBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsPatch"] = accesscontextmanager.get(
        "v1/{parent}/gcpUserAccessBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGcpUserAccessBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsDelete"] = accesscontextmanager.get(
        "v1/{parent}/gcpUserAccessBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGcpUserAccessBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsCreate"] = accesscontextmanager.get(
        "v1/{parent}/gcpUserAccessBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGcpUserAccessBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsList"] = accesscontextmanager.get(
        "v1/{parent}/gcpUserAccessBindings",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListGcpUserAccessBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="accesscontextmanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
