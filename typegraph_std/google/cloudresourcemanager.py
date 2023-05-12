from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudresourcemanager() -> Import:
    cloudresourcemanager = HTTPRuntime("https://cloudresourcemanager.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudresourcemanager_1_ErrorResponse",
        "ListTagKeysResponseIn": "_cloudresourcemanager_2_ListTagKeysResponseIn",
        "ListTagKeysResponseOut": "_cloudresourcemanager_3_ListTagKeysResponseOut",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn": "_cloudresourcemanager_4_CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut": "_cloudresourcemanager_5_CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut",
        "UpdateTagValueMetadataIn": "_cloudresourcemanager_6_UpdateTagValueMetadataIn",
        "UpdateTagValueMetadataOut": "_cloudresourcemanager_7_UpdateTagValueMetadataOut",
        "DeleteTagKeyMetadataIn": "_cloudresourcemanager_8_DeleteTagKeyMetadataIn",
        "DeleteTagKeyMetadataOut": "_cloudresourcemanager_9_DeleteTagKeyMetadataOut",
        "ProjectCreationStatusIn": "_cloudresourcemanager_10_ProjectCreationStatusIn",
        "ProjectCreationStatusOut": "_cloudresourcemanager_11_ProjectCreationStatusOut",
        "ListLiensResponseIn": "_cloudresourcemanager_12_ListLiensResponseIn",
        "ListLiensResponseOut": "_cloudresourcemanager_13_ListLiensResponseOut",
        "TagKeyIn": "_cloudresourcemanager_14_TagKeyIn",
        "TagKeyOut": "_cloudresourcemanager_15_TagKeyOut",
        "CreateTagValueMetadataIn": "_cloudresourcemanager_16_CreateTagValueMetadataIn",
        "CreateTagValueMetadataOut": "_cloudresourcemanager_17_CreateTagValueMetadataOut",
        "UndeleteProjectMetadataIn": "_cloudresourcemanager_18_UndeleteProjectMetadataIn",
        "UndeleteProjectMetadataOut": "_cloudresourcemanager_19_UndeleteProjectMetadataOut",
        "AuditLogConfigIn": "_cloudresourcemanager_20_AuditLogConfigIn",
        "AuditLogConfigOut": "_cloudresourcemanager_21_AuditLogConfigOut",
        "ListTagValuesResponseIn": "_cloudresourcemanager_22_ListTagValuesResponseIn",
        "ListTagValuesResponseOut": "_cloudresourcemanager_23_ListTagValuesResponseOut",
        "GetPolicyOptionsIn": "_cloudresourcemanager_24_GetPolicyOptionsIn",
        "GetPolicyOptionsOut": "_cloudresourcemanager_25_GetPolicyOptionsOut",
        "DeleteTagValueMetadataIn": "_cloudresourcemanager_26_DeleteTagValueMetadataIn",
        "DeleteTagValueMetadataOut": "_cloudresourcemanager_27_DeleteTagValueMetadataOut",
        "OrganizationIn": "_cloudresourcemanager_28_OrganizationIn",
        "OrganizationOut": "_cloudresourcemanager_29_OrganizationOut",
        "FolderOperationIn": "_cloudresourcemanager_30_FolderOperationIn",
        "FolderOperationOut": "_cloudresourcemanager_31_FolderOperationOut",
        "TagValueIn": "_cloudresourcemanager_32_TagValueIn",
        "TagValueOut": "_cloudresourcemanager_33_TagValueOut",
        "FolderOperationErrorIn": "_cloudresourcemanager_34_FolderOperationErrorIn",
        "FolderOperationErrorOut": "_cloudresourcemanager_35_FolderOperationErrorOut",
        "MoveFolderMetadataIn": "_cloudresourcemanager_36_MoveFolderMetadataIn",
        "MoveFolderMetadataOut": "_cloudresourcemanager_37_MoveFolderMetadataOut",
        "SearchOrganizationsResponseIn": "_cloudresourcemanager_38_SearchOrganizationsResponseIn",
        "SearchOrganizationsResponseOut": "_cloudresourcemanager_39_SearchOrganizationsResponseOut",
        "ListEffectiveTagsResponseIn": "_cloudresourcemanager_40_ListEffectiveTagsResponseIn",
        "ListEffectiveTagsResponseOut": "_cloudresourcemanager_41_ListEffectiveTagsResponseOut",
        "GetIamPolicyRequestIn": "_cloudresourcemanager_42_GetIamPolicyRequestIn",
        "GetIamPolicyRequestOut": "_cloudresourcemanager_43_GetIamPolicyRequestOut",
        "TestIamPermissionsResponseIn": "_cloudresourcemanager_44_TestIamPermissionsResponseIn",
        "TestIamPermissionsResponseOut": "_cloudresourcemanager_45_TestIamPermissionsResponseOut",
        "ListFoldersResponseIn": "_cloudresourcemanager_46_ListFoldersResponseIn",
        "ListFoldersResponseOut": "_cloudresourcemanager_47_ListFoldersResponseOut",
        "TestIamPermissionsRequestIn": "_cloudresourcemanager_48_TestIamPermissionsRequestIn",
        "TestIamPermissionsRequestOut": "_cloudresourcemanager_49_TestIamPermissionsRequestOut",
        "FolderIn": "_cloudresourcemanager_50_FolderIn",
        "FolderOut": "_cloudresourcemanager_51_FolderOut",
        "SearchFoldersResponseIn": "_cloudresourcemanager_52_SearchFoldersResponseIn",
        "SearchFoldersResponseOut": "_cloudresourcemanager_53_SearchFoldersResponseOut",
        "OperationIn": "_cloudresourcemanager_54_OperationIn",
        "OperationOut": "_cloudresourcemanager_55_OperationOut",
        "StatusIn": "_cloudresourcemanager_56_StatusIn",
        "StatusOut": "_cloudresourcemanager_57_StatusOut",
        "UpdateFolderMetadataIn": "_cloudresourcemanager_58_UpdateFolderMetadataIn",
        "UpdateFolderMetadataOut": "_cloudresourcemanager_59_UpdateFolderMetadataOut",
        "EmptyIn": "_cloudresourcemanager_60_EmptyIn",
        "EmptyOut": "_cloudresourcemanager_61_EmptyOut",
        "MoveProjectRequestIn": "_cloudresourcemanager_62_MoveProjectRequestIn",
        "MoveProjectRequestOut": "_cloudresourcemanager_63_MoveProjectRequestOut",
        "CreateTagBindingMetadataIn": "_cloudresourcemanager_64_CreateTagBindingMetadataIn",
        "CreateTagBindingMetadataOut": "_cloudresourcemanager_65_CreateTagBindingMetadataOut",
        "ProjectIn": "_cloudresourcemanager_66_ProjectIn",
        "ProjectOut": "_cloudresourcemanager_67_ProjectOut",
        "PolicyIn": "_cloudresourcemanager_68_PolicyIn",
        "PolicyOut": "_cloudresourcemanager_69_PolicyOut",
        "UpdateTagKeyMetadataIn": "_cloudresourcemanager_70_UpdateTagKeyMetadataIn",
        "UpdateTagKeyMetadataOut": "_cloudresourcemanager_71_UpdateTagKeyMetadataOut",
        "CreateProjectMetadataIn": "_cloudresourcemanager_72_CreateProjectMetadataIn",
        "CreateProjectMetadataOut": "_cloudresourcemanager_73_CreateProjectMetadataOut",
        "BindingIn": "_cloudresourcemanager_74_BindingIn",
        "BindingOut": "_cloudresourcemanager_75_BindingOut",
        "ListTagBindingsResponseIn": "_cloudresourcemanager_76_ListTagBindingsResponseIn",
        "ListTagBindingsResponseOut": "_cloudresourcemanager_77_ListTagBindingsResponseOut",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn": "_cloudresourcemanager_78_CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn",
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut": "_cloudresourcemanager_79_CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut",
        "UndeleteFolderRequestIn": "_cloudresourcemanager_80_UndeleteFolderRequestIn",
        "UndeleteFolderRequestOut": "_cloudresourcemanager_81_UndeleteFolderRequestOut",
        "CreateTagKeyMetadataIn": "_cloudresourcemanager_82_CreateTagKeyMetadataIn",
        "CreateTagKeyMetadataOut": "_cloudresourcemanager_83_CreateTagKeyMetadataOut",
        "SetIamPolicyRequestIn": "_cloudresourcemanager_84_SetIamPolicyRequestIn",
        "SetIamPolicyRequestOut": "_cloudresourcemanager_85_SetIamPolicyRequestOut",
        "CreateFolderMetadataIn": "_cloudresourcemanager_86_CreateFolderMetadataIn",
        "CreateFolderMetadataOut": "_cloudresourcemanager_87_CreateFolderMetadataOut",
        "UndeleteProjectRequestIn": "_cloudresourcemanager_88_UndeleteProjectRequestIn",
        "UndeleteProjectRequestOut": "_cloudresourcemanager_89_UndeleteProjectRequestOut",
        "TagBindingIn": "_cloudresourcemanager_90_TagBindingIn",
        "TagBindingOut": "_cloudresourcemanager_91_TagBindingOut",
        "ListProjectsResponseIn": "_cloudresourcemanager_92_ListProjectsResponseIn",
        "ListProjectsResponseOut": "_cloudresourcemanager_93_ListProjectsResponseOut",
        "MoveProjectMetadataIn": "_cloudresourcemanager_94_MoveProjectMetadataIn",
        "MoveProjectMetadataOut": "_cloudresourcemanager_95_MoveProjectMetadataOut",
        "DeleteTagBindingMetadataIn": "_cloudresourcemanager_96_DeleteTagBindingMetadataIn",
        "DeleteTagBindingMetadataOut": "_cloudresourcemanager_97_DeleteTagBindingMetadataOut",
        "UndeleteOrganizationMetadataIn": "_cloudresourcemanager_98_UndeleteOrganizationMetadataIn",
        "UndeleteOrganizationMetadataOut": "_cloudresourcemanager_99_UndeleteOrganizationMetadataOut",
        "TagHoldIn": "_cloudresourcemanager_100_TagHoldIn",
        "TagHoldOut": "_cloudresourcemanager_101_TagHoldOut",
        "UndeleteFolderMetadataIn": "_cloudresourcemanager_102_UndeleteFolderMetadataIn",
        "UndeleteFolderMetadataOut": "_cloudresourcemanager_103_UndeleteFolderMetadataOut",
        "DeleteProjectMetadataIn": "_cloudresourcemanager_104_DeleteProjectMetadataIn",
        "DeleteProjectMetadataOut": "_cloudresourcemanager_105_DeleteProjectMetadataOut",
        "SearchProjectsResponseIn": "_cloudresourcemanager_106_SearchProjectsResponseIn",
        "SearchProjectsResponseOut": "_cloudresourcemanager_107_SearchProjectsResponseOut",
        "ExprIn": "_cloudresourcemanager_108_ExprIn",
        "ExprOut": "_cloudresourcemanager_109_ExprOut",
        "ListTagHoldsResponseIn": "_cloudresourcemanager_110_ListTagHoldsResponseIn",
        "ListTagHoldsResponseOut": "_cloudresourcemanager_111_ListTagHoldsResponseOut",
        "EffectiveTagIn": "_cloudresourcemanager_112_EffectiveTagIn",
        "EffectiveTagOut": "_cloudresourcemanager_113_EffectiveTagOut",
        "MoveFolderRequestIn": "_cloudresourcemanager_114_MoveFolderRequestIn",
        "MoveFolderRequestOut": "_cloudresourcemanager_115_MoveFolderRequestOut",
        "LienIn": "_cloudresourcemanager_116_LienIn",
        "LienOut": "_cloudresourcemanager_117_LienOut",
        "DeleteFolderMetadataIn": "_cloudresourcemanager_118_DeleteFolderMetadataIn",
        "DeleteFolderMetadataOut": "_cloudresourcemanager_119_DeleteFolderMetadataOut",
        "UpdateProjectMetadataIn": "_cloudresourcemanager_120_UpdateProjectMetadataIn",
        "UpdateProjectMetadataOut": "_cloudresourcemanager_121_UpdateProjectMetadataOut",
        "AuditConfigIn": "_cloudresourcemanager_122_AuditConfigIn",
        "AuditConfigOut": "_cloudresourcemanager_123_AuditConfigOut",
        "DeleteOrganizationMetadataIn": "_cloudresourcemanager_124_DeleteOrganizationMetadataIn",
        "DeleteOrganizationMetadataOut": "_cloudresourcemanager_125_DeleteOrganizationMetadataOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationIn"
    ] = t.struct(
        {
            "destinationParent": t.string().optional(),
            "sourceParent": t.string().optional(),
            "displayName": t.string().optional(),
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
            "destinationParent": t.string().optional(),
            "sourceParent": t.string().optional(),
            "displayName": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2beta1FolderOperationOut"
        ]
    )
    types["UpdateTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateTagValueMetadataIn"]
    )
    types["UpdateTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateTagValueMetadataOut"])
    types["DeleteTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagKeyMetadataIn"]
    )
    types["DeleteTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagKeyMetadataOut"])
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
    types["TagKeyIn"] = t.struct(
        {
            "name": t.string().optional(),
            "purpose": t.string().optional(),
            "shortName": t.string(),
            "purposeData": t.struct({"_": t.string().optional()}).optional(),
            "parent": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["TagKeyIn"])
    types["TagKeyOut"] = t.struct(
        {
            "name": t.string().optional(),
            "purpose": t.string().optional(),
            "createTime": t.string().optional(),
            "shortName": t.string(),
            "namespacedName": t.string().optional(),
            "purposeData": t.struct({"_": t.string().optional()}).optional(),
            "parent": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "description": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagKeyOut"])
    types["CreateTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagValueMetadataIn"]
    )
    types["CreateTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagValueMetadataOut"])
    types["UndeleteProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteProjectMetadataIn"]
    )
    types["UndeleteProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteProjectMetadataOut"])
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
    types["GetPolicyOptionsIn"] = t.struct(
        {"requestedPolicyVersion": t.integer().optional()}
    ).named(renames["GetPolicyOptionsIn"])
    types["GetPolicyOptionsOut"] = t.struct(
        {
            "requestedPolicyVersion": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetPolicyOptionsOut"])
    types["DeleteTagValueMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagValueMetadataIn"]
    )
    types["DeleteTagValueMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagValueMetadataOut"])
    types["OrganizationIn"] = t.struct(
        {"directoryCustomerId": t.string().optional()}
    ).named(renames["OrganizationIn"])
    types["OrganizationOut"] = t.struct(
        {
            "directoryCustomerId": t.string().optional(),
            "deleteTime": t.string().optional(),
            "name": t.string().optional(),
            "createTime": t.string().optional(),
            "state": t.string().optional(),
            "displayName": t.string().optional(),
            "updateTime": t.string().optional(),
            "etag": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["OrganizationOut"])
    types["FolderOperationIn"] = t.struct(
        {
            "destinationParent": t.string().optional(),
            "sourceParent": t.string().optional(),
            "displayName": t.string().optional(),
            "operationType": t.string().optional(),
        }
    ).named(renames["FolderOperationIn"])
    types["FolderOperationOut"] = t.struct(
        {
            "destinationParent": t.string().optional(),
            "sourceParent": t.string().optional(),
            "displayName": t.string().optional(),
            "operationType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOperationOut"])
    types["TagValueIn"] = t.struct(
        {
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "parent": t.string().optional(),
            "description": t.string().optional(),
            "shortName": t.string(),
        }
    ).named(renames["TagValueIn"])
    types["TagValueOut"] = t.struct(
        {
            "name": t.string().optional(),
            "etag": t.string().optional(),
            "parent": t.string().optional(),
            "createTime": t.string().optional(),
            "updateTime": t.string().optional(),
            "description": t.string().optional(),
            "shortName": t.string(),
            "namespacedName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagValueOut"])
    types["FolderOperationErrorIn"] = t.struct(
        {"errorMessageId": t.string().optional()}
    ).named(renames["FolderOperationErrorIn"])
    types["FolderOperationErrorOut"] = t.struct(
        {
            "errorMessageId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOperationErrorOut"])
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
    types["GetIamPolicyRequestIn"] = t.struct(
        {"options": t.proxy(renames["GetPolicyOptionsIn"]).optional()}
    ).named(renames["GetIamPolicyRequestIn"])
    types["GetIamPolicyRequestOut"] = t.struct(
        {
            "options": t.proxy(renames["GetPolicyOptionsOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["GetIamPolicyRequestOut"])
    types["TestIamPermissionsResponseIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsResponseIn"])
    types["TestIamPermissionsResponseOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsResponseOut"])
    types["ListFoldersResponseIn"] = t.struct(
        {
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
            "nextPageToken": t.string().optional(),
        }
    ).named(renames["ListFoldersResponseIn"])
    types["ListFoldersResponseOut"] = t.struct(
        {
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "nextPageToken": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ListFoldersResponseOut"])
    types["TestIamPermissionsRequestIn"] = t.struct(
        {"permissions": t.array(t.string()).optional()}
    ).named(renames["TestIamPermissionsRequestIn"])
    types["TestIamPermissionsRequestOut"] = t.struct(
        {
            "permissions": t.array(t.string()).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TestIamPermissionsRequestOut"])
    types["FolderIn"] = t.struct(
        {"displayName": t.string().optional(), "parent": t.string()}
    ).named(renames["FolderIn"])
    types["FolderOut"] = t.struct(
        {
            "displayName": t.string().optional(),
            "etag": t.string().optional(),
            "deleteTime": t.string().optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "parent": t.string(),
            "state": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FolderOut"])
    types["SearchFoldersResponseIn"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderIn"])).optional(),
        }
    ).named(renames["SearchFoldersResponseIn"])
    types["SearchFoldersResponseOut"] = t.struct(
        {
            "nextPageToken": t.string().optional(),
            "folders": t.array(t.proxy(renames["FolderOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SearchFoldersResponseOut"])
    types["OperationIn"] = t.struct(
        {
            "error": t.proxy(renames["StatusIn"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationIn"])
    types["OperationOut"] = t.struct(
        {
            "error": t.proxy(renames["ErrorResponse"]).optional(),
            "response": t.struct({"_": t.string().optional()}).optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "name": t.string().optional(),
            "done": t.boolean().optional(),
        }
    ).named(renames["OperationOut"])
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
    types["UpdateFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateFolderMetadataIn"]
    )
    types["UpdateFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateFolderMetadataOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["MoveProjectRequestIn"] = t.struct({"destinationParent": t.string()}).named(
        renames["MoveProjectRequestIn"]
    )
    types["MoveProjectRequestOut"] = t.struct(
        {
            "destinationParent": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MoveProjectRequestOut"])
    types["CreateTagBindingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagBindingMetadataIn"]
    )
    types["CreateTagBindingMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagBindingMetadataOut"])
    types["ProjectIn"] = t.struct(
        {
            "projectId": t.string().optional(),
            "displayName": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parent": t.string().optional(),
        }
    ).named(renames["ProjectIn"])
    types["ProjectOut"] = t.struct(
        {
            "state": t.string().optional(),
            "etag": t.string().optional(),
            "createTime": t.string().optional(),
            "projectId": t.string().optional(),
            "displayName": t.string().optional(),
            "deleteTime": t.string().optional(),
            "labels": t.struct({"_": t.string().optional()}).optional(),
            "parent": t.string().optional(),
            "name": t.string().optional(),
            "updateTime": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ProjectOut"])
    types["PolicyIn"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingIn"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigIn"])).optional(),
            "version": t.integer().optional(),
        }
    ).named(renames["PolicyIn"])
    types["PolicyOut"] = t.struct(
        {
            "etag": t.string().optional(),
            "bindings": t.array(t.proxy(renames["BindingOut"])).optional(),
            "auditConfigs": t.array(t.proxy(renames["AuditConfigOut"])).optional(),
            "version": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PolicyOut"])
    types["UpdateTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UpdateTagKeyMetadataIn"]
    )
    types["UpdateTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UpdateTagKeyMetadataOut"])
    types["CreateProjectMetadataIn"] = t.struct(
        {
            "gettable": t.boolean().optional(),
            "createTime": t.string().optional(),
            "ready": t.boolean().optional(),
        }
    ).named(renames["CreateProjectMetadataIn"])
    types["CreateProjectMetadataOut"] = t.struct(
        {
            "gettable": t.boolean().optional(),
            "createTime": t.string().optional(),
            "ready": t.boolean().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["CreateProjectMetadataOut"])
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
    types[
        "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationIn"
    ] = t.struct(
        {
            "operationType": t.string().optional(),
            "sourceParent": t.string().optional(),
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
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
            "operationType": t.string().optional(),
            "sourceParent": t.string().optional(),
            "destinationParent": t.string().optional(),
            "displayName": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(
        renames[
            "CloudresourcemanagerGoogleCloudResourcemanagerV2alpha1FolderOperationOut"
        ]
    )
    types["UndeleteFolderRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteFolderRequestIn"]
    )
    types["UndeleteFolderRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteFolderRequestOut"])
    types["CreateTagKeyMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["CreateTagKeyMetadataIn"]
    )
    types["CreateTagKeyMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["CreateTagKeyMetadataOut"])
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
    types["UndeleteProjectRequestIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteProjectRequestIn"]
    )
    types["UndeleteProjectRequestOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteProjectRequestOut"])
    types["TagBindingIn"] = t.struct(
        {
            "tagValueNamespacedName": t.string().optional(),
            "parent": t.string().optional(),
            "tagValue": t.string().optional(),
        }
    ).named(renames["TagBindingIn"])
    types["TagBindingOut"] = t.struct(
        {
            "tagValueNamespacedName": t.string().optional(),
            "parent": t.string().optional(),
            "tagValue": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagBindingOut"])
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
    types["MoveProjectMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["MoveProjectMetadataIn"]
    )
    types["MoveProjectMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["MoveProjectMetadataOut"])
    types["DeleteTagBindingMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteTagBindingMetadataIn"]
    )
    types["DeleteTagBindingMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteTagBindingMetadataOut"])
    types["UndeleteOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["UndeleteOrganizationMetadataIn"])
    types["UndeleteOrganizationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteOrganizationMetadataOut"])
    types["TagHoldIn"] = t.struct(
        {
            "holder": t.string(),
            "helpLink": t.string().optional(),
            "origin": t.string().optional(),
        }
    ).named(renames["TagHoldIn"])
    types["TagHoldOut"] = t.struct(
        {
            "holder": t.string(),
            "helpLink": t.string().optional(),
            "createTime": t.string().optional(),
            "origin": t.string().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TagHoldOut"])
    types["UndeleteFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["UndeleteFolderMetadataIn"]
    )
    types["UndeleteFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["UndeleteFolderMetadataOut"])
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
    types["EffectiveTagIn"] = t.struct(
        {
            "tagKey": t.string().optional(),
            "tagValue": t.string().optional(),
            "inherited": t.boolean().optional(),
            "namespacedTagValue": t.string().optional(),
            "tagKeyParentName": t.string().optional(),
            "namespacedTagKey": t.string().optional(),
        }
    ).named(renames["EffectiveTagIn"])
    types["EffectiveTagOut"] = t.struct(
        {
            "tagKey": t.string().optional(),
            "tagValue": t.string().optional(),
            "inherited": t.boolean().optional(),
            "namespacedTagValue": t.string().optional(),
            "tagKeyParentName": t.string().optional(),
            "namespacedTagKey": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EffectiveTagOut"])
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
            "parent": t.string().optional(),
            "origin": t.string().optional(),
            "restrictions": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "reason": t.string().optional(),
        }
    ).named(renames["LienIn"])
    types["LienOut"] = t.struct(
        {
            "parent": t.string().optional(),
            "origin": t.string().optional(),
            "restrictions": t.array(t.string()).optional(),
            "createTime": t.string().optional(),
            "name": t.string().optional(),
            "reason": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LienOut"])
    types["DeleteFolderMetadataIn"] = t.struct({"_": t.string().optional()}).named(
        renames["DeleteFolderMetadataIn"]
    )
    types["DeleteFolderMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteFolderMetadataOut"])
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
    types["DeleteOrganizationMetadataIn"] = t.struct(
        {"_": t.string().optional()}
    ).named(renames["DeleteOrganizationMetadataIn"])
    types["DeleteOrganizationMetadataOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["DeleteOrganizationMetadataOut"])

    functions = {}
    functions["projectsList"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGet"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTestIamPermissions"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsCreate"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsUndelete"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSetIamPolicy"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsMove"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsGetIamPolicy"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsDelete"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsPatch"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsSearch"] = cloudresourcemanager.get(
        "v3/projects:search",
        t.struct(
            {
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchProjectsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagBindingsList"] = cloudresourcemanager.post(
        "v3/tagBindings",
        t.struct(
            {
                "validateOnly": t.boolean().optional(),
                "tagValueNamespacedName": t.string().optional(),
                "parent": t.string().optional(),
                "tagValue": t.string().optional(),
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
                "tagValueNamespacedName": t.string().optional(),
                "parent": t.string().optional(),
                "tagValue": t.string().optional(),
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
                "tagValueNamespacedName": t.string().optional(),
                "parent": t.string().optional(),
                "tagValue": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensList"] = cloudresourcemanager.post(
        "v3/liens",
        t.struct(
            {
                "parent": t.string().optional(),
                "origin": t.string().optional(),
                "restrictions": t.array(t.string()).optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LienOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensGet"] = cloudresourcemanager.post(
        "v3/liens",
        t.struct(
            {
                "parent": t.string().optional(),
                "origin": t.string().optional(),
                "restrictions": t.array(t.string()).optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LienOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensDelete"] = cloudresourcemanager.post(
        "v3/liens",
        t.struct(
            {
                "parent": t.string().optional(),
                "origin": t.string().optional(),
                "restrictions": t.array(t.string()).optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LienOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["liensCreate"] = cloudresourcemanager.post(
        "v3/liens",
        t.struct(
            {
                "parent": t.string().optional(),
                "origin": t.string().optional(),
                "restrictions": t.array(t.string()).optional(),
                "createTime": t.string().optional(),
                "name": t.string().optional(),
                "reason": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["LienOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["foldersSearch"] = cloudresourcemanager.post(
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
    functions["foldersGet"] = cloudresourcemanager.post(
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
    functions["foldersList"] = cloudresourcemanager.post(
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
    functions["foldersDelete"] = cloudresourcemanager.post(
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
    functions["foldersCreate"] = cloudresourcemanager.post(
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
    functions["foldersUndelete"] = cloudresourcemanager.post(
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
    functions["foldersMove"] = cloudresourcemanager.post(
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
    functions["foldersPatch"] = cloudresourcemanager.post(
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
    functions["foldersGetIamPolicy"] = cloudresourcemanager.post(
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
    functions["foldersTestIamPermissions"] = cloudresourcemanager.post(
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
    functions["foldersSetIamPolicy"] = cloudresourcemanager.post(
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
    functions["tagValuesTestIamPermissions"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesDelete"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesSetIamPolicy"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesPatch"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesGetNamespaced"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesGetIamPolicy"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesCreate"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesList"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string(), "auth": t.string().optional()}),
        t.proxy(renames["TagValueOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagValuesGet"] = cloudresourcemanager.get(
        "v3/{name}",
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
    functions["operationsGet"] = cloudresourcemanager.get(
        "v3/{name}",
        t.struct({"name": t.string().optional(), "auth": t.string().optional()}),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGetIamPolicy"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysPatch"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysTestIamPermissions"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGetNamespaced"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysSetIamPolicy"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysCreate"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysGet"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysList"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["tagKeysDelete"] = cloudresourcemanager.delete(
        "v3/{name}",
        t.struct(
            {
                "name": t.string(),
                "validateOnly": t.boolean().optional(),
                "etag": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["OperationOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsGetIamPolicy"] = cloudresourcemanager.get(
        "v3/organizations:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOrganizationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["organizationsSetIamPolicy"] = cloudresourcemanager.get(
        "v3/organizations:search",
        t.struct(
            {
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
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
                "pageToken": t.string().optional(),
                "pageSize": t.integer().optional(),
                "query": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SearchOrganizationsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["effectiveTagsList"] = cloudresourcemanager.get(
        "v3/effectiveTags",
        t.struct(
            {
                "parent": t.string(),
                "pageSize": t.integer().optional(),
                "pageToken": t.string().optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ListEffectiveTagsResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudresourcemanager",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
