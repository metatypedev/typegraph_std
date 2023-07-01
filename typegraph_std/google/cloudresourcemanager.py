from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudresourcemanager():
    cloudresourcemanager = HTTPRuntime("https://cloudresourcemanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudresourcemanager_1_ErrorResponse",
        "TestIamPermissionsRequestIn": "_cloudresourcemanager_2_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudresourcemanager_3_TestIamPermissionsRequestOut",
        "UpdateFolderMetadataIn": "_cloudresourcemanager_4_UpdateFolderMetadataIn",
        "UpdateFolderMetadataOut": "_cloudresourcemanager_5_UpdateFolderMetadataOut",
        "ExprIn": "_cloudresourcemanager_6_ExprIn",
        "ExprOut": "_cloudresourcemanager_7_ExprOut",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn": "_cloudresourcemanager_8_CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut": "_cloudresourcemanager_9_CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut",
        "UndeleteProjectMetadataIn": "_cloudresourcemanager_10_UndeleteProjectMetadataIn",
        "UndeleteProjectMetadataOut": "_cloudresourcemanager_11_UndeleteProjectMetadataOut",
        "MoveProjectMetadataIn": "_cloudresourcemanager_12_MoveProjectMetadataIn",
        "MoveProjectMetadataOut": "_cloudresourcemanager_13_MoveProjectMetadataOut",
        "MoveFolderMetadataIn": "_cloudresourcemanager_14_MoveFolderMetadataIn",
        "MoveFolderMetadataOut": "_cloudresourcemanager_15_MoveFolderMetadataOut",
        "GetPolicyOptionsIn": "_cloudresourcemanager_16_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_cloudresourcemanager_17_GetPolicyOptionsOut",
        "DeleteOrganizationMetadataIn": "_cloudresourcemanager_18_DeleteOrganizationMetadataIn",
        "DeleteOrganizationMetadataOut": "_cloudresourcemanager_19_DeleteOrganizationMetadataOut",
        "PolicyIn": "_cloudresourcemanager_20_PolicyIn",
        "PolicyOut": "_cloudresourcemanager_21_PolicyOut",
        "TagBindingIn": "_cloudresourcemanager_22_TagBindingIn",
        "TagBindingOut": "_cloudresourcemanager_23_TagBindingOut",
        "OperationIn": "_cloudresourcemanager_24_OperationIn",
        "OperationOut": "_cloudresourcemanager_25_OperationOut",
        "DeleteFolderMetadataIn": "_cloudresourcemanager_26_DeleteFolderMetadataIn",
        "DeleteFolderMetadataOut": "_cloudresourcemanager_27_DeleteFolderMetadataOut",
        "UndeleteFolderRequestIn": "_cloudresourcemanager_28_UndeleteFolderRequestIn",
        "UndeleteFolderRequestOut": "_cloudresourcemanager_29_UndeleteFolderRequestOut",
        "DeleteTagValueMetadataIn": "_cloudresourcemanager_30_DeleteTagValueMetadataIn",
        "DeleteTagValueMetadataOut": "_cloudresourcemanager_31_DeleteTagValueMetadataOut",
        "DeleteTagKeyMetadataIn": "_cloudresourcemanager_32_DeleteTagKeyMetadataIn",
        "DeleteTagKeyMetadataOut": "_cloudresourcemanager_33_DeleteTagKeyMetadataOut",
        "CreateTagKeyMetadataIn": "_cloudresourcemanager_34_CreateTagKeyMetadataIn",
        "CreateTagKeyMetadataOut": "_cloudresourcemanager_35_CreateTagKeyMetadataOut",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn": "_cloudresourcemanager_36_CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut": "_cloudresourcemanager_37_CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut",
        "GetIamPolicyRequestIn": "_cloudresourcemanager_38_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_cloudresourcemanager_39_GetIamPolicyRequestOut",
        "CreateTagValueMetadataIn": "_cloudresourcemanager_40_CreateTagValueMetadataIn",
        "CreateTagValueMetadataOut": "_cloudresourcemanager_41_CreateTagValueMetadataOut",
        "DeleteTagBindingMetadataIn": "_cloudresourcemanager_42_DeleteTagBindingMetadataIn",
        "DeleteTagBindingMetadataOut": "_cloudresourcemanager_43_DeleteTagBindingMetadataOut",
        "CreateFolderMetadataIn": "_cloudresourcemanager_44_CreateFolderMetadataIn",
        "CreateFolderMetadataOut": "_cloudresourcemanager_45_CreateFolderMetadataOut",
        "AuditLogConfigIn": "_cloudresourcemanager_46_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudresourcemanager_47_AuditLogConfigOut",
        "UndeleteOrganizationMetadataIn": "_cloudresourcemanager_48_UndeleteOrganizationMetadataIn",
        "UndeleteOrganizationMetadataOut": "_cloudresourcemanager_49_UndeleteOrganizationMetadataOut",
        "CreateProjectMetadataIn": "_cloudresourcemanager_50_CreateProjectMetadataIn",
        "CreateProjectMetadataOut": "_cloudresourcemanager_51_CreateProjectMetadataOut",
        "ListEffectiveTagsResponseIn": "_cloudresourcemanager_52_ListEffectiveTagsResponseIn",
        "ListEffectiveTagsResponseOut": "_cloudresourcemanager_53_ListEffectiveTagsResponseOut",
        "MoveFolderRequestIn": "_cloudresourcemanager_54_MoveFolderRequestIn",
        "MoveFolderRequestOut": "_cloudresourcemanager_55_MoveFolderRequestOut",
        "SearchProjectsResponseIn": "_cloudresourcemanager_56_SearchProjectsResponseIn",
        "SearchProjectsResponseOut": "_cloudresourcemanager_57_SearchProjectsResponseOut",
        "ListTagKeysResponseIn": "_cloudresourcemanager_58_ListTagKeysResponseIn",
        "ListTagKeysResponseOut": "_cloudresourcemanager_59_ListTagKeysResponseOut",
        "ProjectCreationStatusIn": "_cloudresourcemanager_60_ProjectCreationStatusIn",
        "ProjectCreationStatusOut": "_cloudresourcemanager_61_ProjectCreationStatusOut",
        "LienIn": "_cloudresourcemanager_62_LienIn",
        "LienOut": "_cloudresourcemanager_63_LienOut",
        "FolderOperationIn": "_cloudresourcemanager_64_FolderOperationIn",
        "FolderOperationOut": "_cloudresourcemanager_65_FolderOperationOut",
        "ListFoldersResponseIn": "_cloudresourcemanager_66_ListFoldersResponseIn",
        "ListFoldersResponseOut": "_cloudresourcemanager_67_ListFoldersResponseOut",
        "CreateTagBindingMetadataIn": "_cloudresourcemanager_68_CreateTagBindingMetadataIn",
        "CreateTagBindingMetadataOut": "_cloudresourcemanager_69_CreateTagBindingMetadataOut",
        "TagValueIn": "_cloudresourcemanager_70_TagValueIn",
        "TagValueOut": "_cloudresourcemanager_71_TagValueOut",
        "TestIamPermissionsResponseIn": "_cloudresourcemanager_72_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudresourcemanager_73_TestIamPermissionsResponseOut",
        "ListTagValuesResponseIn": "_cloudresourcemanager_74_ListTagValuesResponseIn",
        "ListTagValuesResponseOut": "_cloudresourcemanager_75_ListTagValuesResponseOut",
        "UpdateTagKeyMetadataIn": "_cloudresourcemanager_76_UpdateTagKeyMetadataIn",
        "UpdateTagKeyMetadataOut": "_cloudresourcemanager_77_UpdateTagKeyMetadataOut",
        "BindingIn": "_cloudresourcemanager_78_BindingIn",
        "BindingOut": "_cloudresourcemanager_79_BindingOut",
        "DeleteProjectMetadataIn": "_cloudresourcemanager_80_DeleteProjectMetadataIn",
        "DeleteProjectMetadataOut": "_cloudresourcemanager_81_DeleteProjectMetadataOut",
        "FolderOperationErrorIn": "_cloudresourcemanager_82_FolderOperationErrorIn",
        "FolderOperationErrorOut": "_cloudresourcemanager_83_FolderOperationErrorOut",
        "EmptyIn": "_cloudresourcemanager_84_EmptyIn",
        "EmptyOut": "_cloudresourcemanager_85_EmptyOut",
        "ListTagHoldsResponseIn": "_cloudresourcemanager_86_ListTagHoldsResponseIn",
        "ListTagHoldsResponseOut": "_cloudresourcemanager_87_ListTagHoldsResponseOut",
        "ListProjectsResponseIn": "_cloudresourcemanager_88_ListProjectsResponseIn",
        "ListProjectsResponseOut": "_cloudresourcemanager_89_ListProjectsResponseOut",
        "ProjectIn": "_cloudresourcemanager_90_ProjectIn",
        "ProjectOut": "_cloudresourcemanager_91_ProjectOut",
        "OrganizationIn": "_cloudresourcemanager_92_OrganizationIn",
        "OrganizationOut": "_cloudresourcemanager_93_OrganizationOut",
        "UndeleteProjectRequestIn": "_cloudresourcemanager_94_UndeleteProjectRequestIn",
        "UndeleteProjectRequestOut": "_cloudresourcemanager_95_UndeleteProjectRequestOut",
        "TagKeyIn": "_cloudresourcemanager_96_TagKeyIn",
        "TagKeyOut": "_cloudresourcemanager_97_TagKeyOut",
        "MoveProjectRequestIn": "_cloudresourcemanager_98_MoveProjectRequestIn",
        "MoveProjectRequestOut": "_cloudresourcemanager_99_MoveProjectRequestOut",
        "UndeleteFolderMetadataIn": "_cloudresourcemanager_100_UndeleteFolderMetadataIn",
        "UndeleteFolderMetadataOut": "_cloudresourcemanager_101_UndeleteFolderMetadataOut",
        "FolderIn": "_cloudresourcemanager_102_FolderIn",
        "FolderOut": "_cloudresourcemanager_103_FolderOut",
        "SearchFoldersResponseIn": "_cloudresourcemanager_104_SearchFoldersResponseIn",
        "SearchFoldersResponseOut": "_cloudresourcemanager_105_SearchFoldersResponseOut",
        "TagHoldIn": "_cloudresourcemanager_106_TagHoldIn",
        "TagHoldOut": "_cloudresourcemanager_107_TagHoldOut",
        "SearchOrganizationsResponseIn": "_cloudresourcemanager_108_SearchOrganizationsResponseIn",
        "SearchOrganizationsResponseOut": "_cloudresourcemanager_109_SearchOrganizationsResponseOut",
        "AuditConfigIn": "_cloudresourcemanager_110_AuditConfigIn",
        "AuditConfigOut": "_cloudresourcemanager_111_AuditConfigOut",
        "StatusIn": "_cloudresourcemanager_112_StatusIn",
        "StatusOut": "_cloudresourcemanager_113_StatusOut",
        "UpdateTagValueMetadataIn": "_cloudresourcemanager_114_UpdateTagValueMetadataIn",
        "UpdateTagValueMetadataOut": "_cloudresourcemanager_115_UpdateTagValueMetadataOut",
        "ListLiensResponseIn": "_cloudresourcemanager_116_ListLiensResponseIn",
        "ListLiensResponseOut": "_cloudresourcemanager_117_ListLiensResponseOut",
        "ListTagBindingsResponseIn": "_cloudresourcemanager_118_ListTagBindingsResponseIn",
        "ListTagBindingsResponseOut": "_cloudresourcemanager_119_ListTagBindingsResponseOut",
        "SetIamPolicyRequestIn": "_cloudresourcemanager_120_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudresourcemanager_121_SetIamPolicyRequestOut",
        "EffectiveTagIn": "_cloudresourcemanager_122_EffectiveTagIn",
        "EffectiveTagOut": "_cloudresourcemanager_123_EffectiveTagOut",
        "UpdateProjectMetadataIn": "_cloudresourcemanager_124_UpdateProjectMetadataIn",
        "UpdateProjectMetadataOut": "_cloudresourcemanager_125_UpdateProjectMetadataOut",
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
    types["UpdateFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateFolderMetadataIn"]
    )
    types["UpdateFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateFolderMetadataOut"])
    types["ExprIn"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "description": t.string().optional(),
            "title": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn"
    ] = t.struct(
        {
            "destinationParent": t.string().optional(),
            "operationType": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
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
            "destinationParent": t.string().optional(),
            "operationType": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut"
        ]
    )
    types["UndeleteProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteProjectMetadataIn"]
    )
    types["UndeleteProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteProjectMetadataOut"])
    types["MoveProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoveProjectMetadataIn"]
    )
    types["MoveProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveProjectMetadataOut"])
    types["MoveFolderMetadataIn"] = t.struct(
        {
            "sourceParent": t.string().optional(),
            "displayName": t.string().optional(),
            "destinationParent": t.string().optional(),
        }
    ).named(renames["MoveFolderMetadataIn"])
    types["MoveFolderMetadataOut"] = t.struct(
        {
            "sourceParent": t.string().optional(),
            "displayName": t.string().optional(),
            "destinationParent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveFolderMetadataOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["DeleteOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteOrganizationMetadataIn"])
    types["DeleteOrganizationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteOrganizationMetadataOut"])
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
    types["OperationIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "done": t.boolean().optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["DeleteFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteFolderMetadataIn"]
    )
    types["DeleteFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteFolderMetadataOut"])
    types["UndeleteFolderRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteFolderRequestIn"]
    )
    types["UndeleteFolderRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteFolderRequestOut"])
    types["DeleteTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagValueMetadataIn"]
    )
    types["DeleteTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagValueMetadataOut"])
    types["DeleteTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagKeyMetadataIn"]
    )
    types["DeleteTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagKeyMetadataOut"])
    types["CreateTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagKeyMetadataIn"]
    )
    types["CreateTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagKeyMetadataOut"])
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn"
    ] = t.struct(
        {
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
            "operationType": t.string().optional(),
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
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut"
        ]
    )
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["CreateTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagValueMetadataIn"]
    )
    types["CreateTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagValueMetadataOut"])
    types["DeleteTagBindingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagBindingMetadataIn"]
    )
    types["DeleteTagBindingMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagBindingMetadataOut"])
    types["CreateFolderMetadataIn"] = t.struct(
        {"parent": t.string().optional(), "displayName": t.string().optional()}
    ).named(renames["CreateFolderMetadataIn"])
    types["CreateFolderMetadataOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateFolderMetadataOut"])
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
    types["UndeleteOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UndeleteOrganizationMetadataIn"])
    types["UndeleteOrganizationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteOrganizationMetadataOut"])
    types["CreateProjectMetadataIn"] = t.struct(
        {
            "ready": t.boolean().optional(),
            "createTime": t.string().optional(),
            "gettable": t.boolean().optional(),
        }
    ).named(renames["CreateProjectMetadataIn"])
    types["CreateProjectMetadataOut"] = t.struct(
        {
            "ready": t.boolean().optional(),
            "createTime": t.string().optional(),
            "gettable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateProjectMetadataOut"])
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
    types["MoveFolderRequestIn"] = t.struct({"destinationParent": t.string()}).named(
        renames["MoveFolderRequestIn"]
    )
    types["MoveFolderRequestOut"] = t.struct(
        {
            "destinationParent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveFolderRequestOut"])
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
    types["ProjectCreationStatusIn"] = t.struct(
        {
            "ready": t.boolean().optional(),
            "createTime": t.string().optional(),
            "gettable": t.boolean().optional(),
        }
    ).named(renames["ProjectCreationStatusIn"])
    types["ProjectCreationStatusOut"] = t.struct(
        {
            "ready": t.boolean().optional(),
            "createTime": t.string().optional(),
            "gettable": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectCreationStatusOut"])
    types["LienIn"] = t.struct(
        {
            "restrictions": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "origin": t.string().optional(),
            "createTime": t.string().optional(),
            "reason": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["LienIn"])
    types["LienOut"] = t.struct(
        {
            "restrictions": t.array(t.string()).optional(),
            "name": t.string().optional(),
            "origin": t.string().optional(),
            "createTime": t.string().optional(),
            "reason": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LienOut"])
    types["FolderOperationIn"] = t.struct(
        {
            "sourceParent": t.string().optional(),
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
            "operationType": t.string().optional(),
        }
    ).named(renames["FolderOperationIn"])
    types["FolderOperationOut"] = t.struct(
        {
            "sourceParent": t.string().optional(),
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOperationOut"])
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
    types["CreateTagBindingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagBindingMetadataIn"]
    )
    types["CreateTagBindingMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagBindingMetadataOut"])
    types["TagValueIn"] = t.struct(
        {
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "shortName": t.string(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["TagValueIn"])
    types["TagValueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "shortName": t.string(),
            "createTime": t.string().optional(),
            "namespacedName": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagValueOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["UpdateTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateTagKeyMetadataIn"]
    )
    types["UpdateTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateTagKeyMetadataOut"])
    types["BindingIn"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprIn"]).optional(),
        }
    ).named(renames["BindingIn"])
    types["BindingOut"] = t.struct(
        {
            "role": t.string().optional(),
            "members": t.array(t.string()).optional(),
            "condition": t.proxy(renames["ExprOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BindingOut"])
    types["DeleteProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteProjectMetadataIn"]
    )
    types["DeleteProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteProjectMetadataOut"])
    types["FolderOperationErrorIn"] = t.struct(
        {"errorMessageId": t.string().optional()}
    ).named(renames["FolderOperationErrorIn"])
    types["FolderOperationErrorOut"] = t.struct(
        {
            "errorMessageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOperationErrorOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["ProjectIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "updateTime": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "projectId": t.string().optional(),
            "parent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["OrganizationIn"] = t.struct(
        {"directoryCustomerId": t.string().optional()}
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "displayName": t.string().optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "directoryCustomerId": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
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
            "shortName": t.string(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "parent": t.string().optional(),
            "purpose": t.string().optional(),
            "purposeData": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TagKeyIn"])
    types["TagKeyOut"] = t.struct(
        {
            "namespacedName": t.string().optional(),
            "createTime": t.string().optional(),
            "shortName": t.string(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "description": t.string().optional(),
            "parent": t.string().optional(),
            "purpose": t.string().optional(),
            "purposeData": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagKeyOut"])
    types["MoveProjectRequestIn"] = t.struct({"destinationParent": t.string()}).named(
        renames["MoveProjectRequestIn"]
    )
    types["MoveProjectRequestOut"] = t.struct(
        {
            "destinationParent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveProjectRequestOut"])
    types["UndeleteFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteFolderMetadataIn"]
    )
    types["UndeleteFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteFolderMetadataOut"])
    types["FolderIn"] = t.struct(
        {"parent": t.string(), "displayName": t.string().optional()}
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "parent": t.string(),
            "displayName": t.string().optional(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
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
    types["TagHoldIn"] = t.struct(
        {
            "origin": t.string().optional(),
            "helpLink": t.string().optional(),
            "holder": t.string(),
        }
    ).named(renames["TagHoldIn"])
    types["TagHoldOut"] = t.struct(
        {
            "origin": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "helpLink": t.string().optional(),
            "holder": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagHoldOut"])
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
    types["UpdateTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateTagValueMetadataIn"]
    )
    types["UpdateTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateTagValueMetadataOut"])
    types["ListLiensResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "liens": t.array(t.proxy(renames["LienIn"])).optional(),
        }
    ).named(renames["ListLiensResponseIn"])
    types["ListLiensResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "liens": t.array(t.proxy(renames["LienOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListLiensResponseOut"])
    types["ListTagBindingsResponseIn"] = t.struct(
        {
            "tagBindings": t.array(t.proxy(renames["TagBindingIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListTagBindingsResponseIn"])
    types["ListTagBindingsResponseOut"] = t.struct(
        {
            "tagBindings": t.array(t.proxy(renames["TagBindingOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagBindingsResponseOut"])
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
    types["EffectiveTagIn"] = t.struct(
        {
            "namespacedTagValue": t.string().optional(),
            "namespacedTagKey": t.string().optional(),
            "tagKeyParentName": t.string().optional(),
            "tagKey": t.string().optional(),
            "tagValue": t.string().optional(),
            "inherited": t.boolean().optional(),
        }
    ).named(renames["EffectiveTagIn"])
    types["EffectiveTagOut"] = t.struct(
        {
            "namespacedTagValue": t.string().optional(),
            "namespacedTagKey": t.string().optional(),
            "tagKeyParentName": t.string().optional(),
            "tagKey": t.string().optional(),
            "tagValue": t.string().optional(),
            "inherited": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EffectiveTagOut"])
    types["UpdateProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateProjectMetadataIn"]
    )
    types["UpdateProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateProjectMetadataOut"])

    functions = {}
    functions["tagValuesTestIamPermissions"] = cloudresourcemanager.get(
        "v3/tagValues/namespaced",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesSetIamPolicy"] = cloudresourcemanager.get(
        "v3/tagValues/namespaced",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesGetIamPolicy"] = cloudresourcemanager.get(
        "v3/tagValues/namespaced",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesGet"] = cloudresourcemanager.get(
        "v3/tagValues/namespaced",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesList"] = cloudresourcemanager.get(
        "v3/tagValues/namespaced",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesDelete"] = cloudresourcemanager.get(
        "v3/tagValues/namespaced",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesCreate"] = cloudresourcemanager.get(
        "v3/tagValues/namespaced",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesPatch"] = cloudresourcemanager.get(
        "v3/tagValues/namespaced",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesGetNamespaced"] = cloudresourcemanager.get(
        "v3/tagValues/namespaced",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesTagHoldsList"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesTagHoldsCreate"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesTagHoldsDelete"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCreate"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestIamPermissions"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSearch"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSetIamPolicy"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsList"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMove"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetIamPolicy"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatch"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUndelete"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDelete"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysPatch"] = cloudresourcemanager.get(
        "v3/tagKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysTestIamPermissions"] = cloudresourcemanager.get(
        "v3/tagKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGetIamPolicy"] = cloudresourcemanager.get(
        "v3/tagKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysCreate"] = cloudresourcemanager.get(
        "v3/tagKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysDelete"] = cloudresourcemanager.get(
        "v3/tagKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGetNamespaced"] = cloudresourcemanager.get(
        "v3/tagKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysSetIamPolicy"] = cloudresourcemanager.get(
        "v3/tagKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGet"] = cloudresourcemanager.get(
        "v3/tagKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagKeysResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysList"] = cloudresourcemanager.get(
        "v3/tagKeys",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagKeysResponseOut"]),
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
    functions["liensGet"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensList"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensCreate"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensDelete"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["effectiveTagsList"] = cloudresourcemanager.get(
        "v3/effectiveTags",
        t.struct(
            {
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEffectiveTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSetIamPolicy"] = cloudresourcemanager.get(
        "v3/organizations:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOrganizationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGet"] = cloudresourcemanager.get(
        "v3/organizations:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOrganizationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetIamPolicy"] = cloudresourcemanager.get(
        "v3/organizations:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOrganizationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsTestIamPermissions"] = cloudresourcemanager.get(
        "v3/organizations:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOrganizationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSearch"] = cloudresourcemanager.get(
        "v3/organizations:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOrganizationsResponseOut"]),
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
    functions["foldersGetIamPolicy"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersUndelete"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersList"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSearch"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPatch"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersCreate"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersTestIamPermissions"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersDelete"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMove"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSetIamPolicy"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGet"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["FolderOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudresourcemanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
