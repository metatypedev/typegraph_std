from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_accesscontextmanager() -> Import:
    accesscontextmanager = HTTPRuntime("https://accesscontextmanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_accesscontextmanager_1_ErrorResponse",
        "CommitServicePerimetersResponseIn": "_accesscontextmanager_2_CommitServicePerimetersResponseIn",
        "CommitServicePerimetersResponseOut": "_accesscontextmanager_3_CommitServicePerimetersResponseOut",
        "ListServicePerimetersResponseIn": "_accesscontextmanager_4_ListServicePerimetersResponseIn",
        "ListServicePerimetersResponseOut": "_accesscontextmanager_5_ListServicePerimetersResponseOut",
        "TestIamPermissionsResponseIn": "_accesscontextmanager_6_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_accesscontextmanager_7_TestIamPermissionsResponseOut",
        "CustomLevelIn": "_accesscontextmanager_8_CustomLevelIn",
        "CustomLevelOut": "_accesscontextmanager_9_CustomLevelOut",
        "AuditConfigIn": "_accesscontextmanager_10_AuditConfigIn",
        "AuditConfigOut": "_accesscontextmanager_11_AuditConfigOut",
        "ListAuthorizedOrgsDescsResponseIn": "_accesscontextmanager_12_ListAuthorizedOrgsDescsResponseIn",
        "ListAuthorizedOrgsDescsResponseOut": "_accesscontextmanager_13_ListAuthorizedOrgsDescsResponseOut",
        "ReplaceServicePerimetersRequestIn": "_accesscontextmanager_14_ReplaceServicePerimetersRequestIn",
        "ReplaceServicePerimetersRequestOut": "_accesscontextmanager_15_ReplaceServicePerimetersRequestOut",
        "ServicePerimeterIn": "_accesscontextmanager_16_ServicePerimeterIn",
        "ServicePerimeterOut": "_accesscontextmanager_17_ServicePerimeterOut",
        "IngressFromIn": "_accesscontextmanager_18_IngressFromIn",
        "IngressFromOut": "_accesscontextmanager_19_IngressFromOut",
        "AuthorizedOrgsDescIn": "_accesscontextmanager_20_AuthorizedOrgsDescIn",
        "AuthorizedOrgsDescOut": "_accesscontextmanager_21_AuthorizedOrgsDescOut",
        "EmptyIn": "_accesscontextmanager_22_EmptyIn",
        "EmptyOut": "_accesscontextmanager_23_EmptyOut",
        "ReplaceAccessLevelsResponseIn": "_accesscontextmanager_24_ReplaceAccessLevelsResponseIn",
        "ReplaceAccessLevelsResponseOut": "_accesscontextmanager_25_ReplaceAccessLevelsResponseOut",
        "ConditionIn": "_accesscontextmanager_26_ConditionIn",
        "ConditionOut": "_accesscontextmanager_27_ConditionOut",
        "ListAccessLevelsResponseIn": "_accesscontextmanager_28_ListAccessLevelsResponseIn",
        "ListAccessLevelsResponseOut": "_accesscontextmanager_29_ListAccessLevelsResponseOut",
        "EgressPolicyIn": "_accesscontextmanager_30_EgressPolicyIn",
        "EgressPolicyOut": "_accesscontextmanager_31_EgressPolicyOut",
        "VpcAccessibleServicesIn": "_accesscontextmanager_32_VpcAccessibleServicesIn",
        "VpcAccessibleServicesOut": "_accesscontextmanager_33_VpcAccessibleServicesOut",
        "ListAccessPoliciesResponseIn": "_accesscontextmanager_34_ListAccessPoliciesResponseIn",
        "ListAccessPoliciesResponseOut": "_accesscontextmanager_35_ListAccessPoliciesResponseOut",
        "GcpUserAccessBindingIn": "_accesscontextmanager_36_GcpUserAccessBindingIn",
        "GcpUserAccessBindingOut": "_accesscontextmanager_37_GcpUserAccessBindingOut",
        "ApiOperationIn": "_accesscontextmanager_38_ApiOperationIn",
        "ApiOperationOut": "_accesscontextmanager_39_ApiOperationOut",
        "GcpUserAccessBindingOperationMetadataIn": "_accesscontextmanager_40_GcpUserAccessBindingOperationMetadataIn",
        "GcpUserAccessBindingOperationMetadataOut": "_accesscontextmanager_41_GcpUserAccessBindingOperationMetadataOut",
        "BindingIn": "_accesscontextmanager_42_BindingIn",
        "BindingOut": "_accesscontextmanager_43_BindingOut",
        "GetPolicyOptionsIn": "_accesscontextmanager_44_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_accesscontextmanager_45_GetPolicyOptionsOut",
        "IngressPolicyIn": "_accesscontextmanager_46_IngressPolicyIn",
        "IngressPolicyOut": "_accesscontextmanager_47_IngressPolicyOut",
        "PolicyIn": "_accesscontextmanager_48_PolicyIn",
        "PolicyOut": "_accesscontextmanager_49_PolicyOut",
        "EgressFromIn": "_accesscontextmanager_50_EgressFromIn",
        "EgressFromOut": "_accesscontextmanager_51_EgressFromOut",
        "TestIamPermissionsRequestIn": "_accesscontextmanager_52_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_accesscontextmanager_53_TestIamPermissionsRequestOut",
        "ListGcpUserAccessBindingsResponseIn": "_accesscontextmanager_54_ListGcpUserAccessBindingsResponseIn",
        "ListGcpUserAccessBindingsResponseOut": "_accesscontextmanager_55_ListGcpUserAccessBindingsResponseOut",
        "AccessContextManagerOperationMetadataIn": "_accesscontextmanager_56_AccessContextManagerOperationMetadataIn",
        "AccessContextManagerOperationMetadataOut": "_accesscontextmanager_57_AccessContextManagerOperationMetadataOut",
        "CommitServicePerimetersRequestIn": "_accesscontextmanager_58_CommitServicePerimetersRequestIn",
        "CommitServicePerimetersRequestOut": "_accesscontextmanager_59_CommitServicePerimetersRequestOut",
        "BasicLevelIn": "_accesscontextmanager_60_BasicLevelIn",
        "BasicLevelOut": "_accesscontextmanager_61_BasicLevelOut",
        "IngressSourceIn": "_accesscontextmanager_62_IngressSourceIn",
        "IngressSourceOut": "_accesscontextmanager_63_IngressSourceOut",
        "StatusIn": "_accesscontextmanager_64_StatusIn",
        "StatusOut": "_accesscontextmanager_65_StatusOut",
        "IngressToIn": "_accesscontextmanager_66_IngressToIn",
        "IngressToOut": "_accesscontextmanager_67_IngressToOut",
        "AuditLogConfigIn": "_accesscontextmanager_68_AuditLogConfigIn",
        "AuditLogConfigOut": "_accesscontextmanager_69_AuditLogConfigOut",
        "AccessPolicyIn": "_accesscontextmanager_70_AccessPolicyIn",
        "AccessPolicyOut": "_accesscontextmanager_71_AccessPolicyOut",
        "MethodSelectorIn": "_accesscontextmanager_72_MethodSelectorIn",
        "MethodSelectorOut": "_accesscontextmanager_73_MethodSelectorOut",
        "OsConstraintIn": "_accesscontextmanager_74_OsConstraintIn",
        "OsConstraintOut": "_accesscontextmanager_75_OsConstraintOut",
        "DevicePolicyIn": "_accesscontextmanager_76_DevicePolicyIn",
        "DevicePolicyOut": "_accesscontextmanager_77_DevicePolicyOut",
        "ListOperationsResponseIn": "_accesscontextmanager_78_ListOperationsResponseIn",
        "ListOperationsResponseOut": "_accesscontextmanager_79_ListOperationsResponseOut",
        "ExprIn": "_accesscontextmanager_80_ExprIn",
        "ExprOut": "_accesscontextmanager_81_ExprOut",
        "ServicePerimeterConfigIn": "_accesscontextmanager_82_ServicePerimeterConfigIn",
        "ServicePerimeterConfigOut": "_accesscontextmanager_83_ServicePerimeterConfigOut",
        "ReplaceServicePerimetersResponseIn": "_accesscontextmanager_84_ReplaceServicePerimetersResponseIn",
        "ReplaceServicePerimetersResponseOut": "_accesscontextmanager_85_ReplaceServicePerimetersResponseOut",
        "OperationIn": "_accesscontextmanager_86_OperationIn",
        "OperationOut": "_accesscontextmanager_87_OperationOut",
        "GetIamPolicyRequestIn": "_accesscontextmanager_88_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_accesscontextmanager_89_GetIamPolicyRequestOut",
        "AccessLevelIn": "_accesscontextmanager_90_AccessLevelIn",
        "AccessLevelOut": "_accesscontextmanager_91_AccessLevelOut",
        "SetIamPolicyRequestIn": "_accesscontextmanager_92_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_accesscontextmanager_93_SetIamPolicyRequestOut",
        "ReplaceAccessLevelsRequestIn": "_accesscontextmanager_94_ReplaceAccessLevelsRequestIn",
        "ReplaceAccessLevelsRequestOut": "_accesscontextmanager_95_ReplaceAccessLevelsRequestOut",
        "EgressToIn": "_accesscontextmanager_96_EgressToIn",
        "EgressToOut": "_accesscontextmanager_97_EgressToOut",
        "CancelOperationRequestIn": "_accesscontextmanager_98_CancelOperationRequestIn",
        "CancelOperationRequestOut": "_accesscontextmanager_99_CancelOperationRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["CustomLevelIn"] = t.struct({"expr": t.proxy(renames["ExprIn"])}).named(
        renames["CustomLevelIn"]
    )
    types["CustomLevelOut"] = t.struct(
        {
            "expr": t.proxy(renames["ExprOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CustomLevelOut"])
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
    types["ServicePerimeterIn"] = t.struct(
        {
            "useExplicitDryRunSpec": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "status": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
            "title": t.string().optional(),
            "perimeterType": t.string().optional(),
            "spec": t.proxy(renames["ServicePerimeterConfigIn"]).optional(),
        }
    ).named(renames["ServicePerimeterIn"])
    types["ServicePerimeterOut"] = t.struct(
        {
            "useExplicitDryRunSpec": t.boolean().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "status": t.proxy(renames["ServicePerimeterConfigOut"]).optional(),
            "title": t.string().optional(),
            "perimeterType": t.string().optional(),
            "spec": t.proxy(renames["ServicePerimeterConfigOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicePerimeterOut"])
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
    types["AuthorizedOrgsDescIn"] = t.struct(
        {
            "orgs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "authorizationType": t.string().optional(),
            "authorizationDirection": t.string().optional(),
            "assetType": t.string().optional(),
        }
    ).named(renames["AuthorizedOrgsDescIn"])
    types["AuthorizedOrgsDescOut"] = t.struct(
        {
            "orgs": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "authorizationType": t.string().optional(),
            "authorizationDirection": t.string().optional(),
            "assetType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AuthorizedOrgsDescOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ReplaceAccessLevelsResponseIn"] = t.struct(
        {"accessLevels": t.array(t.proxy(renames["AccessLevelIn"])).optional()}
    ).named(renames["ReplaceAccessLevelsResponseIn"])
    types["ReplaceAccessLevelsResponseOut"] = t.struct(
        {
            "accessLevels": t.array(t.proxy(renames["AccessLevelOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ReplaceAccessLevelsResponseOut"])
    types["ConditionIn"] = t.struct(
        {
            "regions": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(renames["DevicePolicyIn"]).optional(),
            "negate": t.boolean().optional(),
            "members": t.array(t.string()).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
        }
    ).named(renames["ConditionIn"])
    types["ConditionOut"] = t.struct(
        {
            "regions": t.array(t.string()).optional(),
            "ipSubnetworks": t.array(t.string()).optional(),
            "devicePolicy": t.proxy(renames["DevicePolicyOut"]).optional(),
            "negate": t.boolean().optional(),
            "members": t.array(t.string()).optional(),
            "requiredAccessLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ConditionOut"])
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
            "name": t.string().optional(),
            "groupKey": t.string(),
            "dryRunAccessLevels": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
        }
    ).named(renames["GcpUserAccessBindingIn"])
    types["GcpUserAccessBindingOut"] = t.struct(
        {
            "name": t.string().optional(),
            "groupKey": t.string(),
            "dryRunAccessLevels": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GcpUserAccessBindingOut"])
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
    types["GcpUserAccessBindingOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["GcpUserAccessBindingOperationMetadataIn"])
    types["GcpUserAccessBindingOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["GcpUserAccessBindingOperationMetadataOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
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
    types["PolicyIn"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
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
    types["AccessContextManagerOperationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["AccessContextManagerOperationMetadataIn"])
    types["AccessContextManagerOperationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["AccessContextManagerOperationMetadataOut"])
    types["CommitServicePerimetersRequestIn"] = t.struct(
        {"etag": t.string().optional()}
    ).named(renames["CommitServicePerimetersRequestIn"])
    types["CommitServicePerimetersRequestOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CommitServicePerimetersRequestOut"])
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
    types["AccessPolicyIn"] = t.struct(
        {
            "parent": t.string(),
            "scopes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "title": t.string(),
        }
    ).named(renames["AccessPolicyIn"])
    types["AccessPolicyOut"] = t.struct(
        {
            "parent": t.string(),
            "scopes": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "title": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessPolicyOut"])
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
    types["DevicePolicyIn"] = t.struct(
        {
            "requireScreenlock": t.boolean().optional(),
            "osConstraints": t.array(t.proxy(renames["OsConstraintIn"])).optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
        }
    ).named(renames["DevicePolicyIn"])
    types["DevicePolicyOut"] = t.struct(
        {
            "requireScreenlock": t.boolean().optional(),
            "osConstraints": t.array(t.proxy(renames["OsConstraintOut"])).optional(),
            "allowedDeviceManagementLevels": t.array(t.string()).optional(),
            "requireAdminApproval": t.boolean().optional(),
            "allowedEncryptionStatuses": t.array(t.string()).optional(),
            "requireCorpOwned": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DevicePolicyOut"])
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
    types["ServicePerimeterConfigIn"] = t.struct(
        {
            "egressPolicies": t.array(t.proxy(renames["EgressPolicyIn"])).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["VpcAccessibleServicesIn"]
            ).optional(),
            "ingressPolicies": t.array(t.proxy(renames["IngressPolicyIn"])).optional(),
        }
    ).named(renames["ServicePerimeterConfigIn"])
    types["ServicePerimeterConfigOut"] = t.struct(
        {
            "egressPolicies": t.array(t.proxy(renames["EgressPolicyOut"])).optional(),
            "restrictedServices": t.array(t.string()).optional(),
            "accessLevels": t.array(t.string()).optional(),
            "resources": t.array(t.string()).optional(),
            "vpcAccessibleServices": t.proxy(
                renames["VpcAccessibleServicesOut"]
            ).optional(),
            "ingressPolicies": t.array(t.proxy(renames["IngressPolicyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ServicePerimeterConfigOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "done": t.boolean().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OperationOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["AccessLevelIn"] = t.struct(
        {
            "title": t.string().optional(),
            "basic": t.proxy(renames["BasicLevelIn"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "custom": t.proxy(renames["CustomLevelIn"]).optional(),
        }
    ).named(renames["AccessLevelIn"])
    types["AccessLevelOut"] = t.struct(
        {
            "title": t.string().optional(),
            "basic": t.proxy(renames["BasicLevelOut"]).optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "custom": t.proxy(renames["CustomLevelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AccessLevelOut"])
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
    types["EgressToIn"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "operations": t.array(t.proxy(renames["ApiOperationIn"])).optional(),
            "externalResources": t.array(t.string()).optional(),
        }
    ).named(renames["EgressToIn"])
    types["EgressToOut"] = t.struct(
        {
            "resources": t.array(t.string()).optional(),
            "operations": t.array(t.proxy(renames["ApiOperationOut"])).optional(),
            "externalResources": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EgressToOut"])
    types["CancelOperationRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CancelOperationRequestIn"]
    )
    types["CancelOperationRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CancelOperationRequestOut"])

    functions = {}
    functions["accessPoliciesPatch"] = accesscontextmanager.get(
        "v1/accessPolicies",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesTestIamPermissions"] = accesscontextmanager.get(
        "v1/accessPolicies",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesGetIamPolicy"] = accesscontextmanager.get(
        "v1/accessPolicies",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesSetIamPolicy"] = accesscontextmanager.get(
        "v1/accessPolicies",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesCreate"] = accesscontextmanager.get(
        "v1/accessPolicies",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesDelete"] = accesscontextmanager.get(
        "v1/accessPolicies",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesGet"] = accesscontextmanager.get(
        "v1/accessPolicies",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessPoliciesResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesList"] = accesscontextmanager.get(
        "v1/accessPolicies",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListAccessPoliciesResponseOut"]),
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
                "authorizationType": t.string().optional(),
                "authorizationDirection": t.string().optional(),
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
                "authorizationType": t.string().optional(),
                "authorizationDirection": t.string().optional(),
                "assetType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
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
                "authorizationType": t.string().optional(),
                "authorizationDirection": t.string().optional(),
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
                "authorizationType": t.string().optional(),
                "authorizationDirection": t.string().optional(),
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
                "authorizationType": t.string().optional(),
                "authorizationDirection": t.string().optional(),
                "assetType": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersPatch"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServicePerimeterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersCreate"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServicePerimeterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersReplaceAll"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServicePerimeterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accessPoliciesServicePerimetersTestIamPermissions"
    ] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServicePerimeterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersCommit"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServicePerimeterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersDelete"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServicePerimeterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersList"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServicePerimeterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesServicePerimetersGet"] = accesscontextmanager.get(
        "v1/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ServicePerimeterOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsDelete"] = accesscontextmanager.post(
        "v1/{parent}/accessLevels:replaceAll",
        t.struct(
            {
                "parent": t.string(),
                "etag": t.string().optional(),
                "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsPatch"] = accesscontextmanager.post(
        "v1/{parent}/accessLevels:replaceAll",
        t.struct(
            {
                "parent": t.string(),
                "etag": t.string().optional(),
                "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsList"] = accesscontextmanager.post(
        "v1/{parent}/accessLevels:replaceAll",
        t.struct(
            {
                "parent": t.string(),
                "etag": t.string().optional(),
                "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsGet"] = accesscontextmanager.post(
        "v1/{parent}/accessLevels:replaceAll",
        t.struct(
            {
                "parent": t.string(),
                "etag": t.string().optional(),
                "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions[
        "accessPoliciesAccessLevelsTestIamPermissions"
    ] = accesscontextmanager.post(
        "v1/{parent}/accessLevels:replaceAll",
        t.struct(
            {
                "parent": t.string(),
                "etag": t.string().optional(),
                "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsCreate"] = accesscontextmanager.post(
        "v1/{parent}/accessLevels:replaceAll",
        t.struct(
            {
                "parent": t.string(),
                "etag": t.string().optional(),
                "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["accessPoliciesAccessLevelsReplaceAll"] = accesscontextmanager.post(
        "v1/{parent}/accessLevels:replaceAll",
        t.struct(
            {
                "parent": t.string(),
                "etag": t.string().optional(),
                "accessLevels": t.array(t.proxy(renames["AccessLevelIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsList"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsCancel"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsDelete"] = accesscontextmanager.delete(
        "v1/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsDelete"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "accessLevels": t.array(t.string()).optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "accessLevels": t.array(t.string()).optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "accessLevels": t.array(t.string()).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGcpUserAccessBindingsList"] = accesscontextmanager.patch(
        "v1/{name}",
        t.struct(
            {
                "name": t.string().optional(),
                "updateMask": t.string(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "accessLevels": t.array(t.string()).optional(),
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
                "name": t.string().optional(),
                "updateMask": t.string(),
                "groupKey": t.string(),
                "dryRunAccessLevels": t.array(t.string()).optional(),
                "accessLevels": t.array(t.string()).optional(),
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
        types=types,
        functions=functions,
    )
