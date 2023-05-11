from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudresourcemanager() -> Import:
    cloudresourcemanager = HTTPRuntime("https://cloudresourcemanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudresourcemanager_1_ErrorResponse",
        "DeleteOrganizationMetadataIn": "_cloudresourcemanager_2_DeleteOrganizationMetadataIn",
        "DeleteOrganizationMetadataOut": "_cloudresourcemanager_3_DeleteOrganizationMetadataOut",
        "UndeleteFolderRequestIn": "_cloudresourcemanager_4_UndeleteFolderRequestIn",
        "UndeleteFolderRequestOut": "_cloudresourcemanager_5_UndeleteFolderRequestOut",
        "DeleteTagKeyMetadataIn": "_cloudresourcemanager_6_DeleteTagKeyMetadataIn",
        "DeleteTagKeyMetadataOut": "_cloudresourcemanager_7_DeleteTagKeyMetadataOut",
        "TestIamPermissionsResponseIn": "_cloudresourcemanager_8_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudresourcemanager_9_TestIamPermissionsResponseOut",
        "TagBindingIn": "_cloudresourcemanager_10_TagBindingIn",
        "TagBindingOut": "_cloudresourcemanager_11_TagBindingOut",
        "PolicyIn": "_cloudresourcemanager_12_PolicyIn",
        "PolicyOut": "_cloudresourcemanager_13_PolicyOut",
        "BindingIn": "_cloudresourcemanager_14_BindingIn",
        "BindingOut": "_cloudresourcemanager_15_BindingOut",
        "SearchFoldersResponseIn": "_cloudresourcemanager_16_SearchFoldersResponseIn",
        "SearchFoldersResponseOut": "_cloudresourcemanager_17_SearchFoldersResponseOut",
        "SetIamPolicyRequestIn": "_cloudresourcemanager_18_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudresourcemanager_19_SetIamPolicyRequestOut",
        "TagValueIn": "_cloudresourcemanager_20_TagValueIn",
        "TagValueOut": "_cloudresourcemanager_21_TagValueOut",
        "MoveFolderRequestIn": "_cloudresourcemanager_22_MoveFolderRequestIn",
        "MoveFolderRequestOut": "_cloudresourcemanager_23_MoveFolderRequestOut",
        "ExprIn": "_cloudresourcemanager_24_ExprIn",
        "ExprOut": "_cloudresourcemanager_25_ExprOut",
        "DeleteProjectMetadataIn": "_cloudresourcemanager_26_DeleteProjectMetadataIn",
        "DeleteProjectMetadataOut": "_cloudresourcemanager_27_DeleteProjectMetadataOut",
        "SearchProjectsResponseIn": "_cloudresourcemanager_28_SearchProjectsResponseIn",
        "SearchProjectsResponseOut": "_cloudresourcemanager_29_SearchProjectsResponseOut",
        "DeleteFolderMetadataIn": "_cloudresourcemanager_30_DeleteFolderMetadataIn",
        "DeleteFolderMetadataOut": "_cloudresourcemanager_31_DeleteFolderMetadataOut",
        "ListTagValuesResponseIn": "_cloudresourcemanager_32_ListTagValuesResponseIn",
        "ListTagValuesResponseOut": "_cloudresourcemanager_33_ListTagValuesResponseOut",
        "MoveProjectMetadataIn": "_cloudresourcemanager_34_MoveProjectMetadataIn",
        "MoveProjectMetadataOut": "_cloudresourcemanager_35_MoveProjectMetadataOut",
        "MoveFolderMetadataIn": "_cloudresourcemanager_36_MoveFolderMetadataIn",
        "MoveFolderMetadataOut": "_cloudresourcemanager_37_MoveFolderMetadataOut",
        "ListLiensResponseIn": "_cloudresourcemanager_38_ListLiensResponseIn",
        "ListLiensResponseOut": "_cloudresourcemanager_39_ListLiensResponseOut",
        "UndeleteProjectMetadataIn": "_cloudresourcemanager_40_UndeleteProjectMetadataIn",
        "UndeleteProjectMetadataOut": "_cloudresourcemanager_41_UndeleteProjectMetadataOut",
        "TagHoldIn": "_cloudresourcemanager_42_TagHoldIn",
        "TagHoldOut": "_cloudresourcemanager_43_TagHoldOut",
        "AuditLogConfigIn": "_cloudresourcemanager_44_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudresourcemanager_45_AuditLogConfigOut",
        "StatusIn": "_cloudresourcemanager_46_StatusIn",
        "StatusOut": "_cloudresourcemanager_47_StatusOut",
        "LienIn": "_cloudresourcemanager_48_LienIn",
        "LienOut": "_cloudresourcemanager_49_LienOut",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn": "_cloudresourcemanager_50_CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut": "_cloudresourcemanager_51_CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut",
        "CreateTagBindingMetadataIn": "_cloudresourcemanager_52_CreateTagBindingMetadataIn",
        "CreateTagBindingMetadataOut": "_cloudresourcemanager_53_CreateTagBindingMetadataOut",
        "CreateTagKeyMetadataIn": "_cloudresourcemanager_54_CreateTagKeyMetadataIn",
        "CreateTagKeyMetadataOut": "_cloudresourcemanager_55_CreateTagKeyMetadataOut",
        "SearchOrganizationsResponseIn": "_cloudresourcemanager_56_SearchOrganizationsResponseIn",
        "SearchOrganizationsResponseOut": "_cloudresourcemanager_57_SearchOrganizationsResponseOut",
        "UpdateTagKeyMetadataIn": "_cloudresourcemanager_58_UpdateTagKeyMetadataIn",
        "UpdateTagKeyMetadataOut": "_cloudresourcemanager_59_UpdateTagKeyMetadataOut",
        "ListTagBindingsResponseIn": "_cloudresourcemanager_60_ListTagBindingsResponseIn",
        "ListTagBindingsResponseOut": "_cloudresourcemanager_61_ListTagBindingsResponseOut",
        "EffectiveTagIn": "_cloudresourcemanager_62_EffectiveTagIn",
        "EffectiveTagOut": "_cloudresourcemanager_63_EffectiveTagOut",
        "DeleteTagValueMetadataIn": "_cloudresourcemanager_64_DeleteTagValueMetadataIn",
        "DeleteTagValueMetadataOut": "_cloudresourcemanager_65_DeleteTagValueMetadataOut",
        "GetIamPolicyRequestIn": "_cloudresourcemanager_66_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_cloudresourcemanager_67_GetIamPolicyRequestOut",
        "UpdateTagValueMetadataIn": "_cloudresourcemanager_68_UpdateTagValueMetadataIn",
        "UpdateTagValueMetadataOut": "_cloudresourcemanager_69_UpdateTagValueMetadataOut",
        "ProjectIn": "_cloudresourcemanager_70_ProjectIn",
        "ProjectOut": "_cloudresourcemanager_71_ProjectOut",
        "OperationIn": "_cloudresourcemanager_72_OperationIn",
        "OperationOut": "_cloudresourcemanager_73_OperationOut",
        "UndeleteOrganizationMetadataIn": "_cloudresourcemanager_74_UndeleteOrganizationMetadataIn",
        "UndeleteOrganizationMetadataOut": "_cloudresourcemanager_75_UndeleteOrganizationMetadataOut",
        "ListTagHoldsResponseIn": "_cloudresourcemanager_76_ListTagHoldsResponseIn",
        "ListTagHoldsResponseOut": "_cloudresourcemanager_77_ListTagHoldsResponseOut",
        "UpdateProjectMetadataIn": "_cloudresourcemanager_78_UpdateProjectMetadataIn",
        "UpdateProjectMetadataOut": "_cloudresourcemanager_79_UpdateProjectMetadataOut",
        "AuditConfigIn": "_cloudresourcemanager_80_AuditConfigIn",
        "AuditConfigOut": "_cloudresourcemanager_81_AuditConfigOut",
        "ListProjectsResponseIn": "_cloudresourcemanager_82_ListProjectsResponseIn",
        "ListProjectsResponseOut": "_cloudresourcemanager_83_ListProjectsResponseOut",
        "GetPolicyOptionsIn": "_cloudresourcemanager_84_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_cloudresourcemanager_85_GetPolicyOptionsOut",
        "CreateProjectMetadataIn": "_cloudresourcemanager_86_CreateProjectMetadataIn",
        "CreateProjectMetadataOut": "_cloudresourcemanager_87_CreateProjectMetadataOut",
        "OrganizationIn": "_cloudresourcemanager_88_OrganizationIn",
        "OrganizationOut": "_cloudresourcemanager_89_OrganizationOut",
        "UndeleteProjectRequestIn": "_cloudresourcemanager_90_UndeleteProjectRequestIn",
        "UndeleteProjectRequestOut": "_cloudresourcemanager_91_UndeleteProjectRequestOut",
        "TagKeyIn": "_cloudresourcemanager_92_TagKeyIn",
        "TagKeyOut": "_cloudresourcemanager_93_TagKeyOut",
        "ListEffectiveTagsResponseIn": "_cloudresourcemanager_94_ListEffectiveTagsResponseIn",
        "ListEffectiveTagsResponseOut": "_cloudresourcemanager_95_ListEffectiveTagsResponseOut",
        "UpdateFolderMetadataIn": "_cloudresourcemanager_96_UpdateFolderMetadataIn",
        "UpdateFolderMetadataOut": "_cloudresourcemanager_97_UpdateFolderMetadataOut",
        "FolderOperationErrorIn": "_cloudresourcemanager_98_FolderOperationErrorIn",
        "FolderOperationErrorOut": "_cloudresourcemanager_99_FolderOperationErrorOut",
        "MoveProjectRequestIn": "_cloudresourcemanager_100_MoveProjectRequestIn",
        "MoveProjectRequestOut": "_cloudresourcemanager_101_MoveProjectRequestOut",
        "ProjectCreationStatusIn": "_cloudresourcemanager_102_ProjectCreationStatusIn",
        "ProjectCreationStatusOut": "_cloudresourcemanager_103_ProjectCreationStatusOut",
        "ListFoldersResponseIn": "_cloudresourcemanager_104_ListFoldersResponseIn",
        "ListFoldersResponseOut": "_cloudresourcemanager_105_ListFoldersResponseOut",
        "EmptyIn": "_cloudresourcemanager_106_EmptyIn",
        "EmptyOut": "_cloudresourcemanager_107_EmptyOut",
        "TestIamPermissionsRequestIn": "_cloudresourcemanager_108_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudresourcemanager_109_TestIamPermissionsRequestOut",
        "FolderOperationIn": "_cloudresourcemanager_110_FolderOperationIn",
        "FolderOperationOut": "_cloudresourcemanager_111_FolderOperationOut",
        "FolderIn": "_cloudresourcemanager_112_FolderIn",
        "FolderOut": "_cloudresourcemanager_113_FolderOut",
        "CreateTagValueMetadataIn": "_cloudresourcemanager_114_CreateTagValueMetadataIn",
        "CreateTagValueMetadataOut": "_cloudresourcemanager_115_CreateTagValueMetadataOut",
        "UndeleteFolderMetadataIn": "_cloudresourcemanager_116_UndeleteFolderMetadataIn",
        "UndeleteFolderMetadataOut": "_cloudresourcemanager_117_UndeleteFolderMetadataOut",
        "CreateFolderMetadataIn": "_cloudresourcemanager_118_CreateFolderMetadataIn",
        "CreateFolderMetadataOut": "_cloudresourcemanager_119_CreateFolderMetadataOut",
        "DeleteTagBindingMetadataIn": "_cloudresourcemanager_120_DeleteTagBindingMetadataIn",
        "DeleteTagBindingMetadataOut": "_cloudresourcemanager_121_DeleteTagBindingMetadataOut",
        "ListTagKeysResponseIn": "_cloudresourcemanager_122_ListTagKeysResponseIn",
        "ListTagKeysResponseOut": "_cloudresourcemanager_123_ListTagKeysResponseOut",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn": "_cloudresourcemanager_124_CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut": "_cloudresourcemanager_125_CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["DeleteOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteOrganizationMetadataIn"])
    types["DeleteOrganizationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteOrganizationMetadataOut"])
    types["UndeleteFolderRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteFolderRequestIn"]
    )
    types["UndeleteFolderRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteFolderRequestOut"])
    types["DeleteTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagKeyMetadataIn"]
    )
    types["DeleteTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagKeyMetadataOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["TagBindingIn"] = t.struct(
        {
            "tagValue": t.string().optional(),
            "tagValueNamespacedName": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["TagBindingIn"])
    types["TagBindingOut"] = t.struct(
        {
            "tagValue": t.string().optional(),
            "tagValueNamespacedName": t.string().optional(),
            "parent": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagBindingOut"])
    types["PolicyIn"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "version": t.integer().optional(),
            "etag": t.string().optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
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
    types["SearchFoldersResponseIn"] = t.struct(
        {
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchFoldersResponseIn"])
    types["SearchFoldersResponseOut"] = t.struct(
        {
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchFoldersResponseOut"])
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
    types["TagValueIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "shortName": t.string(),
            "name": t.string().optional(),
        }
    ).named(renames["TagValueIn"])
    types["TagValueOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "namespacedName": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "shortName": t.string(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagValueOut"])
    types["MoveFolderRequestIn"] = t.struct({"destinationParent": t.string()}).named(
        renames["MoveFolderRequestIn"]
    )
    types["MoveFolderRequestOut"] = t.struct(
        {
            "destinationParent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveFolderRequestOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["DeleteProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteProjectMetadataIn"]
    )
    types["DeleteProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteProjectMetadataOut"])
    types["SearchProjectsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "projects": t.array(t.proxy(renames["ProjectIn"])).optional(),
        }
    ).named(renames["SearchProjectsResponseIn"])
    types["SearchProjectsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "projects": t.array(t.proxy(renames["ProjectOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchProjectsResponseOut"])
    types["DeleteFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteFolderMetadataIn"]
    )
    types["DeleteFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteFolderMetadataOut"])
    types["ListTagValuesResponseIn"] = t.struct(
        {
            "tagValues": t.array(t.proxy(renames["TagValueIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTagValuesResponseIn"])
    types["ListTagValuesResponseOut"] = t.struct(
        {
            "tagValues": t.array(t.proxy(renames["TagValueOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagValuesResponseOut"])
    types["MoveProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoveProjectMetadataIn"]
    )
    types["MoveProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveProjectMetadataOut"])
    types["MoveFolderMetadataIn"] = t.struct(
        {
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
        }
    ).named(renames["MoveFolderMetadataIn"])
    types["MoveFolderMetadataOut"] = t.struct(
        {
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveFolderMetadataOut"])
    types["ListLiensResponseIn"] = t.struct(
        {
            "liens": t.array(t.proxy(renames["LienIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListLiensResponseIn"])
    types["ListLiensResponseOut"] = t.struct(
        {
            "liens": t.array(t.proxy(renames["LienOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLiensResponseOut"])
    types["UndeleteProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteProjectMetadataIn"]
    )
    types["UndeleteProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteProjectMetadataOut"])
    types["TagHoldIn"] = t.struct(
        {
            "helpLink": t.string().optional(),
            "holder": t.string(),
            "origin": t.string().optional(),
        }
    ).named(renames["TagHoldIn"])
    types["TagHoldOut"] = t.struct(
        {
            "helpLink": t.string().optional(),
            "holder": t.string(),
            "origin": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagHoldOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["LienIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "restrictions": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "reason": t.string().optional(),
            "parent": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["LienIn"])
    types["LienOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "restrictions": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "reason": t.string().optional(),
            "parent": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LienOut"])
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn"
    ] = t.struct(
        {
            "sourceParent": t.string().optional(),
            "displayName": t.string().optional(),
            "destinationParent": t.string().optional(),
            "operationType": t.string().optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn"
        ]
    )
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut"
    ] = t.struct(
        {
            "sourceParent": t.string().optional(),
            "displayName": t.string().optional(),
            "destinationParent": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut"
        ]
    )
    types["CreateTagBindingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagBindingMetadataIn"]
    )
    types["CreateTagBindingMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagBindingMetadataOut"])
    types["CreateTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagKeyMetadataIn"]
    )
    types["CreateTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagKeyMetadataOut"])
    types["SearchOrganizationsResponseIn"] = t.struct(
        {
            "organizations": t.array(t.proxy(renames["OrganizationIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchOrganizationsResponseIn"])
    types["SearchOrganizationsResponseOut"] = t.struct(
        {
            "organizations": t.array(t.proxy(renames["OrganizationOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchOrganizationsResponseOut"])
    types["UpdateTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateTagKeyMetadataIn"]
    )
    types["UpdateTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateTagKeyMetadataOut"])
    types["ListTagBindingsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tagBindings": t.array(t.proxy(renames["TagBindingIn"])).optional(),
        }
    ).named(renames["ListTagBindingsResponseIn"])
    types["ListTagBindingsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tagBindings": t.array(t.proxy(renames["TagBindingOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagBindingsResponseOut"])
    types["EffectiveTagIn"] = t.struct(
        {
            "namespacedTagValue": t.string().optional(),
            "tagValue": t.string().optional(),
            "namespacedTagKey": t.string().optional(),
            "inherited": t.boolean().optional(),
            "tagKeyParentName": t.string().optional(),
            "tagKey": t.string().optional(),
        }
    ).named(renames["EffectiveTagIn"])
    types["EffectiveTagOut"] = t.struct(
        {
            "namespacedTagValue": t.string().optional(),
            "tagValue": t.string().optional(),
            "namespacedTagKey": t.string().optional(),
            "inherited": t.boolean().optional(),
            "tagKeyParentName": t.string().optional(),
            "tagKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EffectiveTagOut"])
    types["DeleteTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagValueMetadataIn"]
    )
    types["DeleteTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagValueMetadataOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["UpdateTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateTagValueMetadataIn"]
    )
    types["UpdateTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateTagValueMetadataOut"])
    types["ProjectIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "projectId": t.string().optional(),
            "createTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "deleteTime": t.string().optional(),
            "parent": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
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
    types["UndeleteOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UndeleteOrganizationMetadataIn"])
    types["UndeleteOrganizationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteOrganizationMetadataOut"])
    types["ListTagHoldsResponseIn"] = t.struct(
        {
            "tagHolds": t.array(t.proxy(renames["TagHoldIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTagHoldsResponseIn"])
    types["ListTagHoldsResponseOut"] = t.struct(
        {
            "tagHolds": t.array(t.proxy(renames["TagHoldOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagHoldsResponseOut"])
    types["UpdateProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateProjectMetadataIn"]
    )
    types["UpdateProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateProjectMetadataOut"])
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
    types["ListProjectsResponseIn"] = t.struct(
        {
            "projects": t.array(t.proxy(renames["ProjectIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListProjectsResponseIn"])
    types["ListProjectsResponseOut"] = t.struct(
        {
            "projects": t.array(t.proxy(renames["ProjectOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListProjectsResponseOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["CreateProjectMetadataIn"] = t.struct(
        {
            "gettable": t.boolean().optional(),
            "ready": t.boolean().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["CreateProjectMetadataIn"])
    types["CreateProjectMetadataOut"] = t.struct(
        {
            "gettable": t.boolean().optional(),
            "ready": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateProjectMetadataOut"])
    types["OrganizationIn"] = t.struct(
        {"directoryCustomerId": t.string().optional()}
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "directoryCustomerId": t.string().optional(),
            "state": t.string().optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationOut"])
    types["UndeleteProjectRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteProjectRequestIn"]
    )
    types["UndeleteProjectRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteProjectRequestOut"])
    types["TagKeyIn"] = t.struct(
        {
            "parent": t.string().optional(),
            "etag": t.string().optional(),
            "purposeData": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "shortName": t.string(),
            "purpose": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["TagKeyIn"])
    types["TagKeyOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "purposeData": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "namespacedName": t.string().optional(),
            "shortName": t.string(),
            "purpose": t.string().optional(),
            "createTime": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagKeyOut"])
    types["ListEffectiveTagsResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "effectiveTags": t.array(t.proxy(renames["EffectiveTagIn"])).optional(),
        }
    ).named(renames["ListEffectiveTagsResponseIn"])
    types["ListEffectiveTagsResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "effectiveTags": t.array(t.proxy(renames["EffectiveTagOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEffectiveTagsResponseOut"])
    types["UpdateFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateFolderMetadataIn"]
    )
    types["UpdateFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateFolderMetadataOut"])
    types["FolderOperationErrorIn"] = t.struct(
        {"errorMessageId": t.string().optional()}
    ).named(renames["FolderOperationErrorIn"])
    types["FolderOperationErrorOut"] = t.struct(
        {
            "errorMessageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOperationErrorOut"])
    types["MoveProjectRequestIn"] = t.struct({"destinationParent": t.string()}).named(
        renames["MoveProjectRequestIn"]
    )
    types["MoveProjectRequestOut"] = t.struct(
        {
            "destinationParent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveProjectRequestOut"])
    types["ProjectCreationStatusIn"] = t.struct(
        {
            "createTime": t.string().optional(),
            "gettable": t.boolean().optional(),
            "ready": t.boolean().optional(),
        }
    ).named(renames["ProjectCreationStatusIn"])
    types["ProjectCreationStatusOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "gettable": t.boolean().optional(),
            "ready": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectCreationStatusOut"])
    types["ListFoldersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
        }
    ).named(renames["ListFoldersResponseIn"])
    types["ListFoldersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFoldersResponseOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["FolderOperationIn"] = t.struct(
        {
            "operationType": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
            "destinationParent": t.string().optional(),
        }
    ).named(renames["FolderOperationIn"])
    types["FolderOperationOut"] = t.struct(
        {
            "operationType": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
            "destinationParent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOperationOut"])
    types["FolderIn"] = t.struct(
        {"parent": t.string(), "displayName": t.string().optional()}
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "parent": t.string(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["CreateTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagValueMetadataIn"]
    )
    types["CreateTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagValueMetadataOut"])
    types["UndeleteFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteFolderMetadataIn"]
    )
    types["UndeleteFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteFolderMetadataOut"])
    types["CreateFolderMetadataIn"] = t.struct(
        {"displayName": t.string().optional(), "parent": t.string().optional()}
    ).named(renames["CreateFolderMetadataIn"])
    types["CreateFolderMetadataOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFolderMetadataOut"])
    types["DeleteTagBindingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagBindingMetadataIn"]
    )
    types["DeleteTagBindingMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagBindingMetadataOut"])
    types["ListTagKeysResponseIn"] = t.struct(
        {
            "tagKeys": t.array(t.proxy(renames["TagKeyIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTagKeysResponseIn"])
    types["ListTagKeysResponseOut"] = t.struct(
        {
            "tagKeys": t.array(t.proxy(renames["TagKeyOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagKeysResponseOut"])
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn"
    ] = t.struct(
        {
            "displayName": t.string().optional(),
            "operationType": t.string().optional(),
            "destinationParent": t.string().optional(),
            "sourceParent": t.string().optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn"
        ]
    )
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut"
    ] = t.struct(
        {
            "displayName": t.string().optional(),
            "operationType": t.string().optional(),
            "destinationParent": t.string().optional(),
            "sourceParent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut"
        ]
    )

    functions = {}
    functions["projectsSetIamPolicy"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsMove"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsList"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsDelete"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsGetIamPolicy"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsSearch"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsPatch"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsUndelete"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsGet"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsCreate"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["projectsTestIamPermissions"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["foldersSetIamPolicy"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersCreate"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersList"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMove"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSearch"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersTestIamPermissions"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGet"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPatch"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersUndelete"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetIamPolicy"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersDelete"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensCreate"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LienOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensList"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LienOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensDelete"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LienOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensGet"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["LienOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["operationsGet"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagBindingsDelete"] = cloudresourcemanager.post(
        "v3/tagBindings",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "tagValue": t.string().optional(),
                "tagValueNamespacedName": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagBindingsList"] = cloudresourcemanager.post(
        "v3/tagBindings",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "tagValue": t.string().optional(),
                "tagValueNamespacedName": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagBindingsCreate"] = cloudresourcemanager.post(
        "v3/tagBindings",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "tagValue": t.string().optional(),
                "tagValueNamespacedName": t.string().optional(),
                "parent": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGetIamPolicy"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["tagKeysList"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["tagKeysSetIamPolicy"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["tagKeysGetNamespaced"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["tagKeysCreate"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["tagKeysDelete"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["tagKeysPatch"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["tagKeysGet"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["tagKeysTestIamPermissions"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["effectiveTagsList"] = cloudresourcemanager.get(
        "v3/effectiveTags",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEffectiveTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesSetIamPolicy"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesPatch"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesGetIamPolicy"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesList"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesTestIamPermissions"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesGetNamespaced"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesGet"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesCreate"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesDelete"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "etag": t.string().optional(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesTagHoldsList"] = cloudresourcemanager.post(
        "v3/{parent}/tagHolds",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "helpLink": t.string().optional(),
                "holder": t.string(),
                "origin": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesTagHoldsDelete"] = cloudresourcemanager.post(
        "v3/{parent}/tagHolds",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "helpLink": t.string().optional(),
                "holder": t.string(),
                "origin": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesTagHoldsCreate"] = cloudresourcemanager.post(
        "v3/{parent}/tagHolds",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "parent": t.string(),
                "helpLink": t.string().optional(),
                "holder": t.string(),
                "origin": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSetIamPolicy"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["organizationsGetIamPolicy"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["organizationsGet"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["organizationsSearch"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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
    functions["organizationsTestIamPermissions"] = cloudresourcemanager.post(
        "v3/{resource}:testIamPermissions",
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

    return Import(
        importer="cloudresourcemanager",
        renames=renames,
        types=types,
        functions=functions,
    )
