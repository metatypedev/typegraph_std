from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudresourcemanager() -> Import:
    cloudresourcemanager = HTTPRuntime("https://cloudresourcemanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudresourcemanager_1_ErrorResponse",
        "StatusIn": "_cloudresourcemanager_2_StatusIn",
        "StatusOut": "_cloudresourcemanager_3_StatusOut",
        "TestIamPermissionsRequestIn": "_cloudresourcemanager_4_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudresourcemanager_5_TestIamPermissionsRequestOut",
        "EffectiveTagIn": "_cloudresourcemanager_6_EffectiveTagIn",
        "EffectiveTagOut": "_cloudresourcemanager_7_EffectiveTagOut",
        "FolderIn": "_cloudresourcemanager_8_FolderIn",
        "FolderOut": "_cloudresourcemanager_9_FolderOut",
        "CreateTagValueMetadataIn": "_cloudresourcemanager_10_CreateTagValueMetadataIn",
        "CreateTagValueMetadataOut": "_cloudresourcemanager_11_CreateTagValueMetadataOut",
        "ExprIn": "_cloudresourcemanager_12_ExprIn",
        "ExprOut": "_cloudresourcemanager_13_ExprOut",
        "DeleteFolderMetadataIn": "_cloudresourcemanager_14_DeleteFolderMetadataIn",
        "DeleteFolderMetadataOut": "_cloudresourcemanager_15_DeleteFolderMetadataOut",
        "MoveProjectRequestIn": "_cloudresourcemanager_16_MoveProjectRequestIn",
        "MoveProjectRequestOut": "_cloudresourcemanager_17_MoveProjectRequestOut",
        "DeleteTagKeyMetadataIn": "_cloudresourcemanager_18_DeleteTagKeyMetadataIn",
        "DeleteTagKeyMetadataOut": "_cloudresourcemanager_19_DeleteTagKeyMetadataOut",
        "EmptyIn": "_cloudresourcemanager_20_EmptyIn",
        "EmptyOut": "_cloudresourcemanager_21_EmptyOut",
        "SearchProjectsResponseIn": "_cloudresourcemanager_22_SearchProjectsResponseIn",
        "SearchProjectsResponseOut": "_cloudresourcemanager_23_SearchProjectsResponseOut",
        "OperationIn": "_cloudresourcemanager_24_OperationIn",
        "OperationOut": "_cloudresourcemanager_25_OperationOut",
        "MoveFolderMetadataIn": "_cloudresourcemanager_26_MoveFolderMetadataIn",
        "MoveFolderMetadataOut": "_cloudresourcemanager_27_MoveFolderMetadataOut",
        "DeleteOrganizationMetadataIn": "_cloudresourcemanager_28_DeleteOrganizationMetadataIn",
        "DeleteOrganizationMetadataOut": "_cloudresourcemanager_29_DeleteOrganizationMetadataOut",
        "SearchFoldersResponseIn": "_cloudresourcemanager_30_SearchFoldersResponseIn",
        "SearchFoldersResponseOut": "_cloudresourcemanager_31_SearchFoldersResponseOut",
        "ListProjectsResponseIn": "_cloudresourcemanager_32_ListProjectsResponseIn",
        "ListProjectsResponseOut": "_cloudresourcemanager_33_ListProjectsResponseOut",
        "FolderOperationErrorIn": "_cloudresourcemanager_34_FolderOperationErrorIn",
        "FolderOperationErrorOut": "_cloudresourcemanager_35_FolderOperationErrorOut",
        "UpdateTagValueMetadataIn": "_cloudresourcemanager_36_UpdateTagValueMetadataIn",
        "UpdateTagValueMetadataOut": "_cloudresourcemanager_37_UpdateTagValueMetadataOut",
        "DeleteTagValueMetadataIn": "_cloudresourcemanager_38_DeleteTagValueMetadataIn",
        "DeleteTagValueMetadataOut": "_cloudresourcemanager_39_DeleteTagValueMetadataOut",
        "UpdateTagKeyMetadataIn": "_cloudresourcemanager_40_UpdateTagKeyMetadataIn",
        "UpdateTagKeyMetadataOut": "_cloudresourcemanager_41_UpdateTagKeyMetadataOut",
        "CreateTagKeyMetadataIn": "_cloudresourcemanager_42_CreateTagKeyMetadataIn",
        "CreateTagKeyMetadataOut": "_cloudresourcemanager_43_CreateTagKeyMetadataOut",
        "ListTagHoldsResponseIn": "_cloudresourcemanager_44_ListTagHoldsResponseIn",
        "ListTagHoldsResponseOut": "_cloudresourcemanager_45_ListTagHoldsResponseOut",
        "DeleteTagBindingMetadataIn": "_cloudresourcemanager_46_DeleteTagBindingMetadataIn",
        "DeleteTagBindingMetadataOut": "_cloudresourcemanager_47_DeleteTagBindingMetadataOut",
        "UpdateProjectMetadataIn": "_cloudresourcemanager_48_UpdateProjectMetadataIn",
        "UpdateProjectMetadataOut": "_cloudresourcemanager_49_UpdateProjectMetadataOut",
        "AuditConfigIn": "_cloudresourcemanager_50_AuditConfigIn",
        "AuditConfigOut": "_cloudresourcemanager_51_AuditConfigOut",
        "CreateProjectMetadataIn": "_cloudresourcemanager_52_CreateProjectMetadataIn",
        "CreateProjectMetadataOut": "_cloudresourcemanager_53_CreateProjectMetadataOut",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn": "_cloudresourcemanager_54_CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut": "_cloudresourcemanager_55_CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut",
        "TagHoldIn": "_cloudresourcemanager_56_TagHoldIn",
        "TagHoldOut": "_cloudresourcemanager_57_TagHoldOut",
        "UndeleteProjectRequestIn": "_cloudresourcemanager_58_UndeleteProjectRequestIn",
        "UndeleteProjectRequestOut": "_cloudresourcemanager_59_UndeleteProjectRequestOut",
        "ListTagKeysResponseIn": "_cloudresourcemanager_60_ListTagKeysResponseIn",
        "ListTagKeysResponseOut": "_cloudresourcemanager_61_ListTagKeysResponseOut",
        "SearchOrganizationsResponseIn": "_cloudresourcemanager_62_SearchOrganizationsResponseIn",
        "SearchOrganizationsResponseOut": "_cloudresourcemanager_63_SearchOrganizationsResponseOut",
        "TagKeyIn": "_cloudresourcemanager_64_TagKeyIn",
        "TagKeyOut": "_cloudresourcemanager_65_TagKeyOut",
        "UndeleteOrganizationMetadataIn": "_cloudresourcemanager_66_UndeleteOrganizationMetadataIn",
        "UndeleteOrganizationMetadataOut": "_cloudresourcemanager_67_UndeleteOrganizationMetadataOut",
        "UndeleteFolderRequestIn": "_cloudresourcemanager_68_UndeleteFolderRequestIn",
        "UndeleteFolderRequestOut": "_cloudresourcemanager_69_UndeleteFolderRequestOut",
        "TagValueIn": "_cloudresourcemanager_70_TagValueIn",
        "TagValueOut": "_cloudresourcemanager_71_TagValueOut",
        "UndeleteProjectMetadataIn": "_cloudresourcemanager_72_UndeleteProjectMetadataIn",
        "UndeleteProjectMetadataOut": "_cloudresourcemanager_73_UndeleteProjectMetadataOut",
        "MoveProjectMetadataIn": "_cloudresourcemanager_74_MoveProjectMetadataIn",
        "MoveProjectMetadataOut": "_cloudresourcemanager_75_MoveProjectMetadataOut",
        "AuditLogConfigIn": "_cloudresourcemanager_76_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudresourcemanager_77_AuditLogConfigOut",
        "ProjectCreationStatusIn": "_cloudresourcemanager_78_ProjectCreationStatusIn",
        "ProjectCreationStatusOut": "_cloudresourcemanager_79_ProjectCreationStatusOut",
        "GetIamPolicyRequestIn": "_cloudresourcemanager_80_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_cloudresourcemanager_81_GetIamPolicyRequestOut",
        "CreateTagBindingMetadataIn": "_cloudresourcemanager_82_CreateTagBindingMetadataIn",
        "CreateTagBindingMetadataOut": "_cloudresourcemanager_83_CreateTagBindingMetadataOut",
        "PolicyIn": "_cloudresourcemanager_84_PolicyIn",
        "PolicyOut": "_cloudresourcemanager_85_PolicyOut",
        "TagBindingIn": "_cloudresourcemanager_86_TagBindingIn",
        "TagBindingOut": "_cloudresourcemanager_87_TagBindingOut",
        "SetIamPolicyRequestIn": "_cloudresourcemanager_88_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudresourcemanager_89_SetIamPolicyRequestOut",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn": "_cloudresourcemanager_90_CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut": "_cloudresourcemanager_91_CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut",
        "ListFoldersResponseIn": "_cloudresourcemanager_92_ListFoldersResponseIn",
        "ListFoldersResponseOut": "_cloudresourcemanager_93_ListFoldersResponseOut",
        "ListTagBindingsResponseIn": "_cloudresourcemanager_94_ListTagBindingsResponseIn",
        "ListTagBindingsResponseOut": "_cloudresourcemanager_95_ListTagBindingsResponseOut",
        "TestIamPermissionsResponseIn": "_cloudresourcemanager_96_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudresourcemanager_97_TestIamPermissionsResponseOut",
        "CreateFolderMetadataIn": "_cloudresourcemanager_98_CreateFolderMetadataIn",
        "CreateFolderMetadataOut": "_cloudresourcemanager_99_CreateFolderMetadataOut",
        "ListLiensResponseIn": "_cloudresourcemanager_100_ListLiensResponseIn",
        "ListLiensResponseOut": "_cloudresourcemanager_101_ListLiensResponseOut",
        "ProjectIn": "_cloudresourcemanager_102_ProjectIn",
        "ProjectOut": "_cloudresourcemanager_103_ProjectOut",
        "DeleteProjectMetadataIn": "_cloudresourcemanager_104_DeleteProjectMetadataIn",
        "DeleteProjectMetadataOut": "_cloudresourcemanager_105_DeleteProjectMetadataOut",
        "GetPolicyOptionsIn": "_cloudresourcemanager_106_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_cloudresourcemanager_107_GetPolicyOptionsOut",
        "FolderOperationIn": "_cloudresourcemanager_108_FolderOperationIn",
        "FolderOperationOut": "_cloudresourcemanager_109_FolderOperationOut",
        "UpdateFolderMetadataIn": "_cloudresourcemanager_110_UpdateFolderMetadataIn",
        "UpdateFolderMetadataOut": "_cloudresourcemanager_111_UpdateFolderMetadataOut",
        "ListTagValuesResponseIn": "_cloudresourcemanager_112_ListTagValuesResponseIn",
        "ListTagValuesResponseOut": "_cloudresourcemanager_113_ListTagValuesResponseOut",
        "ListEffectiveTagsResponseIn": "_cloudresourcemanager_114_ListEffectiveTagsResponseIn",
        "ListEffectiveTagsResponseOut": "_cloudresourcemanager_115_ListEffectiveTagsResponseOut",
        "OrganizationIn": "_cloudresourcemanager_116_OrganizationIn",
        "OrganizationOut": "_cloudresourcemanager_117_OrganizationOut",
        "UndeleteFolderMetadataIn": "_cloudresourcemanager_118_UndeleteFolderMetadataIn",
        "UndeleteFolderMetadataOut": "_cloudresourcemanager_119_UndeleteFolderMetadataOut",
        "MoveFolderRequestIn": "_cloudresourcemanager_120_MoveFolderRequestIn",
        "MoveFolderRequestOut": "_cloudresourcemanager_121_MoveFolderRequestOut",
        "LienIn": "_cloudresourcemanager_122_LienIn",
        "LienOut": "_cloudresourcemanager_123_LienOut",
        "BindingIn": "_cloudresourcemanager_124_BindingIn",
        "BindingOut": "_cloudresourcemanager_125_BindingOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["EffectiveTagIn"] = t.struct(
        {
            "tagValue": t.string().optional(),
            "tagKey": t.string().optional(),
            "namespacedTagKey": t.string().optional(),
            "tagKeyParentName": t.string().optional(),
            "inherited": t.boolean().optional(),
            "namespacedTagValue": t.string().optional(),
        }
    ).named(renames["EffectiveTagIn"])
    types["EffectiveTagOut"] = t.struct(
        {
            "tagValue": t.string().optional(),
            "tagKey": t.string().optional(),
            "namespacedTagKey": t.string().optional(),
            "tagKeyParentName": t.string().optional(),
            "inherited": t.boolean().optional(),
            "namespacedTagValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EffectiveTagOut"])
    types["FolderIn"] = t.struct(
        {"parent": t.string(), "displayName": t.string().optional()}
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "parent": t.string(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "name": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["CreateTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagValueMetadataIn"]
    )
    types["CreateTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagValueMetadataOut"])
    types["ExprIn"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
        }
    ).named(renames["ExprIn"])
    types["ExprOut"] = t.struct(
        {
            "title": t.string().optional(),
            "description": t.string().optional(),
            "expression": t.string().optional(),
            "location": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ExprOut"])
    types["DeleteFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteFolderMetadataIn"]
    )
    types["DeleteFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteFolderMetadataOut"])
    types["MoveProjectRequestIn"] = t.struct({"destinationParent": t.string()}).named(
        renames["MoveProjectRequestIn"]
    )
    types["MoveProjectRequestOut"] = t.struct(
        {
            "destinationParent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveProjectRequestOut"])
    types["DeleteTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagKeyMetadataIn"]
    )
    types["DeleteTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagKeyMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["SearchProjectsResponseIn"] = t.struct(
        {
            "projects": t.array(t.proxy(renames["ProjectIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["SearchProjectsResponseIn"])
    types["SearchProjectsResponseOut"] = t.struct(
        {
            "projects": t.array(t.proxy(renames["ProjectOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchProjectsResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "done": t.boolean().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["OperationOut"])
    types["MoveFolderMetadataIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "destinationParent": t.string().optional(),
            "sourceParent": t.string().optional(),
        }
    ).named(renames["MoveFolderMetadataIn"])
    types["MoveFolderMetadataOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "destinationParent": t.string().optional(),
            "sourceParent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveFolderMetadataOut"])
    types["DeleteOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteOrganizationMetadataIn"])
    types["DeleteOrganizationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteOrganizationMetadataOut"])
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
    types["FolderOperationErrorIn"] = t.struct(
        {"errorMessageId": t.string().optional()}
    ).named(renames["FolderOperationErrorIn"])
    types["FolderOperationErrorOut"] = t.struct(
        {
            "errorMessageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOperationErrorOut"])
    types["UpdateTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateTagValueMetadataIn"]
    )
    types["UpdateTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateTagValueMetadataOut"])
    types["DeleteTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagValueMetadataIn"]
    )
    types["DeleteTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagValueMetadataOut"])
    types["UpdateTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateTagKeyMetadataIn"]
    )
    types["UpdateTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateTagKeyMetadataOut"])
    types["CreateTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagKeyMetadataIn"]
    )
    types["CreateTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagKeyMetadataOut"])
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
    types["DeleteTagBindingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagBindingMetadataIn"]
    )
    types["DeleteTagBindingMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagBindingMetadataOut"])
    types["UpdateProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateProjectMetadataIn"]
    )
    types["UpdateProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateProjectMetadataOut"])
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
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn"
    ] = t.struct(
        {
            "sourceParent": t.string().optional(),
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
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
            "sourceParent": t.string().optional(),
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut"
        ]
    )
    types["TagHoldIn"] = t.struct(
        {
            "holder": t.string(),
            "origin": t.string().optional(),
            "helpLink": t.string().optional(),
        }
    ).named(renames["TagHoldIn"])
    types["TagHoldOut"] = t.struct(
        {
            "name": t.string().optional(),
            "holder": t.string(),
            "origin": t.string().optional(),
            "createTime": t.string().optional(),
            "helpLink": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagHoldOut"])
    types["UndeleteProjectRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteProjectRequestIn"]
    )
    types["UndeleteProjectRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteProjectRequestOut"])
    types["ListTagKeysResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tagKeys": t.array(t.proxy(renames["TagKeyIn"])).optional(),
        }
    ).named(renames["ListTagKeysResponseIn"])
    types["ListTagKeysResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tagKeys": t.array(t.proxy(renames["TagKeyOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagKeysResponseOut"])
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
    types["TagKeyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "purpose": t.string().optional(),
            "shortName": t.string(),
            "description": t.string().optional(),
            "purposeData": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["TagKeyIn"])
    types["TagKeyOut"] = t.struct(
        {
            "namespacedName": t.string().optional(),
            "etag": t.string().optional(),
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "purpose": t.string().optional(),
            "shortName": t.string(),
            "description": t.string().optional(),
            "purposeData": t.struct({"_": t.string().optional()}).optional(),
            "updateTime": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagKeyOut"])
    types["UndeleteOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UndeleteOrganizationMetadataIn"])
    types["UndeleteOrganizationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteOrganizationMetadataOut"])
    types["UndeleteFolderRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteFolderRequestIn"]
    )
    types["UndeleteFolderRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteFolderRequestOut"])
    types["TagValueIn"] = t.struct(
        {
            "description": t.string().optional(),
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "shortName": t.string(),
            "etag": t.string().optional(),
        }
    ).named(renames["TagValueIn"])
    types["TagValueOut"] = t.struct(
        {
            "namespacedName": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "parent": t.string().optional(),
            "shortName": t.string(),
            "createTime": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagValueOut"])
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
    types["ProjectCreationStatusIn"] = t.struct(
        {
            "ready": t.boolean().optional(),
            "gettable": t.boolean().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["ProjectCreationStatusIn"])
    types["ProjectCreationStatusOut"] = t.struct(
        {
            "ready": t.boolean().optional(),
            "gettable": t.boolean().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectCreationStatusOut"])
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["CreateTagBindingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagBindingMetadataIn"]
    )
    types["CreateTagBindingMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagBindingMetadataOut"])
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
    types["TagBindingIn"] = t.struct(
        {
            "tagValue": t.string().optional(),
            "parent": t.string().optional(),
            "tagValueNamespacedName": t.string().optional(),
        }
    ).named(renames["TagBindingIn"])
    types["TagBindingOut"] = t.struct(
        {
            "tagValue": t.string().optional(),
            "parent": t.string().optional(),
            "tagValueNamespacedName": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagBindingOut"])
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
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn"
    ] = t.struct(
        {
            "operationType": t.string().optional(),
            "destinationParent": t.string().optional(),
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
            "operationType": t.string().optional(),
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut"
        ]
    )
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
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
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
    types["ProjectIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "projectId": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "deleteTime": t.string().optional(),
            "displayName": t.string().optional(),
            "projectId": t.string().optional(),
            "state": t.string().optional(),
            "name": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parent": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["DeleteProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteProjectMetadataIn"]
    )
    types["DeleteProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteProjectMetadataOut"])
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["FolderOperationIn"] = t.struct(
        {
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
            "operationType": t.string().optional(),
            "destinationParent": t.string().optional(),
        }
    ).named(renames["FolderOperationIn"])
    types["FolderOperationOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "sourceParent": t.string().optional(),
            "operationType": t.string().optional(),
            "destinationParent": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOperationOut"])
    types["UpdateFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateFolderMetadataIn"]
    )
    types["UpdateFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateFolderMetadataOut"])
    types["ListTagValuesResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tagValues": t.array(t.proxy(renames["TagValueIn"])).optional(),
        }
    ).named(renames["ListTagValuesResponseIn"])
    types["ListTagValuesResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "tagValues": t.array(t.proxy(renames["TagValueOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListTagValuesResponseOut"])
    types["ListEffectiveTagsResponseIn"] = t.struct(
        {
            "effectiveTags": t.array(t.proxy(renames["EffectiveTagIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListEffectiveTagsResponseIn"])
    types["ListEffectiveTagsResponseOut"] = t.struct(
        {
            "effectiveTags": t.array(t.proxy(renames["EffectiveTagOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListEffectiveTagsResponseOut"])
    types["OrganizationIn"] = t.struct(
        {"directoryCustomerId": t.string().optional()}
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "updateTime": t.string().optional(),
            "deleteTime": t.string().optional(),
            "etag": t.string().optional(),
            "directoryCustomerId": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationOut"])
    types["UndeleteFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteFolderMetadataIn"]
    )
    types["UndeleteFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteFolderMetadataOut"])
    types["MoveFolderRequestIn"] = t.struct({"destinationParent": t.string()}).named(
        renames["MoveFolderRequestIn"]
    )
    types["MoveFolderRequestOut"] = t.struct(
        {
            "destinationParent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveFolderRequestOut"])
    types["LienIn"] = t.struct(
        {
            "restrictions": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "parent": t.string().optional(),
            "reason": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
        }
    ).named(renames["LienIn"])
    types["LienOut"] = t.struct(
        {
            "restrictions": t.array(t.string()).optional(),
            "origin": t.string().optional(),
            "parent": t.string().optional(),
            "reason": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LienOut"])
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

    functions = {}
    functions["liensDelete"] = cloudresourcemanager.get(
        "v3/liens",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLiensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensGet"] = cloudresourcemanager.get(
        "v3/liens",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLiensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensCreate"] = cloudresourcemanager.get(
        "v3/liens",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLiensResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensList"] = cloudresourcemanager.get(
        "v3/liens",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "parent": t.string(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListLiensResponseOut"]),
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
    functions["foldersSearch"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGetIamPolicy"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersList"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersDelete"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersUndelete"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersTestIamPermissions"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersCreate"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSetIamPolicy"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersGet"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersPatch"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersMove"] = cloudresourcemanager.post(
        "v3/{name}:move",
        t.struct(
            {
                "name": t.string(),
                "destinationParent": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetIamPolicy"] = cloudresourcemanager.post(
        "v3/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSearch"] = cloudresourcemanager.post(
        "v3/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGet"] = cloudresourcemanager.post(
        "v3/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsTestIamPermissions"] = cloudresourcemanager.post(
        "v3/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSetIamPolicy"] = cloudresourcemanager.post(
        "v3/{resource}:setIamPolicy",
        t.struct(
            {
                "resource": t.string().optional(),
                "updateMask": t.string().optional(),
                "policy": t.proxy(renames["PolicyIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["PolicyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagBindingsDelete"] = cloudresourcemanager.get(
        "v3/tagBindings",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagBindingsCreate"] = cloudresourcemanager.get(
        "v3/tagBindings",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagBindingsList"] = cloudresourcemanager.get(
        "v3/tagBindings",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListTagBindingsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMove"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCreate"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestIamPermissions"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSearch"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatch"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUndelete"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetIamPolicy"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDelete"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsList"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSetIamPolicy"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["ProjectOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysPatch"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGetIamPolicy"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysCreate"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysSetIamPolicy"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGetNamespaced"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysList"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysDelete"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysTestIamPermissions"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagKeyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGet"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagKeyOut"]),
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

    return Import(
        importer="cloudresourcemanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
